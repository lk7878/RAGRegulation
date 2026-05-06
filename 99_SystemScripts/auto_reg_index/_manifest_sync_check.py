"""检查 manifest vs wiki 的 reg_id/region 一致性。"""
import json
import yaml
from pathlib import Path

MF_PATH = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")


def main() -> int:
    data = json.loads(MF_PATH.read_text(encoding="utf-8"))

    # 扫 wiki 所有 note → source_pdf 映射
    note_map: dict[str, tuple[Path, dict]] = {}
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
            note_map[key] = (p, fm)

    stale_regid = 0
    stale_region = 0
    note_missing = 0
    examples: list[tuple[str, str]] = []
    region_examples: list[tuple[str, str]] = []

    written_records = [r for r in data["records"].values() if r.get("state") == "written"]
    for rec in written_records:
        path = str(rec.get("path", "")).replace("\\", "/").lstrip("/")
        if path not in note_map:
            note_missing += 1
            continue
        _, fm = note_map[path]
        mf_rid = rec.get("reg_id")
        fm_rid = fm.get("reg_id")
        if mf_rid != fm_rid:
            stale_regid += 1
            if len(examples) < 5:
                examples.append((mf_rid, fm_rid))
        mf_reg = rec.get("region")
        fm_reg = fm.get("region")
        if mf_reg != fm_reg:
            stale_region += 1
            if len(region_examples) < 5:
                region_examples.append((mf_reg, fm_reg))

    print(f"manifest records (written): {len(written_records)}")
    print(f"notes on disk: {len(note_map)}")
    print(f"manifest records missing note file: {note_missing}")
    print(f"stale reg_id (mf != fm): {stale_regid}")
    print(f"stale region (mf != fm): {stale_region}")
    print("\nreg_id examples (mf → fm):")
    for mf_rid, fm_rid in examples:
        print(f"  {mf_rid!r} → {fm_rid!r}")
    print("\nregion examples (mf → fm):")
    for mf_reg, fm_reg in region_examples:
        print(f"  {mf_reg!r} → {fm_reg!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
