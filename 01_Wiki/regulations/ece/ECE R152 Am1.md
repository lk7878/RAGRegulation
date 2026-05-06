---
reg_id: ECE R152 Am1
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles
status: active
publication_date: 2020-11-04
implementation_date_new_vehicle: 2020-09-25
source_file: R152am1e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\152\R152am1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
title_conf: low
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: title
  status: mismatch
  extracted: Uniform provisions concerning the approval of motor vehicles with regard
    to the Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles
  original: Uniform provisions concerning the approval of motor vehicles with regard
    to the Advanced Emergency Braking System (AEBS) for M and N vehicles
  note: A 中为 "M1 and N1 vehicles"，B 中为 "M and N vehicles"。B 的标题中明确为 "M and N"，但正文定义中指向
    M1 和 N1。标题文字不一致。
  recheck_verdict: confirmed_mismatch
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: 双方均未明确提及标准机构（如 UNECE/WP.29），无法核实。
- field: implementation_date_new_vehicle
  status: normalized
  extracted: 2020-09-25
  original: 2020-09-25
  note: '[Auto-reclassified] Same date after parsing: 2020-09-25 == 2020-09-25'
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未提及在用车的实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未提及替代关系。
stage2_reclassified:
- implementation_date_new_vehicle
stage2_reclassified_at: '2026-04-18'
scope: Applies to vehicles of Category M1 and N1 with regard to an on-board Advanced
  Emergency Braking System to avoid or mitigate rear-end in-lane collisions with passenger
  cars and impacts with pedestrians.
_low_conf_recheck_source: stage3_llm_opus
_low_conf_recheck_verdict: upgrade
_low_conf_recheck_reason: body 内容结构完整，覆盖范围（Scope）、定义、审批、技术规格（Car-to-Car、Car-to-Pedestrian）、驾驶员中断、停用及警告等核心条款均有明确描述，标题与
  M1/N1 车辆范围一致可证。但 body 属摘要性重述而非逐条原文，部分细节（如具体表格数值、publication_date）无法从 body 直接核实，故升级至
  medium 而非 high。
_ocr_upgraded: mineru
_mineru_content_hash: f6d7e4d90071266a
_mineru_outputs_dir: outputs/f6d7e4d90071266a
_mineru_blocks:
  tables: 4
  formulas: 0
  images: 2
_mineru_merged_at: '2026-04-22'
---

# UN Regulation No. 152 - Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles

## 1. Scope
This Regulation applies to the approval of vehicles of Category M1 and N1 with regard to an on-board system to:
(a) Avoid or mitigate the severity of a rear-end in-lane collision with a passenger car,
(b) Avoid or mitigate the severity of an impact with a pedestrian.

## 2. Definitions
Key definitions include:
- **Advanced Emergency Braking System (AEBS)**: A system which can automatically detect an imminent forward collision and activate the vehicle braking system to decelerate the vehicle with the purpose of avoiding or mitigating a collision.
- **Emergency Braking**: A braking demand emitted by the AEBS to the service braking system of the vehicle.
- **Collision Warning**: A warning emitted by the AEBS to the driver when the AEBS has detected an imminent forward collision.
- **Time To Collision (TTC)**: The value of time obtained by dividing the longitudinal distance between the subject vehicle and the target by the longitudinal relative speed of the subject vehicle and the target, at any instant in time.
- **Dry road**: A road with a nominal peak braking coefficient of 0.9.

## 3. Application for Approval
The application for approval of a vehicle type with regard to the AEBS shall be submitted by the vehicle manufacturer or by their authorised representative, accompanied by required documentation and a representative vehicle.

## 4. Approval
If the vehicle type meets the requirements, approval shall be granted with an assigned approval number. An international approval mark must be affixed to every conforming vehicle.

## 5. Specifications

### 5.1. General Requirements
- The AEBS, when activated and operated within prescribed speed ranges, must meet performance requirements.
- Effectiveness shall not be adversely affected by magnetic or electrical fields (conformity with UN R10 required).
- Must meet safety aspects for electronic control systems (Annex 3).
- Must provide appropriate warnings for system failures, deactivation, and non-electrical failures.
- Designed to minimize false collision warnings and avoid unnecessary emergency braking.
- Vehicles must meet braking performance requirements of UN R13-H or R13 and be equipped with an anti-lock braking function.

### 5.2. Specific Requirements

#### 5.2.1. Car-to-Car Scenario
- **Collision Warning**: Must be provided when a collision is imminent, triggered at the latest 0.8 seconds before emergency braking starts.
- **Emergency Braking**: Upon detecting an imminent collision, a braking demand of at least 5.0 m/s² must be applied.
- **Speed Range**: System must be active at least within 10 km/h to 60 km/h.
- **Speed Reduction**: Specifies maximum allowable relative impact speeds for M1 and N1 vehicles under defined conditions (see tables in regulation).

#### 5.2.2. Car-to-Pedestrian Scenario
- **Collision Warning**: Must be provided when a collision with a pedestrian crossing at 5 km/h is imminent, no later than the start of emergency braking.
- **Emergency Braking**: A braking demand of at least 5.0 m/s² must be applied.
- **Speed Range**: System must be active at least within 20 km/h to 60 km/h.
- **Speed Reduction**: Specifies maximum allowable impact speeds for M1 and N1 vehicles under defined conditions (see tables in regulation).

### 5.3. Interruption by the Driver
The AEBS must provide means for the driver to interrupt the collision warning and emergency braking through positive actions (e.g., accelerator kick-down, steering input).

### 5.4. Deactivation
- If manually deactivated, the AEBS must automatically reactivate with each new ignition cycle. Deactivation must require at least two deliberate actions and not be possible above 10 km/h.
- If automatically deactivated (e.g., for off-road use), it must automatically reactivate when conditions permit.
- A constant optical warning signal must indicate deactivation.

### 5.5. Warning Indication
- Collision warning must use at least two modes (acoustic, haptic, or optical).
- Failure warning must be a constant yellow optical signal.
- Optical signals must be visible in daylight and verifiable from the driver's seat.

### 5.6. Provisions for Periodic Technical Inspection
It must be possible to confirm the AEBS operational status by observing the failure warning signal after power-on.

## 6. Test Procedure
- **Test Conditions**: Flat, dry surface with PBC of 0.9; ambient temperature 0°C to 45°C; specific illumination requirements.
- **Vehicle Conditions**: Tested at mass in running order and at maximum mass.
- **Test Targets**: For car-to-car: M1 vehicle or representative soft target. For pedestrian: child articulated soft target.
- **Specific Tests**:
    - Warning and activation test with a stationary vehicle target.
    - Warning and activation test with a moving vehicle target.
    - Warning and activation test with a pedestrian target.
    - Failure detection test.
    - Deactivation test.

## 7. Modification of Vehicle Type and Extension of Approval
Modifications must be notified to the Type Approval Authority, which may grant an extension or require further tests.

## 8. Conformity of Production
Manufactured vehicles must conform to the approved type. The Type Approval Authority may verify conformity control methods.

## 9. Penalties for Non-Conformity of Production
Approval may be withdrawn if conformity of production requirements are not met.

## 10. Production Definitively Discontinued
The approval holder must inform the Type Approval Authority if production ceases.

## 11. Names and Addresses of Technical Services and Type Approval Authorities
Contracting Parties must communicate relevant information to the UN Secretariat.

## Annexes
- **Annex 1**: Communication form for approval notifications.
- **Annex 2**: Arrangement of approval markings.
- **Annex 3**: Special requirements for the safety aspects of electronic control systems, including documentation, safety concept, and verification procedures. Appendix 2 lists false reaction scenarios for testing.
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 5 个
> - 公式 0 个
> - 图像 2 个
> - 全文 Markdown 67,914 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 5 个）

#### 表 1 (page 7)
**Maximum relative Impact Speed $\mathbf { ( k m / h ) }$ for Mi vehicle\* **

<table><tr><td rowspan=2 colspan=1>Relative Speed(km/h)</td><td rowspan=1 colspan=2>Stationary/ Moving</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>15.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr></table>

#### 表 2 (page 7)
**Maximum relative Impact Speed $\mathbf { ( k m / h ) }$ for $\mathbf { N _ { 1 } }$ vehicles \* **

<table><tr><td colspan="1" rowspan="3">Relative Speed(km/h)</td><td colspan="4" rowspan="1">Stationary/Moving</td></tr><tr><td colspan="2" rowspan="1">Maximum mass</td><td colspan="2" rowspan="1">Mass in running order</td></tr><tr><td colspan="1" rowspan="1">a&gt;1.3</td><td colspan="1" rowspan="1">a ≤1.3</td><td colspan="1" rowspan="1">a &gt;1.3</td><td colspan="1" rowspan="1">α ≤1.3</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">32</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">15.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">35</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">15.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">38</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">20.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">15.00</td></tr><tr><td colspan="1" rowspan="1">40</td><td colspan="1" rowspan="1">10.00</td><td colspan="1" rowspan="1">20.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">15.00</td></tr><tr><td colspan="1" rowspan="1">42</td><td colspan="1" rowspan="1">15.00</td><td colspan="1" rowspan="1">25.00</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">20.00</td></tr><tr><td colspan="1" rowspan="1">45</td><td colspan="1" rowspan="1">20.00</td><td colspan="1" rowspan="1">25.00</td><td colspan="1" rowspan="1">15.00</td><td colspan="1" rowspan="1">25.00</td></tr><tr><td colspan="1" rowspan="1">50</td><td colspan="1" rowspan="1">30.00</td><td colspan="1" rowspan="1">35.00</td><td colspan="1" rowspan="1">25.00</td><td colspan="1" rowspan="1">30.00</td></tr><tr><td colspan="1" rowspan="1">55</td><td colspan="1" rowspan="1">35.00</td><td colspan="1" rowspan="1">40.00</td><td colspan="1" rowspan="1">30.00</td><td colspan="1" rowspan="1">35.00</td></tr><tr><td colspan="1" rowspan="1">60</td><td colspan="1" rowspan="1">40.00</td><td colspan="1" rowspan="1">45.00</td><td colspan="1" rowspan="1">35.00</td><td colspan="1" rowspan="1">40.00</td></tr></table>

#### 表 3 (page 8)
#### 表 4 (page 9)
<table><tr><td rowspan=1 colspan=1>Subject vehicle speed(km/h)</td><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>20.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>40.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>45.00</td></tr></table>

#### 表 5 (page 9)
<table><tr><td rowspan=2 colspan=1>Subjectvehicle speed(km/h)</td><td rowspan=1 colspan=2>Maximum mass</td><td rowspan=1 colspan=2>Mass in running order</td></tr><tr><td rowspan=1 colspan=1>a&gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>α≤1.3</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>20.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>45.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>50.00</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>50.00</td></tr></table>

### 图像（取前 2 张）

![图 page 16](../_mineru_assets/ECE R152 Am1/2813cde17b8eab1fd04da0506470beb2203c437154bbc43a4a4fe2c1aaf7959c.jpg)  

![图 page 16](../_mineru_assets/ECE R152 Am1/d378679d04af3e3275bad64df3ae3366c8116b6b373da0d46c46d53e36f9a2b5.jpg)  

