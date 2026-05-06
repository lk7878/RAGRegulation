"""
构建 supersession 反向链：
- 扫描所有 notes 的 supersedes 字段（字符串含 [[...]] 或 列表）
- 对每个被替代的 note，写回 superseded_by 字段
- 输出 supersession 关系图 到 .stage4/supersession_chain.json

支持 --dry-run。
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
OUT_DIR = ROOT / ".stage4"
OUT_DIR.mkdir(exist_ok=True)

_WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(\|[^\]]*)?\]\]")


def parse_supersedes(v) -> list[str]:
    """从 supersedes 值返回规范化的 reg_id 列表。"""
    if not v:
        return []
    items = []

    def _split_str(s: str) -> list[str]:
        """优先 wikilink，否则按逗号/顿号拆分。"""
        s = s.strip()
        m = _WIKILINK_RE.findall(s)
        if m:
            return [a.strip() for a, _ in m]
        # 按中英文逗号、顿号、分号拆分（避免误拆年份中的逗号）
        parts = re.split(r"[,，、;；]\s*", s)
        return [p.strip() for p in parts if p.strip()]

    if isinstance(v, str):
        items = _split_str(v)
    elif isinstance(v, list):
        for x in v:
            if isinstance(x, str):
                items.extend(_split_str(x))
            elif isinstance(x, dict):
                ref = x.get("ref") or x.get("reg_id")
                if ref:
                    items.append(str(ref).strip())
    return [i for i in items if i]


def scan_wiki() -> tuple[dict[str, Path], dict[str, list[str]]]:
    """
    返回:
      reg_id_to_path: reg_id -> file path
      forward_map: src_reg_id -> [predecessors] （来自 supersedes 字段）
    """
    reg_to_path: dict[str, Path] = {}
    forward_map: dict[str, list[str]] = {}
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if not txt.startswith("---"):
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        try:
            fm = yaml.safe_load(txt[4:end]) or {}
        except yaml.YAMLError:
            continue
        reg_id = (fm.get("reg_id") or "").strip()
        if reg_id:
            reg_to_path[reg_id] = p
        sup = parse_supersedes(fm.get("supersedes"))
        if sup:
            forward_map[reg_id] = sup
    return reg_to_path, forward_map


def build_reverse(forward: dict[str, list[str]]) -> dict[str, list[str]]:
    """反转：predecessor -> [successors that supersede it]。"""
    rev: dict[str, list[str]] = defaultdict(list)
    for successor, preds in forward.items():
        for pred in preds:
            rev[pred].append(successor)
    return dict(rev)


def write_superseded_by(
    path: Path,
    successors: list[str],
    dry_run: bool,
    mark_status: bool = False,
) -> tuple[bool, bool]:
    """往 note FM 写 superseded_by 字段。

    Args:
        path: note 路径
        successors: 后继 reg_id 列表
        dry_run: 是否试跑
        mark_status: 若 True 且当前 status=active，顺便改成 superseded

    Returns:
        (file_modified, status_changed)
    """
    txt = path.read_text(encoding="utf-8", errors="replace")
    if not txt.startswith("---"):
        return False, False
    end = txt.find("\n---", 4)
    if end < 0:
        return False, False
    try:
        fm = yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        return False, False

    # 用 wikilink 列表形式（Obsidian 友好）
    links = [f"[[{s}]]" for s in sorted(set(successors))]
    new_value = links[0] if len(links) == 1 else links

    changed_by = fm.get("superseded_by") != new_value
    changed_status = False

    if changed_by:
        fm["superseded_by"] = new_value

    if mark_status and fm.get("status") == "active":
        fm["status"] = "superseded"
        changed_status = True

    if not (changed_by or changed_status):
        return False, False

    if dry_run:
        return changed_by, changed_status

    body = txt[end + 4 :]
    new_content = (
        "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---" + body
    )
    path.write_text(new_content, encoding="utf-8")
    return changed_by, changed_status


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--mark-superseded-status",
        action="store_true",
        help="被代替的 note 若当前 status=active，自动改为 superseded",
    )
    args = ap.parse_args()

    reg_to_path, forward = scan_wiki()
    reverse = build_reverse(forward)

    print(f"Notes with supersedes: {len(forward)}")
    print(f"Unique predecessors: {len(reverse)}")

    # 资源匹配：通过 reg_id 精确匹配到文件
    updates = 0
    status_updates = 0
    orphans = []  # supersedes 指向的 reg_id 找不到对应文件
    for pred, successors in reverse.items():
        path = reg_to_path.get(pred)
        if not path:
            orphans.append({"pred": pred, "successors": successors})
            continue
        changed_by, changed_status = write_superseded_by(
            path, successors, args.dry_run, mark_status=args.mark_superseded_status
        )
        if changed_by:
            updates += 1
        if changed_status:
            status_updates += 1

    # 保存 JSON 图
    chain_data = {
        "forward_map": forward,  # successor -> [preds]
        "reverse_map": reverse,  # pred -> [successors]
        "stats": {
            "total_links": sum(len(v) for v in forward.values()),
            "unique_successors": len(forward),
            "unique_predecessors": len(reverse),
            "files_updated": updates,
            "orphans": len(orphans),
        },
        "orphans": orphans[:50],
    }
    (OUT_DIR / "supersession_chain.json").write_text(
        json.dumps(chain_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"Files updated with superseded_by: {updates}")
    if args.mark_superseded_status:
        print(f"Files status active -> superseded: {status_updates}")
    print(f"Orphan predecessors (no matching note): {len(orphans)}")
    if orphans:
        print("Sample orphans:")
        for o in orphans[:5]:
            print(f"  {o['pred']!r} <- {o['successors']}")
    if args.dry_run:
        print("\n[DRY RUN] No files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
