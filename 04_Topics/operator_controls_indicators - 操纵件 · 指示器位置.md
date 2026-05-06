---
type: topic
topic_key: operator_controls_indicators
label: 操纵件 / 指示器位置
note_count: 38
regions:
  ece: 26
  cn: 12
types:
  type/version: 20
  type/amendment: 18
statuses:
  active: 35
  superseded: 3
generated_by: stage4_auto
tags:
- type/topic
- topic/operator_controls_indicators
---

# 操纵件 / 指示器位置（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

操纵件与指示器位置主题（34 notes，几乎全 ECE R121 家族）聚焦 **驾驶员人机接口**：手动控制件（按钮 / 旋钮 / 杆柄）+ 告警指示灯（tell-tales）+ 仪表 / 信号装置的位置、图形符号、颜色规范。

**① ECE 核心**
- `ECE R121`：M、N 类机动车辆手操纵件 / 指示器 / 告警信号装置的位置和标识（Rev1 / Rev2 连续 Am1–Am7 多次修订）
  - 位置约束（驾驶员可及范围）
  - 识别符号（ISO 2575 标准化图形）
  - 颜色编码（红=警告 / 黄=提示 / 绿=运行 / 蓝=远光）
  - 照明 / 可读性要求
- `ECE R35`：踏板布置位置
- `ECE R60`：L 类摩托车操纵件位置

**② 国内对应**
- `GB 4094`：汽车操纵件、指示器及信号装置的标志（对应 R121 + ISO 2575）
- `GB 15365`：摩托车和轻便摩托车操纵件、指示器及信号装置的图形符号（对应 R60）
- `GB/T 17867`：汽车手操纵件、指示器及信号装置的位置（在 `lighting_signaling`，与本主题相邻）

**③ 智能座舱挑战**
- R121 原本为机械仪表设计，**大屏 / 可重配置数字仪表的合规性**是当前修订焦点
- 2022+ Am7: 明确数字告警灯需符合亮度、响应时间 + 防止驾驶员遮挡误切
- 国内：`GB 4094` 2021 修订版加入新能源车状态指示（绿色车辆就绪、充电状态等）

**④ 与其它主题关系**
- `lighting_signaling`：外部信号灯（前照灯、转向灯）
- `identification`：车辆外部标识（VIN、制造厂代号）
- `interior_protrusions`：仪表板硬件尖锐点
- 本主题专注 **驾驶员主观可见/可及的控制与告警**

**跨区域速查**：
- `GB 4094` ≈ `ECE R121`（操纵件位置标识，国内含新能源扩展）
- `GB 15365` ≈ `ECE R60`（L 类操纵件图形符号）
- `GB/T 17867` 涵盖 R121 位置相关部分，图形符号部分由 GB 4094 承担

## 覆盖范围

- 共 **38** 条 notes
- 按区域：ece=26, cn=12
- 按类型：type/version=20, type/amendment=18
- 按状态：active=35, superseded=3

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 11561-1989, GB 15365-1994, GB 15365-2008, GB 4094-2016, GB/T 17867-1999, GB/T 17867-2023, GB/T 21055-2007, GB/T 4094.2-2005, GB/T 4094.2-2017, GB/T 43382-2023, GB/T 43402-2023, GB/T 4782-2001 |
| ece | ECE R121, ECE R121 Rev1, ECE R121 Rev1 Am1, ECE R121 Rev1 Am2, ECE R121 Rev1 Am3, ECE R121 Rev1 Am3 Corr1, ECE R121 Rev1 Am4, ECE R121 Rev1 Am5, ECE R121 Rev1 Am6, ECE R121 Rev1 Am7, ECE R121 Rev2, ECE R121 Rev2 Am1, ECE R121 Rev2 Am2, ECE R121 Rev2 Am3, ECE R121 Rev2 Am4, ECE R121 Rev2 Am5, ECE R35, ECE R35 Rev1, ECE R35 Rev1 Am1, ECE R35 Rev1 Am2, ECE R60, ECE R60 Am1, ECE R60 Am2, ECE R60 Am3, ECE R60 Rev1, ECE R60 Rev1 Am1 |

## 时间线（最近 30 条）

- **2023-11-27** — [[GB T 43402-2023]] · 乘用车 驾驶员手控制区域
- **2023-11-27** — [[GB T 43382-2023]] · 道路车辆手控装置常规运动方向
- **2023-11-27** — [[GB T 17867-2023]] · 汽车手操纵件、指示器及信号装置的位置
- **2022-11-15** — [[ECE R121 Rev2 Am5]] · Uniform provisions concerning the approval of vehicles with 
- **2021-07-02** — [[ECE R35 Rev1 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2020-11-02** — [[ECE R121 Rev2 Am4]] · Uniform provisions concerning the approval of vehicles with 
- **2018-11-02** — [[ECE R121 Rev2 Am3]] · Uniform provisions concerning the approval of vehicles with 
- **2018-11-02** — [[ECE R121 Rev1 Am7]] · Uniform provisions concerning the approval of vehicles with 
- **2018-08-10** — [[ECE R121 Rev2 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2017-09-29** — [[GB T 4094.2-2017]] · 电动汽车 操纵件、指示器及信号装置的标志
- **2017-07-26** — [[ECE R121 Rev2 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2017-07-26** — [[ECE R121 Rev1 Am6]] · Uniform provisions concerning the approval of vehicles with 
- **2017-02-22** — [[ECE R60 Rev1 Am1]] · Uniform provisions concerning the approval of two-wheeled mo
- **2016-12-30** — [[GB 4094-2016]] · 汽车操纵件、指示器及信号装置的标志
- **2015-11-12** — [[ECE R121 Rev2]] · Uniform provisions concerning the approval of vehicles with 
- **2015-06-22** — [[ECE R121 Rev1 Am5]] · Uniform provisions concerning the approval of vehicles with 
- **2014-12-20** — [[ECE R121 Rev1 Am3 Corr1]] · Uniform provisions concerning the approval of vehicles with 
- **2013-08-06** — [[ECE R121 Rev1 Am4]] · Uniform provisions concerning the approval of vehicles with 
- **2013-01-07** — [[ECE R121 Rev1 Am3]] · Uniform provisions concerning the approval of vehicles with 
- **2012-08-15** — [[ECE R121 Rev1 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2011-12-12** — [[ECE R121 Rev1 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2011-10-04** — [[ECE R121 Rev1]] · Uniform provisions concerning the approval of vehicles with 
- **2008-12-31** — [[GB 15365-2008]] · 摩托车和轻便摩托车操纵件、指示器及信号装置的图形符号
- **2007-08-13** — [[GB T 21055-2007]] · 肢体残疾人驾驶汽车的操纵辅助装置
- **2006-11-14** — [[ECE R60 Am3]] · Uniform provisions concerning the approval of two-wheeled mo
- **2006-10-10** — [[ECE R35 Rev1 Am1]] · UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH 
- **2006-01-18** — [[ECE R121]] · 关于手控装置、信号装置和指示器位置及识别的车辆认证的统一规定
- **2004-10-01** — [[ECE R60 Am2]] · UNIFORM PROVISIONS CONCERNING THE APPROVAL OF TWO-WHEELED MO
- **2001-07-03** — [[GB T 4782-2001]] · 道路车辆 操纵件、指示器及信号装置 词汇
- **1999-05** — [[ECE R35]] · 关于车辆脚制动控制器装配位置认证的统一规定

## 完整索引

### cn (12)

- [[GB 11561-1989]] — 汽车加速器控制系统的技术要求 · 1989-08-10 · active
- [[GB 15365-1994]] — 摩托车操纵件、指示器及信号装置的图形符号 · 1994-12-27 · superseded
- [[GB 15365-2008]] — 摩托车和轻便摩托车操纵件、指示器及信号装置的图形符号 · 2008-12-31 · superseded
- [[GB 4094-2016]] — 汽车操纵件、指示器及信号装置的标志 · 2016-12-30 · active
- [[GB T 17867-1999]] —  · active
- [[GB T 17867-2023]] — 汽车手操纵件、指示器及信号装置的位置 · 2023-11-27 · active
- [[GB T 21055-2007]] — 肢体残疾人驾驶汽车的操纵辅助装置 · 2007-08-13 · active
- [[GB T 4094.2-2005]] —  · superseded
- [[GB T 4094.2-2017]] — 电动汽车 操纵件、指示器及信号装置的标志 · 2017-09-29 · active
- [[GB T 43382-2023]] — 道路车辆手控装置常规运动方向 · 2023-11-27 · active
- [[GB T 43402-2023]] — 乘用车 驾驶员手控制区域 · 2023-11-27 · active
- [[GB T 4782-2001]] — 道路车辆 操纵件、指示器及信号装置 词汇 · 2001-07-03 · active

### ece (26)

- [[ECE R121]] — 关于手控装置、信号装置和指示器位置及识别的车辆认证的统一规定 · 2006-01-18 · active
- [[ECE R121 Rev1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2011-10-04 · active
- [[ECE R121 Rev1 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2011-12-12 · active
- [[ECE R121 Rev1 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2012-08-15 · active
- [[ECE R121 Rev1 Am3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2013-01-07 · active
- [[ECE R121 Rev1 Am3 Corr1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2014-12-20 · active
- [[ECE R121 Rev1 Am4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2013-08-06 · active
- [[ECE R121 Rev1 Am5]] — Uniform provisions concerning the approval of vehicles with regard to  · 2015-06-22 · active
- [[ECE R121 Rev1 Am6]] — Uniform provisions concerning the approval of vehicles with regard to  · 2017-07-26 · active
- [[ECE R121 Rev1 Am7]] — Uniform provisions concerning the approval of vehicles with regard to  · 2018-11-02 · active
- [[ECE R121 Rev2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2015-11-12 · active
- [[ECE R121 Rev2 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2017-07-26 · active
- [[ECE R121 Rev2 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2018-08-10 · active
- [[ECE R121 Rev2 Am3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2018-11-02 · active
- [[ECE R121 Rev2 Am4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-11-02 · active
- [[ECE R121 Rev2 Am5]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-11-15 · active
- [[ECE R35]] — 关于车辆脚制动控制器装配位置认证的统一规定 · 1999-05 · active
- [[ECE R35 Rev1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH REGARD TO  · 1993-10-12 · active
- [[ECE R35 Rev1 Am1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH REGARD TO  · 2006-10-10 · active
- [[ECE R35 Rev1 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-07-02 · active
- [[ECE R60]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF TWO-WHEELED MOTOR CYCLES · 1984-07-18 · active
- [[ECE R60 Am1]] —  · active
- [[ECE R60 Am2]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF TWO-WHEELED MOTOR CYCLES · 2004-10-01 · active
- [[ECE R60 Am3]] — Uniform provisions concerning the approval of two-wheeled motor cycles · 2006-11-14 · active
- [[ECE R60 Rev1]] — Uniform provisions concerning the approval of two-wheeled motor cycles · 1995-06-16 · active
- [[ECE R60 Rev1 Am1]] — Uniform provisions concerning the approval of two-wheeled motor cycles · 2017-02-22 · active

## 相关主题

- [[lighting_signaling - 照明与信号装置]]
- [[motorcycle - 摩托车 / L 类]]
- [[identification - 车辆识别 / 标记]]
- [[brakes - 制动系统]]
- [[restraints_airbags - 安全带与乘员约束]]
