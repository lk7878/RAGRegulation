"""扫描全 vault 里的伪图 markdown：![...](图X描述...) 模式。"""
from __future__ import annotations
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

# 伪图 pattern：src 以"图"开头，不是真实文件路径
# 真图 src 形如 "../_mineru_assets/..." 或 "http..."
FAKE_IMG_RE = re.compile(r"!\[([^\]]*)\]\((图[^)]*)\)")

per_note: dict[str, int] = {}
total_hits = 0
all_srcs: Counter[str] = Counter()

for p in WIKI.rglob("*.md"):
    if "_mineru_assets" in str(p):
        continue
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    hits = FAKE_IMG_RE.findall(txt)
    if hits:
        per_note[p.name] = len(hits)
        total_hits += len(hits)
        for alt, src in hits:
            all_srcs[src[:30]] += 1

print(f"发现伪图总引用: {total_hits}")
print(f"涉及 notes: {len(per_note)}")
print()

print("=== Top 20 notes (按伪图数量) ===")
for name, n in sorted(per_note.items(), key=lambda x: -x[1])[:20]:
    print(f"  {n:>3}  {name}")

print()
print("=== 伪图 src 样本分布（前缀 30 字符，Top 10） ===")
for src, n in all_srcs.most_common(10):
    print(f"  {n:>3}  {src}")
