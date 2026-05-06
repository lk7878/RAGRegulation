"""OCR 完成后的报告：成功率、失败原因、扫描件 vs 电子版、每 region 统计。"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, r"D:\CcVault\99_SystemScripts\auto_reg_index")
from manifest import Manifest

mf = Manifest.load_or_create()
all_recs = list(mf.records.values())

# State breakdown
states = Counter(r.state for r in all_recs)
print("=== State breakdown ===")
for s, c in sorted(states.items(), key=lambda x: -x[1]):
    print(f"  {c:5}  {s}")

# Failed reasons
failed = [r for r in all_recs if r.state == "failed"]
print(f"\n=== Failed files ({len(failed)}) ===")
reasons: defaultdict[str, int] = defaultdict(int)
for r in failed:
    err = r.error or "no error msg"
    if "Likely scanned PDF" in err:
        reasons["scan (pdfplumber sparse)"] += 1
    elif "MinerU" in err or "magic-pdf" in err:
        reasons["scan (MinerU not installed)"] += 1
    elif "baidu" in err.lower():
        reasons["scan (baidu not configured)"] += 1
    elif "All OCR layers failed" in err:
        reasons["scan (all layers failed)"] += 1
    elif "not found" in err.lower():
        reasons["file missing"] += 1
    else:
        reasons[f"other: {err[:60]}"] += 1
for r, c in sorted(reasons.items(), key=lambda x: -x[1])[:20]:
    print(f"  {c:5}  {r}")

# Region breakdown of ocr_done
ocr_done = [r for r in all_recs if r.state == "ocr_done"]
print(f"\n=== OCR succeeded by top-dir ({len(ocr_done)}) ===")
by_top = Counter()
for r in ocr_done:
    top = r.path.replace("\\", "/").split("/")[0]
    by_top[top] += 1
for t, c in by_top.most_common():
    print(f"  {c:5}  {t}")

# Sizes of ocr_done raw.md
print(f"\n=== Raw.md size distribution ===")
STAGING = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.staging")
sizes = []
for r in ocr_done:
    p = STAGING / r.content_hash[:2] / r.content_hash / "raw.md"
    if p.exists():
        sizes.append(p.stat().st_size)
if sizes:
    sizes.sort()
    print(f"  count: {len(sizes)}")
    print(f"  min:   {sizes[0]:>10,} bytes")
    print(f"  p50:   {sizes[len(sizes)//2]:>10,} bytes")
    print(f"  p90:   {sizes[int(len(sizes)*0.9)]:>10,} bytes")
    print(f"  max:   {sizes[-1]:>10,} bytes")
    print(f"  sum:   {sum(sizes):>10,} bytes = {sum(sizes)/1024/1024:.1f} MB")
    # Estimate extract cost
    # 中文 ~3 bytes/token, 英文 ~4 bytes/token. Use 3.5 as average.
    input_tokens = sum(sizes) / 3.5
    # Output ~20% of input
    output_tokens = input_tokens * 0.2
    # DeepSeek V3: $0.27/Mtok input, $1.10/Mtok output
    cost = input_tokens * 0.27 / 1e6 + output_tokens * 1.10 / 1e6
    print(f"\n  est. extract cost: ${cost:.2f} USD ≈ ¥{cost*7.2:.0f}")
