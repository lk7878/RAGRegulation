---
reg_id: ECE R79 Rev4
region: ece
type: type/version
title: Uniform provisions concerning the approval of vehicles with regard to steering
  equipment
status: active
publication_date: 2018-11-07
implementation_date_new_vehicle: 2018-10-18
source_file: R079r4e.pdf
tags:
- type/version
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\79\R079r4e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中未明确提及标准机构名称（如 UNECE），无法核实。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中未提及针对在用车辆的单独实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中未提及本版本替代了哪个旧版本。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A 的摘要中未提取具体技术要求的数值限值，B 提供的原文部分也未包含具体限值。
_ocr_upgraded: mineru
_mineru_content_hash: b1465ae209267ff7
_mineru_outputs_dir: outputs/b1465ae209267ff7
_mineru_blocks:
  tables: 7
  formulas: 2
  images: 6
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 79 (Revision 4)

**Uniform provisions concerning the approval of vehicles with regard to steering equipment**

**Addendum 78: UN Regulation No. 79, Revision 4**
Incorporating all valid text up to:
*   Supplement 1 to the 02 series of amendments – Date of entry into force: 18 October 2018
*   03 series of amendments – Date of entry into force: 18 October 2018

## Introduction
This Regulation establishes uniform provisions for the layout and performance of steering systems fitted to road vehicles. It has been amended to account for new technologies, including systems without a positive mechanical connection between the steering control and the road wheels.

The Regulation defines **Advanced Driver Assistance Steering Systems (ADASS)**, which assist the driver while the driver remains in primary control. These can include:
*   **Automatically Commanded Steering Functions (ACSF)**: e.g., lane guidance, lane keeping, parking assistance.
*   **Corrective Steering Functions (CSF)**: e.g., lane departure avoidance, stability improvement.
*   **Emergency Steering Functions (ESF)**: automatically steers to avoid or mitigate a collision.

The driver must be able to override these functions at all times. The Regulation does **not** permit the approval of **Autonomous Steering Systems** (controlled by external signals without a driver) or positive trailer steering via electrical control from the towing vehicle (pending future standards).

## Scope
*   Applies to steering equipment of vehicles of categories M, N, and O.
*   **Does not apply to:**
    *   Purely pneumatic steering transmission.
    *   Autonomous Steering Systems.
    *   ACSF of Category B2, D, or E until specific provisions are introduced.

## Key Definitions
*   **Steering Equipment**: All equipment to determine vehicle direction, comprising steering control, steering transmission, steered wheels, and energy supply.
*   **Steering Transmission**: Components linking steering control to road wheels, divided into **control transmission** (signals) and **energy transmission** (power).
*   **Advanced Driver Assistance Steering System (ADASS)**: System assisting the driver, who remains in primary control. Includes ACSF and CSF.
*   **Automatically Commanded Steering Function (ACSF)**: Function where steering actuation results from automatic evaluation of on-board signals.
    *   **Category A**: Low-speed/parking manoeuvring assistance (≤ 10 km/h).
    *   **Category B1**: Lane keeping assistance.
    *   **Category B2**: Extended lane keeping without further driver confirmation *(provisions reserved)*.
    *   **Category C**: Single lateral manoeuvre (e.g., lane change) on driver command.
    *   **Category D**: Indicates possible manoeuvre, performs only after driver confirmation.
    *   **Category E**: Continuously determines and performs manoeuvres without further driver confirmation *(provisions reserved)*.
*   **Corrective Steering Function (CSF)**: Function that temporarily changes steering angle to compensate for side force changes, improve stability, or correct lane departure.
*   **Emergency Steering Function (ESF)**: Function that automatically detects a potential collision and activates steering to avoid/mitigate it for a limited duration.
*   **Remote Controlled Parking (RCP)**: An ACSF Category A function actuated by remote control in close proximity to the vehicle.
*   **Full-power Steering Equipment**: Steering forces provided solely by one or more energy supplies.
*   **Power Assisted Steering Equipment**: Steering forces from both driver muscular effort and energy supply.

## Construction Provisions
### General Requirements
*   Must ensure easy and safe handling up to maximum design speed, with a tendency to self-centre.
*   Direction of steering control operation must correspond to intended vehicle direction change, with a continuous relationship between control deflection and steering angle (exceptions for ACSF, CSF, ESF, ASE, and certain full-power steering conditions).
*   Must withstand normal operational stresses.
*   Effectiveness must not be adversely affected by magnetic/electric fields (comply with UN R10).
*   ADASS must not deteriorate basic steering system performance and must be overrideable by driver deliberate action.
*   **CSF Requirements**:
    *   Optical warning signal for every intervention (≥1s or duration of intervention).
    *   Acoustic warning for prolonged interventions or consecutive interventions within 180s without driver steering input.
    *   Override force ≤ 50 N.
*   **ESF Requirements**:
    *   Only intervenes when collision risk detected.
    *   Must monitor driving environment when active.
    *   Automatic manoeuvre must not lead vehicle to leave road or cross lane markings (with exceptions).
    *   Must not lead to collision with another road user.
    *   Optical and acoustic/haptic warning at start of intervention.
    *   System failure optical warning.
    *   Override force ≤ 50 N.
*   Steered wheels shall not be solely the rear wheels (except for semi-trailers).
*   Control systems subject to **Annex 6** (safety aspects of complex electronic control systems).

### Failure Provisions & Performance
*   Parts amply dimensioned, accessible for maintenance, and with safety features equivalent to other essential components are not considered liable to breakage.
*   Requirements for straight-line travel, direction correspondence, and self-centring must also be satisfied with a steering equipment failure (if vehicle can still be driven at required speeds).
*   Any failure in a non-purely mechanical transmission must be clearly indicated to the driver.
*   If steering shares an energy source with braking and that source fails, **steering has priority**. Braking performance on first subsequent application must meet specified minimums (see Annex 3).
*   **Power Assisted Steering**: Engine stop or transmission failure must not cause immediate steering angle change. Must meet performance requirements for system with failure at speeds >10 km/h.
*   **Full-power Steering**:
    *   Vehicle must not be driven indefinitely >10 km/h with a fault requiring a warning signal.
    *   Control transmission failure must still allow steering at intact system performance level.
    *   Energy source failure must allow at least 24 "figure of eight" manoeuvres at intact performance level.
    *   Energy transmission failure must not cause immediate angle change; after 25 "figure of eight" manoeuvres, must meet requirements for system with failure.

### Warning Signals
*   Any non-mechanical fault impairing steering function must be signalled to driver.
*   Optical signals must be visible by daylight, distinguishable, and verifiable from driver's seat.
*   Acoustic signals can be continuous/intermittent sound or vocal information (in market language(s)).
*   If steering shares energy source with other systems, warning required when stored energy drops to a level liable to increase steering effort.
*   **Full-power steering** must provide:
    *   Red warning signal for failures within main steering equipment.
    *   Yellow warning signal for other electrically detected defects.
*   Warning if additional steering equipment is in operation or not returned to normal position.

### Provisions for ACSF
All ACSF are subject to Annex 6 requirements.
*   **Category A (e.g., Parking Assist/RCP)**:
    *   Operates only ≤ 10 km/h (+2 km/h tolerance).
    *   Activated by deliberate driver action.
    *   Must be deactivatable by driver at any time.
    *   If includes acceleration/braking control, must detect obstacles and stop to avoid collision.
    *   System operational status must be indicated to driver.
    *   **RCP-specific**: Requires continuous driver actuation of remote; vehicle stops if actuation interrupted, signal lost, or door/trunk opened; parking brake engages automatically at final position; max operating range ≤ 6 m; protected against unauthorized activation.
*   **Category B1 (Lane Keeping)**:
    *   Must ensure vehicle does not cross lane markings within specified lateral acceleration limits (see tables in regulation).
    *   Driver must be able to activate/deactivate. Deactivation must be possible by single action.
    *   Override force ≤ 50 N.
    *   Specified max lateral acceleration (ay_smax) and lateral jerk limits defined.
    *   Optical signals for active and standby modes.
    *   Warning when system reaches boundary conditions (e.g., max lateral acceleration) and tyre starts to cross lane marking.
    *   **Driver hands-on detection**: Optical warning after ≤15s of hands-off, red pictorial/acoustic warning after ≤30s, system deactivation after ≤30s of acoustic warning.
*   **Category C (Lane Change)**:
    *   Vehicle must also be equipped with a compliant ACSF of Category B1.
    *   Default status is 'off' at each new engine start/run cycle.
    *   Activation (standby) only possible by driver deliberate action on specific road types (e.g., physically separated highways).
    *   Override force ≤ 50 N.
    *   Lateral acceleration and jerk limits during manoeuvre.
    *   Specific Human-Machine Interface (HMI) requirements for status, procedure, suppression, and failure.
    *   **Lane Change Procedure**: Initiated by driver activating direction indicator; timing constraints for start and completion of manoeuvre; automatic resumption of Category B1 function afterwards.
    *   Procedure suppression conditions defined (e.g., critical situation, driver override, boundaries reached).
    *   **Critical situation** defined based on relative speed/distance to approaching vehicle in target lane.
    *   Must detect approaching vehicles from rear up to a declared minimum distance (≥55 m). Minimum operation speed calculated based on this distance.
    *   Sensor blindness detection required.

## Test Provisions
### General
*   Tests on level surface with good adhesion.
*   Vehicle loaded to technically permissible maximum mass and maximum load on steered axle(s).
*   For systems using electrical energy, tests under simulated load of all essential shared systems (lighting, wipers, engine management, braking).

### Motor Vehicles
*   **Curve Exit**: Must be able to leave a 50m radius curve at a tangent without unusual vibration at specified speeds (e.g., 50 km/h for M1, 40 km/h for M2/M3/N1/N2/N3).
*   **Self-centring**: When driven in a circle at ≥10 km/h with wheels at ~half lock, turning circle must remain same or become larger if steering control released.
*   **Steering Effort & Time**: Measured at 10 km/h from straight ahead into a spiral to achieve specified turning radius. Maximum permitted effort and time defined for intact system and system with a failure (see table in regulation).

### Trailers
*   **Straight-line running**: Must travel without excessive deviation/vibration at 80 km/h (or max speed if lower).
*   **Steady-state turn**: Circle described by trailer at 25 km/h must not exceed circle at 5 km/h by more than 0.7 m (25m radius turn).
*   **Tangent departure**: No part of trailer shall move >0.5m beyond tangent when leaving a 25m circle at 25 km/h.
*   **Swept annular width**: With a fault, increase in swept width ≤15% compared to intact system, with no increase in outer radius.

## Annexes
1.  **Communication**: Model for approval communication form.
2.  **Arrangements of Approval Marks**: Examples of approval mark placement.
3.  **Braking Performance for Shared Energy Source**: Specifies minimum braking performance required if steering shares energy source with brakes and a failure occurs.
4.  **Additional Provisions for Auxiliary Steering Equipment (ASE)**: Specific requirements and tests for vehicles equipped with ASE.
5.  **Provisions for Trailers with Hydraulic Steering Transmission**: Additional requirements for hydraulic lines, pressure protection.
6.  **Special Requirements for Safety Aspects of Complex Electronic Control Systems**: Defines documentation, fault strategy, and verification requirements for electronic systems covered by this regulation.
7.  **Special Provisions for Powering Trailer Steering from Towing Vehicle**: Requirements for electrical energy supply connections.
8.  **Test Requirements for Corrective and Automatically Commanded Steering Functions**: Specifies vehicle tests for CSF and ACSF (Categories A, B1, C, ESF).

## Administrative Provisions
*   **Approval**: Granted if vehicle meets requirements. Approval number assigned, with first two digits indicating series of amendments.
*   **Approval Mark**: Circle with "E" and country number, plus regulation number and approval number.
*   **Conformity of Production**: Must comply with 1958 Agreement procedures. Records kept for up to 10 years after production discontinuation.
*   **Modifications & Extensions**: Notifications and procedures for changes to approved type.
*   **Transitional Provisions**: Defined for acceptance of approvals under 02 and 03 series of amendments.
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 7 个
> - 公式 2 个
> - 图像 6 个
> - 全文 Markdown 154,828 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 7 个）

#### 表 1 (page 20)
**Table 1 For vehicles of category M1, N1 **

<table><tr><td rowspan=1 colspan=1>Speed range</td><td rowspan=1 colspan=1>10 - 60 km/h</td><td rowspan=1 colspan=1>&gt; 60-100km/h</td><td rowspan=1 colspan=1>&gt; 100-130km/h</td><td rowspan=1 colspan=1>&gt;130km/h</td></tr><tr><td rowspan=1 colspan=1>Maximum value for thespecified maximum lateralacceleration</td><td rowspan=1 colspan=1>3 m/s²</td><td rowspan=1 colspan=1>3 m/s²</td><td rowspan=1 colspan=1>3 m/s²</td><td rowspan=1 colspan=1>3 m/s²</td></tr><tr><td rowspan=1 colspan=1>Minimum value for thespecified maximum lateralacceleration</td><td rowspan=1 colspan=1>0 m/s²</td><td rowspan=1 colspan=1>0.5 m/s²</td><td rowspan=1 colspan=1>0.8 m/s²</td><td rowspan=1 colspan=1>0.3 m/s²</td></tr></table>

#### 表 2 (page 20)
**For vehicles of category $\mathbf { M } _ { 2 } , \mathbf { M } _ { 3 } , \mathbf { N } _ { 2 } , \mathbf { N } _ { 3 }$ **

<table><tr><td rowspan=1 colspan=1>Speed range</td><td rowspan=1 colspan=1>10 - 30 km/h</td><td rowspan=1 colspan=1>&gt;30-60km/h</td><td rowspan=1 colspan=1>&gt; 60 km/h</td></tr><tr><td rowspan=1 colspan=1>Maximum value for thespecified maximum lateralacceleration</td><td rowspan=1 colspan=1>2.5 m/s²</td><td rowspan=1 colspan=1>2.5 m/s²</td><td rowspan=1 colspan=1>2.5 m/s²</td></tr><tr><td rowspan=1 colspan=1>Minimum value for thespecified maximum lateralacceleration</td><td rowspan=1 colspan=1>0 m/s²</td><td rowspan=1 colspan=1>0.3 m/s²</td><td rowspan=1 colspan=1>0.5 m/s²</td></tr></table>

#### 表 3 (page 29)
**Table 2 Steering control effort requirements **

<table><tr><td rowspan=1 colspan=1>VehicleCategory</td><td rowspan=1 colspan=3>INTACT</td><td rowspan=1 colspan=3>WITHAFAILURE</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Maximumeffort(daN)</td><td rowspan=1 colspan=1>Time(s)</td><td rowspan=1 colspan=1>Turningradius(m)</td><td rowspan=1 colspan=1>MaximumEffort(daN)</td><td rowspan=1 colspan=1>Time(s)</td><td rowspan=1 colspan=1>TurningRadius(m)</td></tr><tr><td rowspan=1 colspan=1>M1</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>M2</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>M3</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>12 **</td><td rowspan=1 colspan=1>45 *</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>N1</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>N2</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>N3</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>12 **</td><td rowspan=1 colspan=1>45 *</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>20</td></tr></table>

#### 表 4 (page 35)
<table><tr><td>79</td><td>032439</td></tr><tr><td>31</td><td>021628</td></tr></table>

#### 表 5 (page 36)
**Table 3 **

<table><tr><td rowspan=1 colspan=2>Category</td><td rowspan=1 colspan=1>V (km/h)</td><td rowspan=1 colspan=1>Service braking (m/s2)</td><td rowspan=1 colspan=1>F (daN)</td></tr><tr><td rowspan=1 colspan=2>M1</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>6.43</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=2>M2 and M3</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>70</td></tr><tr><td rowspan=2 colspan=1>Nab</td><td rowspan=1 colspan=1>(i)</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>70</td></tr><tr><td rowspan=1 colspan=1>(i)</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>6.43</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=2>N2 and N3</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>70</td></tr></table>

#### 表 6 (page 37)
**Table 4 Secondary and residual efficiency **

<table><tr><td rowspan=1 colspan=2>Category</td><td rowspan=1 colspan=1>V (km/h)</td><td rowspan=1 colspan=1>Secondary braking (m/s2)</td><td rowspan=1 colspan=1>Residual braking (m/s2)</td></tr><tr><td rowspan=1 colspan=2>M1</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>2.44</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=2>M2 and M3</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=2 colspan=1>Na, b</td><td rowspan=1 colspan=1>(i)</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=1>(ii)</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>2.44</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=2>N2</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>1.3</td></tr><tr><td rowspan=1 colspan=2>N3</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>2.2</td><td rowspan=1 colspan=1>1.3</td></tr></table>

#### 表 7 (page 39)
**Table 5 **

<table><tr><td rowspan=1 colspan=1>Vehicle category</td><td rowspan=1 colspan=1>R3</td><td rowspan=1 colspan=1>v12</td></tr><tr><td rowspan=1 colspan=1>M and N1</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>80</td></tr><tr><td rowspan=1 colspan=1>M2 and N2</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>M3 and N3</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>45</td></tr></table>

### 公式（取前 2 个）

**公式 1** (page 25):

$$
\mathbf { S } _ { c r i t i c a l } = ( \nu _ { r e a r } - \nu _ { A C S F } ) * { } t _ { B } + ( \nu _ { r e a r } - \nu _ { A C S F } ) ^ { 2 } / ( 2 * a ) + \nu _ { A C S F } * { } t _ { G }
$$

**公式 2** (page 25):

$$
V _ { S m i n } = \ a * ( t _ { B } - t _ { G } ) + v _ { a p p } - \sqrt { a ^ { 2 } * ( t _ { B } - t _ { G } ) ^ { 2 } - 2 * a * ( v _ { a p p } * t _ { G } - S _ { r e a r } ) }
$$

### 图像（取前 6 张）

![Example1. ](../_mineru_assets/ECE R79 Rev4/38721b12b63aa5d8546b55056ca04fa31db18a0859f2797b97bd2bb31b25d9b5.jpg)  
*Example1. * (page 21)

![Example 2. ](../_mineru_assets/ECE R79 Rev4/4f0e95e27ac4d2071cf0c39ac56ac7e709803316fcaeefd8a3469f9961339d8e.jpg)  
*Example 2. * (page 21)

![图 page 26](../_mineru_assets/ECE R79 Rev4/2459243797b6ea7c9fb9567dab6199c048c2edefa06fb2beb4794a6a4162e3dc.jpg)  

![图 page 33](../_mineru_assets/ECE R79 Rev4/ff8b572a9f85aee5fe078ba60b260d192ff1c88f3b16db83025613b0ced20cd7.jpg)  

![图 page 35](../_mineru_assets/ECE R79 Rev4/da0af1fe389a757d97b71f64a890781fdb852253455e022a285604a1033dc822.jpg)  

![图 page 35](../_mineru_assets/ECE R79 Rev4/c5afeb3a40c33ad50a25cd0b68ec1384a9ef45209fb972c973c9d080e1444a99.jpg)  

