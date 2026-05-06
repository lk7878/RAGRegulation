"""
读取各主题的代表性 notes（summary / keywords / title），
生成紧凑 digest 给 Cascade 写 Overview 用。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CLUSTER = ROOT / ".stage4" / "cluster_assignment.json"
OUT = ROOT / ".stage4" / "topic_digest.md"


def read_fm(p: Path) -> dict:
    try:
        txt = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}
    if not txt.startswith("---"):
        return {}
    end = txt.find("\n---", 4)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        return {}


def main() -> int:
    topics = sys.argv[1:] if len(sys.argv) > 1 else None
    clusters = json.loads(CLUSTER.read_text(encoding="utf-8"))
    out_lines = []
    for topic_key, notes in clusters.items():
        if topics and topic_key not in topics:
            continue
        out_lines.append(f"\n## Topic: {topic_key} ({len(notes)} notes)\n")
        # 选代表性：有 summary 的前 8 条（按 publication_date 最新）
        enriched = []
        for n in notes:
            fm = read_fm(Path(n["path"]))
            enriched.append({
                "reg_id": fm.get("reg_id") or n.get("reg_id"),
                "region": fm.get("region") or n.get("region"),
                "title": (fm.get("title") or "").strip(),
                "date": str(fm.get("publication_date") or ""),
                "summary": (fm.get("summary") or "").strip(),
                "keywords": fm.get("keywords") or [],
                "status": fm.get("status") or "",
            })
        with_summary = [e for e in enriched if e["summary"]]
        with_summary.sort(key=lambda x: x["date"], reverse=True)
        samples = with_summary[:8]
        if not samples:
            # 无 summary 的退回前 5 条只列 title
            samples = enriched[:5]

        # regions 统计
        from collections import Counter
        region_counter = Counter(e["region"] for e in enriched)
        out_lines.append(f"**Regions**: {dict(region_counter)}")
        out_lines.append("")

        # 代表性 reg_ids (前 15 个)
        reg_ids_all = sorted({e["reg_id"] for e in enriched})
        out_lines.append(f"**Sample reg_ids**: {', '.join(reg_ids_all[:15])}{' …' if len(reg_ids_all) > 15 else ''}")
        out_lines.append("")

        out_lines.append("**Key notes**:")
        for s in samples:
            summary_trunc = (s["summary"][:280] + "…") if len(s["summary"]) > 280 else s["summary"]
            kw = ", ".join(s["keywords"][:6]) if isinstance(s["keywords"], list) else ""
            out_lines.append(f"- **{s['reg_id']}** ({s['region']}, {s['date']}) *{s['title'][:60]}*")
            if summary_trunc:
                out_lines.append(f"  - summary: {summary_trunc}")
            if kw:
                out_lines.append(f"  - keywords: {kw}")
        out_lines.append("")

    OUT.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote digest to {OUT}  ({len(out_lines)} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
