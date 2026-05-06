import re, yaml, sys
from pathlib import Path
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
for p in WIKI.rglob("3.2024*"):
    txt = p.read_text(encoding="utf-8")
    mo = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n", txt)
    fm = yaml.safe_load(mo.group(1)) if mo else {}
    print(f"file: {p}")
    print(f"  reg_id: {fm.get('reg_id')!r}")
    print(f"  title:  {fm.get('title')!r}")
    print(f"  type:   {fm.get('type')!r}")
    print(f"  body_len: {len(txt[mo.end():]) if mo else 0}")
