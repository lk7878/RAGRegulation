---
type: topic
topic_key: crash_impact
label: 碰撞与被动安全
note_count: 86
regions:
  ece: 73
  cn: 13
types:
  type/version: 47
  type/amendment: 39
statuses:
  active: 81
  superseded: 5
generated_by: stage4_auto
tags:
- type/topic
- topic/crash_impact
---

# 碰撞与被动安全（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

碰撞与被动安全主题覆盖 **车身结构 + 防护装置 + 碰撞测试工况** 三大类（98 notes，ECE=82, CN=16），是汽车整车型式认证最严格的实车测试域，和 `restraints_airbags`、`interior_protrusions`、`brakes`（AEBS）紧密关联。

**① 碰撞工况法规（按方向）**
- **正面碰撞**：`ECE R94`（乘用车 M1，40% 偏置），`ECE R137`（全宽碰撞，M1/N1），`GB 11551-2014`（正面碰撞乘员保护）
- **侧面碰撞**：`ECE R95`（MDB 移动壁障），`GB 20071-2006`（侧碰乘员保护）
- **后碰撞**：`ECE R32/R42`（后下部防护 / 保险杠），`GB 20072-2024`（M1 后碰安全要求含 EV 高压）
- **翻车 / 顶盖强度**：`ECE R66`（M2/M3 大客车上部结构），`GB 17578-2013`（客车上部结构强度）
- **行人保护**：`ECE R127`（Pedestrian Safety，Rev1–Rev3 Am1–Am2 持续修订）

**② 车身结构防护**
- 前/后防护装置：`ECE R58`（后下部防护，N2/N3/O3/O4），`GB 11567-2017`（汽车及挂车侧面与后下部）
- 转向柱溃缩：`ECE R12`（转向机构对驾驶员伤害），`GB 11557-2011`（国内对应）
- 侧围刚度 / 门锁保持：`ECE R11`（门锁与铰链，归 `doors_mechanisms` 主题），辅以 R33（正面撞击结构）

**③ 测试工具与参考条件**
- `ECE R32 附录 4`：冲击器（移动壁障 vs 摆锤）参数
- `GB/T 41722-2022`：侧风敏感性风机开环试验（辅助动力学 + 碰撞稳定性）
- Hybrid-III 假人、MDB、AE-MDB、WorldSID 等工装定义散见于各法规附件

**④ 重点演进**
- 2021：R127 Rev3 引入行人保护新测试点（腿部 / 头部区域重新分区）
- 2022–2023：R95 Rev.2 补充 AE-MDB（先进移动壁障），`R94` 与 `R137` 对 FMVSS 208 对齐持续推进
- 2024：`GB 20072-2024` 重写后碰撞要求，明确涵盖 EV 高压切断与热失控；`GB 11557` / `GB 11551` 持续修订中

**跨区域速查**：
- `GB 11551` ≈ `ECE R94` + `ECE R137`（正面偏置 + 全宽）
- `GB 20071` ≈ `ECE R95`（侧面 MDB）
- `GB 20072` 独含 EV 电安全要求，超出当前 `ECE R32/R42` 范围
- `GB 17578` ≈ `ECE R66`（客车翻车）
- `GB 11557` ≈ `ECE R12`（转向柱溃缩）

## 覆盖范围

- 共 **86** 条 notes
- 按区域：ece=73, cn=13
- 按类型：type/version=47, type/amendment=39
- 按状态：active=81, superseded=5

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 11551-2003, GB 11553-1989, GB 11557-2011, GB 11567-2017, GB 11567.2-2001, GB 17354-1998, GB 17354-2024, GB 20071-2006, GB 20071-2025, GB 20072-2024, GB 26134-2010, GB 26134-2024, GB 26512-2021 |
| ece | ECE R12, ECE R12 Rev4, ECE R12 Rev4 Am1, ECE R12 Rev4 Am2, ECE R12 Rev4 Am3, ECE R12 Rev4 Am4, ECE R12 Rev4 Am5, ECE R127, ECE R127 Am1, ECE R127 Corr1, ECE R127 Rev1, ECE R127 Rev1 Am1, ECE R127 Rev2, ECE R127 Rev3 Am1, ECE R127 Rev3 Am2, ECE R127-03 Rev2 Am2, ECE R135, ECE R135 Am1, ECE R135 Am2, ECE R135 Rev1, ECE R135 Rev1 Am1, ECE R135 Rev1 Am2, ECE R135 Rev1 Am3, ECE R135 Rev1 Am4, ECE R137, ECE R137 Am2, ECE R137 Rev1, ECE R137 Rev1 Am1, ECE R137 Rev1 Am2, ECE R137 Rev1 Am3 … (+41) |

## 时间线（最近 30 条）

- **2025-04-25** — [[GB 20071-2025]] · 汽车侧面碰撞的乘员保护
- **2024-12-31** — [[GB 20072-2024]] · 乘用车后碰撞安全要求
- **2024-08-23** — [[GB 26134-2024]] · 乘用车顶部抗压强度
- **2024-08-23** — [[GB 17354-2024]] · 乘用车前后端保护装置
- **2023-06-19** — [[ECE R127 Rev3 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2023-06-19** — [[ECE R127 Rev3 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2023-06-16** — [[ECE R166]] · Uniform Provisions Concerning the Approval of Devices and Mo
- **2023-02-24** — [[ECE R137 Rev2 Am3]] · Uniform provisions concerning the approval of passenger cars
- **2023-02-24** — [[ECE R137 Rev1 Am5]] · Uniform provisions concerning the approval of passenger cars
- **2023-02-23** — [[ECE R135 Rev1 Am4]] · Uniform provisions concerning the approval of vehicles with 
- **2023-02-21** — [[ECE R127-03 Rev2 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2023-02-09** — [[ECE R12 Rev4 Am5]] · Uniform provisions concerning the approval of vehicles with 
- **2022-12-30** — [[ECE R95 Rev3]] · Uniform provisions concerning the approval of vehicles with 
- **2022-12-29** — [[ECE R94 Rev4]] · Uniform provisions concerning the approval of vehicles with 
- **2022-09-29** — [[ECE R158 Am1]] · UN Regulation on uniform provisions concerning the approval 
- **2022-09-22** — [[ECE R137 Rev2 Am2]] · Uniform provisions concerning the approval of passenger cars
- **2022-09-22** — [[ECE R135 Rev1 Am3]] · Uniform provisions concerning the approval of vehicles with 
- **2022-09-16** — [[ECE R94 Rev4 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2021-07-06** — [[ECE R158]] · Uniform provisions concerning the approval of devices for re
- **2021-07-02** — [[ECE R93 Am1]] · Uniform provisions concerning the approval of: I. Front unde
- **2021-07-02** — [[ECE R153 Am1]] · Uniform provisions concerning the approval of vehicles with 
- **2021-07-02** — [[ECE R137 Rev1 Am4]] · Uniform provisions concerning the approval of vehicles in th
- **2021-03-05** — [[ECE R153]] · Approval of vehicles with regard to fuel system integrity an
- **2021-02-20** — [[GB 26512-2021]] · 商用车驾驶室乘员保护
- **2021-02-02** — [[ECE R42 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2021-02-02** — [[ECE R137 Rev1 Am3]] · Uniform provisions concerning the approval of passenger cars
- **2020-07-01** — [[ECE R135 Rev1 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2020-07-01** — [[ECE R135 Am2]] · Uniform provisions concerning the approval of vehicles with 
- **2019-11-18** — [[ECE R73 Rev1 Am2]] · UN Regulation No. 73 (Lateral protection devices) - Revision
- **2019-06-24** — [[ECE R137 Rev1 Am2]] · Uniform provisions concerning the approval of passenger cars

## 完整索引

### cn (13)

- [[GB 11551-2003]] — 汽车正面碰撞的乘员保护 · unknown · superseded
- [[GB 11553-1989]] — 汽车正面碰撞时对燃油泄漏的规定 · 1989-08-10 · active
- [[GB 11557-2011]] — 防止汽车转向机构对驾驶员伤害的规定 · 2011-05-12 · active
- [[GB 11567-2017]] — 汽车及挂车侧面和后下部防护要求 · 2017-09-29 · active
- [[GB 11567.2-2001]] — 汽车和挂车后下部防护要求 · 2001-08-22 · superseded
- [[GB 17354-1998]] — 汽车前、后端保护装置 · 1998-05-06 · superseded
- [[GB 17354-2024]] — 乘用车前后端保护装置 · 2024-08-23 · active
- [[GB 20071-2006]] — 汽车侧面碰撞的乘员保护 · unknown · superseded
- [[GB 20071-2025]] — 汽车侧面碰撞的乘员保护 · 2025-04-25 · active
- [[GB 20072-2024]] — 乘用车后碰撞安全要求 · 2024-12-31 · active
- [[GB 26134-2010]] — 乘用车顶部抗压强度 · 2011-01-14 · superseded
- [[GB 26134-2024]] — 乘用车顶部抗压强度 · 2024-08-23 · active
- [[GB 26512-2021]] — 商用车驾驶室乘员保护 · 2021-02-20 · active

### ece (73)

- [[ECE R12]] — 关于防止在汽车碰撞时转向机构对驾驶员的伤害认证的统一规定 · 2000-08-04 · active
- [[ECE R12 Rev4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2012-10-10 · active
- [[ECE R12 Rev4 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2013-08-06 · active
- [[ECE R12 Rev4 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2014-06-20 · active
- [[ECE R12 Rev4 Am3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2016-07-11 · active
- [[ECE R12 Rev4 Am4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2018-08-10 · active
- [[ECE R12 Rev4 Am5]] — Uniform provisions concerning the approval of vehicles with regard to  · 2023-02-09 · active
- [[ECE R127]] — Uniform provisions concerning the approval of motor vehicles with rega · 2013-01-07 · active
- [[ECE R127 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2015-02-03 · active
- [[ECE R127 Corr1]] — Corrigendum 1 to Regulation No. 127 - Uniform provisions concerning th · 2013-10-16 · active
- [[ECE R127 Rev1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2015-02-04 · active
- [[ECE R127 Rev1 Am1]] — Regulation No. 127 - Uniform provisions concerning the approval of mot · 2016-07-11 · active
- [[ECE R127 Rev2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2018-05-23 · active
- [[ECE R127 Rev3 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-06-19 · active
- [[ECE R127 Rev3 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-06-19 · active
- [[ECE R127-03 Rev2 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-02-21 · active
- [[ECE R135]] — Uniform provisions concerning the approval of vehicles with regard to  · 2015-06-25 · active
- [[ECE R135 Am1]] — Amendment 1 to Regulation No. 135 - Uniform provisions concerning the  · 2016-02-05 · active
- [[ECE R135 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-07-01 · active
- [[ECE R135 Rev1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2016-02-05 · active
- [[ECE R135 Rev1 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2017-01-26 · active
- [[ECE R135 Rev1 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2020-07-01 · active
- [[ECE R135 Rev1 Am3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-09-22 · active
- [[ECE R135 Rev1 Am4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2023-02-23 · active
- [[ECE R137]] — Uniform provisions concerning the approval of passenger cars in the ev · 2016-06-22 · active
- [[ECE R137 Am2]] — Uniform provisions concerning the approval of passenger cars in the ev · 2019-01-16 · active
- [[ECE R137 Rev1]] — Uniform provisions concerning the approval of passenger cars in the ev · 2017-09-13 · active
- [[ECE R137 Rev1 Am1]] — Uniform provisions concerning the approval of passenger cars in the ev · 2018-12-29 · active
- [[ECE R137 Rev1 Am2]] — Uniform provisions concerning the approval of passenger cars in the ev · 2019-06-24 · active
- [[ECE R137 Rev1 Am3]] — Uniform provisions concerning the approval of passenger cars in the ev · 2021-02-02 · active
- [[ECE R137 Rev1 Am4]] — Uniform provisions concerning the approval of vehicles in the event of · 2021-07-02 · active
- [[ECE R137 Rev1 Am5]] — Uniform provisions concerning the approval of passenger cars in the ev · 2023-02-24 · active
- [[ECE R137 Rev2 Am2]] — Uniform provisions concerning the approval of passenger cars in the ev · 2022-09-22 · active
- [[ECE R137 Rev2 Am3]] — Uniform provisions concerning the approval of passenger cars in the ev · 2023-02-24 · active
- [[ECE R137-01 Am1]] — Uniform provisions concerning the approval of passenger cars in the ev · 2017-02-23 · active
- [[ECE R153]] — Approval of vehicles with regard to fuel system integrity and safety o · 2021-03-05 · active
- [[ECE R153 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-07-02 · active
- [[ECE R158]] — Uniform provisions concerning the approval of devices for reversing mo · 2021-07-06 · active
- [[ECE R158 Am1]] — UN Regulation on uniform provisions concerning the approval of devices · 2022-09-29 · active
- [[ECE R166]] — Uniform Provisions Concerning the Approval of Devices and Motor Vehicl · 2023-06-16 · active
- [[ECE R32]] — 关于后面碰撞汽车结构特性认证的统一规定 · 1993-10-12 · active
- [[ECE R32 Rev1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH REGARD TO  · 1993-10-12 · active
- [[ECE R32 Rev1 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2007-08-06 · active
- [[ECE R33]] — 关于正面碰撞车辆结构特性认证的统一规定 · 2000-02-11 · active
- [[ECE R33 Rev1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH REGARD TO  · 1993-10-12 · active
- [[ECE R33 Rev1 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2000-02-11 · active
- [[ECE R33 Rev1 Am2]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH REGARD TO  · 2007-06-11 · active
- [[ECE R42 (EN)]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES WITH REGARD TO  · 1980-03-24 · active
- [[ECE R42]] — 关于汽车前后保护装置（保险杠等）认证的统一规定 · 1985-10-01 · active
- [[ECE R42 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2007-08-08 · active
- [[ECE R42 Am2]] — Uniform provisions concerning the approval of vehicles with regard to  · 2021-02-02 · active
- [[ECE R42 Corr1]] — Uniform provisions concerning the approval of vehicles with regard to  · 1980-06-01 · active
- [[ECE R66]] — 关于大型客车上层结构强度认证的统一规定 · 1997-12-03 · active
- [[ECE R66 Rev1]] — Uniform Technical Prescriptions Concerning the Approval of Large Passe · 2006-02-22 · active
- [[ECE R66 Rev1 Am1]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF LARGE PASSENGER VEHICLES · 2008-11-04 · active
- [[ECE R66 Rev1 Corr1]] — Uniform technical prescriptions concerning the approval of large passe · 2006-03-27 · active
- [[ECE R66 Rev1 Corr2]] — Uniform technical prescriptions concerning the approval of large passe · 2007-04-24 · active
- [[ECE R66 Rev1 Corr3]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF LARGE PASSENGER VEHICLES · 2007-06-13 · active
- [[ECE R66-02 Rev1 Am2]] — Uniform provisions concerning the approval of large passenger vehicles · 2010-10-04 · active
- [[ECE R73]] — 关于货用汽车挂车和半挂车侧面防护装置认证的统一规定 · 1988-01-01 · active
- [[ECE R73 Rev1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2011-09-01 · active
- [[ECE R73 Rev1 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2017-12-07 · active
- [[ECE R73 Rev1 Am2]] — UN Regulation No. 73 (Lateral protection devices) - Revision 1 - Amend · 2019-11-18 · active
- [[ECE R73 Rev1 Corr1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2016-11-01 · active
- [[ECE R93 (EN)]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF FRONT UNDERRUN PROTECTIV · 1994-03-15 · active
- [[ECE R93]] — 前下部防护装置（FUPDs） · 1994-03-15 · active
- [[ECE R93 Am1]] — Uniform provisions concerning the approval of: I. Front underrun prote · 2021-07-02 · active
- [[ECE R93 Corr1]] — PRESCRIPTIONS UNIFORMES RELATIVES À L'HOMOLOGATION: I. DES DISPOSITIFS · 2009-07-17 · active
- [[ECE R94]] — 关于车辆正面碰撞乘员保护认证的统一规定 · 1998-09-18 · active
- [[ECE R94 Rev4]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-12-29 · active
- [[ECE R94 Rev4 Am1]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-09-16 · active
- [[ECE R95]] — 关于车辆侧面碰撞乘员保护认证的统一规定 · 1995-07-20 · active
- [[ECE R95 Rev3]] — Uniform provisions concerning the approval of vehicles with regard to  · 2022-12-30 · active

## 相关主题

- [[restraints_airbags - 安全带与乘员约束]]
- [[commercial_operations - 营运 / 商用车管理]]
- [[bus_coach - 客车 / 公交车]]
- [[special_vehicles - 特种 / 危险车辆]]
- [[motorcycle - 摩托车 / L 类]]
