"""
Stage 3：从 04_Topics 下每个主题页的 "跨区域速查" + Overview 正文提取 GB↔ECE 对应关系。

解析规则：
- 匹配 "`GB XXXX` ≈ `ECE RNN`" / "`GB XXXX` ≈ `ECE RNN` + `EU YYYY`" / "`GB XXX` 无 ECE 直接对应" 等模式
- 支持多目标 (`ECE A + B` 合并形式)
- 输出有向边 + 关系描述

输出：
- .stage3/curated_equivalences.json — 从主题页抽取的映射（高质量）
- .stage3/curated_equivalences.yaml — 便于 Obsidian 阅读
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

TOPIC_DIR = Path(r"D:\CcVault\04_Topics")
OUT_DIR = Path(__file__).parent / ".stage3"
OUT_DIR.mkdir(exist_ok=True)


# 正则：匹配反引号中的 reg_id
_BACKTICK_REG_RE = re.compile(r"`([A-Z/]+[A-Z\s]*[\w.\-/]+)`")

# 整行匹配 "- `src` ≈ `target` + `target` ...（描述）"
_LINE_EQ_RE = re.compile(
    r"^\s*[-•]\s*`(?P<src>[^`]+)`\s*(?P<op>≈|等[效同于]|=|对应)\s*(?P<rest>.+?)$"
)
# "- `src` 无 ECE 直接对应"
_LINE_NEG_RE = re.compile(
    r"^\s*[-•]\s*`(?P<src>[^`]+)`\s*[^≈]*?(无\s*(ECE|EU|ISO|国际)[^，]*?(直接)?对应|无\s*[^，]*?等效)"
)


def parse_topic_page(path: Path) -> list[dict]:
    """抽取一个主题页的所有 equivalence 边。返回 [{src, targets, relation, context_topic, line}]。"""
    edges = []
    topic_key = path.stem.split(" - ", 1)[0]
    try:
        txt = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return edges

    # 遍历每一行
    for line in txt.split("\n"):
        line_strip = line.strip()
        # 负向：明确说"无对应"
        m_neg = _LINE_NEG_RE.match(line_strip)
        if m_neg:
            src = m_neg.group("src")
            edges.append({
                "src": src,
                "targets": [],
                "relation": "no_direct_match",
                "topic": topic_key,
                "line": line_strip[:200],
            })
            continue

        # 正向：src ≈ targets
        m = _LINE_EQ_RE.match(line_strip)
        if not m:
            continue
        src = m.group("src").strip()
        rest = m.group("rest")
        # 提取 rest 中所有反引号内容作为 targets
        targets = _BACKTICK_REG_RE.findall(rest)
        # 过滤非法 target（太短或不是法规）
        targets = [t.strip() for t in targets if len(t) > 2 and not t.startswith(("A", "Part"))]
        if not targets:
            continue

        edges.append({
            "src": src,
            "targets": targets,
            "relation": "equivalent",
            "topic": topic_key,
            "line": line_strip[:200],
        })

    return edges


def normalize_reg(s: str) -> str:
    """规整 reg_id 名称。"""
    s = s.strip()
    s = re.sub(r"^UN\s+(ECE\s+)?", "", s)
    # 移除内部注释部分 "ECE R48 附件 5" -> "ECE R48"
    s = re.sub(r"\s+附.*$", "", s)
    s = re.sub(r"\s+Annex.*$", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s+Part\s*[IVX]+.*$", "", s, flags=re.IGNORECASE)
    return s.strip()


def main() -> int:
    all_edges = []
    seen_sources = {}

    for p in TOPIC_DIR.glob("*.md"):
        if p.name.startswith("_"):
            continue
        edges = parse_topic_page(p)
        for e in edges:
            e["src"] = normalize_reg(e["src"])
            e["targets"] = [normalize_reg(t) for t in e["targets"]]
            all_edges.append(e)

    # 去重 + 归并
    merged = {}
    for e in all_edges:
        src = e["src"]
        for t in e["targets"]:
            if not t or t == src:
                continue
            key = f"{src} :: {t}"
            if key not in merged:
                merged[key] = {
                    "src": src,
                    "target": t,
                    "relation": e["relation"],
                    "topic": e["topic"],
                    "line": e["line"],
                }
        if e["relation"] == "no_direct_match" and not e["targets"]:
            key = f"{src} :: (无对应)"
            merged[key] = {
                "src": src,
                "target": None,
                "relation": "no_direct_match",
                "topic": e["topic"],
                "line": e["line"],
            }

    # 写 JSON
    (OUT_DIR / "curated_equivalences.json").write_text(
        json.dumps(list(merged.values()), ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 写 YAML（按 src 排序）
    by_src: dict[str, list] = {}
    for v in merged.values():
        by_src.setdefault(v["src"], []).append(v)
    yaml_out = {}
    for src in sorted(by_src):
        yaml_out[src] = [
            {"target": v["target"], "relation": v["relation"], "topic": v["topic"]}
            for v in by_src[src]
        ]
    (OUT_DIR / "curated_equivalences.yaml").write_text(
        yaml.safe_dump(yaml_out, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )

    print(f"Topics scanned: {len(list(TOPIC_DIR.glob('*.md'))) - 1}")
    print(f"Raw edges: {len(all_edges)}")
    print(f"Unique src-target edges: {len(merged)}")
    print(f"Unique src reg_ids: {len(by_src)}")
    print()
    print("Top 15 sources by # targets:")
    top = sorted(by_src.items(), key=lambda x: -len(x[1]))[:15]
    for src, ts in top:
        tgts = ", ".join(t["target"] or "(无)" for t in ts[:5])
        print(f"  {src:35} -> {tgts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
