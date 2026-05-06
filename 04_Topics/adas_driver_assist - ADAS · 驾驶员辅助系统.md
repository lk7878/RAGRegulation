---
type: topic
topic_key: adas_driver_assist
label: ADAS / 驾驶员辅助系统
note_count: 20
regions:
  ece: 19
  cn: 1
types:
  type/amendment: 13
  type/version: 7
statuses:
  active: 20
generated_by: stage4_auto
tags:
- type/topic
- topic/adas_driver_assist
---

# ADAS / 驾驶员辅助系统（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

ADAS / 驾驶员辅助系统主题（20 notes，几乎全部 ECE，1 条 GB 39732）汇总 **UN WP.29 近 10 年针对驾驶员辅助和自动化系统的标准化成果**。与 `brakes`（R152 AEBS）、`steering_suspension`（R79 ACSF）、`electronics_emc`（R155 网安 / R156 OTA）形成完整 ADAS 法规生态。

**① 主动预警类（警示驾驶员）**
- `ECE R130`（LDWS）：车道偏离警示 — 商用车（M2/M3, N2/N3）强制
- `ECE R151`（BSIS）：盲点信息系统 — 对行人 / 自行车检测，N 类商用车强制
- `ECE R159`（MOIS）：起步辅助 / 移动起步信息系统 — 启动瞬间检测前方障碍物

**② 主动干预类（控制车辆）**
- `ECE R157`（ALKS）：自动车道保持系统 — **唯一 L3 自动驾驶国际法规**，Rev.1+ Am4 已演进多次
  - 基础版本：低速 (≤60 km/h)，高速公路场景，相当于 L3 限定条件
  - Am3 Rev.1+：扩展车速到 130 km/h，增加变道功能
- `ECE R158`：倒车运动探测（对撞前警示 + 可选制动干预）

**③ 事件记录类**
- `ECE R160`（EDR）：事件数据记录仪 — 2022+ 欧洲新车强制，仿 NHTSA FMVSS 405 / SAE J2728
  - Rev.1 更新：扩展 event 记录阈值 / 时间轴

**④ 国内 GB 对应**
- `GB 39732-2020`：汽车事件数据记录系统（EDR） — 对应 `ECE R160`
- `GB/T 39263-2020`：道路车辆 先进驾驶辅助系统（ADAS）术语及定义
- `GB/T 39901-2021`：乘用车自动紧急制动系统（AEB）性能要求及试验方法

**⑤ 演进里程碑**
- **2014**：R130 LDWS 生效（欧洲商用车强制）
- **2018**：R151 BSIS 通过
- **2020**：R157 ALKS 原版批准（首个 L3 国际法规）
- **2021**：R160 EDR + R159 MOIS 通过
- **2022+**：R157 加速修订，扩展应用范围

**⑥ 与其它主题耦合**
- `brakes` → `ECE R152` M1/N1 AEBS（紧急制动执行层）
- `steering_suspension` → `ECE R79` ACSF（主动方向盘干预）
- `electronics_emc` → `ECE R155`（ADAS 系统网络安全）、`ECE R156`（OTA 升级）
- `crash_impact` → `ECE R137` 前碰（碰撞避免后作为 fallback）

**跨区域速查**：
- `GB 39732-2020` ≈ `ECE R160`（EDR）
- `GB/T 39901` ≈ `ECE R152`（AEB 性能，虽分属不同主题）
- **R157 ALKS 国内暂无直接对应**，工信部有"L3 驾驶自动化系统准入试点管理办法"

## 覆盖范围

- 共 **20** 条 notes
- 按区域：ece=19, cn=1
- 按类型：type/amendment=13, type/version=7
- 按状态：active=20

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 39732-2020 |
| ece | ECE R130, ECE R130 Am1, ECE R151, ECE R151 Am1, ECE R151 Am2, ECE R151 Am3, ECE R157, ECE R157 Am1, ECE R157 Am2, ECE R157 Am3, ECE R157 Am4, ECE R159, ECE R159 Am1, ECE R159 Am2, ECE R160, ECE R160 Am1, ECE R160 Am2, ECE R160 Rev1, ECE R160 Rev1 Am1 |

## 时间线（最近 30 条）

- **2023-06-16** — [[ECE R159 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2023-03-20** — [[ECE R160 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2023-03-03** — [[ECE R157 Am4]] · Uniform provisions concerning the approval of vehicles with 
- **2023-02-03** — [[ECE R160 Rev1]] · Uniform provisions concerning the approval of motor vehicles
- **2022-11-24** — [[ECE R160 Rev1 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2022-11-24** — [[ECE R160 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2022-09-29** — [[ECE R157 Am3]] · Uniform provisions concerning the approval of vehicles with 
- **2022-09-23** — [[ECE R159 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2022-08-30** — [[ECE R151 Am3]] · Uniform provisions concerning the approval of motor vehicles
- **2022-03-21** — [[ECE R157 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2022-01-13** — [[ECE R157 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2021-10-21** — [[ECE R160]] · Uniform provisions concerning the approval of motor vehicles
- **2021-07-06** — [[ECE R159]] · Uniform provisions concerning the approval of motor vehicles
- **2021-07-02** — [[ECE R151 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2021-03-04** — [[ECE R157]] · Uniform provisions concerning the approval of vehicles with 
- **2020-12-24** — [[GB 39732-2020]] · 汽车事件数据记录系统
- **2020-11-05** — [[ECE R151 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2020-01-13** — [[ECE R151]] · Uniform provisions concerning the approval of motor vehicles
- **2016-10-28** — [[ECE R130 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2013-08-07** — [[ECE R130]] · Uniform provisions concerning the approval of motor vehicles

## 完整索引

### cn (1)

- [[GB 39732-2020]] — 汽车事件数据记录系统 · 2020-12-24 · active

### ece (19)

- [[ECE R130]] — Uniform provisions concerning the approval of motor vehicles with rega · 2013-08-07 · active
- [[ECE R130 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2016-10-28 · active
- [[ECE R151]] — Uniform provisions concerning the approval of motor vehicles with rega · 2020-01-13 · active
- [[ECE R151 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2020-11-05 · active
- [[ECE R151 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2021-07-02 · active
- [[ECE R151 Am3]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-08-30 · active
- [[ECE R157]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-03-04 · active
- [[ECE R157 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-01-13 · active
- [[ECE R157 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-03-21 · active
- [[ECE R157 Am3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-09-29 · active
- [[ECE R157 Am4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2023-03-03 · active
- [[ECE R159]] — Uniform provisions concerning the approval of motor vehicles with rega · 2021-07-06 · active
- [[ECE R159 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-09-23 · active
- [[ECE R159 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-06-16 · active
- [[ECE R160]] — Uniform provisions concerning the approval of motor vehicles with rega · 2021-10-21 · active
- [[ECE R160 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-03-20 · active
- [[ECE R160 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-11-24 · active
- [[ECE R160 Rev1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-02-03 · active
- [[ECE R160 Rev1 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-11-24 · active

## 相关主题

- [[identification - 车辆识别 / 标记]]
- [[crash_impact - 碰撞与被动安全]]
- [[type_approval_general - 总体型式认证 / 通用要求]]
- [[dimensions_weights - 尺寸 / 质量 / 类别]]
