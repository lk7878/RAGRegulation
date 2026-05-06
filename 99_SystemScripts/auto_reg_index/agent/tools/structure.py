"""结构类 tools：等价映射 / 替代链 / 社区详情 / 主题成员。"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional

from langchain.tools import tool

from ._shared import (
    COMM_DIR,
    ROOT,
    find_note_by_reg_id,
    load_all_notes,
    parse_note,
    truncate,
)


@tool
def get_equivalence(reg_id: str) -> str:
    """查某条法规的跨区域等价映射（equivalent_to 字段）。

    用途：当问"ECE R13 对应的中国标准是什么""GB 4785 和国外对标情况"这类问题。
    返回：等价的其他法规 + relation 类型（identical / modified / reference / ...）。

    Args:
        reg_id: 法规编号。
    """
    n = find_note_by_reg_id(reg_id)
    if not n:
        return f"[not found] reg_id={reg_id!r}."

    eq = n.get("equivalent_to") or []
    if not eq:
        return f"{n['reg_id']} 没有 equivalent_to 字段。"

    lines = [f"=== {n['reg_id']} 的跨区域等价映射 ==="]
    if isinstance(eq, list):
        for item in eq:
            if isinstance(item, dict):
                rid = item.get("reg_id", "?")
                rel = item.get("relation", "?")
                note = item.get("note", "")
                lines.append(f"  → {rid:<28} [{rel}] {note}"[:150])
            else:
                lines.append(f"  → {item}")
    else:
        lines.append(f"  → {eq}")
    return "\n".join(lines)


@tool
def get_supersession_chain(reg_id: str) -> str:
    """查某法规的版本演化链（supersedes / superseded_by 字段）。

    用途："GB 4785 历经了哪些版本""ECE R13 最新版本是什么"。
    会沿着 superseded_by 链向前找到最新，并沿 supersedes 链向后找到最早。

    Args:
        reg_id: 法规编号。
    """
    start = find_note_by_reg_id(reg_id)
    if not start:
        return f"[not found] reg_id={reg_id!r}."

    def _follow(node: dict, direction: str, max_hops: int = 10) -> list[str]:
        """沿 supersedes 或 superseded_by 链条向一个方向追溯。"""
        chain = []
        cur = node
        for _ in range(max_hops):
            links = cur.get(direction) or cur.get("fm", {}).get(direction) or []
            if not isinstance(links, list):
                links = [links]
            if not links:
                break
            nxt_id = links[0]
            if isinstance(nxt_id, dict):
                nxt_id = nxt_id.get("reg_id", "")
            nxt = find_note_by_reg_id(str(nxt_id))
            if not nxt or nxt["reg_id"] == cur["reg_id"]:
                break
            chain.append(nxt["reg_id"])
            cur = nxt
        return chain

    older = _follow(start, "supersedes")
    newer = _follow(start, "superseded_by")

    lines = [f"=== {start['reg_id']} 版本链 ==="]
    if older:
        lines.append("更早版本（supersedes 链）:")
        for rid in older:
            lines.append(f"  ← {rid}")
    if newer:
        lines.append("更新版本（superseded_by 链）:")
        for rid in newer:
            lines.append(f"  → {rid}")
    if not older and not newer:
        lines.append("  （该 note 没有版本演化链接）")

    lines.append(f"\n当前 note: {start['reg_id']}  status={start['status']}  "
                 f"publication={start.get('publication_date', '')}")
    return "\n".join(lines)


@tool
def get_community(community_id: int) -> str:
    """读取某 GraphRAG 社区的综述摘要 + 完整成员列表。

    用途：用户已知社区编号（如从 search_communities_graphrag 返回），想深入看这个社区。

    Args:
        community_id: 社区编号（0–32）。
    """
    cid = int(community_id)
    target = COMM_DIR / f"community_{cid:03d}.md"
    if not target.exists():
        return f"[not found] community_{cid:03d}.md。有效范围 0–32（共 33 个）。"

    fm, body = parse_note(target)
    lines = [
        f"=== Community #{cid:03d} ===",
        f"label        : {fm.get('label', '')}",
        f"member_count : {fm.get('member_count', 0)}",
        f"edge_count   : {fm.get('edge_count', 0)}",
        f"top_region   : {fm.get('top_region', '')}",
        f"top_topic    : {fm.get('top_topic', '')}",
    ]

    core = fm.get("core_nodes") or []
    if core:
        lines.append(f"core_nodes   : {', '.join(str(x) for x in core)}")

    # 提取成员清单（[[...]] wikilinks）
    members = re.findall(r"\[\[([^\]|#]+)", body)
    if members:
        dedup = list(dict.fromkeys(members))  # 保序去重
        lines.append(f"\n成员 ({len(dedup)}):")
        for m in dedup[:30]:
            lines.append(f"  - {m}")
        if len(dedup) > 30:
            lines.append(f"  ... and {len(dedup) - 30} more")

    # 取第 2/3 节（关系结构 + 同类对比）前 1500 字作为摘要
    summary_match = re.search(r"## 2\..*?(?=\n## 4\.)", body, re.DOTALL)
    if summary_match:
        lines.append("\n--- 综述摘要 ---")
        lines.append(summary_match.group(0)[:1500])
    return truncate("\n".join(lines), limit=5000)


@tool
def list_by_topic(topic: str, limit: int = 50) -> str:
    """列出指定 topic 下的所有 notes。

    Args:
        topic: 37 个 topic 之一，如 brakes / lighting_signaling / ev_battery_safety。
        limit: 最多列出 N 条，默认 50，最大 200。
    """
    limit = max(1, min(int(limit), 200))
    notes = load_all_notes()
    matched = [n for n in notes if n["topic"] == topic]
    if not matched:
        # 模糊建议
        from collections import Counter
        topics = Counter(n["topic"] for n in notes if n["topic"])
        hint = ", ".join(t for t, _ in topics.most_common(10))
        return f"[not found] topic={topic!r}. 前 10 个 topic: {hint}"

    # 按 region 分组
    from collections import defaultdict
    by_region: dict[str, list[dict]] = defaultdict(list)
    for n in matched:
        by_region[n["region"] or "(未标注)"].append(n)

    lines = [f"=== Topic={topic}: {len(matched)} 条 notes ==="]
    shown = 0
    for region in sorted(by_region.keys()):
        group = by_region[region]
        lines.append(f"\n[{region}] {len(group)} 条:")
        for n in group:
            if shown >= limit:
                lines.append(f"  ... ({len(matched) - shown} more, 用 limit 参数增加)")
                return truncate("\n".join(lines), limit=4500)
            title = n["title"] or n["title_en"] or ""
            lines.append(f"  {n['reg_id']:<28} {title[:50]}")
            shown += 1
    return truncate("\n".join(lines), limit=4500)


STRUCTURE_TOOLS = [
    get_equivalence,
    get_supersession_chain,
    get_community,
    list_by_topic,
]
