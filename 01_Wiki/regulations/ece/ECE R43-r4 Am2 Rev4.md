---
reg_id: ECE R43-r4 Am2
type: type/amendment
region: ece
title: Uniform provisions concerning the approval of safety glazing materials and
  their installation on vehicles
status: active
standard_body: UNECE
publication_date: 2018-08-10
implementation_date_new_vehicle: 2018-07-19
source_file: R043r4am2e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\43\R043r4am2e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及针对在用车辆的单独实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及取代的法规版本。
_ocr_upgraded: mineru
_mineru_content_hash: 1def8a5f1445e618
_mineru_outputs_dir: outputs/1def8a5f1445e618
_mineru_blocks:
  tables: 2
  formulas: 6
  images: 8
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 43 - Revision 4 - Amendment 2

**Supplement 6 to the 01 series of amendments**
**Date of entry into force: 19 July 2018**

## 概览
本文件是《关于采用轮式车辆、可安装和/或用于轮式车辆的设备及部件的统一技术法规以及基于这些联合国法规批准相互承认条件的协定》的增补文件。具体为第43号联合国法规（安全玻璃材料及其在车辆上的安装）的第4修订版第2修正案。

## 主要修订内容

### 附件 3 - 测试方法修订

#### 3.2.1. 设备（假人头）
*   允许使用无线数据传输（如无线电传输）替代电缆传输。
*   规定额外安装在假人头内的电子组件不得影响其质量、重心和弹簧力，且仅能安装在底板（24）上。
*   如有必要，质量校正也仅限于在假人头内腔朝向的底板表面进行。
*   如需用于控制电子模块的微型组件（如微动开关、供电充电插座），可替换同轴电缆，但必须使用盖板（29）和保护帽（30）上的原始孔进行安装和布线。
*   更新了图2.1中10公斤假人头的零件清单（位置1至30），包含标准代号、材料和备注。

#### 3.2.2. 调整与校准
*   如果使用无线数据传输，在没有任何电缆阻碍自由垂直下落风险的情况下，可以省略导向系统。
*   假人头不得受到下落装置或测量电缆（如适用）的额外冲量，应仅受重力加速并垂直下落。

#### 3.2.2.1. 测量设备
*   明确用于记录和评估从假人头加速度计通过有线或无线传输的加速度曲线 a_x(t), a_y(t), a_z(t) 的设备要求，需符合ISO 6487标准，通道振幅等级CAC 5,000 m/s²，通道频率等级CFC 1,000 Hz。

#### 3.2.2.2. & 3.2.2.3. 假人头校准设备与程序
*   规定了冲击板的尺寸（600mm x 600mm）、厚度（至少50mm）和表面要求（粗糙度R_a < 0.5 μm，平面度公差t = 0.05 mm）。
*   冲击板应清洁干燥，测试时需无固定地放置在混凝土基座上，或置于与混凝土基础相连的坚固支撑装置中。
*   提供了不同下落高度（50, 100, 150, 254 mm）下，z轴最大减速度a_z（以重力加速度g的倍数表示）的允许范围表。
*   规定减速度曲线应基于单峰振动。254 mm下落高度的减速度曲线应在100 g以上运行至少1.5 ms，最多2 ms。

#### 新增 3.2.3.1. 和 3.2.3.2. - 测试件支撑
*   **3.2.3.1.** 对于平面测试件，支撑装置如3.1.3.所述，但修改为橡胶垫片宽度应为50 mm +1/-0 mm（原为15 mm ± 1 mm），完全覆盖两个钢架的边缘。M20螺栓的最小推荐扭矩为30 Nm。或者，可使用其他压制技术，如液压或气压压制。
*   **3.2.3.2.** 对于完整玻璃件，支撑应由与玻璃形状相对应的刚性部件组成，使假人头重量作用于内表面。玻璃应通过适当装置夹紧到支撑结构上，中间夹有硬度70 IRHD、厚度约3 mm的橡胶条，整个周边的接触宽度约为15 mm。

#### 3.2.5. 测试程序
*   测试件应按3.2.3.1.（平面件）或3.2.3.2.（完整玻璃件）夹紧。螺栓扭矩或液压/气压压力应确保测试期间测试件的移动不超过2 mm。
*   假人头应撞击在测试件或玻璃上代表塑料玻璃安装在车辆上时内表面的那一侧，且撞击点在其几何中心40 mm范围内。
*   对于垂直冲击，加速度分量a_x和a_y应小于0.1 a_z。

#### 3.2.6. 评估
*   更新了合成加速度a_res(t)和头部伤害准则（HIC）的计算公式（1）和（2）。
*   HIC值用于衡量钝性颅脑损伤风险，需选择积分限t1和t2使函数f(t)取最大值。

### 第4章 - 磨耗测试修订

#### 4.1. Taber测试设备
*   **4.1.1. 磨耗仪**：详细描述了水平转台、配重平行臂、磨轮距离（对称面之间65.1 mm ± 1.0 mm）、磨轮轴线与转台轴线的水平偏移（19.05 mm ± 0.30 mm）以及真空吸尘系统（吸嘴孔径11 mm，高度可调）的要求。增加了图4.1和4.2。
*   **4.1.2. 磨轮**：规定了磨轮的圆柱形状、由弹性粘合剂和磨粒（氧化铝、碳化硅，粒径20-102 μm）组成。尺寸：宽度12.7 mm ± 0.3 mm，外径小于52.5 mm且不小于44.4 mm，轮毂轴向孔径16.0 mm ± 0.1 mm。
*   **新增 4.1.2.1. 至 4.1.2.3. - 磨轮资格认定与标准化**
    *   **4.1.2.1. 玻璃测试**：规定用于玻璃测试的磨轮，对3块浮法玻璃样品进行1000次循环磨耗后，光散射值（最终雾度减初始雾度）应在0.7% ± 0.5% 范围内。
    *   **4.1.2.2. 塑料材料测试**：规定用于塑料测试的磨轮，对3块AS4000S硬涂层聚碳酸酯参考样品进行磨耗后，光散射值必须在特定资格范围内（100次循环：0% 至 2.6%；500次循环：0.5% 至 6.3%；1000次循环：1.0% 至 7.4%）。只有满足此要求，才能使用该磨轮对进行测试。使用该磨轮对测试样品时，需使用基于参考样品测试结果计算的校正因子对测量值进行校正。
    *   **4.1.2.3. 磨轮标准化**：详细规定了使用Taber ST-11重修石（或等效品）重修磨轮的程序（25次循环）、重修前后的清洁方法、新磨轮的磨合程序（100次循环）、重修石的使用寿命（约7500次循环后更换）以及重修后到测试的最长允许时间（2分钟）。
*   **4.1.3. 雾度计**：修订了雾度计的构成描述。
*   **新增 4.1.3.1. 和 4.1.3.2.**：规定了光源（色温2856 K ± 50 K）、探测器（符合1931 CIE标准色度观察者响应）、积分球（端口总面积不超过球内反射面积的4.0%）、光路几何条件等详细要求。
*   **4.1.4. 和 4.1.5.**：更新了照明光束要求（最大发散角0.05 rad/3°）、用于将光束对准磨痕并限制其在测试件上直径为7 mm ± 1 mm的光阑、积分球内表面特性、光阱以及测试件夹具的要求。替换了图5.1。
*   **4.2. 测试条件**：明确为温度23 °C ± 2 °C，气压860至1060 mbar，相对湿度50% ± 5%。
*   **4.4.1. 至 4.4.3. - 清洁、调节和初始雾度测量**：修订了清洁程序（推荐使用异丙醇IPA，或兼容的清洁剂）、调节条件（23 °C ± 2 °C，50% ± 5% RH，至少48小时）以及初始雾度测量的计算方法和读数要求（至少4个等距点）。
*   **新增 4.4.4. 至 4.4.6. - 磨耗、磨耗后清洁和最终雾度测量**
    *   **4.4.4. 磨耗**：规定每个样品进行3次测试。测试件以45°角安装在转台上（见图5.2）。详细描述了磨轮负载（500g/轮）、真空吸嘴高度设置（距表面1mm）、真空吸力（残压≤13.7 kPa）和循环数设置的程序。
    *   **4.4.5. 磨耗后清洁**：描述了使用软毛防静电刷或去离子水清洁测试件表面以及清洁真空吸嘴的程序。
    *   **4.4.6. 最终雾度测量**：规定在磨痕上至少测量4个（如不均匀最多16个）等距点的最终雾度，并取平均值。
*   **4.5. 结果表示**
*   **新增 4.5.1. 至 4.5.2.2.**
    *   **4.5.1. 通则**：结果表示为Δ雾度（平均最终雾度减平均初始雾度）。
    *   **4.5.2. 校正计算（仅适用于塑料材料测试）**：测量得到的Δ雾度值需使用基于同一磨轮对测试AS4000S参考样品确定的校正因子进行校正。
 *   **4.5.2.1.** 给出了校正后的Δ雾度计算公式：∆haze_c(r) = ∆haze_m(r) × X_c(r)。
 *   **4.5.2.2.** 规定了校正因子X_c(r)的计算方法：X_c(r) = ∆haze_rv(r) / ∆haze_av(r)。其中，∆haze_rv(r)是AS4000S参考样品在特定循环数r下的固定参考Δ雾度值（100次: 1.1%；500次: 2.8%；1000次: 3.7%），∆haze_av(r)是使用该磨轮对实际测试3块参考样品得到的平均Δ雾度值。校正因子应在磨轮对寿命初期（直径约52mm）和中期（直径约48mm）各测定一次。

### 附件 21
*   修订了图2a（左侧驾驶车辆示例），展示了如第2.4.2.2.段定义的上部遮蔽区域“B”，并提供了相对于车辆纵向中间平面C_L对称（详图X）和不对称（详图Y）的示例。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 3 个
> - 公式 6 个
> - 图像 8 个
> - 全文 Markdown 38,209 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 3 个）

#### 表 1 (page 1)
**List of pieces for the $\mathbf { 1 0 k g }$ headform of Figure 2.1 **

<table><tr><td colspan="1" rowspan="1">PositionNo.</td><td colspan="1" rowspan="1">Numberofpieces</td><td colspan="1" rowspan="1">Standard notation</td><td colspan="1" rowspan="1">Material</td><td colspan="1" rowspan="1">Remarks</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Magnetic holding device</td><td colspan="1" rowspan="1">Steel EN10025-2-E295GC</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Vibration damper</td><td colspan="1" rowspan="1">Rubber／Steel</td><td colspan="1" rowspan="1">Diameter:  50 mmThickness: 30 mmThread:     M10</td></tr><tr><td colspan="1" rowspan="1">3(a)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">HF connector BNC</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Coupler-coupler (EN122120)</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Hexagonal nut ISO10511-M10-05</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">Disc ISO7090-6-200HV</td><td colspan="1" rowspan="1">=</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">6@</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Transition piece</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">Cylinder screw ISO4762-M6x140-8.8</td><td colspan="1" rowspan="1">=</td><td colspan="1" rowspan="1">Torque about 12 Nm</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Hexagonal nut ISO10511-M8-05</td><td colspan="1" rowspan="1">=</td><td colspan="1" rowspan="1">Torque about 4 Nm (ref.paragraph 3.2.2.3.)</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Disc</td><td colspan="1" rowspan="1">Steel EN10025-2-E295GC</td><td colspan="1" rowspan="1">Hole Diameter:8 mmOuter Diameter: 35 mmThickness:   1.5 mm</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Rubber ring</td><td colspan="1" rowspan="1">Rubber,hardness 60 IRHD</td><td colspan="1" rowspan="1">Hole Diameter:8mmOuter Diameter: 30mmThickness:    10 mm</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Damping ring</td><td colspan="1" rowspan="1">Gasket paper</td><td colspan="1" rowspan="1">Hole Diameter:120 mmOuter Diameter: 199 mmThickness:    0.5 mm</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Intermediate ring</td><td colspan="1" rowspan="1">Butadiene-rubber,hardnessabout 60 IRHD</td><td colspan="1" rowspan="1">Hole Diameter: 129 mmOuter Diameter: 192 mmThickness: about 6 mm(ref. paragraph 3.2.2.3.)</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Guide tube</td><td colspan="1" rowspan="1">Polytetrafluoroethylene(PTFE)</td><td colspan="1" rowspan="1">Inner Diameter:  8 mmOuter Diameter: 10 mmLength:          40 mm</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Hexagonal nut ISO10511-M8-05</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Threaded bolt DIN 976-1-M8x90-B-8.8</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Screwed insert</td><td colspan="1" rowspan="1">Cast alloyEN1982-CuZn39Pb1Al-C-GP</td><td colspan="1" rowspan="1">Dimensions M8x12(DIN 7965)</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Basin</td><td colspan="1" rowspan="1">Polyamide 12 (ISO 1874-1)</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Cover</td><td colspan="1" rowspan="1">Butadiene-rubber</td><td colspan="1" rowspan="1">Thickness:   6mmRib on one side</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Guide bush</td><td colspan="1" rowspan="1">Steel EN10025-2-E295GC</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">Counter sunk screwISO2009-M5x10-5.8</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Damping disc</td><td colspan="1" rowspan="1">Gasket paper</td><td colspan="1" rowspan="1">Diameter:  65mmThickness: 0.5mm</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Base plate</td><td colspan="1" rowspan="1">Steel EN10025-2-E295GC</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Set screw with hexagonal socket</td><td colspan="1" rowspan="1">Class of strength 45H (ISO898-5)</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Tri-axial mounting block</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">Acceleration gauge</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">ref. paragraph 3.2.2.1.</td></tr><tr><td colspan="1" rowspan="1">28</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Wood component</td><td colspan="1" rowspan="1">Hornbeam, glued in layers</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">29</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Cover plate</td><td colspan="1" rowspan="1">Alloy EN573-3 ; EN AW-5019 (EN AW-AIMg5)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">Protective cap</td><td colspan="1" rowspan="1">Polyamide 12 (ISO 1874-1)</td><td colspan="1" rowspan="1"></td></tr></table>

#### 表 2 (page 2)
#### 表 3 (page 3)
<table><tr><td>Drop height mm</td><td>Greatest deceleration az as a multiple of acceleration due to gravity g</td></tr><tr><td>50</td><td>82±8</td></tr><tr><td>100</td><td>128±8</td></tr><tr><td>150</td><td>167 ± 10</td></tr><tr><td>254</td><td>227± 14</td></tr></table>

### 公式（取前 6 个）

**公式 1** (page 4):

$$
\mathrm { a _ { r e s } } \left( \mathrm { t } \right) { = } \left( \mathrm { a _ { x } ^ { 2 } } \left( \mathrm { t } \right) { + } \mathrm { a _ { y } ^ { 2 } } \left( \mathrm { t } \right) { + } \mathrm { a _ { z } ^ { 2 } } \left( \mathrm { t } \right) \right) ^ { 1 / 2 }
$$

**公式 2** (page 4):

$$
\begin{array} { r } { H I C = \operatorname* { m a x } { f ( t ) } = \operatorname* { m a x } _ { t _ { 1 } , t _ { 2 } } \Bigg [ { \left( { t _ { 2 } } - t _ { 1 } \right) } ^ { - 1 . 5 \left( \displaystyle \int _ { { t _ { 1 } } } ^ { t _ { 2 } } { a _ { r e s } \left( t \right) } d t \right) ^ { 2 . 5 } \Bigg ] } } \end{array}
$$

**公式 3** (page 11):

$$
\mathrm { { T } _ { { d } } = \frac { \mathrm { { T } _ { 4 } - \mathrm { { T } _ { 3 } \mathrm { { ( T _ { 2 } / T _ { 1 } ) } } } } } { \mathrm { { T } _ { 1 } - T _ { 3 } } } }
$$

**公式 4** (page 11):

$$
{ \mathrm { H a z e , o r l i g h t s c a t t e r e d , } } = { \begin{array} { l } { { \mathrm { ~ \frac { T _ { \mathrm { d } } ~ } { T _ { \mathrm { t } } } ~ } } \times 1 0 0 \ { \% } } \end{array} }
$$

**公式 5** (page 13):

$$
\Delta \mathrm { h a z e } _ { \mathrm { c } } ( \mathrm { r } ) = \Delta \mathrm { h a z e } _ { \mathrm { m } } ( \mathrm { r } ) \times \mathrm { X } _ { \mathrm { c } } ( \mathrm { r } )
$$

**公式 6** (page 13):

$$
\mathrm { X } _ { \mathrm { c } } ( \mathrm { r } ) = \Delta \mathrm { h a z e } _ { \mathrm { r v } } ( \mathrm { r } ) / \Delta \mathrm { h a z e } _ { \mathrm { a v } } ( \mathrm { r } )
$$

### 图像（取前 8 张）

![Figure 4.1 Diagram of abrading instrument ](../_mineru_assets/ECE R43-r4 Am2/366e0c8debd74a5cc1d73c807c6f072cd0ef5f206ca7f86eece0170d8fd08062.jpg)  
*Figure 4.1 Diagram of abrading instrument * (page 5)

![图 page 6](../_mineru_assets/ECE R43-r4 Am2/f451930909400acec18cdaf2821a2355a1508f5d7af20a2ad73da2a0d2b763db.jpg)  

![Figure 5.1 Hazemeter  / Dotted lines show position of reflectance standard for total transmittance measurement. ](../_mineru_assets/ECE R43-r4 Am2/911df056daa0096b18b2240def88eb16aaeb7bec8bdcd54a287fdaff34301e85.jpg)  
*Figure 5.1 Hazemeter  / Dotted lines show position of reflectance standard for total transmittance measurement. * (page 9)

![图 page 12](../_mineru_assets/ECE R43-r4 Am2/2761f6fb577504bfaaf7afdc52dd591674282f32af1e7178cfcbb546ba38fea3.jpg)  

![图 page 14](../_mineru_assets/ECE R43-r4 Am2/4ad77c0f6d8eb9e38e3c0f04d9cd80f223fe1b6bf301e59955fa4e3c867a9b83.jpg)  

![图 page 14](../_mineru_assets/ECE R43-r4 Am2/02bb27c58a622e5c3554ab1fad62e261fb6525da238a94f582d97ddb4c2d6b57.jpg)  

![图 page 15](../_mineru_assets/ECE R43-r4 Am2/ad6e13c62ff959631f3104636d042b0afdb09359b3c7db2bf2593a997c03b513.jpg)  

![图 page 15](../_mineru_assets/ECE R43-r4 Am2/05a2e919a1753881c4b559478cccaea985c1fca434ef80b92012745dc1138187.jpg)  

