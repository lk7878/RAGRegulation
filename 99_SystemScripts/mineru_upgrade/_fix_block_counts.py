"""
_fix_block_counts.py — 扫每条已合并的 note，从 body "## 原文参考（MinerU 云解析）" 节
重新统计真实的 tables/formulas/images 数量，回填 FM `_mineru_blocks`。

修的是：merge bug 修复前合并的 notes，FM 里 declared 数跟 body actual 数不一致。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
MINERU_SECTION_RE = re.compile(
    r"## 原文参考（MinerU 云解析[^）]*）(.*?)(?:\n## [^原]|\Z)",
    re.DOTALL,
)
# 表格：含 `<table ...>` 的 block，`</table>` 结尾
TABLE_RE = re.compile(r"<table[^>]*>.*?</table>", re.DOTALL)
# 公式：$$...$$（display math）
# 用 [\s\S]+? 而不是 [^$]+，允许公式内部含转义 $ (如 MinerU 产出的 `\$9`)
# 与 _qc_merged.py 的计数逻辑保持一致
FORMULA_RE = re.compile(r"\$\$[\s\S]+?\$\$", re.DOTALL)
# 图像：`![](path)` 或 `![alt](path)`
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def count_blocks(body: str) -> tuple[int, int, int]:
    """统计 body 里 MinerU section 的 table/formula/image 数量。"""
    m = MINERU_SECTION_RE.search(body)
    if not m:
        return 0, 0, 0
    section = m.group(1)

    tables = len(TABLE_RE.findall(section))
    formulas = len(FORMULA_RE.findall(section))
    images = 0
    for img_match in IMAGE_RE.finditer(section):
        path = img_match.group(1).strip()
        if path and not path.startswith("图"):  # 过滤 LLM 占位符 "图4描述"
            images += 1
    return tables, formulas, images


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    fixed = 0
    unchanged = 0
    skipped = 0

    for p in WIKI.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = FM_RE.match(text)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            skipped += 1
            continue
        if fm.get("_ocr_upgraded") != "mineru":
            continue

        body = text[m.end():]
        t, f, i = count_blocks(body)

        declared = fm.get("_mineru_blocks") or {}
        dt = declared.get("tables", 0)
        df = declared.get("formulas", 0)
        di = declared.get("images", 0)

        if (dt, df, di) == (t, f, i):
            unchanged += 1
            continue

        # 需要修复
        fm["_mineru_blocks"] = {"tables": t, "formulas": f, "images": i}

        if args.dry_run:
            print(f"  [DRY] {p.name:40s}  ({dt}/{df}/{di}) → ({t}/{f}/{i})")
        else:
            new_fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
            new_text = f"---\n{new_fm_text}---\n{body}"
            p.write_text(new_text, encoding="utf-8")
        fixed += 1

    print(f"\n修复: {fixed}  |  已对齐: {unchanged}  |  跳过(FM 破损): {skipped}")
    if args.dry_run:
        print("[DRY-RUN] 未写入。加 --execute 实跑（此脚本没 --execute 参数，去掉 --dry-run 即是实跑）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
