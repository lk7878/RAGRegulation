"""
_repair_broken_fm.py — 一次性修复 merge 脚本 bug 造成的 FM 破损

症状：closing --- 后直接贴 body 的 `# Title`，没空行：
    ---
    reg_id: X
    ---# UN Regulation ...

修复：在 closing --- 后插入 \n\n。
识别方法：用正则找 `^---\S` (即 --- 后直接接非空白字符，非正常)。

Dry-run 先预览，无误再实跑。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

# 匹配一行以 --- 开头、后直接跟非换行字符（即破损的 closing FM）
# 允许第四个字符是任何非空白（包括另一个 -，用于 `----` 这种 4+ 连 dash 的边界 case）
BROKEN_RE = re.compile(r"^---([^\n\s])", re.MULTILINE)


def repair(text: str) -> tuple[str, int]:
    """
    只修复第一个破损的 closing ---（FM 结束处），body 里理论上不应出现 `---<字符>` 模式。
    返回 (repaired, n_replacements)。

    识别模式：
    - `---<非空白>`：例如 `---# Title` 或 `----body` （4+ dash）
    正常 FM 结尾是 `---\n<空行>\n<body>`，字符 4 是 `\n`，被 `\s` 排除不会误匹配。
    """
    # 只替换第 1 次匹配（即 FM 的 closing）
    new_text, n = BROKEN_RE.subn(r"---\n\n\1", text, count=1)
    return new_text, n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    fixed = []
    untouched = 0
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        # 仅对开头是 --- 的 YAML FM 文件动
        if not txt.startswith("---\n"):
            continue
        new_txt, n = repair(txt)
        if n == 0:
            untouched += 1
            continue
        fixed.append((p, n))
        if not args.dry_run:
            p.write_text(new_txt, encoding="utf-8")

    print(f"扫描到以 FM 开头的 notes: {untouched + len(fixed)}")
    print(f"  无需修复: {untouched}")
    print(f"  需要修复: {len(fixed)}")
    print(f"\nTop 20 被修复的:")
    for p, n in fixed[:20]:
        print(f"  {p.name:<45} ({n} 处)")
    if len(fixed) > 20:
        print(f"  ... 还有 {len(fixed) - 20}")
    if args.dry_run:
        print("\n[DRY RUN] 未写入")
    else:
        print("\n✓ 修复完成")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
