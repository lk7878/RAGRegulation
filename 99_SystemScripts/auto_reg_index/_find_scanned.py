"""列出需要 Baidu OCR 处理的扫描件记录。"""
import json
from pathlib import Path

mf = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")
data = json.loads(mf.read_text(encoding="utf-8"))

pending_ocr = []
failed_ocr = []
for h, r in data["records"].items():
    state = r.get("state")
    err = r.get("error") or ""
    if state in ("pending",):
        pending_ocr.append((h, r))
    elif state in ("ocr_failed", "failed") or "empty" in err.lower() or "scan" in err.lower():
        failed_ocr.append((h, r))

print(f"pending state: {len(pending_ocr)}")
print(f"failed/empty OCR state: {len(failed_ocr)}")

# 按 size 排序
failed_ocr.sort(key=lambda x: x[1].get("size_bytes", 0) or 0)

print("\nsmallest 10 failed (candidates for Baidu OCR test):")
for h, r in failed_ocr[:10]:
    sz_kb = (r.get("size_bytes") or 0) // 1024
    path = str(r.get("path", ""))[:70]
    print(f"  {sz_kb:6}KB  hash={h[:8]}  {path}")

print("\nlargest 5 failed (cost warning):")
for h, r in failed_ocr[-5:]:
    sz_kb = (r.get("size_bytes") or 0) // 1024
    path = str(r.get("path", ""))[:70]
    print(f"  {sz_kb:6}KB  hash={h[:8]}  {path}")

# 统计所有 state
from collections import Counter
state_cnt = Counter(r.get("state") for r in data["records"].values())
print("\nall states:")
for s, c in state_cnt.most_common():
    print(f"  {s}: {c}")
