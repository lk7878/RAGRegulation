---
type: type/schema
title: 四维度 Tag 字典
version: 0.1
---

# 02 · 四维度 Tag 字典

> 每份 note 同时打 4 个维度的 tag。前两级固定（enum），三四级开放（AI 提议 + 月度规整）。

---

## 0. 设计原则

- **正交**：4 个维度互相独立，不合并
- **前 2 级 enum**：从下面的表里取，不允许自造
- **后 2 级开放**：AI 可自动提议新 tag，每月用 Tag Wrangler 插件规整一次
- **工具**：Obsidian 原生嵌套 tag（`parent/child/grandchild`），Dataview 按任一维度聚合

---

## 1. `type/` 维度（节点类型）

| tag | 用途 |
|---|---|
| `type/regulation` | 法规主条目（不含版本细节） |
| `type/version` | 某版本的完整内容 |
| `type/amendment` | 修改单 |
| `type/test-method` | 试验方法 |
| `type/dummy` | 假人模型 |
| `type/injury-metric` | 损伤指标 |
| `type/vehicle-class` | 车型分类 |
| `type/topic` | 主题聚合页 |
| `type/index` | vault 首页等索引页 |
| `type/schema` | 02_Schema 下的元数据文档 |
| `type/review-queue` | 待审队列 |
| `type/design-doc` | 设计文档 |

辅助标记（可与上面并存）：
| tag | 用途 |
|---|---|
| `status/needs-review` | 进入 `_review_queue.md` |
| `status/draft` | AI 抽取后未经任何审校 |
| `status/verified` | 经 cross-check 通过 |
| `status/manually-edited` | 你人工精修过 |

---

## 2. `reg/` 维度（地区）

### 前 2 级 enum（禁自造）

| 第 1 级 | 第 2 级（国家/区域） | 法规体系 |
|---|---|---|
| `reg/cn` | — | GB 国标 |
| `reg/ece` | — | UNECE 法规（R 系列） |
| `reg/eu` | — | EU Directive / Regulation |
| `reg/us` | `reg/us/fmvss` `reg/us/cfr` | FMVSS 联邦机动车安全标准 / CFR |
| `reg/jp` | — | JIS / 保安基准 |
| `reg/kr` | — | KMVSS |
| `reg/asean` | `reg/asean/th` `reg/asean/id` `reg/asean/my` `reg/asean/vn` `reg/asean/ph` `reg/asean/sg` | 东盟各国 |
| `reg/gcc` | `reg/gcc/sa` `reg/gcc/ae` `reg/gcc/kw` | 海湾合作 |
| `reg/ru-eaeu` | — | 俄罗斯 + 欧亚经济联盟 |
| `reg/in` | — | 印度 AIS / CMVR |
| `reg/br` | — | 巴西 Denatran |
| `reg/au` | — | 澳大利亚 ADR |
| `reg/za` | — | 南非 NRCS |
| `reg/international` | — | ISO / SAE 等国际组织 |

---

## 3. `topic/` 维度（主题）

### 前 2 级 enum（禁自造）

```
topic/passive-safety/            被动安全
  ├── frontal-impact             正面碰撞
  ├── side-impact                侧面碰撞
  ├── rear-impact                后碰
  ├── rollover                   翻滚
  ├── pedestrian-protection      行人保护
  ├── roof-strength              顶压
  └── restraint                  约束系统

topic/active-safety/             主动安全
  ├── aeb                        自动紧急制动
  ├── lka                        车道保持
  ├── esc                        电子稳定控制
  ├── bsd                        盲区监测
  └── acc                        自适应巡航

topic/brake-steer/               制动与转向
  ├── service-brake
  ├── abs
  ├── steering
  └── parking-brake

topic/lighting/                  照明信号
  ├── headlamp
  ├── position-lamp
  ├── signal-lamp
  └── retroreflective

topic/visibility/                视野
  ├── driver-forward-view
  ├── defrost-demist
  └── mirror-camera

topic/emission-energy/           排放与能耗
  ├── emission-light-duty
  ├── emission-heavy-duty
  ├── fuel-economy-lv
  ├── fuel-economy-hv
  └── ev-energy

topic/ev-safety/                 电动车安全
  ├── rescs                      可充电储能系统
  ├── insulation
  ├── charging-interface
  └── thermal-runaway

topic/emc                        电磁兼容
topic/recycling                  回收利用

topic/structure-body/            车身结构
  ├── bus-structure
  ├── bumper
  ├── exterior-projection
  └── glazing

topic/wheel-tyre/                车轮与轮胎
  ├── tyre
  └── wheel-rim

topic/special-vehicle/           特种车辆
  ├── school-bus
  ├── dangerous-goods
  └── commercial

topic/identification/            标识
  ├── vin
  └── nameplate

topic/admin/                     管理/制度
  ├── ccc
  ├── wvta
  ├── type-approval
  └── market-access
```

### 第 3-4 级开放规则

- AI 提取法规时可以自由提议第 3-4 级（例如 `topic/passive-safety/frontal-impact/occupant-protection/dummy-response`）
- 每月月底，我跑一次 "tag 规整" 专项：Tag Wrangler 批量合并语义相同但拼写不同的 tag
- 禁止出现空第 3 级（如 `topic/lighting/自造中文名`，要么用预定义的 `headlamp`，要么新增预定义 enum）

---

## 4. `veh/` 维度（车型分类）

| tag | 描述 | 对应 ECE 分类 |
|---|---|---|
| `veh/M1` | 乘用车 ≤ 9 座 | M₁ |
| `veh/M2` | 客车 > 9 座 且 ≤ 5 t | M₂ |
| `veh/M3` | 客车 > 9 座 且 > 5 t | M₃ |
| `veh/N1` | 货车 ≤ 3.5 t | N₁ |
| `veh/N2` | 货车 3.5–12 t | N₂ |
| `veh/N3` | 货车 > 12 t | N₃ |
| `veh/L` | 摩托车/二轮/三轮 | L 类 |
| `veh/O` | 挂车 | O 类 |
| `veh/G` | 越野车子类 | — |
| `veh/all` | 适用全部车型 | — |

**不做第 2 级**（M1a / M1b 这种细分没必要，法规通常适用整个 M1）。

---

## 5. 实例：GB 4785-2019 的完整 tag 组合

```yaml
tags:
  - type/version
  - status/verified
  - reg/cn
  - topic/lighting
  - topic/lighting/headlamp       # 3 级（开放）
  - topic/lighting/position-lamp
  - topic/lighting/signal-lamp
  - veh/M1
  - veh/M2
  - veh/M3
  - veh/N1
  - veh/N2
  - veh/N3
  - veh/O
```

---

## 6. 月度规整流程

每月 1 号（约 30 分钟）：

1. 打开 Obsidian 的 **Tag Wrangler** 插件
2. 查看所有第 3-4 级 tag，按使用频次排序
3. 合并拼写接近的 tag（如 `topic/lighting/head-lamp` → `topic/lighting/headlamp`）
4. 删除使用次数 = 0 的孤儿 tag
5. 检查第 1-2 级是否有意外污染（AI 偶尔会造 `topic/lighting/headlamp/led-specific`）
6. 更新本文件的"第 3-4 级规整后 enum"表（如果某个第 3 级被高频使用 20 次以上，升格为固定 enum）
