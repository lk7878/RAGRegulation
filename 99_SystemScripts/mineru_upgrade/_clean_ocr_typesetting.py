"""
_clean_ocr_typesetting.py — 清理 OCR 排版残留（连续空格 / 省略号 / 点号等）

诊断时发现 50+ notes body 含 30+ 连续相同非字母字符，主要是：
  - 连续空格（章节标题与页码间留白）
  - 连续 `…`（目录省略号）
  - 连续 `.` `·` `-` `_`（章节分隔/装饰）

策略（保守清理，只清"明显排版残留"）：
  1. 跳过 FM
  2. 跳过 markdown 代码块（```...``` 内）
  3. 跳过 markdown 表格行（含 `|`）
  4. 跳过 HTML 表格（<table> 内）
  5. 把连续 8+ 个 `空格 / … / · / . / - / _` 压缩为 3 个相同字符 + 单空格
  6. 字母连续 30+ 不动（应由 _fix_llm_alphabet_repetition.py 处理）
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
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

# 需清理的字符（连续 8+）
CLEAN_CHARS = [" ", "\u3000", "…", "·", "．", ".", "-", "_", "—"]
CLEAN_PATTERN = re.compile(
    r"([ \u3000…·．\.\-_—])\1{7,}"
)

# 跳过的范围：代码块、HTML 表格、markdown 表格
CODE_BLOCK_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)
HTML_TABLE_RE = re.compile(r"<table[\s\S]*?</table>", re.MULTILINE | re.IGNORECASE)


def clean_body(body: str) -> tuple[str, int]:
    """清理 body，返回 (新 body, 替换计数)"""
    # 1. 把所有需保护的段落（代码块、HTML 表格、markdown 表行）用占位符替换
    placeholders: list[str] = []
    def stash(m):
        idx = len(placeholders)
        placeholders.append(m.group(0))
        return f"\x00PLACEHOLDER_{idx}\x00"

    # 代码块
    body = CODE_BLOCK_RE.sub(stash, body)
    # HTML 表格
    body = HTML_TABLE_RE.sub(stash, body)
    # markdown 表格行（以 | 开始或含 | 的行）
    md_table_lines = []
    new_lines = []
    for line in body.split("\n"):
        if "|" in line and line.strip().startswith(("|", "- |", "* |")) or re.match(r"^\s*\|.*\|\s*$", line):
            idx = len(placeholders)
            placeholders.append(line)
            new_lines.append(f"\x00PLACEHOLDER_{idx}\x00")
        else:
            new_lines.append(line)
    body = "\n".join(new_lines)

    # 2. 清理连续重复字符
    count = 0
    def shrink(m):
        nonlocal count
        ch = m.group(1)
        count += 1
        # 空格压成 1 个空格；其他装饰字符压成 3 个相同字符
        if ch in (" ", "\u3000"):
            return " "
        return ch * 3

    body = CLEAN_PATTERN.sub(shrink, body)

    # 3. 还原占位符
    def restore(m):
        idx = int(m.group(1))
        return placeholders[idx]
    body = re.sub(r"\x00PLACEHOLDER_(\d+)\x00", restore, body)

    return body, count


def fix_one(p: Path, dry_run: bool) -> dict:
    result = {"file": str(p.relative_to(VAULT)), "before_size": 0, "after_size": 0,
              "replacements": 0, "status": ""}
    txt = p.read_text(encoding="utf-8", errors="replace")
    result["before_size"] = len(txt)

    mo = FM_RE.match(txt)
    if not mo:
        result["status"] = "no_fm"
        return result
    fm_str = txt[:mo.end()]
    body = txt[mo.end():]

    new_body, count = clean_body(body)
    result["replacements"] = count
    if count == 0:
        result["status"] = "clean_already"
        return result

    new_text = fm_str + new_body
    result["after_size"] = len(new_text)

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
    ap.add_argument("--limit", type=int, default=0, help="只处理前 N 条")
    args = ap.parse_args()

    # 扫描所有受影响 notes（含 30+ 连续非字母字符）
    targets: list[Path] = []
    for sub in ["01_Wiki", "02_Wiki"]:
        for p in (VAULT / sub).rglob("*.md"):
            try:
                txt = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            mo = FM_RE.match(txt)
            body = txt[mo.end():] if mo else txt
            # 找连续 8+ 排版字符
            if CLEAN_PATTERN.search(body):
                targets.append(p)

    print(f"\n{'='*72}")
    print(f"  扫描到 {len(targets)} 条 notes 含排版残留")
    print(f"{'='*72}\n")

    if args.limit:
        targets = targets[:args.limit]

    fixed = 0
    total_before = 0
    total_after = 0
    total_repl = 0
    for p in targets:
        r = fix_one(p, args.dry_run)
        if r["status"] in ("fixed", "dry_run_ok"):
            fixed += 1
            total_before += r["before_size"]
            total_after += r["after_size"]
            total_repl += r["replacements"]
            saved = r["before_size"] - r["after_size"]
            print(f"  ✓ {r['file']:<55}  {r['replacements']:>3} 替换  "
                  f"{r['before_size']:>6} → {r['after_size']:>6}  (-{saved})")
        elif r["status"] == "clean_already":
            pass  # 不打印
        else:
            print(f"  · {r['file']}: {r['status']}")

    saved_total = total_before - total_after
    print(f"\n  处理: {fixed} / {len(targets)}")
    print(f"  替换计数: {total_repl}")
    print(f"  字节节省: {saved_total:,} ({saved_total/1024:.1f} KB)")
    if args.dry_run:
        print(f"  [DRY-RUN] 未写入")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
