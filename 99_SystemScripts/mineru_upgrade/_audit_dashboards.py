"""审视 10 个非主 dashboards 是否含过时数字"""
import re, sys
from pathlib import Path
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\CcVault\00_Dashboards")
for p in sorted(ROOT.glob("*.md")):
    if p.name in ("_Dashboards MOC.md", "_MinerU_Upgrades.md"):
        continue
    txt = p.read_text(encoding="utf-8")
    issues = []
    if re.search(r"\b1444\b", txt):
        issues.append("含 1444（应 1414）")
    if re.search(r"\b1416\b", txt):
        issues.append("含 1416")
    if re.search(r"\b1417\b", txt):
        issues.append("含 1417")
    if re.search(r"updated:\s*2026-04-2[0-3]\b", txt):
        issues.append("updated 是 04-20~23")
    if re.search(r"updated:\s*2026-0[123]", txt):
        issues.append("updated 比 04 还旧")
    # 提取头部前几行说明
    head = "\n".join(txt.split("\n")[:12])
    print(f"\n=== {p.name} ===")
    if issues:
        print(f"  ⚠ {' / '.join(issues)}")
    else:
        print(f"  ✓ 数字 OK")
    # 简短头部摘要
    for line in head.split("\n"):
        line = line.strip()
        if line.startswith("#") or "条" in line or "updated" in line.lower():
            print(f"  | {line[:80]}")
