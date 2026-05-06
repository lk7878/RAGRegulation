---
reg_id: ECE R160 Rev1
region: ece
type: type/version
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Event Data Recorder
source_file: 国外法规\ECE标准\标准法规-UNECE\121~160\160\R160r1e.pdf
status: active
publication_date: 2023-02-03
implementation_date_new_vehicle: 2022-10-08
version: Revision 1, 01 series of amendments
authentic_source: ECE/TRANS/WP.29/2021/58
scope: 'This Regulation applies to the approval of vehicles of categories M1 and N1
  with regard to their Event Data Recorder (EDR). It establishes uniform provisions
  concerning the minimum collection, storage and crash survivability of motor vehicle
  crash event data, intended to facilitate effective crash investigations and analysis
  of safety equipment performance.

  The Regulation is without prejudice to national or regional laws related to privacy,
  data protection and personal data processing. Certain data elements (e.g., VIN,
  location data, driver information, date/time) are explicitly excluded from its scope.

  '
standard_body: United Nations Economic Commission for Europe (UNECE)
keywords:
- Event Data Recorder
- EDR
- vehicle approval
- crash data
- data recording
- UN Regulation
tags:
- type/version
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\160\R160r1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及在用车实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及替代法规。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: B 提供的文本未包含具体技术要求的数值限值。
_ocr_upgraded: mineru
_mineru_content_hash: 7f46aa397193a168
_mineru_outputs_dir: outputs/7f46aa397193a168
_mineru_blocks:
  tables: 3
  formulas: 1
  images: 2
_mineru_merged_at: '2026-04-22'
---

# UN Regulation No. 160 (Revision 1) - Event Data Recorder (EDR)

## 0. Introduction
- **0.1.** Establishes uniform provisions for approval of M1 and N1 category vehicles regarding their Event Data Recorders (EDRs).
- **0.2.** Concerns minimum collection, storage, and crash survivability of crash event data. Data retrieval tools/methods are subject to national/regional requirements.
- **0.3.** Purpose: Ensure EDRs record data valuable for crash investigations and safety equipment performance analysis to facilitate safer vehicle designs.

## 1. Scope
- **1.1.** Applies to approval of M1 and N1 vehicles regarding their EDR.
- **1.2.** Without prejudice to national/regional privacy, data protection, and personal data processing laws.
- **1.3.** Excluded data: VIN, associated vehicle details, location/positioning data, driver information, date and time of event.
- **1.4.** No requirement to record data if the necessary system/sensor is not designed to provide it in the format specified in Annex 4 or is not operational at recording time. However, if an OEM sensor/system is fitted and designed to provide the data in the specified format, it must report the data when operational. System/sensor failures must be recorded by the EDR.

## 2. Definitions
Provides definitions for key terms used in the Regulation, including but not limited to:
- **2.1.** ABS activity
- **2.10.** Event
- **2.11.** Event data recorder (EDR): A device or function that records vehicle dynamic, time-series data prior to or during a crash event, intended for post-crash retrieval (excludes audio/video).
- **2.20.** Maximum delta-V, resultant
- **2.21.** Multi-event crash
- **2.22.** Non-volatile memory
- **2.28.** Record
- **2.45.** Time zero
- **2.46.** Trigger threshold
- **2.48.** Vehicle type with regard to its Event Data Recorder
- **2.49.** Volatile memory
- **2.50.** Vulnerable road user secondary safety system
- **2.51.-2.53.** X, Y, Z-direction
- **2.54.** Vehicle roll rate
- **2.55.** Vehicle yaw rate

## 3. Application for Approval
- **3.1.** Submitted by manufacturer or authorized representative to the approval authority.
- **3.2.** Required documentation includes description of vehicle type (EDR location, triggers, storage capacity, resistance), data elements/format, and data retrieval instructions (model in Annex 2).
- **3.3.** A representative vehicle must be submitted for testing.

## 4. Approval
- **4.1.** Granted if vehicle type meets requirements of paragraph 5.
- **4.2.** An approval number is assigned. The first two digits indicate the series of amendments.
- **4.3.** Notices of approval actions communicated to Contracting Parties using form in Annex 1.
- **4.4.** An international approval mark (circle with "E" or oval with "UI") must be affixed to conforming vehicles.
- **4.5.** Mark must be legible and indelible.
- **4.6.** Approval authority must verify satisfactory conformity of production arrangements.

## 5. Requirements
Requirements cover data elements, format, capture, and crash test performance/survivability.
- **5.1. Data Elements:** Vehicles with EDRs must record mandatory data elements under specified conditions, intervals, and sample rates per **Annex 4, Table 1**.
- **5.2. Data Format:** Recorded data must comply with range, accuracy, and resolution in Annex 4, Table 1. Specifies format for acceleration time-history data.
- **5.3. Data Capture:**
    - **5.3.1. Triggering Recording:** An event is recorded if thresholds are met: >8 km/h delta-V (longitudinal/lateral within 150ms), activation of non-reversible occupant restraint system, or activation of VRU secondary safety system (if fitted).
    - **5.3.2. Triggering Locking:** Memory is locked to prevent overwriting after: deployment of non-reversible restraint, frontal impact with >25 km/h delta-V (x-axis, 150ms) if no frontal restraint system, or activation of VRU secondary safety system.
    - **5.3.3. Time Zero:** Defined as the first occurrence of algorithm activation or specific delta-V thresholds.
    - **5.3.4. Overwriting:** Recorded data can be overwritten on a FIFO basis if no free buffer, except data locked per 5.3.2. Data from deployment events overwrites non-locked data.
    - **5.3.5. Power Failure:** Data in non-volatile memory is retained after power loss.
- **5.4. Crash Test Performance and Survivability:** Data must be recorded, exist post-test, and be retrievable after impacts of severity set by UN Regulations Nos. 94, 95, or 137.
- **5.5.** The EDR must not be deactivatable.

## 6. Modification of Vehicle Type and Extension of Approval
- **6.1.** Modifications must be notified. Approval authority may grant extension or require further tests.
- **6.2.-6.3.** Communication of extension/refusal and assignment of extension number.

## 7. Conformity of Production
- **7.1.-7.3.** Production must conform to approved type. Approval authority verifies control methods at least biennially.

## 8. Penalties for Non-Conformity of Production
- **8.1.-8.2.** Approval may be withdrawn for non-conformity, with notification to other Contracting Parties.

## 9. Production Definitively Discontinued
- Manufacturer must inform approval authority, which notifies other Contracting Parties.

## 10. Names and Addresses of Technical Services and Type Approval Authorities
- Contracting Parties communicate details to UN Secretariat.

## 11. Transitional Provisions
- **11.1.** From entry into force of 01 series (8 Oct 2022), Contracting Parties shall not refuse approvals under amended Regulation.
- **11.2.** From 1 July 2024, not obliged to accept new approvals to original version.
- **11.3.** Until 1 July 2026, shall accept approvals to original version issued before 1 July 2024.
- **11.4.** From 1 July 2026, not obliged to accept approvals to original version.
- **11.5.** Continue to accept original version approvals for vehicles unaffected by 01 series amendments.
- **11.6.** Shall not refuse to grant approvals according to preceding amendment series.

## Annexes
- **Annex 1:** Communication form for approval actions.
- **Annex 2:** Information document template for type approval application.
- **Annex 3:** Arrangements of approval marks (E-mark or Unique Identifier).
- **Annex 4:** **Data elements and format (Table 1).** Core technical specification detailing each required data element, its recording condition, interval/time relative to time zero, sample rate, minimum range, accuracy, resolution, and applicable event types (Planar, VRU, Rollover). This table is extensive and defines the precise technical parameters for EDR data recording.
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 10 个
> - 公式 1 个
> - 图像 2 个
> - 全文 Markdown 49,218 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 13)
<table><tr><td rowspan=1 colspan=1>Dataelement</td><td rowspan=1 colspan=1>Recordinginterval/time(relativeto timezero)</td><td rowspan=1 colspan=1>Data sample rate(samples persecond)</td><td rowspan=1 colspan=1>Minimum range</td><td rowspan=1 colspan=1>Accuracy</td><td rowspan=1 colspan=1>Resolution</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 2 (page 15)
**Table 1 **

<table><tr><td>Tabier Data element</td><td>Condition for requirement² Mandatory -</td><td>Recording interval/time (relative to time zero) 0 to 250 ms</td><td>Data sample rate (samples per second) 100</td><td>Minimum range -100 km/h to +±10%</td><td> Accuracy4</td><td>Resolution 1 km/h.</td><td>Event(s) recorded for Planar</td></tr><tr><td>Delta-V, longitudinal</td><td>not required if longitudinal acceleration recorded at ≥500 Hz with sufficient range and resolution to calculate delta-v with required</td><td>or O to End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>100 km/h.</td><td></td><td></td><td></td></tr><tr><td>Maximum delta-V, longitudinal</td><td>accuracy Mandatory - not required if O to End of longitudinal acceleration recorded at ≥500 Hz</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Time, maximum delta-V, longitudinal</td><td>Mandatory - not required if O to End of longitudinal acceleration recorded at ≥500 Hz</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms,whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Speed, vehicle indicated</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 km/h to 250 km/h</td><td>±1 km/h</td><td>1 km/h.</td><td>Planar VRU</td></tr><tr><td>Engine throttle, % full (or accelerator pedal, % full)</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 to 100%</td><td>±5%</td><td>1%</td><td>Planar Rollover VRU</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time³ (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td>Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Service brake，Mandatory on/off</td><td></td><td>-5.0 to 0 sec</td><td>2</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar VRU Rollover</td></tr><tr><td>Ignition cycle, Mandatory crash</td><td></td><td> -1.0 sec</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Planar VRU Rollover</td></tr><tr><td>Ignition cycle, Mandatory download</td><td></td><td>At time of download6</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Planar VRU Rollover</td></tr><tr><td>Safety belt status, driver</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Air bag warning lamp7,</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar Rollover</td></tr><tr><td>Frontal air bag deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in the case of a</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Frontal air bag Mandatory deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in the case of a multi-stage air bag, front</td><td></td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Multi-event crash, number of event</td><td>If Recorded8</td><td>Event</td><td>N/A</td><td>1 or more</td><td>N/A</td><td>1 or more.</td><td>Planar VRU</td></tr><tr><td>Time from event 1 to 2</td><td>Mandatory</td><td>As needed</td><td>N/A</td><td>0 to 5.0 sec</td><td>±0.1 sec</td><td>0.1 sec.</td><td>Rollover Planar Rollover</td></tr><tr><td>Complete file recorded (yes, no)</td><td>Mandatory</td><td>Following other data</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar VRU</td></tr><tr><td>Lateral acceleration</td><td>If Recorded</td><td>0-250 ms or O to End of Event Time</td><td>500Hz</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Rollover Planar Rollover</td></tr><tr><td>(post-crash)</td><td></td><td>plus 30 ms, whichever is shorter. 0-250 ms or</td><td></td><td></td><td>+/- 10%</td><td></td><td>Planar</td></tr><tr><td>Longitudinal acceleration (post-crash)</td><td>If Recorded</td><td>0 to End of Event Time plus 30 ms, whichever is shorter.</td><td>500Hz</td><td>-50 to +50g</td><td></td><td>1g</td><td></td></tr><tr><td>Normal acceleration (post-crash)</td><td>If recorded</td><td>-1.0 to 5.0 sec9</td><td>10Hz</td><td>-5 g t0+5g</td><td>±10%</td><td>0.5g</td><td>Rollover</td></tr><tr><td>Delta-V, lateral</td><td>Mandatory - not required if O to End of lateral acceleration recorded at ≥500 Hz and with sufficient range and resolution to calculate</td><td>0-250 ms or Event Time plus 30 ms, whichever is shorter.</td><td>100</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td>Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Maximum delta-V,lateral</td><td>Mandatory - not required if O to End of lateral acceleration recorded at ≥500 Hz</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Time maximum delta-V, lateral</td><td>Mandatory - not required if O to End of lateral acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Time for maximum delta-V,</td><td>shorter. Mandatory - not required if O to End of relevant acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Engine rpm</td><td>≥500 Hz Mandatory</td><td>shorter. -5.0 to 0 sec</td><td>2</td><td>0 to 10,000 rpm ±100</td><td>rpm10</td><td>100 rpm.</td><td>Planar Rollover</td></tr><tr><td>Vehicle roll angle</td><td>If recorded</td><td>-1.0 up to 5.0 10 sec</td><td></td><td>-1080 deg to + 1080 deg.</td><td>±10%</td><td>10 deg.</td><td>Rollover</td></tr><tr><td>Vehicle roll rate</td><td>Mandatory if fitted and used for rollover protection system control</td><td>-1.0 up to 5.0 10 secl1</td><td></td><td>-240 to + 240 deg/sec</td><td>+/- 10%12</td><td>1 deg/sec</td><td>Rollover</td></tr><tr><td>ABS activity</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, Active, N/A Intervening13</td><td></td><td>Faulted, Active, Intervening12</td><td>Planar VRU</td></tr><tr><td>Stability control</td><td>Mandatory</td><td>-5.0 to0 sec2</td><td></td><td>Faulted, On, Off, Intervening12</td><td>N/A</td><td>Faulted, On, Off, Intervening12</td><td>Planar VRU</td></tr><tr><td>Steering input</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td></td><td>-250 deg CW to ±5% + 250 deg CCw.</td><td></td><td>±1%.</td><td>Planar VRU</td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time³ (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Safety belt status, front passenger</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Passenger air bag suppression status, front</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Suppressed or not suppressed</td><td>N/A</td><td>Suppressed or Planar not suppressed</td><td>Rollover</td></tr><tr><td>Frontal air bag deployment, time to nth stage, driver4.</td><td>Mandatory ifEvent fitted with a driver's frontal air bag with a multi- stage inflator.</td><td></td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Frontal air bag deployment, time to nth stage, front passenger14.</td><td>Mandatory if fitted with a front passenger's frontal air bag with a multi-</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side air bag deployment, time to deploy,</td><td>stage inflator. Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>driver. Side air bag deployment, time to deploy, front</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>passenger. Side curtain/tube air bag deployment, time to deploy,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>driver side. Side curtain/tube air bag deployment,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Pretensioner deployment, time to fire, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td colspan="8"></td></tr><tr><td>Data element Pretensioner</td><td>Condition for requirement² Mandatory</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range 0 to 250 ms</td><td>Accuracy4 ±2 ms</td><td>Resolution</td><td>Event(s) recorded for Planar</td></tr><tr><td>deployment, time to fire, front passenger.</td><td></td><td>Event</td><td>N/A</td><td></td><td></td><td>1 ms.</td><td>Rollover</td></tr><tr><td>Seat track position switch, foremost, status, driver.</td><td>Mandatory if -1.0 sec fitted and used for deployment</td><td></td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Seat track position switch, foremost,</td><td>decision Mandatory if fitted and used for deployment</td><td>f-1.0 sec</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>status, front passenger. Occupant size classification,</td><td>decision If recorded</td><td>-1.0 sec</td><td>N/A</td><td>5th percentileN/A</td><td></td><td>Yes or No.</td><td>Planar</td></tr><tr><td>driver Occupant size classification,</td><td>If recorded</td><td>-1.0 sec</td><td>N/A</td><td>female or larger. 6yr old HII USN/A</td><td></td><td>Yes or No.</td><td>Rollover Planar</td></tr><tr><td>front passenger Safety belt</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>ATD or Q6 ATD or smaller Fastened, not</td><td>N/A</td><td>Fastened, not</td><td>Rollover Planar</td></tr><tr><td>status, rear passengers Tyre Pressure</td><td>Mandatory</td><td>-1.0 second</td><td>N/A</td><td>fastened N/A</td><td>N/A</td><td>fastened On, Off</td><td>Rollover Planar</td></tr><tr><td>Monitoring System (TPMS) Warning Lamp Status</td><td></td><td>relative to time zero</td><td></td><td></td><td></td><td></td><td>Rollover</td></tr><tr><td>Longitudinal acceleration (pre -crash)</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2Hz</td><td>-1.5g to +1.5g</td><td>+/- 10%</td><td>0.1g</td><td>Planar VRU</td></tr><tr><td>Lateral acceleration (pre - crash)</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2 Hz</td><td>-1.0g to +1.0g</td><td>+/- 10%</td><td>0.1g</td><td>Planar</td></tr><tr><td>Yaw Rate</td><td>Mandatory</td><td>-5 to0 seconds relative to</td><td>2</td><td>-75 to +75 degrees /second the full</td><td>±10% of0.1 range of</td><td></td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td>Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Traction Control Status</td><td>Mandatory if not fitted with second ESC</td><td>-5.0 to 0 relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Actively controlling, Faulted, Commanded Off, or On but Not</td><td>Planar Rollover</td></tr><tr><td>AEBS status</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Actively Warning, Actively Engaged,</td><td>Planar VRU Rollover</td></tr><tr><td>Cruise Control System</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Not Active Actively Controlling, Faulted, Commanded Off, On but</td><td>Planar VRU</td></tr><tr><td>Adaptive Cruise Control Status (driving automation system level 1)</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Controlling Actively Controlling, Faulted, Commanded Off, On but</td><td>Planar VRU Rollover</td></tr><tr><td>VRU secondary safety system deployment,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>Controlling 1 ms</td><td>VRU</td></tr><tr><td>time to deploy VRU secondary Mandatory safety system warning</td><td></td><td>-1.1 to 0 relative to time zero</td><td>N/A</td><td>N/A</td><td>N/A</td><td>On or Off</td><td>VRU</td></tr><tr><td>indicator status15 Safety belt status mid-</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>position front Far side impact Mandatory center airbag</td><td></td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>+/-2 ms</td><td>1 ms</td><td>Planar</td></tr></table>

#### 表 3 (page 16)
#### 表 4 (page 17)
#### 表 5 (page 18)
#### 表 6 (page 19)
#### 表 7 (page 20)
#### 表 8 (page 21)
#### 表 9 (page 22)
<table><tr><td>Data element Lane departure Mandatory</td><td>Condition for requirement2</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second) 2</td><td>Minimum range N/A</td><td>Accuracy4 N/A</td><td>Resolution Faulted,</td></tr><tr><td>warning system status</td><td></td><td>-5.0 to 0 sec</td><td></td><td></td><td></td><td>Off, On but not warning, On - Warning left, On - Warning</td></tr><tr><td>Corrective steering function (CSF) status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>right Faulted, Off, On but not intervening, On - Actively intervening</td></tr><tr><td>Emergency steering function (ESF) status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not intervening, On －Actively intervening</td></tr><tr><td>Automatically commanded steering function (ACSF) category A status</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not controlling, On - Actively</td></tr><tr><td>Automatically commanded steering function (ACSF) category B1 status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling Faulted, Off, On but not controlling, On － Actively</td></tr><tr><td>Automatically commanded steering function (ACSF) category B2</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling Faulted, Off, On but not controlling, On －Actively</td></tr><tr><td>status Automatically commanded steering function (ACSF) category C status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling Faulted, Off, On but not controlling, On - Actively controlling</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td>Accuracy4</td><td>Resolution</td></tr><tr><td>Automatically commanded steering function (ACSF) category D</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not controlling, On - Actively</td></tr><tr><td>AutomaticallyMandatory commanded steering function (ACSF) category E status</td><td></td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>controlling Faulted, Off, On but not controlling, On - Actively</td></tr><tr><td>Accident emergency call</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>N/A</td><td>N/A</td><td>controlling Faulted, On but emergency call not automatically triggered,</td></tr></table>

#### 表 10 (page 23)
### 公式（取前 1 个）

**公式 1** (page 14):

$$
\mathrm { a } = 8 \mathrm { m m } \mathrm { m i n }
$$

### 图像（取前 2 张）

![图 page 12](../_mineru_assets/ECE R160 Rev1/83a93bad6f0836d97229512607d5eec4128d5c9a2fe5998047660df66d69a0bc.jpg)  

![图 page 14](../_mineru_assets/ECE R160 Rev1/12069d7d15b609019e37d5c2705737d62fd07255bcbd04d0b74d1e8826d39d6a.jpg)  

