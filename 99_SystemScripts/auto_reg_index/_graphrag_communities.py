"""
Stage 5b — GraphRAG · 社区检测

读取 `.stage5/graph.json`（由 `_build_graph.py` 产出），用 Louvain 算法做社区检测。
对过大社区（> MAX_COMMUNITY_SIZE）递归细分；过小社区（< MIN_COMMUNITY_SIZE）标 too_small。

输出：
  .stage5/communities.json
    {
      "meta": {"algorithm": "louvain", "resolution": 1.0, ...},
      "communities": [
        {"id": 0, "size": 12, "status": "ready", "members": [reg_id, ...],
         "top_region": "cn", "top_topic": "brakes", "internal_edges": 15}
      ]
    }

用法：
  python _graphrag_communities.py                    # 全量
  python _graphrag_communities.py --resolution 1.2   # 更细的社区
  python _graphrag_communities.py --dry-run          # 只统计不写
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx
from networkx.algorithms.community import louvain_communities

ROOT = Path(__file__).parent
STAGE5 = ROOT / ".stage5"

MIN_COMMUNITY_SIZE = 3
MAX_COMMUNITY_SIZE = 30


def load_graph() -> tuple[dict, nx.Graph]:
    """读 graph.json，构建无向图（社区检测不关心方向）。"""
    gpath = STAGE5 / "graph.json"
    if not gpath.exists():
        raise FileNotFoundError(
            f"找不到 {gpath}。请先跑 python _build_graph.py 生成图数据。"
        )
    data = json.loads(gpath.read_text(encoding="utf-8"))

    g = nx.Graph()
    for reg_id, node in data["nodes"].items():
        g.add_node(
            reg_id,
            region=node.get("region", "unknown"),
            topic=node.get("topic", ""),
            status=node.get("status", "unknown"),
            title=node.get("title", ""),
            date=node.get("date", ""),
        )
    for e in data["edges"]:
        src, dst = e["src"], e["dst"]
        if src == dst:
            continue
        # 多重边合并，保留第一个 rel 作为主关系
        if g.has_edge(src, dst):
            attrs = g[src][dst]
            attrs["weight"] = attrs.get("weight", 1) + 1
            rels = set(attrs.get("rels", [])) | {e.get("rel", "")}
            attrs["rels"] = sorted(r for r in rels if r)
        else:
            g.add_edge(src, dst, weight=1, rels=[e.get("rel", "")] if e.get("rel") else [])
    return data, g


def split_large_community(
    g: nx.Graph,
    members: set[str],
    *,
    max_size: int,
    resolution: float,
    seed: int,
) -> list[set[str]]:
    """对 >max_size 的社区递归细分，返回子社区列表。"""
    if len(members) <= max_size:
        return [members]
    subg = g.subgraph(members).copy()
    # 逐步提高 resolution 直到切开
    current_res = resolution
    for _ in range(5):
        current_res *= 1.5
        subs = louvain_communities(subg, resolution=current_res, seed=seed)
        if len(subs) > 1:
            break
    else:
        # 切不开就硬分（按 reg_id 排序切块）
        ordered = sorted(members)
        chunks: list[set[str]] = []
        for i in range(0, len(ordered), max_size):
            chunks.append(set(ordered[i : i + max_size]))
        return chunks

    # 递归细分每个子社区
    result: list[set[str]] = []
    for sub in subs:
        result.extend(
            split_large_community(
                g, set(sub), max_size=max_size, resolution=current_res, seed=seed
            )
        )
    return result


def classify_communities(
    g: nx.Graph,
    communities: list[set[str]],
) -> list[dict]:
    """把每个 community 转为元数据字典。"""
    out: list[dict] = []
    for i, members in enumerate(communities):
        if not members:
            continue
        # 区域 / 主题分布
        regions = Counter(g.nodes[n].get("region", "unknown") for n in members if n in g.nodes)
        topics = Counter(g.nodes[n].get("topic", "") for n in members if n in g.nodes)
        top_region = regions.most_common(1)[0][0] if regions else "unknown"
        top_topic = topics.most_common(1)[0][0] if topics else ""

        # 内部边
        subg = g.subgraph(members)
        internal_edges = subg.number_of_edges()

        # 按 in-degree 排序找 core_nodes（社区内度数最高的 top-3）
        deg = sorted(
            ((n, subg.degree(n)) for n in members),
            key=lambda x: x[1],
            reverse=True,
        )
        core_nodes = [n for n, _ in deg[:3]]

        size = len(members)
        if size < MIN_COMMUNITY_SIZE:
            status = "too_small"
        elif internal_edges == 0:
            status = "disconnected"  # 成员之间无边（理论上 louvain 不应产生）
        else:
            status = "ready"

        out.append({
            "id": i,
            "size": size,
            "status": status,
            "top_region": top_region,
            "top_topic": top_topic,
            "internal_edges": internal_edges,
            "core_nodes": core_nodes,
            "members": sorted(members),
        })
    # 按 size 降序
    out.sort(key=lambda c: c["size"], reverse=True)
    # 重新分配 id
    for new_id, c in enumerate(out):
        c["id"] = new_id
    return out


def print_report(communities: list[dict]):
    ready = [c for c in communities if c["status"] == "ready"]
    too_small = [c for c in communities if c["status"] == "too_small"]
    disc = [c for c in communities if c["status"] == "disconnected"]
    total_members = sum(c["size"] for c in communities)

    print("\n=== Community Detection Report ===")
    print(f"  Communities total:   {len(communities)}")
    print(f"    ready (≥{MIN_COMMUNITY_SIZE}):        {len(ready)}")
    print(f"    too_small (<{MIN_COMMUNITY_SIZE}):    {len(too_small)}")
    print(f"    disconnected:      {len(disc)}")
    print(f"  Members total:       {total_members}")
    print(f"    in ready:          {sum(c['size'] for c in ready)}")
    print()

    if ready:
        print("  Size distribution (ready):")
        sizes = [c["size"] for c in ready]
        print(f"    min={min(sizes)}, max={max(sizes)}, avg={sum(sizes)/len(sizes):.1f}")
        print()
        print("  Top 10 communities by size:")
        for c in ready[:10]:
            label = f"[{c['top_region']}/{c['top_topic'] or '?'}]"
            core = ", ".join(c["core_nodes"][:2])
            print(f"    #{c['id']:3d} n={c['size']:3d} edges={c['internal_edges']:3d} {label:30s}  core: {core}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolution", type=float, default=1.0,
                    help="Louvain resolution (>1 produces smaller communities)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--max-size", type=int, default=MAX_COMMUNITY_SIZE)
    ap.add_argument("--dry-run", action="store_true", help="不写 communities.json")
    args = ap.parse_args()

    print("Loading graph from .stage5/graph.json ...")
    raw_data, g = load_graph()
    print(f"  Nodes: {g.number_of_nodes()}, Edges: {g.number_of_edges()}")

    print(f"\nRunning Louvain (resolution={args.resolution}, seed={args.seed}) ...")
    raw = louvain_communities(g, resolution=args.resolution, seed=args.seed)
    print(f"  Initial communities: {len(raw)}")

    print(f"\nSplitting large communities (>{args.max_size}) ...")
    refined: list[set[str]] = []
    for c in raw:
        if len(c) > args.max_size:
            parts = split_large_community(
                g, set(c),
                max_size=args.max_size,
                resolution=args.resolution,
                seed=args.seed,
            )
            refined.extend(parts)
        else:
            refined.append(set(c))
    print(f"  After split: {len(refined)}")

    print("\nClassifying ...")
    communities = classify_communities(g, refined)
    print_report(communities)

    if args.dry_run:
        print("\n[dry-run] 未写入。")
        return 0

    meta = {
        "algorithm": "louvain",
        "resolution": args.resolution,
        "seed": args.seed,
        "max_size": args.max_size,
        "min_size": MIN_COMMUNITY_SIZE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "graph_nodes": g.number_of_nodes(),
        "graph_edges": g.number_of_edges(),
        "communities_ready": len([c for c in communities if c["status"] == "ready"]),
        "communities_too_small": len([c for c in communities if c["status"] == "too_small"]),
    }

    out = STAGE5 / "communities.json"
    out.write_text(
        json.dumps({"meta": meta, "communities": communities}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n✓ Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
