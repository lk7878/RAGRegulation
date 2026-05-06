"""画像 102 条 mineru_not_run notes：分析 type / size / 性质"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
RAW = Path(r"D:\CcVault\00_Raw\标准库")
STATE = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_state.json")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")

state = json.loads(STATE.read_text(encoding="utf-8"))
m = json.loads(MANIFEST.read_text(encoding="utf-8"))
manifest_fwd = {r["path"].replace("\\", "/"): h for h, r in m["records"].items() if r.get("path")}
done_hash = set(state["done"].keys())
failed_hash = set(state.get("failed", {}).keys())

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

candidates: list[dict] = []
for p in WIKI.rglob("*.md"):
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    mo = FM_RE.match(txt)
    if not mo:
        continue
    try:
        fm = yaml.safe_load(mo.group(1)) or {}
    except yaml.YAMLError:
        continue
    if fm.get("_ocr_upgraded") in ("mineru", "mineru_split", "mineru_no_assets"):
        continue
    sp = (fm.get("source_pdf") or fm.get("source_file") or "").replace("\\", "/")
    if not sp:
        candidates.append({"name": p.name, "type": fm.get("type", "?"), "reason": "no_source_pdf",
                           "source": "", "size_mb": 0, "title": fm.get("title", "")[:60]})
        continue
    h = manifest_fwd.get(sp)
    if not h or h not in done_hash:
        # 真没跑
        # 试着找 raw 文件 size
        raw_path = RAW / sp.replace("/", "\\")
        size_mb = 0.0
        if raw_path.exists():
            size_mb = raw_path.stat().st_size / (1024 * 1024)
        # 检查在 failed 里
        in_failed = h in failed_hash if h else False
        candidates.append({
            "name": p.name,
            "type": fm.get("type", "?"),
            "reason": "in_failed" if in_failed else "not_in_state",
            "source": sp[-80:],
            "size_mb": round(size_mb, 1),
            "title": (fm.get("title") or "")[:60],
        })

# 统计
print(f"\n{'='*72}")
print(f"  102 条 not_run 画像")
print(f"{'='*72}")
print(f"  总数: {len(candidates)}")

# 按 type
type_cnt = Counter(c["type"] for c in candidates)
print(f"\n  按 type 分布:")
for t, n in type_cnt.most_common():
    print(f"    {n:>3}  {t}")

# 按 reason
reason_cnt = Counter(c["reason"] for c in candidates)
print(f"\n  按原因:")
for r, n in reason_cnt.most_common():
    print(f"    {n:>3}  {r}")

# 按 size 桶
size_buckets = Counter()
for c in candidates:
    s = c["size_mb"]
    if s == 0:
        size_buckets["unknown"] += 1
    elif s < 1:
        size_buckets["<1MB"] += 1
    elif s < 5:
        size_buckets["1-5MB"] += 1
    elif s < 10:
        size_buckets["5-10MB"] += 1
    else:
        size_buckets[">10MB"] += 1
print(f"\n  按 size:")
for b in [">10MB", "5-10MB", "1-5MB", "<1MB", "unknown"]:
    print(f"    {size_buckets[b]:>3}  {b}")

# 可跑（size <10MB 且非综述类）的具体列表
print(f"\n  可跑候选（size<10MB 且 type 是 amendment/version/regulation）前 20:")
runnable = [c for c in candidates if c["size_mb"] > 0 and c["size_mb"] < 10
            and c["type"] in ("type/amendment", "type/version", "type/regulation")]
for c in runnable[:20]:
    print(f"    [{c['size_mb']:>4} MB]  {c['name']:<35}  type={c['type']}")
print(f"\n  可跑候选总数: {len(runnable)}")

# 大件 >10MB
big = [c for c in candidates if c["size_mb"] >= 10]
print(f"\n  >10MB 大件（被 size filter 跳过）: {len(big)}")
for c in big[:10]:
    print(f"    [{c['size_mb']:>5} MB]  {c['name']:<35}  type={c['type']}")
