---
reg_id: ECE R151
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Blind Spot Information System for the Detection of Bicycles
region: ece
type: type/version
status: active
publication_date: 2020-01-13
implementation_date_new_vehicle: 2019-11-15
source: ECE/TRANS/505/Rev.3/Add.150
authentic_source: ECE/TRANS/WP.29/2019/28
amendments: Revision 3, including amendments effective 2017-09-14
topics:
- Blind Spot Information System (BSIS)
- vehicle safety
- vulnerable road users (VRU)
- bicycles
- driver assistance systems
vehicle_categories:
- N2 (> 8 t)
- N3
- N2 (≤ 8 t) (optional)
- M2 (optional)
- M3 (optional)
tags:
- type/version
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\151\R151e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
技术要求限值_conf: low
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: ece
  original: null
  note: 原文B未明确提及标准机构名称，但根据上下文推断为UNECE。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及针对在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及替代关系。
- field: 技术要求限值
  status: unsure
  extracted: 'Operational Range: At least from standstill to 30 km/h, in ambient light
    > 15 Lux.

    Activation Conditions: The information signal must be given at the LPI for a bicycle
    moving 5-20 km/h, at a lateral separation of 0.9-4.25 m, which could result in
    a collision with an impact position 0-6 m from the vehicle''s front right corner.
    It must also activate for a bicycle at 0.25-0.9 m lateral separation, longitudinally
    at'
  original: 原文B的“5. Specifications”部分未提供具体的性能要求限值。A中引用的限值可能来自原文后续章节（如第6节测试程序），但未在提供的B片段中。
  note: A中包含了具体的技术要求限值，但提供的原文B片段（至5.3.1）未包含这些具体数值。因此无法核实，视为不匹配。
  recheck_reason: 提供的原文片段仅包含法规目录和引言，未包含“5. Specifications”章节的具体内容，无法核实提取的限值信息。
_low_conf_recheck_source: stage3_llm_opus
_low_conf_recheck_verdict: upgrade
_low_conf_recheck_reason: body 内容结构完整，覆盖了法规的引言、适用范围、定义、批准程序、技术规格（含性能要求、信息信号、警告信号）等核心章节，标题与FM一致，法规编号清晰。主要缺失为具体技术数值未在前4000字中完整呈现，且publication_date无法从body直接证实，因此升级至medium而非high。
_ocr_upgraded: mineru
_mineru_content_hash: 4d27c991d7aa616f
_mineru_outputs_dir: outputs/4d27c991d7aa616f
_mineru_blocks:
  tables: 2
  formulas: 8
  images: 6
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 151

## 0. Introduction (for information)
This regulation addresses collisions between trucks turning right and cyclists, which often have serious consequences. It mandates a Blind Spot Information System (BSIS) to inform drivers of nearby bicycles. The system provides an early **information signal** and a later **warning signal** when a collision becomes imminent. The design aims to alert the driver early without causing annoyance, allowing sufficient reaction time.

## 1. Scope
*   Applies to the BSIS of vehicles of categories **N2 (> 8 t technically permissible maximum mass)** and **N3**.
*   Vehicles of categories **N2 (≤ 8 t)**, **M2**, and **M3** may be approved at the manufacturer's request.
*   Requirements are written for right-hand traffic; for left-hand traffic, criteria are inverted where appropriate.

## 2. Definitions
Key definitions include:
*   **Blind Spot Information System (BSIS):** A system to inform the driver of a possible collision with a bicycle on the near side.
*   **Near side:** The side of the vehicle near the bicycle (right side for right-hand traffic).
*   **Information signal:** An optical signal informing the driver about a nearby moving bicycle.
*   **Last Point of Information (LPI):** The point at which the information signal must have been given, preceding an expected turning motion.
*   **Collision point:** The position where vehicle and bicycle trajectories would intersect if a turn is initiated.
*   **Bicycle:** A combination of bicycle and cyclist, simulated in tests per specified standards.

## 3. Application for Approval
Submitted by the vehicle manufacturer or authorized representative, accompanied by required documentation and a representative vehicle.

## 4. Approval
Granted if the vehicle type meets the requirements. An approval number is assigned. An international approval mark (circle with "E" or oval with "UI") must be affixed to conforming vehicles.

## 5. Specifications
### 5.1. General
Any vehicle fitted with a BSIS must meet the following requirements.

### 5.2. General Requirements
System effectiveness must not be adversely affected by magnetic or electrical fields (compliance with UN R10).

### 5.3. Performance Requirements
*   The BSIS must inform the driver about nearby bicycles via an optical signal, enabling the vehicle to stop before crossing the bicycle's path. It must also inform about approaching bicycles while the vehicle is stationary.
*   It must warn the driver (optical, acoustical, haptic, or combination) when collision risk increases.
*   **Operational Range:** At least from standstill to 30 km/h, in ambient light > 15 Lux.
*   **Activation Conditions:** The information signal must be given at the LPI for a bicycle moving 5-20 km/h, at a lateral separation of 0.9-4.25 m, which could result in a collision with an impact position 0-6 m from the vehicle's front right corner. It must also activate for a bicycle at 0.25-0.9 m lateral separation, longitudinally at least at the front wheel.
*   **False Positives:** Must be minimized for static non-VRU objects.
*   **Deactivation:** Must deactivate automatically if sensors are contaminated (ice, snow, mud) or in low light (<15 Lux), and indicate this state. Must reactivate automatically when conditions normalize.
*   **Failure Warning:** Must provide a failure warning if a fault prevents compliance.
*   The manufacturer must demonstrate performance for smaller bicycles/cyclists (up to 36% smaller than reference).

### 5.4. Information Signal
*   Must be noticeable and easily verifiable by the driver, visible by day and night.
*   Emitting device must be located on the near side at a horizontal angle >30° from an axis through the ocular reference point (may be reduced if driver's seat is on the near side).

### 5.5. Warning Signal
*   Must differ from the information signal (e.g., in mode or activation strategy).
*   Must be easily understandable. If optical, visible by day and night.
*   Activation strategy (e.g., based on trajectory intersection, turn indicator) must be explained and verified. Must not depend solely on turn indicator activation.

### 5.6. Failure Warning Signals
*   Must be a yellow optical signal, distinct from the information signal, visible by day and night, easily verifiable.
*   Signals for temporary unavailability must remain active while the BSIS is unavailable.
*   Must activate with the vehicle master control switch (except for signals in a common space).

### 5.7. Provisions for Inspection
Correct operational status must be confirmable by visible observation of the failure warning signal.

## 6. Test Procedure
### 6.1. Documentation
Manufacturer must provide documentation explaining system design, function, sensing/warning strategy, status check, and failure warning conditions.

### 6.2-6.3. Test & Vehicle Conditions
*   Tests on flat, dry asphalt/concrete, ambient temperature 0-45°C, good visibility.
*   Vehicle tested at manufacturer-stated load condition (not exceeding axle limits), normal tyre pressures.
*   If BSIS has user-adjustable timing, tests performed at the "worst-case" setting (signal closest to collision point).

### 6.4. Optical Failure Warning Signals Verification Test
Verify compliance of warning, information, and failure signals with the vehicle stationary.

### 6.5. Blind Spot Information Dynamic Test
*   Conducted using a corridor and bicycle dummy per **Appendix 1, Figure 1 and Table 1**.
*   Vehicle drives through corridor at specified speed (±2 km/h). Bicycle dummy moves on a straight path, synchronized to cross specific lines with the vehicle.
*   **Pass Criteria:** Information signal must activate **before** vehicle crosses line C, and must **not** activate before vehicle crosses line D or when passing the traffic sign/cones with the dummy stationary.
*   Test repeated for cases in Table 1. Technical Service may select other test cases within specified parameter ranges.

### 6.6. Blind Spot Information Static Tests
*   **Type 1:** Stationary vehicle. Bicycle dummy moves perpendicular towards vehicle front (impact position 1.15 m ahead) at 5 km/h. Signal must activate at latest when bicycle is 2 m away.
*   **Type 2:** Stationary vehicle. Bicycle dummy moves parallel to vehicle at 20 km/h, lateral separation 2.75 m. Signal must activate at latest when bicycle is 7.77 m ahead of vehicle's front point.

### 6.7. Demonstration for Other Stationary Objects
Manufacturer must demonstrate (via documentation/simulation) that the information signal is not activated when passing usual stationary objects (especially parked cars).

### 6.8. Failure Detection Test
Simulate a BSIS failure (e.g., disconnect power). The failure warning signal must activate and remain active while driving, and reactivate with each master control switch activation as long as the failure exists.

### 6.9. Automatic Deactivation Test
Contaminate sensors (e.g., with substance simulating snow/mud). BSIS must deactivate automatically and indicate this. Upon contamination removal and master control switch reactivation, BSIS must reactivate automatically within 60 seconds of driving.

## 7. Modification of Vehicle Type and Extension of Approval
Modifications must be notified to the Type Approval Authority, which may grant an extension or require further tests.

## 8. Conformity of Production
Production vehicles must conform to the approved type. Conformity control inspections normally occur every two years.

## 9. Penalties for Non-Conformity of Production
Approval may be withdrawn if production conformity requirements are not met.

## 10. Production Definitively Discontinued
Manufacturer must inform the Type Approval Authority if production of an approved type ceases.

## 11. Names and Addresses of Technical Services and Authorities
Contracting Parties must communicate relevant details to the UN Secretariat.

## Appendices and Annexes
*   **Appendix 1:** Contains figures and tables for test setup (dynamic/static test layouts, impact location, test case parameters, `d_c` values for speeds >25 km/h).
*   **Annex 1:** Model communication form.
*   **Annex 2:** Arrangements of approval marks (E-mark and Unique Identifier examples).
*   **Annex 3:** Procedure to define performance requirements for test cases other than those in the main table.
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 2 个
> - 公式 8 个
> - 图像 6 个
> - 全文 Markdown 45,864 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 2 个）

#### 表 1 (page 15)
**Table 1 Test cases **

<table><tr><td rowspan=2 colspan=1>TestCase</td><td rowspan=2 colspan=1>Vbicyclee[km/h]</td><td rowspan=2 colspan=1>Vvehicle[km/h]</td><td rowspan=2 colspan=1>dlateral[m]</td><td rowspan=2 colspan=1>da[m]</td><td rowspan=2 colspan=1>db[m]</td><td rowspan=2 colspan=1>dc[m]</td><td rowspan=2 colspan=1>dd[m]</td><td rowspan=2 colspan=1>dbicyele[m]</td><td rowspan=2 colspan=1>lcorridor[m]</td><td rowspan=2 colspan=1>dcorridor[m]</td><td rowspan=1 colspan=2>Forinformation only (not influencing testparameters)</td></tr><tr><td rowspan=1 colspan=1>Impact Position [m]</td><td rowspan=1 colspan=1>Turn Radius [m]</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>10</td><td rowspan=3 colspan=1>1.25</td><td rowspan=3 colspan=1>44.4</td><td rowspan=1 colspan=1>15.8</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>26.1</td><td rowspan=7 colspan=1>65</td><td rowspan=7 colspan=1>80</td><td rowspan=7 colspan=1>vehiclewidth+1m</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>32.3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>38.3</td><td rowspan=1 colspan=1>38.3</td><td rowspan=1 colspan=1>65</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>25</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>22.2</td><td rowspan=1 colspan=1>43.5</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>43.2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>25</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>19.8</td><td rowspan=1 colspan=1>19.8</td><td rowspan=1 colspan=1>65</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=2 colspan=1>20</td><td rowspan=2 colspan=1>10</td><td rowspan=2 colspan=1>4.25</td><td rowspan=2 colspan=1>44.4</td><td rowspan=1 colspan=1>14.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>26.1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>17.7</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>29.1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>10</td></tr></table>

#### 表 2 (page 16)
**able 2 dc for speeds above 25 km/h **

<table><tr><td>Vehicle Speed [km/h]</td><td>dc[m]</td></tr><tr><td>25</td><td>15</td></tr><tr><td>26</td><td>15.33</td></tr><tr><td>27</td><td>16.13</td></tr><tr><td>28</td><td>16.94</td></tr><tr><td>29</td><td>17.77</td></tr><tr><td>30</td><td>18.61</td></tr></table>

### 公式（取前 8 个）

**公式 1** (page 19):

$$
d _ { \mathrm { a } } = 8 s \cdot v _ { \mathrm { B i c y c l e } }
$$

**公式 2** (page 19):

$$
d _ { \mathrm { b } , 1 } = 8 s \cdot v _ { \mathrm { V e h i c l e } }
$$

**公式 3** (page 19):

$$
d _ { \mathbf { b } , 2 } = L
$$

**公式 4** (page 19):

$$
d _ { \mathsf { b } , 3 } = R \cdot \mathsf { c o s } ^ { - 1 } \left( \frac { R - Y } { R } \right) - \sqrt { R ^ { 2 } - ( R - Y ) ^ { 2 } }
$$

**公式 5** (page 19):

$$
d _ { b } = 8 s \cdot v _ { \mathrm { V e h i c l e } } - L - R \ \cos ^ { - 1 } \left( { \frac { R - Y } { R } } \right) + { \sqrt { R ^ { 2 } - ( R - Y ) ^ { 2 } } }
$$

**公式 6** (page 20):

$$
d _ { \mathrm { S t o p } } = v _ { \mathrm { v e h i c l e } } \cdot t _ { \mathrm { r e a c t } } + { \frac { v _ { \mathrm { V e h i c l e } } ^ { 2 } } { 2 \left| a \right| } }
$$

**公式 7** (page 20):

$$
d _ { \mathrm { c } } = M A X \left( 1 5 \mathrm { m } ; v _ { \mathrm { v e h i c l e } } \cdot t _ { \mathrm { r e a c t } } + { \frac { v _ { \mathrm { V e h i c l e } } ^ { 2 } } { 2 \left| a \right| } } \right)
$$

**公式 8** (page 20):

$$
d _ { d } = d _ { \mathrm { c } } + 4 s \cdot v _ { \mathrm { V e h i c l e } } + ( 6 \mathrm { m } - I m p a c t ~ P o s i t i o n ) .
$$

### 图像（取前 6 张）

![Figure 1 Dynamic tests ](../_mineru_assets/ECE R151/4d6a9541a51eb31aaf498b72b4ad35974a20e6bc1a7e4c4e7c7a4df5bb94c1a7.jpg)  
*Figure 1 Dynamic tests * (page 14)

![Figure 2 Static tests ](../_mineru_assets/ECE R151/03f99f3e0bab56b13f39be49dc8e369cdb2cfa90e68e0c82e05373b060f7bd7b.jpg)  
*Figure 2 Static tests * (page 14)

![Figure 3 Impact location ](../_mineru_assets/ECE R151/dbd459c2f717a78be84d0bc535c1991acd2c21c0a2f5c5c903fa1de4c9cc4ecf.jpg)  
*Figure 3 Impact location * (page 15)

![图 page 17](../_mineru_assets/ECE R151/0dd0df3a9bacd92652aa5105462c3397d9a488d0db24afdf4760b65f268fe2b7.jpg)  

![图 page 17](../_mineru_assets/ECE R151/70f1c2a992ae5879c4a78d94e39707068e27fbcc499f0a4bb82c70c5ec0a46f4.jpg)  

![图 page 18](../_mineru_assets/ECE R151/be6be1902eca35dbef36b80f3321d1dd2b7375400f05c0518ee7712f4cdd3d1d.jpg)  

