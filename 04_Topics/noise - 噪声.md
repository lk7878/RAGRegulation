---
type: topic
topic_key: noise
label: 噪声
note_count: 68
regions:
  ece: 64
  cn: 4
types:
  type/amendment: 48
  type/version: 20
statuses:
  active: 67
  original: 1
generated_by: stage4_auto
tags:
- type/topic
- topic/noise
---

# 噪声（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

噪声主题（68 notes，ECE=63, CN=5）聚焦 **整车辐射噪声 + 轮胎滚动噪声 + 电动车最低警示声** 三类，外加少量 L 类 / 非道路机械（拖拉机、土方机械）专项。ECE 以 `R41/R51/R59/R63/R92/R117/R138` 为主。

**① 整车对外噪声（pass-by）**
- `ECE R51`：四轮以上机动车噪声（M/N 类）— 核心标准，Rev3 Am1–Am2 对齐 EU (EC) 540/2014 三阶段限值下调
- `ECE R41`：L 类摩托车噪声（Rev2 多次 Am，与环境政策耦合）
- `ECE R63`：轻便摩托车（moped）噪声
- 国内：`GB 1495`（加速行驶车外噪声，未在本簇），`GB/T 40625-2021`（室内底盘测功机测量法，对应 R51 测试替代方案）

**② 排气系统与消声器**
- `ECE R59`：替换消声器系统认证
- `ECE R92`：L 类摩托替换消声器

**③ 轮胎噪声**
- `ECE R117`：滚动阻力 + 湿地抓地 + **通过噪声**（Rolling Noise 综合标签）— 同时出现在 `tires_wheels` 主题，本主题收录其 "噪声" 维度

**④ 电动车最低警示声（AVAS）**
- `ECE R138`：Quiet Road Transport Vehicles (M/N1 EV/HEV)，规定低速下最低声压 + 多普勒频移 + pause-function 的禁用
- 发展：2022 Am1–Am2 后禁用 pause 按钮、提高低速段声强下限

**⑤ 工程机械类（边缘）**
- `GB 16710-2010`：土方机械机外发射噪声 + 司机位置噪声
- `GB 6376-2008`：农林拖拉机噪声限值

**⑥ 重点里程碑**
- 2014：EU 540/2014 三阶段降噪 (Phase 1: 2016, Phase 2: 2020, Phase 3: 2024)，驱动 R51 Rev3 Am1+
- 2017：R138 正式纳入 EU 540，强制 EV 配 AVAS（2019/7 起）
- 2018：R117 Rev4 Am1–Am3 升级噪声测量到 68 km/h 参考速度
- 2021：`GB/T 40625-2021` 发布，国内启动室内测量方案对标 R51

**跨区域速查**：
- `GB 1495` ≈ `ECE R51`（整车噪声，限值国内较 EU Phase 2 略松）
- `GB/T 40625` ≈ `ECE R51 Annex 7`（室内替代法）
- `ECE R138` 无国内直接等效；`GB/T 37153`（电动车低速提示音）仅参考引用
- `ECE R117` 噪声部分 ≈ `GB/T 26985`（轮胎噪声试验方法）

## 覆盖范围

- 共 **68** 条 notes
- 按区域：ece=64, cn=4
- 按类型：type/amendment=48, type/version=20
- 按状态：active=67, original=1

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 1495-2002, GB 16710-2010, GB 6376-2008, GB/T 40578-2021 |
| ece | ECE R117 Rev4, ECE R117 Rev4 Am1, ECE R117 Rev4 Am3, ECE R117 Rev4 Am4, ECE R117 Rev4 Am6, ECE R117-03 Rev4 Am7, ECE R117-04am5 Rev4 Am5, ECE R138, ECE R138 Am1, ECE R138 Am2, ECE R138 Rev1, ECE R138 Rev1 Am1, ECE R138 Rev1 Am2, ECE R41 Rev2, ECE R41 Rev2 Am1, ECE R41 Rev2 Am10, ECE R41 Rev2 Am11, ECE R41 Rev2 Am2, ECE R41 Rev2 Am3, ECE R41 Rev2 Am4, ECE R41 Rev2 Am5, ECE R41 Rev2 Am6, ECE R41 Rev2 Am7, ECE R41 Rev2 Am8, ECE R41 Rev2 Am9, ECE R51, ECE R51 Rev2, ECE R51 Rev3 Am1, ECE R51 Rev3 Am2, ECE R51 Rev3 Am3 … (+33) |

## 时间线（最近 30 条）

- **2023-02-20** — [[ECE R117-03 Rev4 Am7]] · Uniform provisions concerning the approval of tyres with reg
- **2023-02-13** — [[ECE R51 Rev3 Am7]] · Uniform provisions concerning the approval of motor vehicles
- **2022-11-23** — [[ECE R117 Rev4 Am6]] · Uniform provisions concerning the approval of tyres with reg
- **2022-11-11** — [[ECE R63 Rev1 Am5]] · Uniform provisions concerning the approval of L1 category ve
- **2022-02-21** — [[ECE R41 Rev2 Am11]] · Uniform provisions concerning the approval of motor cycles w
- **2021-12-10** — [[ECE R117-04am5 Rev4 Am5]] · Addendum 116 – UN Regulation No. 117
Revision 4 - Amendment 
- **2021-11-30** — [[ECE R41 Rev2 Am9]] · Addendum 40 – UN Regulation No. 41, Revision 2 - Amendment 9
- **2021-11-26** — [[ECE R41 Rev2 Am10]] · Uniform provisions concerning the approval of motorcycles wi
- **2021-10-11** — [[GB T 40578-2021]] · 轻型汽车多工况行驶车外噪声测量方法
- **2021-02-02** — [[ECE R41 Rev2 Am8]] · Uniform provisions concerning the approval of motor cycles w
- **2021-02-02** — [[ECE R138 Rev1 Am2]] · Uniform provisions concerning the approval of Quiet Road Tra
- **2021-02-02** — [[ECE R117 Rev4 Am4]] · Uniform provisions concerning the approval of tyres with reg
- **2020-11-04** — [[ECE R117 Rev4 Am3]] · Uniform provisions concerning the approval of tyres with reg
- **2020-11-02** — [[ECE R59 Rev2 Am2]] · Uniform provisions concerning the approval of replacement si
- **2020-11-02** — [[ECE R51 Rev3 Am6]] · Uniform provisions concerning the approval of motor vehicles
- **2020-10-29** — [[ECE R9 Rev4 Am1]] · Uniform provisions concerning the approval of category L2, L
- **2020-01-29** — [[ECE R138 Rev1 Am1]] · Uniform provisions concerning the approval of Quiet Road Tra
- **2019-11-19** — [[ECE R92 Rev1 Am3]] · Uniform provisions concerning the approval of non-original r
- **2019-11-11** — [[ECE R51 Rev3 Am5]] · Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 5
- **2019-11-08** — [[ECE R41 Rev2 Am7]] · UN Regulation No. 41 - Noise emissions of motorcycles
- **2019-11-07** — [[ECE R9 Rev3 Am4]] · UN Regulation No. 9 - Noise of three-wheeled vehicles
- **2019-01-16** — [[ECE R63 Rev1 Am4]] · Uniform provisions concerning the approval of L1 category ve
- **2019-01-16** — [[ECE R51 Rev3 Am4]] · Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 4
- **2018-11-05** — [[ECE R51 Rev3 Am3]] · Uniform provisions concerning the approval of motor vehicles
- **2018-11-02** — [[ECE R41 Rev2 Am6]] · Uniform provisions concerning the approval of motor cycles w
- **2018-04-26** — [[ECE R51 Rev3 Am2]] · Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 2
- **2017-12-11** — [[ECE R138 Am2]] · Uniform provisions concerning the approval of Quiet Road Tra
- **2017-12-11** — [[ECE R138 Am1]] · Uniform provisions concerning the approval of Quiet Road Tra
- **2017-12-07** — [[ECE R92 Rev1 Am2]] · Uniform provisions concerning the approval of non-original r
- **2017-11-16** — [[ECE R138 Rev1]] · Uniform provisions concerning the approval of Quiet Road Tra

## 完整索引

### cn (4)

- [[GB 1495-2002]] — 汽车加速行驶车外噪声限值及测量方法 · 2002-01-04 · active
- [[GB 16710-2010]] — 土方机械 噪声限值 · 2010-12-23 · active
- [[GB 6376-2008]] — 拖拉机 噪声限值 · 2008-11-17 · active
- [[GB T 40578-2021]] — 轻型汽车多工况行驶车外噪声测量方法 · 2021-10-11 · active

### ece (64)

- [[ECE R117 Rev4]] — Uniform provisions concerning the approval of tyres with regard to rol · 2016-02-16 · active
- [[ECE R117 Rev4 Am1]] — Uniform provisions concerning the approval of tyres with regard to rol · 2017-02-22 · active
- [[ECE R117 Rev4 Am3]] — Uniform provisions concerning the approval of tyres with regard to rol · 2020-11-04 · active
- [[ECE R117 Rev4 Am4]] — Uniform provisions concerning the approval of tyres with regard to rol · 2021-02-02 · active
- [[ECE R117 Rev4 Am6]] — Uniform provisions concerning the approval of tyres with regard to rol · 2022-11-23 · active
- [[ECE R117-03 Rev4 Am7]] — Uniform provisions concerning the approval of tyres with regard to rol · 2023-02-20 · active
- [[ECE R117-04am5 Rev4 Am5]] — Addendum 116 – UN Regulation No. 117
Revision 4 - Amendment 5
Suppleme · 2021-12-10 · active
- [[ECE R138]] — Uniform provisions concerning the approval of Quiet Road Transport Veh · 2016-10-24 · active
- [[ECE R138 Am1]] — Uniform provisions concerning the approval of Quiet Road Transport Veh · 2017-12-11 · active
- [[ECE R138 Am2]] — Uniform provisions concerning the approval of Quiet Road Transport Veh · 2017-12-11 · active
- [[ECE R138 Rev1]] — Uniform provisions concerning the approval of Quiet Road Transport Veh · 2017-11-16 · active
- [[ECE R138 Rev1 Am1]] — Uniform provisions concerning the approval of Quiet Road Transport Veh · 2020-01-29 · active
- [[ECE R138 Rev1 Am2]] — Uniform provisions concerning the approval of Quiet Road Transport Veh · 2021-02-02 · active
- [[ECE R41 Rev2]] — Uniform provisions concerning the approval of motor cycles with regard · 2012-08-14 · active
- [[ECE R41 Rev2 Am1]] — Uniform provisions concerning the approval of motor cycles with regard · 2014-10-17 · active
- [[ECE R41 Rev2 Am10]] — Uniform provisions concerning the approval of motorcycles with regard  · 2021-11-26 · active
- [[ECE R41 Rev2 Am11]] — Uniform provisions concerning the approval of motor cycles with regard · 2022-02-21 · active
- [[ECE R41 Rev2 Am2]] — Uniform provisions concerning the approval of motor cycles with regard · 2015-11-09 · active
- [[ECE R41 Rev2 Am3]] — Uniform provisions concerning the approval of motor cycles with regard · 2016-02-05 · active
- [[ECE R41 Rev2 Am4]] — Uniform provisions concerning the approval of motor cycles with regard · 2016-10-28 · active
- [[ECE R41 Rev2 Am5]] — Uniform provisions concerning the approval of motor cycles with regard · 2017-02-22 · active
- [[ECE R41 Rev2 Am6]] — Uniform provisions concerning the approval of motor cycles with regard · 2018-11-02 · active
- [[ECE R41 Rev2 Am7]] — UN Regulation No. 41 - Noise emissions of motorcycles · 2019-11-08 · active
- [[ECE R41 Rev2 Am8]] — Uniform provisions concerning the approval of motor cycles with regard · 2021-02-02 · active
- [[ECE R41 Rev2 Am9]] — Addendum 40 – UN Regulation No. 41, Revision 2 - Amendment 9 · 2021-11-30 · active
- [[ECE R51]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF MOTOR VEHICLES HAVING AT · unknown · active
- [[ECE R51 Rev2]] — Uniform provisions concerning the approval of motor vehicles having at · 2011-11-29 · active
- [[ECE R51 Rev3 Am1]] — Uniform provisions concerning the approval of motor vehicles having at · 2016-10-28 · active
- [[ECE R51 Rev3 Am2]] — Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 2 · 2018-04-26 · active
- [[ECE R51 Rev3 Am3]] — Uniform provisions concerning the approval of motor vehicles having at · 2018-11-05 · active
- [[ECE R51 Rev3 Am4]] — Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 4 · 2019-01-16 · active
- [[ECE R51 Rev3 Am5]] — Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 5, Suppleme · 2019-11-11 · active
- [[ECE R51 Rev3 Am6]] — Uniform provisions concerning the approval of motor vehicles having at · 2020-11-02 · active
- [[ECE R51 Rev3 Am7]] — Uniform provisions concerning the approval of motor vehicles having at · 2023-02-13 · active
- [[ECE R51.03 Rev3]] — Uniform provisions concerning the approval of motor vehicles having at · 2016-02-05 · active
- [[ECE R59 (EN)]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF REPLACEMENT SILENCING SY · 1983-09-22 · active
- [[ECE R59]] — 关于替代消声系统认证的统一规定 · 1995-04-11 · active
- [[ECE R59 Am1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF REPLACEMENT SILENCING SY · 1990-01-22 · active
- [[ECE R59 Am2 Rev059]] — Uniform provisions concerning the approval of replacement silencing sy · 1995-04-11 · active
- [[ECE R59 Am3]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF REPLACEMENT SILENCING SY · 2006-11-10 · active
- [[ECE R59 Rev1]] — Uniform provisions concerning the approval of replacement silencing sy · 1990-01-28 · active
- [[ECE R59 Rev2]] — Uniform provisions concerning the approval of replacement silencing sy · 2015-11-09 · active
- [[ECE R59 Rev2 Am1]] — Uniform provisions concerning the approval of replacement silencing sy · 2016-02-05 · active
- [[ECE R59 Rev2 Am2]] — Uniform provisions concerning the approval of replacement silencing sy · 2020-11-02 · active
- [[ECE R63]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF MOPEDS WITH REGARD TO NO · 1985-06-24 · original
- [[ECE R63 Am1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF TWO-WHEELED MOPEDS WITH  · 1999-07-16 · active
- [[ECE R63 Am1 Corr1]] — Uniform provisions concerning the approval of two-wheeled mopeds with  · 1999-09-29 · active
- [[ECE R63 Am1 Corr2]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF TWO-WHEELED MOPEDS WITH  · 2001-07-18 · active
- [[ECE R63 Am2 Rev063]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF TWO-WHEELED MOPEDS WITH  · 2006-11-14 · active
- [[ECE R63 Rev1]] — Uniform provisions concerning the approval of two-wheeled mopeds with  · 2013-12-02 · active
- [[ECE R63 Rev1 Am1]] — Uniform provisions concerning the approval of two-wheeled mopeds with  · 2016-02-05 · active
- [[ECE R63 Rev1 Am2]] — Uniform provisions concerning the approval of two-wheeled mopeds with  · 2017-02-22 · active
- [[ECE R63 Rev1 Am3]] — Uniform provisions concerning the approval of L category vehicles with · 2017-10-10 · active
- [[ECE R63 Rev1 Am4]] — Uniform provisions concerning the approval of L1 category vehicles wit · 2019-01-16 · active
- [[ECE R63 Rev1 Am5]] — Uniform provisions concerning the approval of L1 category vehicles wit · 2022-11-11 · active
- [[ECE R9 Rev3]] — Uniform provisions concerning the approval of category L2, L4 and L5 v · 2013-12-02 · active
- [[ECE R9 Rev3 Am1]] — Uniform provisions concerning the approval of category L2, L4 and L5 v · 2016-02-05 · active
- [[ECE R9 Rev3 Am2]] — Uniform provisions concerning the approval of category L2, L4 and L5 v · 2017-02-22 · active
- [[ECE R9 Rev3 Am4]] — UN Regulation No. 9 - Noise of three-wheeled vehicles · 2019-11-07 · active
- [[ECE R9 Rev4 Am1]] — Uniform provisions concerning the approval of category L2, L4 and L5 v · 2020-10-29 · active
- [[ECE R92 Rev1]] — Uniform provisions concerning the approval of non-original replacement · 2012-12-05 · active
- [[ECE R92 Rev1 Am1]] — Uniform provisions concerning the approval of non-original replacement · 2017-02-22 · active
- [[ECE R92 Rev1 Am2]] — Uniform provisions concerning the approval of non-original replacement · 2017-12-07 · active
- [[ECE R92 Rev1 Am3]] — Uniform provisions concerning the approval of non-original replacement · 2019-11-19 · active

## 相关主题

- [[motorcycle - 摩托车 / L 类]]
- [[tires_wheels - 轮胎与车轮]]
- [[emissions_exhaust - 排放与燃料]]
- [[identification - 车辆识别 / 标记]]
- [[type_approval_general - 总体型式认证 / 通用要求]]
