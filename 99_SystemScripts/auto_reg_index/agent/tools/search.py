"""检索类 tools：BM25 点查 / GraphRAG 层级 / 按 reg_id 读 note。"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from langchain.tools import tool

from ._shared import (
    COMM_DIR,
    fmt_note_line,
    find_note_by_reg_id,
    load_bm25_index,
    load_community_index,
    parse_note,
    truncate,
)


@tool
def search_regulations_bm25(
    query: str,
    region: Optional[str] = None,
    topic: Optional[str] = None,
    limit: int = 10,
) -> str:
    """按关键词在全部法规 notes 上做 BM25 检索（中英文混合 jieba 分词）。

    用途：找"具体某条或某几条法规"。query 支持 reg_id、主题词、中文或英文标题片段。
    如果用户问的是"领域全景"（"制动系统整体格局"）应优先用 search_communities_graphrag。

    Args:
        query: 自然语言查询词，可含中英文。
        region: 可选，过滤区域：cn / ece / eu / us / jp / kr / iso / sae。
        topic: 可选，过滤主题（37 个人工 topic 之一，如 brakes / lighting_signaling）。
        limit: 返回前 N 条，默认 10，最大 30。
    """
    limit = max(1, min(int(limit), 30))
    idx = load_bm25_index()
    if idx is None:
        return "[error] BM25 index not found. Run `python _semantic_search.py --rebuild` first."

    # 复用 _semantic_search.py 的 search()
    import sys
    from pathlib import Path as _P
    sys.path.insert(0, str(_P(__file__).parent.parent.parent))
    from _semantic_search import search  # type: ignore

    results = search(idx, query, limit=limit, region=region, topic=topic)
    if not results:
        hint = f" (filter: region={region}, topic={topic})" if (region or topic) else ""
        return f"No BM25 results for {query!r}{hint}."

    lines = [f"Top {len(results)} BM25 hits for {query!r}:"]
    for r in results:
        lines.append(fmt_note_line(r, score=r.get("score")))
    return truncate("\n".join(lines))


@tool
def search_communities_graphrag(
    query: str,
    topk_communities: int = 3,
    topk_members: int = 5,
) -> str:
    """GraphRAG 层级检索：先命中 top-K 相关社区（领域全景），再在社区成员内做细粒度 BM25。

    用途：问"某领域的整体格局""各主题下最相关法规"这类问题。
    33 个社区是基于 supersedes/equivalent_to/references 关系图的 Louvain 聚类。

    Args:
        query: 自然语言查询词。
        topk_communities: 返回前 N 个社区，默认 3，最大 10。
        topk_members: 每个社区内返回前 M 条法规，默认 5，最大 15。
    """
    topk_communities = max(1, min(int(topk_communities), 10))
    topk_members = max(1, min(int(topk_members), 15))

    comm_idx = load_community_index()
    if comm_idx is None:
        return ("[error] Community index not available. "
                "确认 04_Topics/communities/ 下有 community_*.md。")

    import sys
    from pathlib import Path as _P
    sys.path.insert(0, str(_P(__file__).parent.parent.parent))
    from _graphrag_search import (  # type: ignore
        search_communities,
        search_notes_in_members,
        _get_community_members,
    )
    notes_idx = load_bm25_index()

    communities = search_communities(comm_idx, query, topk=topk_communities)
    if not communities:
        return f"No community matches for {query!r}. Try broader or different keywords."

    lines = [f"Top {len(communities)} GraphRAG communities for {query!r}:"]
    for i, c in enumerate(communities, 1):
        lines.append(
            f"\n[{i}] Community #{c['community_id']:03d}  {c['label']}"
            f"\n    score={c['score']} | {c['member_count']} 成员 / {c['edge_count']} 边 "
            f"| {c['top_region']}/{c['top_topic']}"
        )
        if c["core_nodes"]:
            core = ", ".join(str(x) for x in c["core_nodes"])
            lines.append(f"    核心: {core}")
        if c["body_preview"]:
            preview = c["body_preview"].replace("\n", " ")[:180]
            lines.append(f"    摘要: {preview}...")

        # 细粒度成员
        members = _get_community_members(c["path"])
        hits = search_notes_in_members(notes_idx, members, query, topk=topk_members)
        if hits:
            lines.append(f"    成员 top-{len(hits)}:")
            for h in hits:
                lines.append(
                    f"      - {h['reg_id']:<28} ({h['region']}) "
                    f"score={h['score']} {h['title'][:40]}"
                )

    return truncate("\n".join(lines), limit=6000)


@tool
def read_regulation(reg_id: str, body_chars: int = 2000) -> str:
    """按 reg_id 精确读取某条法规的 FM 关键字段 + body 前 N 字符。

    用途：当 LLM 已经知道某条法规的 reg_id，需要看详情。
    reg_id 支持精确（如 "GB 4785-2019"）或紧凑形式（如 "GB4785-2019"）。

    Args:
        reg_id: 法规编号，如 "ECE R13-H" / "GB 21670-2008" / "GB4785-2019"。
        body_chars: 返回 body 前 N 字符，默认 2000，最大 6000。
    """
    body_chars = max(200, min(int(body_chars), 6000))
    n = find_note_by_reg_id(reg_id)
    if not n:
        return f"[not found] reg_id={reg_id!r}. 用 search_regulations_bm25 先找。"

    fm, body = parse_note(Path(n["path"]))
    lines = [
        f"=== {n['reg_id']} ===",
        f"title       : {n.get('title', '') or '[空]'}",
        f"title_en    : {n.get('title_en', '') or '[空]'}",
        f"region      : {n.get('region', '')}",
        f"status      : {n.get('status', '')}",
        f"topic       : {n.get('topic', '')}",
        f"publication : {n.get('publication_date', '')}",
        f"effective   : {n.get('effective_date', '')}",
        f"confidence  : {n.get('confidence', '')}",
        f"path        : {n['path']}",
    ]
    if fm.get("supersedes"):
        lines.append(f"supersedes  : {fm['supersedes']}")
    if fm.get("superseded_by"):
        lines.append(f"superseded_by: {fm['superseded_by']}")
    if fm.get("equivalent_to"):
        eq = fm["equivalent_to"]
        if isinstance(eq, list):
            eq_brief = [f"{x.get('reg_id', x)} ({x.get('relation', '?')})"
                        if isinstance(x, dict) else str(x) for x in eq[:5]]
        else:
            eq_brief = [str(eq)]
        lines.append(f"equivalent_to: {eq_brief}")

    lines.append("\n--- body preview ---")
    body_clean = body.strip()
    lines.append(body_clean[:body_chars] + ("\n...[truncated]" if len(body_clean) > body_chars else ""))
    return truncate("\n".join(lines), limit=body_chars + 1500)


SEARCH_TOOLS = [
    search_regulations_bm25,
    search_communities_graphrag,
    read_regulation,
]
