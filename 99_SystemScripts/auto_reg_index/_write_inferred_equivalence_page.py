"""
生成 03_Equivalence/_Equivalence Inferred.md —— 从 FM 里按 source 聚合非 curated 来源的等价映射。

与 _Equivalence MOC.md 的区别:
- MOC：基于 04_Topics/ 人工策划的 curated_equivalences.json（精华）
- Inferred（本页）：基于各 note FM 的 equivalent_to 字段，source 属于:
    - stage3_body_inference  （正则抽取前言采标声明）
    - stage3_llm_opus         （Claude Opus LLM 补抽）
  其他 source 也统一展示以供审阅

用途:
- 作为「待 promotion 到 curated」的候选清单
- 每条都带 body evidence 供人工一键复核
- 格式便于复制到主题页「跨区域速查」章节
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
OUT = Path(r"D:\CcVault\03_Equivalence") / "_Equivalence Inferred.md"
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$")

# 非 curated 的 source 标签（其他 source 也会显示）
NON_CURATED_SOURCES = {
    "stage3_body_inference": ("📖 规则抽取（前言采标）", "auto_rule"),
    "stage3_llm_opus": ("🤖 LLM 抽取（Opus）", "auto_llm"),
    "stage3_opus_batch": ("🤖 LLM 抽取（Opus Batch）", "auto_llm"),
}


def collect():
    """扫 FM，收集所有带 source 的 equivalent_to 条目。"""
    grouped: dict[str, list] = defaultdict(list)  # source -> [entry]
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = FM_RE.match(txt)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        reg_id = (fm.get("reg_id") or "").strip()
        title = (fm.get("title") or "").strip()
        equivs = fm.get("equivalent_to") or []
        if not isinstance(equivs, list):
            continue
        for e in equivs:
            if not isinstance(e, dict):
                continue
            source = e.get("source") or "unknown"
            grouped[source].append({
                "src_reg_id": reg_id,
                "src_title": title,
                "ref": e.get("ref") or e.get("reg_id") or "",
                "relation": e.get("relation") or "",
                "source": source,
                "evidence": e.get("evidence") or "",
                "note_path": str(p),
            })
    return grouped


RELATION_LABELS = {
    "identical": "等同",
    "equivalent": "等效",
    "modified": "修改",
    "non_equivalent": "非等效",
    "reference": "参照",
}


def render(grouped: dict) -> str:
    total = sum(len(v) for v in grouped.values())
    non_curated_total = sum(
        len(grouped.get(s, [])) for s in NON_CURATED_SOURCES
    )

    lines = [
        "---",
        "type: moc",
        "purpose: equivalence_inferred",
        "tags:",
        "- type/moc",
        "- equivalence/inferred",
        "---",
        "",
        "# 跨区域等价映射（自动推断待复核）",
        "",
        "> **本页与 [[_Equivalence MOC]] 的分工**：",
        "> - MOC = **人工策划精华**（基于 04_Topics/ 主题页手写的「跨区域速查」）",
        "> - 本页 = **自动抽取候选**（基于各 note FM body 正则 + LLM 推断），**需要人工复核**。",
        "",
        f"> 统计：总 equivalent_to refs **{total}** 条；其中自动推断 **{non_curated_total}** 条（下面按来源分类）。",
        "",
        "## 如何审阅",
        "",
        "1. 逐条读 evidence（body 字面摘录）判断 relation 对不对",
        "2. 判断对 → 把该映射手工补录到对应 [[_Topics MOC|主题页]] 的「跨区域速查」",
        "3. 判断错 → 直接在源 note 的 FM 里删该 entry，下次 rebuild 不会再出现",
        "",
    ]

    # 按非 curated source 一块块展开
    for source, (label, _kind) in NON_CURATED_SOURCES.items():
        entries = grouped.get(source, [])
        if not entries:
            continue
        lines.append(f"## {label}  · {len(entries)} 条")
        lines.append("")
        lines.append("| 源法规 | 关系 | 目标 | Evidence 摘录 |")
        lines.append("| --- | :-: | --- | --- |")
        # 按 src_reg_id 排
        entries.sort(key=lambda e: e["src_reg_id"])
        for e in entries:
            src_link = f"[[{Path(e['note_path']).stem}|{e['src_reg_id']}]]"
            rel_cn = RELATION_LABELS.get(e["relation"], e["relation"] or "?")
            ev = (e["evidence"] or "").replace("\n", " ").replace("|", "\\|")
            if len(ev) > 100:
                ev = ev[:97] + "..."
            ev_disp = f"*{ev}*" if ev else "—"
            lines.append(f"| {src_link} | {rel_cn} | `{e['ref']}` | {ev_disp} |")
        lines.append("")

    # 其他 source 汇总
    other_sources = [s for s in grouped if s not in NON_CURATED_SOURCES]
    if other_sources:
        lines.append("## 其他来源（含 curated 等）")
        lines.append("")
        lines.append("| source | 条数 |")
        lines.append("| --- | --: |")
        for s in sorted(other_sources, key=lambda x: -len(grouped[x])):
            lines.append(f"| `{s}` | {len(grouped[s])} |")
        lines.append("")
        lines.append("> 这部分已落入 `_Equivalence MOC.md` 或来自其它管线，通常不需要在此页审阅。")
        lines.append("")

    # 按源法规聚合的「待 promotion」视图
    lines.append("## 按源法规聚合（可快速审阅）")
    lines.append("")
    by_src = defaultdict(list)
    for source in NON_CURATED_SOURCES:
        for e in grouped.get(source, []):
            by_src[e["src_reg_id"]].append(e)
    for src in sorted(by_src):
        entries = by_src[src]
        note = entries[0]["note_path"]
        title = entries[0]["src_title"]
        lines.append(f"### [[{Path(note).stem}|{src}]] · {title[:50]}")
        for e in entries:
            rel_cn = RELATION_LABELS.get(e["relation"], e["relation"] or "?")
            src_tag = "🤖" if "llm" in e["source"] else "📖"
            lines.append(f"- {src_tag} **{rel_cn}** `{e['ref']}`")
            if e.get("evidence"):
                lines.append(f"  > {e['evidence'][:200]}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*自动生成自 FM 扫描 · {non_curated_total} 条自动推断待复核 · 由 `_write_inferred_equivalence_page.py` 产出*")

    return "\n".join(lines)


def main() -> int:
    grouped = collect()
    # 统计打印
    print("按 source 分组:")
    for s, entries in sorted(grouped.items(), key=lambda x: -len(x[1])):
        print(f"  {s:<28}: {len(entries)}")

    content = render(grouped)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"\nWrote: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
