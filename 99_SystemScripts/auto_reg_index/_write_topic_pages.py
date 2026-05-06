"""
Stage 4 writer：基于 cluster_assignment.json 生成主题索引页。

每个主题一个 MD：04_Topics/<topic_key>.md
内容：
  - FM（topic_key/label/region 统计/count）
  - Overview（占位，后续由 Cascade 填充）
  - Cross-reference table（ECE ↔ GB 等区域比对）
  - Chronology（按 publication_date）
  - Full note index（按 reg_id 分组）
  - Related topics
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CLUSTER = ROOT / ".stage4" / "cluster_assignment.json"
TOPIC_DIR = Path(r"D:\CcVault\04_Topics")
TOPIC_DIR.mkdir(exist_ok=True)

TOPIC_LABELS = {
    "lighting_signaling": "照明与信号装置",
    "brakes": "制动系统",
    "emissions_exhaust": "排放与燃料",
    "restraints_airbags": "安全带与乘员约束",
    "crash_impact": "碰撞与被动安全",
    "tires_wheels": "轮胎与车轮",
    "steering_suspension": "转向与悬挂",
    "visibility_glazing": "视野 / 玻璃 / 雨刮",
    "electronics_emc": "电气电子与 EMC",
    "fuel_lpg_cng": "燃料装置（液体 / 气体）",
    "noise": "噪声",
    "dimensions_weights": "尺寸 / 质量 / 类别",
    "doors_mechanisms": "门锁 / 铰链 / 座椅机构",
    "type_approval_general": "总体型式认证 / 通用要求",
    "identification": "车辆识别 / 标记",
    "anti_theft_security": "防盗与安全防护",
    "engine_power_performance": "发动机功率 / 性能测试",
    "hv_battery_ev": "电动车 / 动力电池 / 充电保护",
    "interior_protrusions": "内部凸出物 / 内饰",
    "special_vehicles": "特种 / 危险车辆",
    "bus_coach": "客车 / 公交车",
    "motorcycle": "摩托车 / L 类",
    "overview_directory": "目录 / 体系概览",
    "lubricants_fluids": "润滑油 / 工作液",
    "fire_fighting_equipment": "消防器材 / 灭火系统",
    "speed_control_speedometer": "车速 / 限速装置",
    "body_markings": "车身标识 / 反光标志",
    "energy_labeling": "能耗 / 油耗标识",
    "commercial_operations": "营运 / 商用车管理",
    "certification_admin": "强制认证 / 管理制度",
    "operator_controls_indicators": "操纵件 / 指示器位置",
    "test_methods": "试验方法 / 测量规程",
    "trailer_coupling": "挂车 / 联结装置",
    "adas_driver_assist": "ADAS / 驾驶员辅助系统",
    "recycling_reuse": "回收 / 再制造 / 禁用物质",
    "out_of_scope": "非汽车法规 / 越界",
    "reference_material": "参考资料（非法规）",
    "misc": "其他 / 未归类",
}


def note_wikilink(note: dict) -> str:
    """生成 Obsidian wikilink。"""
    p = Path(note["path"])
    return f"[[{p.stem}]]"


def region_stats(notes: list[dict]) -> dict:
    c = Counter(n["region"] for n in notes)
    return dict(c.most_common())


def type_stats(notes: list[dict]) -> dict:
    c = Counter(n["type"] for n in notes)
    return dict(c.most_common())


def status_stats(notes: list[dict]) -> dict:
    c = Counter(n["status"] for n in notes)
    return dict(c.most_common())


def build_chronology(notes: list[dict]) -> list[dict]:
    import re as _re
    # 只保留有合法 YYYY-MM-DD 或 YYYY-MM 的
    dated = []
    for n in notes:
        pd = str(n.get("publication_date") or "")
        if _re.match(r"^\d{4}(-\d{2})?(-\d{2})?$", pd):
            dated.append(n)
    dated.sort(key=lambda x: str(x["publication_date"]))
    return dated


def build_cross_ref_table(notes: list[dict]) -> list[dict]:
    """按 region 分组，标出可能的对应关系（reg_id 前缀）。"""
    by_region = defaultdict(list)
    for n in notes:
        by_region[n["region"]].append(n)
    # 仅输出每个 region 的 reg_id 列表
    return {r: sorted({n["reg_id"] for n in ns}) for r, ns in by_region.items()}


def render_topic_page(topic_key: str, notes: list[dict], all_clusters: dict) -> str:
    label = TOPIC_LABELS.get(topic_key, topic_key)
    regions = region_stats(notes)
    types_ = type_stats(notes)
    statuses = status_stats(notes)
    chrono = build_chronology(notes)
    cross_ref = build_cross_ref_table(notes)

    # 相关主题：共现率最高的其它主题（基于 topic_scores 二三名）
    related_score = Counter()
    for n in notes:
        for tk, sc in (n.get("scores") or {}).items():
            if tk != topic_key:
                related_score[tk] += sc
    related = [
        (tk, TOPIC_LABELS.get(tk, tk))
        for tk, _ in related_score.most_common(5)
        if tk in all_clusters
    ]

    fm = {
        "type": "topic",
        "topic_key": topic_key,
        "label": label,
        "note_count": len(notes),
        "regions": regions,
        "types": types_,
        "statuses": statuses,
        "generated_by": "stage4_auto",
        "tags": ["type/topic", f"topic/{topic_key}"],
    }

    parts = [
        "---",
        yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).rstrip(),
        "---",
        "",
        f"# {label}（Topic Index）",
        "",
        "> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。",
        "",
        "## Overview",
        "",
        "_（待 Cascade 根据本主题 notes 内容综合填写：核心技术域、典型法规体系、关键里程碑等）_",
        "",
        "## 覆盖范围",
        "",
        f"- 共 **{len(notes)}** 条 notes",
        f"- 按区域：{', '.join(f'{r}={c}' for r, c in regions.items())}",
        f"- 按类型：{', '.join((t or '—') + '=' + str(c) for t, c in types_.items())}",
        f"- 按状态：{', '.join((s or '—') + '=' + str(c) for s, c in statuses.items())}",
        "",
    ]

    # Cross-region ref table
    if len(cross_ref) > 1:
        parts += [
            "## 跨区域法规索引",
            "",
            "| Region | reg_ids |",
            "| --- | --- |",
        ]
        for r in sorted(cross_ref):
            ids = cross_ref[r]
            row = ", ".join(ids[:30]) + (f" … (+{len(ids)-30})" if len(ids) > 30 else "")
            parts.append(f"| {r} | {row} |")
        parts.append("")

    # Chronology (latest 30)
    if chrono:
        parts += [
            "## 时间线（最近 30 条）",
            "",
        ]
        for n in chrono[-30:][::-1]:
            title = (n.get("title") or "").replace("|", "\\|")
            parts.append(f"- **{n['publication_date']}** — {note_wikilink(n)} · {title[:60]}")
        parts.append("")

    # Full index grouped by region
    parts += [
        "## 完整索引",
        "",
    ]
    by_region_full = defaultdict(list)
    for n in notes:
        by_region_full[n["region"]].append(n)
    for r in sorted(by_region_full):
        ns = sorted(by_region_full[r], key=lambda x: x["reg_id"])
        parts.append(f"### {r} ({len(ns)})")
        parts.append("")
        for n in ns:
            title = (n.get("title") or "").strip()
            date = n.get("publication_date") or ""
            st = n.get("status") or ""
            suffix = f" · {date}" if date else ""
            suffix += f" · {st}" if st else ""
            parts.append(f"- {note_wikilink(n)} — {title[:70]}{suffix}")
        parts.append("")

    # Related topics
    if related:
        parts += [
            "## 相关主题",
            "",
        ]
        for tk, tl in related:
            parts.append(f"- [[{tk} - {tl}]]")
        parts.append("")

    return "\n".join(parts)


def extract_overview(existing_path: Path) -> str | None:
    """从旧 topic 页读取 ## Overview 段，用于保留手写内容。返回 None 表示未手写。"""
    if not existing_path.exists():
        return None
    txt = existing_path.read_text(encoding="utf-8", errors="replace")
    # 定位 "## Overview" 到下一个 "## " 之间
    import re as _re
    m = _re.search(r"## Overview\s*\n(.*?)(?=\n## )", txt, _re.DOTALL)
    if not m:
        return None
    body = m.group(1).strip()
    # 如果是占位文本 —— 未手写
    if body.startswith("_（待 Cascade") or not body:
        return None
    return body


def main() -> int:
    clusters = json.loads(CLUSTER.read_text(encoding="utf-8"))
    written = preserved = 0
    for topic_key, notes in clusters.items():
        label = TOPIC_LABELS.get(topic_key, topic_key)
        safe_label = label.replace("/", "·")
        fname = f"{topic_key} - {safe_label}.md"
        fpath = TOPIC_DIR / fname

        # 读旧 Overview（如有手写）
        old_overview = extract_overview(fpath)

        page = render_topic_page(topic_key, notes, clusters)
        if old_overview:
            # 替换占位
            placeholder = "_（待 Cascade 根据本主题 notes 内容综合填写：核心技术域、典型法规体系、关键里程碑等）_"
            page = page.replace(placeholder, old_overview)
            preserved += 1
        fpath.write_text(page, encoding="utf-8")
        written += 1
        print(f"  {fname}  ({len(notes)} notes){' [preserved]' if old_overview else ''}")
    print(f"\nWrote {written} topic pages to {TOPIC_DIR} ({preserved} with preserved Overview)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
