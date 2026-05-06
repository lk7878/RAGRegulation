"""
_dedupe_notes.py

半自动去重 _dup 系列文件。修复审计报告 P0.2。

策略：
- 按 reg_id 分组，找出同 reg_id 多文件的情况
- 评分规则：confidence (high=3/medium=2/low=1/空=0) * 10000 + body_length
- 若 loser body 长度 >= winner 的 1.5x → 标记为 conflict 需人工审，不自动处理
- 否则：winner 保留，losers 软删除到 05_Audit/trash_dups/<date>/

用法：
    python _dedupe_notes.py --dry-run       # 预览方案
    python _dedupe_notes.py                 # 正式执行（搬到 trash）

安全：
- 永不直接 rm 文件
- losers 搬到 05_Audit/trash_dups/<date>/<原路径>/<原文件名>
- 同时写 05_Audit/dedupe_report_<date>.md 审计报告
- conflict 条目写入 05_Audit/dedupe_conflicts_<date>.md 等人工处理
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
AUDIT = Path(r"D:\CcVault\05_Audit")

CONF_SCORE = {"high": 3, "medium": 2, "low": 1, "unknown": 0, "": 0, None: 0}


def read_note(p: Path) -> tuple[dict, str]:
    """读 note，返回 (fm, body)."""
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}, ""
    if not txt.startswith("---"):
        return {}, txt
    end = txt.find("\n---", 4)
    if end < 0:
        return {}, txt
    try:
        fm = yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        fm = {}
    body = txt[end + 4 :]
    return fm, body


def score_note(fm: dict, body: str) -> tuple[int, int]:
    """评分: (confidence_score, body_length)."""
    conf = (fm.get("cross_check_overall_confidence") or "").lower()
    conf_score = CONF_SCORE.get(conf, 0)
    return (conf_score, len(body))


def is_dup_file(p: Path) -> bool:
    """判断文件名是否带 _dup 后缀。"""
    return bool(re.search(r"_dup\d*\.md$", p.name))


def collect_groups() -> dict[str, list[Path]]:
    """按 reg_id 分组 notes。"""
    groups: dict[str, list[Path]] = defaultdict(list)
    for p in WIKI.rglob("*.md"):
        fm, _ = read_note(p)
        reg_id = (fm.get("reg_id") or "").strip()
        if reg_id:
            groups[reg_id].append(p)
    return {k: v for k, v in groups.items() if len(v) > 1}


def choose_winner(candidates: list[Path]) -> tuple[Path, list[tuple[Path, str]], bool]:
    """
    从 candidates 选 winner。

    Returns:
        (winner, losers_with_reason, has_conflict)

    conflict 判定（保守）：
      - 任一 loser body 长度 >= winner 的 1.5x 且 loser confidence >= winner
      - 或任一 loser 不是 _dup 文件（不走自动流程，防误删真数据）
    """
    scored = []
    for p in candidates:
        fm, body = read_note(p)
        s = score_note(fm, body)
        is_canonical = not is_dup_file(p)
        scored.append((p, s, is_canonical, fm, body))

    # 排序优先级：is_canonical desc → confidence_score desc → body_length desc
    scored.sort(key=lambda x: (x[2], x[1][0], x[1][1]), reverse=True)
    winner_entry = scored[0]
    winner = winner_entry[0]
    w_conf, w_body_len = winner_entry[1]

    losers_with_reason = []
    has_conflict = False
    for entry in scored[1:]:
        p, (conf, body_len), is_canon, _fm, _body = entry
        reason_parts = []
        if winner_entry[2] and not is_canon:
            reason_parts.append("winner=canonical, loser=_dup")
        reason_parts.append(
            f"winner conf={winner_entry[1][0]} body={winner_entry[1][1]}, "
            f"loser conf={conf} body={body_len}"
        )
        # 保守 conflict 检测
        if body_len >= w_body_len * 1.5 and conf >= w_conf:
            reason_parts.append("CONFLICT: loser body much longer + higher confidence")
            has_conflict = True
        elif is_canon:
            # loser 不是 _dup 后缀文件 → 两个都是"原生"文件名冲突 → 人工决定
            reason_parts.append("CONFLICT: both files are non-_dup (reg_id mismatch?)")
            has_conflict = True
        losers_with_reason.append((p, "; ".join(reason_parts)))

    return winner, losers_with_reason, has_conflict


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="不执行移动，只输出方案")
    args = ap.parse_args()

    today = dt.date.today().isoformat()
    trash_root = AUDIT / "trash_dups" / today
    report_path = AUDIT / f"dedupe_report_{today}.md"
    conflicts_path = AUDIT / f"dedupe_conflicts_{today}.md"

    groups = collect_groups()

    auto_decisions = []  # (reg_id, winner, losers_with_reason)
    conflict_decisions = []  # 同上但含 conflict

    for reg_id, files in sorted(groups.items()):
        winner, losers, has_conflict = choose_winner(files)
        if has_conflict:
            conflict_decisions.append((reg_id, winner, losers))
        else:
            auto_decisions.append((reg_id, winner, losers))

    # ---------- 打印 + 写报告 ----------
    report_lines = [
        "---",
        "type: audit_report",
        f"created: {today}",
        "category: dedupe",
        "tags: [audit/dedupe, audit/p0_fix]",
        "---",
        "",
        f"# Dedupe Report · {today}",
        "",
        f"**总组数（含 _dup 或同 reg_id 多文件）**: {len(groups)}",
        f"**自动处理（移入 trash）**: {len(auto_decisions)}",
        f"**⚠️ 冲突（需人工审）**: {len(conflict_decisions)}",
        "",
    ]

    print(f"Groups with duplicate reg_id: {len(groups)}")
    print(f"Auto-dedupe (move to trash)  : {len(auto_decisions)}")
    print(f"⚠️  Conflicts (need human)   : {len(conflict_decisions)}")

    if auto_decisions:
        report_lines += ["## 自动处理清单", ""]
        for reg_id, winner, losers in auto_decisions:
            report_lines.append(
                f"### `{reg_id}`"
            )
            report_lines.append(
                f"- **Winner** (保留): `{winner.relative_to(WIKI)}`"
            )
            for loser, reason in losers:
                report_lines.append(
                    f"- **Loser** (→ trash): `{loser.relative_to(WIKI)}` — _{reason}_"
                )
            report_lines.append("")

    if conflict_decisions:
        report_lines += ["", "## ⚠️ 冲突清单（不自动处理）", ""]
        for reg_id, winner, losers in conflict_decisions:
            report_lines.append(f"### `{reg_id}`")
            report_lines.append(f"- Winner 候选: `{winner.relative_to(WIKI)}`")
            for loser, reason in losers:
                report_lines.append(f"- Loser 候选: `{loser.relative_to(WIKI)}` — {reason}")
            report_lines.append("")

    # ---------- 执行移动 ----------
    moved = 0
    if not args.dry_run:
        trash_root.mkdir(parents=True, exist_ok=True)
        for reg_id, winner, losers in auto_decisions:
            for loser, _reason in losers:
                # 保留原路径结构
                rel = loser.relative_to(WIKI)
                target = trash_root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(loser), str(target))
                moved += 1

        report_path.write_text("\n".join(report_lines), encoding="utf-8")

        if conflict_decisions:
            conflict_lines = [
                "---",
                "type: audit_report",
                f"created: {today}",
                "category: dedupe_conflict",
                "severity: high",
                "status: needs_human_review",
                "tags: [audit/dedupe, audit/conflict, audit/needs_review]",
                "---",
                "",
                f"# Dedupe Conflicts · {today}",
                "",
                f"共 {len(conflict_decisions)} 组需人工决定保留哪份。",
                "",
                "## 判定标准",
                "- Loser body 长度 >= Winner 的 1.5x，且 confidence >= Winner",
                "- 通常意味着 _dup 可能是更完整的版本",
                "- 建议对比两份 body 后决定",
                "",
                "---",
                "",
            ]
            for reg_id, winner, losers in conflict_decisions:
                conflict_lines.append(f"## `{reg_id}`")
                conflict_lines.append("")
                conflict_lines.append(f"- Winner 候选: `{winner.relative_to(WIKI)}`")
                for loser, reason in losers:
                    conflict_lines.append(f"- Loser 候选: `{loser.relative_to(WIKI)}` — {reason}")
                conflict_lines.append("")
            conflicts_path.write_text("\n".join(conflict_lines), encoding="utf-8")

    # ---------- 终端摘要 ----------
    if args.dry_run:
        print("\n=== DRY RUN · 预览 ===\n")
        for reg_id, winner, losers in auto_decisions[:10]:
            print(f"  [{reg_id}]")
            print(f"    winner: {winner.relative_to(WIKI)}")
            for loser, reason in losers:
                print(f"    trash : {loser.relative_to(WIKI)}  ({reason})")
        if len(auto_decisions) > 10:
            print(f"  ... and {len(auto_decisions) - 10} more auto decisions")

        if conflict_decisions:
            print(f"\n⚠️  {len(conflict_decisions)} conflicts found:")
            for reg_id, winner, losers in conflict_decisions:
                print(f"  [{reg_id}]")
                for loser, reason in losers:
                    print(f"    conflict: {loser.relative_to(WIKI)} vs {winner.relative_to(WIKI)}")

        print("\n[DRY RUN] No files moved.")
        print("Re-run without --dry-run to apply.")
    else:
        print(f"\n{moved} files moved to {trash_root}")
        print(f"Report: {report_path}")
        if conflict_decisions:
            print(f"Conflicts: {conflicts_path}")

    print("\nNext steps:")
    print("  python _semantic_search.py --rebuild   # 重建 BM25 索引")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
