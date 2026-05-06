---
type: topic
topic_key: bus_coach
label: 客车 / 公交车
note_count: 12
regions:
  ece: 7
  cn: 5
types:
  type/version: 12
statuses:
  active: 10
  superseded: 2
generated_by: stage4_auto
tags:
- type/topic
- topic/bus_coach
---

# 客车 / 公交车（Topic Index）

> 本页由 Stage 4 聚类脚本自动生成。Overview 段可由 Cascade 迭代完善。

## Overview

客车 / 公交车主题（10 notes，ECE=5, CN=5）聚焦 **M2/M3 类客车的专项整车法规**，尤其是大客车结构 / 内饰阻燃 / 双层巴士 / 校车专项。

**① 客车结构与安全**
- `ECE R52`：轻型客车（M2/M3 I 级）结构通用要求 — Rev3 最新
- `ECE R107`：M2/M3 整车（所有等级客车），含车身结构、通道、出口、紧急装备等

**② 客车内饰阻燃**
- `ECE R118`：M3 客车内饰材料阻燃性 — Rev3 最新

**③ 国内客车专项**
- `GB 13094-2017 / 2025`：客车结构安全要求（2025 为最新版，整合多项安全要素）
- `GB 19260-2016`：低地板 / 低入口城市客车结构要求（I 级客车）
- `GB 24407-2009 / 2025`：专用校车安全技术条件（2025 大修订）

**④ 相关跨主题**
- 客车上部结构强度：`GB 17578-2013`（在 `crash_impact`）
- 客车座椅：`GB 13057-2014`（在 `restraints_airbags`）
- 校车座椅：`GB 24406-2024`（在 `restraints_airbags`）

**跨区域速查**：
- `GB 13094` ≈ `ECE R107`（整车结构）
- `GB 19260` 专注低地板城市客车，`ECE R107 附件 11` 部分对应
- `GB 24407` 校车技术条件 ≈ `ECE R107` + 国内校车专项补充
- `GB 38262` 客车内饰阻燃（在 `identification` 主题）≈ `ECE R118`

## 覆盖范围

- 共 **12** 条 notes
- 按区域：ece=7, cn=5
- 按类型：type/version=12
- 按状态：active=10, superseded=2

## 跨区域法规索引

| Region | reg_ids |
| --- | --- |
| cn | GB 13094-2017, GB 13094-2025, GB 19260-2016, GB 24407-2009, GB 24407-2025 |
| ece | ECE R107 Rev8, ECE R118, ECE R118 Rev3, ECE R36, ECE R36 Rev3, ECE R52, ECE R52 Rev3 |

## 时间线（最近 30 条）

- **2025-12-31** — [[GB 24407-2025]] · 专用校车安全技术条件
- **2025-12-31** — [[GB 13094-2025]] · 客车结构安全要求
- **2023-02-14** — [[ECE R107 Rev8]] · Uniform provisions concerning the approval of category M2 or
- **2023-02-06** — [[ECE R118 Rev3]] · Uniform technical prescriptions concerning the burning behav
- **2017-10-14** — [[GB 13094-2017]] · 客车结构安全要求
- **2016-12-30** — [[GB 19260-2016]] · 低地板及低入口城市客车结构要求
- **2009-09-30** — [[GB 24407-2009]] · 专用小学生校车安全技术条件
- **2008-02-20** — [[ECE R36 Rev3]] · Uniform provisions concerning the approval of large passenge
- **2008-02-15** — [[ECE R52 Rev3]] · UNIFORM PROVISIONS CONCERNING THE APPROVAL OF M2 AND M3 SMAL
- **2005-04-06** — [[ECE R118]] · 用于某些类型机动车辆内部结构的材料的燃烧特性的统一技术规定
- **2000-12-29** — [[ECE R52]] · 关于小型公共汽车结构认证的统一规定
- **2000-07-06** — [[ECE R36]] · 关于大型客车一般结构认证的统一规定

## 完整索引

### cn (5)

- [[GB 13094-2017]] — 客车结构安全要求 · 2017-10-14 · active
- [[GB 13094-2025]] — 客车结构安全要求 · 2025-12-31 · active
- [[GB 19260-2016]] — 低地板及低入口城市客车结构要求 · 2016-12-30 · active
- [[GB 24407-2009]] — 专用小学生校车安全技术条件 · 2009-09-30 · superseded
- [[GB 24407-2025]] — 专用校车安全技术条件 · 2025-12-31 · active

### ece (7)

- [[ECE R107 Rev8]] — Uniform provisions concerning the approval of category M2 or M3 vehicl · 2023-02-14 · active
- [[ECE R118]] — 用于某些类型机动车辆内部结构的材料的燃烧特性的统一技术规定 · 2005-04-06 · active
- [[ECE R118 Rev3]] — Uniform technical prescriptions concerning the burning behaviour and/o · 2023-02-06 · active
- [[ECE R36]] — 关于大型客车一般结构认证的统一规定 · 2000-07-06 · active
- [[ECE R36 Rev3]] — Uniform provisions concerning the approval of large passenger vehicles · 2008-02-20 · active
- [[ECE R52]] — 关于小型公共汽车结构认证的统一规定 · 2000-12-29 · active
- [[ECE R52 Rev3]] — UNIFORM PROVISIONS CONCERNING THE APPROVAL OF M2 AND M3 SMALL CAPACITY · 2008-02-15 · superseded

## 相关主题

- [[brakes - 制动系统]]
- [[restraints_airbags - 安全带与乘员约束]]
- [[lubricants_fluids - 润滑油 / 工作液]]
