"""
修复 _qc_merged.py 扫出的 3 类问题：

1. LaTeX 不平衡 (GB T 12544-2012.md 里 `\\]` 应为 `$$`)
2. 伪图占位 (3 条 note 共 12 个 `![xxx](图N描述...)` 这种 markdown，
   替换成 `*图 N（说明）见下方"原文参考"段*` 纯文本)

使用：
    python _fix_qc_issues.py --dry-run    # 看要改什么
    python _fix_qc_issues.py              # 实跑
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

# pattern: ![alt](src) 且 src 以 "图" 开头（伪图占位，不是真文件路径）
FAKE_IMG_RE = re.compile(r"!\[([^\]]*)\]\((图[^)]*)\)")
# alt 里提取 "图 N" 或 "图N" 后的说明
ALT_CAPTION_RE = re.compile(r"图\s*(\d+)\s*(.*)")
# src 里提取 "描述：" 或 "说明：" 后的补充文字
SRC_EXTRA_RE = re.compile(r"图\s*\d+\s*(?:描述|说明)\s*[:：](.*)", re.DOTALL)


def extract_caption_and_note(alt: str, src: str) -> str:
    """根据 alt-text 和 src 生成替换文本。

    优先保留 src 里"描述：xxx"中的变量定义等有效信息，追加成一段引用。
    """
    suffix = '见下方"原文参考"段'

    # 解析 alt 里的图号和说明
    alt_m = ALT_CAPTION_RE.search(alt.strip())
    if alt_m:
        num = alt_m.group(1)
        caption = alt_m.group(2).strip()
        if caption:
            head = f"*图 {num}（{caption}）{suffix}*"
        else:
            head = f"*图 {num} {suffix}*"
    else:
        head = f"*{alt} · {suffix}*"

    # 解析 src 里的补充说明
    extra_m = SRC_EXTRA_RE.search(src)
    if extra_m:
        extra = extra_m.group(1).strip()
        if extra:
            return f"{head}\n> 说明：{extra}"

    return head


def fix_fake_images(text: str) -> tuple[str, int]:
    """替换所有 ![...](图X...) 为纯文本引用。返回 (新文本, 替换数)。"""
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        count += 1
        alt, src = m.group(1), m.group(2)
        return extract_caption_and_note(alt, src)

    new = FAKE_IMG_RE.sub(repl, text)
    return new, count


def fix_latex_unbalanced(text: str, note_name: str) -> tuple[str, bool]:
    """只针对已知 note 修复。"""
    if note_name != "GB T 12544-2012.md":
        return text, False

    # line: `$$ k = \frac{V_D}{V_A} \]`
    old = r"$$ k = \frac{V_D}{V_A} \]"
    new = r"$$ k = \frac{V_D}{V_A} $$"
    if old in text:
        text = text.replace(old, new)
        return text, True
    return text, False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total_fake = 0
    total_latex = 0
    touched_notes: list[tuple[str, str]] = []  # (note_name, what_changed)

    for p in WIKI.rglob("*.md"):
        if "_mineru_assets" in str(p):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        new_text = text
        changes = []

        # 1) LaTeX
        new_text, fixed_latex = fix_latex_unbalanced(new_text, p.name)
        if fixed_latex:
            total_latex += 1
            changes.append("latex")

        # 2) Fake images
        new_text, n_fake = fix_fake_images(new_text)
        if n_fake:
            total_fake += n_fake
            changes.append(f"fake_imgs={n_fake}")

        if changes:
            touched_notes.append((p.name, ", ".join(changes)))
            if args.dry_run:
                print(f"  [DRY] {p.name:40s}  {', '.join(changes)}")
            else:
                p.write_text(new_text, encoding="utf-8")
                print(f"  [WRITE] {p.name:40s}  {', '.join(changes)}")

    print(f"\n修复汇总:")
    print(f"  伪图替换:     {total_fake}")
    print(f"  LaTeX 修复:   {total_latex}")
    print(f"  涉及 notes:   {len(touched_notes)}")
    if args.dry_run:
        print("\n[DRY-RUN] 未写入。去掉 --dry-run 实跑。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
