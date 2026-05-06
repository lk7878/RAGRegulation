---
type: dashboard_index
tags:
- type/moc
- dashboard/index
---

# 汽车法规知识库·查询面板（MOC）

> 使用 Obsidian **Dataview 插件** 实时查询 1414 条法规 notes。打开任一子页后，DQL 查询结果自动渲染为表格。
>
> **2026-04-25 更新**：MinerU 云 OCR 处理率达 **100%**（982 with assets + 406 no_assets + 13 split + 13 skipped），见 [[_MinerU_Upgrades]]。

## 可用面板

- [[_Needs_Review|需要复核的法规]] — Stage 2 标记 `status/needs-review` 的 notes
- [[_By_Region_Latest|按区域最新发布]] — 每个 region 最近 20 条
- [[_Emissions_Watch|排放法规监控]] — 国六 / Euro VI / WLTP 系列跟踪
- [[_EV_BEV_Watch|新能源车法规监控]] — R100 / R136 / GB 18384 / 38031 系列
- [[_Supersession_Chains|替代链溯源]] — 所有已知 supersedes/superseded_by 关系
- [[_Cross_Region_Matrix|跨区域对标矩阵]] — GB ↔ ECE ≈ 对应关系（Dataview 反向查询）
- [[_Recent_Amendments|近 3 个月 ECE 修正案]] — 最新 ECE Am 跟踪
- [[_High_Confidence_Index|高可信度索引]] — `cross_check_overall_confidence: high` 清单
- [[_Graph_Insights|关系网络洞察 (Stage 5a)]] — PageRank / 桥梁节点 / 区域流向 / 主题耦合
- [[_Semantic_Search|语义检索 (Stage 5b · BM25)]] — CLI 工具使用说明与示例
- [[_MinerU_Upgrades|MinerU 云 OCR 升级索引]] ⭐ — 按表格/公式/图像数量排序的富信息 notes

## 必装插件

- **Dataview** (blacksmithgu) — 提供 DQL 查询
- 可选：**Dataview+JS** — 需要时启用 JS 查询（本 MOC 仅用基础 DQL）

## FM Schema 参考

每条法规 note 的标准 FM 字段（可用于 DQL）：

```yaml
reg_id: GB XXX-YYYY         # 主键
region: cn|ece|eu|us|...    # 区域
type: type/version|type/amendment|type/regulation
status: active|superseded|withdrawn|...
title: 中文标题
title_en: English Title
publication_date: YYYY-MM-DD
implementation_date_new_vehicle: YYYY-MM-DD
standard_body: 发布机构
supersedes: [[prev reg_id]]
superseded_by: [[next reg_id]]
equivalent_to:                   # Stage 3 产出
  - ref: ECE RXX
    relation: equivalent
    source: stage3_curated:topic_key
tags:                            # 含 status/verified | status/needs-review
- reg/cn
- status/active
- status/verified
verified_by: deepseek-v3         # Stage 2 产出
cross_check_overall_confidence: high|medium|low
```
