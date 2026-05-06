---
type: topic
topic_key: brakes
label: 制动系统
note_count: 83
regions:
  ece: 63
  cn: 20
types:
  type/amendment: 48
  type/version: 34
  type/regulation: 1
statuses:
  active: 76
  superseded: 6
  under_revision: 1
generated_by: stage4_auto
tags:
- type/topic
- topic/brakes
---

# 制动系统（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

制动系统是汽车安全的核心主动防护域（84 notes）。本主题以 **`ECE R13/R13-H`** 为整车级双核，配合多个功能专项法规，国内以 **`GB 12676`（商用车）+ `GB 21670`（乘用车）** 双线对应。

**① 整车制动基线**
- `ECE R13`：M2、M3、N、O 类商用车及挂车 → 行车制动 + 应急制动 + 驻车制动三重 + EBS/ABS + Trailer 联动
- `ECE R13-H`：M1、N1 类乘用车专用（简化版）
- 国内：`GB 12676-2014`（商用车）、`GB 21670-2008 / 2025`（乘用车，2025 重写）、`GB 38900-2020`（商用车挂车 EBS）
- L 类摩托：`ECE R78`

**② 更换件 / 辅助制动**
- 更换制动衬片/鼓/盘：`ECE R90`（本主题最活跃 ECE 标准，近 4 年 Am4–Am10 连续修订）
- 再生制动性能：混入 R13 新附件 + R131（AEBS 前碰预警自动紧急制动）
- 防抱死诊断：`GB/T 13594-2025`（商用车辆和挂车防抱 ABS）

**③ 新兴主动制动法规**
- `ECE R131`：AEBS（高级紧急制动，M2/M3/N2/N3）
- `ECE R139`：BAS（制动辅助）
- `ECE R140`：ESC（车身稳定）
- `ECE R152`：AEBS M1/N1（乘用车自动紧急制动，2022 后快速修订）
- 对应国内：`GB 40164-2021`（车辆纵向控制 & AEB）、`GB 20073-2018`（ABS 专项）、`GB/T 38796`（ESC）

**④ 重点里程碑**
- 2014：ECE R13 Rev.8 发布，接入 EBS + ESC + 再生制动规范
- 2021–2023：R13 Rev.8 Am10/11 + Rev.9 Am1/2，同步 WP.29 数字化转型
- 2022–2023：R152 / R131 多轮修订（Am3–Am6），AEBS 测试工况扩展至复杂场景
- 2025：`GB/T 13594-2025`、`GB 21670-2025` 国内大修订，对标 ECE R13 最新技术内容

**跨区域速查**：
- `GB 12676` ≈ `ECE R13`（商用车整车制动）
- `GB 21670` ≈ `ECE R13-H`（乘用车整车制动）
- `GB/T 38796` ≈ `ECE R140`（ESC）
- `GB 40164 / AEB 部分` ≈ `ECE R131 + R152`（AEBS）

## 覆盖范围

- 共 **83** 条 notes
- 按区域：ece=63, cn=20
- 按类型：type/amendment=48, type/version=34, type/regulation=1
- 按状态：active=76, superseded=6, under_revision=1

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 12676-1999, GB 12676-2014, GB 13594-2003, GB 16897-1997, GB 16897-2010, GB 17352-1998, GB 17352-2010, GB 17355-1998, GB 20073-2018, GB 21670-2008, GB 21670-2025, GB 24407-2012, GB 38900-2020, GB 40164-2021, GB/T 13594-2025, GB/T 17346-1998, GB/T 17346-2023, GB/T 36881-2018, 汽车典型结构图册_人民交通出版社汽车图书出版中心编, 汽车构造_李晶华主编 |
| ece | ECE R13, ECE R13 Rev4, ECE R13 Rev4 Am2, ECE R13 Rev8, ECE R13 Rev8 Am1, ECE R13 Rev8 Am10, ECE R13 Rev8 Am11, ECE R13 Rev8 Am2, ECE R13 Rev8 Am3, ECE R13 Rev8 Am4, ECE R13 Rev8 Am5, ECE R13 Rev8 Am6, ECE R13 Rev8 Am7, ECE R13 Rev9 Am1, ECE R13 Rev9 Am2, ECE R13-12r8am9e Rev8 Am9, ECE R131, ECE R131 Am1, ECE R131 Rev1, ECE R131 Rev1 Am1, ECE R131 Rev1 Am2, ECE R139, ECE R139 Am1, ECE R139 Am2, ECE R13H, ECE R13H Rev4 Am1, ECE R13H Rev4 Am4, ECE R140, ECE R140 Am1, ECE R140 Am2 … (+33) |

## 时间线（最近 30 条）

- **2025-05-30** — [[GB 21670-2025]] · 乘用车制动系统技术要求及试验方法
- **2025-04-25** — [[GB T 13594-2025]] · 商用车辆和挂车防抱制动系统性能要求及试验方法
- **2023-06-20** — [[ECE R90 Rev3 Am10]] · Uniform provisions concerning the approval of replacement br
- **2023-06-15** — [[ECE R152 Rev2]] · Uniform provisions concerning the approval of motor vehicles
- **2023-06-15** — [[ECE R13 Rev9 Am2]] · Uniform provisions concerning the approval of vehicles of ca
- **2023-06-15** — [[ECE R13 Rev8 Am11]] · Uniform provisions concerning the approval of vehicles of ca
- **2023-03-17** — [[GB T 17346-2023]] · 汽车脚踏板位置尺寸测量方法
- **2023-02-21** — [[ECE R131 Rev1 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2023-02-17** — [[ECE R90 Rev3 Am9]] · Uniform provisions concerning the approval of replacement br
- **2023-02-09** — [[ECE R13H Rev4 Am4]] · Uniform provisions concerning the approval of passenger cars
- **2023-02-09** — [[ECE R13 Rev9 Am1]] · Uniform provisions concerning the approval of vehicles of ca
- **2023-02-09** — [[ECE R13 Rev8 Am10]] · Uniform provisions concerning the approval of vehicles of ca
- **2022-11-29** — [[ECE R78 Rev3]] · Uniform provisions concerning the approval of vehicles of ca
- **2022-11-25** — [[ECE R152 Rev2 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2022-11-24** — [[ECE R152 Rev1 Am5]] · Uniform provisions concerning the approval of motor vehicles
- **2022-11-23** — [[ECE R90 Rev3 Am8]] · Uniform provisions concerning the approval of replacement br
- **2022-11-23** — [[ECE R152 Am6]] · Uniform provisions concerning the approval of motor vehicles
- **2022-11-17** — [[ECE R78 Rev3 Am1]] · Uniform provisions concerning the approval of vehicles of ca
- **2022-11-10** — [[ECE R13-12r8am9e Rev8 Am9]] · Uniform provisions concerning the approval of vehicles of ca
- **2022-09-29** — [[ECE R152 Rev2 Am1]] · Uniform provisions concerning the approval of motor vehicles
- **2022-09-23** — [[ECE R152 Rev1 Am4]] · Uniform provisions concerning the approval of motor vehicles
- **2022-09-23** — [[ECE R152 Am5]] · Uniform provisions concerning the approval of motor vehicles
- **2022-08-30** — [[ECE R90 Rev3 Am7]] · Uniform provisions concerning the approval of replacement br
- **2022-02-21** — [[R013Hr4e4a3 Rev4 Am3]] · UN Regulation No. 13H - Uniform provisions concerning the ap
- **2021-12-21** — [[ECE R152 Rev1 Am3]] · Uniform provisions concerning the approval of motor vehicles
- **2021-12-21** — [[ECE R152 Rev1 Am2]] · Uniform provisions concerning the approval of motor vehicles
- **2021-12-21** — [[ECE R152 Am4]] · UN Regulation No. 152 - Amendment 4 - Advanced Emergency Bra
- **2021-11-25** — [[ECE R13 Rev4 Am2]] · Uniform provisions concerning the approval of passenger cars
- **2021-07-02** — [[ECE R13 Rev8 Am7]] · Uniform provisions concerning the approval of vehicles of ca
- **2021-04-30** — [[GB 40164-2021]] · 汽车和挂车 制动器用零部件技术要求及试验方法

## 完整索引

### cn (20)

- [[GB 12676-1999]] — 汽车制动系统 结构、性能和试验方法 · unknown · superseded
- [[GB 12676-2014]] — 商用车辆和挂车制动系统技术要求及试验方法 · 2014-10-10 · active
- [[GB 13594-2003]] — 汽车防抱制动系统性能要求和试验方法 · 2003-11-27 · active
- [[GB 16897-1997]] — 制动软管 · 1997-06-30 · active
- [[GB 16897-2010]] — 制动软管的结构、性能要求及试验方法 · superseded
- [[GB 17352-1998]] — 摩托车和轻便摩托车后视镜及其安装要求 · 1998-05-06 · superseded
- [[GB 17352-2010]] — 摩托车和轻便摩托车后视镜的性能和安装要求 · 2011-01-10 · superseded
- [[GB 17355-1998]] — 摩托车和轻便摩托车制动性能指标限值 · 1998-05-06 · active
- [[GB 20073-2018]] — 摩托车和轻便摩托车 制动性能要求及试验方法 · 2018-02-06 · active
- [[GB 21670-2008]] — 乘用车制动系统技术要求及试验方法 · 2008-04-25 · superseded
- [[GB 21670-2025]] — 乘用车制动系统技术要求及试验方法 · 2025-05-30 · active
- [[GB 24407-2012]] — 专用校车安全技术条件 · 2012-04-10 · active
- [[GB 38900-2020]] — 机动车安全技术检验项目和方法 · 2020-05-26 · active
- [[GB 40164-2021]] — 汽车和挂车 制动器用零部件技术要求及试验方法 · 2021-04-30 · active
- [[GB T 13594-2025]] — 商用车辆和挂车防抱制动系统性能要求及试验方法 · 2025-04-25 · active
- [[GB T 17346-1998]] — 轿车脚踏板的侧向间距 · 1998-05-06 · superseded
- [[GB T 17346-2023]] — 汽车脚踏板位置尺寸测量方法 · 2023-03-17 · active
- [[GB T 36881-2018]] — 多用途面包车安全技术条件 · 2018-10-10 · active
- [[汽车典型结构图册_人民交通出版社汽车图书出版中心编]] — 汽车典型结构图册 · 2008-01-01 · active
- [[汽车构造_李晶华主编]] — 汽车构造 · 2006-03-01 · active

### ece (63)

- [[ECE R13]] — 有关 M、N 和 O 类车辆制动认证的统一规定 · 2001-08-01 · active
- [[ECE R13 Rev4]] — Uniform provisions concerning the approval of passenger cars with rega · 2018-06-05 · active
- [[ECE R13 Rev4 Am2]] — Uniform provisions concerning the approval of passenger cars with rega · 2021-11-25 · active
- [[ECE R13 Rev8]] — Uniform provisions concerning the approval of vehicles of categories M · 2014-03-03 · active
- [[ECE R13 Rev8 Am1]] — Uniform provisions concerning the approval of vehicles of categories M · 2014-10-17 · active
- [[ECE R13 Rev8 Am10]] — Uniform provisions concerning the approval of vehicles of categories M · 2023-02-09 · active
- [[ECE R13 Rev8 Am11]] — Uniform provisions concerning the approval of vehicles of categories M · 2023-06-15 · active
- [[ECE R13 Rev8 Am2]] — Uniform provisions concerning the approval of vehicles of categories M · 2015-06-22 · active
- [[ECE R13 Rev8 Am3]] — Uniform provisions concerning the approval of vehicles of categories M · 2015-11-09 · active
- [[ECE R13 Rev8 Am4]] — Uniform provisions concerning the approval of vehicles of categories M · 2017-02-22 · active
- [[ECE R13 Rev8 Am5]] — Uniform provisions concerning the approval of vehicles of categories M · 2018-11-02 · active
- [[ECE R13 Rev8 Am6]] — Uniform provisions concerning the approval of vehicles of categories M · 2019-01-16 · active
- [[ECE R13 Rev8 Am7]] — Uniform provisions concerning the approval of vehicles of categories M · 2021-07-02 · active
- [[ECE R13 Rev9 Am1]] — Uniform provisions concerning the approval of vehicles of categories M · 2023-02-09 · active
- [[ECE R13 Rev9 Am2]] — Uniform provisions concerning the approval of vehicles of categories M · 2023-06-15 · active
- [[ECE R13-12r8am9e Rev8 Am9]] — Uniform provisions concerning the approval of vehicles of categories M · 2022-11-10 · active
- [[ECE R131]] — Uniform provisions concerning the approval of motor vehicles with rega · 2013-08-07 · active
- [[ECE R131 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2014-02-10 · active
- [[ECE R131 Rev1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2014-02-27 · active
- [[ECE R131 Rev1 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2016-10-28 · under_revision
- [[ECE R131 Rev1 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-02-21 · active
- [[ECE R139]] — Uniform provisions concerning the approval of passenger cars with rega · 2017-01-30 · active
- [[ECE R139 Am1]] — Uniform provisions concerning the approval of passenger cars with rega · 2019-01-16 · active
- [[ECE R139 Am2]] — Uniform provisions concerning the approval of passenger cars with rega · 2020-01-29 · active
- [[ECE R13H]] — 关于乘用车制动认证的统一规定 · 1998-06-19 · active
- [[ECE R13H Rev4 Am1]] — Uniform provisions concerning the approval of passenger cars with rega · 2019-01-16 · active
- [[ECE R13H Rev4 Am4]] — Uniform provisions concerning the approval of passenger cars with rega · 2023-02-09 · active
- [[ECE R140]] — Uniform provisions concerning the approval of passenger cars with rega · 2017-01-31 · active
- [[ECE R140 Am1]] — Uniform provisions concerning the approval of passenger cars with rega · 2018-11-02 · active
- [[ECE R140 Am2]] — Uniform provisions concerning the approval of passenger cars with rega · 2019-01-16 · active
- [[ECE R140 Am3]] — Uniform provisions concerning the approval of passenger cars with rega · 2020-01-29 · active
- [[ECE R140 Am4]] — Uniform provisions concerning the approval of passenger cars with rega · 2021-02-02 · active
- [[ECE R152]] — Uniform provisions concerning the approval of motor vehicles with rega · 2020-01-22 · active
- [[ECE R152 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2020-11-04 · active
- [[ECE R152 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2020-11-04 · active
- [[ECE R152 Am3]] — Uniform provisions concerning the approval of motor vehicles with rega · 2021-02-02 · active
- [[ECE R152 Am4]] — UN Regulation No. 152 - Amendment 4 - Advanced Emergency Braking Syste · 2021-12-21 · active
- [[ECE R152 Am5]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-09-23 · active
- [[ECE R152 Am6]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-11-23 · active
- [[ECE R152 Rev1 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2021-12-21 · active
- [[ECE R152 Rev1 Am3]] — Uniform provisions concerning the approval of motor vehicles with rega · 2021-12-21 · active
- [[ECE R152 Rev1 Am4]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-09-23 · active
- [[ECE R152 Rev1 Am5]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-11-24 · active
- [[ECE R152 Rev2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2023-06-15 · active
- [[ECE R152 Rev2 Am1]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-09-29 · active
- [[ECE R152 Rev2 Am2]] — Uniform provisions concerning the approval of motor vehicles with rega · 2022-11-25 · active
- [[ECE R78 Rev3]] — Uniform provisions concerning the approval of vehicles of categories L · 2022-11-29 · active
- [[ECE R78 Rev3 Am1]] — Uniform provisions concerning the approval of vehicles of categories L · 2022-11-17 · active
- [[ECE R90]] — 关于动力驱动车及挂车可替代的制动衬片及鼓式制动衬片认证的统一规定 · 2001-08-01 · active
- [[ECE R90 Rev3]] — Uniform provisions concerning the approval of replacement brake lining · 2012-02-17 · active
- [[ECE R90 Rev3 Am1]] — Addendum 89: Regulation No. 90, Revision 3 – Amendment 1 · 2012-12-06 · active
- [[ECE R90 Rev3 Am1 Corr1]] — Uniform provisions concerning the approval of replacement brake lining · 2013-03-26 · active
- [[ECE R90 Rev3 Am10]] — Uniform provisions concerning the approval of replacement brake lining · 2023-06-20 · active
- [[ECE R90 Rev3 Am2]] — Uniform provisions concerning the approval of replacement brake lining · 2015-02-03 · active
- [[ECE R90 Rev3 Am3]] — Uniform provisions concerning the approval of replacement brake lining · 2017-02-22 · active
- [[ECE R90 Rev3 Am4]] — Uniform provisions concerning the approval of replacement brake lining · 2018-11-02 · active
- [[ECE R90 Rev3 Am5]] — Uniform provisions concerning the approval of replacement brake lining · 2020-01-20 · active
- [[ECE R90 Rev3 Am6]] — Uniform provisions concerning the approval of replacement brake lining · 2020-11-02 · active
- [[ECE R90 Rev3 Am7]] — Uniform provisions concerning the approval of replacement brake lining · 2022-08-30 · active
- [[ECE R90 Rev3 Am8]] — Uniform provisions concerning the approval of replacement brake lining · 2022-11-23 · active
- [[ECE R90 Rev3 Am9]] — Uniform provisions concerning the approval of replacement brake lining · 2023-02-17 · active
- [[ECE R90 Rev3 Corr1]] — Corrigendum 1 to Revision 3 of Regulation No. 90 - Uniform provisions  · 2013-02-13 · active
- [[R013Hr4e4a3 Rev4 Am3]] — UN Regulation No. 13H - Uniform provisions concerning the approval of  · 2022-02-21 · active

## 相关主题

- [[dimensions_weights - 尺寸 / 质量 / 类别]]
- [[motorcycle - 摩托车 / L 类]]
- [[bus_coach - 客车 / 公交车]]
- [[test_methods - 试验方法 / 测量规程]]
- [[crash_impact - 碰撞与被动安全]]
