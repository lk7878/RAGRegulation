"""
_expand_equivalence_llm.py — 用 Claude Opus 补抽 GB 法规的 equivalent_to 关系

定位：P1.2 等价映射 rule-based 之后的 LLM fallback
- 只跑"强候选"：CN region + 无 equivalent_to + body 含外标线索
- 每条 note 把 body 前 3000 字 + reg_id + title 塞给 Opus
- 要求结构化 JSON 输出，每条关系必须附带 body evidence snippet
- evidence 必须在 body 内真实出现才接受（防 Opus 幻觉）
- 写入 FM 时 source 标 `stage3_llm_opus` 区分
- 支持 --dry-run / --resume

用法:
    python _expand_equivalence_llm.py --dry-run --limit 3        # 先 3 条看效果
    python _expand_equivalence_llm.py --dry-run                  # 全 dry-run 看所有结果
    python _expand_equivalence_llm.py                             # 真写回
    python _expand_equivalence_llm.py --workers 4                 # 4 路并发
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
RESUME_LOG = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.stage3") / "llm_equiv_resume.jsonl"
RESUME_LOG.parent.mkdir(exist_ok=True)

API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
OPUS_MODEL = os.environ.get("CLAUDE_OPUS_MODEL", "claude-opus-4-6").strip()

HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

VALID_RELATIONS = {"identical", "modified", "non_equivalent", "reference"}

FOREIGN_REF_RE = re.compile(
    r"(ECE\s*R\s*\d+|UN\s*R\s*\d+|ISO\s*\d+|EU\s*\d+|FMVSS\s*\d+|JIS\s*\w+|"
    r"UNECE|联合国|欧洲经济委员会|国际标准化组织|美国联邦机动车)",
    re.IGNORECASE,
)
CITE_KEYWORDS_RE = re.compile(
    r"(等效采用|修改采用|非等效采用|等同采用|参照|采用|对应|对标|based on|equivalent to|modified from)"
)

# canonicalize 工具（与 rule-based 保持一致）
ECE_RE = re.compile(
    r"\b(?:UN(?:ECE)?|ECE)[-\s]?R\s?(\d{1,4})([Hh])?"
    r"(?:\s*(?:Rev|版本|修订)\s*(\d+))?"
    r"(?:\s*(?:Am|修改单)\s*(\d+))?",
    re.IGNORECASE,
)
ISO_RE = re.compile(r"\bISO\s?(\d{2,6})(?:[-:](\d{2,4}))?", re.IGNORECASE)
EU_RE = re.compile(r"\b(?:Regulation\s+)?\(?EU\)?\s+(\d{4}[-/\s]\d{1,4})", re.IGNORECASE)


def canonicalize_ref(raw: str) -> str | None:
    """把 LLM 返回的 ref 字符串归一化到 FM 标准形态，失败返回 None。"""
    if not raw:
        return None
    raw = raw.strip()
    m = ECE_RE.search(raw)
    if m:
        num, h, rev, am = m.groups()
        h = h.upper() if h else ""
        parts = [f"ECE R{int(num)}{h}"]
        if rev:
            parts.append(f"Rev{int(rev)}")
        if am:
            parts.append(f"Am{int(am)}")
        return " ".join(parts)
    m = ISO_RE.search(raw)
    if m:
        num, year = m.groups()
        return f"ISO {num}:{year}" if year else f"ISO {num}"
    m = EU_RE.search(raw)
    if m:
        payload = m.group(1).replace(" ", "/").replace("-", "/")
        return f"(EU) {payload}"
    return None


def parse_existing_equivs(fm: dict) -> set[str]:
    equivs = fm.get("equivalent_to") or []
    if not isinstance(equivs, list):
        return set()
    refs = set()
    for item in equivs:
        if isinstance(item, dict):
            r = item.get("ref") or item.get("reg_id")
            if r:
                refs.add(str(r).strip())
        elif isinstance(item, str):
            m = re.search(r"\[\[([^\]|]+)", item)
            refs.add(m.group(1).strip() if m else item.strip())
    return refs


SYSTEM_PROMPT = """你是汽车法规等价关系抽取专家。
根据中国 GB 标准的【前言/引言】，识别它与外国标准（ECE/UN/ISO/EU 法规等）的等价关系。

只输出一个 JSON 对象，不要 markdown，不要解释。schema:
{
  "relations": [
    {
      "ref": "<外国法规编号，如 'ECE R13' / 'ISO 15008' / '(EU) 2018/858'>",
      "relation": "<四选一: identical|modified|non_equivalent|reference>",
      "evidence": "<body 里 20-80 字的原文句子片段，必须是字面摘录，不允许改写>"
    }
  ]
}

relation 判定规则:
- identical: 原文出现"等同采用/等效采用"或 identical adoption
- modified: 原文出现"修改采用"或 modified adoption/based on but with modifications
- non_equivalent: 原文明确说"非等效采用/非等同采用"
- reference: 原文出现"参照/参考/借鉴" 或 based on（未说明修改程度）

硬性约束:
- 若 body 没有明确采标声明，返回 {"relations": []}
- 不要猜测未出现的关系
- evidence 必须是 body 的字面原文摘录，若改写则本条丢弃
- ref 要写成规范化形态：ECE R<N>（带 H/Rev/Am 后缀按原文保留），ISO <N>[:年] ，(EU) <年份/编号>
- 同一个外标只返回一次，relation 取置信度最高的（identical > modified > non_equivalent > reference）
"""


def extract_with_opus(
    body_head: str,
    reg_id: str,
    title: str,
    *,
    client: httpx.Client,
    max_retries: int = 3,
) -> tuple[list[dict], dict]:
    """调 Opus 抽取，返回 (relations, usage)。失败抛异常。"""
    user_prompt = (
        f"GB 标准编号: {reg_id}\n"
        f"标准名称: {title}\n\n"
        f"body 前言部分（前 3000 字）:\n---\n{body_head}\n---\n\n"
        f"请按 schema 输出 JSON。"
    )
    payload = {
        "model": OPUS_MODEL,
        "max_tokens": 800,
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
            # 抽 JSON
            m = re.search(r"\{[\s\S]*\}", txt)
            if not m:
                last_err = f"No JSON in response: {txt[:200]}"
                time.sleep(1)
                continue
            data = json.loads(m.group(0))
            relations = data.get("relations") or []
            if not isinstance(relations, list):
                relations = []
            return relations, usage
        except Exception as e:
            last_err = str(e)
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Opus call failed after {max_retries} retries: {last_err}")


def validate_relation(rel: dict, body_head: str) -> dict | None:
    """验证 LLM 返回的一条 relation，返回规范化版本或 None。"""
    ref = canonicalize_ref(rel.get("ref") or "")
    relation = (rel.get("relation") or "").strip().lower()
    evidence = (rel.get("evidence") or "").strip()

    if not ref:
        return None
    if relation not in VALID_RELATIONS:
        return None
    if len(evidence) < 5:
        return None
    # evidence 必须在 body 里出现（允许标点波动，取前 20 字做近似匹配）
    probe = re.sub(r"\s+", "", evidence[:20])
    body_strip = re.sub(r"\s+", "", body_head)
    if probe and probe not in body_strip:
        return None
    return {"ref": ref, "relation": relation, "evidence": evidence}


def process_one(
    p: Path, client: httpx.Client, dry_run: bool
) -> dict:
    """处理单个 note 文件，返回结果字典。"""
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

    # 调 Opus
    try:
        raw_relations, usage = extract_with_opus(body_head, reg_id, title, client=client)
    except Exception as e:
        return {"file": p.name, "reg_id": reg_id, "status": "api_error", "err": str(e)}

    # 验证 + 规范化
    existing = parse_existing_equivs(fm)
    self_reg = reg_id
    accepted = []
    seen_refs = set()
    for rel in raw_relations:
        v = validate_relation(rel, body_head)
        if not v:
            continue
        if v["ref"] == self_reg:
            continue
        if v["ref"] in existing or v["ref"] in seen_refs:
            continue
        seen_refs.add(v["ref"])
        accepted.append(v)

    result = {
        "file": p.name,
        "reg_id": reg_id,
        "status": "ok",
        "raw_count": len(raw_relations),
        "accepted_count": len(accepted),
        "accepted": accepted,
        "usage": usage,
    }

    # 写回
    if accepted and not dry_run:
        equivs = fm.get("equivalent_to") or []
        if not isinstance(equivs, list):
            equivs = []
        for v in accepted:
            equivs.append({
                "ref": v["ref"],
                "relation": v["relation"],
                "source": "stage3_llm_opus",
                "evidence": v["evidence"][:200],
            })
        fm["equivalent_to"] = equivs
        new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        p.write_text("---\n" + new_fm + "---" + body, encoding="utf-8")
        result["written"] = True

    return result


def find_candidates() -> list[Path]:
    cn_dir = WIKI / "cn"
    out = []
    for p in cn_dir.rglob("*.md"):
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
        eq = fm.get("equivalent_to") or []
        if isinstance(eq, list) and len(eq) > 0:
            continue
        body_head = txt[end + 4:][:3000]
        foreign = FOREIGN_REF_RE.findall(body_head)
        cites = CITE_KEYWORDS_RE.findall(body_head)
        if not foreign:
            continue
        if cites or len(foreign) >= 2:
            out.append(p)
    return out


def load_resume() -> set[str]:
    """读取已完成的 note 名，支持断点续跑。"""
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
    RESUME_LOG.parent.mkdir(exist_ok=True)
    with RESUME_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="不写回，只打印")
    ap.add_argument("--limit", type=int, default=0, help="最多处理 N 条，0=全跑")
    ap.add_argument("--workers", type=int, default=3, help="并发数，默认 3")
    ap.add_argument("--resume", action="store_true", help="跳过已写入 resume log 的文件")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    candidates = find_candidates()
    print(f"候选 notes: {len(candidates)}")

    if args.resume:
        done = load_resume()
        candidates = [p for p in candidates if p.name not in done]
        print(f"跳过已完成: {len(done)}, 剩余待处理: {len(candidates)}")

    if args.limit > 0:
        candidates = candidates[: args.limit]
        print(f"受 --limit 限制，本次处理: {len(candidates)}")

    mode = "DRY RUN" if args.dry_run else "APPLY"
    print(f"模式: {mode}, workers: {args.workers}, model: {OPUS_MODEL}")
    print("-" * 60)

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
                if not args.dry_run and r.get("status") == "ok":
                    append_resume(r)
                u = r.get("usage") or {}
                total_in += u.get("input_tokens") or 0
                total_out += u.get("output_tokens") or 0
                line = f"[{i:>3}/{len(candidates)}] {r.get('reg_id','?'):<25} status={r.get('status'):<10}"
                if r.get("accepted_count") is not None:
                    line += f" accepted={r['accepted_count']}"
                print(line)
                if args.verbose and r.get("accepted"):
                    for a in r["accepted"]:
                        print(f"       - {a['ref']} [{a['relation']}] evidence={a['evidence'][:60]}...")

    print("-" * 60)
    ok_count = sum(1 for r in results if r.get("status") == "ok")
    err_count = sum(1 for r in results if r.get("status") not in ("ok",))
    accepted_total = sum(r.get("accepted_count") or 0 for r in results)
    print(f"完成 ok: {ok_count}, error: {err_count}")
    print(f"新增 relations: {accepted_total}")
    print(f"Token 消耗: input={total_in:,}, output={total_out:,}")

    # 成本估算（Opus 4 官方价）
    cost_in = total_in / 1_000_000 * 15
    cost_out = total_out / 1_000_000 * 75
    print(f"成本估算（官方 Opus）: ${cost_in:.3f} + ${cost_out:.3f} = ${cost_in + cost_out:.3f}")

    if args.dry_run:
        print("\n[DRY RUN] 没写回任何文件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
