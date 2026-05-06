---
reg_id: ECE R100 Rev3
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to specific
  requirements for the electric power train
type: type/version
status: active
standard_body: UNECE
publication_date: 2022-03-23
version: Revision 3
amendments:
- series: 2
  supplement: 1
  entry_force: 2014-06-10
- series: 2
  supplement: 2
  entry_force: 2016-01-29
- series: 2
  supplement: 3
  entry_force: 2016-06-18
- series: 2
  supplement: 4
  entry_force: 2019-05-28
- series: 3
  entry_force: 2021-06-09
scope: '**Part I:** Safety requirements for the electric power train of road vehicles
  of categories M and N1 (maximum design speed > 25 km/h), excluding vehicles permanently
  connected to the grid. Excludes post-crash safety and high voltage components not
  galvanically connected to the high voltage bus.

  **Part II:** Safety requirements for the Rechargeable Electrical Energy Storage
  System (REESS) of road vehicles of categories M and N equipped with electric power
  train, excluding vehicles permanently connected to the grid. Excludes batteries
  primarily for starting, lighting, or auxiliary systems.

  '
keywords:
- electric vehicle
- EV
- high voltage
- electrical safety
- REESS
- battery safety
- isolation resistance
- direct contact
- indirect contact
- thermal runaway
- thermal propagation
- hydrogen emissions
- type approval
- UN Regulation
file_path: 国外法规\ECE标准\标准法规-UNECE\81~120\100\R100r3e.pdf
source_ocr: true
tags:
- type/version
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\100\R100r3e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 中未提及新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及在用车型实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及替代的旧版本。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: 提供的 B 文本中未包含具体的技术要求限值。
_ocr_upgraded: mineru
_mineru_content_hash: 509127760edf2347
_mineru_outputs_dir: outputs/509127760edf2347
_mineru_blocks:
  tables: 6
  formulas: 10
  images: 8
_mineru_merged_at: '2026-04-22'
---

# Regulation No. 100 (Revision 3)

## 1. Scope
1.1. **Part I:** Safety requirements with respect to the electric power train of road vehicles of categories M and N1, with a maximum design speed exceeding 25 km/h, equipped with electric power train, excluding vehicles permanently connected to the grid.
    *Part I does not cover:*
    (a) Post-crash safety requirements.
    (b) High voltage components and systems not galvanically connected to the high voltage bus.
1.2. **Part II:** Safety requirements with respect to the Rechargeable Electrical Energy Storage System (REESS) of road vehicles of categories M and N equipped with electric power train, excluding vehicles permanently connected to the grid.
    *Part II does not apply to a battery whose primary use is to supply power for starting the engine and/or lighting and/or other vehicle auxiliaries' systems.*

## 2. Definitions
Key definitions include:
*   **Active driving possible mode:** Vehicle mode where accelerator pedal application or brake release causes propulsion.
*   **Cell:** Single encased electrochemical unit.
*   **Direct/Indirect contact:** Contact with high voltage live parts / exposed conductive parts.
*   **Electric power train:** Electrical circuit including traction motor(s), REESS, converters, wiring, and charging coupling system.
*   **High Voltage:** > 60 V and ≤ 1500 V DC or > 30 V and ≤ 1000 V AC rms.
*   **Protection degree IPXXB/IPXXD:** Protection against contact using a Jointed Test Finger / Test Wire.
*   **Rechargeable Electrical Energy Storage System (REESS):** Rechargeable energy storage system for electrical propulsion (excludes starter batteries).
*   **Thermal runaway:** Uncontrolled increase of cell temperature.
*   **Thermal propagation:** Sequential thermal runaway within a REESS triggered by a single cell.
*   **Venting:** Release of excessive internal pressure intended to preclude rupture/explosion.
*   **Working voltage:** Highest rms voltage between any conductive parts under normal operation.

## 3. Application for Approval
*   **3.1. Part I (Vehicle):** Submitted by vehicle manufacturer with detailed description of electric power train and evidence of REESS compliance.
*   **3.2. Part II (REESS):** Submitted by REESS manufacturer with detailed description of REESS safety.
*   **3.3:** Type Approval Authority verifies conformity of production arrangements.

## 4. Approval
*   Assigns approval number.
*   Communication via forms in Annex 1.
*   **Approval mark:** Circle with "E" and country number, Regulation number "100R", approval number. For REESS, includes "ES".
*   Mark must be legible, indelible, on vehicle data plate or REESS major element.

## 5. Part I: Vehicle Requirements for Electric Power Train
### 5.1. Protection Against Electrical Shock
Applies to high voltage buses and galvanically connected components when not connected to external supplies.
*   **5.1.1. Direct Contact:** Live parts must be protected (IPXXD inside passenger/luggage compartment, IPXXB elsewhere). Barriers/enclosures require tools or operator control to open. Connectors may be separated without tools if they remain protected, have a locking mechanism, or voltage drops to safe levels within 1s. Specific exemptions for roof-mounted charging devices on certain vehicle categories.
*   **5.1.2. Indirect Contact:** Exposed conductive parts must be securely connected to electrical chassis. Resistance < 0.1 Ω (0.2 A current). For vehicles charging from grounded external supply, a device to connect chassis to earth ground is required.
*   **5.1.3. Isolation Resistance:**
    *   **5.1.3.1. Separate DC/AC buses:** ≥ 100 Ω/V for DC, ≥ 500 Ω/V for AC.
    *   **5.1.3.2. Combined DC/AC buses:** ≥ 500 Ω/V, or ≥ 100 Ω/V if AC buses have specific robust protections.
    *   **5.1.3.3. Fuel cell vehicles:** Require on-board isolation resistance monitoring system with driver warning (< 100 Ω/V).
    *   **5.1.3.4. Charging coupling system:** Must meet isolation requirements when disconnected.
*   **5.1.4. Protection Against Water Effects:** Vehicle must maintain isolation resistance after water exposure. Compliance can be shown via documentation/design verification (Annex 7A), physical vehicle test (Annex 7B), or via an isolation resistance monitoring system with driver warning.

### 5.2. Rechargeable Electrical Energy Storage System (REESS)
*   **5.2.1:** REESS must be type-approved per Part II and installed per instructions, OR the vehicle's REESS system must comply with Part II requirements.
*   **5.2.2:** Ventilation required for open-type traction batteries to prevent hydrogen accumulation.
*   **5.2.3:** Warning to driver in active driving mode upon REESS failure (paras. 6.13-6.15).
*   **5.2.4:** For pure electric vehicles, warning for low REESS state of charge.

### 5.3. Preventing Accidental or Unintended Vehicle Movement
*   **5.3.1:** Indication when first entering "active driving possible mode".
*   **5.3.2:** Signal if vehicle left in active driving mode (mandatory for large M2/M3 vehicles when driver leaves seat).
*   **5.3.3:** Propulsion impossible while vehicle connector is physically connected for charging.
*   **5.3.4:** Drive direction state identifiable to driver.

### 5.4. Determination of Hydrogen Emissions
*   Applies to vehicles with open-type traction batteries.
*   Test per Annex 8.
*   **Normal charge:** < 125 g/5h or < 25 x t g during t (hours).
*   **Charge with charger failure:** < 42 g, limited to 30 min.
*   Charging must be automatic, with permanent indication of important failures.

## 6. Part II: Requirements for REESS Safety
General requirement: Apply procedures in Annex 9.
*   **6.2. Vibration:** Test per Annex 9A. No leakage, rupture (HV), venting, fire, explosion. Post-test isolation ≥ 100 Ω/V.
*   **6.3. Thermal Shock & Cycling:** Test per Annex 9B. Same acceptance criteria as 6.2.
*   **6.4. Mechanical Impact:**
    *   **6.4.1. Mechanical Shock:** Vehicle-based (UN R94/R137 frontal, R95 side) or component-based (Annex 9C). No fire, explosion. Limited electrolyte leakage allowed. REESS must remain attached/contained. Post-test isolation ≥ 100 Ω/V or IPXXB protection.
    *   **6.4.2. Mechanical Integrity (M1/N1 vehicles):** Vehicle-based (crash tests) or component-based (Annex 9D). Same acceptance criteria as 6.4.1.
*   **6.5. Fire Resistance (REESS with flammable electrolyte):** Vehicle-based or component-based test (Annex 9E). No explosion.
*   **6.6. External Short Circuit Protection:** Test per Annex 9F. Acceptance criteria as per 6.2.
*   **6.7. Overcharge Protection:** Test per Annex 9G. Acceptance criteria as per 6.2.
*   **6.8. Over-discharge Protection:** Test per Annex 9H. Acceptance criteria as per 6.2.
*   **6.9. Over-temperature Protection:** Test per Annex 9I. Acceptance criteria as per 6.2.
*   **6.10. Overcurrent Protection (M1/N1 with DC charging):** Test per Annex 9J. Acceptance criteria as per 6.2, plus charging termination or temperature stabilization.
*   **6.11. Low-temperature Protection:** Manufacturer must provide documentation on safety performance at low temperatures.
*   **6.12. Management of Gases:** Occupants not exposed to hazardous emissions. Open-type batteries must meet hydrogen emission requirements (5.4). Others deemed compliant if passing specified tests.
*   **6.13. Warning for REESS Control Failure:** Signal to activate vehicle warning (5.2.3) upon failure of controls managing REESS safe operation. Documentation required.
*   **6.14. Warning for Thermal Event:** Signal to activate warning in case of thermal event in REESS. Documentation required.
*   **6.15. Thermal Propagation (REESS with flammable electrolyte):** Occupants must be protected from hazardous environment due to thermal propagation from a single cell thermal runaway.
    *   **6.15.1:** Advance warning (5 minutes prior to passenger compartment hazard) OR no hazard occurs.
    *   **6.15.2:** REESS/vehicle must have protective functions/characteristics. Requires risk reduction analysis and detailed documentation.

## 7. Modifications and Extension of Type Approval
*   Modifications notified to Authority. May lead to new approval, revision (minor changes), or extension (further tests/info change/request for newer amendments).

## 8. Conformity of Production
*   Must comply with Schedule 1 of the Agreement (E/ECE/TRANS/505/Rev.3).
*   Production checks required.

## 9. Penalties for Non-conformity of Production
*   Approval may be withdrawn.

## 10. Production Definitively Discontinued
*   Holder informs Authority, who notifies other Parties.

## 11. Names and Addresses of Technical Services and Authorities
*   Contracting Parties communicate details to UN Secretariat.

## 12. Transitional Provisions
*   **03 series amendments:** Apply from entry into force.
*   Acceptance of prior series: Obligatory until 1 Sep 2025 for approvals first issued before 1 Sep 2023.
*   New Contracting Parties applying the Regulation after the latest amendments are not obliged to accept prior series approvals.

## Annexes (Referenced)
*   **Annex 1:** Communication forms and essential characteristics.
*   **Annex 2:** Approval mark arrangements.
*   **Annex 3:** Protection against direct contact (IPXXB/IPXXD test probes).
*   **Annex 4:** Verification of potential equalization.
*   **Annex 5A/B:** Isolation resistance measurement (vehicle/component).
*   **Annex 6:** Confirmation of on-board isolation resistance monitoring system function.
*   **Annex 7A/B:** Protection against water effects (documentation/vehicle test).
*   **Annex 8:** Determination of hydrogen emissions.
*   **Annex 9 & Appendices:** REESS test procedures (vibration, thermal shock, mechanical tests, electrical tests, fire resistance).
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 6 个
> - 公式 10 个
> - 图像 24 个
> - 全文 Markdown 194,842 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 6 个）

#### 表 1 (page 34)
<table><tr><td>100</td><td>03 2492</td></tr><tr><td>42</td><td>00 1628</td></tr></table>

#### 表 2 (page 70)
**Table 1 Frequency and acceleration **

<table><tr><td rowspan=1 colspan=1>Frequency (Hz)</td><td rowspan=1 colspan=1>Acceleration (m/s2)</td></tr><tr><td rowspan=1 colspan=1>7-18</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>18 - 30</td><td rowspan=1 colspan=1> gradually reduced from 10 to 2</td></tr><tr><td rowspan=1 colspan=1>30 -50</td><td rowspan=1 colspan=1>2</td></tr></table>

#### 表 3 (page 73)
**Table 1 for $\mathbf { M _ { 1 } }$ and $\mathbf { N _ { 1 } }$ vehicles: **

<table><tr><td rowspan=2 colspan=1>Point</td><td rowspan=2 colspan=1>Time (ms)</td><td rowspan=1 colspan=2>Acceleration (g)</td></tr><tr><td rowspan=1 colspan=1>Longitudinal</td><td rowspan=1 colspan=1>Transverse</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>65</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>4.5</td></tr><tr><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr></table>

#### 表 4 (page 73)
**Table 2 for ${ { \bf { M } } _ { 2 } }$ and ${ \bf N } _ { 2 }$ vehicles: **

<table><tr><td rowspan=2 colspan=1>Point</td><td rowspan=2 colspan=1>Time (ms)</td><td rowspan=1 colspan=2>Aeceleration (g)</td></tr><tr><td rowspan=1 colspan=1>Longitudinal</td><td rowspan=1 colspan=1>Transverse</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>65</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>2.5</td></tr><tr><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>10</td></tr></table>

#### 表 5 (page 74)
**Table 3 for $\mathbf { M } _ { 3 }$ and ${ \bf N } _ { 3 }$ vehicles: **

<table><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr></table>

#### 表 6 (page 74)
<table><tr><td rowspan=2 colspan=1>Point</td><td rowspan=2 colspan=1> Time (ms)</td><td rowspan=1 colspan=2> Acceleration (g)</td></tr><tr><td rowspan=1 colspan=1>Longitudinal</td><td rowspan=1 colspan=1>Transverse</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>6.6</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>65</td><td rowspan=1 colspan=1>6,6</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>2.5</td></tr><tr><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>10</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr></table>

### 公式（取前 10 个）

**公式 1** (page 34):

$$
\mathbf { a } = 8 \mathrm { m m } \mathrm { m i n } .
$$

**公式 2** (page 38):

$$
\mathbf { R } = \mathbf { U } / \mathbf { I }
$$

**公式 3** (page 41):

$$
\mathrm { R i } = \mathrm { R o ^ { * } U b ^ { * } ( 1 / U 1 ^ { \prime } - 1 / U 1 ) }
$$

**公式 4** (page 41):

$$
\mathrm { R i } = \mathrm { R o ^ { * } U b ^ { * } ( 1 / U 2 ^ { \prime } - 1 / U 2 ) }
$$

**公式 5** (page 44):

$$
\mathrm { R i } = \mathrm { R o ^ { * } U _ { b } } ^ { * } ( 1 / \mathrm { U _ { l } } ^ { \prime } - 1 / \mathrm { U _ { l } } )
$$

**公式 6** (page 45):

$$
\mathrm { R i } = \mathrm { R o ^ { * } U b ^ { * } ( 1 / U _ { 2 } } ^ { \prime } - 1 / U _ { 2 } )
$$

**公式 7** (page 46):

$$
1 / ( 1 / ( 9 5 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) \leq \mathrm { { R o } } < 1 / ( 1 / ( 1 0 0 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) } }
$$

**公式 8** (page 46):

$$
1 / ( 1 / ( 4 7 5 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) \leq \mathrm { { R o } } < 1 / ( 1 / ( 5 0 0 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) } }
$$

**公式 9** (page 60):

$$
{ \bf { M } } _ { \mathrm { { H } 2 } } = { \bf { k } } \times { \bf { V } } \times { 1 0 } ^ { - 4 } \times \left( { \frac { ( 1 + \frac { { \bf { V } } _ { \mathrm { { o u t } } } } { { \bf { V } } } ) \times { \bf { C } } _ { \mathrm { { H } 2 f } } \times { \bf { P } } _ { \mathrm { { f } } } } { \bf { T } _ { \mathrm { { f } } } } } - \frac { { \bf { C } } _ { \mathrm { { H } 2 i } } \times { \bf { P } } _ { \mathrm { { i } } } } { \bf { T } _ { \mathrm { { i } } } } \right)
$$

**公式 10** (page 63):

$$
{ \bf { M } } _ { \mathrm { { H } 2 } } = { \bf { k } } \times { \bf { V } } \times { 1 0 ^ { - 4 } } \times \left( { \frac { ( 1 + \frac { { \bf { V } } _ { \mathrm { { o u t } } } } { { \bf { V } } } ) \times { \bf { C } } _ { \mathrm { { H } 2 f } } \times { \bf { P } } _ { \mathrm { { f } } } } { \bf { T } _ { \mathrm { { f } } } } } - \frac { { \bf { C } } _ { \mathrm { { H } 2 i } } \times { \bf { P } } _ { \mathrm { { i } } } } { \bf { T } _ { \mathrm { { i } } } } \right)
$$

### 图像（取前 8 张）

![Figure 1 Schematic to Measure Wrap-Around Distance ](../_mineru_assets/ECE R100 Rev3/e1546e7b9db836ee7c55c10ce2fe9f585326f68de224df827039f21eab75992e.jpg)  
*Figure 1 Schematic to Measure Wrap-Around Distance * (page 10)

![图 page 27](../_mineru_assets/ECE R100 Rev3/fc1fb5a07400a5045e7a9553b54eb08d3308c278e74cffb17fc40dd70d27e7d4.jpg)  

![Figure 1 ](../_mineru_assets/ECE R100 Rev3/58fd8f8f1675eb16447640be8067208ee6f75977b670bc0a9df11e60943e20ef.jpg)  
*Figure 1 * (page 34)

![Figure 2 ](../_mineru_assets/ECE R100 Rev3/90e2ab9f986675414c2e1a7c77ce762266d3067278026eb36cd3d5a98af407e6.jpg)  
*Figure 2 * (page 34)

![图 page 34](../_mineru_assets/ECE R100 Rev3/49f22bb0de182186557ca70680cc35f99d8539437a5007a10733624008623f51.jpg)  

![图 page 36](../_mineru_assets/ECE R100 Rev3/8aa5a52667ea14f278e8b3c831d0b50b7655b9535670ee1c2f8bc32c06c29425.jpg)  

![Figure 1 Jointed Test Finger ](../_mineru_assets/ECE R100 Rev3/538a25661e1f34f4ed2c9d026dc52c717179ab46170b2be1c6bc34eba8badfd8.jpg)  
*Figure 1 Jointed Test Finger * (page 37)

![Figure 1 Example of Test Method using DC Power Supply ](../_mineru_assets/ECE R100 Rev3/68405cecd9674a0d573324d045bc4fc2227e48f56352b225f180bffc355c1c72.jpg)  
*Figure 1 Example of Test Method using DC Power Supply * (page 38)

