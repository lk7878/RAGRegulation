"""
_apply_dedupe_decisions.py — 执行 Opus 在 dedupe_resolution_proposal_2026-04-21.md 中的决议

决议类型：
1. 🔄 _dup 替换 canonical（2 组）：
   - 把 canonical 移到 .trash/<reg_id>_canonical_replaced_YYYY-MM-DD.md
   - 把 _dup1 重命名为 canonical
2. 📑 两份都留·_dup 重命名为 "(EN)"（13 组）：
   - `ECE R108_dup1.md` → `ECE R108 (EN).md`
3. ❓ 跳过 EU 2018/858（需人工）

默认 dry-run，加 --execute 才真动。
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
TRASH = Path(r"D:\CcVault\.trash")
TODAY = date.today().isoformat()


# Group 1: _dup 替换 canonical（2 组）
REPLACE_DECISIONS = [
    {
        "reg_id": "GB/T 38892-2020",
        "canonical": WIKI / "cn" / "GB T 38892-2020.md",
        "dup": WIKI / "cn" / "GB T 38892-2020_dup1.md",
        "reason": "_dup (10272 chars) 是原文展开版，canonical (3574) 是摘要，_dup 质量更高",
    },
    {
        "reg_id": "GB 21670-2008",
        "canonical": WIKI / "cn" / "GB 21670-2008.md",
        "dup": WIKI / "cn" / "GB 21670-2008_dup1.md",
        "reason": "_dup (20236) 是原文完整版，canonical (5568) 是摘要；注意 status 不一致（active vs superseded）",
    },
]


# Group 2: _dup 重命名为 (EN)（13 组）
RENAME_DECISIONS = [
    {
        "reg_id": "ECE R108",
        "dup": WIKI / "ece" / "ECE R108_dup1.md",
        "new_name": "ECE R108 (EN).md",
    },
    {
        "reg_id": "ECE R102",
        "dup": WIKI / "ece" / "ECE R102_dup1.md",
        "new_name": "ECE R102 (EN).md",
    },
    {
        "reg_id": "ECE R114",
        "dup": WIKI / "ece" / "ECE R114_dup.md",
        "new_name": "ECE R114 (EN).md",
    },
    {
        "reg_id": "ECE R122",
        "dup": WIKI / "ece" / "ECE R122_dup.md",
        "new_name": "ECE R122 (EN).md",
    },
    {
        "reg_id": "ECE R13",
        "dup": WIKI / "ece" / "ECE R13_dup1.md",
        "new_name": "ECE R13-H Rev4 Am2 (EN).md",
        "note": "原 ECE R13 Rev4 Am2.md 也存在但 reg_id 标注有误；此次只处理 _dup1",
    },
    {
        "reg_id": "ECE R55 Rev1 Corr1",
        "dup": WIKI / "ece" / "ECE R55 Rev1 Corr1_dup1.md",
        "new_name": "ECE R55 Rev1 Corr1 (EN).md",
    },
    {
        "reg_id": "ECE R21 Rev2",
        "dup": WIKI / "ece" / "ECE R21 Rev2_dup1.md",
        "new_name": "ECE R21 Rev2 (EN).md",
    },
    {
        "reg_id": "ECE R42",
        "dup": WIKI / "ece" / "ECE R42_dup1.md",
        "new_name": "ECE R42 (EN).md",
    },
    {
        "reg_id": "ECE R68",
        "dup": WIKI / "ece" / "ECE R68_dup1.md",
        "new_name": "ECE R68 (EN).md",
    },
    {
        "reg_id": "ECE R59",
        "dup": WIKI / "ece" / "ECE R59_dup1.md",
        "new_name": "ECE R59 (EN).md",
    },
    {
        "reg_id": "ECE R84",
        "dup": WIKI / "ece" / "ECE R84_dup1.md",
        "new_name": "ECE R84 (EN).md",
    },
    {
        "reg_id": "ECE R89",
        "dup": WIKI / "ece" / "ECE R89_dup1.md",
        "new_name": "ECE R89 (EN).md",
    },
    {
        "reg_id": "ECE R93",
        "dup": WIKI / "ece" / "ECE R93_dup1.md",
        "new_name": "ECE R93 (EN).md",
    },
]

# ECE R13 Rev4 Am2 特殊 case
# 原名 ECE R13 Rev4 Am2.md 实为 ECE R13-H Rev4 Am2 的英文修正，reg_id 被标错为 ECE R13
# Opus 建议重命名为 ECE R13-H Rev4 Am2 (EN).md
# 但 _dup1 也建议用同样名字，需二选一避免冲突。
# 这里先不动 `ECE R13 Rev4 Am2.md`，只处理 _dup1


def execute_replace(src_canonical: Path, src_dup: Path, execute: bool) -> bool:
    """把 canonical 移 trash，把 _dup 升为 canonical."""
    if not src_canonical.exists():
        print(f"  ⚠️ canonical 不存在: {src_canonical.name}")
        return False
    if not src_dup.exists():
        print(f"  ⚠️ _dup 不存在: {src_dup.name}")
        return False

    trash_name = f"{src_canonical.stem}_replaced_{TODAY}.md"
    trash_path = TRASH / trash_name

    if not execute:
        print(f"  [DRY] {src_canonical.name} -> .trash/{trash_name}")
        print(f"  [DRY] {src_dup.name} -> {src_canonical.name}")
        return True

    TRASH.mkdir(exist_ok=True)
    shutil.move(str(src_canonical), str(trash_path))
    shutil.move(str(src_dup), str(src_canonical))
    print(f"  ✓ canonical → .trash/{trash_name}")
    print(f"  ✓ _dup → {src_canonical.name}")
    return True


def execute_rename(src: Path, new_name: str, execute: bool) -> bool:
    """在同目录重命名."""
    if not src.exists():
        print(f"  ⚠️ 源文件不存在: {src.name}")
        return False
    dest = src.parent / new_name
    if dest.exists():
        print(f"  ⚠️ 目标已存在，跳过: {dest.name}")
        return False
    if not execute:
        print(f"  [DRY] {src.name} -> {new_name}")
        return True
    src.rename(dest)
    print(f"  ✓ {src.name} -> {new_name}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true",
                    help="真实执行；默认 dry-run")
    args = ap.parse_args()

    print("=" * 70)
    print(f"  Dedupe 决议执行 · mode={'REAL' if args.execute else 'DRY-RUN'}")
    print("=" * 70)

    print("\n[1] _dup 替换 canonical（2 组）:\n")
    replace_ok = 0
    for d in REPLACE_DECISIONS:
        print(f"--- {d['reg_id']}")
        print(f"    理由: {d['reason']}")
        if execute_replace(d["canonical"], d["dup"], args.execute):
            replace_ok += 1

    print(f"\n[2] _dup 重命名为 (EN)（13 组）:\n")
    rename_ok = 0
    for d in RENAME_DECISIONS:
        print(f"--- {d['reg_id']}")
        if execute_rename(d["dup"], d["new_name"], args.execute):
            rename_ok += 1

    print(f"\n[3] 需要人工判断（1 组）:")
    print(f"  ❓ (EU) 2018/858 — _dup 实为多法规汇编，reg_id 可能标错。跳过。")

    print(f"\n{'=' * 70}")
    print(f"  汇总: replace {replace_ok}/2  ·  rename {rename_ok}/13")
    if not args.execute:
        print(f"  [DRY-RUN] 未写入。确认无误后加 --execute 真实执行。")
    else:
        print(f"  ✓ 完成。记得：")
        print(f"    1. 跑 `_manifest_sync.py` 同步 manifest")
        print(f"    2. 跑 `_semantic_search.py --rebuild` 重建 BM25 索引")
        print(f"    3. 手工更新 `05_Audit/dedupe_conflicts_2026-04-21.md` 状态为 resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
