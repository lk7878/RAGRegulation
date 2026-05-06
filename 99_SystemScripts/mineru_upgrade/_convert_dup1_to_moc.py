"""
_convert_dup1_to_moc.py — 把 (EU) 2018 858_dup1.md 转化为 EU 法规目录 MOC

操作：
  1. 改 FM：reg_id → 'EU Tech Directives Index', type → 'type/index', title/scope 重写
  2. 删除针对原 reg_id 的 cross_check_flags
  3. 保留 body 全部内容（已结构化目录）
  4. 重命名文件 → 'EU Tech Directives Index.md'
  5. 更新 type_approval_general MOC 里的 wikilink
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
EU_DIR = VAULT / "01_Wiki" / "regulations" / "eu"
OLD_PATH = EU_DIR / "(EU) 2018 858_dup1.md"
NEW_PATH = EU_DIR / "EU Tech Directives Index.md"

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")


def main() -> int:
    if not OLD_PATH.exists():
        print(f"[ERROR] 源文件不存在: {OLD_PATH}")
        return 1
    if NEW_PATH.exists():
        print(f"[ERROR] 目标文件已存在: {NEW_PATH}")
        return 1

    txt = OLD_PATH.read_text(encoding="utf-8")
    mo = FM_RE.match(txt)
    if not mo:
        print("[ERROR] 缺 FM")
        return 1

    body = txt[mo.end():]
    today = date.today().isoformat()

    # 新 FM —— 完全重写为 MOC 类型
    new_fm = {
        "reg_id": "EU Tech Directives Index",
        "region": "eu",
        "type": "type/index",
        "title": "欧盟汽车技术法规与指令目录索引",
        "scope": "汇集 (EU) 2018/858 框架下及历史相关的欧盟汽车技术法规和指令目录，包含 60+ 条记录，按 topic 分组（环境保护 / 主动安全 / 被动安全 / 灯光信号 / 其它）。每条含 reg_id、标题、状态、发布机构、简短 summary。",
        "language": "zh",
        "source_pdf": "国外法规\\1.欧盟\\（欧标）欧洲联盟汽车技术指令.pdf",
        "tags": [
            "type/index",
            "region/eu",
            "topic/regulation_directory",
        ],
        # 保留 MinerU 来源信息
        "_ocr_upgraded": "mineru",
        "_mineru_content_hash": "090866a520e703fe",
        "_mineru_outputs_dir": "outputs/090866a520e703fe",
        "_mineru_blocks": {"tables": 10, "formulas": 0, "images": 0},
        "_mineru_merged_at": "2026-04-22",
        # 转换溯源
        "_converted_from": "(EU) 2018 858_dup1.md",
        "_converted_to_moc_at": today,
        "_converted_reason": "原文件本质是 EU 法规目录索引，含 60+ 个 reg_id 元数据条目（无单一法规 body），不适合作为单一 reg_id 的 note。",
    }

    new_fm_str = yaml.safe_dump(new_fm, allow_unicode=True, sort_keys=False)
    new_text = f"---\n{new_fm_str}---\n\n# 欧盟汽车技术法规与指令目录索引\n\n> **说明**：本目录由 `(EU) 2018 858_dup1.md` 转化而来。原文件 reg_id 标注为 (EU) 2018/858，实际内容是 (EU) 2018/858 框架下及历史相关欧盟法规/指令的元数据汇编（60+ 条），不是单一法规原文。\n>\n> 每条记录格式：YAML 块 + 相关法规修订本列表。条目按 topic 分组。\n\n{body}"
    if not new_text.endswith("\n"):
        new_text += "\n"

    # 写新文件
    NEW_PATH.write_text(new_text, encoding="utf-8")
    print(f"✓ 写新文件: {NEW_PATH.name}  ({len(new_text)} 字符)")

    # 删原文件
    OLD_PATH.unlink()
    print(f"✓ 删原文件: {OLD_PATH.name}")

    # 更新 wikilink
    topic_md = VAULT / "01_Wiki" / "04_Topics" / "type_approval_general - 总体型式认证 · 通用要求.md"
    if topic_md.exists():
        t = topic_md.read_text(encoding="utf-8")
        old_link_re = re.compile(r"\[\[\(EU\) 2018 858_dup1(\||\])")
        cnt = len(old_link_re.findall(t))
        if cnt > 0:
            t_new = old_link_re.sub(r"[[EU Tech Directives Index\1", t)
            topic_md.write_text(t_new, encoding="utf-8")
            print(f"✓ 更新 wikilink: {topic_md.name} ({cnt} 处)")
        else:
            print(f"  (no wikilink found in {topic_md.name})")
    else:
        print(f"[WARN] topic 文件不存在: {topic_md}")

    print("\n[DONE]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
