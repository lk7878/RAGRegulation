"""
_fix_llm_alphabet_repetition.py — 修复 3 条 LLM 续抽时陷入「附录 A→B→...→Z→AA→...→ZZZZZZ」字母递增重复退化的 notes

策略：
  1. 找到灾难起始点：第一处 `附录\s*AA` 或 `附录\s*BB`（双字母及以上附录是 LLM 幻觉起点）
  2. 向前回溯到最近的换行符（保留正常段落）
  3. 截断灾难段，替换为说明性标注
  4. 加 FM 标记 _data_quality: llm_repetition_corrupted_truncated_2026-04-25

不删原 _ocr_upgraded 等 MinerU FM 字段，「## 原文参考」段在灾难之后的话也保留。
"""
from __future__ import annotations
import re
import sys
from datetime import date
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(r"D:\CcVault")
TARGETS = [
    r"02_Wiki\non_automotive\GB 3565-2005.md",
    r"01_Wiki\regulations\cn\GB 15084-2006.md",
    r"01_Wiki\regulations\cn\GB 4785-2006.md",
]

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")
# 灾难起点：附录 + 至少 2 个相同字母（AA / BB / ZZ）
DISASTER_RE = re.compile(r"附录\s*([A-Z])\1{1,}")


def fix_one(rel: str, dry_run: bool) -> dict:
    p = VAULT / rel
    result = {"file": rel, "status": "", "before_size": 0, "after_size": 0, "saved": 0}
    if not p.exists():
        result["status"] = "not_found"
        return result
    txt = p.read_text(encoding="utf-8", errors="replace")
    result["before_size"] = len(txt)

    mo = FM_RE.match(txt)
    if not mo:
        result["status"] = "no_fm"
        return result
    fm = yaml.safe_load(mo.group(1)) or {}
    body = txt[mo.end():]

    # 找「## 原文参考」位置（之后的内容是 MinerU 增补，要保留）
    mineru_section_pos = body.find("## 原文参考")

    # 找灾难起始点
    dis = DISASTER_RE.search(body)
    if not dis:
        result["status"] = "no_disaster"
        return result

    disaster_start = dis.start()

    # 如果灾难在 MinerU 段之后，不动 body 主体（说明灾难发生在 MinerU 段，可能是 OCR 噪声）
    if mineru_section_pos > 0 and disaster_start > mineru_section_pos:
        result["status"] = "disaster_in_mineru_section_skip"
        return result

    # 向前回溯到最近换行符 + 1（句子边界）
    cut_pos = body.rfind("\n", 0, disaster_start)
    if cut_pos < 0:
        cut_pos = disaster_start
    else:
        cut_pos = cut_pos + 1

    # 提取灾难段 → 截断 → 替换为说明 + 保留 MinerU 段
    healthy_body = body[:cut_pos].rstrip() + "\n"

    notice = (
        "\n"
        "> **⚠ 数据质量说明（2026-04-25 修复）**：\n"
        "> 本 note body 在 stage1 LLM 续抽（_continuation_passes）时陷入「附录 A、附录 AA、附录 AAA…」字母递增重复退化模式，"
        "原本可能延伸 70+ KB 的无意义重复字符已被截断。\n"
        "> 完整的附录章节请查阅原始 PDF（见 `source_pdf` 字段）或下方「原文参考（MinerU 云解析）」段。\n"
        "\n"
    )

    # 如果 MinerU 段在灾难之后，保留 MinerU 段
    if mineru_section_pos > disaster_start:
        # 找 MinerU 段在原 body 的实际起始（不在 disaster 段之后位置）
        # 注意：body[mineru_section_pos:] 是从 ## 原文参考 起到尾
        mineru_part = body[mineru_section_pos:]
        new_body = healthy_body + notice + mineru_part
    else:
        new_body = healthy_body + notice

    # 加 FM 标记
    fm["_data_quality"] = "llm_repetition_corrupted_truncated"
    fm["_data_quality_fixed_at"] = date.today().isoformat()
    fm["_data_quality_note"] = "stage1 LLM 续抽时陷入「附录 A→AA→AAA」字母递增重复退化，已截断"

    new_fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    new_text = f"---\n{new_fm_str}---\n\n{new_body.lstrip()}"
    if not new_text.endswith("\n"):
        new_text += "\n"

    result["after_size"] = len(new_text)
    result["saved"] = result["before_size"] - result["after_size"]

    if dry_run:
        result["status"] = "dry_run_ok"
    else:
        p.write_text(new_text, encoding="utf-8")
        result["status"] = "fixed"
    return result


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"\n{'='*72}")
    print(f"  修复 LLM 字母递增重复退化 · {len(TARGETS)} 条")
    print(f"{'='*72}\n")
    total_saved = 0
    for rel in TARGETS:
        r = fix_one(rel, args.dry_run)
        if r["status"] in ("fixed", "dry_run_ok"):
            print(f"  ✓ {r['file']}")
            print(f"    before: {r['before_size']:,} → after: {r['after_size']:,}  (saved {r['saved']:,} bytes)")
            total_saved += r["saved"]
        else:
            print(f"  · {r['file']}: {r['status']}")
    print(f"\n  累计删减: {total_saved:,} bytes ({total_saved/1024:.1f} KB)")
    if args.dry_run:
        print(f"  [DRY-RUN] 未写入")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
