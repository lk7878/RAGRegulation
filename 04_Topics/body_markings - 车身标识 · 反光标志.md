---
type: topic
topic_key: body_markings
label: 车身标识 / 反光标志
note_count: 26
regions:
  ece: 13
  cn: 13
types:
  type/version: 16
  type/amendment: 10
statuses:
  active: 25
  superseded: 1
generated_by: stage4_auto
tags:
- type/topic
- topic/body_markings
---

# 车身标识 / 反光标志（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

车身标识主题（26 notes，ECE=13, CN=13）覆盖 **反光标识 + 车辆标识板 + 车道专用警示** 三类被动安全提示，与 `lighting_signaling` 主题的主动灯具形成互补。

**① 反光材料认证**
- `ECE R104`：商用车和长车辆反光标识材料（级别 C/D/E 分类）— Rev1 Am1–Am4 持续修订，对应 **被动反光标识条**
- `ECE R150`：回复反射装置整车安装（替代 R70 老版）— Am1–Am5 跟进 2020 后新体系

**② 国内合并标准**
- `GB 11564-2024`：机动车回复反射装置 — **合并回复反射器 + 车身反光标识 + 车辆尾部标志板 + 三角警告牌**，最新大修订（2024）
- `GB 23254-2009`：货车及挂车车身反光标识（GB 11564 收录后，独立价值降低）
- `GB 23826-2009`：高速公路 LED 可变限速标志（主动灯但归本主题）

**③ 专用车辆标识**
- `GB 24315-2009` + 其 XG1-2012 修改单：《校车标识》 — 包括校车前 / 后 / 侧面反光警示
- `GB 21253-2007`：奥林匹克专用车道标志和标线（特定场景车道标记）
- `GB 24965.2-2010`：交通警示灯 第 2 部分：黄色闪烁警示灯

**④ 重点演进**
- 2015–2020：R150 接替老 R70 分立流程，WP.29 归一成 1 套反射装置总法规
- 2023：R150 Am5 明确新型 Class V 反射等级参数
- 2024：`GB 11564-2024` 一次重写，国内反射装置法规从 "多标并行" 进入 "一标统一"
- 持续：`ECE R104` / `R150` 每季度微调反射等级、色度角要求

**跨区域速查**：
- `GB 11564` ≈ `ECE R104 + R3 + R150`（国内 3 合 1）
- `GB 23254` 部分被 GB 11564 吸收，保留为 **具体货车应用指南**
- `GB 24315` 无 ECE 对应（校车标识是 **国内独有**）

> 与 `lighting_signaling` 的区别：本主题专注 **无源 / 被动反光元件**（含变速标志的 LED 可变限速牌）；主动灯（前照灯 / 信号灯）归 `lighting_signaling`。

## 覆盖范围

- 共 **26** 条 notes
- 按区域：ece=13, cn=13
- 按类型：type/version=16, type/amendment=10
- 按状态：active=25, superseded=1

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 21253-2007, GB 23254-2009, GB 23826-2009, GB 24315-2009, GB 24315-2009/XG1-2012, GB 24965.2-2010, GB 5768-1999, GB 5768.1-2009, GB 5768.2-2022, GB 5768.3-2009, GB 5768.4-2017, GB 5768.5-2017, GB 5768.6-2017 |
| ece | ECE R104, ECE R104 Rev1, ECE R104 Rev1 Am1, ECE R104 Rev1 Am2, ECE R104 Rev1 Am3, ECE R104 Rev1 Am4, ECE R104 Rev1 Corr1, ECE R104 Rev1 Corr2, ECE R150, ECE R150 Am1, ECE R150 Am2, ECE R150 Am3, ECE R150 Am5 |

## 时间线（最近 30 条）

- **2023-03-03** — [[ECE R150 Am5]] · Uniform provisions concerning the approval of retro-reflecti
- **2022-03-15** — [[GB 5768.2-2022]] · 道路交通标志和标线 第2部分：道路交通标志
- **2021-12-17** — [[ECE R150 Am3]] · Uniform provisions concerning the approval of retro-reflecti
- **2020-11-03** — [[ECE R150 Am2]] · Uniform provisions concerning the approval of retro-reflecti
- **2020-07-01** — [[ECE R150 Am1]] · Uniform provisions concerning the approval of retro-reflecti
- **2020-01-13** — [[ECE R150]] · Uniform provisions concerning the approval of retro-reflecti
- **2019-11-19** — [[ECE R104 Rev1 Am4]] · Addendum 103 – UN Regulation No. 104 Revision 1 - Amendment 
- **2017-12-07** — [[ECE R104 Rev1 Am3]] · Uniform provisions concerning the approval of retro-reflecti
- **2017-07-31** — [[GB 5768.6-2017]] · 道路交通标志和标线 第6部分：铁路道口
- **2017-07-31** — [[GB 5768.5-2017]] · 道路交通标志和标线 第5部分：限制速度
- **2017-07-31** — [[GB 5768.4-2017]] · 道路交通标志和标线 第4部分：作业区
- **2015-06-22** — [[ECE R104 Rev1 Am2]] · Uniform provisions concerning the approval of retro-reflecti
- **2012-08-15** — [[ECE R104 Rev1 Am1]] · Uniform provisions concerning the approval of retro-reflecti
- **2010-12-02** — [[ECE R104 Rev1 Corr2]] · Uniform provisions concerning the approval of retro-reflecti
- **2010-08-09** — [[GB 24965.2-2010]] · 交通警示灯 第2部分：黄色闪烁警示灯
- **2010-07-05** — [[ECE R104 Rev1 Corr1]] · Uniform provisions concerning the approval of retro-reflecti
- **2010-03-25** — [[ECE R104 Rev1]] · UNIFORM PROVISIONS CONCERNING THE APPROVAL OF RETRO-REFLECTI
- **2009-09-30** — [[GB 24315-2009]] · 校车标识
- **2009-05-25** — [[GB 5768.3-2009]] · 道路交通标志和标线 第3部分：道路交通标线
- **2009-05-25** — [[GB 5768.1-2009]] · 道路交通标志和标线 第1部分：总则
- **2009-05-25** — [[GB 23826-2009]] · 高速公路 LED 可变限速标志
- **2009-03-06** — [[GB 23254-2009]] · 货车及挂车 车身反光标识
- **2007-11-01** — [[GB 21253-2007]] · 奥林匹克专用车道标志和标线
- **2000-12-01** — [[ECE R104]] · 重型、长型车及其挂车回复反射标志认证的统一规定
- **1999-04-05** — [[GB 5768-1999]] · 道路交通标志和标线

## 完整索引

### cn (13)

- [[GB 21253-2007]] — 奥林匹克专用车道标志和标线 · 2007-11-01 · active
- [[GB 23254-2009]] — 货车及挂车 车身反光标识 · 2009-03-06 · active
- [[GB 23826-2009]] — 高速公路 LED 可变限速标志 · 2009-05-25 · active
- [[GB 24315-2009]] — 校车标识 · 2009-09-30 · active
- [[GB 24315-2009 XG1-2012]] — 《校车标识》国家标准第1号修改单 · active
- [[GB 24965.2-2010]] — 交通警示灯 第2部分：黄色闪烁警示灯 · 2010-08-09 · active
- [[GB 5768-1999]] — 道路交通标志和标线 · 1999-04-05 · superseded
- [[GB 5768.1-2009]] — 道路交通标志和标线 第1部分：总则 · 2009-05-25 · active
- [[GB 5768.2-2022]] — 道路交通标志和标线 第2部分：道路交通标志 · 2022-03-15 · active
- [[GB 5768.3-2009]] — 道路交通标志和标线 第3部分：道路交通标线 · 2009-05-25 · active
- [[GB 5768.4-2017]] — 道路交通标志和标线 第4部分：作业区 · 2017-07-31 · active
- [[GB 5768.5-2017]] — 道路交通标志和标线 第5部分：限制速度 · 2017-07-31 · active
- [[GB 5768.6-2017]] — 道路交通标志和标线 第6部分：铁路道口 · 2017-07-31 · active

### ece (13)

- [[ECE R104]] — 重型、长型车及其挂车回复反射标志认证的统一规定 · 2000-12-01 · active
- [[ECE R104 Rev1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF RETRO-REFLECTIVE MARKING · 2010-03-25 · active
- [[ECE R104 Rev1 Am1]] — Uniform provisions concerning the approval of retro-reflective marking · 2012-08-15 · active
- [[ECE R104 Rev1 Am2]] — Uniform provisions concerning the approval of retro-reflective marking · 2015-06-22 · active
- [[ECE R104 Rev1 Am3]] — Uniform provisions concerning the approval of retro-reflective marking · 2017-12-07 · active
- [[ECE R104 Rev1 Am4]] — Addendum 103 – UN Regulation No. 104 Revision 1 - Amendment 4 · 2019-11-19 · active
- [[ECE R104 Rev1 Corr1]] — Uniform provisions concerning the approval of retro-reflective marking · 2010-07-05 · active
- [[ECE R104 Rev1 Corr2]] — Uniform provisions concerning the approval of retro-reflective marking · 2010-12-02 · active
- [[ECE R150]] — Uniform provisions concerning the approval of retro-reflective devices · 2020-01-13 · active
- [[ECE R150 Am1]] — Uniform provisions concerning the approval of retro-reflective devices · 2020-07-01 · active
- [[ECE R150 Am2]] — Uniform provisions concerning the approval of retro-reflective devices · 2020-11-03 · active
- [[ECE R150 Am3]] — Uniform provisions concerning the approval of retro-reflective devices · 2021-12-17 · active
- [[ECE R150 Am5]] — Uniform provisions concerning the approval of retro-reflective devices · 2023-03-03 · active

## 相关主题

- [[speed_control_speedometer - 车速 / 限速装置]]
- [[bus_coach - 客车 / 公交车]]
- [[tires_wheels - 轮胎与车轮]]
- [[lighting_signaling - 照明与信号装置]]
