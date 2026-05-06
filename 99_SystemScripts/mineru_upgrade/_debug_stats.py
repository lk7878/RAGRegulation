"""Debug stats discrepancy."""
from pathlib import Path
import re
import yaml
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

p = WIKI / "ece" / "ECE R75 Rev2 Am2.md"
txt = p.read_text(encoding="utf-8", errors="replace")
m = FM_RE.match(txt)
print(f"FM match: {bool(m)}")
if m:
    fm_src = m.group(1)
    print(f"FM source length: {len(fm_src)}")
    print(f"FM source last 300 chars:")
    print(repr(fm_src[-300:]))
    try:
        fm = yaml.safe_load(fm_src)
        print(f"\nParsed type: {type(fm).__name__}")
        if fm:
            print(f"_ocr_upgraded key: {fm.get('_ocr_upgraded')}")
            print(f"_mineru_blocks: {fm.get('_mineru_blocks')}")
    except yaml.YAMLError as e:
        print(f"\nYAML error: {e}")

# 再对比全扫统计
print("\n=== 全扫 matched notes ===")
matched = 0
fm_fail = 0
upgraded = 0
for p in WIKI.rglob("*.md"):
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    m = FM_RE.match(txt)
    if not m:
        continue
    matched += 1
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        fm_fail += 1
        continue
    if not isinstance(fm, dict):
        continue
    if fm.get("_ocr_upgraded") == "mineru":
        upgraded += 1
print(f"总 notes: {matched}")
print(f"FM 解析失败: {fm_fail}")
print(f"_ocr_upgraded=mineru: {upgraded}")
