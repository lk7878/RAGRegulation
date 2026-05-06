---
reg_id: ECE R79 Rev4 Am9
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of vehicles with regard to steering
  equipment
status: active
publication_date: 2023-02-16
implementation_date_new_vehicle: 2023-01-04
source_file: 国外法规\ECE标准\标准法规-UNECE\41～80\79\R079r4am9e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\79\R079r4am9e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及 standard_body 字段。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及针对在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及等效法规信息。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及本修正案替代了哪个文件。
_ocr_upgraded: mineru
_mineru_content_hash: 03a72544fd4f2bfb
_mineru_outputs_dir: outputs/03a72544fd4f2bfb
_mineru_blocks:
  tables: 9
  formulas: 1
  images: 3
_mineru_merged_at: '2026-04-22'
---

# UN Regulation No. 79 Revision 4 - Amendment 9

**Supplement 8 to the 03 series of amendments – Date of entry into force: 4 January 2023**

This document constitutes **Amendment 9** to **UN Regulation No. 79, Revision 4** (Steering Equipment). The authentic and legally binding text is: **ECE/TRANS/WP.29/2022/80**.

## Summary of Amendments

This amendment introduces significant updates to the regulation concerning Automated Commanded Steering Functions (ACSF), particularly focusing on **ACSF of Category C** (lane change assistance). Key changes include new definitions, detailed technical requirements for lane change maneuvers involving trailers, and the introduction of new annexes for data communication and compatibility testing.

## Detailed Amendments

### 1. Definitions (Paragraph 2.)
*   **2.4.17. "Lane Change Manoeuvre"**: Amended to precisely define the start and end points of the maneuver based on vehicle wheel positions relative to lane markings.
*   **2.7. "Electric control line"**: Amended to clarify it includes components for data communication and electrical energy supply for trailer control transmission.
*   **New 2.8. "Data communication"**: Defined as the transfer of digital data under protocol rules.
*   **New 2.9. "Point-to-point"**: Defined as a communication network topology with only two units, each with an integrated termination resistor.

### 2. Requirements for Control of the Steering Equipment (Paragraph 5.)
*   **5.1.6.1.1. (CSF Intervention Warning)**: Amended to allow the ESC flashing tell-tale to be used as an alternative optical warning signal for interventions controlled by ESC or Vehicle Stability Function.
*   **5.3.3.1. (System Design - Faults)**: Amended to require system design preventing indefinite driving above 10 km/h when a fault triggering the paragraph 5.4.2.1.1. warning signal exists.
*   **5.6.4. (Special Provisions for ACSF of Category C)**: Amended introductory text.
*   **5.6.4.1.1.**: Amended to require a power-driven vehicle with ACSF Category C to also be equipped with a compliant ACSF of Category B1.
*   **New 5.6.4.5.5.1.**: Requires a system failure signal from a trailer (supporting lane change) transmitted via the electric control line to trigger the corresponding warning signal on the towing vehicle.
*   **5.6.4.8.1. (Rear detection and minimum operation speed)**: Restructured and expanded into new sub-paragraphs (5.6.4.8.1.1. to 5.6.4.8.1.4.) with specific requirements for:
    *   **5.6.4.8.1.1.**: Vehicles/trailers in solo condition or trailers supporting lane change. Defines minimum rear detection distance `S_rear` (≥55 m) and testing method.
    *   **5.6.4.8.1.2.**: Category N2/N3 vehicles coupled to trailers *supporting* lane change. Specifies detection areas, requirements, and deactivation conditions.
    *   **5.6.4.8.1.3.**: Category N2/N3 vehicles coupled to trailers *not supporting* lane change. Specifies `S_rear` measurement point, maximum trailer length `L_T` declaration, and system deactivation logic.
    *   **5.6.4.8.1.4.**: Formula for calculating minimum operation speed `V_smin`, with provisions for lower speed limits and conditions allowing maneuvers below `V_smin`.
*   **5.6.4.8.2. (Detection area on ground level)**: Amended.
*   **5.6.4.8.3. (Initialization after start cycle)**: Amended to require system prevention of lane change until a moving object beyond `S_rear` is detected.
*   **5.6.4.8.4. (Sensor blindness detection)**: Amended to include detection on trailers and require prevention of lane change maneuver upon detection.
*   **New 5.6.4.9. (Connections for ACSF between power-driven vehicle and trailer)**:
    *   **5.6.4.9.1.**: Specifies data communication line must conform to ISO 11992-1:2019 & -3:2021, point-to-point, using ISO 12098 connector or equivalent automated connector.
    *   **5.6.4.9.1.1.**: Refers to Annex 9 for supported ISO 11992-3:2021 messages.
    *   **5.6.4.9.1.2.**: Requires functional compatibility assessment per ISO 11992 standards, with Annex 10 providing example tests.
    *   **5.6.4.9.1.3.**: Requires detection and driver warning for continuous failures (>40 ms) in the electric control line.
    *   **5.6.4.9.1.4.**: Requires power-driven vehicles to use trailer data, send GPM 11, and receive GPM 21 before enabling ACSF-C.
*   **New 5.6.4.9.2. (Special provisions for trailers supporting lane change)**:
    *   **5.6.4.9.2.1.**: Functionality enabled only upon GPM 11/GPM 21 message exchange.
    *   **5.6.4.9.2.2.**: Trailers with ACSF sensors must conform to ISO 11992-3:2021 and Annex 9. Failure warnings must be activated via the connector.
    *   **5.6.4.9.2.3.**: Trailer system failures must be transmitted to the motor vehicle.
*   **Renumbered 5.6.4.10. (System information data)**: Lists data required for type approval documentation.
*   **Renumbered 5.6.4.11.**: Specifies testing according to Annex 8, with safe operation demonstration per Annex 6 for uncovered situations.

### 3. Amendments to Annexes
*   **Annex 1 (Communication)**: New paragraphs **7.3.**, **7.3.1.**, **7.3.2.**, **7.3.3.** and **8.4.** added to the model information document for declaring ACSF Category C capabilities and trailer support status.
*   **Annex 8 (Tests for ACSF)**: 
    *   **Paragraph 3.5.**: Amended with general test provisions for ACSF Category C, specifying test configurations based on vehicle/trailer capabilities declared in Annex 1.
    *   **Paragraph 3.5.4.1.**: Amended test procedure for system state transitions and overrides.
    *   **New Paragraphs 3.5.8., 3.5.8.1., 3.5.8.2.**: Introduce lane change suppression tests for different vehicle/trailer combinations.
    *   **New Paragraphs 3.5.9., 3.5.9.1., 3.5.9.2.**: Introduce object detection tests for trailers supporting lane change functions.
*   **New Annex 9**: "Compatibility between towing vehicles and trailers with regard to data transmission according to ISO 11992 for environmental monitoring". Defines mandatory and optional ISO 11992-3:2021 messages (GPM, ODM) that must be supported by towing vehicles and trailers for ACSF data exchange, including message definitions and object selection rules.
*   **New Annex 10**: "Test procedure to assess the functional compatibility of vehicles equipped with ACSF control lines". Provides a procedure (using simulators) for Technical Services to check compliance of towing vehicles and trailers with the data communication and failure warning requirements of paragraph 5.6.4.9.1.2.

---
**Note:** This summary is based on the provided OCR text of the amendment. For definitive application, the authentic source document **ECE/TRANS/WP.29/2022/80** should be consulted.
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 9 个
> - 公式 1 个
> - 图像 3 个
> - 全文 Markdown 41,446 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 9 个）

#### 表 1 (page 9)
<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO 11992-03:2021</td><td>Regulation No.79 Reference</td></tr><tr><td>1</td><td>1 to 2</td><td>Vehicle type</td><td>Regulation No. 79,</td></tr><tr><td></td><td>3 to8</td><td>Detailed Vehicle Type</td><td>Paragraph 5.6.4.9.1.4. Regulation No. 79,</td></tr><tr><td></td><td></td><td></td><td>Paragraph 5.6.4.9.1.4.</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>5 to8</td><td>ODM version request</td><td>Regulation No. 79,</td></tr><tr><td></td><td></td><td></td><td>Paragraph 5.6.4.9.1.4.</td></tr></table>

#### 表 2 (page 10)
**ODM11 message definition**

<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO 11992-03:2021</td></tr><tr><td>1</td><td>---</td><td>CRC</td></tr><tr><td>2</td><td>1 to 4</td><td>sequence counter</td></tr><tr><td></td><td>5 to8</td><td>ODM input</td></tr><tr><td>3 to 4</td><td>---</td><td>longitudinal speed</td></tr><tr><td>5 to 6</td><td></td><td>lateral speed</td></tr><tr><td>7 to8</td><td>--</td><td>yaw rate</td></tr></table>

#### 表 3 (page 10)
**ODM 21,ODM 23,ODM 25,ODM 27,ODM 29,ODM 211,ODM 213, ODM 215 message definition **

<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO 11992-03:2021</td><td>Regulation No.79Reference</td></tr><tr><td>1</td><td>1 to 2</td><td>Vehicle Type</td><td>Regulation No. 79, Paragraph 5.6.4.9.2.1.</td></tr><tr><td></td><td>3 to8</td><td>Detailed Vehicle Type</td><td>Regulation No. 79,</td></tr><tr><td>2</td><td>5 to8</td><td>ODM Version Information</td><td>Paragraph 5.6.4.9.2.1. Regulation No. 79,</td></tr><tr><td>7</td><td>1 to 8</td><td>Identification Data Index</td><td>Paragraph 5.6.4.9.2.1. Regulation No. 79,</td></tr><tr><td>8</td><td>1 to 8</td><td>Identification Data Content</td><td>Paragraph 5.6.4.9.2.1. Regulation No. 79,</td></tr></table>

#### 表 4 (page 10)
<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO 11992-03:2021</td></tr><tr><td>1</td><td>---</td><td>Cyclic Redundancy Check (CRC-8)</td></tr><tr><td>2</td><td>1 to 4</td><td>Sequence Counter</td></tr><tr><td>2</td><td>5 to8</td><td>Status Indicator</td></tr><tr><td>3 to4</td><td>-</td><td>Automated Steering Longitudinal Distance Object</td></tr><tr><td>5 to 6</td><td>-</td><td>Automated Steering Lateral Distance Object</td></tr><tr><td>7</td><td>1 to 4</td><td>Automated Steering Standard Deviation of Longitudinal and Lateral Distance</td></tr><tr><td>7</td><td>5 to8</td><td>reserved by this document</td></tr><tr><td>8</td><td>1 to8</td><td>Track ID</td></tr></table>

#### 表 5 (page 11)
<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>ParameterISO 11992-03:2021</td></tr><tr><td>1</td><td>---</td><td>Cyclic Redundancy Check (CRC-8)</td></tr><tr><td>2</td><td>1 to 4</td><td>Sequence Counter</td></tr><tr><td>2</td><td>5 to8</td><td>Status Indicator</td></tr><tr><td>3 to 4</td><td>-</td><td>Automated Steering Absolute Longitudinal Speed Object</td></tr><tr><td>5 t06</td><td>---</td><td>Automated Steering Absolute Lateral Speed Object</td></tr><tr><td>7</td><td>1 to 4</td><td>Automated Steering Normal Deviation of Longitudinal and Lateral Speed</td></tr><tr><td>7</td><td>5 to7</td><td>reserved by this document</td></tr></table>

#### 表 6 (page 13)
<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO11992-03:2021</td></tr><tr><td>1</td><td>--</td><td>Cyclic Redundancy Check (CRC-8)</td></tr><tr><td>2</td><td>1 to 4</td><td>Sequence Counter</td></tr><tr><td>2</td><td>5 to8</td><td>Status Indicator</td></tr><tr><td>3 to 4</td><td></td><td>Geometric Item #1</td></tr><tr><td>5 to 6</td><td>---</td><td>Geometric Item #2</td></tr><tr><td>7 to8</td><td>---</td><td>Geometric Item #3</td></tr></table>

#### 表 7 (page 13)
<table><tr><td>Sequence counter</td><td>Item</td><td>Parameter ISO 11992-03:2021</td></tr><tr><td>1 or 9</td><td>#1</td><td>distance to rear coupling point</td></tr><tr><td>1or 9</td><td>#2</td><td>distance to centre of rotation</td></tr></table>

#### 表 8 (page 13)
<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO 11992-03:2021</td></tr><tr><td>3 to 4</td><td>1 to 16</td><td>Articulation Angle between towing and towed vehicle</td></tr><tr><td>5 to 6</td><td>1 to 16</td><td>Angle between towing vehicle and drawbar</td></tr><tr><td>7 to 8</td><td>1 to 16</td><td>Angle between drawbar and towed vehicle</td></tr></table>

#### 表 9 (page 13)
<table><tr><td>Byte pos.</td><td>Bit pos.</td><td>Parameter ISO 11992-03:2021</td></tr><tr><td>3 to4</td><td>1 to 16</td><td>Articulation Angle between towing and towed vehicle</td></tr><tr><td>5 to 6</td><td>1 to 16</td><td>Articulation Angle drawbar and towed vehicle</td></tr></table>

### 公式（取前 1 个）

**公式 1** (page 3):

$$
V _ { S m i n } = \ a * ( t _ { B } - t _ { G } ) + v _ { a p p } - \sqrt { a ^ { 2 } * ( t _ { B } - t _ { G } ) ^ { 2 } - 2 * a * ( v _ { a p p } * t _ { G } - S _ { r e a r } ) }
$$

### 图像（取前 3 张）

![图 page 4](../_mineru_assets/ECE R79 Rev4 Am9/7d51910be317ae01e83321150a28923512162582bfcf560e06eaa33d8342d419.jpg)  

![图 page 11](../_mineru_assets/ECE R79 Rev4 Am9/beb81405838b98d590d1a44b929e8f7a3422276c62ac71ec626bdd76370c2ccf.jpg)  

![图 page 12](../_mineru_assets/ECE R79 Rev4 Am9/cc97b7dc8a83defaaf4689455f4aeb78fc6f5f8a6972d92cf29c5489db5ebf0d.jpg)  

