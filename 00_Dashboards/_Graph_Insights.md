---
type: dashboard
purpose: graph_network_insights
stage: 5a
tags:
- type/dashboard
- stage/5a
- graph/insights
---

# 关系网络洞察（Stage 5a）

> 由 `_build_graph.py` + `_graph_analytics.py` 分析得出。1414 个可解析节点 × 416 条有效关系边。GraphML 位于 `.stage5/graph.graphml`，可用 Gephi / Cytoscape / yEd 可视化。

## 网络整体结构

| 指标 | 数值 | 解读 |
| --- | --: | --- |
| 节点数 | 1414 | 唯一 reg_id（去除 _dupN） |
| 边数 | 416 | FM 内 supersedes/equivalent_to/references/related |
| 图密度 | 0.000208 | 极稀疏，典型知识图谱特征 |
| 弱连通分量 | 1171 | 绝大多数规 / 其家族独立成团 |
| 最大分量 | 93 节点 | 乘员约束 + 商用 + 座椅核心集群 |
| 孤立节点 | 1101 (77.9%) | 多为特定修正案版本（如 `UN R48 Rev6 Am5`），被家族代表节点"代言" |

**关系类型占比**：
- `supersedes`: 139（33%）
- `references`: 126（30%）
- `equivalent_to`: 78（19%）
- `superseded_by`: 69（17%）
- `related`: 4（<1%）

## PageRank Top 15 — "基础性最强"法规

可以理解为 **被最多其他标准隐式或显式依赖** 的节点，是 vault 的"引力中心"：

| Rank | reg_id | PageRank | Region | Topic | 意义 |
| --- | --- | --: | --- | --- | --- |
| 1 | `GB/T 15089-2001` | 0.0103 | cn | — | **机动车辆及挂车分类**，所有车辆类型定义的词汇表，被 N 多 GB 作基础引用 |
| 2 | `GB 5768-1999` | 0.0067 | cn | — | 道路交通标志和标线，作为交通法规基础 |
| 3 | `GB 20300-2018` | 0.0055 | cn | commercial_operations | 道路运输车辆信号仪表 |
| 4 | `GB 17761-2018` | 0.0050 | cn | electronics_emc | 电动自行车安全技术规范（连"新国标"） |
| 5 | `GB 17761-1999` | 0.0047 | cn | — | 电动自行车原始版本 |
| 6 | `GB/T 12673-2019` | 0.0044 | cn | test_methods | 主要尺寸测量方法 |
| 7 | `GB 11567-2017` | 0.0043 | cn | commercial_operations | 汽车和挂车侧后防护 |
| 8 | `GB 15084-2013` | 0.0043 | cn | visibility_glazing | 后视镜要求和测量方法 |
| 9 | `GB/T 12540-2009` | 0.0043 | cn | test_methods | 最小转弯直径 / 通道圆测量 |
| 10 | `GB/T 18655-2010` | 0.0043 | cn | electronics_emc | 车载电子设备无线电骚扰 |

**发现**：前 10 位中有 5 个 GB/T（推荐性）— 说明 **基础性方法学标准** 是网络的"黏合剂"，比强制标准（GB）的汇聚度还高。

## Betweenness Centrality Top 10 — "跨主题桥梁"

桥梁节点横跨多个主题，是知识流动的关键枢纽：

| reg_id | BC | Topic | 跨主题意义 |
| --- | --: | --- | --- |
| `GB 24406-2012` | 0.0065 | restraints_airbags | 专用校车儿童约束 — 横跨 crash / bus_coach / restraints |
| `GB 13057-2023` | 0.0060 | restraints_airbags | 客车座椅固定件强度 — 横跨 bus / restraints / crash |
| `GB 14166-2024` | 0.0028 | restraints_airbags | 安全带 / 约束系统 — 横跨 ISOFIX / crash |
| `ECE R80` | 0.0025 | restraints_airbags | 大客车座椅 — 横跨 bus / restraints |
| `GB 11551-2014` | 0.0018 | crash_impact | 正面碰撞乘员保护 — 横跨 restraints / crash |
| `GB 18384-2020` | 0.0014 | electronics_emc | 电动车安全要求 — 横跨 ev / crash / emc |

**发现**：`restraints_airbags` + `crash_impact` + `bus_coach` 三主题交叉的 **客车座椅安全** 是最密耦合的知识域。

## 最大连通分量（93 节点）

第一大 WCC 包含 93 个互相关联的 notes：
- 63 个 cn + 30 个 ece（GB-ECE 对标最密集区域）
- 核心聚焦：**乘员保护三件套（座椅 + 安全带 + 儿童约束） + 商用车专用 + 碰撞**
- 典型样本：`GB 14166`, `GB 14167`, `GB 13057`, `GB 24406`, `GB 11551`, `ECE R14`, `ECE R16`, `ECE R44`, `ECE R94`

**工程含义**：中国乘员保护体系与 ECE 1958 协议最贴近，采信链最长。

## Cross-Topic 边 Top 10 — 知识耦合实态

| From → To | 边数 | 物理含义 |
| --- | --: | --- |
| `fuel_lpg_cng → emissions_exhaust` | 6 | 燃料类型直接决定排放特性 |
| `dimensions_weights → misc` | 5 | 车辆分类标准被多个非主流主题引用 |
| `electronics_emc → crash_impact` | 4 | R94/R137 引用 R100 动力电池安全 |
| `tires_wheels → restraints_airbags` | 4 | TPMS 某些情况下联动约束系统 |
| `restraints_airbags → crash_impact` | 3 | 碰撞工况引用约束性能 |
| `brakes → misc` | 3 | 制动标准引用非制动基础 |
| `motorcycle → lighting_signaling` | 3 | L 类摩托车照明独立 |
| `bus_coach → restraints_airbags` | 2 | 校车约束关联 |

**诊断**：部分到 `misc` 的边表明 misc 中仍有应迁到主题的底层基础标准（如 GB/T 分类 / 尺寸）。

## Region Flow（跨区域引用流向）

| From | To | 边数 | 说明 |
| --- | --- | --: | --- |
| cn | cn | 253 | 国内内部引用（基础 GB/T → 具体 GB） |
| cn | ece | 81 | **国内追赶国际**：GB 引用 ECE 作对标 |
| ece | ece | 79 | ECE 系列内部引用（如 R83 引用 R49） |
| eu | eu | 2 | EU 指令互引 |
| gcc | gcc | 1 | 海合会内部 |

**关键数据**：`cn → ece` 的 81 条正向引用是 **国内汽车法规国际化进程** 的定量表达。反向几乎没有（`ece → cn` 不存在），反映 ECE 独立性。

## 主题孤立率排名（10+ 节点主题）

> 孤立 = 该节点 0 入 0 出度。高孤立率主题说明标准本身自成体系，缺少 supersedes/references/equivalent_to 记录。

| Topic | 孤立率 | 解读 |
| --- | --: | --- |
| `type_approval_general` | 94.4% | 整车型式认证是顶层框架，自然不被具体技术标准引用 |
| `overview_directory` | 92.9% | 国别体系概览文档，非技术标准 |
| `special_vehicles` | 91.3% | 特种车独立法规体系 |
| `noise` | 89.7% | 噪声标准本身是独立实体 |
| `steering_suspension` | 89.5% | ADAS/ACSF 新兴标准尚未沉淀引用关系 |
| `anti_theft_security` | 87.2% | 防盗标准跨 IT 安全独立体系 |
| `misc` | 83.1% | 未归类兜底 |
| `crash_impact` | 81.8% | 最大连通分量核心，但许多版本 Am 未互联 |

**可改进方向**：Steering / anti-theft 等主题低引用度可以用 LLM 补充 references 字段（Stage 2 cross-check 检测到 1206 条 supersedes 缺失 / 1312 条 equivalent_to 缺失）。

## 孤立的"外部引用"Top 10

这些是 **本库外** 的标准（外部规范 / 权威文件 / 被删除规范）：

| 目标 | 引用次数 | 说明 |
| --- | --: | --- |
| `Agreement Concerning the Adoption of Uniform Technical Prescriptions for Wheeled Vehicles` | 7 | **WP.29 1958 协议**（全文引述） |
| `Consolidated Resolution R.E.3` | 4 | WP.29 决议，非 R 号 |
| `ISO` | 3 | 裸 "ISO" 命名不精确 |
| `EU 2019/631` | 3 | 欧盟 CO2 条例（2019/631） |
| `GB 1334-77` | 3 | 超旧 GB（1977 版，未入库） |
| `GB/T 2423.1/2/3` | 6 | 电工电子环境试验（基础通用，未入库） |
| `UN R112` | 3 | 模糊正则未匹配（已修） |

## 产出文件

- `.stage5/graph.json` — 节点 + 边原始数据（JSON）
- `.stage5/graph.graphml` — Gephi / Cytoscape / yEd 可视化
- `.stage5/graph_stats.json` — 度分布 / 孤立节点 / 顶级 hubs
- `.stage5/graph_analytics.json` — PageRank / Betweenness / WCC / 主题流向

## 脚本

- `_build_graph.py` — 构建关系图（含 family-level 模糊匹配）
- `_graph_analytics.py` — 深度分析（需 networkx + numpy + scipy）
- `_build_supersession_chain.py` — 反向 supersedes 链（前置，已跑）
