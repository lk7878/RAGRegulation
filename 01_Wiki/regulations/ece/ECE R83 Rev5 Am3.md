---
reg_id: ECE R83 Rev5 Am3
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of vehicles with regard to the emission
  of pollutants according to engine fuel requirements
source: https://unece.org/transport/documents/2021/03/standards/un-regulation-no-83-revision-5-amendment-3
status: active
publication_date: 2017-02-22
implementation_date_new_vehicle: 2017-02-09
authority: UNECE
part_of: UN Regulation No. 83
version: Revision 5 - Amendment 3 (Supplement 3 to the 07 series of amendments)
reference: ECE/TRANS/WP.29/2016/43
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\83\R083r5am3e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及 standard_body 字段。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及针对在用车的实施日期。
- field: equivalent_to.ref
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效法规。
- field: equivalent_to.version
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效法规版本。
- field: equivalent_to.relation
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未提及本修正案替代了哪个文件。
_ocr_upgraded: mineru
_mineru_content_hash: ad58ad2303c62843
_mineru_outputs_dir: outputs/ad58ad2303c62843
_mineru_blocks:
  tables: 2
  formulas: 10
  images: 0
_mineru_merged_at: '2026-04-23'
---

# R083r5am3e - Amendment to UN Regulation No. 83 (Revision 5)

## 概述
本文件是《关于轮式车辆、其装备和部件采用统一技术规定以及基于这些规定授予批准的相互认可条件的协定》的增补文件。具体是对**UN Regulation No. 83**（关于根据发动机燃料要求就污染物排放方面对车辆进行批准的统一规定）的第5次修订版（Rev.5）的第3次修正案（Amend.3），同时也是07系列修正案的第3号补编（Supplement 3）。本修正案于**2017年2月9日**生效。

**权威及具有法律约束力的文本**是：ECE/TRANS/WP.29/2016/43。

## 主要修订内容
本修正案主要修订了法规附件4a的附录7中关于道路负荷测定的具体程序和要求。

### 修订章节：附录 7
修订范围涵盖段落 5.1.1.1. 至 5.1.1.2.7.，并涉及后续段落的重编号和调整。

#### 5.1.1.1. 测试设备与误差
*   时间测量误差应低于 ±0.1 秒。
*   速度测量误差应低于 ±2%。
*   测试期间，应以至少 1 Hz 的频率测量和记录经过的时间及车速。

#### 5.1.1.2. 测试程序
详细规定了滑行测试方法，用于确定车辆在特定参考速度下的道路负荷。关键步骤包括：
1.  **加速与滑行**：将车辆加速至比选定测试速度 `v` 高 10 km/h 的速度，然后挂空挡滑行。
2.  **测量区间**：对于每个参考速度点 `v_j`，测量车辆从速度 `v_2 = v_j + Δv` km/h 减速到 `v_1 = v_j - Δv` km/h 所需的时间 `ΔT_aj`，其中 `Δv = 5 km/h`。
3.  **反向测试**：在相反方向进行相同测试，得到 `ΔT_bj`。
4.  **统计精度要求**：需在每个参考速度 `v_j` 进行至少三对连续的、方向相反的测量，并满足定义的统计精度 `p_j ≤ 3%`。统计精度的计算考虑了测量次数 `n`、平均滑行时间 `ΔT_j` 和标准偏差 `s_j`，并使用了基于 `n` 的系数 `t`（由提供的表格给出）。
5.  **数据剔除**：如果在一个方向的测量中发生任何影响道路负荷测试的外部因素或驾驶员操作，则该次测量及其在相反方向的对应测量均应被剔除。
6.  **总阻力计算**：根据公式分别计算方向 `a` 和 `b` 在参考速度 `v_j` 下的总阻力 `F_aj` 和 `F_bj`。公式中使用了参考质量 `M`、速度增量 `Δv` 以及对应方向的平均滑行时间 `ΔT_aj` 和 `ΔT_bj`。
7.  **平均总阻力与功率计算**：计算平均总阻力 `F_j = (F_aj + F_bj) / 2`。然后计算每个参考速度 `v_j` 下的功率 `P_j = (F_j * v_j) / 1000`（单位：kW）。
8.  **功率曲线拟合**：完整的功率曲线 `P`（kW）作为速度（km/h）的函数，应使用最小二乘回归分析进行计算。

#### 对其他段落的影响
*   原段落 5.1.1.2.8. 被重新编号为 **5.1.1.2.11.**。
*   段落 5.1.2.2.5. 至 5.1.2.2.7. 被修订，以引用更新后的计算方法和结果（特别是新编号的 5.1.1.2.11. 中的系数 `K`），用于将道路测试结果转换到底盘测功机上。
*   段落 5.2.1.2.7. 被修订，规定在道路上测得的平均扭矩 `C_T` 应使用段落 5.1.1.2.11. 中指定的系数 `K` 修正到参考环境条件。

### 参考速度点
测试中使用的参考速度 `v_j`（km/h）为：20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120。

### 统计系数表
用于计算统计精度的系数 `t` 与测量对数 `n` 的关系如下表所示：
| n  | t    | t/√n | n  | t    | t/√n |
|----|------|------|----|------|------|
| 3  | 4.3  | 2.48 | 10 | 2.2  | 0.73 |
| 4  | 3.2  | 1.60 | 11 | 2.2  | 0.66 |
| 5  | 2.8  | 1.25 | 12 | 2.2  | 0.64 |
| 6  | 2.6  | 1.06 | 13 | 2.2  | 0.61 |
| 7  | 2.5  | 0.94 | 14 | 2.2  | 0.59 |
| 8  | 2.4  | 0.85 | 15 | 2.2  | 0.57 |
| 9  | 2.3  | 0.77 |    |      |      |

---
**文档标识**：GE.17-01977(E)
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 2 个
> - 公式 10 个
> - 图像 0 个
> - 全文 Markdown 10,314 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 2 个）

#### 表 1 (page 1)
<table><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>110</td><td rowspan=1 colspan=1>120</td></tr></table>

#### 表 2 (page 2)
**Coefficient t as function of n **

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>vVn</td><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>n</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4.3</td><td rowspan=1 colspan=1>2.48</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>0.73</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3.2</td><td rowspan=1 colspan=1>1.60</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>0.66</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>2.8</td><td rowspan=1 colspan=1>1.25</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>0.64</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>2.6</td><td rowspan=1 colspan=1>1.06</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>0.61</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>0.94</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>0.59</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1>0.85</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>0.57</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>0.77</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

### 公式（取前 10 个）

**公式 1** (page 1):

$$
\begin{array} { r } { \mathrm { p _ { j } } = \frac { \mathrm { t } \cdot \mathrm { s _ { j } } } { \sqrt { \mathrm { n } } } \cdot \frac { 1 0 0 } { \Delta \mathrm { T _ { j } } } \leq 3 \mathrm { p e r c e n t } } \end{array}
$$

**公式 2** (page 1):

$$
\begin{array} { r } { \Delta \mathrm { T } _ { \mathrm { j } } = \frac { 1 } { \mathrm { n } } \sum _ { \mathrm { i } = 1 } ^ { \mathrm { n } } \Delta \mathrm { T } _ { \mathrm { j i } } } \end{array}
$$

**公式 3** (page 1):

$$
\begin{array} { r } { \Delta \mathrm { T } _ { \mathrm { j i } } = \frac { 2 } { \left( \frac { 1 } { \Delta \mathrm { T } _ { \mathrm { a j i } } } \right) + \left( \frac { 1 } { \Delta \mathrm { T } _ { \mathrm { b j i } } } \right) } } \end{array}
$$

**公式 4** (page 2):

$$
\mathrm { s _ { j } = \sqrt { \frac { 1 } { n - 1 } \sum _ { i = 1 } ^ { n } ( \Delta T _ { j i } - \Delta T _ { j } ) ^ { 2 } } }
$$

**公式 5** (page 2):

$$
\mathrm { F _ { a j } } = \frac { 1 } { 3 . 6 } \cdot \mathrm { M } \cdot \frac { 2 \cdot \Delta \mathrm { v } } { \Delta \mathrm { T _ { a j } } }
$$

**公式 6** (page 2):

$$
\mathrm { F } _ { \mathrm { b j } } = \frac { 1 } { 3 . 6 } \cdot \mathrm { M } \cdot \frac { 2 \cdot \Delta \mathrm { v } } { \Delta \mathrm { T } _ { \mathrm { b j } } }
$$

**公式 7** (page 2):

$$
\begin{array} { r l } & { \Delta \mathrm { T } _ { \mathrm { a j } } = \frac { 1 } { \mathrm { n } } \mathrm { \sum _ { i = 1 } ^ { n } } \Delta \mathrm { T } _ { \mathrm { a j i } } } \\ & { \mathrm { a n d ~ } \Delta \mathrm { T } _ { \mathrm { b j } } = \frac { 1 } { \mathrm { n } } \mathrm { \sum _ { i = 1 } ^ { n } } \Delta \mathrm { T } _ { \mathrm { b j i } } } \end{array}
$$

**公式 8** (page 2):

$$
\mathrm { F _ { j } } = { \frac { ( F _ { \mathrm { a j } } + F _ { b j } ) } { 2 } }
$$

**公式 9** (page 2):

$$
\mathrm { P _ { j } } = ( \mathrm { F _ { j } } \cdot \mathrm { v _ { j } } ) / 1 \mathrm { , 0 0 0 }
$$

**公式 10** (page 3):

$$
\mathbf { T } _ { \mathrm { c o r e c t e d } } = \frac { \mathbf { T } _ { \mathrm { m e a s u r e d } } } { \mathbf { K } } \cdot \frac { \mathbf { I } } { \mathbf { M } }
$$

