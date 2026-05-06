"""
_mark_final_skipped.py — 给最后 13 条 not_run notes 打分类 skip 标记

按性质分类（4 类）：
  - skip_redundant_chinese  : 中文扫描版冗余（vault 已有英文版 OCR）
  - skip_split_pending      : 中文版超页待 split（暂不处理）
  - skip_non_regulation     : 综述/参考书（不该走法规 OCR）
  - skip_oversize_unprocessable : >50MB 超大件 / 上传错误大件

操作：给 FM 加：
  - _ocr_upgraded: skipped
  - _ocr_skip_reason: <category>
  - _ocr_skip_note: <说明>
  - _ocr_skipped_at: 2026-04-25
"""
from __future__ import annotations
import re
import sys
from datetime import date
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

# 13 条分类
CATEGORIES: dict[str, dict] = {
    # 5 条中文扫描版冗余
    "ECE R44.md":  {"reason": "skip_redundant_chinese",
                    "note": "中文扫描版（11.ECE法规（中文）/法规44号/44.pdf, 145p / 26MB），与已 OCR 的英文 ECE R44 Rev3 内容冗余"},
    "ECE R46.md":  {"reason": "skip_redundant_chinese",
                    "note": "中文扫描版（欧标法规后视镜要求-0725.pdf, 65p / 31MB），与已 OCR 的英文 ECE R46 Rev6 系列冗余"},
    "ECE R48.md":  {"reason": "skip_redundant_chinese",
                    "note": "中文扫描版（法规48号/48.pdf, 76p / 10.6MB），与已 OCR 的英文 ECE R48 Rev12 冗余"},
    "ECE R99.md":  {"reason": "skip_redundant_chinese",
                    "note": "中文扫描版（法规99号/99.pdf, 43p / 24MB），文件性质为扫描件 PPT 转 PDF"},
    "ECE R115.md": {"reason": "skip_redundant_chinese",
                    "note": "中文扫描版（法规115号/115.pdf, 62p / 21MB），与英文 ECE R115 Rev1 系列冗余"},

    # 1 条中文超页待 split
    "ECE R49.md":  {"reason": "skip_split_pending",
                    "note": "中文超页扫描版（法规49号/49.pdf, 217p / 51MB），需走 split 流程；vault 已有英文 ECE R49 Rev6 三 part split 完成"},

    # 3 条非法规综述/参考书
    "automobile2019.md": {"reason": "skip_non_regulation",
                          "note": "国外法规年度综述（30.7MB），非单一法规文档"},
    "汽车典型结构图册_人民交通出版社汽车图书出版中心编.md": {
        "reason": "skip_non_regulation",
        "note": "工程参考书（42.4MB），非法规文档"},
    "汽车构造_李晶华主编.md": {"reason": "skip_non_regulation",
                              "note": "教材（17.6MB），非法规文档"},

    # 4 条超大件 GB 标准
    "GB 13392-2023.md":  {"reason": "skip_oversize_unprocessable",
                          "note": "19.8MB 大件，含大量道路交通图示（扫描），OCR 收益不确定"},
    "GB 27887-2024.md":  {"reason": "skip_oversize_unprocessable",
                          "note": "14.8MB 大件（儿童约束系统），含大量图表扫描"},
    "GB 5768.2-2022.md": {"reason": "skip_oversize_unprocessable",
                          "note": "**123.3MB** 巨大件（道路交通标志和标线·第2部分），超过常规 OCR 处理能力"},
    "GB T 43402-2023.md":{"reason": "skip_oversize_unprocessable",
                          "note": "20.9MB 大件，多次 upload_error；扫描质量需后续手工评估"},
}


def main() -> int:
    today = date.today().isoformat()
    print(f"\n{'='*72}")
    print(f"  最后一批 skip 标记 · {len(CATEGORIES)} 条")
    print(f"{'='*72}\n")

    by_category: dict[str, int] = {}
    written = 0
    not_found = []
    already_marked = []

    for fname, info in CATEGORIES.items():
        # 找文件
        candidates = list(WIKI.rglob(fname))
        if not candidates:
            not_found.append(fname)
            continue
        p = candidates[0]
        txt = p.read_text(encoding="utf-8", errors="replace")
        mo = FM_RE.match(txt)
        if not mo:
            print(f"  ✗ {fname}: 无 FM")
            continue
        try:
            fm = yaml.safe_load(mo.group(1)) or {}
        except yaml.YAMLError:
            print(f"  ✗ {fname}: bad FM")
            continue
        body = txt[mo.end():]

        if fm.get("_ocr_upgraded"):
            already_marked.append((fname, fm.get("_ocr_upgraded")))
            continue

        # 加标记
        fm["_ocr_upgraded"] = "skipped"
        fm["_ocr_skip_reason"] = info["reason"]
        fm["_ocr_skip_note"] = info["note"]
        fm["_ocr_skipped_at"] = today

        new_fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        body_clean = body.lstrip("\n")
        new_text = f"---\n{new_fm_str}---\n\n{body_clean}"
        if not new_text.endswith("\n"):
            new_text += "\n"
        p.write_text(new_text, encoding="utf-8")
        written += 1
        by_category[info["reason"]] = by_category.get(info["reason"], 0) + 1
        print(f"  ✓ {fname:<50}  → {info['reason']}")

    print(f"\n{'='*72}")
    print(f"  写入: {written} / {len(CATEGORIES)}")
    if already_marked:
        print(f"\n  已被标记（跳过）:")
        for n, v in already_marked:
            print(f"    · {n}  ({v})")
    if not_found:
        print(f"\n  ✗ 未找到的文件:")
        for n in not_found:
            print(f"    · {n}")
    if by_category:
        print(f"\n  分类汇总:")
        for k, v in by_category.items():
            print(f"    {k:<32}  {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
