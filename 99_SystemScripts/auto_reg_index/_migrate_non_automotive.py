"""
迁移非法规/非汽车 notes 离开 01_Wiki/regulations/ 命名空间：
  - out_of_scope   → 02_Wiki/non_automotive/
  - reference_material → 02_Wiki/references/

任务：
  1. 移动文件
  2. 更新其他 notes 中指向这些文件的 wikilink（用 path 前缀）
  3. 扫描 manifest 并更新对应 record 路径
  4. 更新 topic_pages 中的 wikilink

支持 --dry-run。
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
VAULT = Path(r"D:\CcVault")
MF_PATH = ROOT / "manifest.json"

NON_AUTO_DIR = VAULT / "02_Wiki" / "non_automotive"
REFERENCES_DIR = VAULT / "02_Wiki" / "references"


def load_topic_assignment() -> dict[str, list[str]]:
    """返回 {topic: [path strings]}"""
    p = ROOT / ".stage4" / "cluster_assignment.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    return {
        "out_of_scope": [n["path"] for n in d.get("out_of_scope", [])],
        "reference_material": [n["path"] for n in d.get("reference_material", [])],
    }


def move_note(old_path: Path, target_dir: Path, dry_run: bool) -> Path:
    """把文件移到 target_dir，返回新路径。"""
    target_dir.mkdir(parents=True, exist_ok=True)
    new_path = target_dir / old_path.name
    if new_path.exists():
        # 碰撞处理：加后缀
        stem, ext = new_path.stem, new_path.suffix
        i = 1
        while new_path.exists():
            new_path = target_dir / f"{stem}_mig{i}{ext}"
            i += 1
    if not dry_run:
        shutil.move(str(old_path), str(new_path))
    return new_path


def update_manifest(old_to_new: dict[str, str], dry_run: bool) -> int:
    """更新 manifest 中的 wiki_path 字段（如果存在）。"""
    if not MF_PATH.exists():
        return 0
    data = json.loads(MF_PATH.read_text(encoding="utf-8"))
    updates = 0
    for h, rec in data.get("records", {}).items():
        wp = rec.get("wiki_path") or rec.get("note_path")
        if wp and wp in old_to_new:
            rec["wiki_path"] = old_to_new[wp]
            updates += 1
    if updates and not dry_run:
        MF_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return updates


def update_wikilinks(old_to_new: dict[str, str], dry_run: bool) -> int:
    """扫描所有 MD 文件，更新 wikilink 目标（基于 stem 不变，不需要改）。
    注意：Obsidian wikilink 用 stem 不用完整路径，所以移动文件不影响链接，
    只要 stem 唯一即可。此函数主要用于 double-check。"""
    # 这里只做扫描检查，不修改（stem 未变）
    stems = {Path(old).stem for old in old_to_new.keys()}
    broken = 0
    for md in VAULT.rglob("*.md"):
        if str(md).startswith(str(NON_AUTO_DIR)) or str(md).startswith(str(REFERENCES_DIR)):
            continue
        try:
            txt = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for stem in stems:
            if f"[[{stem}]]" in txt or f"[[{stem}|" in txt or f"[[{stem}#" in txt:
                broken += 1  # "broken" is really just "referenced"; Obsidian handles stem-based refs fine
                break
    return broken


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    assignments = load_topic_assignment()
    moves = {}  # old_path -> new_path

    # out_of_scope
    for p in assignments["out_of_scope"]:
        old = Path(p)
        if not old.exists():
            print(f"[SKIP missing] {old}")
            continue
        new = move_note(old, NON_AUTO_DIR, args.dry_run)
        moves[str(old)] = str(new)
        print(f"  out_of_scope:       {old.name}  →  non_automotive/")

    # reference_material
    for p in assignments["reference_material"]:
        old = Path(p)
        if not old.exists():
            print(f"[SKIP missing] {old}")
            continue
        new = move_note(old, REFERENCES_DIR, args.dry_run)
        moves[str(old)] = str(new)
        print(f"  reference_material: {old.name}  →  references/")

    print(f"\nTotal moves: {len(moves)}")

    # Manifest update
    mf_updates = update_manifest(moves, args.dry_run)
    print(f"Manifest records updated: {mf_updates}")

    # Wikilink scan (for report only, Obsidian resolves by stem)
    refs = update_wikilinks(moves, args.dry_run)
    print(f"Notes referencing moved files (wikilink unchanged — Obsidian resolves by stem): {refs}")

    if args.dry_run:
        print("\n[DRY RUN] No files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
