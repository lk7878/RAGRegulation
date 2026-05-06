"""
Stage 5b —— 语义检索（BM25 + jieba）。

设计：
  - 扫描所有 1429 条 notes，建 jieba 分词后的 BM25 索引
  - 索引字段：reg_id (权重 3) + title (3) + title_en (2) + scope (1) + summary (1) + topic (1)
  - 支持 region / topic / status 过滤
  - Top-N 结果含 score 和字段高亮
  - 第一次运行自动建索引，后续查询走缓存（pickle）

用法：
  python _semantic_search.py "国六 轻型车 排放"
  python _semantic_search.py "ALKS 自动车道保持" --topic adas_driver_assist
  python _semantic_search.py "儿童约束" --region cn --limit 5
  python _semantic_search.py --rebuild    # 强制重建索引

索引缓存：.stage5/bm25_index.pkl
"""
from __future__ import annotations

import argparse
import pickle
import re
import sys
from pathlib import Path
from typing import Optional

import jieba
import yaml
from rank_bm25 import BM25Okapi

ROOT = Path(__file__).parent
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
INDEX_PATH = ROOT / ".stage5" / "bm25_index.pkl"

# 字段权重 —— 复制到 tokens 中使高权重字段被重复计数
FIELD_WEIGHTS = {
    "reg_id": 3,
    "title": 3,
    "title_en": 2,
    "summary": 1,
    "scope": 1,
    "topic": 1,
}


def tokenize(text: str) -> list[str]:
    """中英文混合分词。"""
    if not text:
        return []
    # 清理
    text = re.sub(r"[^\w\s\u4e00-\u9fff/.-]", " ", str(text).lower())
    tokens = list(jieba.cut_for_search(text))
    return [t.strip() for t in tokens if t.strip() and len(t.strip()) > 0]


def load_cluster_topic() -> dict[str, str]:
    import json
    p = ROOT / ".stage4" / "cluster_assignment.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    out = {}
    for topic, records in d.items():
        for r in records:
            if r.get("path"):
                out[r["path"]] = topic
    return out


def build_index() -> dict:
    """扫 WIKI，构建 BM25 索引。"""
    print(f"Building BM25 index from {WIKI}...")
    topics = load_cluster_topic()
    docs = []  # [token_list, ...]
    meta = []  # [{path, reg_id, title, ...}, ...]
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

        fields = {
            "reg_id": str(fm.get("reg_id") or ""),
            "title": str(fm.get("title") or ""),
            "title_en": str(fm.get("title_en") or ""),
            "summary": str(fm.get("summary") or "")[:500],
            "scope": str(fm.get("scope") or "")[:300],
            "topic": topics.get(str(p), ""),
        }

        # Tokens（含字段权重）
        all_tokens = []
        for k, w in FIELD_WEIGHTS.items():
            toks = tokenize(fields[k])
            all_tokens.extend(toks * w)
        if not all_tokens:
            continue

        docs.append(all_tokens)
        meta.append({
            "path": str(p),
            "reg_id": fields["reg_id"],
            "title": fields["title"],
            "title_en": fields["title_en"][:100],
            "summary": fields["summary"][:200],
            "region": fm.get("region", ""),
            "status": fm.get("status", ""),
            "topic": fields["topic"],
            "confidence": fm.get("cross_check_overall_confidence", ""),
            "publication_date": str(fm.get("publication_date") or ""),
        })

    print(f"  Indexed {len(docs)} notes")
    bm25 = BM25Okapi(docs)
    index = {"bm25": bm25, "docs": docs, "meta": meta}
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_PATH, "wb") as f:
        pickle.dump(index, f)
    print(f"  Saved to {INDEX_PATH}")
    return index


def load_or_build() -> dict:
    if INDEX_PATH.exists():
        try:
            with open(INDEX_PATH, "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    return build_index()


def search(
    index: dict,
    query: str,
    *,
    limit: int = 10,
    region: Optional[str] = None,
    topic: Optional[str] = None,
    status: Optional[str] = None,
    min_confidence: Optional[str] = None,
) -> list[dict]:
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    bm25 = index["bm25"]
    meta = index["meta"]
    scores = bm25.get_scores(q_tokens)

    # 过滤
    conf_order = {"high": 3, "medium": 2, "low": 1, "unknown": 0, "": 0}
    min_conf_score = conf_order.get(min_confidence or "", 0)

    filtered = []
    for i, s in enumerate(scores):
        if s <= 0:
            continue
        m = meta[i]
        if region and m["region"] != region:
            continue
        if topic and m["topic"] != topic:
            continue
        if status and m["status"] != status:
            continue
        if conf_order.get(m["confidence"], 0) < min_conf_score:
            continue
        filtered.append({**m, "score": float(s)})

    filtered.sort(key=lambda x: -x["score"])
    return filtered[:limit]


def print_results(results: list[dict], query: str):
    from rich.console import Console

    console = Console()
    if not results:
        console.print(f"[yellow]No results for: [bold]{query}[/bold][/yellow]")
        return

    console.print(f"\n[bold cyan]Top {len(results)} for: {query}[/bold cyan]\n")
    for i, r in enumerate(results, 1):
        title = r["title"] or r["title_en"] or "[no title]"
        if len(title) > 80:
            title = title[:77] + "…"
        console.print(
            f"  [dim]{i:>2}.[/dim] "
            f"[green]{r['score']:5.2f}[/green] "
            f"[cyan]{r['reg_id']:<30}[/cyan] "
            f"[yellow]{r['topic'][:20]:<20}[/yellow] "
            f"[dim]{r['region']:<4}[/dim] "
            f"{title}"
        )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", help="Natural language query (中英文均可)")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--region", help="Filter by region (cn/ece/eu/...)")
    ap.add_argument("--topic", help="Filter by topic key")
    ap.add_argument("--status", help="Filter by status (active/superseded/...)")
    ap.add_argument("--min-confidence", choices=["high", "medium", "low"])
    ap.add_argument("--rebuild", action="store_true", help="Force rebuild index")
    args = ap.parse_args()

    if args.rebuild:
        INDEX_PATH.unlink(missing_ok=True)

    index = load_or_build()

    if not args.query:
        print("Index ready. Use: python _semantic_search.py \"your query\"")
        print(f"Corpus size: {len(index['meta'])} notes")
        return 0

    results = search(
        index,
        args.query,
        limit=args.limit,
        region=args.region,
        topic=args.topic,
        status=args.status,
        min_confidence=args.min_confidence,
    )
    print_results(results, args.query)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
