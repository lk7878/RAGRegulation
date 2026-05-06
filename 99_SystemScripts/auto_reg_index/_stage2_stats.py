"""
Stage 2 cross-check 结果统计。

扫描所有 wiki notes：
- verified_by 字段存在 → cross-checked
- cross_check_overall_confidence 分布
- cross_check_flags 统计（mismatch/unsure fields 分布）
- recommend_review 数量
"""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")


def main() -> int:
    total = 0
    verified = 0
    conf_dist = Counter()
    flag_field_dist = Counter()
    flag_status_dist = Counter()
    needs_review = 0
    verified_ok = 0

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

        total += 1
        if fm.get("verified_by"):
            verified += 1
            conf = str(fm.get("cross_check_overall_confidence") or "unknown").lower()
            conf_dist[conf] += 1

            flags = fm.get("cross_check_flags") or []
            if flags:
                for flag in flags:
                    if isinstance(flag, dict):
                        flag_field_dist[str(flag.get("field") or "unknown")] += 1
                        flag_status_dist[str(flag.get("status") or "unknown")] += 1

            tags = fm.get("tags") or []
            if isinstance(tags, list):
                if "status/needs-review" in tags:
                    needs_review += 1
                if "status/verified" in tags:
                    verified_ok += 1

    print(f"Total notes: {total}")
    print(f"Cross-checked: {verified} ({verified / max(total, 1) * 100:.1f}%)")
    print()
    print("Confidence distribution:")
    for k, v in conf_dist.most_common():
        print(f"  {k:12} {v:5d} ({v / max(verified, 1) * 100:.1f}%)")
    print()
    print(f"Tag: status/verified   = {verified_ok}")
    print(f"Tag: status/needs-review = {needs_review}")
    print()
    print("Flagged field distribution (top 15):")
    for k, v in flag_field_dist.most_common(15):
        print(f"  {k:40} {v:4d}")
    print()
    print("Flag status distribution:")
    for k, v in flag_status_dist.most_common():
        print(f"  {k:12} {v:5d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
