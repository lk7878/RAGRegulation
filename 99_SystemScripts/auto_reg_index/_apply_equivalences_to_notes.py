"""
Stage 3：把 curated_equivalences 的映射 写回到具体 note 的 FM。

规则：
- src (家族级，如 "GB 14166") → 匹配该家族下所有 notes (GB 14166-1993, GB 14166-2013)
- 每个 note FM 加上/更新 equivalent_to 列表，含 ref + relation + source (topic)
- 目标侧：targets 家族是 ECE R16，则反向也给 ECE R16 家族下的 notes 添加反向映射

用法：--dry-run 预演，或直接执行
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CURATED = ROOT / ".stage3" / "curated_equivalences.json"
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")


def strip_version(reg_id: str) -> str:
    """'GB 14166-2013' -> 'GB 14166'; 'ECE R16 Rev2 Am1' -> 'ECE R16'."""
    s = (reg_id or "").strip()
    s = re.sub(r"-(19|20)\d{2}(/XG\d+-\d{4})?$", "", s)
    s = re.sub(r"\s+(Rev\.?\d+|Am\.?\d+|Corr\.?\d+|Amendment\s*\d+|amd\d+).*$", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s*\(Rev\.?\d+[^)]*\)\s*$", "", s)
    return s.strip()


def normalize_eq_target(t: str) -> str:
    """target 如 'R44' 规整为 'ECE R44'（从上下文推断）。"""
    t = t.strip()
    if re.match(r"^R\d", t):
        return f"ECE {t}"
    return t


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    curated = json.loads(CURATED.read_text(encoding="utf-8"))

    # 构建 family -> [edges] 映射
    family_to_edges: dict[str, list] = defaultdict(list)
    for e in curated:
        if e["target"] and e["relation"] != "no_direct_match":
            family_to_edges[e["src"]].append({
                "ref": normalize_eq_target(e["target"]),
                "relation": "equivalent",
                "topic": e["topic"],
            })

    # 扫描所有 notes，家族匹配即加字段
    stats = {"scanned": 0, "updated": 0, "new_eq": 0, "already_present": 0}

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

        stats["scanned"] += 1
        reg_id = fm.get("reg_id") or ""
        family = strip_version(reg_id)
        if family not in family_to_edges:
            continue

        eqs_to_add = family_to_edges[family]

        # 获取当前 equivalent_to
        existing = fm.get("equivalent_to") or []
        if isinstance(existing, dict):
            existing = [existing]
        if not isinstance(existing, list):
            existing = []

        existing_refs = {str(e.get("ref") or "").strip() for e in existing if isinstance(e, dict)}

        added_any = False
        for eq in eqs_to_add:
            if eq["ref"] not in existing_refs:
                existing.append({
                    "ref": eq["ref"],
                    "relation": eq["relation"],
                    "source": f"stage3_curated:{eq['topic']}",
                })
                added_any = True
                stats["new_eq"] += 1
                existing_refs.add(eq["ref"])
            else:
                stats["already_present"] += 1

        if added_any:
            fm["equivalent_to"] = existing
            if not args.dry_run:
                new_fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
                body = txt[end + 4 :]
                new_content = "---\n" + new_fm_yaml + "---" + body
                p.write_text(new_content, encoding="utf-8")
            stats["updated"] += 1

    print("Stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if args.dry_run:
        print("\n[DRY RUN] No files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
