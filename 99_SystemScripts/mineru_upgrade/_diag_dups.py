"""临时诊断：5 条 _dup 文件 + canonical 状态比对"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")
m = json.loads(MANIFEST.read_text(encoding="utf-8"))
manifest_paths = {
    r["path"].replace("\\", "/"): h
    for h, r in m["records"].items() if r.get("path")
}

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")


def info(p: Path) -> dict:
    """返回 note 的 FM 关键字段 + body 长度"""
    if not p.exists():
        return {"exists": False}
    txt = p.read_text(encoding="utf-8", errors="replace")
    mo = FM_RE.match(txt)
    if not mo:
        return {"exists": True, "no_fm": True, "body_len": len(txt)}
    try:
        fm = yaml.safe_load(mo.group(1)) or {}
    except Exception:
        return {"exists": True, "bad_fm": True, "body_len": len(txt)}
    body = txt[mo.end():]
    sp = (fm.get("source_pdf") or fm.get("source_file") or "").replace("\\", "/")
    h = manifest_paths.get(sp)
    return {
        "exists": True,
        "body_len": len(body),
        "reg_id": fm.get("reg_id"),
        "title": (fm.get("title") or "")[:80],
        "region": fm.get("region"),
        "source_pdf": sp,
        "conf": fm.get("cross_check_overall_confidence"),
        "_ocr_upgraded": fm.get("_ocr_upgraded"),
        "manifest_hash": h[:16] if h else "MISSING",
    }


dup_pairs = [
    (r"ece\ECE R125_dup1.md",          r"ece\ECE R125.md"),
    (r"ece\ECE R127_dup1.md",          r"ece\ECE R127.md"),
    (r"ece\ECE R135_dup1.md",          r"ece\ECE R135.md"),
    (r"ece\ECE R144_dup1.md",          r"ece\ECE R144.md"),
    (r"eu\(EU) 2018 858_dup1.md",      r"eu\(EU) 2018 858.md"),
]

for dup_rel, can_rel in dup_pairs:
    print(f"\n{'='*72}")
    print(f"  对比: {dup_rel}")
    print(f"{'='*72}")
    print("\n[DUP]")
    di = info(WIKI / dup_rel)
    for k, v in di.items():
        print(f"  {k}: {v}")
    print("\n[CANONICAL]")
    ci = info(WIKI / can_rel)
    for k, v in ci.items():
        print(f"  {k}: {v}")
