"""
_recheck_low_conf_opus.py — Claude Opus 复审低置信度 notes

审计报告 P1.3：
- 原 79 条 low confidence → DeepSeek Phase 2b 跑过一轮 → 75 条（升级 4）
- 现在 Opus 复审，目标是再升级一批，同时修正关键字段

策略：
- 候选 = cross_check_overall_confidence=low 且 body>=1500 字符（≈47 条）
  （body<1500 的 28 条是 OCR floor，Opus 帮不上）
- 每条发 Opus：FM 关键字段 + body 前 4000 字
- Opus 重新评估：应得的 confidence、哪些字段需更正
- 字段更正必须带 evidence（body 字面摘录）

输出字段：
  {
    "new_confidence": "high | medium | low",
    "reason": "<100字说明>",
    "corrections": {                    # 只写需改的字段
      "title": {"new": "...", "evidence": "..."},
      "status": {"new": "...", "evidence": "..."},
      "publication_date": {"new": "YYYY-MM-DD", "evidence": "..."}
    },
    "verdict": "upgrade | keep | data_floor"
  }

evidence 防幻觉校验：每个 correction 的 evidence 必须在 body 字面出现。
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
RESUME_LOG = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.stage3") / "llm_recheck_resume.jsonl"
RESUME_LOG.parent.mkdir(exist_ok=True)

API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
OPUS_MODEL = os.environ.get("CLAUDE_OPUS_MODEL", "claude-opus-4-6").strip()

HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

VALID_CONF = {"high", "medium", "low"}
VALID_VERDICT = {"upgrade", "keep", "data_floor"}
# 可修正的字段白名单（防 Opus 乱改）
EDITABLE = {"title", "status", "publication_date", "scope", "version",
            "standard_body", "region", "type"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

SYSTEM_PROMPT = """你是汽车法规数据质量复审专家。
用户给你一个 note 的元数据（FM）+ body 前 4000 字。该 note 当前 `cross_check_overall_confidence=low`。
你的任务：基于 body 实际内容，判断是否应该升级 confidence，并修正明显错误/缺失的字段。

⭐ 决策 3 选 1:
- **upgrade**: body 证据充分，数据质量没那么差，应升级到 medium 或 high
- **keep**: 低置信度确实合理，但 body 里有少量可修正项
- **data_floor**: body 内容本就稀薄（如短修订文本），无法改善，接受现状

⭐ 可修正字段（白名单）:
title, status, publication_date, scope, version, standard_body, region, type

⭐ 评估 confidence 标准:
- **high**: body 内容完整覆盖法规核心条款，标题/日期/版本清晰可证
- **medium**: body 覆盖大部分信息但细节缺失，或标题/日期有 1 处不确定
- **low**: body 不完整或结构混乱，关键字段多处不确定

⭐ 硬性要求（防幻觉）:
- 每个 correction 必须带 evidence：body 里 10-80 字的字面原文摘录
- evidence 不允许改写、压缩、合并
- 若 body 里没有支持该字段的证据 → 不要 correct 该字段
- status 只能是 active / superseded / withdrawn / draft / pending / unknown
- publication_date 只接受 YYYY-MM-DD，年份 1950-2030
- 拒绝从 reg_id 里的年份后缀（如 GB 14167-2006）倒推 publication_date

⭐ 输出格式（只输出 JSON，不要 markdown）:
{
  "verdict": "<upgrade | keep | data_floor>",
  "new_confidence": "<high | medium | low>",
  "reason": "<50-120 字判定理由>",
  "corrections": {
    "title": {"new": "...", "evidence": "..."},        // 仅需更正的字段才写
    "status": {"new": "active", "evidence": "..."},
    "publication_date": {"new": "2020-03-15", "evidence": "2020年3月15日发布"}
  }
}
- 若没有任何字段要改，corrections 写 {}
- 不要输出白名单之外的字段
"""


def call_opus(
    note_path: Path,
    fm: dict,
    body_head: str,
    *,
    client: httpx.Client,
    max_retries: int = 3,
) -> tuple[dict, dict]:
    # 送给 Opus 的 FM 精简版
    show_keys = ["reg_id", "title", "region", "type", "status", "publication_date",
                 "version", "standard_body", "scope",
                 "cross_check_overall_confidence"]
    fm_show = {k: fm.get(k) for k in show_keys if fm.get(k) is not None}
    flags = fm.get("cross_check_flags") or []
    flags_show = [f"{fl.get('field', '?')}: {fl.get('note', '')[:80]}"
                  for fl in flags[:6]]

    user = (
        f"note 文件: {note_path.name}\n\n"
        f"FM 关键字段:\n{yaml.safe_dump(fm_show, allow_unicode=True, sort_keys=False)}\n"
        f"现有 cross_check_flags (前6条):\n" + "\n".join(f"  - {x}" for x in flags_show) + "\n\n"
        f"body 前 4000 字:\n---\n{body_head}\n---\n\n"
        f"请按 schema 评估并输出 JSON。"
    )
    payload = {
        "model": OPUS_MODEL,
        "max_tokens": 900,
        "temperature": 0,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user}],
    }
    last_err = None
    for attempt in range(max_retries):
        try:
            r = client.post(f"{BASE_URL}/v1/messages", json=payload, timeout=120)
            if r.status_code != 200:
                last_err = f"HTTP {r.status_code}: {r.text[:200]}"
                time.sleep(2 ** attempt)
                continue
            j = r.json()
            txt = "".join(c.get("text", "") for c in j.get("content", []))
            usage = j.get("usage", {})
            m = re.search(r"\{[\s\S]*\}", txt)
            if not m:
                last_err = "no JSON"
                continue
            raw_json = m.group(0)
            try:
                data = json.loads(raw_json)
            except json.JSONDecodeError:
                # 尝试修复 evidence 字段中未转义的引号：把 "evidence": "...containing "quotes"..." 里的内部引号替换
                # 简单策略：替换中文引号，并放宽为只提取 verdict/new_confidence/reason
                # 若仍失败，返回一个最小可用对象
                try:
                    fixed = re.sub(r'([""''])', '"', raw_json)
                    data = json.loads(fixed)
                except json.JSONDecodeError:
                    # 最后回退：只提取 verdict / new_confidence / reason
                    verdict_m = re.search(r'"verdict"\s*:\s*"([^"]+)"', raw_json)
                    conf_m = re.search(r'"new_confidence"\s*:\s*"([^"]+)"', raw_json)
                    reason_m = re.search(r'"reason"\s*:\s*"([^"]*?)"\s*[,}]', raw_json)
                    if verdict_m and conf_m:
                        data = {
                            "verdict": verdict_m.group(1),
                            "new_confidence": conf_m.group(1),
                            "reason": (reason_m.group(1) if reason_m else "") + "（JSON 部分解析失败，corrections 已丢弃）",
                            "corrections": {},
                        }
                    else:
                        last_err = "json decode + fallback failed"
                        continue
            return data, usage
        except Exception as e:
            last_err = str(e)
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Opus failed: {last_err}")


def validate(data: dict, body_head: str) -> dict | None:
    verdict = (data.get("verdict") or "").strip().lower()
    new_conf = (data.get("new_confidence") or "").strip().lower()
    reason = (data.get("reason") or "").strip()
    corr_raw = data.get("corrections") or {}

    if verdict not in VALID_VERDICT:
        return None
    if new_conf not in VALID_CONF:
        return None

    # 校验每个 correction 的 evidence
    body_clean = re.sub(r"\s+", "", body_head)
    clean_corr = {}
    for field, v in corr_raw.items():
        if field not in EDITABLE:
            continue
        if not isinstance(v, dict):
            continue
        new_val = v.get("new")
        ev = (v.get("evidence") or "").strip()
        if not ev or len(ev) < 8:
            continue
        probe = re.sub(r"\s+", "", ev[:20])
        if probe not in body_clean:
            # evidence 不是字面摘录 → 丢弃
            continue
        # 特殊字段校验
        if field == "publication_date":
            if not (isinstance(new_val, str) and DATE_RE.match(new_val)):
                continue
            year = new_val[:4]
            if year not in re.sub(r"\s+", "", ev):
                # evidence 里没出现年份数字 → 拒绝
                continue
            try:
                yi = int(year)
                if not (1950 <= yi <= 2030):
                    continue
            except ValueError:
                continue
        elif field == "status":
            if new_val not in ("active", "superseded", "withdrawn", "draft", "pending", "unknown"):
                continue
        elif field in ("title", "scope") and isinstance(new_val, str):
            if len(new_val) < 3 or len(new_val) > 500:
                continue
        clean_corr[field] = {"new": new_val, "evidence": ev}

    return {
        "verdict": verdict,
        "new_confidence": new_conf,
        "reason": reason,
        "corrections": clean_corr,
    }


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
    body_head = body[:4000]

    try:
        raw, usage = call_opus(p, fm, body_head, client=client)
    except Exception as e:
        return {"file": p.name, "reg_id": fm.get("reg_id"), "status": "api_error", "err": str(e)}

    v = validate(raw, body_head)
    result = {
        "file": p.name,
        "reg_id": fm.get("reg_id"),
        "status": "ok",
        "raw": raw,
        "validated": v,
        "usage": usage,
    }
    if not v:
        result["status"] = "bad_output"
        return result

    # 写回决策
    did_write = False
    if not dry_run:
        changes = {}
        # 1. confidence 升级
        if v["verdict"] == "upgrade" and v["new_confidence"] != "low":
            changes["cross_check_overall_confidence"] = v["new_confidence"]
        # 2. 字段修正
        for field, c in v["corrections"].items():
            new_val = c["new"]
            if fm.get(field) != new_val:
                changes[field] = new_val
        if changes:
            for k, val in changes.items():
                fm[k] = val
            # 标记来源
            fm["_low_conf_recheck_source"] = "stage3_llm_opus"
            fm["_low_conf_recheck_verdict"] = v["verdict"]
            fm["_low_conf_recheck_reason"] = v["reason"][:200]
            new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
            p.write_text("---\n" + new_fm + "---" + body, encoding="utf-8")
            did_write = True
            result["changed_fields"] = list(changes.keys())
    result["did_write"] = did_write
    return result


def find_candidates(min_body: int = 1500) -> list[Path]:
    out = []
    skipped_short = 0
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
        if (fm.get("cross_check_overall_confidence") or "").lower() != "low":
            continue
        body_len = len(txt) - end - 4
        if body_len < min_body:
            skipped_short += 1
            continue
        out.append(p)
    print(f"(跳过 {skipped_short} 条 body<{min_body} 的 data-floor 候选)")
    return out


def load_resume() -> set[str]:
    done = set()
    if RESUME_LOG.exists():
        for line in RESUME_LOG.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
                if rec.get("status") == "ok":
                    done.add(rec["file"])
            except Exception:
                continue
    return done


def append_resume(rec: dict) -> None:
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
    ap.add_argument("--min-body", type=int, default=1500)
    args = ap.parse_args()

    candidates = find_candidates(min_body=args.min_body)
    print(f"候选（low conf + body>={args.min_body}）: {len(candidates)}")

    if args.resume:
        done = load_resume()
        candidates = [p for p in candidates if p.name not in done]
        print(f"resume 跳过: {len(done)}, 剩余: {len(candidates)}")

    if args.limit > 0:
        candidates = candidates[: args.limit]

    mode = "DRY RUN" if args.dry_run else "APPLY"
    print(f"模式: {mode}, workers: {args.workers}, model: {OPUS_MODEL}")
    print("-" * 70)

    results = []
    total_in = total_out = 0
    with httpx.Client(headers=HEADERS, timeout=120) as client:
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
                changed = r.get("changed_fields") or []
                verdict = v.get("verdict") or "?"
                new_conf = v.get("new_confidence") or "?"
                line = (f"[{i:>3}/{len(candidates)}] {r.get('reg_id','?'):<28}"
                        f" {r.get('status'):<11} verdict={verdict:<10} new={new_conf:<7}"
                        f" fields={','.join(changed) if changed else '-'}")
                print(line)
                if args.verbose and v and v.get("reason"):
                    print(f"    reason: {v['reason'][:150]}")

    print("-" * 70)
    upgrades = sum(1 for r in results if (r.get("validated") or {}).get("verdict") == "upgrade")
    kept = sum(1 for r in results if (r.get("validated") or {}).get("verdict") == "keep")
    floor = sum(1 for r in results if (r.get("validated") or {}).get("verdict") == "data_floor")
    wrote = sum(1 for r in results if r.get("did_write"))
    err = sum(1 for r in results if r.get("status") not in ("ok",))
    print(f"upgrade: {upgrades}   keep: {kept}   data_floor: {floor}   err: {err}")
    print(f"字段写入: {wrote} 条")
    print(f"Token: in={total_in:,} out={total_out:,}")
    cost = total_in * 15 / 1e6 + total_out * 75 / 1e6
    print(f"成本: ${cost:.2f}")
    if args.dry_run:
        print("\n[DRY RUN] 未写入任何文件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
