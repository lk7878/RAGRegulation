---
type: topic
topic_key: steering_suspension
label: 转向与悬挂
note_count: 14
regions:
  ece: 11
  cn: 3
types:
  type/amendment: 9
  type/version: 5
statuses:
  active: 13
  superseded: 1
generated_by: stage4_auto
tags:
- type/topic
- topic/steering_suspension
---

# 转向与悬挂（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

转向与悬挂主题（31 notes，ECE=24, CN=7）是 **自动驾驶 / ADAS 法规的主战场**。ECE `R79` 是唯一覆盖转向装置的总法规，近 4 年迭代 Am1–Am8 对应 **ACSF (Automatically Commanded Steering Function)** 分级到 L2/L3/L4 自动驾驶能力扩展。

**① 转向装置基础与 ADAS**
- `ECE R79`：转向设备统一认证 — **ACSF 分级**：
  - Class A：仅转向辅助（不脱手）
  - Class B1：车道保持 (LKAS)
  - Class B2：紧急车道保持 (ELKS)
  - Class C：车道变更辅助 (LCA)
  - Class D：有限工况自主变道
  - Class E：非限工况自主变道 (L4 雏形)
- Rev4 Am1–Am8 (2019–2023)：逐步补充 ACSF Class C/D/E 与 RCP（驾驶员监控）条款

**② 后市场转向件**
- `ECE R128`：LED 光源替换件认证 — 误入此簇，实为 `lighting_signaling` 遗漏（R128 是 LED 光源非转向）
- 后续清理建议：移至 `lighting_signaling`

**③ 国内对应**
- `GB 17675-2021`：汽车转向系统基本要求（含 EPS / SBW 线控转向）
- `GB/T 12540-1990`：最小转弯直径测定方法

**④ 悬挂**
- `ECE R89`：限速装置 — 可能误入此簇
- 本主题 **悬挂专项法规空缺** — 悬挂认证大多合并在整车结构 (R13, R79, R107 等) 或未单独发 R，国内也无独立标准

**⑤ 新兴高度自动化**
- `ECE R157`：ALKS Automated Lane Keeping System — **L3 自动驾驶首个强制法规**（2020 生效）— 本簇未直接收录，建议检查后补录
- `ECE R140`：ESC 分配在 `brakes` 主题
- 与 `GB 44497`（ALKS 国内版）跨主题关联

**⑥ 重点演进**
- 2019：R79 Rev4 发布，正式定义 ACSF Class B1
- 2020：R157 ALKS 通过（M1 L3 自动驾驶 60 km/h 以下）
- 2021–2023：R79 Am2–Am8 对 ACSF Class C/D 持续完善，中国 `GB 17675-2021` 纳入 EPS / SBW
- 2024：R157 Am1 将 L3 速度上限放宽至 130 km/h

**跨区域速查**：
- `GB 17675` ≈ `ECE R79 主体部分`
- `GB/T 12540` ≈ `ECE R79 附件 1` 转弯半径定义部分

> ⚠️ **误分类提示**：`R128` 应迁至 `lighting_signaling`，`R6` 转向信号灯不属此主题。

## 覆盖范围

- 共 **14** 条 notes
- 按区域：ece=11, cn=3
- 按类型：type/amendment=9, type/version=5
- 按状态：active=13, superseded=1

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 17675-1999, GB 17675-2021, GB 17675-2025 |
| ece | ECE R79, ECE R79 Rev4, ECE R79 Rev4 Am1, ECE R79 Rev4 Am2, ECE R79 Rev4 Am3, ECE R79 Rev4 Am4, ECE R79 Rev4 Am5, ECE R79 Rev4 Am8, ECE R79 Rev4 Am9, ECE R79-04e6 Rev4 Am6, ECE R79-r4 Am7 |

## 时间线（最近 30 条）

- **2025-12-02** — [[GB 17675-2025]] · 汽车转向系 基本要求
- **2023-02-16** — [[ECE R79 Rev4 Am9]] · Uniform provisions concerning the approval of vehicles with 
- **2022-11-21** — [[ECE R79 Rev4 Am8]] · Uniform provisions concerning the approval of vehicles with 
- **2022-09-13** — [[ECE R79-r4 Am7 Rev4]] · Uniform provisions concerning the approval of vehicles with 
- **2022-03-17** — [[ECE R79-04e6 Rev4 Am6]] · Uniform provisions concerning the approval of vehicles with 
- **2022-03-17** — [[ECE R79 Rev4 Am5]] · Uniform provisions concerning the approval of vehicles with 
- **2021-12-08** — [[ECE R79 Rev4 Am4]] · Uniform provisions concerning the approval of vehicles with 
- **2021-02-20** — [[GB 17675-2021]] · 汽车转向系 基本要求
- **2021-02-02** — [[ECE R79 Rev4 Am3]] · Uniform provisions concerning the approval of vehicles with 
- **2020-11-02** — [[ECE R79 Rev4 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2020-01-17** — [[ECE R79 Rev4 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2018-11-07** — [[ECE R79 Rev4]] · Uniform provisions concerning the approval of vehicles with 
- **1999-09** — [[ECE R79]] · 汽车转向机构认证的统一规定
- **1999-02-14** — [[GB 17675-1999]] · 汽车转向系 基本要求

## 完整索引

### cn (3)

- [[GB 17675-1999]] — 汽车转向系 基本要求 · 1999-02-14 · active
- [[GB 17675-2021]] — 汽车转向系 基本要求 · 2021-02-20 · superseded
- [[GB 17675-2025]] — 汽车转向系 基本要求 · 2025-12-02 · active

### ece (11)

- [[ECE R79]] — 汽车转向机构认证的统一规定 · 1999-09 · active
- [[ECE R79 Rev4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2018-11-07 · active
- [[ECE R79 Rev4 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-01-17 · active
- [[ECE R79 Rev4 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-11-02 · active
- [[ECE R79 Rev4 Am3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-02-02 · active
- [[ECE R79 Rev4 Am4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-12-08 · active
- [[ECE R79 Rev4 Am5]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-03-17 · active
- [[ECE R79 Rev4 Am8]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-11-21 · active
- [[ECE R79 Rev4 Am9]] — Uniform provisions concerning the approval of vehicles with regard to  · 2023-02-16 · active
- [[ECE R79-04e6 Rev4 Am6]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-03-17 · active
- [[ECE R79-r4 Am7 Rev4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-09-13 · active

## 相关主题

- [[adas_driver_assist - ADAS / 驾驶员辅助系统]]
- [[test_methods - 试验方法 / 测量规程]]
- [[crash_impact - 碰撞与被动安全]]
- [[tires_wheels - 轮胎与车轮]]
- [[dimensions_weights - 尺寸 / 质量 / 类别]]
