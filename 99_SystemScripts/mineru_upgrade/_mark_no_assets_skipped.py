"""
_mark_no_assets_skipped.py — 给 "MinerU 跑过但合并时无 assets 被 skip" 的 notes
打上 `_ocr_upgraded: mineru_no_assets` 标记，让数字反映真实处理状态。

判定条件（必须同时满足）：
  1. note 的 source_pdf 在 manifest 里能找到 hash
  2. 该 hash 在 _mineru_state.json 的 done 中
  3. note FM 里 _ocr_upgraded 字段不存在 / 不为 mineru 或 mineru_split

操作：
  - 给 FM 加 `_ocr_upgraded: mineru_no_assets`
  - 加 `_mineru_done_at: <state.done[hash].date>`
  - 加 `_mineru_outputs_dir: <state.done[hash].outputs_dir>`
  - **不改** body / 不删原字段

用法：
    python _mark_no_assets_skipped.py --dry-run
    python _mark_no_assets_skipped.py
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
STATE = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_state.json")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state = json.loads(STATE.read_text(encoding="utf-8"))
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))

    # path → hash（manifest 用 forward slash）
    manifest_fwd: dict[str, str] = {
        r["path"].replace("\\", "/"): h
        for h, r in m["records"].items() if r.get("path")
    }
    done_info = state["done"]

    candidates: list[tuple[Path, str, dict]] = []
    skipped_already_upgraded = 0
    skipped_no_match = 0

    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        mo = FM_RE.match(txt)
        if not mo:
            continue
        try:
            fm = yaml.safe_load(mo.group(1)) or {}
        except yaml.YAMLError:
            continue

        existing = fm.get("_ocr_upgraded")
        if existing in ("mineru", "mineru_split", "mineru_no_assets"):
            skipped_already_upgraded += 1
            continue

        sp = fm.get("source_pdf") or fm.get("source_file")
        if not sp:
            continue
        sp_fwd = str(sp).replace("\\", "/")
        h = manifest_fwd.get(sp_fwd)
        if not h or h not in done_info:
            skipped_no_match += 1
            continue

        info = done_info[h]
        candidates.append((p, h, info))

    print(f"\n{'='*72}")
    print(f"  扫描结果")
    print(f"{'='*72}")
    print(f"  已 upgraded（mineru/mineru_split/mineru_no_assets）: {skipped_already_upgraded}")
    print(f"  source_pdf 不匹配 manifest 或未 done:                {skipped_no_match}")
    print(f"  待打 mineru_no_assets 标记:                          {len(candidates)}")
    print(f"{'='*72}\n")

    if not candidates:
        print("[OK] 无候选可处理")
        return 0

    print("Top 5 候选预览:")
    for p, h, info in candidates[:5]:
        print(f"  · {p.name:<35}  hash={h[:16]}  date={info.get('date','?')}  pages={info.get('pages','?')}")
    if len(candidates) > 5:
        print(f"  ... 还有 {len(candidates) - 5}")
    print()

    if args.dry_run:
        print("[DRY-RUN] 未写入")
        return 0

    # 实际改写
    updated = 0
    for p, h, info in candidates:
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        mo = FM_RE.match(txt)
        if not mo:
            continue
        try:
            fm = yaml.safe_load(mo.group(1)) or {}
        except yaml.YAMLError:
            continue
        body = txt[mo.end():]

        # 加新字段（保持原 FM 字段顺序，新字段追加到末尾）
        fm["_ocr_upgraded"] = "mineru_no_assets"
        fm["_mineru_done_at"] = info.get("date", "")
        fm["_mineru_outputs_dir"] = info.get("outputs_dir", "")

        new_fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        body_clean = body.lstrip("\n")
        new_text = f"---\n{new_fm_str}---\n\n{body_clean}"
        # 确保末尾有 newline
        if not new_text.endswith("\n"):
            new_text += "\n"
        p.write_text(new_text, encoding="utf-8")
        updated += 1

    print(f"[DONE] 写入 {updated} / {len(candidates)} 条 note")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
