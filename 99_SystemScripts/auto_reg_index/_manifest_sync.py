"""把 manifest 的 reg_id/region 字段按 wiki 当前 FM 状态回写同步。"""
import argparse
import json
import yaml
from pathlib import Path

MF_PATH = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.loads(MF_PATH.read_text(encoding="utf-8"))

    # 扫 wiki 建立 source_pdf → fm 映射
    note_map: dict[str, dict] = {}
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        fm = yaml.safe_load(txt[4:end]) or {}
        src = fm.get("source_pdf") or fm.get("source_file") or ""
        if src:
            key = str(src).replace("\\", "/").lstrip("/")
            note_map[key] = fm

    n_regid = 0
    n_region = 0
    n_skipped = 0

    for h, rec in data["records"].items():
        if rec.get("state") != "written":
            continue
        path = str(rec.get("path", "")).replace("\\", "/").lstrip("/")
        if path not in note_map:
            n_skipped += 1
            continue
        fm = note_map[path]
        fm_rid = fm.get("reg_id")
        fm_reg = fm.get("region")
        if fm_rid and rec.get("reg_id") != fm_rid:
            rec["reg_id"] = fm_rid
            n_regid += 1
        if fm_reg and rec.get("region") != fm_reg:
            rec["region"] = fm_reg
            n_region += 1

    print(f"{'[DRY-RUN] ' if args.dry_run else ''}Sync result:")
    print(f"  reg_id updated: {n_regid}")
    print(f"  region updated: {n_region}")
    print(f"  skipped (no matching note): {n_skipped}")

    if not args.dry_run and (n_regid or n_region):
        # 更新 updated_at
        from datetime import datetime, timezone
        data["updated_at"] = datetime.now(timezone.utc).isoformat()
        MF_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  manifest saved: {MF_PATH}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
