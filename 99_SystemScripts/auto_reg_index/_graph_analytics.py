"""
Stage 5a — 深度图分析

读取 .stage5/graph.json 并计算：
  - PageRank / HITS / Betweenness Centrality
  - 弱连通分量 (WCC)
  - 社区（按 topic 着色）
  - 分区域节点度统计
  - 关键发现输出

用法：python _graph_analytics.py
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

ROOT = Path(__file__).parent
STAGE5 = ROOT / ".stage5"


def _flatten(v) -> str:
    if isinstance(v, list):
        return ",".join(str(x) for x in v) if v else ""
    return str(v) if v is not None else ""


def load_graph() -> tuple[nx.MultiDiGraph, dict, list]:
    data = json.loads((STAGE5 / "graph.json").read_text(encoding="utf-8"))
    nodes = data["nodes"]
    edges = data["edges"]

    G = nx.MultiDiGraph()
    for rid, n in nodes.items():
        # 所有属性都展平成 str（避免 list 不 hashable）
        attrs = {k: _flatten(v) for k, v in n.items() if k != "path"}
        G.add_node(rid, **attrs)
    for e in edges:
        G.add_edge(e["src"], e["dst"], rel=e["rel"])
    return G, nodes, edges


def main():
    G, nodes, edges = load_graph()
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"Density: {nx.density(G):.6f}")

    # === 简单图用于 undirected 度量 ===
    UG = G.to_undirected()
    print(f"Undirected degree mean: {sum(d for _, d in UG.degree()) / UG.number_of_nodes():.2f}")

    # === Weakly Connected Components ===
    wcc = list(nx.weakly_connected_components(G))
    wcc.sort(key=len, reverse=True)
    print(f"\n=== Weakly Connected Components: {len(wcc)} ===")
    print(f"Largest component: {len(wcc[0])} nodes")
    print(f"Components of size >= 5: {sum(1 for c in wcc if len(c) >= 5)}")
    print(f"Singletons (size 1): {sum(1 for c in wcc if len(c) == 1)}")

    print("\nTop 5 components:")
    for i, c in enumerate(wcc[:5]):
        sample = list(c)[:5]
        # 找 topic 分布
        topics = Counter()
        regions = Counter()
        for n in c:
            topics[G.nodes[n].get("topic", "")] += 1
            regions[G.nodes[n].get("region", "")] += 1
        top_topic = topics.most_common(1)[0] if topics else ("", 0)
        top_region = regions.most_common(2)
        print(f"  #{i+1}: {len(c)} nodes | topic={top_topic[0]} ({top_topic[1]}) | regions={dict(top_region)}")
        print(f"       sample: {sample[:3]}")

    # === PageRank ===
    print("\n=== PageRank (top 15) ===")
    pr = nx.pagerank(G, alpha=0.85)
    top_pr = sorted(pr.items(), key=lambda x: -x[1])[:15]
    pr_results = []
    for rid, score in top_pr:
        nd = G.nodes[rid]
        print(f"  {rid:35s} pr={score:.4f}  region={nd.get('region','?'):6s}  topic={nd.get('topic','')}")
        pr_results.append({
            "reg_id": rid,
            "pagerank": round(score, 5),
            "region": nd.get("region"),
            "topic": nd.get("topic"),
            "title": nd.get("title", "")[:80],
        })

    # === Betweenness ===
    # 仅算大连通分量上的 betweenness (O(V*E))
    big_nodes = set(wcc[0]) if wcc else set()
    big_subgraph = G.subgraph(big_nodes)
    betw = nx.betweenness_centrality(big_subgraph, k=min(200, len(big_nodes)))
    top_betw = sorted(betw.items(), key=lambda x: -x[1])[:10]
    print("\n=== Top 10 Betweenness Centrality (bridges) ===")
    betw_results = []
    for rid, score in top_betw:
        nd = G.nodes[rid]
        print(f"  {rid:35s} bc={score:.4f}  topic={nd.get('topic','')}")
        betw_results.append({
            "reg_id": rid,
            "betweenness": round(score, 5),
            "topic": nd.get("topic"),
            "title": nd.get("title", "")[:80],
        })

    # === 按 topic 聚合 ===
    topic_edges = Counter()
    cross_topic_edges = Counter()
    for u, v, d in G.edges(data=True):
        ut = G.nodes[u].get("topic", "")
        vt = G.nodes[v].get("topic", "")
        if ut and vt:
            if ut == vt:
                topic_edges[ut] += 1
            else:
                cross_topic_edges[(ut, vt)] += 1

    print("\n=== Top 10 Cross-Topic Edges (potential consolidation) ===")
    cross_topic_results = []
    for (ut, vt), c in cross_topic_edges.most_common(10):
        print(f"  {ut:30s} -> {vt:30s} ({c}x)")
        cross_topic_results.append({"from": ut, "to": vt, "count": c})

    # === 按区域聚合 ===
    region_edges = Counter()
    for u, v, d in G.edges(data=True):
        ur = G.nodes[u].get("region", "")
        vr = G.nodes[v].get("region", "")
        region_edges[(ur, vr)] += 1
    print("\n=== Region Flow (top 10) ===")
    region_results = []
    for (ur, vr), c in region_edges.most_common(10):
        print(f"  {ur:6s} -> {vr:6s} ({c}x)")
        region_results.append({"from": ur, "to": vr, "count": c})

    # === Isolation by topic ===
    print("\n=== Isolation ratio by topic (highest first, topics with 10+ notes) ===")
    topic_nodes = defaultdict(set)
    for n, nd in G.nodes(data=True):
        topic_nodes[nd.get("topic", "")].add(n)
    iso_by_topic = []
    for t, ns in topic_nodes.items():
        if len(ns) < 10 or not t:
            continue
        iso = sum(1 for n in ns if UG.degree(n) == 0)
        iso_by_topic.append({"topic": t, "total": len(ns), "isolated": iso, "ratio": iso / len(ns)})
    iso_by_topic.sort(key=lambda x: -x["ratio"])
    for x in iso_by_topic[:8]:
        print(f"  {x['topic']:32s} isolated={x['isolated']:3d}/{x['total']:3d}  ({x['ratio']*100:.1f}%)")

    # === 保存详细分析 ===
    analytics = {
        "summary": {
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges(),
            "density": nx.density(G),
            "wcc_count": len(wcc),
            "wcc_largest": len(wcc[0]) if wcc else 0,
            "wcc_singletons": sum(1 for c in wcc if len(c) == 1),
        },
        "top_pagerank": pr_results,
        "top_betweenness": betw_results,
        "cross_topic_edges": cross_topic_results,
        "region_flow": region_results,
        "isolation_by_topic": iso_by_topic,
        "top_components": [
            {
                "size": len(c),
                "sample": list(c)[:10],
            }
            for c in wcc[:10]
        ],
    }
    (STAGE5 / "graph_analytics.json").write_text(
        json.dumps(analytics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nWrote {STAGE5 / 'graph_analytics.json'}")


if __name__ == "__main__":
    main()
