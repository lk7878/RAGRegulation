"""扫描 vault 里有没有指向 5 条 _dup 文件 / 对应 canonical 的 wikilink"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(r"D:\CcVault")
TARGETS = ["ECE R125", "ECE R127", "ECE R135", "ECE R144", "(EU) 2018 858"]

results: dict[str, dict] = defaultdict(lambda: {"canonical_links": [], "dup_links": []})

for target in TARGETS:
    canon_re = re.compile(rf"\[\[{re.escape(target)}(\||\])")
    dup_re = re.compile(rf"\[\[{re.escape(target)}_dup\d*(\||\])")
    for p in VAULT.rglob("*.md"):
        sp = str(p).lower()
        if ".trash" in sp or "trash_dups" in sp:
            continue
        # 跳过 _dup 文件自身（避免计入"自引用"的内部链接）
        if p.name == f"{target}_dup1.md" or p.name == f"{target}_dup.md":
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if canon_re.search(txt):
            results[target]["canonical_links"].append(p.name)
        if dup_re.search(txt):
            results[target]["dup_links"].append(p.name)

print("=" * 72)
print("  Wikilink 引用扫描（不含 _dup 文件自身）")
print("=" * 72)
for target in TARGETS:
    r = results[target]
    print(f"\n● {target}")
    print(f"  [[{target}]] 引用 (canonical 形式):  {len(r['canonical_links'])} 处")
    for n in r["canonical_links"][:5]:
        print(f"    · {n}")
    if len(r["canonical_links"]) > 5:
        print(f"    ... 还有 {len(r['canonical_links']) - 5}")
    print(f"  [[{target}_dup1]] 引用 (dup 形式):    {len(r['dup_links'])} 处")
    for n in r["dup_links"][:5]:
        print(f"    · {n}")
