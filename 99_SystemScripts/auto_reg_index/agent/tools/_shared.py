"""Agent tools 共享工具。

关键决策：
  - 所有工具返回 **字符串**，LLM 看得懂；限制最大长度避免炸 context
  - FM 解析一次缓存在 module-level _FM_CACHE，多个 tool 共用
  - reg_id 查找支持精确 + 模糊，降低幻觉
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Optional

import yaml

# ---------------------------------------------------------------------------
# 路径常量
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent.parent                  # auto_reg_index/
VAULT = Path(r"D:\CcVault")
WIKI = VAULT / "01_Wiki" / "regulations"
TOPICS_DIR = VAULT / "04_Topics"
COMM_DIR = TOPICS_DIR / "communities"
EQUIV_DIR = VAULT / "03_Equivalence"
DASHBOARDS_DIR = VAULT / "00_Dashboards"

# ---------------------------------------------------------------------------
# 输出长度守门
# ---------------------------------------------------------------------------
MAX_TOOL_OUTPUT = 4000    # 单个 tool 返回字符上限（防 context 爆炸）


def truncate(text: str, limit: int = MAX_TOOL_OUTPUT, tail: str = "\n…[truncated]") -> str:
    """兜底截断。"""
    if not text:
        return text
    if len(text) <= limit:
        return text
    return text[: limit - len(tail)] + tail


# ---------------------------------------------------------------------------
# FM 加载（缓存）
# ---------------------------------------------------------------------------
FM_SPLIT_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$")

# path -> (fm_dict, body_str)
_FM_CACHE: dict[str, tuple[dict, str]] = {}


def parse_note(path: Path) -> tuple[dict, str]:
    """解析 note：返回 (frontmatter dict, body text)。空 FM 返回 ({}, body)。"""
    key = str(path)
    if key in _FM_CACHE:
        return _FM_CACHE[key]
    try:
        txt = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ({}, "")
    m = FM_SPLIT_RE.match(txt)
    if not m:
        _FM_CACHE[key] = ({}, txt)
        return ({}, txt)
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    body = m.group(2)
    _FM_CACHE[key] = (fm, body)
    return (fm, body)


@lru_cache(maxsize=1)
def _load_cluster_topic() -> dict[str, str]:
    """从 .stage4/cluster_assignment.json 读 path -> topic 映射。

    与 _semantic_search.py:load_cluster_topic 一致。
    """
    import json
    p = ROOT / ".stage4" / "cluster_assignment.json"
    if not p.exists():
        return {}
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    out = {}
    for topic, records in d.items():
        for r in records or []:
            if isinstance(r, dict) and r.get("path"):
                out[r["path"]] = topic
    return out


@lru_cache(maxsize=1)
def load_all_notes() -> list[dict]:
    """扫 01_Wiki/regulations 全量，返回 [{path, fm, ...}, ...]。缓存一次。

    topic 字段优先从 .stage4/cluster_assignment.json 读（权威来源），
    FM 里的 topic/tags 作为兜底。
    """
    topic_map = _load_cluster_topic()
    out = []
    for p in WIKI.rglob("*.md"):
        fm, _body = parse_note(p)
        if not fm:
            continue
        path_str = str(p)
        # topic 解析：cluster_assignment > FM.topic > FM.tags 里形如 topic/xxx 的标签
        topic = topic_map.get(path_str) or ""
        if not topic:
            fm_topic = fm.get("topic")
            if isinstance(fm_topic, str):
                topic = fm_topic
        if not topic:
            tags = fm.get("tags") or []
            if isinstance(tags, list):
                for t in tags:
                    if isinstance(t, str) and t.startswith("topic/"):
                        topic = t.split("/", 1)[1]
                        break

        out.append({
            "path": path_str,
            "reg_id": str(fm.get("reg_id") or ""),
            "title": str(fm.get("title") or ""),
            "title_en": str(fm.get("title_en") or ""),
            "region": str(fm.get("region") or ""),
            "status": str(fm.get("status") or ""),
            "topic": topic,
            "publication_date": str(fm.get("publication_date") or ""),
            "effective_date": str(fm.get("effective_date") or ""),
            "confidence": str(fm.get("cross_check_overall_confidence") or ""),
            "equivalent_to": fm.get("equivalent_to") or [],
            "supersedes": fm.get("supersedes") or [],
            "superseded_by": fm.get("superseded_by") or [],
            "fm": fm,
        })
    return out


# ---------------------------------------------------------------------------
# reg_id 匹配（用于 read / equivalence / supersession）
# ---------------------------------------------------------------------------

def normalize_reg_id(rid: str) -> str:
    """把 'GB4785-2019' 和 'GB 4785-2019' 统一到去空格小写形式。"""
    return re.sub(r"\s+", "", (rid or "").lower())


def find_note_by_reg_id(reg_id: str) -> Optional[dict]:
    """精确匹配优先，失败降级到"去空格小写"匹配。"""
    if not reg_id:
        return None
    notes = load_all_notes()
    for n in notes:
        if n["reg_id"] == reg_id:
            return n
    target = normalize_reg_id(reg_id)
    for n in notes:
        if normalize_reg_id(n["reg_id"]) == target:
            return n
    return None


# ---------------------------------------------------------------------------
# 检索索引（懒加载）
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1)
def load_bm25_index() -> Optional[dict]:
    """加载 _semantic_search.py 产出的 BM25 索引。找不到返回 None。"""
    import pickle
    p = ROOT / ".stage5" / "bm25_index.pkl"
    if not p.exists():
        return None
    try:
        with p.open("rb") as f:
            return pickle.load(f)
    except Exception:
        return None


@lru_cache(maxsize=1)
def load_community_index() -> Optional[dict]:
    """加载 GraphRAG 社区 BM25 索引（运行时构建，无持久化）。"""
    try:
        import sys
        sys.path.insert(0, str(ROOT))
        from _graphrag_search import build_community_index  # type: ignore
        return build_community_index()
    except Exception as e:
        print(f"[warn] load_community_index failed: {e}")
        return None


# ---------------------------------------------------------------------------
# 格式化辅助
# ---------------------------------------------------------------------------

def fmt_note_line(n: dict, *, score: Optional[float] = None, width_rid: int = 28) -> str:
    """单行展示一个 note：reg_id | region | topic | title。"""
    title = n.get("title") or n.get("title_en") or "[no title]"
    if len(title) > 60:
        title = title[:57] + "…"
    prefix = f"{score:5.2f}  " if score is not None else ""
    return (
        f"  {prefix}"
        f"{(n.get('reg_id') or ''):<{width_rid}} "
        f"({n.get('region', ''):<4}) "
        f"[{n.get('topic', '')[:22]:<22}] "
        f"{title}"
    )


def fmt_kv_table(title: str, rows: list[tuple[str, object]]) -> str:
    """KV 表格式渲染，tool 输出常用。"""
    lines = [title, "-" * len(title)]
    width = max((len(k) for k, _ in rows), default=0) + 1
    for k, v in rows:
        lines.append(f"  {k:<{width}}: {v}")
    return "\n".join(lines)
