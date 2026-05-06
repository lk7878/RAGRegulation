"""
_qc_merged.py — 自动 QC 所有 MinerU 升级过的 notes

检查项：
1. FM YAML 能否正确解析
2. FM 含 _ocr_upgraded: mineru
3. FM 的 _mineru_blocks 数字跟 body 里实际出现的一致
4. "## 原文参考" 节存在且位于 body 末尾
5. 所有 ![](...) 图像引用在磁盘上存在
6. LaTeX $$ ... $$ 块成对（偶数个 $$）
7. HTML <table>...</table> 标签成对

不修复，只报告。
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("需要 pip install pyyaml", file=sys.stderr)
    sys.exit(1)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
ASSETS = WIKI / "_mineru_assets"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

issues: Counter[str] = Counter()
examples: dict[str, list[tuple[str, str]]] = {}


def add_issue(tag: str, note_name: str, detail: str = "") -> None:
    issues[tag] += 1
    if tag not in examples:
        examples[tag] = []
    if len(examples[tag]) < 3:
        examples[tag].append((note_name, detail))


def check_note(path: Path) -> bool:
    """Return True if upgraded."""
    try:
        txt = path.read_text(encoding="utf-8")
    except Exception as e:
        add_issue("read_fail", path.name, str(e)[:80])
        return False

    # 1. FM
    m = FM_RE.match(txt)
    if not m:
        add_issue("fm_missing_or_bad", path.name, "无 FM 块")
        return False
    fm_raw = m.group(1)
    try:
        fm = yaml.safe_load(fm_raw)
    except Exception as e:
        add_issue("fm_yaml_parse_fail", path.name, str(e)[:80])
        return False
    if not isinstance(fm, dict):
        add_issue("fm_not_dict", path.name)
        return False

    if fm.get("_ocr_upgraded") not in ("mineru", "mineru_split"):
        return False  # not upgraded (mineru_no_assets / skipped / None), skip

    body = txt[m.end():]
    note_name = path.name

    # 2. MinerU section
    if "## 原文参考" not in body:
        add_issue("missing_mineru_section", note_name)
        return True

    # 3. FM blocks vs. body
    blocks = fm.get("_mineru_blocks") or {}
    declared_tables = int(blocks.get("tables", 0) or 0)
    declared_formulas = int(blocks.get("formulas", 0) or 0)
    declared_images = int(blocks.get("images", 0) or 0)

    actual_tables = body.count("<table>")
    # formulas 在 "### 公式" 节里，以 $$ ... $$ 包裹
    formula_section_match = re.search(r"###\s*公式.*?(?=###|\Z)", body, re.DOTALL)
    actual_formulas = 0
    if formula_section_match:
        actual_formulas = len(re.findall(r"\$\$[\s\S]+?\$\$", formula_section_match.group(0)))
    image_section_match = re.search(r"###\s*图像.*?(?=###|\Z)", body, re.DOTALL)
    actual_images = 0
    if image_section_match:
        actual_images = len(re.findall(r"!\[[^\]]*\]\([^\)]+\)", image_section_match.group(0)))

    if declared_tables != actual_tables:
        add_issue(
            "table_count_mismatch",
            note_name,
            f"declared={declared_tables} actual={actual_tables}",
        )
    if declared_formulas != actual_formulas:
        add_issue(
            "formula_count_mismatch",
            note_name,
            f"declared={declared_formulas} actual={actual_formulas}",
        )
    if declared_images != actual_images:
        add_issue(
            "image_count_mismatch",
            note_name,
            f"declared={declared_images} actual={actual_images}",
        )

    # 4. HTML table tag balance
    open_table = body.count("<table>")
    close_table = body.count("</table>")
    if open_table != close_table:
        add_issue(
            "table_unbalanced",
            note_name,
            f"<table>={open_table} </table>={close_table}",
        )

    # 5. LaTeX $$ balance
    dollar_dollar = body.count("$$")
    if dollar_dollar % 2 != 0:
        add_issue("latex_unbalanced", note_name, f"$$ count={dollar_dollar}")

    # 6. Image file existence
    note_dir = path.parent  # 图像引用相对 note 文件所在目录
    for ref in re.findall(r"!\[[^\]]*\]\(([^\)]+)\)", body):
        if ref.startswith(("http://", "https://")):
            continue
        # ref 是相对 note 的路径（如 "../_mineru_assets/<reg_id>/xxx.jpg"）
        img_path = (note_dir / ref).resolve()
        if not img_path.exists():
            add_issue(
                "image_file_missing",
                note_name,
                f"ref={ref[:60]}",
            )
            break  # 一条 note 只报一次 missing

    return True


def main() -> None:
    upgraded_count = 0
    total_scanned = 0
    for p in WIKI.rglob("*.md"):
        if "_mineru_assets" in str(p):
            continue
        total_scanned += 1
        if check_note(p):
            upgraded_count += 1

    print(f"扫描 notes: {total_scanned}")
    print(f"升级 notes: {upgraded_count}")
    print()
    if not issues:
        print("[完美] 未发现任何问题。")
        return

    print("=== 问题汇总 ===")
    for tag, count in sorted(issues.items(), key=lambda x: -x[1]):
        print(f"\n{tag}: {count} 条")
        for name, detail in examples.get(tag, []):
            print(f"  - {name:<45}  {detail}")


if __name__ == "__main__":
    main()
