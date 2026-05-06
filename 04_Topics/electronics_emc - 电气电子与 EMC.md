---
type: topic
topic_key: electronics_emc
label: 电气电子与 EMC
note_count: 17
regions:
  ece: 12
  cn: 5
types:
  type/version: 11
  type/amendment: 6
statuses:
  active: 15
  superseded: 2
generated_by: stage4_auto
tags:
- type/topic
- topic/electronics_emc
---

# 电气电子与 EMC（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

电气电子与 EMC 主题（22 notes，ECE=11, CN=11）覆盖 **电磁兼容性**、**电动车高压电安全**、**动力电池系统安全** 和 **电动自行车子系统**，是 `hv_battery_ev` 主题的上位扩展（本库 EV 相关法规大多分流到此簇，因 reg_id 编号段）。

**① 电磁兼容（EMC）**
- `ECE R10`：车辆 EMC 认证 — Rev6 Am1/Am2 引入无线充电 (WPT) + 5G-V2X 抗扰
- `GB 34660-2017`：道路车辆 EMC 要求和试验方法 — 国内对 R10 对标
- `GB 18655-2002`：保护车载接收机的无线电骚扰（CISPR 25 对标）
- `GB 16669-2010`：声光警报器 EMC 子项

**② 电动车整车 / 高压安全**
- `ECE R100`：电动车高压电安全 + 动力电池物理碰撞安全（**REESS** 概念发源法规）— Rev3 Am1/Am2 分阶段扩展
- `GB 18384-2020`：电动汽车安全要求（整车级，等效 R100 + 部分 GTR No.20 内容）
- `GB 38031-2020`：动力蓄电池安全要求（单体 + 电池包 + 系统）— 首度引入电池热扩散测试，国际领先 2 年
- `ECE R136`：L 类电动车（电动摩托）
- `GB 24155-2020`：纯电动摩托车 / 轻便摩托车安全要求

**③ 氢燃料电池**
- `ECE R134`：氢燃料电池车辆 — 整车级

**④ 电动自行车 (EBM)**
- `GB 43854-2024`：电动自行车用锂离子蓄电池（**国内独有**）
- `GB 42295-2022`：电动自行车电气安全
- `GB 42296-2022`：电动自行车充电器安全

**⑤ 网联信息安全**
- `ECE R156`：软件升级与 OTA 管理系统
- `ECE R155`：网络安全 CSMS（本簇未直接收录，但紧密关联）

**⑥ 重点演进**
- 2018：R10 Rev5 接入无线充电 WPT 测试（与 SAE J2954 协同）
- 2020：`GB 18384 + GB 38031 + GB 38032` 三标齐发，国内 EV 合规进入 "三位一体" 阶段
- 2020+：R100 Rev3 持续补充电池热失控 / 热蔓延测试，2024 与 GB 38031 内容趋同
- 2021：R155/R156 正式生效，国内 2024 `GB 44495`（汽车信息安全）对标
- 2024：`GB 43854-2024` 电动自行车锂电池强制标准，回应两轮车火灾频发

**跨区域速查**：
- `GB 34660` ≈ `ECE R10`（EMC）
- `GB 18384` ≈ `ECE R100 Part I`（电安全）
- `GB 38031` ≈ `ECE R100 Part II + GTR 20`（电池安全，GB 独有热扩散要求）
- `GB 24155` ≈ `ECE R136`（电动 L 类）
- `GB 44495 / GB 44496 / GB 44497` ≈ `ECE R155 / R156 / R157`（网络安全 / OTA / ALKS — 可能在 `steering_suspension` 主题）

## 覆盖范围

- 共 **17** 条 notes
- 按区域：ece=12, cn=5
- 按类型：type/version=11, type/amendment=6
- 按状态：active=15, superseded=2

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 18655-2002, GB 34660-2017, GB/T 18655-2010, GB/T 18655-2018, GB/T 18655-2025 |
| ece | ECE R10, ECE R10 Rev6, ECE R10 Rev6 Am1, ECE R10 Rev6 Am2, ECE R100, ECE R100 Rev3 Am1, ECE R100 Rev3 Am2, ECE R136, ECE R136 Am1, ECE R155, ECE R155 Am1, ECE R156 |

## 时间线（最近 30 条）

- **2025-02-28** — [[GB T 18655-2025]] · 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法
- **2023-02-24** — [[ECE R136 Am1]] · Uniform provisions concerning the approval of vehicles of ca
- **2023-02-17** — [[ECE R100 Rev3 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2022-11-25** — [[ECE R155 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2022-11-11** — [[ECE R10 Rev6 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2022-09-16** — [[ECE R100 Rev3 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2021-03-04** — [[ECE R156]] · Uniform provisions concerning the approval of vehicles with 
- **2021-01-22** — [[ECE R155]] · Uniform provisions concerning the approval of vehicles with 
- **2020-10-30** — [[ECE R10 Rev6 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2019-11-20** — [[ECE R10 Rev6]] · Uniform provisions concerning the approval of vehicles with 
- **2018-07-13** — [[GB T 18655-2018]] · 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法
- **2017-11-01** — [[GB 34660-2017]] · 道路车辆 电磁兼容性要求和试验方法
- **2016-02-05** — [[ECE R136]] · Uniform provisions concerning the approval of vehicles of ca
- **2010-12-23** — [[GB T 18655-2010]] · 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法
- **2002-02-22** — [[GB 18655-2002]] · 用于保护车载接收机的无线电骚扰特性的限值和测量方法
- **2000-04** — [[ECE R10]] · 关于车辆电磁兼容性能认证的统一规定
- **1997-04-11** — [[ECE R100]] · 关于结构和功能安全方面的特殊要求对电池驱动的电动车认证的统一规定

## 完整索引

### cn (5)

- [[GB 18655-2002]] — 用于保护车载接收机的无线电骚扰特性的限值和测量方法 · 2002-02-22 · superseded
- [[GB 34660-2017]] — 道路车辆 电磁兼容性要求和试验方法 · 2017-11-01 · active
- [[GB T 18655-2010]] — 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法 · 2010-12-23 · superseded
- [[GB T 18655-2018]] — 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法 · 2018-07-13 · active
- [[GB T 18655-2025]] — 车辆、船和内燃机 无线电骚扰特性 用于保护车载接收机的限值和测量方法 · 2025-02-28 · active

### ece (12)

- [[ECE R10]] — 关于车辆电磁兼容性能认证的统一规定 · 2000-04 · active
- [[ECE R10 Rev6]] — Uniform provisions concerning the approval of vehicles with regard to  · 2019-11-20 · active
- [[ECE R10 Rev6 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-10-30 · active
- [[ECE R10 Rev6 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-11-11 · active
- [[ECE R100]] — 关于结构和功能安全方面的特殊要求对电池驱动的电动车认证的统一规定 · 1997-04-11 · active
- [[ECE R100 Rev3 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-09-16 · active
- [[ECE R100 Rev3 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2023-02-17 · active
- [[ECE R136]] — Uniform provisions concerning the approval of vehicles of category L w · 2016-02-05 · active
- [[ECE R136 Am1]] — Uniform provisions concerning the approval of vehicles of category L w · 2023-02-24 · active
- [[ECE R155]] — Uniform provisions concerning the approval of vehicles with regards to · 2021-01-22 · active
- [[ECE R155 Am1]] — Uniform provisions concerning the approval of vehicles with regards to · 2022-11-25 · active
- [[ECE R156]] — Uniform provisions concerning the approval of vehicles with regards to · 2021-03-04 · active

## 相关主题

- [[hv_battery_ev - 电动车 / 动力电池 / 充电保护]]
- [[test_methods - 试验方法 / 测量规程]]
- [[special_vehicles - 特种 / 危险车辆]]
- [[emissions_exhaust - 排放与燃料]]
