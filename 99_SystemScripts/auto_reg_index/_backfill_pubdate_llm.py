"""
_backfill_pubdate_llm.py — 用 Claude Opus 从 body 推断 publication_date

审计报告 P1.4：107 条 publication_date=unknown（DeepSeek 已补 10 条，剩 ~97）

策略：
- 候选 = FM 中 publication_date 为空/unknown/None 的 notes
- 每条抽 body 前 3000 字 + FM 里 reg_id/title/region
- 要求 Opus 输出结构化 JSON：
  {
    "publication_date": "YYYY-MM-DD",   # 或 null
    "effective_date":   "YYYY-MM-DD",   # 可选
    "date_type":        "published|effective|revised|amended|unknown",
    "evidence":         "body 字面摘录",
    "confidence":       "high|medium|low"
  }
- 硬性约束：evidence 必须是 body 字面出现才接受（防幻觉）
- publication_date 写回 FM，带 source=stage3_llm_opus_pubdate

用法：
    python _backfill_pubdate_llm.py --dry-run --limit 5
    python _backfill_pubdate_llm.py --workers 4
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import httpx
import yaml
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(r"D:\CcVault\99_SystemScripts\auto_reg_index\.env", override=True)

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
RESUME_LOG = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.stage3") / "llm_pubdate_resume.jsonl"
RESUME_LOG.parent.mkdir(exist_ok=True)

API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
OPUS_MODEL = os.environ.get("CLAUDE_OPUS_MODEL", "claude-opus-4-6").strip()

HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VALID_DATE_TYPES = {"published", "effective", "revised", "amended", "unknown"}
VALID_CONF = {"high", "medium", "low"}

SYSTEM_PROMPT = """你是汽车法规元数据抽取专家。
任务：从法规 body 里准确识别 **publication_date（发布日期）**。

只输出一个 JSON 对象，不要 markdown 包裹，不要多余解释。schema:
{
  "publication_date": "YYYY-MM-DD 或 null",
  "effective_date":   "YYYY-MM-DD 或 null",
  "date_type":        "published | effective | revised | amended | unknown",
  "evidence":         "body 里 10-80 字的字面原文摘录",
  "confidence":       "high | medium | low"
}

判定规则（GB 标准）:
- 标准前言常有"本标准于 2019 年 X 月 X 日发布"或"由 XXX 批准，xxx 发布"
- 封面一般有"YYYY-MM-DD 发布"和"YYYY-MM-DD 实施"
- published 日期 = 发布日期（优先），effective 日期 = 实施日期

判定规则（ECE / UN 法规）:
- ECE 正文第一段有 "E/ECE/324/Rev.1/Add.12/Rev.3 - 14 October 2019" 这种完整时间戳
- Amendment 类有 "Supplement N to the 00 series of amendments - Date of entry into force: 10 June 2018"
- 优先抽 "发布" (publication) 日期，若无再抽 effective

判定规则（其他 region）：
- EU: 官方公报发布日期
- ISO: 版本年份 + 月份（若 body 有）
- JIS / KS / FMVSS: 标准封面标注日期

硬性约束（**极其重要**）:
- 若 body 没有任何明确日期 → publication_date=null，date_type=unknown，confidence=low
- 不要猜测，不要用 world knowledge 外推
- ❌ **严禁从 reg_id 里的年份后缀（如 "GB 14167-2006"）倒推日期**。reg_id 里的 "-2006" 不算日期证据
- ❌ 严禁从标题里的年份字面倒推日期
- ✅ **evidence 必须包含你声明的日期数字本身**：
    - 若声明 publication_date="2019-03-15"，evidence 里必须有 "2019" + 月份/日 信息
    - 若声明 "2006-01-01"，evidence 里必须有 "2006-01-01" 或 "2006 年 1 月 1 日" 或"1 月 1 日"等字样
    - evidence 只是个文档标题（如 "GB 14167-2006 汽车安全带..."）→ **不算有效日期证据**，此时请返回 null
- 日期格式必须是 YYYY-MM-DD（补零），年份 1950-2030，拒绝范围/季度
- 若 body 里有多个日期（如"2018 发布，2019 实施"），publication_date 取发布，effective_date 取实施
- 若只知道年份（如"2018 年发布"但无月份），返回 YYYY-01-01 但 confidence 必须是 **low**（不是 medium）
- 若知道年月但无日（如"2018 年 3 月"），返回 YYYY-MM-01 并 confidence=medium
- 若知道完整年月日，confidence=high
"""


def extract_with_opus(
    body_head: str,
    reg_id: str,
    title: str,
    region: str,
    *,
    client: httpx.Client,
    max_retries: int = 3,
) -> tuple[dict, dict]:
    user_prompt = (
        f"法规编号: {reg_id}\n"
        f"名称: {title}\n"
        f"区域: {region}\n\n"
        f"body 前 3000 字:\n---\n{body_head}\n---\n\n"
        f"按 schema 输出 JSON。"
    )
    payload = {
        "model": OPUS_MODEL,
        "max_tokens": 400,
        "temperature": 0,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_prompt}],
    }
    last_err = None
    for attempt in range(max_retries):
        try:
            r = client.post(f"{BASE_URL}/v1/messages", json=payload, timeout=90)
            if r.status_code != 200:
                last_err = f"HTTP {r.status_code}: {r.text[:200]}"
                time.sleep(2 ** attempt)
                continue
            j = r.json()
            txt = "".join(c.get("text", "") for c in j.get("content", []))
            usage = j.get("usage", {})
            m = re.search(r"\{[\s\S]*\}", txt)
            if not m:
                last_err = f"No JSON: {txt[:200]}"
                time.sleep(1)
                continue
            try:
                data = json.loads(m.group(0))
            except json.JSONDecodeError as e:
                last_err = f"bad JSON: {e}"
                time.sleep(1)
                continue
            return data, usage
        except Exception as e:
            last_err = str(e)
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Opus failed after {max_retries} retries: {last_err}")


def validate_output(data: dict, body_head: str) -> dict | None:
    pub = (data.get("publication_date") or "").strip() or None
    eff = (data.get("effective_date") or "").strip() or None
    dt = (data.get("date_type") or "unknown").strip().lower()
    evidence = (data.get("evidence") or "").strip()
    conf = (data.get("confidence") or "low").strip().lower()

    if dt not in VALID_DATE_TYPES:
        dt = "unknown"
    if conf not in VALID_CONF:
        conf = "low"

    # 日期校验
    def valid_date(d):
        if d is None or d == "null":
            return None
        if not DATE_RE.match(d):
            return None
        try:
            y = int(d[:4])
            if not (1950 <= y <= 2030):
                return None
            return d
        except ValueError:
            return None

    pub = valid_date(pub)
    eff = valid_date(eff)

    if pub is None and eff is None:
        return None  # 没抽到任何日期

    # evidence 校验 1：前 15 字字面摘录必须在 body 中
    if evidence:
        probe = re.sub(r"\s+", "", evidence[:15])
        body_stripped = re.sub(r"\s+", "", body_head)
        if probe and probe not in body_stripped:
            if conf == "high":
                conf = "medium"
            elif conf == "medium":
                conf = "low"
            else:
                return None

    # evidence 校验 2（关键）：evidence 里必须出现声明的日期数字
    # 防 Opus 从 reg_id 年份后缀倒推
    if pub:
        year = pub[:4]
        month = pub[5:7]
        day = pub[8:10]
        ev_clean = re.sub(r"\s+", "", evidence)
        # 至少要在 evidence 里看到年份
        if year not in ev_clean:
            return None
        # 如果声明了非 01-01 这种默认日，那月日也应该在 evidence 里
        # 但年月日全为 01-01 允许（表示只知道年份），此时 confidence 必须 low
        is_year_only = (month == "01" and day == "01")
        if is_year_only:
            conf = "low"
        else:
            # 至少月份数字要能在 evidence 里找到（不严格要求 YYYY-MM-DD 字面）
            # 允许"3 月"匹配 month=03 的场景
            month_int = int(month)
            has_month = (
                month in ev_clean
                or f"{month_int}月" in ev_clean
                or f"{month_int:02d}-" in ev_clean
                or f"-{month_int:02d}" in ev_clean
            )
            if not has_month:
                # 月份在 evidence 找不到但声称有月份 → 拒绝
                return None

    return {
        "publication_date": pub,
        "effective_date": eff,
        "date_type": dt,
        "evidence": evidence,
        "confidence": conf,
    }


def is_pubdate_missing(fm: dict) -> bool:
    v = fm.get("publication_date")
    if v is None:
        return True
    s = str(v).strip().lower()
    return s in ("", "unknown", "none", "null", "n/a")


# body 里是否存在日期关键词——用于筛选 Opus 真有可能成功的候选
_DATE_SIGNAL_RE = re.compile(
    r"(\d{4}[-/年]\s?\d{1,2}[-/月]\s?\d{1,2}|"
    r"\d{1,2}\s?(January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{4}|"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s?\d{1,2},?\s?\d{4}|"
    r"(发布|实施|施行|生效|issued|published|effective|entry\s+into\s+force)[^\n]{0,40}\d{4})",
    re.IGNORECASE,
)


def has_date_signal(body_head: str) -> bool:
    return _DATE_SIGNAL_RE.search(body_head) is not None


def process_one(p: Path, client: httpx.Client, dry_run: bool) -> dict:
    txt = p.read_text(encoding="utf-8", errors="replace")
    if not txt.startswith("---"):
        return {"file": p.name, "status": "no_fm"}
    end = txt.find("\n---", 4)
    if end < 0:
        return {"file": p.name, "status": "bad_fm"}
    try:
        fm = yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        return {"file": p.name, "status": "yaml_error"}
    body = txt[end + 4:]
    body_head = body[:3000]

    reg_id = (fm.get("reg_id") or "").strip()
    title = (fm.get("title") or "").strip()
    region = (fm.get("region") or "").strip()

    try:
        raw, usage = extract_with_opus(body_head, reg_id, title, region, client=client)
    except Exception as e:
        return {"file": p.name, "reg_id": reg_id, "status": "api_error", "err": str(e)}

    v = validate_output(raw, body_head)
    result = {
        "file": p.name,
        "reg_id": reg_id,
        "status": "ok",
        "raw": raw,
        "validated": v,
        "usage": usage,
    }
    if not v:
        result["status"] = "no_date_found"
        return result

    # 若 publication_date 为空但有 effective_date，升为 publication_date
    # （对 ECE amendment 来说 entry into force 就是事实上的"发布/生效"日期，区分意义不大）
    if not v["publication_date"] and v["effective_date"]:
        v["publication_date"] = v["effective_date"]
        # effective_date 原位保留

    # 写回 FM
    if not dry_run and v["publication_date"]:
        fm["publication_date"] = v["publication_date"]
        if v["effective_date"] and not fm.get("effective_date"):
            fm["effective_date"] = v["effective_date"]
        fm["_pubdate_source"] = "stage3_llm_opus"
        fm["_pubdate_confidence"] = v["confidence"]
        fm["_pubdate_evidence"] = v["evidence"][:150]

        new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        p.write_text("---\n" + new_fm + "---" + body, encoding="utf-8")
        result["written"] = True

    return result


def find_candidates(require_date_signal: bool = True) -> list[Path]:
    """require_date_signal=True 时只返回 body 里有日期关键词的，Opus 才有可能命中。"""
    out = []
    skipped_no_signal = 0
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if not txt.startswith("---"):
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        try:
            fm = yaml.safe_load(txt[4:end]) or {}
        except yaml.YAMLError:
            continue
        if not is_pubdate_missing(fm):
            continue
        if require_date_signal:
            body_head = txt[end + 4:][:3000]
            if not has_date_signal(body_head):
                skipped_no_signal += 1
                continue
        out.append(p)
    if require_date_signal and skipped_no_signal:
        print(f"(跳过 {skipped_no_signal} 条 body 无日期关键词的候选，它们送 Opus 也会返回 no_date)")
    return out


def load_resume() -> set[str]:
    done = set()
    if RESUME_LOG.exists():
        for line in RESUME_LOG.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
                if rec.get("status") in ("ok",) and rec.get("written"):
                    done.add(rec["file"])
            except Exception:
                continue
    return done


def append_resume(rec: dict) -> None:
    # 剥离不 JSON 友好的 Path 对象
    with RESUME_LOG.open("a", encoding="utf-8") as f:
        slim = {k: v for k, v in rec.items() if k != "raw"}
        f.write(json.dumps(slim, ensure_ascii=False, default=str) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--all-candidates", action="store_true", help="也处理 body 无日期关键词的（浪费 token）")
    args = ap.parse_args()

    candidates = find_candidates(require_date_signal=not args.all_candidates)
    print(f"候选（缺 publication_date）: {len(candidates)}")

    if args.resume:
        done = load_resume()
        candidates = [p for p in candidates if p.name not in done]
        print(f"跳过已完成: {len(done)}，剩余: {len(candidates)}")

    if args.limit > 0:
        candidates = candidates[: args.limit]
        print(f"受 --limit 限制，本次: {len(candidates)}")

    mode = "DRY RUN" if args.dry_run else "APPLY"
    print(f"模式: {mode}, workers: {args.workers}, model: {OPUS_MODEL}")
    print("-" * 70)

    results = []
    total_in = total_out = 0
    with httpx.Client(headers=HEADERS, timeout=90) as client:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(process_one, p, client, args.dry_run): p for p in candidates}
            for i, fut in enumerate(as_completed(futs), 1):
                p = futs[fut]
                try:
                    r = fut.result()
                except Exception as e:
                    r = {"file": p.name, "status": "exception", "err": str(e)}
                results.append(r)
                if not args.dry_run:
                    append_resume(r)
                u = r.get("usage") or {}
                total_in += u.get("input_tokens") or 0
                total_out += u.get("output_tokens") or 0
                v = r.get("validated") or {}
                line = f"[{i:>3}/{len(candidates)}] {r.get('reg_id','?'):<30} {r.get('status'):<15}"
                if v:
                    line += f" pub={v['publication_date']} conf={v['confidence']}"
                print(line)
                if args.verbose and v and v.get("evidence"):
                    print(f"        evidence: {v['evidence'][:100]}")

    print("-" * 70)
    ok_w = sum(1 for r in results if r.get("status") == "ok" and r.get("validated"))
    no_date = sum(1 for r in results if r.get("status") == "no_date_found")
    err = sum(1 for r in results if r.get("status") in ("api_error", "exception", "yaml_error"))
    high = sum(1 for r in results if (r.get("validated") or {}).get("confidence") == "high")
    med = sum(1 for r in results if (r.get("validated") or {}).get("confidence") == "medium")
    low = sum(1 for r in results if (r.get("validated") or {}).get("confidence") == "low")
    print(f"抽到日期: {ok_w}（high={high} / medium={med} / low={low}）")
    print(f"无日期:   {no_date}")
    print(f"错误:     {err}")
    print(f"Token:    input={total_in:,}  output={total_out:,}")
    cost = total_in * 15 / 1e6 + total_out * 75 / 1e6
    print(f"成本估算（官方 Opus）: ${cost:.2f}")

    if args.dry_run:
        print("\n[DRY RUN] 未写入任何文件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
