---
reg_id: ECE R83 Rev5 Am11
region: ece
type: type/amendment
title: Addendum 82 – UN Regulation No. 83, Revision 5 - Amendment 11
standard_body: UNECE
publication_date: '2021-02-02'
entry_into_force_date: '2021-01-03'
source: E/ECE/324/Rev.1/Add.82/Rev.5/Amend.11, E/ECE/TRANS/505/Rev.1/Add.82/Rev.5/Amend.11
authentic_text: ECE/TRANS/WP.29/2020/63
parent_regulation: '[[UN Regulation No. 83 (R083)]]'
parent_revision: Revision 5
amends_to: Supplement 11 to the 07 series of amendments
status: active
topics:
- vehicle emissions
- pollutant emission approval
- engine fuel requirements
- mono-fuel gas vehicles
- exhaust after-treatment reagent
- road load determination
- OBD system
- malfunction indicator
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\83\R083r5am11e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B中未提及新生产车辆的实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B中未提及在用车辆的实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B中未提及被替代的法规。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A中未提取具体限值，B中亦未提供具体排放限值数字。
_ocr_upgraded: mineru
_mineru_content_hash: dc3229322dba1870
_mineru_outputs_dir: outputs/dc3229322dba1870
_mineru_blocks:
  tables: 0
  formulas: 9
  images: 0
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 83, Revision 5 - Amendment 11

## 概述
本文件是《关于采用轮式车辆、其装备和部件的统一技术法规以及基于这些联合国法规批准相互认可条件的协定》下，联合国第83号法规（关于根据发动机燃料要求批准车辆污染物排放的统一规定）第5次修订版第11号增补件。本修正案自2021年1月3日起生效。具有法律效力的权威文本是：ECE/TRANS/WP.29/2020/63。

## 主要修订内容

### 1. 关于单燃料气体车辆的定义 (第5.3节)
- **5.3.1.2.1.2. (I型试验)**: 尽管有第5.3.1.2.1.1条的要求，单燃料气体车辆在进行I型试验时应被视为只能使用气体燃料运行的车辆。
- **5.3.2.1.2. (II型试验)**: 尽管有第5.3.2.1.1条的要求，单燃料气体车辆在进行II型试验时应被视为只能使用气体燃料运行的车辆。
- **5.3.3.1.2. (III型试验)**: 尽管有第5.3.3.1.1条的要求，单燃料气体车辆在进行III型试验时应被视为只能使用气体燃料运行的车辆。

### 2. 新增关于使用试剂的车辆的要求 (第5.3.9条)
- 新增第5.3.9条：使用试剂进行排气后处理的车辆应满足本法规附录6中描述的要求。

### 3. 附录6修订
- **第1条 (引言)**: 修订为明确本附录规定了依赖使用试剂进行后处理系统以降低排放的车辆的要求。本附录中所有对“试剂箱”的引用也应理解为适用于储存试剂的其他容器。

### 4. 附件1修订
- **第3条脚注8**: 修订为：“(8) 单燃料气体车辆在进行试验时应被视为只能使用气体燃料运行的车辆。”
- **第3.2.12.2.5.5条**: 修订为要求提供燃油箱示意图，并注明标称容量和材料。

### 5. 附件4a修订 (道路负荷确定)
- **第5.1条 (试验程序)**: 修订道路负荷测量程序。
    - 车辆道路负荷的测量程序在本附件附录7a中描述。
    - 如果车辆道路负荷已根据UN GTR No. 15中定义的WLTP程序确定，则可选择使用附录7b中描述的方法。
    - 如果底盘测功机负荷将根据车辆的基准质量设定，则不需要这些程序。
- **附录结构调整**:
    - 将原附录7重命名为附录7a。
    - 新增附录7b：**车辆总道路负荷功率测定的替代程序**。
 - **目的**: 提供当车辆道路负荷已根据UN GTR No. 15中定义的WLTP程序确定时，制造商可选择使用的道路负荷功率计算方法。
 - **方法**:
 1.  **WLTP道路负荷计算**: 根据UN GTR No. 15附件4，或如果车辆是插值家族的一部分，则根据其附件7第3.2.3.2.2点“单车道路负荷计算”进行，考虑单车的输入参数（试验质量、适用轮胎能量等级的RRC值、车辆空气阻力）。
 2.  **适用(NEDC)道路负荷计算**:
 - **不同轮胎压力规定的影响**: 考虑NEDC基准质量下所选轮胎允许的最小和最大轮胎压力的平均值。
 - **轮胎花纹深度的影响**: 根据公式计算。
 - **旋转部件不同考虑的影响**: WLTP考虑旋转质量效应（MRO之和的3%加25公斤），NEDC忽略此效应。
 - **NEDC道路负荷系数确定**: 详细公式用于计算F0、F1、F2系数，考虑不同惯性、轮胎压力、旋转部件惯性和轮胎花纹深度的影响。

### 6. 附件7修订
- **第4.7.2条 (密封室)**: 修订关于密封室内风扇/鼓风机的要求，容量为0.1至0.5 m³/sec，用于彻底混合室内空气。应能在测量期间达到均匀的温度和碳氢化合物浓度。室内的车辆不应受到风扇或鼓风机的直接气流影响。

### 7. 附件11修订 (OBD)
- **第2.14条 (“永久排放默认模式”)**: 修订定义，指发动机管理控制器永久切换到不需要来自故障部件或系统输入的模式，而此类故障会导致车辆排放水平超过本附件第3.3.2条规定的限值。
    - **第2.14.1条**: 定义“永久”在此上下文中意味着默认模式不可恢复，即导致排放默认模式的诊断或控制策略不能在下一个驾驶循环中运行，并且无法确认导致排放默认模式的条件不再存在。所有其他排放默认模式被视为非永久。
- **新增第2.21条 (“跛行回家程序”)**: 指除排放默认模式之外的任何默认模式。
- **第3.1.1条 (OBD系统访问)**: 修订为要求车辆检查、诊断、维修或保养所需的OBD系统访问应不受限制且标准化。所有与排放相关的故障码应符合本附件附录1第6.5.3.5条的规定。
- **第3.5.1条 (故障指示器-MI)**: 修订MI的要求。
    - MI应易于被车辆操作者察觉。
    - MI不得用于除向驾驶员指示紧急启动、排放默认模式或影响排放系统的跛行回家程序之外的任何其他目的。
    - MI在所有合理的照明条件下应可见。
    - 激活时，应显示符合ISO 2575的符号。
    - 车辆不得配备多于一个用于排放相关问题的通用MI。允许使用单独的专用指示器（如制动系统、系安全带、油压等）。
    - 禁止使用红色作为MI的颜色。
- **第3.8.1条 (故障码擦除)**: 修订条件，规定如果在至少40个发动机暖机循环或40个满足以下(a)至(c)标准的车辆运行驾驶循环中未重新记录相同故障，OBD系统可以擦除故障码以及行驶距离和冻结帧信息：
    - (a) 自发动机启动起的累计时间大于或等于600秒；
    - (b) 车速大于或等于40 km/h的累计车辆运行时间大于或等于300秒；
    - (c) 怠速连续运行（即驾驶员松开加速踏板且车速小于或等于1.6 km/h）时间大于或等于30秒。
- **第7.3.2条 (监测器分母递增条件)**: 修订并增加了特定监测器的分母递增条件，包括：
    - (a) 二次空气系统
    - (b) 仅在冷启动期间激活的系统
    - (c) 可变气门正时系统
    - (d) 柴油氧化催化器、柴油颗粒过滤器（需额外满足800公里累计行驶里程）
    - (e) 特定温度传感器（要求驾驶循环以冷启动开始）
    - (f) 增压压力控制系统（需满足特定激活时间）
    - (g) 允许制造商为特定组件或系统申请使用特殊的分母条件，但需向型式批准机构提交数据和/或工程评估以证明其必要性。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 0 个
> - 公式 9 个
> - 图像 0 个
> - 全文 Markdown 13,138 字符（见 `outputs/<hash>/full.md`）

### 公式（取前 9 个）

**公式 1** (page 2):

$$
P _ { a v g } = \left( \frac { P _ { m a x } + P _ { m i n } } { 2 } \right)
$$

**公式 2** (page 2):

$$
T P = { \left( \frac { P _ { a v g } } { P _ { m i n } } \right) } ^ { - 0 . 4 }
$$

**公式 3** (page 2):

$$
\begin{array} { r } { T T D = \left( 2 \cdot \frac { 0 . 1 \cdot R M _ { n } \cdot 9 . 8 1 } { 1 0 0 0 } \right) } \end{array}
$$

**公式 4** (page 3):

$$
F _ { 0 n } ^ { 1 } = F _ { 0 w } \cdot \bigg ( \frac { R M _ { n } } { T M _ { w } } \bigg )
$$

**公式 5** (page 3):

$$
F _ { 0 n } ^ { 2 } = F _ { 0 n } ^ { 1 } \cdot T P
$$

**公式 6** (page 3):

$$
F _ { 0 n } ^ { 3 } = F _ { 0 n } ^ { 2 } \cdot \left( { \frac { 1 } { 1 . 0 3 } } \right)
$$

**公式 7** (page 3):

$$
F _ { 0 n } = F _ { 0 n } ^ { 3 } \cdot T T D
$$

**公式 8** (page 3):

$$
F _ { 1 n } = F _ { 1 w } \cdot \left( { \frac { 1 } { 1 . 0 3 } } \right)
$$

**公式 9** (page 3):

$$
F _ { 2 n } = F _ { 2 w } \cdot \left( { \frac { 1 } { 1 . 0 3 } } \right)
$$

