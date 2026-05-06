"""全量 QC：扫描全部 01_Wiki notes，统计 schema 字段覆盖率 + 异常值。"""
import yaml
from pathlib import Path
from collections import Counter, defaultdict

wiki = Path(r"D:\CcVault\01_Wiki\regulations")

schema_fields = ["reg_id", "title", "type", "region", "status"]
recommended_fields = ["publication_date", "source_pdf", "tags", "scope"]

field_cnt = Counter()
rec_cnt = Counter()
region_cnt = Counter()
status_cnt = Counter()
type_cnt = Counter()

parse_errors = []
total = 0
reg_id_empty = []
reg_id_looks_bad = []

for p in wiki.rglob("*.md"):
    if p.name == ".gitkeep":
        continue
    total += 1
    try:
        txt = p.read_text(encoding="utf-8")
        end = txt.find("\n---", 4)
        fm = yaml.safe_load(txt[4:end]) or {}
    except Exception as e:
        parse_errors.append((p.name, str(e)[:80]))
        continue

    for f in schema_fields:
        if f in fm and fm[f] not in (None, "", []):
            field_cnt[f] += 1
    for f in recommended_fields:
        if f in fm and fm[f] not in (None, "", []):
            rec_cnt[f] += 1

    region_cnt[fm.get("region")] += 1
    status_cnt[fm.get("status")] += 1
    type_cnt[fm.get("type")] += 1

    rid = fm.get("reg_id")
    if not rid:
        reg_id_empty.append(p.name)
    elif isinstance(rid, str):
        # Signals of "bad" reg_id (raw PDF stem still not canonicalized)
        if rid.endswith("_upload_") or "_upload_" in rid:
            reg_id_looks_bad.append((p.name, rid))
        elif rid.startswith("R") and rid[1:5].isdigit() and rid.endswith("e"):
            reg_id_looks_bad.append((p.name, rid))

print(f"Total notes scanned: {total}")
print(f"Parse errors: {len(parse_errors)}")
if parse_errors[:3]:
    for pn, err in parse_errors[:3]:
        print(f"  - {pn}: {err}")

print(f"\n=== Schema field coverage ===")
for f in schema_fields:
    pct = 100 * field_cnt[f] // total if total else 0
    print(f"  {f:11}: {field_cnt[f]:4}/{total} ({pct}%)")

print(f"\n=== Recommended field coverage ===")
for f in recommended_fields:
    pct = 100 * rec_cnt[f] // total if total else 0
    print(f"  {f:19}: {rec_cnt[f]:4}/{total} ({pct}%)")

print(f"\n=== Region distribution ===")
for r, n in region_cnt.most_common():
    print(f"  {str(r):14}: {n}")

print(f"\n=== Status distribution ===")
for s, n in status_cnt.most_common():
    print(f"  {str(s):18}: {n}")

print(f"\n=== Type distribution ===")
for t, n in type_cnt.most_common():
    print(f"  {str(t):30}: {n}")

print(f"\n=== reg_id issues ===")
print(f"  empty reg_id: {len(reg_id_empty)}")
for pn in reg_id_empty[:5]:
    print(f"    - {pn}")
print(f"  looks-bad reg_id: {len(reg_id_looks_bad)}")
for pn, rid in reg_id_looks_bad[:5]:
    print(f"    - {pn} -> {rid!r}")
