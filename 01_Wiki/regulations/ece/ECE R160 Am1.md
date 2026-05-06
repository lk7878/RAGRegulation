---
reg_id: ECE R160 Am1
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Event Data Recorder
status: active
version: Amendment 1
entry_into_force: 2022-04-22
standard_body: UNECE
source: E/ECE/TRANS/505/Rev.3/Add.159/Amend.1
source_url: https://unece.org/transport/documents/2023/03/standards/eecetrans505rev3add159amend1
scope: 'This Regulation applies to the approval of vehicles of categories M1 and N1
  with regard to their Event Data Recorder (EDR). It establishes uniform provisions
  concerning the minimum collection, storage and crash survivability of motor vehicle
  crash event data for effective crash investigations and analysis of safety equipment
  performance.

  '
keywords:
- Event Data Recorder
- EDR
- crash data
- vehicle approval
- data recording
- data format
- data capture
- crash survivability
- UN Regulation
vehicle_category:
- M1
- N1
related_regulations: []
amendments: []
supplements: []
implement_date: null
note: 'This is Amendment 1 to UN Regulation No. 160. The authentic and legally binding
  text is: ECE/TRANS/WP.29/2021/58.

  Transitional provisions specify acceptance timelines for type approvals to the original
  version and the amended version.'
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\160\R160am1e.pdf
publication_date: 2023-03-20
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及新车型的实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及在用车型的实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及替代关系。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: 提供的B文本片段未包含具体的技术要求限值。
_ocr_upgraded: mineru
_mineru_content_hash: 11f71948a32fae45
_mineru_outputs_dir: outputs/11f71948a32fae45
_mineru_blocks:
  tables: 3
  formulas: 0
  images: 2
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 160 - Event Data Recorder (Amendment 1)

## 0. Introduction
The intention of this Regulation is to establish uniform provisions concerning the approval of motor vehicles of Categories M1 and N1 with regard to their Event Data Recorders (EDRs). The provisions concern the minimum collection, storage and crash survivability of motor vehicle crash event data. It does not include specifications for data retrieval tools and methods as that is subject to national/regional level requirement.

The purpose is to ensure that EDRs record, in a readily usable manner, data valuable for effective crash investigations and for analysis of safety equipment performance (e.g., advanced restraint systems).

## 1. Scope
This Regulation applies to the approval of vehicles of categories M1 and N1 with regard to their Event Data Recorder (EDR). It is without prejudice to requirements of national or regional laws related to privacy, data protection and personal data processing.

The following data elements are excluded from the scope: VIN, associated vehicle details, location/positioning data, information of the driver, and date and time of an event.

## 2. Definitions
Key definitions include:
*   **Event Data Recorder (EDR):** A device or function in a vehicle that records the vehicle's dynamic, time-series data during the time period just prior to an event or during a crash event, intended for retrieval after the crash event. Does not include audio and video data.
*   **Event:** A crash or other physical occurrence that causes the trigger threshold to be met or exceeded, or any non-reversible deployable restraint to be deployed, whichever occurs first.
*   **Capture:** The process of buffering EDR data in a temporary, volatile storage where it is continuously updated.
*   **Record:** The process of saving captured EDR data into a non-volatile storage for subsequent retrieval.
*   **Time zero:** The time reference for the EDR data timestamps of an event.
*   **Vehicle type with regard to its Event Data Recorder:** Vehicles which do not differ significantly in essential aspects such as the manufacturer’s trade name, vehicle features significantly influencing EDR performance, and the main characteristics and design of the EDR.

*(The Regulation contains 55 detailed definitions covering parameters like delta-V, acceleration, deployment times, system statuses, etc.)*

## 3. Application for Approval
The application shall be submitted by the vehicle manufacturer or authorized representative to the approval authority. It must be accompanied by documentation including a description of the vehicle type (location of EDR, triggering parameters, etc.), the data elements and format stored, and instructions for retrieving data. A representative vehicle shall be submitted for testing.

## 4. Approval
If the vehicle type meets the requirements, approval shall be granted. An approval number is assigned. An international approval mark (a circle surrounding "E" followed by the country number and regulation number, or an oval surrounding "UI" followed by a Unique Identifier) must be affixed to conforming vehicles.

## 5. Requirements
Requirements for vehicles fitted with an EDR include data elements, data format, data capture, and crash test performance/survivability.

### 5.1. Data Elements
Each vehicle fitted with an EDR shall record the data elements specified as mandatory (and those required under specified conditions) during the interval/time and at the sample rate specified in **Annex 4, Table 1**. Mandatory recording is subject to the vehicle being fitted with the relevant operational sensor/system.

### 5.2. Data Format
Each data element recorded shall be reported in accordance with the range, accuracy, and resolution specified in **Annex 4, Table 1**. Specific format requirements are provided for acceleration time-history data.

### 5.3. Data Capture
*   The EDR non-volatile memory must accommodate data for at least three different events.
*   **Triggering for Recording:** An event is recorded if one of these thresholds is met/exceeded:
    *   Change in longitudinal velocity > 8 km/h within ≤150 ms.
    *   Change in lateral velocity > 8 km/h within ≤150 ms.
    *   Activation of a non-reversible occupant restraint system.
    *   Activation of a Vulnerable Road User (VRU) secondary safety system (if fitted).
*   **Locking of Data (prevent overwriting):** Required when:
    *   A non-reversible occupant restraint system is deployed.
    *   In frontal impact without such a system, if longitudinal delta-V exceeds 25 km/h within ≤150 ms.
    *   Activation of a VRU secondary safety system.
*   **Time Zero Establishment:** Defined as the first occurrence of specific algorithm activation or delta-V thresholds.
*   **Overwriting:** Recorded data may be overwritten on a first-in-first-out basis if memory is full, except data locked per 5.3.2. shall not be overwritten by non-locked data. Data from deployment events shall overwrite any non-locked data.
*   **Power Failure:** Data in non-volatile memory must be retained after loss of power.

### 5.4. Crash Test Performance and Survivability
Data elements must be recorded, exist after completion of specified frontal or side impact crash tests (UN Regulations Nos. 94, 95, or 137), and be retrievable. The "complete file recorded" element must read "yes".

### 5.5. It shall not be possible to deactivate the Event Data Recorder.

## 6. Modification of Vehicle Type and Extension of Approval
Modifications must be notified to the approval authority, which may grant an extension or require further tests.

## 7. Conformity of Production
Procedures must conform to the general provisions of the 1958 Agreement. The approval authority verifies conformity control methods at least once every two years.

## 8. Penalties for Non-Conformity of Production
Approval may be withdrawn if conformity of production requirements are not met.

## 9. Production Definitely Discontinued
The approval holder must inform the approval authority if production ceases.

## 10. Names and Addresses of Technical Services and Approval Authorities
Contracting Parties shall communicate relevant details to the UN Secretariat.

## 11. Transitional Provisions
*   From the entry into force of the 01 series of amendments, Contracting Parties shall not refuse approvals under the amended Regulation.
*   From **1 July 2024**, Contracting Parties are not obliged to accept new type approvals to the *original* version.
*   Until **1 July 2026**, Contracting Parties shall accept type approvals to the *original* version first issued before 1 July 2024.
*   From **1 July 2026**, Contracting Parties are not obliged to accept any type approvals to the *original* version (except for vehicles unaffected by the amendments).

## Annexes
*   **Annex 1:** Communication form for approval notifications.
*   **Annex 2:** Information document template for type approval application.
*   **Annex 3:** Arrangements of approval marks (E-mark and Unique Identifier).
*   **Annex 4:** **Data elements and format (Table 1)** - The core technical specification detailing each required data element, its recording condition, interval, sample rate, minimum range, accuracy, and resolution. Data is categorized for planar events, VRU events, and rollover events.
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 10 个
> - 公式 0 个
> - 图像 2 个
> - 全文 Markdown 49,363 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 13)
<table><tr><td rowspan=1 colspan=1>Data element</td><td rowspan=1 colspan=1>Recordinginterval/time(relative to timezero)</td><td rowspan=1 colspan=1>Data sample rate(samples persecond)</td><td rowspan=1 colspan=1>Minimum range</td><td rowspan=1 colspan=1>Accuracy</td><td rowspan=1 colspan=1>Resolution</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 2 (page 15)
<table><tr><td colspan="9">Table 1 Recording</td></tr><tr><td>Data element Delta-V, longitudinal</td><td>Condition for requirement² Mandatory - not required if or O to End of longitudinal acceleration</td><td>interval/time (relative to time zero) 0 to 250 ms Event Time plus 30 ms,</td><td>Data sample rate (samples per second) 100</td><td>Minimum range -100 km/h to + 100 km/h.</td><td>Accuracy4 ±10%</td><td>Resolution 1 km/h.</td><td>Event(s) recorded for Planar</td></tr><tr><td>Maximum</td><td>recorded at ≥500 Hz with shorter. sufficient range and resolution to calculate delta-v with required accuracy Mandatory -</td><td>whichever is 0-300 ms or</td><td>N/A</td><td>-100 km/h to +±10%</td><td></td><td>1 km/h.</td><td>Planar</td></tr><tr><td>delta-V, longitudinal</td><td>not required if O to End of longitudinal acceleration recorded at ≥500 Hz</td><td>Event Time plus 30 ms, whichever is shorter.</td><td></td><td>100 km/h.</td><td></td><td></td><td></td></tr><tr><td>Time, maximum delta-V, longitudinal</td><td>Mandatory - not required if O to End of longitudinal acceleration recorded at ≥500 Hz</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Speed, vehicle Mandatory indicated</td><td></td><td>-5.0 to 0 sec</td><td>2</td><td>0 km/h to 250 km/h</td><td>±1 km/h</td><td>1 km/h.</td><td>Planar VRU</td></tr><tr><td>Engine throttle, % full (or accelerator pedal, % full)</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>0 to 100%</td><td>±5%</td><td>1%</td><td>Planar Rollover VRU</td></tr><tr><td>Service brake, on/off</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar VRU Rollover</td></tr><tr><td rowspan="2">Data element</td><td rowspan="2">Condition for requirement²</td><td rowspan="2">Recording interval/time³ (relative to time zero)</td><td rowspan="2">Data sample rate (samples per second)</td><td rowspan="2">Minimum range</td><td rowspan="2">Accuracy4 Resolution</td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>Event(s) recorded for5</td></tr><tr><td>Ignition cycle， Mandatory crash</td><td></td><td> -1.0 sec</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Planar VRU Rollover</td></tr><tr><td>Ignition cycle, Mandatory download</td><td></td><td>At time of download6</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Planar VRU Rollover</td></tr><tr><td>Safety belt status, driver</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Air bag warning lamp7,</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar Rollover</td></tr><tr><td>deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in the case of a multi-stage air</td><td>Frontal air bag Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>bag, driver. Frontal air bag Mandatory deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in the case of a multi-stage air bag, front</td><td></td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>passenger. Multi-event crash, number</td><td>If Recorded8</td><td>Event</td><td>N/A</td><td>1 or more</td><td>N/A</td><td>1 or more.</td><td>Planar</td></tr><tr><td>of event</td><td></td><td></td><td></td><td></td><td></td><td></td><td>VRU Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Time from event 1 to 2</td><td>Mandatory</td><td>As needed</td><td>N/A</td><td>0 to 5.0 sec</td><td>±0.1 sec</td><td>0.1 sec.</td><td>Planar Rollover</td></tr><tr><td>Complete file recorded (yes, no)</td><td>Mandatory</td><td>Following other data</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar VRU Rollover</td></tr><tr><td>Lateral acceleration (post-crash)</td><td>If Recorded</td><td>0-250 ms or O to End of Event Time plus 30 ms, whichever is</td><td>500Hz</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Planar Rollover</td></tr><tr><td>Longitudinal acceleration (post-crash)</td><td>If Recorded</td><td>shorter. 0-250 ms or O to End of Event Time plus 30 ms,</td><td>500Hz</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Planar</td></tr><tr><td>Normal acceleration (post-crash)</td><td>If recorded</td><td>shorter. -1.0 to 5.0 sec9</td><td>10Hz</td><td>-5gto+5g</td><td>±10%</td><td>0.5g</td><td>Rollover</td></tr><tr><td>Delta-V, lateral</td><td>Mandatory - lateral acceleration recorded at ≥500 Hz and with sufficient</td><td>0-250 ms or not required if O to End of Event Time plus 30 ms, whichever is shorter.</td><td>100</td><td>-100 km/h to +±10% 100 km/h.</td><td></td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Maximum delta-V,lateral</td><td>Mandatory - lateral acceleration</td><td>0-300 ms or not required if O to End of Event Time plus 30 ms,</td><td>N/A</td><td>-100 km/h to +±10% 100 km/h.</td><td></td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Time maximum delta-V, lateral</td><td>Mandatory - not required if O to End of lateral acceleration recorded at ≥500 Hz</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Time for maximum delta-V, resultant.</td><td>Mandatory - not required if O to End of relevant acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Engine rpm</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 to 10,000 rpm ±100</td><td>rpm10</td><td>100 rpm.</td><td>Planar Rollover</td></tr><tr><td>Vehicle roll angle</td><td>If recorded</td><td>-1.0 up to 5.0 10 sec9</td><td></td><td>-1080 deg to + 1080 deg.</td><td>±10%</td><td>10 deg.</td><td>Rollover</td></tr><tr><td>Vehicle roll rate</td><td>Mandatory if fitted and used for rollover protection system control algorithm</td><td>-1.0up to 5.0 10 secl1</td><td></td><td>-240 to + 240 deg/sec</td><td></td><td>+/- 10%121 deg/sec</td><td>Rollover</td></tr><tr><td>ABS activity</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>Faulted, Active， N/A Intervening13</td><td></td><td>Faulted, Active,</td><td>Planar VRU</td></tr><tr><td>Stability control</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, On, Off, Intervening12</td><td>N/A</td><td>Faulted, On, Off, Intervening12</td><td>Planar VRU</td></tr><tr><td>Steering input</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>-250 deg CW to ±5% + 250 deg CCW.</td><td></td><td>±1%.</td><td>Planar VRU</td></tr><tr><td>Safety belt status, front passenger</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time³ (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Passenger air bag suppression status, front</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Suppressed or not suppressed</td><td>N/A</td><td>Suppressed or Planar not suppressed</td><td>Rollover</td></tr><tr><td>Frontal air bag deployment, time to nth stage, driver4.</td><td>Mandatory if Event fitted with a driver's frontal air bag with a multi- stage inflator.</td><td></td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Frontal air bag deployment, time to nth stage, front passenger14.</td><td>Mandatory if Event fitted with a front passenger's frontal air bag with a multi- stage inflator.</td><td></td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side air bag deployment, time to deploy, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side air bag deployment, time to deploy, front</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>passenger. Side curtain/tube air bag deployment, time to deploy,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>driver side. Side curtain/tube air bag deployment, time to deploy,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Pretensioner deployment, time to fire, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td colspan="9"></td></tr><tr><td></td><td>Condition for</td><td>Recording interval/time³ (relative to time</td><td>Data sample rate (samples</td><td></td><td></td><td></td><td>Event(s)</td></tr><tr><td>Data element Pretensioner deployment,</td><td>requirement² Mandatory</td><td>zero) Event</td><td>per second) N/A</td><td>Minimum range 0 to 250 ms</td><td>Accuracy4 ±2 ms</td><td>Resolution 1 ms.</td><td>recorded for Planar</td></tr><tr><td>time to fire, front passenger. Seat track</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Rollover</td></tr><tr><td>position switch, foremost, status, driver.</td><td>Mandatory if fitted and used for deployment decision</td><td>-1.0 sec</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Seat track position switch, foremost, status, front</td><td>Mandatory if fitted and used for deployment decision</td><td>-1.0 sec</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>passenger. Occupant size classification, driver</td><td>If recorded</td><td> -1.0 sec</td><td>N/A</td><td>5th percentile female or larger.</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Occupant size classification,</td><td>If recorded</td><td>-1.0 sec</td><td>N/A</td><td>6yr old HIII USN/A ATD or Q6</td><td></td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>front passenger Safety belt status, rear</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>ATD or smaller Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>passengers Tyre Pressure Monitoring System (TPMS)</td><td>Mandatory</td><td>-1.0 second relative to time zero</td><td>N/A</td><td>N/A</td><td>N/A</td><td>On, Off</td><td>Planar Rollover</td></tr><tr><td>Warning Lamp Status Longitudinal acceleration</td><td>Mandatory</td><td>-5.0 to 0 second</td><td>2 Hz</td><td>-1.5g to +1.5g</td><td>+/- 10%</td><td>0.1g</td><td>Planar</td></tr><tr><td>(pre - crash) Lateral</td><td>Mandatory</td><td>relative to time zero -5.0 to 0</td><td>2Hz</td><td>-1.0g to +1.0g</td><td>+/- 10%</td><td>0.1g</td><td>VRU Planar</td></tr><tr><td>acceleration (pre -crash)</td><td></td><td>second relative to time zero</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Yaw Rate</td><td>Mandatory</td><td>-5 to0 seconds relative to time zero</td><td>2</td><td>-75 to +75 degrees / second the full</td><td>±10% of0.1 range of the sensor</td><td></td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time² (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range</td><td> Accuracy4</td><td>Resolution Actively</td><td>Event(s) recorded for</td></tr><tr><td>Traction Control Status</td><td>Mandatory if not fitted with second ESC</td><td>-5.0 to 0 relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling, Faulted, Commanded Off, or On but Not Controlling</td><td>Planar Rollover</td></tr><tr><td>AEBS status</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Actively Warning, Actively Engaged, Faulted, Off,</td><td>Planar VRU Rollover</td></tr><tr><td>Cruise Control System</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Not Active Actively Controlling, Faulted, Commanded Off, On but Not</td><td>Planar VRU Rollover</td></tr><tr><td>Adaptive Cruise Control Status (driving automation system level 1)</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Controlling Actively Controlling, Faulted, Commanded Off, On but Not</td><td>Planar VRU Rollover</td></tr><tr><td>VRU secondary safety system deployment, time to deploy</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>Controlling 1 ms</td><td>VRU</td></tr><tr><td>VRU secondary Mandatory safety system warning</td><td></td><td>-1.1 to 0 relative to time zero</td><td>N/A</td><td>N/A</td><td>N/A</td><td>On or Off</td><td>VRU</td></tr><tr><td>indicator status15 Safety belt status mid-</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar</td></tr><tr><td>position front</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Rollover</td></tr><tr><td>Far side impact Mandatory center airbag</td><td></td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>+/-2 ms</td><td>1 ms</td><td>Planar Rollover</td></tr></table>

#### 表 3 (page 16)
#### 表 4 (page 17)
#### 表 5 (page 18)
#### 表 6 (page 19)
#### 表 7 (page 20)
#### 表 8 (page 21)
#### 表 9 (page 22)
<table><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td></tr><tr><td>Lane departure Mandatory warning system status</td><td></td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not warning, On - Warning left, On - Warning</td></tr><tr><td>Corrective steering function (CSF) status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not intervening, On - Actively</td></tr><tr><td>Emergency steering function (ESF) status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>intervening Faulted, Off, On but not intervening, On - Actively</td></tr><tr><td>Automatically commanded steering function (ACSF) category A status</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>intervening Faulted, Off, On but not controlling, On - Actively controlling</td></tr><tr><td>Automatically commanded steering function (ACSF) category B1</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not controlling, On -Actively</td></tr><tr><td>status commanded steering function (ACSF) category B2</td><td>AutomaticallyMandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling Faulted, Off, On but not controlling, On - Actively</td></tr><tr><td>Automatically commanded steering function (ACSF) category C</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling Faulted, Off, On but not controlling,</td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td>Accuracy4</td><td>E Resolution re</td></tr><tr><td>Automatically commanded steering function (ACSF) category D</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not controlling, On - Actively controlling</td></tr><tr><td>status commanded steering function (ACSF) category E</td><td>AutomaticallyMandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not controlling, On - Actively</td></tr><tr><td>status Accident emergency call system status</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>N/A</td><td>N/A</td><td>controlling Faulted, On but emergency call not automatically triggered,</td></tr></table>

#### 表 10 (page 23)
### 图像（取前 2 张）

![图 page 12](../_mineru_assets/ECE R160 Am1/dc1a25e1b31535eeaf88f9cb3478f5df7dcd0025f737404bc71690c0faf36761.jpg)  

![图 page 14](../_mineru_assets/ECE R160 Am1/befa19c27eee3e3d7f6c49c000de8df3e07aa522d686a0a3334f6bb4c0a1b05b.jpg)  

