"""统计类 tools：全局概览 / 按条件计数 / 按字段分组 / 最近改动。"""
from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from langchain.tools import tool

from ._shared import (
    COMM_DIR,
    ROOT,
    VAULT,
    load_all_notes,
    truncate,
)


@tool
def describe_vault() -> str:
    """CcVault 全局统计概览。无参数。

    返回：notes 总数、按区域/主题/status 分布、social 社区数、等价映射数、近 7 天改动数。
    这个 tool 应当在"vault 里有多少 X"/"整体情况"类问题时首选调用。
    """
    notes = load_all_notes()
    n_total = len(notes)

    by_region = Counter(n["region"] for n in notes)
    by_status = Counter(n["status"] for n in notes)
    by_topic = Counter(n["topic"] for n in notes)
    by_confidence = Counter(n["confidence"] for n in notes)

    # 社区数
    comm_files = list(COMM_DIR.glob("community_*.md")) if COMM_DIR.exists() else []

    # 等价映射数
    equiv_count = 0
    equiv_page = VAULT / "03_Equivalence" / "_Equivalence MOC.md"
    if equiv_page.exists():
        txt = equiv_page.read_text(encoding="utf-8", errors="replace")
        # 简单数 `|   1  |` 这种行（Dataview 表格行数）
        equiv_count = len(re.findall(r"\n\|[ \t]*\d+[ \t]*\|", txt))
    # 兜底：累加 FM 的 equivalent_to
    if equiv_count == 0:
        for n in notes:
            eq = n.get("equivalent_to") or []
            if isinstance(eq, list):
                equiv_count += len(eq)

    lines = [
        "=== CcVault 全局概览 ===",
        f"Notes 总数: {n_total}",
        f"社区数 (GraphRAG): {len(comm_files)}",
        f"等价映射条数: {equiv_count}",
        "",
        "— 按区域分布 —",
    ]
    for r, c in by_region.most_common():
        lines.append(f"  {r or '(空)':<10}: {c}")

    lines.append("\n— 按 status 分布 —")
    for s, c in by_status.most_common():
        lines.append(f"  {s or '(空)':<14}: {c}")

    lines.append("\n— 按 cross_check 置信度 —")
    for cf, c in by_confidence.most_common():
        lines.append(f"  {cf or '(空)':<10}: {c}")

    lines.append(f"\n— 主题分布 top-15（共 {len(by_topic)} 个主题） —")
    for t, c in by_topic.most_common(15):
        lines.append(f"  {t or '(空)':<32}: {c}")

    return truncate("\n".join(lines), limit=5000)


@tool
def count_regulations(
    region: Optional[str] = None,
    topic: Optional[str] = None,
    status: Optional[str] = None,
    year_from: Optional[int] = None,
    year_to: Optional[int] = None,
    confidence: Optional[str] = None,
) -> str:
    """按条件过滤 notes 并计数。所有参数均可选，不传则对全量计数。

    用途：精确回答"XX 有多少条法规"类问题。
    如"2024 年后实施的电动车法规": region=None, topic='ev_battery_safety', year_from=2024。

    Args:
        region: cn / ece / eu / us / jp / kr / iso / sae / ...
        topic: 37 个 topic 之一（参考 02_Schema/02_taxonomy.md）。
        status: active / current / superseded / withdrawn / draft / pending / ...
        year_from: 按 publication_date 年份 >= 此值过滤。
        year_to: 按 publication_date 年份 <= 此值过滤。
        confidence: high / medium / low。
    """
    notes = load_all_notes()
    filtered = []
    for n in notes:
        if region and n["region"] != region:
            continue
        if topic and n["topic"] != topic:
            continue
        if status and n["status"] != status:
            continue
        if confidence and n["confidence"] != confidence:
            continue
        if year_from or year_to:
            pd = n.get("publication_date") or ""
            m = re.match(r"(\d{4})", str(pd))
            if not m:
                continue
            y = int(m.group(1))
            if year_from and y < year_from:
                continue
            if year_to and y > year_to:
                continue
        filtered.append(n)

    filters = []
    if region: filters.append(f"region={region}")
    if topic: filters.append(f"topic={topic}")
    if status: filters.append(f"status={status}")
    if year_from: filters.append(f"year>={year_from}")
    if year_to: filters.append(f"year<={year_to}")
    if confidence: filters.append(f"confidence={confidence}")

    filter_str = " AND ".join(filters) if filters else "(no filter)"
    lines = [f"Matching count: {len(filtered)}  [{filter_str}]"]

    # 列出前 15 条作为 preview（LLM 想进一步详读可再调 read_regulation）
    if filtered:
        lines.append(f"\n前 {min(15, len(filtered))} 条 preview:")
        for n in filtered[:15]:
            lines.append(
                f"  {n['reg_id']:<28} ({n['region']:<4}) "
                f"{n.get('publication_date', '')[:10]:<10} "
                f"[{n['status']:<12}] {(n['title'] or n['title_en'])[:40]}"
            )
    return truncate("\n".join(lines), limit=3500)


@tool
def stats_by_field(field: str, top_n: int = 30) -> str:
    """按单个 FM 字段做分组计数。

    Args:
        field: 分组字段，支持：region / topic / status / year / confidence / source_type。
        top_n: 返回前 N 组，默认 30。
    """
    field = field.strip().lower()
    valid = {"region", "topic", "status", "year", "confidence", "source_type"}
    if field not in valid:
        return f"[error] field 必须是 {sorted(valid)} 之一，得到 {field!r}。"

    notes = load_all_notes()
    if field == "year":
        keys = []
        for n in notes:
            pd = n.get("publication_date") or ""
            m = re.match(r"(\d{4})", str(pd))
            keys.append(m.group(1) if m else "(unknown)")
    elif field == "source_type":
        keys = [n.get("fm", {}).get("source_type") or "(空)" for n in notes]
    elif field == "confidence":
        keys = [n.get("confidence") or "(空)" for n in notes]
    else:
        keys = [n.get(field) or "(空)" for n in notes]

    c = Counter(keys)
    lines = [f"=== 按 {field} 分布（共 {len(c)} 组，show top {top_n}） ==="]
    for k, count in c.most_common(top_n):
        lines.append(f"  {str(k):<32}: {count}")
    return truncate("\n".join(lines), limit=3500)


@tool
def list_recent_changes(days: int = 7, limit: int = 20) -> str:
    """列出最近 N 天内 git 有改动的 note 文件。依赖 `git log` 可用。

    用途：回答"最近我改了什么""上周的变化"等问题。

    Args:
        days: 回溯天数，默认 7，最大 90。
        limit: 最多列出几条，默认 20，最大 50。
    """
    days = max(1, min(int(days), 90))
    limit = max(1, min(int(limit), 50))

    # VAULT 不是 git 仓库时降级：用 file mtime 排序
    since = datetime.now() - timedelta(days=days)
    try:
        r = subprocess.run(
            ["git", "log", f"--since={since.isoformat()}",
             "--name-only", "--pretty=format:COMMIT|%h|%ai|%s", "--", "01_Wiki/"],
            cwd=str(VAULT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
        if r.returncode == 0 and r.stdout.strip():
            return _parse_git_log(r.stdout, limit)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback：按 mtime 排
    notes = load_all_notes()
    with_mtime = []
    for n in notes:
        try:
            mt = Path(n["path"]).stat().st_mtime
            if mt >= since.timestamp():
                with_mtime.append((mt, n))
        except OSError:
            continue
    with_mtime.sort(key=lambda x: -x[0])
    lines = [f"最近 {days} 天内改动的 notes（按 mtime 排序，共 {len(with_mtime)}，show top {limit}）:"]
    for mt, n in with_mtime[:limit]:
        ts = datetime.fromtimestamp(mt).strftime("%Y-%m-%d %H:%M")
        lines.append(f"  {ts}  {n['reg_id']:<28} [{n['topic']}]")
    return truncate("\n".join(lines), limit=3500)


def _parse_git_log(stdout: str, limit: int) -> str:
    """解析 git log 输出，按 commit 聚合显示。"""
    commits = []
    cur = None
    for line in stdout.splitlines():
        if line.startswith("COMMIT|"):
            if cur:
                commits.append(cur)
            parts = line.split("|", 3)
            cur = {"sha": parts[1], "date": parts[2][:10], "msg": parts[3], "files": []}
        elif line.strip() and cur:
            cur["files"].append(line.strip())
    if cur:
        commits.append(cur)

    lines = [f"最近 {len(commits)} 个 commits 涉及 notes 改动:"]
    for c in commits[:limit]:
        lines.append(f"\n  {c['date']}  {c['sha']}  {c['msg']}")
        for f in c["files"][:10]:
            lines.append(f"      + {f}")
        if len(c["files"]) > 10:
            lines.append(f"      ... and {len(c['files']) - 10} more files")
    return truncate("\n".join(lines), limit=4000)


STATS_TOOLS = [
    describe_vault,
    count_regulations,
    stats_by_field,
    list_recent_changes,
]
