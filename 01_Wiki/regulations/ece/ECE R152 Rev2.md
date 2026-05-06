---
reg_id: ECE R152 Rev2
region: ece
type: type/version
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles
status: active
standard_body: UNECE
publication_date: 2023-06-15
version: Revision 2
tags:
- type/version
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\152\R152r2e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
title_conf: low
cross_check_flags:
- field: title
  status: mismatch
  extracted: Uniform provisions concerning the approval of motor vehicles with regard
    to the Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles
  original: Uniform provisions concerning the approval of motor vehicles with regard
    to the Advanced Emergency Braking System (AEBS) for M and N vehicles
  note: A 中为 "M1 and N1"，B 中为 "M and N"。B 的脚注1说明 M1 和 N1 的定义，但标题本身未包含数字 "1"。
  recheck_verdict: confirmed_mismatch
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未明确提及新车型的实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未明确提及在用车型的实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 原文 B 未明确提及取代的法规版本。
scope: Applies to vehicles of Category M1 and N1 with regard to an on-board AEBS to
  avoid or mitigate rear-end in-lane collisions with passenger cars, impacts with
  pedestrians, and impacts with bicycles.
_low_conf_recheck_source: stage3_llm_opus
_low_conf_recheck_verdict: upgrade
_low_conf_recheck_reason: body 内容结构完整，覆盖了法规的核心章节（适用范围、定义、申请、批准、技术规范），关键技术参数清晰（速度范围、制动需求≥5.0
  m/s²、碰撞场景三类），标题在 body 中明确标注为 M1 和 N1，与 FM title 一致。但 publication_date 在 body 中无直接证据，body
  末尾 5.5 节内容缺失，细节不完整，定为 medium。
_ocr_upgraded: mineru
_mineru_content_hash: 7310ee5ec05d09a8
_mineru_outputs_dir: outputs/7310ee5ec05d09a8
_mineru_blocks:
  tables: 9
  formulas: 2
  images: 6
_mineru_merged_at: '2026-04-22'
---

# UN Regulation No. 152 - Advanced Emergency Braking System (AEBS) for M1 and N1 Vehicles

## 1. Scope
This Regulation applies to the approval of vehicles of Category M1 and N1 with regard to an on-board system to:
*   Avoid or mitigate the severity of a rear-end in-lane collision with a passenger car.
*   Avoid or mitigate the severity of an impact with a pedestrian.
*   Avoid or mitigate the severity of an impact with a bicycle.

## 2. Definitions
Key definitions include:
*   **Advanced Emergency Braking System (AEBS):** A system which can automatically detect an imminent forward collision and activate the vehicle braking system to decelerate the vehicle to avoid or mitigate a collision.
*   **Emergency Braking:** A braking demand emitted by the AEBS to the service braking system.
*   **Collision Warning:** A warning emitted by the AEBS to the driver when an imminent forward collision is detected.
*   **Subject Vehicle:** The vehicle being tested.
*   **Vehicle Target, Pedestrian Target, Bicycle Target:** Soft targets representing a vehicle, pedestrian, or bicycle with cyclist, respectively.
*   **Time To Collision (TTC):** The longitudinal distance between the subject vehicle and target divided by their longitudinal relative speed.
*   **Dry road:** A road with a nominal peak braking coefficient (PBC) of 0.9.

## 3. Application for Approval
The application must be submitted by the vehicle manufacturer or authorized representative, accompanied by technical documentation and a representative vehicle for testing.

## 4. Approval
Approval is granted if the vehicle type meets the requirements. An approval number is assigned, and an international approval mark must be affixed to conforming vehicles.

## 5. Specifications

### 5.1. General Requirements
*   The AEBS must meet performance requirements when activated within prescribed speed ranges.
*   Effectiveness must not be adversely affected by magnetic or electrical fields (conformity with UN R10, 05 series).
*   Must conform to the safety aspects for electronic control systems (Annex 3).
*   Must provide appropriate warnings for system failures and deactivation.
*   Must minimize false warnings and avoid false emergency braking.
*   The vehicle must meet the braking performance requirements of UN R13-H (01 series) or UN R13 (11 series) and be equipped with an anti-lock braking function.

### 5.2. Specific Requirements
Performance requirements are specified for three scenarios:
1.  **Car-to-Car:** System must be active between 10 km/h and 60 km/h. Specifies collision warning timing, emergency braking demand (≥5.0 m/s²), and maximum allowable relative impact speeds under defined test conditions (see tables in regulation).
2.  **Car-to-Pedestrian:** System must be active between 20 km/h and 60 km/h. Specifies collision warning, emergency braking demand (≥5.0 m/s²), and maximum allowable impact speeds for crossing pedestrians (5 km/h) under defined test conditions (see tables in regulation).
3.  **Car-to-Bicycle:** System must be active between 20 km/h and 60 km/h. Specifies collision warning, emergency braking demand (≥5.0 m/s²), and maximum allowable impact speeds for crossing bicycles (10-15 km/h) under defined test conditions (see tables in regulation).

### 5.3. Interruption by the Driver
The AEBS must provide means for the driver to interrupt collision warnings and emergency braking through positive actions (e.g., accelerator kick-down, steering action).

### 5.4. Deactivation
*   If manual deactivation is possible, it must require at least two deliberate actions, be automatically reinstated at each new ignition cycle, and not be possible above 10 km/h.
*   Automatic deactivation (e.g., for off-road use) criteria must be documented.
*   A constant optical warning signal must indicate deactivation.
*   During automated driving (e.g., ALKS active), the AEBS may be suspended or adapted if equivalent collision avoidance capability is maintained.

### 5.5. Warning Indication
*   Collision warning must use at least two modes (acoustic, haptic, or optical).
*   Failure warning must be a constant yellow optical signal.
*   Warning signals must be visible by daylight and verifiable by the driver.

### 5.6. Provisions for Periodic Technical Inspection
It must be possible to confirm the AEBS operational status via observation of the failure warning signal after power-on.

## 6. Test Procedure
*   **Conditions:** Tests on flat, dry road surface (PBC 0.9), ambient temperature 0-45°C, specified minimum ambient illumination (1000 lux for car-to-car, 2000 lux for pedestrian/bicycle), no significant wind.
*   **Vehicle Conditions:** Tests at mass in running order (+125 kg max for equipment) and at maximum mass.
*   **Targets:** Defined soft targets representing a passenger car (ISO 19206-3), a pedestrian (ISO 19206-2), and a bicycle with cyclist (ISO 19206-4).
*   **Test Scenarios:** Detailed procedures for warning and activation tests with stationary/moving vehicle targets, pedestrian targets, and bicycle targets. Specifies test speeds, TTC start conditions, and driver input restrictions.
*   **Other Tests:** Failure detection test and deactivation test.
*   **Robustness:** Test scenarios must be performed twice. Allowable failure rates are specified per scenario category (Car-to-Car: 10%, Car-to-Pedestrian: 10%, Car-to-Bicycle: 20%).

## 7. Modification of Vehicle Type and Extension of Approval
Modifications affecting the AEBS must be notified to the Type Approval Authority, which may grant an extension or require further tests.

## 8. Conformity of Production
Manufactured vehicles must conform to the approved type. The Type Approval Authority verifies conformity control methods at least once every two years.

## 9. Penalties for Non-Conformity of Production
Approval may be withdrawn if production conformity requirements are not met.

## 10. Production Definitively Discontinued
The approval holder must inform the Type Approval Authority if production ceases.

## 11. Technical Services and Type Approval Authorities
Contracting Parties must communicate the responsible Technical Services and Type Approval Authorities to the UN Secretariat.

## 12. Transitional Provisions
*   **01 Series Amendments:** Contracting Parties are not obliged to accept approvals to the original regulation issued after 1 May 2024, and shall not accept them after 1 May 2026 (with exceptions for unaffected vehicles).
*   **02 Series Amendments:** Contracting Parties are not obliged to accept approvals to the preceding series issued after 1 May 2024, and shall not accept them after 1 July 2026 (with exceptions for unaffected vehicles, e.g., car-to-car/pedestrian approvals not affected by the 02 series).

## Annexes
*   **Annex 1:** Model communication form for approvals.
*   **Annex 2:** Arrangement of approval markings.
*   **Annex 3:** Special requirements for the safety aspects of electronic control systems. Includes documentation requirements, safety concept, verification procedures, and assessment forms (Appendix 1). **Appendix 2** lists specific "False Reaction" scenarios (e.g., turning at intersections, lane changes) that must be assessed to minimize false warnings/braking.
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 15 个
> - 公式 2 个
> - 图像 6 个
> - 全文 Markdown 87,810 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 8)
<table><tr><td rowspan=2 colspan=1>Relative Speed(km/h)</td><td rowspan=1 colspan=2>Stationary/ Moving</td></tr><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in runningorder</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>15.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr></table>

#### 表 2 (page 8)
<table><tr><td colspan="1" rowspan="2">Relative Speed(km/h)</td><td colspan="2" rowspan="1">Stationary/Moving</td></tr><tr><td colspan="1" rowspan="1">Maximum mass</td><td colspan="1" rowspan="1">Mass in running order</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">32</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">35</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">38</td><td colspan="1" rowspan="1">0.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">40</td><td colspan="1" rowspan="1">10.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">42</td><td colspan="1" rowspan="1">15.00</td><td colspan="1" rowspan="1">0.00</td></tr><tr><td colspan="1" rowspan="1">45</td><td colspan="1" rowspan="1">20.00</td><td colspan="1" rowspan="1">15.00</td></tr><tr><td colspan="1" rowspan="1">50</td><td colspan="1" rowspan="1">30.00</td><td colspan="1" rowspan="1">25.00</td></tr><tr><td colspan="1" rowspan="1">55</td><td colspan="1" rowspan="1">35.00</td><td colspan="1" rowspan="1">30.00</td></tr><tr><td colspan="1" rowspan="1">60</td><td colspan="1" rowspan="1">40.00</td><td colspan="1" rowspan="1">35.00</td></tr></table>

#### 表 3 (page 9)
#### 表 4 (page 10)
<table><tr><td rowspan=1 colspan=1>Subject vehicle speed(km/h)</td><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>15.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr></table>

#### 表 5 (page 10)
<table><tr><td rowspan=1 colspan=1>Subject vehicle speed(km/h)</td><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>15.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>35.00</td></tr></table>

#### 表 6 (page 12)
<table><tr><td rowspan=1 colspan=1>Subject vehicle speed(km/h)</td><td rowspan=1 colspan=1>Maximummass</td><td rowspan=1 colspan=1>Mass in running order</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>40.00</td></tr></table>

#### 表 7 (page 12)
<table><tr><td rowspan=1 colspan=1>Subject vehicle speed(km/h)</td><td rowspan=1 colspan=1>Maximummass</td><td rowspan=1 colspan=1>Mass in running order</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>35.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>40.00</td></tr></table>

#### 表 8 (page 16)
<table><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>+0/-2</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 9 (page 16)
<table><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>+0/-2</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 10 (page 16)
<table><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

### 公式（取前 2 个）

**公式 1** (page 31):

$$
\mathrm { R _ { o v e r l a p } = L _ { o v e r l a p } / W _ { v e h i c l e } \ast 1 0 0 }
$$

**公式 2** (page 31):

$$
\begin{array} { r l } & { \mathrm { \bf R } _ { \mathrm { o f f s e t } } = \mathrm { \bf L } _ { \mathrm { o f f s e t } } / ( 0 . 5 ^ { * } \mathrm { \bf W } _ { \mathrm { v e h i c l e } } ) ^ { * } 1 0 0 } \\ & { \mathrm { \bf { R } } _ { \mathrm { o f f s e t } } : \mathrm { O f f s e t r a t i o } [ \% ] } \end{array}
$$

### 图像（取前 6 张）

![图 page 22](../_mineru_assets/ECE R152 Rev2/dc0b5aa53bcc567cdbcc342c77497d3721feaa9bb22c24f76eda50e3fd636bc9.jpg)  

![图 page 23](../_mineru_assets/ECE R152 Rev2/cb0320634649cad90f1544160da8e7a4d3e503c65a8343e56bbe6d04f4010a8a.jpg)  

![Figure 1 Left turn or right turn at the intersection ](../_mineru_assets/ECE R152 Rev2/e2f15c5db833ac414e71783fad27fd743bab9c6e4809767578f4a9c372e42bbb.jpg)  
*Figure 1 Left turn or right turn at the intersection * (page 32)

![Figure 2 Right turn or left turn of a forward vehicle ](../_mineru_assets/ECE R152 Rev2/01ea61690d019f2461c3de5406e9b09c5f951ead84d34ccc7944837afb81d9bb.jpg)  
*Figure 2 Right turn or left turn of a forward vehicle * (page 33)

![Figure 3 Curved road with guard pipes and a stationary object ](../_mineru_assets/ECE R152 Rev2/251c924b748f1ffa8090135e619792cd69ad5efb9bf5776f2fe38c4f5ffccb36.jpg)  
*Figure 3 Curved road with guard pipes and a stationary object * (page 34)

![图 page 35](../_mineru_assets/ECE R152 Rev2/0931419857ae50025bde02540cecb3032653aa6d065e1350265cc0d2ce407a28.jpg)  

