"""Day summary stats — 汇总 MinerU 升级通道累计成果。"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from datetime import date

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade")
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

state = json.loads((ROOT / "_mineru_state.json").read_text(encoding="utf-8"))
done = state["done"]
today = date.today().isoformat()
used = state["daily_pages_used"].get(today, 0)

print(f"累计 MinerU 处理 PDFs: {len(done)} / 1444 ({len(done)*100//1444}%)")
print(f"今日消耗页数: {used} / 2000 ({used*100//2000}%)")
print(f"今日剩余配额: {2000 - used}")

upgraded = 0
total_t = total_f = total_i = 0
body_grew_10x = 0
top = []
for p in WIKI.rglob("*.md"):
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    m = FM_RE.match(txt)
    if not m:
        continue
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        continue
    if fm.get("_ocr_upgraded") == "mineru":
        upgraded += 1
        b = fm.get("_mineru_blocks", {})
        t, f, i = b.get("tables", 0), b.get("formulas", 0), b.get("images", 0)
        total_t += t
        total_f += f
        total_i += i
        top.append((t + f + i, fm.get("reg_id", p.name), t, f, i))

top.sort(reverse=True)
print(f"\n=== Day 1 合并总成果 ===")
print(f"已升级 notes: {upgraded}")
print(f"  累计表格: {total_t}")
print(f"  累计公式: {total_f}")
print(f"  累计图像: {total_i}")
print(f"\nTop 10 含元素最多的升级：")
for total, rid, t, f, i in top[:10]:
    print(f"  {rid:<30} tables={t:>2}  formulas={f:>2}  images={i:>2}")

# 估算全量剩余时间
if len(done) > 0 and used > 0:
    pages_per_pdf = used / len(done)
    print(f"\n=== 剩余估算 ===")
    print(f"均页/PDF: {pages_per_pdf:.1f}")
    remaining_pdfs = 1444 - len(done)
    remaining_pages_est = int(remaining_pdfs * pages_per_pdf)
    days_at_2000 = (remaining_pages_est + 1999) // 2000
    print(f"剩余 {remaining_pdfs} PDFs ≈ {remaining_pages_est} 页")
    print(f"每日 2000 页配额 → 再约 {days_at_2000} 天完工")
