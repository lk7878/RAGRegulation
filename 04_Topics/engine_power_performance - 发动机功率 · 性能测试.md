---
type: topic
topic_key: engine_power_performance
label: 发动机功率 / 性能测试
note_count: 13
regions:
  ece: 11
  cn: 2
types:
  type/version: 7
  type/amendment: 6
statuses:
  active: 13
generated_by: stage4_auto
tags:
- type/topic
- topic/engine_power_performance
---

# 发动机功率 / 性能测试（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

发动机功率 / 性能测试主题（13 notes，ECE=11, CN=2）聚焦 **内燃机净功率 + 电驱动最大 30min 功率** 的台架测量方法，是整车能量管理 / 排放合规的基础工具。

**① 整车动力测量**
- `ECE R85`：M 类 + N 类车辆内燃机净功率 + 电驱动 30min 最大功率测量（Rev1 Am1–Am5 持续更新）— 核心对接 WLTP 惯量参数
- `ECE R68`：乘用车最高速度测定（Am1，2000 年起频率降低）
- 国内：`GB 17692-1999` → `GB/T 17692-2024`（25 年后大修订，扩展至混动电机系统）

**② 测量条件与修正因子**
- 环境参数修正（温度、湿度、气压）
- 进气阻力、排气背压、冷却系统
- 涡轮增压 / 机械增压发动机的功率修正公式（R85 Rev1 Am1 更新核心）

**③ 应用场景**
- CAFC 合规基础（见 `emissions_exhaust`）
- 车辆型式批准 "额定功率" 录入基础
- 混动车系统功率叠加逻辑（HEV/PHEV）

**跨区域速查**：
- `GB/T 17692` ≈ `ECE R85`（净功率 + 30min 最大）
- `GB/T 18297` ≈ `ECE R24`（汽车动力性能试验方法）
- `ISO 1585`（内燃机净功率）作为国际基础，R85 / GB/T 17692 均从其发展

## 覆盖范围

- 共 **13** 条 notes
- 按区域：ece=11, cn=2
- 按类型：type/version=7, type/amendment=6
- 按状态：active=13

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 17692-1999, GB/T 17692-2024 |
| ece | ECE R68, ECE R68 Am1, ECE R85, ECE R85 Rev1, ECE R85 Rev1 Am1, ECE R85 Rev1 Am2, ECE R85 Rev1 Am3, ECE R85 Rev1 Am4, ECE R85 Rev1 Am5, ECE R85 Rev1 Corr1 |

## 时间线（最近 30 条）

- **2024-06-29** — [[GB T 17692-2024]] · 汽车发动机及驱动电机净功率测试方法
- **2023-02-17** — [[ECE R85 Rev1 Am5]] · Uniform provisions concerning the approval of internal combu
- **2020-07-01** — [[ECE R85 Rev1 Am4]] · Uniform provisions concerning the approval of internal combu
- **2020-01-20** — [[ECE R85 Rev1 Am3]] · Uniform provisions concerning the approval of internal combu
- **2019-01-16** — [[ECE R85 Rev1 Am2]] · Uniform provisions concerning the approval of internal combu
- **2016-09-22** — [[ECE R85 Rev1 Corr1]] · Uniform provisions concerning the approval of internal combu
- **2016-07-11** — [[ECE R85 Rev1 Am1]] · Uniform provisions concerning the approval of internal combu
- **2013-08-21** — [[ECE R85 Rev1]] · Uniform provisions concerning the approval of internal combu
- **1998-08-11** — [[ECE R85]] · 用于驱动 M 类和 N 类汽车的内燃机净功率或电力驱动机构 30min 最大功率测量认证的统一规定
- **1997-03-21** — [[ECE R68 Am1]] · Uniform provisions concerning the approval of power-driven v
- **1987-04-15** — [[ECE R68 (EN)]] · UNIFORM PROVISIONS CONCERNING THE APPROVAL OF POWER-DRIVEN V

## 完整索引

### cn (2)

- [[GB 17692-1999]] — 汽车用发动机净功率测试方法 · active
- [[GB T 17692-2024]] — 汽车发动机及驱动电机净功率测试方法 · 2024-06-29 · active

### ece (11)

- [[ECE R68 (EN)]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF POWER-DRIVEN VEHICLES WI · 1987-04-15 · active
- [[ECE R68]] — 关于对动力驱动车辆包括纯电动车辆的最高车速测量认证的统一规定 · unknown · active
- [[ECE R68 Am1]] — Uniform provisions concerning the approval of power-driven vehicles in · 1997-03-21 · active
- [[ECE R85]] — 用于驱动 M 类和 N 类汽车的内燃机净功率或电力驱动机构 30min 最大功率测量认证的统一规定 · 1998-08-11 · active
- [[ECE R85 Rev1]] — Uniform provisions concerning the approval of internal combustion engi · 2013-08-21 · active
- [[ECE R85 Rev1 Am1]] — Uniform provisions concerning the approval of internal combustion engi · 2016-07-11 · active
- [[ECE R85 Rev1 Am2]] — Uniform provisions concerning the approval of internal combustion engi · 2019-01-16 · active
- [[ECE R85 Rev1 Am3]] — Uniform provisions concerning the approval of internal combustion engi · 2020-01-20 · active
- [[ECE R85 Rev1 Am4]] — Uniform provisions concerning the approval of internal combustion engi · 2020-07-01 · active
- [[ECE R85 Rev1 Am5]] — Uniform provisions concerning the approval of internal combustion engi · 2023-02-17 · active
- [[ECE R85 Rev1 Corr1]] — Uniform provisions concerning the approval of internal combustion engi · 2016-09-22 · active

## 相关主题

- [[emissions_exhaust - 排放与燃料]]
- [[test_methods - 试验方法 / 测量规程]]
- [[hv_battery_ev - 电动车 / 动力电池 / 充电保护]]
