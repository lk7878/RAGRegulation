"""
Stage 5a — 关系图构建与分析

从 1444 notes FM 提取所有关系边：
  - supersedes / superseded_by（时序）
  - equivalent_to（跨区域）
  - references（引用其他标准）
  - related（横向关联）

输出：
  1. .stage5/graph.graphml         — 可用 Gephi/Cytoscape 打开
  2. .stage5/graph_stats.json      — 度分布/中心度/孤立节点/组件
  3. .stage5/graph.json            — 节点+边 JSON（便于后续脚本复用）

用法：
  python _build_graph.py [--min-degree 1] [--include-orphans]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
OUT_DIR = ROOT / ".stage5"
OUT_DIR.mkdir(exist_ok=True)

_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")
_SPLIT_RE = re.compile(r"[,，、;；]\s*")


def normalize_ref(s: str) -> str:
    """把任意引用字符串规整为匹配 reg_id 的形式。"""
    s = s.strip()
    # 剥 wikilink
    m = _WIKILINK_RE.match(s)
    if m:
        s = m.group(1).strip()
    # 去掉标题后缀（取首个 token 组合）
    # 如 "GB 11562 汽车驾驶员前方视野要求及测量方法" -> "GB 11562"
    # 如 "GB/T 11563 汽车H点确定程序" -> "GB/T 11563"
    m = re.match(r"^(GB(?:/T)?|Q/[A-Z]+|JT|HJ|ZB[A-Z]?|SY|QC|CNCA-C\d+-\d+|DB[A-Z]*)\s+[\d\.\-/]+(?:-\d+)?", s)
    if m:
        return m.group(0).strip()
    # ECE/UN R 号
    m = re.match(r"^(ECE\s*|UN\s*)?R\s*0?\d+[\w.\- ]*", s, re.IGNORECASE)
    if m:
        out = m.group(0).strip()
        if not out.lower().startswith(("ece", "un")):
            out = "UN " + out
        return out
    # ISO / SAE / EN / DIN
    m = re.match(r"^(ISO|IEC|SAE|EN|DIN|JIS|FMVSS|JSO)\s*[\w\d\-:.\s]*", s, re.IGNORECASE)
    if m:
        return m.group(0).strip()
    return s


def parse_list(v) -> list[str]:
    """把任意 FM 值转为字符串列表。"""
    if not v:
        return []
    items = []
    if isinstance(v, str):
        parts = _SPLIT_RE.split(v) if not _WIKILINK_RE.search(v) else [m.group(1) for m in _WIKILINK_RE.finditer(v)]
        items = [p.strip() for p in parts if p.strip()]
    elif isinstance(v, list):
        for x in v:
            if isinstance(x, str):
                if _WIKILINK_RE.search(x):
                    items.extend(m.group(1).strip() for m in _WIKILINK_RE.finditer(x))
                else:
                    items.extend(p.strip() for p in _SPLIT_RE.split(x) if p.strip())
            elif isinstance(x, dict):
                ref = x.get("ref") or x.get("reg_id") or x.get("target")
                if ref:
                    items.append(str(ref).strip())
    return items


def _load_cluster_assignment() -> dict[str, str]:
    """从 .stage4/cluster_assignment.json 读取 path -> cluster_topic 映射。"""
    p = ROOT / ".stage4" / "cluster_assignment.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for topic, records in d.items():
        for r in records:
            path = r.get("path")
            if path:
                out[path] = topic
    return out


def load_vault() -> dict[str, dict]:
    """返回 reg_id -> node data 映射。"""
    cluster_topic = _load_cluster_assignment()
    nodes: dict[str, dict] = {}
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
        if not reg_id:
            continue
        # 多文件同 reg_id 时（_dupN）取第一个
        if reg_id in nodes:
            continue
        nodes[reg_id] = {
            "reg_id": reg_id,
            "path": str(p),
            "region": fm.get("region", "unknown"),
            "type": fm.get("type", "unknown"),
            "status": fm.get("status", "unknown"),
            "title": fm.get("title") or fm.get("title_en") or "",
            "date": str(fm.get("publication_date") or ""),
            "confidence": fm.get("cross_check_overall_confidence", "unknown"),
            "topic": cluster_topic.get(str(p), ""),  # Stage 4 聚类结果
            "_fm": fm,
        }
    return nodes


def build_edges(nodes: dict[str, dict]) -> list[dict]:
    """从 nodes 的 FM 构造所有关系边。"""
    edges: list[dict] = []
    for reg_id, node in nodes.items():
        fm = node["_fm"]

        for tgt in parse_list(fm.get("supersedes")):
            edges.append({
                "src": reg_id,
                "dst": normalize_ref(tgt),
                "rel": "supersedes",
            })
        for tgt in parse_list(fm.get("superseded_by")):
            edges.append({
                "src": reg_id,
                "dst": normalize_ref(tgt),
                "rel": "superseded_by",
            })
        # equivalent_to 可能含 dict
        eq = fm.get("equivalent_to")
        if isinstance(eq, list):
            for x in eq:
                if isinstance(x, dict):
                    ref = x.get("ref") or x.get("reg_id")
                    if ref:
                        edges.append({
                            "src": reg_id,
                            "dst": normalize_ref(str(ref)),
                            "rel": "equivalent_to",
                            "relation": x.get("relation", "equivalent"),
                        })
                elif isinstance(x, str):
                    edges.append({
                        "src": reg_id,
                        "dst": normalize_ref(x),
                        "rel": "equivalent_to",
                    })
        for tgt in parse_list(fm.get("references")):
            edges.append({
                "src": reg_id,
                "dst": normalize_ref(tgt),
                "rel": "references",
            })
        for tgt in parse_list(fm.get("related")):
            edges.append({
                "src": reg_id,
                "dst": normalize_ref(tgt),
                "rel": "related",
            })
    return edges


def _family_key(reg_id: str) -> str | None:
    """从 reg_id 提取 'family' 键，供模糊匹配。
    例：'UN R48 Rev6 Am5' -> 'un:r48'
        'GB 11551-2003'    -> 'gb:11551'
        'GB/T 15089-2001'  -> 'gb/t:15089'
        'ECE R48'          -> 'un:r48'
    """
    s = reg_id.strip().lower()
    # UN/ECE R 号
    m = re.match(r"^(ece|un)\s*r\s*0?(\d+)", s)
    if m:
        return f"un:r{m.group(2)}"
    # GB / GB/T 数字-年
    m = re.match(r"^(gb(?:/t)?)\s*(\d+(?:\.\d+)?)", s)
    if m:
        return f"{m.group(1)}:{m.group(2)}"
    # ISO / EN / SAE / FMVSS 数字
    m = re.match(r"^(iso|en|sae|din|fmvss|jis|iec|jt|hj|qc)\s*([\w\d\-]+)", s)
    if m:
        return f"{m.group(1)}:{m.group(2).split('-')[0]}"
    # EU yyyy/nn
    m = re.match(r"^eu\s*(\d+/\d+)", s)
    if m:
        return f"eu:{m.group(1)}"
    return None


def resolve_edges(edges: list[dict], nodes: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    """
    把目标解析到现有节点。返回 (resolved_edges, dangling_edges)。
    resolved: dst 存在于 vault（精确或 family-level 匹配）
    dangling: dst 在 vault 外（dead ref / external standard）
    """
    node_ids = set(nodes.keys())

    # 精确归一
    loose_map: dict[str, str] = {}
    for rid in node_ids:
        loose_map.setdefault(rid.lower().replace(" ", ""), rid)

    # Family-level：fam_key -> 按日期选"主代表节点"（最新版本）
    family_map: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for rid, n in nodes.items():
        fk = _family_key(rid)
        if fk:
            family_map[fk].append((rid, str(n.get("date") or "")))

    family_repr: dict[str, str] = {}
    for fk, entries in family_map.items():
        # 按日期降序，取最新；无日期的放后面
        entries.sort(key=lambda x: (x[1] or "0000-00-00"), reverse=True)
        family_repr[fk] = entries[0][0]

    def _find(dst: str) -> str | None:
        if dst in node_ids:
            return dst
        key = dst.lower().replace(" ", "")
        if key in loose_map:
            return loose_map[key]
        fk = _family_key(dst)
        if fk and fk in family_repr:
            return family_repr[fk]
        return None

    resolved, dangling = [], []
    for e in edges:
        hit = _find(e["dst"])
        if hit:
            e2 = dict(e)
            e2["dst_original"] = e["dst"]
            e2["dst"] = hit
            e2["resolution"] = "exact" if e["dst"] == hit else "family"
            resolved.append(e2)
        else:
            dangling.append(e)
    return resolved, dangling


def compute_stats(nodes, resolved, dangling):
    """度分布 / 孤立点 / 简单中心度。"""
    in_deg = Counter()
    out_deg = Counter()
    rel_count = Counter()
    for e in resolved:
        in_deg[e["dst"]] += 1
        out_deg[e["src"]] += 1
        rel_count[e["rel"]] += 1

    isolated = [rid for rid in nodes if in_deg[rid] == 0 and out_deg[rid] == 0]
    # Hubs
    top_in = in_deg.most_common(25)
    top_out = out_deg.most_common(25)

    # Dangling targets by category
    dangling_targets = Counter(e["dst"] for e in dangling)

    return {
        "nodes_total": len(nodes),
        "edges_resolved": len(resolved),
        "edges_dangling": len(dangling),
        "edges_by_rel": dict(rel_count),
        "isolated_nodes": len(isolated),
        "top_in_degree": [{"reg_id": r, "in_deg": d} for r, d in top_in],
        "top_out_degree": [{"reg_id": r, "out_deg": d} for r, d in top_out],
        "top_dangling_targets": [{"target": t, "count": c} for t, c in dangling_targets.most_common(30)],
    }


def write_graphml(path: Path, nodes: dict[str, dict], edges: list[dict]):
    """导出 GraphML 供 Gephi/Cytoscape/yEd 使用。"""
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
        '  <key id="region" for="node" attr.name="region" attr.type="string"/>',
        '  <key id="topic" for="node" attr.name="topic" attr.type="string"/>',
        '  <key id="status" for="node" attr.name="status" attr.type="string"/>',
        '  <key id="title" for="node" attr.name="title" attr.type="string"/>',
        '  <key id="confidence" for="node" attr.name="confidence" attr.type="string"/>',
        '  <key id="rel" for="edge" attr.name="rel" attr.type="string"/>',
        '  <graph id="G" edgedefault="directed">',
    ]
    for rid, n in nodes.items():
        safe_id = rid.replace('"', "&quot;").replace("&", "&amp;")
        title = (n.get("title") or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")[:120]
        lines.append(f'    <node id="{safe_id}">')
        lines.append(f'      <data key="region">{n["region"]}</data>')
        lines.append(f'      <data key="topic">{n["topic"]}</data>')
        lines.append(f'      <data key="status">{n["status"]}</data>')
        lines.append(f'      <data key="title">{title}</data>')
        lines.append(f'      <data key="confidence">{n["confidence"]}</data>')
        lines.append("    </node>")
    for i, e in enumerate(edges):
        s = e["src"].replace('"', "&quot;").replace("&", "&amp;")
        d = e["dst"].replace('"', "&quot;").replace("&", "&amp;")
        lines.append(f'    <edge id="e{i}" source="{s}" target="{d}">')
        lines.append(f'      <data key="rel">{e["rel"]}</data>')
        lines.append("    </edge>")
    lines.append("  </graph>")
    lines.append("</graphml>")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-degree", type=int, default=0,
                    help="export 时只保留 degree >= N 的节点（仅影响 graphml）")
    args = ap.parse_args()

    print("Loading vault...")
    nodes = load_vault()
    print(f"  {len(nodes)} unique reg_ids")

    print("Building edges from FM relations...")
    raw_edges = build_edges(nodes)
    print(f"  {len(raw_edges)} raw edges")

    print("Resolving edges against vault...")
    resolved, dangling = resolve_edges(raw_edges, nodes)
    print(f"  resolved: {len(resolved)}, dangling (external refs): {len(dangling)}")

    stats = compute_stats(nodes, resolved, dangling)
    print("\n=== Stats ===")
    print(f"Nodes: {stats['nodes_total']}, edges resolved: {stats['edges_resolved']}")
    print(f"Edges by relation: {stats['edges_by_rel']}")
    print(f"Isolated nodes (0 in + 0 out): {stats['isolated_nodes']} ({stats['isolated_nodes']*100//stats['nodes_total']}%)")

    print("\n=== Top 10 most-cited (in-degree) ===")
    for x in stats["top_in_degree"][:10]:
        print(f"  {x['reg_id']:35s} in={x['in_deg']}")
    print("\n=== Top 10 most-citing (out-degree) ===")
    for x in stats["top_out_degree"][:10]:
        print(f"  {x['reg_id']:35s} out={x['out_deg']}")
    print("\n=== Top 10 dangling refs ===")
    for x in stats["top_dangling_targets"][:10]:
        print(f"  {x['target']:40s} ({x['count']}×)")

    # Filter by min-degree for GraphML
    if args.min_degree > 0:
        deg = Counter()
        for e in resolved:
            deg[e["src"]] += 1
            deg[e["dst"]] += 1
        keep = {rid for rid, d in deg.items() if d >= args.min_degree}
        filtered_nodes = {k: v for k, v in nodes.items() if k in keep}
        filtered_edges = [e for e in resolved if e["src"] in keep and e["dst"] in keep]
    else:
        filtered_nodes = nodes
        filtered_edges = resolved

    # Drop _fm from stored nodes (too large, raw data)
    export_nodes = {k: {kk: vv for kk, vv in v.items() if kk != "_fm"} for k, v in filtered_nodes.items()}

    print(f"\nExporting: {len(filtered_nodes)} nodes, {len(filtered_edges)} edges")

    (OUT_DIR / "graph.json").write_text(
        json.dumps({"nodes": export_nodes, "edges": filtered_edges}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    (OUT_DIR / "graph_stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    write_graphml(OUT_DIR / "graph.graphml", filtered_nodes, filtered_edges)

    print(f"\nWrote:")
    print(f"  {OUT_DIR / 'graph.json'}")
    print(f"  {OUT_DIR / 'graph_stats.json'}")
    print(f"  {OUT_DIR / 'graph.graphml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
