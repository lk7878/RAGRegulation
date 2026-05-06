"""
_expand_equivalence.py

自动扫 GB 标准 body 的"前言"部分识别采标声明，扩展 FM 的 equivalent_to 字段。
修复审计报告 P1.2 — 等价映射覆盖率偏低（95/448）。

采标模式：
- `本标准修改采用 ECE RXX` → relation: modified
- `本标准等同采用 ISO XXXX` → relation: identical
- `本标准非等效采用` → relation: non_equivalent
- `本标准参照/参考 ECE RXX` → relation: reference

处理逻辑：
- 只扫 body 前 3000 字符（通常前言在此范围）
- 不在段落中找到多次 trigger 内含相同 reg_id 时，取最高置信度的 relation
- 不重复添加已有 equivalent_to 中的 ref
- 写入格式与 s3_equivalence 保持一致：
  equivalent_to:
    - ref: ECE R25
      relation: modified
      source: stage3_body_inference

用法：
    python _expand_equivalence.py --dry-run
    python _expand_equivalence.py
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

# ---------- 采标 trigger → relation ----------
TRIGGER_RELATIONS = [
    ("modified", [r"修改采用", r"modified\s+adoption"]),
    ("identical", [r"等同采用", r"等效采用", r"identical\s+adoption", r"identical\s+to"]),
    ("non_equivalent", [r"非等效采用", r"非等同采用"]),
    ("reference", [r"参照", r"参考", r"based\s+on"]),
]

# ---------- reg_id pattern ----------
# ECE R13H Rev4 Am1 / ECE R25 / ECE R25 版本1 / ECE R25法规
ECE_RE = re.compile(
    r"\b(?:UN(?:ECE)?|ECE)[-\s]?R\s?(\d{1,4})([Hh])?"
    r"(?:\s*(?:Rev|版本|修订)\s*(\d+))?"
    r"(?:\s*(?:Am|修改单)\s*(\d+))?",
    re.IGNORECASE,
)
# ISO 15008 / ISO 16505:2017
ISO_RE = re.compile(r"\bISO\s?(\d{2,6})(?:[-:](\d{2,4}))?", re.IGNORECASE)
# Regulation (EU) 2018/858 / EU 2018 858
EU_RE = re.compile(
    r"\b(?:Regulation\s+)?\(?EU\)?\s+(\d{4}[-/\s]\d{1,4})",
    re.IGNORECASE,
)

RELATION_PRIORITY = {
    "identical": 4,
    "modified": 3,
    "non_equivalent": 2,
    "reference": 1,
}


def canonicalize_ece(match) -> str:
    num, h, rev, am = match.groups()
    h = h.upper() if h else ""
    parts = [f"ECE R{int(num)}{h}"]
    if rev:
        parts.append(f"Rev{int(rev)}")
    if am:
        parts.append(f"Am{int(am)}")
    return " ".join(parts)


def canonicalize_iso(match) -> str:
    num, year = match.groups()
    if year:
        return f"ISO {num}:{year}"
    return f"ISO {num}"


def canonicalize_eu(match) -> str:
    payload = match.group(1).replace(" ", "/").replace("-", "/")
    return f"(EU) {payload}"


def find_equivalences(text: str) -> list[tuple[str, str]]:
    """返回 [(ref_reg_id, relation), ...]，按 trigger 窗口匹配。"""
    results: dict[str, str] = {}  # ref -> relation（高优先级覆盖低的）

    for relation, patterns in TRIGGER_RELATIONS:
        for trig_pattern in patterns:
            for m in re.finditer(trig_pattern, text):
                # 取 trigger 后 80 字符窗口内的 reg_id
                start = m.end()
                window = text[start : start + 120]
                for regex, canon in (
                    (ECE_RE, canonicalize_ece),
                    (ISO_RE, canonicalize_iso),
                    (EU_RE, canonicalize_eu),
                ):
                    for reg_m in regex.finditer(window):
                        ref = canon(reg_m)
                        # 高优先级 relation 覆盖低的
                        existing_rel = results.get(ref)
                        if (
                            existing_rel is None
                            or RELATION_PRIORITY[relation]
                            > RELATION_PRIORITY.get(existing_rel, 0)
                        ):
                            results[ref] = relation
    return sorted(results.items())


def parse_existing_equivs(fm: dict) -> set[str]:
    """获取已有 equivalent_to 的 ref 集合。"""
    equivs = fm.get("equivalent_to") or []
    if not isinstance(equivs, list):
        return set()
    refs = set()
    for item in equivs:
        if isinstance(item, dict):
            ref = item.get("ref") or item.get("reg_id")
            if ref:
                refs.add(str(ref).strip())
        elif isinstance(item, str):
            # 可能是 "[[ECE R25]]" wikilink
            m = re.search(r"\[\[([^\]|]+)", item)
            refs.add(m.group(1).strip() if m else item.strip())
    return refs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only-region", default="cn", help="只处理指定 region，默认 cn")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    target_dir = WIKI / args.only_region if args.only_region else WIKI
    scanned = 0
    with_trigger = 0
    files_updated = 0
    total_new_refs = 0
    predictions = []

    for p in target_dir.rglob("*.md"):
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
        body = txt[end + 4 :]
        scanned += 1

        # 只看 body 前 3000 字符（前言 + 部分章节）
        head = body[:3000]
        candidates = find_equivalences(head)
        if not candidates:
            continue
        with_trigger += 1

        existing_refs = parse_existing_equivs(fm)
        self_reg = (fm.get("reg_id") or "").strip()
        new_refs = [
            (ref, rel) for ref, rel in candidates
            if ref not in existing_refs and ref != self_reg
        ]
        if not new_refs:
            continue

        total_new_refs += len(new_refs)
        predictions.append({
            "file": p.name,
            "reg_id": self_reg,
            "existing_count": len(existing_refs),
            "add": new_refs,
        })

        if args.dry_run:
            continue

        # 写回 FM
        equivs = fm.get("equivalent_to") or []
        if not isinstance(equivs, list):
            equivs = []
        for ref, rel in new_refs:
            equivs.append({
                "ref": ref,
                "relation": rel,
                "source": "stage3_body_inference",
            })
        fm["equivalent_to"] = equivs

        new_fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        new_content = "---\n" + new_fm_yaml + "---" + body
        p.write_text(new_content, encoding="utf-8")
        files_updated += 1

    # 输出
    print(f"Scanned                  : {scanned}")
    print(f"Files with采标 trigger   : {with_trigger}")
    print(f"Files needing backfill   : {len(predictions)}")
    print(f"Total new refs to add    : {total_new_refs}")
    if not args.dry_run:
        print(f"Files updated            : {files_updated}")

    if args.verbose or args.dry_run:
        print("\n=== Predictions ===")
        for pred in predictions:
            print(
                f"  [{pred['reg_id']:<20}] existing={pred['existing_count']}  "
                f"add={pred['add']}"
            )

    if args.dry_run:
        print("\n[DRY RUN] No files written.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
