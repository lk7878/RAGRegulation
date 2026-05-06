"""
_fix_orphan_dups.py — 修复 4 条「孤儿 _dup1」遗留（canonical 不存在的 _dup1 文件）

背景：dedupe 流程曾经把 canonical 移入 trash，但 _dup1 没有重命名。
结果：vault 里只剩 ECE R*** _dup1.md 是该 reg_id 的唯一 note，文件名误导。

操作：
  1. 重命名 4 条 _dup1 → 正名（无冲突，因 canonical 不存在）
  2. 同步更新 vault 里所有指向 [[<reg_id>_dup1]] 的 wikilink → [[<reg_id>]]

不处理：
  - (EU) 2018/858_dup1.md（canonical 存在但内容性质不同，需单独人工拆分）

用法:
    python _fix_orphan_dups.py --dry-run
    python _fix_orphan_dups.py
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(r"D:\CcVault")
WIKI_ECE = VAULT / "01_Wiki" / "regulations" / "ece"

# 4 条 ECE _dup1 -> canonical 名（不带 _dup1）
TARGETS: list[tuple[str, str]] = [
    ("ECE R125_dup1", "ECE R125"),
    ("ECE R127_dup1", "ECE R127"),
    ("ECE R135_dup1", "ECE R135"),
    ("ECE R144_dup1", "ECE R144"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"\n{'='*72}")
    print(f"  修复孤儿 _dup1 · {len(TARGETS)} 条")
    print(f"{'='*72}")

    # Step 1: 校验源文件存在 + 目标文件不存在
    valid_pairs: list[tuple[Path, Path, str, str]] = []
    for old_stem, new_stem in TARGETS:
        old_path = WIKI_ECE / f"{old_stem}.md"
        new_path = WIKI_ECE / f"{new_stem}.md"
        if not old_path.exists():
            print(f"  ✗ {old_stem}: 源不存在")
            continue
        if new_path.exists():
            print(f"  ✗ {old_stem} → {new_stem}: 目标已存在，冲突")
            continue
        print(f"  ✓ {old_stem} → {new_stem}: ready")
        valid_pairs.append((old_path, new_path, old_stem, new_stem))

    if not valid_pairs:
        print("\n[ABORT] 无有效目标")
        return 1

    # Step 2: 扫 vault 里的 wikilink 引用
    print(f"\n{'='*72}")
    print(f"  扫描 wikilink 引用")
    print(f"{'='*72}")

    link_updates: list[tuple[Path, int]] = []  # (file_path, replace_count)
    for src_md in VAULT.rglob("*.md"):
        sp = str(src_md).lower()
        if ".trash" in sp or "trash_dups" in sp:
            continue
        # 跳过被 rename 的 _dup 文件自身
        if any(src_md.name == f"{old_stem}.md" for _, _, old_stem, _ in valid_pairs):
            continue
        try:
            txt = src_md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        new_txt = txt
        total = 0
        for _, _, old_stem, new_stem in valid_pairs:
            old_link_re = re.compile(rf"\[\[{re.escape(old_stem)}(\||\])")
            cnt = len(old_link_re.findall(new_txt))
            if cnt > 0:
                new_txt = old_link_re.sub(rf"[[{new_stem}\1", new_txt)
                total += cnt
        if total > 0:
            link_updates.append((src_md, total, new_txt))
            print(f"  · {src_md.relative_to(VAULT)}: {total} 处")

    print(f"\n  共 {len(link_updates)} 个文件需更新链接")

    if args.dry_run:
        print("\n[DRY-RUN] 未写入")
        return 0

    # Step 3: rename
    print(f"\n{'='*72}")
    print(f"  执行重命名 + 链接更新")
    print(f"{'='*72}")
    for old_path, new_path, old_stem, new_stem in valid_pairs:
        old_path.rename(new_path)
        print(f"  ✓ rename: {old_stem}.md → {new_stem}.md")

    for src_md, cnt, new_txt in link_updates:
        src_md.write_text(new_txt, encoding="utf-8")
        print(f"  ✓ links: {src_md.name} ({cnt} 处)")

    print(f"\n[DONE] {len(valid_pairs)} 条 rename + {len(link_updates)} 个文件 link 更新")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
