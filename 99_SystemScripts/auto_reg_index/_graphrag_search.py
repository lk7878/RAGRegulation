"""
Stage 5d — GraphRAG · 层级检索

把查询先路由到最相关的社区，再在社区成员内做细粒度匹配。
相比普通 BM25 的优势：命中后能看到 **该领域的整体综述**，而不仅仅是单条法规命中。

流程：
  1. 查询 tokenize（jieba）
  2. 在 community_*.md 的 label + 正文段（1/2/3/4）上做 BM25，得 top-K 社区
  3. 对每个命中社区，用 _semantic_search.py 的索引在其 members 上做 BM25，列 top-J notes
  4. 渲染：社区摘要（label、core_nodes、摘要前 300 字） + 细粒度 notes

用法：
  python _graphrag_search.py "刹车踏板行程"
  python _graphrag_search.py "LED 前照灯" --topk-communities 3 --topk-notes 5
  python _graphrag_search.py "国六 轻型车" --region cn
"""
from __future__ import annotations

import argparse
import pickle
import re
from pathlib import Path

import jieba
import yaml
from rank_bm25 import BM25Okapi

ROOT = Path(__file__).parent
VAULT = Path(r"D:\CcVault")
COMM_DIR = VAULT / "04_Topics" / "communities"
NOTES_INDEX_PATH = ROOT / ".stage5" / "bm25_index.pkl"


# ----------------------------------------------------------------------------
# tokenize（与 _semantic_search.py 一致）
# ----------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    if not text:
        return []
    text = re.sub(r"[^\w\s\u4e00-\u9fff/.-]", " ", str(text).lower())
    tokens = list(jieba.cut_for_search(text))
    return [t.strip() for t in tokens if t.strip()]


# ----------------------------------------------------------------------------
# 社区索引（in-memory，每次运行时重建，社区数少）
# ----------------------------------------------------------------------------

FM_SPLIT_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$")


def _extract_sections(body: str) -> str:
    """提取综述中"概要性"段落（第 1/2/3/4 节），去掉 mermaid 图，合成一段纯文本。"""
    # 去 mermaid
    body = re.sub(r"```mermaid[\s\S]*?```", "", body)
    # 只留 ## 1. ## 2. ## 3. ## 4. 四段
    parts = re.findall(r"## [1-4]\..*?(?=\n## |\Z)", body, re.DOTALL)
    merged = "\n".join(parts)
    # 去 markdown wikilink 语法括号，保留文本
    merged = re.sub(r"\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), merged)
    return merged


def build_community_index(comm_dir: Path = COMM_DIR) -> dict:
    if not comm_dir.exists():
        raise FileNotFoundError(f"社区目录不存在：{comm_dir}。先跑 _graphrag_summarize.py")

    meta: list[dict] = []
    docs: list[list[str]] = []
    for p in sorted(comm_dir.glob("community_*.md")):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = FM_SPLIT_RE.match(txt)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        body = m.group(2)

        # 社区检索权重：label × 4 + core_nodes × 3 + 正文抽要 × 1
        label = str(fm.get("label") or "")
        core_nodes = fm.get("core_nodes") or []
        core_text = " ".join(re.sub(r"[\[\]]", "", str(x)) for x in core_nodes)
        sections = _extract_sections(body)[:2000]

        weighted = f"{label} " * 4 + f"{core_text} " * 3 + sections
        tokens = tokenize(weighted)
        if not tokens:
            continue
        meta.append({
            "community_id": fm.get("community_id", -1),
            "label": label,
            "core_nodes": core_nodes,
            "member_count": fm.get("member_count", 0),
            "edge_count": fm.get("edge_count", 0),
            "top_region": fm.get("top_region", ""),
            "top_topic": fm.get("top_topic", ""),
            "path": str(p),
            "body_preview": sections[:350].strip(),
        })
        docs.append(tokens)

    if not docs:
        raise RuntimeError("没有任何有效的 community markdown 可索引")
    return {"meta": meta, "bm25": BM25Okapi(docs)}


# ----------------------------------------------------------------------------
# Notes 索引（复用 _semantic_search.py 产出的 pickle）
# ----------------------------------------------------------------------------

def load_notes_index() -> dict | None:
    if not NOTES_INDEX_PATH.exists():
        return None
    try:
        with NOTES_INDEX_PATH.open("rb") as f:
            return pickle.load(f)
    except Exception:
        return None


def _get_community_members(community_path: str) -> set[str]:
    """从 community_*.md 正文的「## 1. 成员总览」抽出 wikilink 成员 reg_id。"""
    try:
        txt = Path(community_path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return set()
    # 抓「## 1. 成员总览」段
    m = re.search(r"##\s*1\..*?\n([\s\S]*?)(?=\n##\s|\Z)", txt)
    if not m:
        return set()
    seg = m.group(1)
    return set(re.findall(r"\[\[([^\]|#]+)", seg))


# ----------------------------------------------------------------------------
# 查询
# ----------------------------------------------------------------------------

def search_communities(
    index: dict,
    query: str,
    *,
    topk: int = 3,
    region_filter: str | None = None,
) -> list[dict]:
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    scores = index["bm25"].get_scores(q_tokens)
    ranked = sorted(zip(scores, index["meta"]), key=lambda x: x[0], reverse=True)
    out: list[dict] = []
    for score, m in ranked:
        if score <= 0:
            continue
        if region_filter and m["top_region"] != region_filter:
            continue
        out.append({**m, "score": round(float(score), 3)})
        if len(out) >= topk:
            break
    return out


def search_notes_in_members(
    notes_idx: dict | None,
    members: set[str],
    query: str,
    *,
    topk: int = 5,
) -> list[dict]:
    """在 notes BM25 索引里只看社区成员，返回 top-K。"""
    if not notes_idx or not members:
        return []
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    bm25 = notes_idx.get("bm25")
    meta = notes_idx.get("meta") or []
    if bm25 is None or not meta:
        return []

    scores = bm25.get_scores(q_tokens)
    ranked = sorted(zip(scores, meta), key=lambda x: x[0], reverse=True)

    out: list[dict] = []
    for score, m in ranked:
        if score <= 0:
            break
        rid = m.get("reg_id") or ""
        if rid and rid in members:
            out.append({
                "reg_id": rid,
                "title": m.get("title", ""),
                "region": m.get("region", ""),
                "score": round(float(score), 3),
                "path": m.get("path", ""),
            })
        if len(out) >= topk:
            break
    return out


# ----------------------------------------------------------------------------
# 渲染
# ----------------------------------------------------------------------------

def render(
    query: str,
    communities: list[dict],
    note_hits_per_community: dict[int, list[dict]],
):
    print(f"\n🔍 Query: {query!r}")
    if not communities:
        print("  未找到相关社区。尝试降级到直接 BM25（_semantic_search.py）。")
        return

    for i, c in enumerate(communities, 1):
        print()
        print(f"[{i}] Community #{c['community_id']:03d}  {c['label']}")
        print(f"    score={c['score']} | {c['member_count']} 成员 / {c['edge_count']} 边 "
              f"| {c['top_region']}/{c['top_topic']}")
        if c["core_nodes"]:
            print(f"    核心：{', '.join(str(x) for x in c['core_nodes'])}")
        if c["body_preview"]:
            preview = c["body_preview"].replace("\n", " ")
            print(f"    摘要：{preview[:200]}...")
        print(f"    → 完整综述：{Path(c['path']).as_posix()}")

        hits = note_hits_per_community.get(c["community_id"], [])
        if hits:
            print(f"    社区内 top-{len(hits)} 相关法规：")
            for h in hits:
                print(f"      - {h['reg_id']:28s} ({h['region']}) score={h['score']}  {h['title'][:45]}")


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="自然语言查询")
    ap.add_argument("--topk-communities", "-C", type=int, default=3,
                    help="返回 top-N 社区（默认 3）")
    ap.add_argument("--topk-notes", "-N", type=int, default=5,
                    help="每个社区内返回 top-N 法规（默认 5）")
    ap.add_argument("--region", default=None, help="过滤社区主导区域")
    args = ap.parse_args()

    comm_idx = build_community_index()
    notes_idx = load_notes_index()

    cs = search_communities(
        comm_idx, args.query,
        topk=args.topk_communities,
        region_filter=args.region,
    )

    note_hits: dict[int, list[dict]] = {}
    for c in cs:
        members = _get_community_members(c["path"])
        note_hits[c["community_id"]] = search_notes_in_members(
            notes_idx, members, args.query, topk=args.topk_notes
        )

    render(args.query, cs, note_hits)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
