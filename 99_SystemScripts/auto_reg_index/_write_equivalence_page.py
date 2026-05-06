"""
Stage 3：从 curated_equivalences.yaml 生成 Obsidian 等价映射索引页。

输出 03_Equivalence/ 下：
- _Equivalence MOC.md — 主索引，按主题分组列出所有 GB↔ECE 对应
- 每个技术域有一个 section + 查找表
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CURATED = ROOT / ".stage3" / "curated_equivalences.json"
OUT_DIR = Path(r"D:\CcVault\03_Equivalence")
OUT_DIR.mkdir(exist_ok=True)

# 主题 → 展示名映射
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
    "type_approval_general": "总体型式认证",
    "identification": "车辆识别 / 标记",
    "anti_theft_security": "防盗与安全防护",
    "engine_power_performance": "发动机功率",
    "hv_battery_ev": "电动车 / 动力电池",
    "interior_protrusions": "内部凸出物 / 内饰",
    "special_vehicles": "特种 / 危险车辆",
    "bus_coach": "客车 / 公交车",
    "motorcycle": "摩托车 / L 类",
    "overview_directory": "体系概览",
    "lubricants_fluids": "润滑油",
    "fire_fighting_equipment": "消防器材",
    "speed_control_speedometer": "车速 / 限速",
    "body_markings": "车身标识",
    "energy_labeling": "能耗 / 油耗标识",
    "commercial_operations": "营运 / 商用车",
    "certification_admin": "强制认证",
}


def guess_region(reg: str) -> str:
    """reg 名称推测区域。"""
    s = (reg or "").strip().upper()
    if s.startswith("GB"):
        return "CN"
    if s.startswith(("ECE R", "UN R", "ECE-R", "UN-R")):
        return "ECE/UN"
    if s.startswith(("EU ", "EU/", "2007/", "2018/", "2019/")) or "/EC" in s or "/EU" in s:
        return "EU"
    if s.startswith(("FMVSS", "US ", "CFR ")):
        return "US"
    if s.startswith("ISO"):
        return "ISO"
    if s.startswith(("SAE", "SAE ")):
        return "SAE"
    if s.startswith(("API", "ACEA", "NHTSA")):
        return "Other"
    if s.startswith(("GSO", "SASO", "ECAS")):
        return "GCC"
    if s.startswith(("TR ", "EAEU")):
        return "EAEU"
    return "?"


def main() -> int:
    data = json.loads(CURATED.read_text(encoding="utf-8"))

    # 按主题分组
    by_topic: dict[str, list] = defaultdict(list)
    for e in data:
        by_topic[e["topic"]].append(e)

    # 按 region 对统计
    region_pairs = defaultdict(int)
    for e in data:
        if e["target"]:
            a = guess_region(e["src"])
            b = guess_region(e["target"])
            region_pairs[f"{a} <-> {b}"] += 1

    # 生成 MOC
    lines = [
        "---",
        "type: moc",
        "purpose: equivalence_map",
        "tags:",
        "- type/moc",
        "- equivalence/index",
        "---",
        "",
        "# 跨区域法规等价映射（MOC）",
        "",
        "> 本页从 **31 个主题页的手写「跨区域速查」小节** 抽取的 GB / ECE / EU / ISO 等对应关系。",
        "> 总映射数：{0}。按技术主题分组。".format(len(data)),
        "",
        "## 使用说明",
        "",
        "- **「≈」** 表示 **功能等效**（限值 / 测试方法 / 适用范围相当）",
        "- **「(无对应)」** 表示在同等技术域下无直接可互认的对标法规",
        "- 具体条款差异需查对应 [[_Topics MOC|主题页]] 的 Overview 小节",
        "",
        "## 区域对分布",
        "",
        "| 源区域 ↔ 目标区域 | 数量 |",
        "| --- | --: |",
    ]
    for k, v in sorted(region_pairs.items(), key=lambda x: -x[1]):
        lines.append(f"| {k} | {v} |")
    lines.append("")

    # 按主题展开
    lines.append("## 按技术主题列出")
    lines.append("")

    for topic in sorted(by_topic, key=lambda t: -len(by_topic[t])):
        label = TOPIC_LABELS.get(topic, topic)
        topic_safe = label.replace("/", "·")
        lines.append(f"### {label}  · [[{topic} - {topic_safe}|详细主题页]]")
        lines.append("")
        lines.append("| 源 (reg_id) | 关系 | 目标 | 来源主题 |")
        lines.append("| --- | :-: | --- | --- |")
        edges = sorted(by_topic[topic], key=lambda e: e["src"])
        for e in edges:
            src = e["src"]
            if e["relation"] == "no_direct_match" or not e["target"]:
                lines.append(f"| `{src}` | — | *(无对应)* | {topic} |")
            else:
                lines.append(f"| `{src}` | ≈ | `{e['target']}` | {topic} |")
        lines.append("")

    # 反向查询：ECE -> GB
    lines.append("## 反向索引：ECE/UN → GB")
    lines.append("")
    reverse: dict[str, list] = defaultdict(list)
    for e in data:
        if e["target"] and guess_region(e["target"]) == "ECE/UN":
            reverse[e["target"]].append({"src": e["src"], "topic": e["topic"]})
    lines.append("| ECE/UN | 对应国内 |")
    lines.append("| --- | --- |")
    for target in sorted(reverse):
        srcs = reverse[target]
        s = "、".join(f"`{x['src']}`" for x in srcs)
        lines.append(f"| `{target}` | {s} |")
    lines.append("")

    # 未找到对应（no_direct_match）
    lines.append("## 国内独有（无 ECE 直接对应）")
    lines.append("")
    lines.append("| GB | 主题 |")
    lines.append("| --- | --- |")
    no_match = [e for e in data if e["relation"] == "no_direct_match"]
    for e in sorted(no_match, key=lambda x: x["src"]):
        lines.append(f"| `{e['src']}` | {e['topic']} |")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*从 31 主题页自动提取 · 共 {len(data)} 条映射 · 生成自 Stage 3*")

    (OUT_DIR / "_Equivalence MOC.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote _Equivalence MOC.md with {len(data)} mappings to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
