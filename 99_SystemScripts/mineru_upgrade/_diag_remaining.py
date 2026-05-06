"""画像剩余 21 条 not_run 的具体 fail 原因"""
import json, re, sys
from pathlib import Path
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
failed_state = state.get("failed", {})

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

print(f"\n{'='*72}")
print(f"  剩余 21 条 not_run 详细画像")
print(f"{'='*72}\n")

candidates = []
for p in WIKI.rglob("*.md"):
    try: txt = p.read_text(encoding="utf-8", errors="replace")
    except: continue
    mo = FM_RE.match(txt)
    if not mo: continue
    try: fm = yaml.safe_load(mo.group(1)) or {}
    except: continue
    if fm.get("_ocr_upgraded") in ("mineru", "mineru_split", "mineru_no_assets"):
        continue
    sp = (fm.get("source_pdf") or fm.get("source_file") or "").replace("\\", "/")
    if not sp:
        candidates.append({"name": p.name, "sp": "", "h": "", "fail": ""})
        continue
    h = manifest_fwd.get(sp)
    raw = RAW / sp.replace("/", "\\")
    size = round(raw.stat().st_size / 1024 / 1024, 1) if raw.exists() else 0
    fail_info = failed_state.get(h, {}) if h else {}
    candidates.append({
        "name": p.name, "size": size, "h": (h or "")[:16],
        "fail_reason": fail_info.get("error", "") or fail_info.get("reason", ""),
        "fail_status": fail_info.get("status", ""),
        "in_state": "done" if h in done_hash else ("failed" if h in failed_state else "not_run"),
    })

# 按 in_state 分组
by_state = {"failed": [], "not_run": [], "done_but_not_upgraded": []}
for c in candidates:
    by_state.setdefault(c["in_state"], []).append(c)

print(f"--- 在 state.failed 里 ({len(by_state['failed'])} 条) ---")
for c in by_state["failed"]:
    print(f"  [{c['size']:>5} MB] {c['name']:<40} status={c['fail_status']:<20} err={c['fail_reason'][:50]}")

print(f"\n--- 不在 state 里 ({len(by_state['not_run'])} 条) ---")
for c in by_state["not_run"]:
    print(f"  [{c['size']:>5} MB] {c['name']:<40} h={c['h']}")

if by_state.get("done_but_not_upgraded"):
    print(f"\n--- done 但未 upgraded ({len(by_state['done_but_not_upgraded'])} 条) ---")
    for c in by_state["done_but_not_upgraded"]:
        print(f"  [{c['size']:>5} MB] {c['name']}")
