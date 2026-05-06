"""抽样 QC：跨 region 验证字段完整性。"""
import yaml, random
from pathlib import Path
from collections import Counter

wiki = Path(r"D:\CcVault\01_Wiki\regulations")
regions = ["cn", "ece", "eu", "jp", "us", "kr", "au", "br", "za"]
random.seed(42)
samples = []
for r in regions:
    d = wiki / r
    if not d.exists():
        continue
    files = [f for f in d.glob("*.md") if not f.name.startswith(".")]
    if not files:
        continue
    picked = random.sample(files, min(3, len(files)))
    samples.extend(picked)

schema_fields = ["reg_id", "title", "type", "region", "status"]
field_cnt = Counter()

for p in samples:
    txt = p.read_text(encoding="utf-8")
    end = txt.find("\n---", 4)
    fm = yaml.safe_load(txt[4:end]) or {}
    print(f"\n=== {p.parent.name}/{p.name} ===")
    for k in ("reg_id", "type", "region", "status"):
        print(f"  {k:11}: {fm.get(k)!r}")
    tags = fm.get("tags") or []
    print(f"  tags count : {len(tags)}")
    title = str(fm.get("title", ""))
    print(f"  title      : {title[:60]!r}{'...' if len(title) > 60 else ''}")
    missing = [f for f in schema_fields if f not in fm or not fm[f]]
    if missing:
        print(f"  !! MISSING : {missing}")
    for f in schema_fields:
        if f in fm and fm[f]:
            field_cnt[f] += 1

print(f"\n=== Field coverage ({len(samples)} sampled) ===")
for f in schema_fields:
    print(f"  {f}: {field_cnt[f]}/{len(samples)} ({100*field_cnt[f]//len(samples)}%)")
