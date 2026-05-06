---
type: topic
topic_key: restraints_airbags
label: 安全带与乘员约束
note_count: 78
regions:
  ece: 56
  cn: 22
types:
  type/version: 42
  type/amendment: 36
statuses:
  active: 69
  superseded: 9
generated_by: stage4_auto
tags:
- type/topic
- topic/restraints_airbags
---

# 安全带与乘员约束（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

本主题覆盖 **乘员约束系统全链路**（66 notes，ECE=44, CN=22）：**安全带本体 → 固定点 → 儿童约束系统 → 座椅与头枕**，是整车碰撞安全（`crash_impact`）的配套执行层。

**① 安全带本体与卷收器**
- `ECE R16`：安全带总成（卷收器 / 舌片 / 紧急锁止 ELR / ALR / 预紧 / 限力器）
- 国内：`GB 14166-2013`（安全带、约束系统、儿童约束、ISOFIX 等合并，代替 GB 14166-2003）

**② 车辆侧固定点**
- `ECE R14`：安全带安装固定点 + ISOFIX 固定点 + 上拉带 Top Tether
- 国内：`GB 14167-2013`（对应 R14，合并 ISOFIX + 上拉带，覆盖 M1/N1）

**③ 儿童约束系统（CRS）**
- `ECE R44`：传统组别（0/0+/1/2/3，按体重分组）— 仍可售，但新件过渡到 R129
- `ECE R129`：i-Size 新一代（按身高分组 + 强制 ISOFIX + 侧碰测试 + 120cm+ 向前乘坐）— 本主题主体，Rev3/Rev4 Am1–Am8 持续升级
- `ECE R129-04-*`：分阶段引入的 Phase 1–4 要求（侧碰、15 个月向后、整合式 booster seats）

**④ 座椅 / 头枕 / 约束隔板**
- `ECE R17`：座椅及其固定 + 头枕抗冲击
- `ECE R25`：头枕单件认证
- `ECE R80`：M2/M3 大客车座椅强度
- `ECE R107`：M2/M3 整车结构（含座椅固定相关 — 在 `bus_coach`）
- 国内：`GB 11550-2009`（头枕强度）、`GB 13057-2014`（客车座椅及固定件）、`GB 24406-2024`（专用校车学生座椅）、`GB 15083-2019`（乘员座椅）

**⑤ 特殊乘员系统**
- `ECE R21`：内部凸出物（含仪表板 / 乘员区非刚体）— 本主题仅引用
- `ECE R137`：全宽碰撞中乘员保护系统评估

**⑥ 重点演进**
- 2013：R129 Phase 1 发布，欧洲启动 i-Size 过渡
- 2017–2020：R129 Phase 2/3（侧碰 + 15mo 反向）
- 2022–2023：R129 Rev4 Am5–Am8 完成 Phase 4（15–36kg 向前 + integral booster）；国内 `GB 14166` 增补 ISOFIX 多样化
- 2024：`GB 24406-2024` 校车座椅，代替 2012 版；细化前碰/后碰动态伤害指标

**跨区域速查**：
- `GB 14166` ≈ `ECE R16` + `R44` + `R129`（合并包装）
- `GB 14167` ≈ `ECE R14`（固定点）
- `GB 11550` ≈ `ECE R25`（头枕单件）
- `GB 15083` ≈ `ECE R17`（座椅强度）
- `GB 13057` ≈ `ECE R80`（客车座椅）
- `GB 24406` ≈ `ECE R36 附件 5` 的校车座椅特殊条款（国内要求更严的前碰动态）

## 覆盖范围

- 共 **78** 条 notes
- 按区域：ece=56, cn=22
- 按类型：type/version=42, type/amendment=36
- 按状态：active=69, superseded=9

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 11550-1995, GB 11550-2009, GB 11551-2014, GB 13057-2014, GB 13057-2023, GB 14166-2003, GB 14166-2013, GB 14166-2024, GB 14167-2006, GB 14167-2013, GB 14167-2024, GB 15083-1994, GB 15083-2019, GB 24406-2009, GB 24406-2012, GB 24406-2024, GB 27887-2011, GB 27887-2011 第1号修改单, GB 27887-2024, GB/T 24550-2009, GB/T 36125-2018, GB/T 40712-2021 |
| ece | ECE R107, ECE R114, ECE R129 Rev4 Am2 Corr1, ECE R129 Rev4 Am5, ECE R129 Rev4 Am6, ECE R129 Rev4 Am7, ECE R129-03 Rev3 Am2, ECE R129-03 Rev4, ECE R129-03 Rev4 Am3, ECE R129-04-01 Rev4 Am1, ECE R129-04-02 Rev4 Am2, ECE R129-04-04 Rev4 Am4, ECE R129-04-08 Rev4 Am8, ECE R14, ECE R14 Rev6, ECE R14 Rev6 Am1, ECE R14 Rev6 Am2, ECE R14 Rev7 Am1, ECE R14 Rev7 Am2, ECE R144, ECE R144 Am1, ECE R144 Am2, ECE R144 Rev1, ECE R144 Rev1 Am1, ECE R16, ECE R16 Rev10, ECE R16 Rev10 Am1, ECE R16 Rev10 Am2, ECE R16 Rev10 Am3, ECE R17 … (+25) |

## 时间线（最近 30 条）

- **2024-09-29** — [[GB 27887-2024]] · 机动车儿童乘员用约束系统
- **2024-09-29** — [[GB 14167-2024]] · 机动车乘员用安全带和约束系统安装固定点
- **2024-09-29** — [[GB 14166-2024]] · 机动车乘员用安全带和约束系统
- **2024-06-25** — [[GB 24406-2024]] · 专用校车学生座椅及其车辆固定件的强度
- **2023-09-08** — [[GB 13057-2023]] · 客车座椅及其车辆固定件的强度
- **2023-06-21** — [[ECE R129 Rev4 Am2 Corr1]] · Uniform provisions concerning the approval of Enhanced Child
- **2023-06-19** — [[ECE R129-04-08 Rev4 Am8]] · Uniform provisions concerning the approval of Enhanced Child
- **2023-02-21** — [[ECE R129 Rev4 Am7]] · Uniform provisions concerning the approval of Enhanced Child
- **2023-02-07** — [[ECE R144 Rev1]] · Uniform provisions concerning the Accident Emergency Call Sy
- **2022-11-30** — [[ECE R80 Rev3]] · Uniform provisions concerning the approval of seats of large
- **2022-11-11** — [[ECE R129 Rev4 Am6]] · Uniform provisions concerning the approval of Enhanced Child
- **2022-07-28** — [[ECE R16 Rev10 Am3]] · Uniform provisions concerning the approval of: I. Safety-bel
- **2022-07-28** — [[ECE R14 Rev7 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2022-07-28** — [[ECE R14 Rev6 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2022-02-18** — [[ECE R129 Rev4 Am5]] · Uniform provisions concerning the approval of Enhanced Child
- **2021-10-11** — [[GB T 40712-2021]] · 多用途货车通用技术条件
- **2021-07-02** — [[ECE R44 Rev3 Am11]] · Uniform provisions concerning the approval of restraining de
- **2021-07-02** — [[ECE R17 Rev6 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2021-07-02** — [[ECE R16 Rev10 Am2]] · Uniform provisions concerning the approval of safety-belts, 
- **2021-07-02** — [[ECE R144 Rev1 Am1]] · Uniform provisions concerning Accident Emergency Call Compon
- **2021-02-02** — [[ECE R16 Rev10 Am1]] · Uniform provisions concerning the approval of: I. Safety-bel
- **2021-02-02** — [[ECE R14 Rev7 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2021-02-02** — [[ECE R129-04-04 Rev4 Am4]] · Addendum 128 – UN Regulation No. 129 Revision 4 - Amendment 
- **2020-11-03** — [[ECE R144 Am2]] · Uniform provisions concerning Accident Emergency Call Compon
- **2020-11-03** — [[ECE R144 Am1]] · Uniform provisions concerning Accident Emergency Call Compon
- **2020-09-24** — [[ECE R129-03 Rev4]] · Uniform provisions concerning the approval of Enhanced Child
- **2020-07-24** — [[ECE R16 Rev10]] · Uniform provisions concerning the approval of safety-belts, 
- **2020-07-23** — [[ECE R14 Rev6]] · Uniform provisions concerning the approval of vehicles with 
- **2020-07-01** — [[ECE R44 Rev3 Am10]] · Uniform provisions concerning the approval of restraining de
- **2020-07-01** — [[ECE R129-03 Rev4 Am3]] · Uniform provisions concerning the approval of Enhanced Child

## 完整索引

### cn (22)

- [[GB 11550-1995]] — 汽车座椅头枕 性能要求和试验方法 · 1995-11-16 · superseded
- [[GB 11550-2009]] — 汽车座椅头枕强度要求和试验方法 · 2009-09-30 · active
- [[GB 11551-2014]] — 汽车正面碰撞的乘员保护 · 2014-09-03 · active
- [[GB 13057-2014]] — 客车座椅及其车辆固定件的强度 · 2014-10-10 · superseded
- [[GB 13057-2023]] — 客车座椅及其车辆固定件的强度 · 2023-09-08 · active
- [[GB 14166-2003]] — 汽车安全带性能要求和试验方法 · superseded
- [[GB 14166-2013]] — 机动车乘员用安全带、约束系统、儿童约束系统和ISOFIX儿童约束系统 · 2013-05-07 · superseded
- [[GB 14166-2024]] — 机动车乘员用安全带和约束系统 · 2024-09-29 · active
- [[GB 14167-2006]] — 汽车安全带安装固定点 · superseded
- [[GB 14167-2013]] — 汽车安全带安装固定点、ISOFIX固定点系统及上拉带固定点 · 2013-05-07 · superseded
- [[GB 14167-2024]] — 机动车乘员用安全带和约束系统安装固定点 · 2024-09-29 · active
- [[GB 15083-1994]] — 汽车座椅系统强度要求及试验方法 · 1994-05-31 · active
- [[GB 15083-2019]] — 汽车座椅、座椅固定装置及头枕强度要求和试验方法 · 2019-10-14 · active
- [[GB 24406-2009]] — 专用小学生校车座椅及其车辆固定件的强度 · 2009-09-30 · superseded
- [[GB 24406-2012]] — 专用校车学生座椅系统及其车辆固定件的强度 · 2012-04-10 · superseded
- [[GB 24406-2024]] — 专用校车学生座椅及其车辆固定件的强度 · 2024-06-25 · active
- [[GB 27887-2011]] — 机动车儿童乘员用约束系统 · 2011-12-30 · superseded
- [[GB 27887-2011 第1号修改单]] — 机动车儿童乘员用约束系统 国家标准第1号修改单 · active
- [[GB 27887-2024]] — 机动车儿童乘员用约束系统 · 2024-09-29 · active
- [[GB T 24550-2009]] — 汽车对行人的碰撞保护 · 2009-10-30 · active
- [[GB T 36125-2018]] — 行动不便人员运送车 · 2018-05-14 · active
- [[GB T 40712-2021]] — 多用途货车通用技术条件 · 2021-10-11 · active

### ece (56)

- [[ECE R107]] — 关于 M2或M3类车辆一般结构认证的统一规定 · 1999-07-16 · active
- [[ECE R114 (EN)]] — Uniform provisions concerning the approval of an airbag module for a r · 2003-07-02 · active
- [[ECE R114]] — 关于以下各项认证的统一规定 I. 备用安全气囊系统的安全气囊模块； II. 装备经过认证的安全气囊模块的备用方向盘； III. 未安装在方向 · 2003-07-02 · active
- [[ECE R129 Rev4 Am2 Corr1]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2023-06-21 · active
- [[ECE R129 Rev4 Am5]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2022-02-18 · active
- [[ECE R129 Rev4 Am6]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2022-11-11 · active
- [[ECE R129 Rev4 Am7]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2023-02-21 · active
- [[ECE R129-03 Rev3 Am2]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2019-01-16 · active
- [[ECE R129-03 Rev4]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2020-09-24 · active
- [[ECE R129-03 Rev4 Am3]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2020-07-01 · active
- [[ECE R129-04-01 Rev4 Am1]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2019-06-24 · active
- [[ECE R129-04-02 Rev4 Am2]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2020-01-29 · active
- [[ECE R129-04-04 Rev4 Am4]] — Addendum 128 – UN Regulation No. 129 Revision 4 - Amendment 4 · 2021-02-02 · active
- [[ECE R129-04-08 Rev4 Am8]] — Uniform provisions concerning the approval of Enhanced Child Restraint · 2023-06-19 · active
- [[ECE R14]] — 关于汽车安全带安装固定点认证的统一规定 · 2001-07-13 · active
- [[ECE R14 Rev6]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-07-23 · active
- [[ECE R14 Rev6 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2019-01-16 · active
- [[ECE R14 Rev6 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-07-28 · active
- [[ECE R14 Rev7 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-02-02 · active
- [[ECE R14 Rev7 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-07-28 · active
- [[ECE R144]] — Uniform provisions concerning the Accident Emergency Call Systems (AEC · 2018-09-04 · active
- [[ECE R144 Am1]] — Uniform provisions concerning Accident Emergency Call Components (AECC · 2020-11-03 · active
- [[ECE R144 Am2]] — Uniform provisions concerning Accident Emergency Call Components (AECC · 2020-11-03 · active
- [[ECE R144 Rev1]] — Uniform provisions concerning the Accident Emergency Call Systems (AEC · 2023-02-07 · active
- [[ECE R144 Rev1 Am1]] — Uniform provisions concerning Accident Emergency Call Components (AECC · 2021-07-02 · active
- [[ECE R16]] — 关于认证的统一规定 - 安全带及成人约束系统 · unknown · active
- [[ECE R16 Rev10]] — Uniform provisions concerning the approval of safety-belts, restraint  · 2020-07-24 · active
- [[ECE R16 Rev10 Am1]] — Uniform provisions concerning the approval of: I. Safety-belts, restra · 2021-02-02 · active
- [[ECE R16 Rev10 Am2]] — Uniform provisions concerning the approval of safety-belts, restraint  · 2021-07-02 · active
- [[ECE R16 Rev10 Am3]] — Uniform provisions concerning the approval of: I. Safety-belts, restra · 2022-07-28 · active
- [[ECE R17]] — 关于车辆座椅、座椅固定装置及头枕认证的统一规定 · 2000-04-01 · active
- [[ECE R17 Rev6]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-06-11 · active
- [[ECE R17 Rev6 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-01-17 · active
- [[ECE R17 Rev6 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-07-02 · active
- [[ECE R25]] — 关于头枕（不论其是否与座椅连为一体）认证的统一规定 · 1997-04-16 · active
- [[ECE R25 (04 series of amendments) Rev1 Am2]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF HEAD RESTRAINTS (HEADRES · 1997-04-16 · active
- [[ECE R25 Rev1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF HEAD RESTRAINTS (HEADRES · 1990-04-26 · active
- [[ECE R25 Rev1 Am1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF HEAD RESTRAINTS (HEADRES · 1994-01-30 · active
- [[ECE R25 Rev1 Am3]] — Uniform provisions concerning the approval of head restraints (headres · 2015-06-22 · active
- [[ECE R44]] — 动力驱动汽车儿童乘客的约束保护装置认证的统一规定 · unknown · active
- [[ECE R44 Rev3]] — Uniform provisions concerning the approval of restraining devices for  · 2014-02-27 · active
- [[ECE R44 Rev3 Am1]] — Uniform provisions concerning the approval of restraining devices for  · 2015-02-03 · active
- [[ECE R44 Rev3 Am10]] — Uniform provisions concerning the approval of restraining devices for  · 2020-07-01 · active
- [[ECE R44 Rev3 Am11]] — Uniform provisions concerning the approval of restraining devices for  · 2021-07-02 · active
- [[ECE R44 Rev3 Am2]] — Uniform provisions concerning the approval of restraining devices for  · 2015-06-22 · active
- [[ECE R44 Rev3 Am4]] — Uniform provisions concerning the approval of restraining devices for  · 2017-02-22 · active
- [[ECE R44 Rev3 Am5]] — Addendum 43 – Regulation No. 44, Revision 3 – Amendment 5 · 2017-07-26 · active
- [[ECE R44 Rev3 Am6]] — Uniform provisions concerning the approval of restraining devices for  · 2018-08-10 · active
- [[ECE R44 Rev3 Am7]] — Uniform provisions concerning the approval of restraining devices for  · 2019-01-16 · active
- [[ECE R44 Rev3 Am8]] — Uniform provisions concerning the approval of restraining devices for  · 2019-06-24 · active
- [[ECE R44 Rev3 Am9]] — Uniform provisions concerning the approval of restraining devices for  · 2020-01-17 · active
- [[ECE R44 Rev3 Corr1]] — Uniform provisions concerning the approval of restraining devices for  · 2014-03-31 · active
- [[ECE R44-r3 Am3 Rev3]] — Uniform provisions concerning the approval of restraining devices for  · 2016-07-11 · active
- [[ECE R80]] — 关于客车座椅及座椅固定点装置强度认证的统一规定 · 2001-07-18 · active
- [[ECE R80 Rev3]] — Uniform provisions concerning the approval of seats of large passenger · 2022-11-30 · active
- [[R.E.3]] — 汽车结构的强化标准 · 1997-08-11 · active

## 相关主题

- [[special_vehicles - 特种 / 危险车辆]]
- [[emissions_exhaust - 排放与燃料]]
- [[energy_labeling - 能耗 / 油耗标识]]
- [[crash_impact - 碰撞与被动安全]]
- [[test_methods - 试验方法 / 测量规程]]
