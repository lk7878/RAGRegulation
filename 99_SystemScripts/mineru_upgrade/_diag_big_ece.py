"""查 6 条大件 ECE 法规的实际路径和页数"""
import json, sys
from pathlib import Path
import pypdf

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
RAW = Path(r"D:\CcVault\00_Raw\标准库")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")

import re, yaml
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

targets = ["ECE R44", "ECE R46", "ECE R48", "ECE R49", "ECE R99", "ECE R115"]

for p in WIKI.rglob("*.md"):
    if p.stem in targets:
        txt = p.read_text(encoding="utf-8", errors="replace")
        mo = FM_RE.match(txt)
        if not mo: continue
        try: fm = yaml.safe_load(mo.group(1)) or {}
        except: continue
        sp = fm.get("source_pdf") or fm.get("source_file") or ""
        # 拼路径
        raw = RAW / sp.replace("/", "\\")
        if not raw.exists():
            print(f"{p.stem:<10} sp={sp!r}  NOT FOUND")
            continue
        try:
            n = len(pypdf.PdfReader(str(raw)).pages)
            size = raw.stat().st_size / 1024 / 1024
            print(f"{p.stem:<10} {n:>4}p  {size:>5.1f}MB  reg_id={fm.get('reg_id')!r}")
            print(f"    path: {sp}")
        except Exception as e:
            print(f"{p.stem:<10} ERROR: {e}")
