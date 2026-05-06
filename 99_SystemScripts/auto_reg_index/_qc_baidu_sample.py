"""专门抽样百度 OCR 处理过的 notes 做 QC 比对。"""
import json
import random
import yaml
from pathlib import Path

ROOT = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index")
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
STAGING = ROOT / ".staging"

# 从 manifest 找 layer_used=baidu 的 ocr_meta
baidu_hashes = []
for ocr_meta in STAGING.rglob("ocr_meta.yaml"):
    try:
        m = yaml.safe_load(ocr_meta.read_text(encoding="utf-8"))
        if m.get("layer_used") == "baidu":
            baidu_hashes.append(ocr_meta.parent.name)
    except Exception:
        continue

print(f"Baidu OCR-processed: {len(baidu_hashes)} staging dirs")

# 从 manifest 找对应的 wiki note
mf = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
note_by_src = {}
for p in WIKI.rglob("*.md"):
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
        end = txt.find("\n---", 4)
        fm = yaml.safe_load(txt[4:end]) or {}
        src = (fm.get("source_pdf") or "").replace("\\", "/").lstrip("/")
        if src:
            note_by_src[src] = (p, fm)
    except Exception:
        continue

baidu_notes = []
for h in baidu_hashes:
    rec = mf["records"].get(h)
    if not rec:
        continue
    src = rec.get("path", "").replace("\\", "/").lstrip("/")
    if src in note_by_src:
        baidu_notes.append((h, note_by_src[src]))

print(f"Baidu notes matched: {len(baidu_notes)}")

# 随机抽 5 个
random.seed(1)
samples = random.sample(baidu_notes, min(5, len(baidu_notes)))

for h, (note_path, fm) in samples:
    print(f"\n{'='*70}")
    print(f"=== {note_path.parent.name}/{note_path.name} ===")
    for k in ("reg_id", "title", "type", "region", "status", "publication_date", "standard_body"):
        v = fm.get(k)
        vs = repr(v) if v else "—"
        if len(vs) > 90:
            vs = vs[:87] + "...'"
        print(f"  {k:18}: {vs}")

    # 展示 OCR 源片段
    raw_md = STAGING / h[:2] / h / "raw.md"
    if raw_md.exists():
        text = raw_md.read_text(encoding="utf-8", errors="replace").strip()
        print(f"\n  BAIDU OCR (first 400 chars):")
        for line in text[:400].split("\n")[:10]:
            print(f"  > {line[:120]}")
