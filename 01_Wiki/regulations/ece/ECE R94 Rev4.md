---
reg_id: ECE R94 Rev4
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to the protection
  of the occupants in the event of a frontal collision
type: type/version
status: active
standard_body: UNECE
publication_date: 2022-12-29
version: Revision 4
source_file: R094r4e.pdf
tags:
- type/version
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\94\R094r4e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
cross_check_flags:
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: 原文B（提供的片段）未提及新车型的实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 原文B（提供的片段）未提及在用车型的实施日期。
- field: equivalent_to.ref
  status: unsure
  extracted: null
  original: null
  note: 原文B（提供的片段）未提及等效法规。
- field: equivalent_to.version
  status: unsure
  extracted: null
  original: null
  note: 原文B（提供的片段）未提及等效法规版本。
- field: equivalent_to.relation
  status: unsure
  extracted: null
  original: null
  note: 原文B（提供的片段）未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 原文B（提供的片段）未明确提及取代的旧版本。
_ocr_upgraded: mineru
_mineru_content_hash: 993a2925bb68f820
_mineru_outputs_dir: outputs/993a2925bb68f820
_mineru_blocks:
  tables: 5
  formulas: 15
  images: 8
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 94 (Revision 4) - Frontal Collision Occupant Protection

## 法规概述
本法规规定了关于M1类（总质量不超过3500 kg）和N1类（总质量不超过2500 kg）车辆在正面碰撞（偏置可变形壁障试验）中保护前排乘员的统一技术规定和批准条件。其他类别的车辆可根据制造商的请求进行批准。

## 核心技术要求

### 1. 适用范围 (Scope)
适用于M1类（总质量≤3500 kg）和N1类（总质量≤2500 kg）车辆。其他车辆可根据制造商请求批准。

### 2. 定义 (Definitions)
包含43项关键定义，涉及：
- **保护系统**：旨在约束乘员并有助于满足第5条要求的内部装置和设备。
- **车辆类型**：在影响碰撞试验结果的基本方面无差异的车辆类别。
- **乘员舱**：针对乘员保护和电气安全评估分别定义。
- **R点与H点**：座椅参考点。
- **可充电储能系统**：为电力推进提供电能的系统。
- **高压**：工作电压 > 60 V 且 ≤ 1500 V DC，或 > 30 V 且 ≤ 1000 V AC (rms)。
- **电气防护等级IPXXB**：使用关节试验指提供的防接触保护。

### 3. 批准申请 (Application for approval)
由车辆制造商或其正式认可的代表提交，需附详细技术文件。

### 4. 批准 (Approval)
满足本法规要求的车辆类型应被批准，并授予批准编号和国际批准标志。

### 5. 技术规范 (Specifications)
#### 5.1 通用规范
- H点确定需符合附录6程序。
- 安全带组件需满足UN R16要求。
- 安全带固定点需符合UN R14要求。

#### 5.2 试验要求
按照附录3方法进行的车辆试验，若同时满足以下所有条件，则视为合格：
1.  **假人性能指标**（前排外侧座椅）：
    - 头部性能指标(HPC) ≤ 1000，且合成头部加速度超过80g的持续时间不超过3ms。
    - 颈部损伤指标(NIC)不超过规定限值。
    - 颈部绕y轴弯曲力矩 ≤ 57 Nm（伸展）。
    - 胸部压缩指标(ThCC) ≤ 42 mm。
    - 胸部粘性指标(V*C) ≤ 1.0 m/s。
    - 股骨力指标(FFC)不超过力-时间性能标准。
    - 胫骨压缩力指标(TCFC) ≤ 8 kN。
    - 胫骨指数(TI) ≤ 1.3（顶部和底部）。
    - 膝关节滑动位移 ≤ 15 mm。
2.  **转向盘残余位移**：中心处向上垂直方向≤80mm，向后水平方向≤100mm。
3.  **车门状态**：试验中任何车门不得打开；试验后，侧门应解锁。
4.  **可接近性**：试验后，应能不使用工具（支撑假人重量除外）完成以下操作：
    - 每排座椅至少打开一扇门（若无门，可通过激活座椅位移系统实现乘员撤离）。
    - 以不超过60N的力释放假人约束系统。
    - 在不调整座椅的情况下移出假人。
5.  **液体燃料车辆**：碰撞后燃料供给装置仅允许轻微泄漏；若持续泄漏，速率不得超过30 g/min。
6.  **配备电力驱动系统的车辆**：需额外满足以下电气安全要求（可通过单独试验验证）：
    - **防电击保护**：高压母线需满足以下至少一项标准：
 - **无高压**：碰撞后60秒内，电压Ub、U1、U2 ≤ 30 VAC 或 60 VDC。
 - **低电能**：总能量(TE) < 0.2 焦耳。
 - **物理防护**：提供IPXXB防护等级，且暴露导电部件与电底盘间电阻<0.1Ω，可同时触及的暴露导电部件间电阻<0.2Ω。
 - **绝缘电阻**：高压母线与电底盘间绝缘电阻满足规定值（DC总线：≥100 Ω/V工作电压；AC总线：≥500 Ω/V工作电压；混合总线有特定要求）。
    - **电解液泄漏**：
 - 水性电解质REESS：碰撞后60分钟内，无电解液泄漏至乘员舱，且泄漏至乘员舱外的电解液不超过REESS电解液体积的7%（最多5.0升）。
 - 非水性电解质REESS：碰撞后60分钟内，无液体电解液泄漏至乘员舱、行李舱或车外。
    - **REESS保持**：REESS应通过至少一个部件固定点、支架或任何将载荷传递至车辆结构的结构保持连接，且位于乘员舱外的REESS不得进入乘员舱。
    - **REESS火灾危险**：碰撞后60分钟内，REESS无着火或爆炸迹象。

#### 5.3 特殊规定
- 对于基于N1类（总质量>2500 kg）车型的M1类（总质量>2500 kg）车辆，若完全符合UN R137要求且满足特定几何条件（如角度α>22°或轴距比>1.30），可视为满足第5条要求。
- 对于总质量超过2250 kg但不超过2500 kg的N1类车辆，若其结构基础为梯形车架，完全符合UN R137要求且满足上述几何条件，可视为满足第5条要求。

### 6. 配备安全气囊车辆的用户说明 (Instructions for users of vehicles equipped with airbags)
对于配备安全气囊的车辆，需证明符合UN R16（08系列修正）第8.1.8至8.1.9条关于用户说明的要求。

### 7. 车辆类型的修改和扩展批准 (Modification and extension of approval of the vehicle type)
任何修改需通知批准该车辆类型的型式批准机构，可能被指定为“修订”或“扩展”。

### 8. 生产一致性 (Conformity of production)
每辆批准车辆的生产应符合已批准的车辆类型并满足第5条和第6条要求。型式批准机构可每两年验证一次生产设施的一致性控制方法。

### 9. 生产不一致的处罚 (Penalties for non-conformity of production)
若不符合生产一致性要求，可撤销批准。

### 10. 生产永久性终止 (Production definitively discontinued)
若制造商完全停止生产已批准类型的车辆，应通知授予批准的型式批准机构。

### 11. 负责批准试验的技术服务及型式批准机构 (Names and addresses of Technical Services and Type Approval Authorities)
缔约方应向联合国秘书处通报相关信息。

### 12. 过渡性规定 (Transitional provisions)
- 自04系列修正案正式生效之日起，任何适用本法规的缔约方不得拒绝根据04系列修正案授予或接受型式批准。
- 自2023年9月1日起，缔约方无义务接受在此日期之后首次根据先前系列修正案颁发的车辆型式批准。
- 缔约方应继续接受在2023年9月1日之前首次根据先前系列修正案颁发的车辆型式批准，前提是这些先前修正案的过渡性规定预见了这种可能性。
- 缔约方不得拒绝根据本法规任何先前系列修正案或其扩展授予型式批准。
- 新开始适用本法规的缔约方无义务接受根据本法规任何先前系列修正案授予的型式批准。

## 附录清单
1.  **Communication** - 批准通讯表格
2.  **Arrangements of approval marks** - 批准标志布置示例
3.  **Test procedure** - 试验程序（车辆准备、假人安装、推进、测量）
4.  **Head Performance Criterion (HPC) and 3 ms head acceleration performance criteria** - 头部性能指标及3ms头部加速度性能标准
5.  **Arrangement and installation of dummies and adjustment of restraint systems** - 假人布置、安装及约束系统调整
6.  **Procedure for determining the "H" point and the actual torso angle for seating positions in motor vehicles** - H点及实际躯干角确定程序
7.  **Test procedure with trolley** - 台车试验程序
8.  **Technique of measurement in measurement tests: Instrumentation** - 测量技术：仪器设备
9.  **Definition of deformable barrier** - 可变形壁障定义
10. **Certification procedure for the dummy lower leg and foot** - 假人小腿和脚部认证程序
11. **Test procedures for the vehicles equipped with electric power trains** - 配备电力驱动系统车辆的试验程序

## 关键日期与版本信息
- **发布日期**：2022年12月29日
- **版本**：Revision 4
- **纳入的有效文本截止**：
    - 03系列修正案补遗1 – 生效日期：2019年5月28日
    - 03系列修正案补遗2 – 生效日期：2021年1月3日
    - UN法规04系列修正案 – 生效日期：2021年6月9日
- **关于安全气囊用户说明的适用日期**：2020年9月1日起适用于新车型。
- **过渡条款关键日期**：2023年9月1日。

## 关联法规
- **UN R16**：关于安全带、约束系统、儿童约束系统和ISOFIX儿童约束系统的统一规定。
- **UN R14**：关于安全带固定点的统一规定。
- **UN R137**：关于M1和N1类车辆正面全宽碰撞乘员保护的统一规定。
- **1958年协定**：关于对轮式车辆、其装备和部件采用统一技术规定以及基于这些规定相互承认批准的条件协定。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 5 个
> - 公式 15 个
> - 图像 25 个
> - 全文 Markdown 129,446 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 5 个）

#### 表 1 (page 21)
<table><tr><td>94</td><td>041424</td><td>↑a8</td><td rowspan="2">a/2 a/2</td></tr><tr><td>11</td><td>042439</td><td>3</td></tr></table>

#### 表 2 (page 22)
<table><tr><td>1.</td><td>Installation and preparation of the vehicle</td></tr><tr><td>1.1.</td><td>Testing ground</td></tr><tr><td></td><td>The test area shall be large enough to accommodate the run-up track, barrier and technical installations necessary for the test. The last part of the track, for at least 5 m before the barrier, shall be horizontal, flat and smooth.</td></tr><tr><td>1.2.</td><td>Barrier The front face of the barrier consists of a deformable structure as defined in</td></tr><tr><td></td><td>Annex 9 of this Regulation. The front face of the deformable structure is perpendicular within ±1° to the direction of travel of the test vehicle. The barrier is secured to a mass of not less than 7 x 1O4 kg,the front face of which is vertical within ±1°. The mass is anchored in the ground or placed on the ground with, if necessary,additional arresting devices to restrict its movement.</td></tr><tr><td>1.3.</td><td>Orientation of the barrier The orientation of the barrier is such that the first contact of the vehicle with</td></tr><tr><td></td><td>the barrier is on the steering-column side.Where there is a choice between carrying out the test with a right-hand or left-hand drive vehicle,the test shall be carried out with the less favourable hand of drive as determined by the Technical Service responsible for the tests.</td></tr><tr><td>1.3.1.</td><td>Alignment of the vehicle to the barrier</td></tr><tr><td></td><td>The vehicle shall overlap the barrier face by 4O per cent± 2O mm.</td></tr><tr><td>1.4.</td><td>State of vehicle</td></tr><tr><td>1.4.1.</td><td>General specification The test vehicle shall be representative of the series production,shall include</td></tr><tr><td></td><td>all the equipment normally fitted and shall be in normal running order. Some components may be replaced by equivalent masses where this substitution clearly has no noticeable effect on the results measured under paragraph 6.</td></tr><tr><td></td><td>It shall be allowed by agreement between manufacturer and Technical Service to modify the fuel system so that an appropriate amount of fuel can be used to</td></tr><tr><td></td><td>run the engine or the electrical energy conversion system. Mass of vehicle</td></tr><tr><td>1.4.2. 1.4.2.1.</td><td>For the test, the mass of the vehicle submitted shall be the unladen kerb mass.</td></tr><tr><td>1.4.2.2.</td><td>The fuel tank shall be filled with water to mass equal to 9O per cent of the mass</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>of a full load of fuel as specified by the manufacturer with a tolerance of ±1</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>per cent.</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>This requirement does not apply to hydrogen fuel tanks.</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

#### 表 3 (page 26)
<table><tr><td>2.</td><td>Dummies</td></tr><tr><td>2.1.</td><td>Front seats</td></tr><tr><td>2.1.1.</td><td>A dummy corresponding to the specifications for Hybrid III fiftieth percentile male dummyl fitted with a 45°ankle and meeting the specifications for its adjustment shall be installed in each of the front outboard seats in accordance with the conditions set out in Annex 5.The ankle of the dummy shall be</td></tr><tr><td>2.1.2.</td><td>certified in accordance with the procedures in Annex 10. The car will be tested with restraint systems, as provided by the manufacturer.</td></tr><tr><td>3.</td><td>Propulsion and course of vehicle</td></tr><tr><td>3.1.</td><td>The vehicle shall be propelled either by its own engine or by any other propelling device.</td></tr><tr><td>3.2.</td><td>At the moment of impact the vehicle shall no longer be subject to the action of any additional steering or propelling device.</td></tr><tr><td>3.3.</td><td>The course of the vehicle shall be such that it satisfies the requirements of</td></tr><tr><td>4.</td><td>paragraphs 1.2. and 1.3.1. above. Test speed</td></tr><tr><td></td><td>Vehicle speed at the moment of impact shall be 56 -O/+1 km/h. However, if the test was performed at a higher impact speed and the vehicle met the</td></tr><tr><td>5.</td><td>requirements, the test shall be considered satisfactory. Measurements to be made on dummy in front seats</td></tr><tr><td>5.1.</td><td>All the measurements necessary for the verification of the performance criteria shall be made with measurement systems corresponding to the specifications</td></tr><tr><td>5.2.</td><td>of Annex 8. The different parameters shall be recorded through independent data channels of the following CFC (Channel Frequency Class):</td></tr><tr><td>5.2.1.</td><td>Measurements in the head of the dummy</td></tr><tr><td></td><td>The acceleration (a) referring to the centre of gravity is calculated from the triaxial components of the acceleration measured with a CFC of 1,000.</td></tr><tr><td>5.2.2.</td><td>Measurements in the neck of the dummy</td></tr><tr><td>5.2.2.1.</td><td>The axial tensile force and the fore/aft shear force at the neck/head interface</td></tr><tr><td>5.2.2.2.</td><td>are measured with a CFC of 1,000. The bending moment about a lateral axis at the neck/head interface are</td></tr><tr><td>5.2.3.</td><td>measured with a CFC of 600. Measurements in the thorax of the dummy</td></tr><tr><td></td><td>The chest deflection between the sternum and the spine is measured with a</td></tr></table>

#### 表 4 (page 31)
<table><tr><td colspan="2">restramntsystens</td></tr><tr><td>1.</td><td>Arrangement of dummies</td></tr><tr><td>1.1.</td><td>Separate seats</td></tr><tr><td rowspan="2"></td><td>The plane of symmetry of the dummy shall coincide with the vertical median</td></tr><tr><td>plane of the seat. Front bench seat</td></tr><tr><td>1.2. 1.2.1.</td><td>Driver</td></tr><tr><td rowspan="2"></td><td>The plane of symmetry of the dummy shall lie in the vertical plane passing through the steering wheel centre and parallel to the longitudinal median plane of the vehicle.If the seating position is determined by the shape of the bench,</td></tr><tr><td>such seat shall be regarded as a separate seat. Outer passenger</td></tr><tr><td></td><td>The plane of symmetry of the dummy shall be symmetrical with that of the driver dummy relative to the longitudinal median plane of the vehicle.If the seating position is determined by the shape of the bench,such seat shall be regarded as a separate seat.</td></tr><tr><td rowspan="2">1.3.</td><td>Bench seat for front passengers (not including driver) The planes of symmetry of the dummy shall coincide with the median planes</td></tr><tr><td>of the seating positions defined by the manufacturer.</td></tr><tr><td>2.</td><td>Installation of dummies</td></tr><tr><td>2.1.</td><td>Head The transverse instrumentation platform of the head shall be horizontal within</td></tr><tr><td></td><td>non-adjustable backs,the following sequences must be followed.First adjust the position of the &quot;H&quot; point within the limits set forth in paragraph 2.4.3.1. below to level the transverse instrumentation platform of the head of the test dummy.If the transverse instrumentation platform of the head is still not level, then adjust the pelvic angle of the test dummy within the limits provided in paragraph 2.4.3.2. below. If the transverse instrumentation platform of the head is still not level, then adjust the neck bracket of the test dummy the minimum amount necessary to ensure that the transverse instrumentation platform of the head is horizontal within 2.5°.</td></tr><tr><td>2.2. 2.2.1</td><td>Arms The driver&#x27;s upper arms shallbe adiacent to the torso with the centrelines as</td></tr></table>

#### 表 5 (page 43)
<table><tr><td rowspan="2">CFC</td><td rowspan="2">FL</td><td rowspan="2">FH</td><td rowspan="2">FN</td><td colspan="4">N Logarithmic scale</td></tr><tr><td>a b</td><td>土 +</td><td>0.5 0.5; -1</td><td>dB dB</td></tr><tr><td rowspan="2">1,000 600</td><td>Hz ≤0.1</td><td>Hz 1,000</td><td>Hz 1,650</td><td>C d</td><td>+ 1</td><td>0.5; -4 9</td><td>dB dB/octave</td></tr><tr><td>≤0.1</td><td>600</td><td>1,000</td><td>e</td><td>-</td><td>24</td><td>dB/octave</td></tr><tr><td rowspan="3">180 60</td><td>≤0.1 ≤0.1</td><td>180 60</td><td>300 100</td><td>f g</td><td>-30</td><td>8</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

### 公式（取前 15 个）

**公式 1** (page 28):

$$
\mathrm { H P C } = ( \mathbf { t } _ { 2 } - \mathbf { t } _ { 1 } ) \left[ \frac { 1 } { \mathbf { t } _ { 2 } - \mathbf { t } _ { 1 } } \int ^ { 2 } \ a d t \right] ^ { 2 . 5 }
$$

**公式 2** (page 29):

$$
\mathrm { T I } = \left| ~ \mathbf { M } _ { \mathrm { R } } / \left( \mathbf { M } _ { \mathrm { C } } \right) _ { \mathrm { R } } \right| + \left| ~ \mathbf { F } _ { \mathrm { Z } } / \left( \mathbf { F } _ { \mathrm { C } } \right) _ { \mathrm { Z } } \right|
$$

**公式 3** (page 29):

$$
\begin{array} { l l l } { { \bf M } _ { \mathrm { X } } } & { = } & { { \mathrm { b e n d i n g ~ m o m e n t ~ a b o u t ~ t h e ~ x ~ a x i s } } } \\ { { \bf M } _ { \mathrm { Y } } } & { = } & { { \mathrm { b e n d i n g ~ m o m e n t ~ a b o u t ~ t h e ~ y ~ a x i s } } } \\ { { \bf ( M _ { \mathrm { C } } ) } _ { \mathrm { R } } } & { = } & { { \mathrm { c r i t i c a l ~ b e n d i n g ~ m o m e n t ~ a n d ~ s h a l l ~ b e ~ t a k e n ~ t o ~ b e ~ } 2 2 5 \mathrm { { N m } } } } \\ { { \bf F } _ { \mathrm { Z } } } & { = } & { { \mathrm { c o m p r e s s i v e ~ a x i a l ~ f o r c e ~ i n ~ t h e ~ z ~ d i r e c t i o n } } } \\ { { \bf ( F _ { \mathrm { C } } ) } _ { \mathrm { Z } } } & { = } & { { \mathrm { c r i t i c a l ~ c o m p r e s s i v e ~ f o r c e ~ i n ~ t h e ~ z ~ d i r e c t i o n ~ a n d ~ s h a l l ~ b e ~ t a ~ } } } \end{array}
$$

**公式 4** (page 29):

$$
\begin{array} { r l r } { { \bf M } _ { \mathrm { R } } \quad } & { { } \quad } & { = \quad \sqrt { \left( { \bf M } _ { \mathrm { X } } \right) ^ { 2 } + \left( { \bf M } _ { \mathrm { Y } } \right) ^ { 2 } } } \end{array}
$$

**公式 5** (page 29):

$$
\mathbf { C } _ { _ { ( \mathrm { t } ) } } = \frac { \mathbf { D } _ { _ { ( \mathrm { t } ) } } } { 0 . 2 2 9 }
$$

**公式 6** (page 30):

$$
\mathbf { V } _ { \mathrm { ( t ) } } = \frac { 8 \left( \mathbf { D } _ { \mathrm { ( t + 1 ) } } - \mathbf { D } _ { \mathrm { ( t - 1 ) } } \right) - \left( \mathbf { D } _ { \mathrm { ( t + 2 ) } } - \mathbf { D } _ { \mathrm { ( t - 2 ) } } \right) } { 1 2 \hat { \sigma } \mathrm { t } }
$$

**公式 7** (page 46):

$$
\mathbf { A } = { \frac { \left( \mathbf { L } _ { 1 } + \mathbf { L } _ { 2 } + \mathbf { L } _ { 3 } \right) } { 3 } } \mathbf { x } { \frac { \left( \mathbf { W } _ { 1 } + \mathbf { W } _ { 2 } + \mathbf { W } _ { 3 } \right) } { 3 } }
$$

**公式 8** (page 46):

$$
F \left( n \right) = \frac { { \left( F \left( n \right) 1 + F \left( n \right) 2 + . . . + F \left( n \right) m \right) } } { m } ; m = 1 , 2 , 3
$$

**公式 9** (page 46):

$$
\mathbf { S } \left( \mathbf { n } \right) = \frac { \mathbf { F } \left( \mathbf { n } \right) } { \mathbf { A } } ; \mathbf { \Omega } \mathbf { n } = 1 , 2 , 3
$$

**公式 10** (page 61):

$$
\mathrm { T E } = \int \limits _ { t c } ^ { t h } { \bf { U _ { b } } } \times \mathrm { I _ { e } d t }
$$

**公式 11** (page 61):

$$
\mathrm { T E } = 0 . 5 \mathrm { \times C _ { \mathrm { x } } \mathrm { x } U _ { \mathrm { b } } } ^ { 2 }
$$

**公式 12** (page 62):

$$
\begin{array} { r } { \mathrm { T E } _ { \mathrm { y 1 } } = 0 . 5 \mathrm { ~ x ~ C _ { \mathrm { y 1 } } \mathrm { ~ x ~ U _ { 1 } } ^ { 2 } } } \\ { \mathrm { T E } _ { \mathrm { y 2 } } = 0 . 5 \mathrm { ~ x ~ C _ { \mathrm { y 2 } } \mathrm { ~ x ~ U _ { 2 } } ^ { 2 } } } \end{array}
$$

**公式 13** (page 64):

$$
\mathbf { R } = \mathbf { U } / \mathbf { I }
$$

**公式 14** (page 66):

$$
\mathrm { R i } = \mathrm { R o ^ { * } U _ { b } } ^ { * } ( 1 / \mathrm { U _ { l } } ^ { \prime } - 1 / \mathrm { U _ { l } } )
$$

**公式 15** (page 67):

$$
\mathrm { R _ { i } } = \mathrm { R _ { o } } ^ { \ast } \mathrm { U _ { b } } ^ { \ast } ( 1 / \mathrm { U _ { 2 } } ^ { \ast } - 1 / \mathrm { U _ { 2 } } )
$$

### 图像（取前 8 张）

![Figure 1 Neck tension criterion  / Figure 2 Neck shear criterion ](../_mineru_assets/ECE R94 Rev4/9050e75e6540c7b71db1d838bdb251c62388738afe0e525cbf78a05a5040b703.jpg)  
*Figure 1 Neck tension criterion  / Figure 2 Neck shear criterion * (page 10)

![图 page 11](../_mineru_assets/ECE R94 Rev4/1c9aaaa9b854fe579ddd2202285e13183cee6774a4116912f8cb9a797acc349e.jpg)  

![Figure 3 Femur force criterion  / 5.2.1.7. The tibia compression force criterion (TCFC) shall not exceed $8 \ \mathrm { k N }$ ： ](../_mineru_assets/ECE R94 Rev4/db821a4bf44844c55962341114a2185d1e24adb6141393237d2b1b18287b3237.jpg)  
*Figure 3 Femur force criterion  / 5.2.1.7. The tibia compression force criterion (TCFC) shall not exceed $8 \ \mathrm { k N }$ ： * (page 11)

![Figure 4 ](../_mineru_assets/ECE R94 Rev4/b2253d4d23155f60a146ebed981c20ce8414f45a47cf6f448d9a45e30992f187.jpg)  
*Figure 4 * (page 16)

![图 page 19](../_mineru_assets/ECE R94 Rev4/d5504bfcebde2c0969df3ee5f8a84b5d11a466605c0cc18848c87c062de56d30.jpg)  

![图 page 21](../_mineru_assets/ECE R94 Rev4/85a5da0158ce58245c48f685581d2b856d2c94cc60f88f8c3ec5fd0dfb2b3ff9.jpg)  

![图 page 30](../_mineru_assets/ECE R94 Rev4/21467eeb89b9c0d2f00b8232f0f8acb722f1383ce941c704e1b1a837d445b389.jpg)  

![图 page 38](../_mineru_assets/ECE R94 Rev4/baa0d73bea7202956101c5d57814c747e418de9c17031b1a04cf6aea01c24da3.jpg)  

