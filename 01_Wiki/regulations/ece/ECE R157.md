---
reg_id: ECE R157
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to Automated
  Lane Keeping Systems
type: type/version
status: active
publication_date: '2021-03-04'
implementation_date_new_vehicle: '2021-01-22'
source: E/ECE/TRANS/505/Rev.3/Add.156
source_url: https://unece.org/transport/documents/2021/03/standards/un-regulation-no-157-automated-lane-keeping-systems
topics:
- Automated Lane Keeping System (ALKS)
- Automated Driving
- Vehicle Type Approval
- Functional Safety
- Operational Safety
- Human-Machine Interface (HMI)
- Data Storage System for Automated Driving (DSSAD)
- Cybersecurity
- Software Updates
scope: This Regulation applies to the type approval of vehicles of Category M1 with
  regard to their Automated Lane Keeping System (ALKS). ALKS is a system activated
  by the driver which controls the lateral and longitudinal movement of the vehicle
  for extended periods without further driver command, at speeds up to 60 km/h, on
  roads where pedestrians and cyclists are prohibited and which have a physical separation
  dividing opposite traffic.
tags:
- type/version
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\157\R157e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及标准机构（如 UNECE），无法核实。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及针对在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未提及替代法规。
_ocr_upgraded: mineru
_mineru_content_hash: 59f6f9aae5cb9216
_mineru_outputs_dir: outputs/59f6f9aae5cb9216
_mineru_blocks:
  tables: 9
  formulas: 1
  images: 8
_mineru_merged_at: '2026-04-25'
---

**UN Regulation No. 157 - Automated Lane Keeping Systems (ALKS)**

**Introduction**
This Regulation establishes the first regulatory step for an automated driving system in traffic. It aims to address the complexity of evaluating system safety through administrative provisions for type approval, technical requirements, audit and reporting provisions, and testing provisions. The ALKS is designed to perform the Dynamic Driving Task (DDT) instead of the driver when activated, within a specified Operational Design Domain (ODD).

**Key Definitions**
*   **Automated Lane Keeping System (ALKS):** A system activated by the driver which keeps the vehicle within its lane at speeds ≤ 60 km/h by controlling lateral and longitudinal movement for extended periods without further driver input.
*   **Dynamic Driving Task (DDT):** The control and execution of all longitudinal and lateral movements of the vehicle.
*   **Transition Demand:** A procedure to transfer the DDT from the system to the human driver.
*   **Minimum Risk Manoeuvre (MRM):** A procedure automatically performed by the system after a transition demand without driver response or in case of a severe failure, aimed at minimizing risks (e.g., bringing the vehicle to a standstill).
*   **Emergency Manoeuvre (EM):** A manoeuvre performed by the system in case of an imminent collision risk to avoid or mitigate a collision.
*   **Data Storage System for Automated Driving (DSSAD):** A system to record interactions between the ALKS and the driver.
*   **Operational Design Domain (ODD):** The specific operating conditions (environmental, geographic, traffic, etc.) under which the ALKS is designed to function.

**Core Technical Requirements**

1.  **System Safety and Fail-safe Response (Section 5):**
    *   The activated system must perform the DDT, manage all situations including failures, and be free of unreasonable risks to occupants and other road users.
    *   It must comply with traffic rules, avoid reasonably foreseeable and preventable collisions, and perform self-checks.
    *   Requirements for the DDT include lane keeping, speed control (max 60 km/h), maintaining a minimum following distance, and bringing the vehicle to a stop to avoid collisions.
    *   Specifies conditions for triggering and executing Emergency Manoeuvres and Minimum Risk Manoeuvres.

2.  **Human-Machine Interface (HMI) / Operator Information (Section 6):**
    *   Requires a **Driver Availability Recognition System** to detect driver presence, seatbelt fastening, and availability to take over control.
    *   Defines means for activation and deactivation of the ALKS, with the default status being 'off' at each new engine start cycle.
    *   Specifies conditions for system override by driver input (steering, braking, acceleration).
    *   Details information that must be provided to the driver: system status, failures, transition demands, MRM, and EM via optical, acoustic, and/or haptic signals.

3.  **Object and Event Detection and Response (OEDR) (Section 7):**
    *   The vehicle must be equipped with a sensing system capable of determining the driving environment and traffic dynamics.
    *   Specifies minimum forward detection range (≥46 m) and lateral detection range (covering adjacent lanes).
    *   Requires strategies to handle reduced detection range due to environmental conditions and effects of wear and ageing.

4.  **Data Storage System for Automated Driving (DSSAD) (Section 8):**
    *   Mandates a DSSAD to record specific occurrences (e.g., system activation/deactivation, transition demands, MRM/EM engagement, failures, collisions).
    *   Specifies minimum data elements to be recorded (occurrence flag, reason, date, timestamp, relevant software identification).
    *   Requires data to be retrievable, protected against manipulation, and available via a standardized interface (e.g., OBD port).

5.  **Cybersecurity and Software Updates (Section 9):**
    *   System effectiveness must not be adversely affected by cyber-attacks (compliance with UN R155).
    *   Software update procedures must be effective (compliance with UN R156).
    *   Provisions for software identification (R15X SWIN or alternative).

**Approval Process & Administrative Provisions**
*   **Application & Approval (Sections 3-4):** Describes the application process, granting of approval with an assigned number, and the use of an international approval mark.
*   **Modification & Conformity of Production (Sections 10-13):** Procedures for modifying an approved vehicle type, conformity of production checks, and penalties for non-conformity.

**Annexes**
*   **Annex 1:** Communication form for approval.
*   **Annex 2:** Arrangements of approval marks.
*   **Annex 3:** Reserved.
*   **Annex 4: Special requirements for the functional and operational safety aspects of ALKS.** This is a critical annex requiring manufacturers to provide extensive documentation (safety concept, system description, hazard analysis, validation plans) to demonstrate the system is free of unreasonable risk. It involves a process audit and product assessment by the Technical Service.
*   **Annex 5:** Test Specifications for ALKS (referenced throughout the regulation but content not fully provided in the excerpt).
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 12 个
> - 公式 1 个
> - 图像 28 个
> - 全文 Markdown 128,732 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 8)
<table><tr><td>Present speed of the ALKS vehicle</td><td>Minimum time gap</td><td>Minimum following distance</td></tr><tr><td>(km/h) (m/s)</td><td>(s)</td><td>(m)</td></tr><tr><td>7.2 2.0</td><td>1.0</td><td>2.0</td></tr><tr><td>10 2.78</td><td>1.1</td><td>3.1</td></tr><tr><td>20 5.56</td><td>1.2</td><td>6.7</td></tr><tr><td>30 8.33</td><td>1.3</td><td>10.8</td></tr><tr><td>40 11.11</td><td>1.4</td><td>15.6</td></tr><tr><td>50 13.89</td><td>1.5</td><td>20.8</td></tr><tr><td>60 16.67</td><td>1.6</td><td>26.7</td></tr></table>

#### 表 2 (page 24)
<table><tr><td>Country</td><td>Assessed</td><td>Comments on any restrictions</td></tr><tr><td>E1 Germany</td><td>Yes/No</td><td></td></tr><tr><td>E 2 France</td><td></td><td></td></tr><tr><td>E 3 Italy</td><td></td><td></td></tr><tr><td>E 4 Netherlands</td><td></td><td></td></tr><tr><td>E5 Sweden</td><td></td><td></td></tr><tr><td>E 6 Belgium</td><td></td><td></td></tr><tr><td>E 7 Hungary</td><td></td><td></td></tr><tr><td>E 8 Czech Republic</td><td></td><td></td></tr><tr><td>E 9 Spain</td><td></td><td></td></tr><tr><td>E 10 Serbia</td><td></td><td></td></tr><tr><td>E 11 United Kingdom</td><td></td><td></td></tr><tr><td>E 12 Austria</td><td></td><td></td></tr><tr><td>E 13 Luxembourg</td><td></td><td></td></tr><tr><td>E 14 Switzerland</td><td></td><td></td></tr><tr><td>E 16 Norway</td><td></td><td></td></tr><tr><td>E 17 Finland</td><td></td><td></td></tr><tr><td>E 18 Denmark</td><td></td><td></td></tr><tr><td>E 19 Romania</td><td></td><td></td></tr><tr><td>E 20 Poland</td><td></td><td></td></tr><tr><td>E 21 Portugal</td><td></td><td></td></tr><tr><td>E 22 Russian Federation</td><td></td><td></td></tr><tr><td>E 23 Greece</td><td></td><td></td></tr><tr><td>E 24 Ireland</td><td></td><td></td></tr><tr><td>E 25 Croatia</td><td></td><td></td></tr><tr><td>E 26 Slovenia</td><td></td><td></td></tr><tr><td>E 27 Slovakia</td><td></td><td></td></tr><tr><td>E 28 Belarus</td><td></td><td></td></tr></table>

#### 表 3 (page 25)
<table><tr><td>Country</td><td>Assessed</td><td>Comments on any restrictions</td></tr><tr><td>E 29 Estonia</td><td></td><td></td></tr><tr><td>E 30 Republic of Moldova</td><td></td><td></td></tr><tr><td>E 31 Bosnia and</td><td></td><td></td></tr><tr><td>Herzegovina</td><td></td><td></td></tr><tr><td>E 32 Latvia</td><td></td><td></td></tr><tr><td>E 34 Bulgaria</td><td></td><td></td></tr><tr><td>E 35 Kazakhstan</td><td></td><td></td></tr><tr><td>E 36 Lithuania</td><td></td><td></td></tr><tr><td>E 37 Turkey</td><td></td><td></td></tr><tr><td>E 39 Azerbaijan</td><td></td><td></td></tr><tr><td>E 40 North Macedonia</td><td></td><td></td></tr><tr><td>E 43 Japan</td><td></td><td></td></tr><tr><td>E 45 Australia</td><td></td><td></td></tr><tr><td>E 46 Ukraine</td><td></td><td></td></tr><tr><td>E 47 South Africa</td><td></td><td></td></tr><tr><td>E 48 New Zealand</td><td></td><td></td></tr><tr><td>E 49 Cyprus</td><td></td><td></td></tr><tr><td>E 50 Malta</td><td></td><td></td></tr><tr><td>E 51 Republic of Korea</td><td></td><td></td></tr><tr><td>E 52 Malaysia</td><td></td><td></td></tr><tr><td>E 53 Thailand</td><td></td><td></td></tr><tr><td>E 54 Albania</td><td></td><td></td></tr><tr><td>E 55 Armenia</td><td></td><td></td></tr><tr><td>E 56 Montenegro</td><td></td><td></td></tr><tr><td>E 57 San Marino</td><td></td><td></td></tr><tr><td>E 58 Tunisia</td><td></td><td></td></tr><tr><td>E 60 Georgia</td><td></td><td></td></tr><tr><td>E 62 Egypt</td><td></td><td></td></tr><tr><td>E 63 Nigeria</td><td></td><td></td></tr><tr><td>E 64 Pakistan</td><td></td><td></td></tr></table>

#### 表 4 (page 26)
<table><tr><td>157</td><td>002439</td></tr><tr><td>31</td><td>021628</td></tr></table>

#### 表 5 (page 42)
**Table 1 Performance model factors for vehicles **

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Factors</td></tr><tr><td rowspan=2 colspan=1>Risk perception point</td><td rowspan=1 colspan=1>Lane change (cuting in,cutting out)</td><td rowspan=1 colspan=1>Deviation of the center of a vehicle over0.375m from the center of the driving lane(derived from research by Japan)</td></tr><tr><td rowspan=1 colspan=1>Deceleration</td><td rowspan=1 colspan=1>Deceleration ratio of preceding vehicle andfollowing distance of ego vehicle</td></tr><tr><td rowspan=1 colspan=2>Risk evaluation time</td><td rowspan=1 colspan=1>0.4 seconds(from research by Japan)</td></tr><tr><td rowspan=1 colspan=2>Time duration from having finished perception untilstarting deceleration</td><td rowspan=1 colspan=1>0.75 seconds(common data in Japan)</td></tr><tr><td rowspan=1 colspan=2>Jerking time to full deceleration (road friction 1.0)</td><td rowspan=1 colspan=1>0.6 seconds to 0.774G(from experiments by NHTSA and Japan)</td></tr><tr><td rowspan=1 colspan=2>Jerking time to full deceleration (after full wrap ofego vehicle and cut-in vehicle,road friction 1.0)</td><td rowspan=1 colspan=1>0.6 seconds to 0.85G(derived from UN Regulation No.152 onAEBS)</td></tr></table>

#### 表 6 (page 44)
**Table 2 Additional parameters **

<table><tr><td>Operating conditions</td><td>Roadway</td><td>Number of lanes = The number of parallel and adjacent lanes in the same direction of travel</td></tr><tr><td rowspan="2"></td><td></td><td>Roadway grade = The grade of the roadway in the area of test Roadway condition = the condition of the roadway (dry, wet, icy,snow, new, worn) including coefficient of friction Lane markings = the type, colour, width, visibility of</td></tr><tr><td>Environmental conditions</td><td>Lighting conditions = The amount of light and direction (ie,day, night, sunny, cloudy) Weather conditions = The amount, type and intensity of wind, rain, snow etc.</td></tr><tr><td rowspan="4">Initial condition</td><td rowspan="2">Initial velocity</td><td>Ve0 = Ego vehicle</td></tr><tr><td>Vo0 =Leading vehicle in lane or in adjacent lane</td></tr><tr><td rowspan="2">Initial distance</td><td>VfO = Vehicle in front of leading vehicle in lane</td></tr><tr><td>dx0 = Distance in Longitudinal direction between the front end of the ego vehicle and the rear end of the leading vehicle in ego vehicle's lane or in adjacent lane</td></tr><tr><td></td><td></td><td>dyO = Inside Lateral distance between outside edge line of ego vehicle in parallel to the vehicle's median longitudinal plane within lanes and outside edge line of leading vehicle in parallel to the vehicle's median longitudinal plane in adjacent lines.</td></tr><tr><td colspan="1" rowspan="5"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">dy0_f = Inside Lateral distance between outside edgeline of leading vehicle in parallel to the vehicle'smedian longitudinal plane within lanes and outsideedge line of vehicle in front of the leading vehicle inparallel to the vehicle's median longitudinal plane inadjacent lines.</td></tr><tr><td colspan="1" rowspan="4"></td><td colspan="1" rowspan="1">dx0_f = Distance in longitudinal direction betweenfront end of leading vehicle and rear end of vehicle infront of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">dfy = Width of vehicle in front of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">doy = Width of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">dox =Length of the leading vehicle</td></tr><tr><td colspan="1" rowspan="3">Vehiclemotion</td><td colspan="1" rowspan="1">Lateral motion</td><td colspan="1" rowspan="1">Vy =Leading vehicle lateral velocity</td></tr><tr><td colspan="1" rowspan="2">Deceleration</td><td colspan="1" rowspan="1">Gx_max = Maximum deceleration of the leadingvehicle in G</td></tr><tr><td colspan="1" rowspan="1">dG/dt = Deceleration rate (Jerk) of the leadingvehicle</td></tr></table>

#### 表 7 (page 45)
#### 表 8 (page 45)
**Figure 5 Visualisation **

<table><tr><td>Cut in</td><td>Ego idx0 ￥购 VeO dyot VoO Challenging vehicle</td><td></td></tr><tr><td></td><td>Ego VoO Challenging vehicle dx0 回 /dx0 口 VeO VfO</td><td></td></tr><tr><td></td><td>Ego dx0 Vo0 VeO Gx_max Challenging dG/dt vehicle</td><td></td></tr></table>

#### 表 9 (page 46)
<table><tr><td rowspan=4 colspan=1>Initialcondition</td><td rowspan=2 colspan=1>Initialvelocity</td><td rowspan=1 colspan=1>Ve0      Ego vehicle velocity</td></tr><tr><td rowspan=1 colspan=1>Ve0-Vo0Relative velocity</td></tr><tr><td rowspan=2 colspan=1>Initialdistance</td><td rowspan=1 colspan=1>dyo      Latteral distancex</td></tr><tr><td rowspan=1 colspan=1>dxo      Longitudinal distance</td></tr><tr><td rowspan=1 colspan=1>Vehiclemotion</td><td rowspan=1 colspan=1>Lateralmotion</td><td rowspan=1 colspan=1>vy        Lateral velocity</td></tr></table>

#### 表 10 (page 57)
**(Data sheet image) **

<table><tr><td rowspan=5 colspan=1>Ego        dx0           VoO口      ←VeO          Gx_max ChallengingdG/dt       vehicle</td><td rowspan=3 colspan=1>Initialcondition</td><td rowspan=2 colspan=1>Initialvelocity</td><td rowspan=1 colspan=1>Ve0        Ego vehicle velocity</td></tr><tr><td rowspan=1 colspan=1>Vo0        Leading vehicle velocity1</td></tr><tr><td rowspan=1 colspan=1>Initialdistance</td><td rowspan=1 colspan=1>dx0        Longitudinal distance²</td></tr><tr><td rowspan=2 colspan=1>Vehiclemotion</td><td rowspan=2 colspan=1>Deceleration</td><td rowspan=1 colspan=1>Gx_max Maximum deceleration G</td></tr><tr><td rowspan=1 colspan=1>dG/dt     Deceleration rate3</td></tr></table>

### 公式（取前 1 个）

**公式 1** (page 9):

$$
T T C L a n e I n t r u s i o n > v r e l / ( 2 \cdot 6 \mathrm { m } / \mathrm { s } ^ { 2 } ) + 0 . 3 5 s
$$

### 图像（取前 8 张）

![图 page 12](../_mineru_assets/ECE R157/712cc0a43cad5fcdfbf4fd5a64c656692cd5edbaff29def15f154f107deb4fef.jpg)  

![Example1. ](../_mineru_assets/ECE R157/19fee754117a6a9cfb87bc552202728e243b4ef57bddbcf36087c861162f353a.jpg)  
*Example1. * (page 16)

![Example2. ](../_mineru_assets/ECE R157/a291b3723ab215a3858991d359e919028d7d979310dd34b9c9f1f17baafa7889.jpg)  
*Example2. * (page 16)

![图 page 26](../_mineru_assets/ECE R157/9f361d476b9ea265fb349868afd092ace606f209d10025c9901e76ac77671052.jpg)  

![图 page 26](../_mineru_assets/ECE R157/072a626f155843190034430211699e1ff35e9ffc89ea672a4f2d96153a5683d5.jpg)  

![Figure 1 Skilled human performance model ](../_mineru_assets/ECE R157/6ddb1c1dd1c756a1cfcbd2bdcba72ef8979910c40f64d35ab246a3c321c150a2.jpg)  
*Figure 1 Skilled human performance model * (page 42)

![Figure 2 Driver model for thecut-in scenario ](../_mineru_assets/ECE R157/ba835d36a56ffbf069e9382afd388ae523fe36a40103e889240fa85b02def3a2.jpg)  
*Figure 2 Driver model for thecut-in scenario * (page 43)

![Figure 3 Cut in scenario ](../_mineru_assets/ECE R157/b3e9a0005d74788c667bafb7996f865bb72e79792195ed0edb76b57e887a362c.jpg)  
*Figure 3 Cut in scenario * (page 43)

