"""审计类 tools：低置信度 notes / 待审核清单。"""
from __future__ import annotations

from typing import Optional

from langchain.tools import tool

from ._shared import load_all_notes, truncate


@tool
def list_needs_review(
    limit: int = 20,
    confidence: str = "low",
) -> str:
    """列出 cross_check 置信度偏低或被标记为 needs_review 的 notes。

    用途："哪些 notes 需要人工复核""还有哪些低质量的条目"。

    Args:
        limit: 最多返回 N 条，默认 20，最大 100。
        confidence: 置信度门限 low / medium / high。传 "low" 返回 low；传 "medium" 返回 low+medium。
    """
    limit = max(1, min(int(limit), 100))
    conf_order = {"high": 3, "medium": 2, "low": 1}
    threshold = conf_order.get(confidence, 1)

    notes = load_all_notes()
    matched = []
    for n in notes:
        cf = n.get("confidence") or ""
        cf_score = conf_order.get(cf, 0)
        status = n.get("status") or ""
        if status == "needs_review" or (cf_score > 0 and cf_score <= threshold):
            matched.append({
                "reg_id": n["reg_id"],
                "region": n["region"],
                "topic": n["topic"],
                "status": status,
                "confidence": cf,
                "title": n["title"] or n["title_en"],
            })

    if not matched:
        return (f"没有置信度 ≤ {confidence} 或 status=needs_review 的 notes。"
                " Audit queue 是空的 🎉")

    # 按 confidence 升序（low 最先），然后 status
    conf_sort = {"low": 0, "medium": 1, "high": 2, "": 3, "unknown": 3}
    matched.sort(key=lambda x: (conf_sort.get(x["confidence"], 99), x["reg_id"]))

    lines = [f"需要复核的 notes（阈值 confidence ≤ {confidence}）: 共 {len(matched)} 条"]
    for m in matched[:limit]:
        lines.append(
            f"  [{m['confidence']:<8}] {m['reg_id']:<28} "
            f"({m['region']:<4}) [{m['topic'][:22]:<22}] "
            f"{(m['title'] or '')[:35]}"
        )
    if len(matched) > limit:
        lines.append(f"  ... and {len(matched) - limit} more (increase limit to see all)")
    return truncate("\n".join(lines), limit=4000)


AUDIT_TOOLS = [list_needs_review]
