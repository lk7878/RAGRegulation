---
reg_id: ECE R101 Rev3 Am10
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of passenger cars powered by an
  internal combustion engine only, or powered by a hybrid electric power train with
  regard to the measurement of the emission of carbon dioxide and fuel consumption
  and/or the measurement of electric energy consumption and electric range, and of
  categories M1 and N1 vehicles powered by an electric power train only with regard
  to the measurement of electric energy consumption and electric range
status: active
version: Revision 3 - Amendment 10
supplement: Supplement 11 to the 01 series of amendments
entry_into_force: 2022-06-22
authentic_text_ref: ECE/TRANS/WP.29/2021/134
date: 2022-09-29
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\101\R101r3am10e.pdf
publication_date: 2022-09-29
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A和B中均未明确提及standard_body字段。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B中未提及新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B中未提及在用车型实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B中未提及替代关系。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A中未提取具体技术要求的数值限值。
_ocr_upgraded: mineru
_mineru_content_hash: 70719ed8da453409
_mineru_outputs_dir: outputs/70719ed8da453409
_mineru_blocks:
  tables: 3
  formulas: 16
  images: 2
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 101 - Revision 3 - Amendment 10

**Supplement 11 to the 01 series of amendments – Date of entry into force: 22 June 2022**

## 摘要
本修正案（UN R101 Rev.3 Amend.10）主要修订了关于纯电动车辆和可外接充电式混合动力车辆（OVC-HEV）的电能消耗和纯电续驶里程的测量方法。核心修订内容涉及定义、测试程序、生产一致性检查以及相关附录的更新。

## 主要修订内容

### 1. 定义修订 (Paragraph 2.18.)
*   **"Electric range"**：修订为仅适用于纯电动车辆或可外接充电式混合动力车辆（OVC-HEV），指根据本法规附件7和附件9所述程序测量的，一次充满电的电池（或其他电能存储装置）可驱动的距离。

### 2. 测试要求修订 (Paragraph 5.3.)
*   **5.3.1.**：明确技术服务机构负责按照附件7所述方法和测试循环进行电能消耗和续驶里程的测量。
*   **5.3.2.**：规定通过本方法测量的纯电续驶里程De是唯一可包含在销售宣传材料中的数值。
*   **5.3.3.**：规定电能消耗结果必须以瓦时每公里（Wh/km）表示，续驶里程以公里（km）表示，两者均四舍五入至最接近的整数。

### 3. 生产一致性检查修订 (Paragraph 9.4.)
*   **9.4.1.5.**：确保对每种车型进行附件7规定的电能消耗测试。应制造商要求，测试可在未行驶任何里程的车辆上进行（不受附件7第5.1.1.6段要求的限制）。作为制造商的替代选择，电能消耗可通过下文第9.4.3段所述程序进行测试确认。
*   **新增 9.4.3.**：为生产一致性检查中的电能消耗验证提供了制造商可选的替代方案。
    *   **9.4.3.1.**：在生产一致性程序中，附件7第5.2.3.1段（连续循环程序）和第5.2.3.2段（缩短测试程序）中规定的Type 1测试程序的终止准则应替换为：**完成附件7第2段规定的前两个NEDC测试循环即达到生产一致性程序的终止准则**。
    *   **9.4.3.2.**：在这前两个NEDC测试循环中，应根据附件7附录3所述方法测量REESS的直流电能，并除以前两个NEDC测试循环的行驶距离。
    *   **9.4.3.3.**：将根据9.4.3.2段确定的值与根据9.4.3.5段确定的值进行比较。
    *   **9.4.3.4.**：应使用第9.3节所述的统计程序检查电能消耗的一致性。为此一致性检查，术语CO2应替换为电能消耗。
    *   **9.4.3.5.**：规定了用于验证生产一致性的电能消耗声明值计算公式：`EC_DC,COP = EC_DC,first two NEDC × AF_EC`，其中AF_EC为调整因子（`AF_EC = C_dec / C`）。

### 4. 附件7修订
*   **标题**：修订为“**纯电动车辆电能消耗和纯电续驶里程测量方法**”。
*   **新增第1、1.1、1.2段**：
    *   **1.**：说明本测试方法用于测量纯电动车辆的电能消耗（Wh/km）和纯电续驶里程（km）。
    *   **1.1.**：根据测试车辆的估计纯电续驶里程选择测试程序（见下表）。
    *   **1.2.**：列出了测量参数、单位、精度和分辨率要求表格。
*   **测试程序选择表**：
    | 如果估计的纯电续驶里程... | 适用的测试程序 |
    | :--- | :--- |
    | ...小于6个NEDC测试循环的长度。 | 按照本附件第5.2.3.1段的连续循环测试程序。 |
    | ...等于或大于6个NEDC测试循环的长度。 | 按照本附件第5.2.3.2段的缩短测试程序。 |
*   **新增第3段：缩短的NEDC测试序列**：描述了由两个动态NEDC段（DS1和DS2）与两个恒速段（CSSM和CSSE）组成的测试序列，用于减少长续驶里程车辆的测试时间。
*   **章节重新编号与修订**：原第1、1.1、1.2、1.3段重新编号为第2、2.1、2.2、2.3段（NEDC测试循环描述）。原第1.4段重新编号为第4段（公差）。原第2章重新编号为第5章（测试方法），并对车辆条件（5.1）、操作模式（5.2）、测试程序应用（5.2.3）、电池充电（5.2.4）以及纯电续驶里程和电能消耗的确定（5.2.5）进行了详细修订和重述。
*   **新增附录3：PEV的REESS电流和电压测定**：定义了测量可充电储能系统（REESS）电流和电压的方法及仪器要求，允许使用外部测量或车载数据（需向批准机构证明精度）。

### 5. 附件9修订
*   **标题**：修订为“**混合动力车辆电续驶里程及OVC续驶里程测量方法**”。
*   **第1段**：明确本方法用于测量可外接充电式混合动力车辆（OVC-HEV）的电续驶里程和OVC续驶里程。
*   **第3.1.6段**：修订车辆预处理要求。
*   **第4.1.1.1段**：改为“（保留）”。
*   **第4.1.2段**：明确OVC HEV的电池应按照附件8第3.2.2.5段所述正常夜间充电程序进行充电。
*   **第4.2.1段**：改为“（保留）”。

### 6. 附件7附录1修订
*   **第1段**：增加了制造商可选的替代方案，允许根据UN R83最新版本的附件4a附录7中描述的过程确定道路载荷。

---
**注**：本文档仅为记录工具。具有真实性和法律约束力的文本是：ECE/TRANS/WP.29/2021/134。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 3 个
> - 公式 16 个
> - 图像 2 个
> - 全文 Markdown 33,546 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 3 个）

#### 表 1 (page 2)
<table><tr><td rowspan=1 colspan=1>If the estimated pure electricrange is</td><td rowspan=1 colspan=1>Applicable test procedure</td></tr><tr><td rowspan=1 colspan=1>...less than the length of 6NEDC test cycles.</td><td rowspan=1 colspan=1>Consecutive cycle test procedure in accordance with paragraph5.2.3.1. of this Annex.</td></tr><tr><td rowspan=1 colspan=1>...equal to or greater than thelength of 6 NEDC test cycles.</td><td rowspan=1 colspan=1>Shortened test procedure in accordance with paragraph 5.2.3.2.of this Annex.</td></tr></table>

#### 表 2 (page 3)
<table><tr><td>Parameter</td><td>Units</td><td>Accuracy</td><td>Resolution</td></tr><tr><td>Time</td><td>S</td><td>±0.1 s</td><td>0.1 s</td></tr><tr><td>Distance</td><td>m</td><td>±0.1 per cent</td><td>1m</td></tr><tr><td>Temperature</td><td>℃</td><td>±1℃</td><td>1℃</td></tr><tr><td>Speed</td><td>km/h</td><td>±1 per cent</td><td>0.2 km/h</td></tr><tr><td>Mass</td><td>kg</td><td>±0.5 per cent</td><td>1kg</td></tr><tr><td>Electric Energy (a)</td><td>Wh</td><td>±1 per cent</td><td>0.001 kWh (b)</td></tr><tr><td>Electric current</td><td>A</td><td>±0.3 per cent FSD or ±1 per cent of reading (c.d)</td><td>0.1A</td></tr><tr><td>Electric voltage</td><td>V</td><td>±0.3 per cent FSD or ±1 per cent of reading (c)</td><td>0.1 V</td></tr></table>

#### 表 3 (page 7)
<table><tr><td rowspan=1 colspan=1>Distance driven in constant speed segmentCSSm (km)</td><td rowspan=1 colspan=1>Maximum total break (min)</td></tr><tr><td rowspan=1 colspan=1>Up to 100</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>Up to 150</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Up to 200</td><td rowspan=1 colspan=1>30</td></tr><tr><td rowspan=1 colspan=1>Up to 300</td><td rowspan=1 colspan=1>60</td></tr><tr><td rowspan=1 colspan=1>More than 300</td><td rowspan=1 colspan=1>Shall be based on the manufacturer&#x27;srecommendation</td></tr></table>

### 公式（取前 16 个）

**公式 1** (page 2):

$$
E C _ { D C , C O P } = E C _ { D C , f i r s t \ t w o \ N E D C } \times A F _ { E C }
$$

**公式 2** (page 2):

$$
A F _ { E C } = \frac { C _ { d e c } } { C }
$$

**公式 3** (page 4):

$$
d _ { C S S M } = D _ { e , e s t } - d _ { D S 1 } - d _ { D S 2 } - d _ { C S S E }
$$

**公式 4** (page 8):

$$
E C _ { D C , j } = \frac { \Delta E _ { R E E S S , j } } { d _ { j } }
$$

**公式 5** (page 8):

$$
\Delta E _ { R E E S S , j } = \sum _ { j = 1 } ^ { n } \Delta E _ { R E E S S , j , i }
$$

**公式 6** (page 9):

$$
\Delta E _ { R E E S S , j , i } = \frac { 1 } { 3 6 0 0 } \times \int _ { t _ { 0 } } ^ { t _ { e n d } } U ( t ) _ { R E E S S , j , i } \times I ( t ) _ { R E E S S , j , i } d t
$$

**公式 7** (page 9):

$$
D _ { e } = { \frac { U B E _ { C C P } } { E C _ { D C } } }
$$

**公式 8** (page 9):

$$
U B E _ { C C P } = \sum _ { j = 1 } ^ { k } \Delta E _ { R E E S S , j }
$$

**公式 9** (page 9):

$$
E C _ { D C } = \sum _ { j = 1 } ^ { n } E C _ { D C , j } \times k _ { j }
$$

**公式 10** (page 10):

$$
\begin{array} { r } { k _ { 1 } = \frac { \Delta E _ { R E E S S , 1 } } { U B E _ { C C P } } \qquad , k _ { 2 } = \frac { \Delta E _ { R E E S S , 2 } } { U B E _ { C C P } } } \end{array}
$$

**公式 11** (page 10):

$$
\begin{array} { r } { k _ { 1 } = \frac { \Delta E _ { R E E S S , 1 } } { U B E _ { C C P } } \qquad , k _ { 2 } = \frac { \Delta E _ { R E E S S , 2 } } { U B E _ { C C P } } \mathrm { a n d } k _ { j } = \frac { 1 - k _ { 1 } - k _ { 2 } } { n - 2 } \mathrm { f o r } j = 3 \dots n } \end{array}
$$

**公式 12** (page 10):

$$
D _ { e } = { \frac { U B E _ { S T P } } { E C _ { D C } } }
$$

**公式 13** (page 10):

$$
U B E _ { S T P } = \Delta E _ { R E E S S , D S _ { 1 } } + \Delta E _ { R E E S S , D S _ { 2 } } + \Delta E _ { R E E S S , C S S _ { M } } + \Delta E _ { R E E S S , C S S _ { E } }
$$

**公式 14** (page 10):

$$
E C _ { D C } = \sum _ { j = 1 } ^ { 2 } E C _ { D C , j } \times k _ { j }
$$

**公式 15** (page 11):

$$
\begin{array} { r } { k _ { 1 } = \frac { \Delta E _ { R E E S S , D S _ { 1 } } } { U B E _ { S T P } } \qquad \mathrm { a n d } \qquad k _ { 2 } = 1 - k _ { 1 } } \end{array}
$$

**公式 16** (page 11):

$$
C = \frac { E _ { A C } } { D _ { e } }
$$

### 图像（取前 2 张）

![Figure 1 NEDC test cycle ](../_mineru_assets/ECE R101 Rev3 Am10/1ca5f77979d58a071b59f4f877336f3e10f75dc54d1d89ffc78d5b26f4e1a573.jpg)  
*Figure 1 NEDC test cycle * (page 3)

![Figure 3a Shortened NEDC test sequence ](../_mineru_assets/ECE R101 Rev3 Am10/7196c180cabc32ff2e8630974bdb175198caeece1cc49b7b535dc3c668fbd77f.jpg)  
*Figure 3a Shortened NEDC test sequence * (page 4)

