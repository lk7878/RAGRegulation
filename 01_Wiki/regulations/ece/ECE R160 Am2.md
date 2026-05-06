---
reg_id: ECE R160 Am2
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Event Data Recorder
status: active
standard_body: UNECE
publication_date: 2022-11-24
implementation_date_new_vehicle: 2022-10-08
source: E/ECE/TRANS/505/Rev.3/Add.159/Amend.2
source_url: https://unece.org/transport/documents/2022/11/standards/un-regulation-no-160-event-data-recorder
topics:
- event data recorder
- EDR
- vehicle safety
- data recording
- crash data
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\160\R160am2e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
技术要求_限值_conf: low
cross_check_flags:
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及“在用车辆实施日期”。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及替代关系。
- field: 技术要求_限值
  status: normalized
  extracted: 'Delta-V, longitudinal: 记录间隔: 0 to 250 ms or 0 to End of Event Time plus
    30 ms, whichever is shorter.; 采样率: 100; 最小范围: -100 km/h to +100 km/h; 精度: ±10%;
    分辨率: 1 km/h; 记录事件: Planar'
  original: 'Delta-V, longitudinal: 记录间隔: 0 to 250 ms or 0 to End of Event Time plus
    30 ms, whichever is shorter.; 采样率: 100; 最小范围: -100 km/h to +100 km/h; 精度: ±10%;
    分辨率: 1 km/h.; 记录事件: Planar'
  note: A中“分辨率”值为“1 km/h”，B中为“1 km/h.”（多一个句点）。此差异微小，但严格核对为不一致。
  recheck_reason: 原文中“分辨率”值为“1 km/h.”，抽取数据为“1 km/h”，差异仅为末尾句点，属于格式规范化，实质一致。
recheck_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: 3b2285eecc1eb847
_mineru_outputs_dir: outputs/3b2285eecc1eb847
_mineru_blocks:
  tables: 1
  formulas: 0
  images: 0
_mineru_merged_at: '2026-04-22'
---

# UN Regulation No. 160 - Event Data Recorder (Amendment 2)

**Supplement 1 to the original version of the Regulation – Date of entry into force: 8 October 2022**

This document constitutes **Amendment 2** to UN Regulation No. 160. The authentic and legally binding text is: ECE/TRANS/WP.29/2022/25/Rev.1.

## 1. Scope Clarification
Paragraph 1.3 is amended to read:
> "1.3. The following data elements are excluded from the scope: VIN, associated vehicle details, location/positioning data, information of the driver, date and time of an event."

## 2. Definitions
The following definitions are amended:

*   **2.1. "Anti-lock braking activity"** means the anti-lock brake system is actively controlling the vehicle's brakes.
*   **2.14. "Ignition cycle, crash"** means the number (count) of power mode cycles as determined by the EDR ECU at the time when the crash event occurred since the first use of the EDR.
*   **2.15. "Ignition cycle download"** means the number (count) of power mode cycles as determined by the EDR ECU at the time when the data was downloaded since the first use of the EDR.
*   **2.29. “Rollover”** means any vehicle rotation of 90 degrees or more about any true longitudinal or lateral axis.
*   **2.52. "X-direction"** means in the direction of the vehicle’s X-axis, which is parallel to the vehicle's longitudinal centreline. The X-direction is positive in the direction of forward vehicle travel.

**Paragraphs 2.54., 2.55., are deleted.**
Paragraphs 2.29. to 2.53., are renumbered as 2.30. to 2.54., respectively.

## 3. Data Locking Conditions
Paragraph 5.3.2. is amended to read:
> "5.3.2. Conditions for triggering locking of data
> In the circumstances provided below, the memory for the event shall be locked to prevent any future overwriting of the data by subsequent events."

## 4. Annex 4 - Data Element Specifications
Table 1 in Annex 4 is amended. Key specifications for mandatory and conditional data elements are summarized below. "Mandatory" is subject to the conditions detailed in Section 1 of the regulation.

| Data element | Condition for requirement | Recording interval/time (relative to time zero) | Data sample rate (samples per second) | Minimum range | Accuracy | Resolution | Event(s) recorded for |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Delta-V, longitudinal** | Mandatory - not required if longitudinal acceleration recorded at ≥500 Hz | 0 to 250 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | 100 | -100 km/h to +100 km/h | ±10% | 1 km/h | Planar |
| **Maximum delta-V, longitudinal** | Mandatory - not required if longitudinal acceleration recorded at ≥500 Hz | 0–300 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | N/A | -100 km/h to +100 km/h | ±10% | 1 km/h | Planar |
| **Time, maximum delta-V, longitudinal** | Mandatory - not required if longitudinal acceleration recorded at ≥500 Hz | 0–300 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | N/A | 0–300 ms, or 0- End of Event Time plus 30 ms, whichever is shorter. | ±3 ms | 2.5 ms | Planar |
| **Speed, vehicle indicated** | Mandatory | -5.0 to 0 sec | 2 | 0 km/h to 250 km/h | ±1 km/h | 1 km/h | Planar, VRU, Rollover |
| **Engine throttle, % full (or accelerator pedal, % full)** | Mandatory | -5.0 to 0 sec | 2 | 0 to 100% | ±5% | 1% | Planar, VRU, Rollover |
| **Service brake, on/off** | Mandatory | -5.0 to 0 sec | 2 | On or Off | N/A | On or Off | Planar, VRU, Rollover |
| **Ignition cycle, crash** | Mandatory | -1.0 sec | N/A | 0 to 60,000 | ±1 cycle | 1 cycle | Planar, VRU, Rollover |
| **Ignition cycle, download** | Mandatory | At time of download | N/A | 0 to 60,000 | ±1 cycle | 1 cycle | Planar, VRU, Rollover |
| **Safety belt status, driver** | Mandatory | -1.0 sec | N/A | Fastened, not fastened | N/A | Fastened, not fastened | Planar, Rollover |
| **Air bag warning lamp** | Mandatory | -1.0 sec | N/A | On or Off | N/A | On or Off | Planar, Rollover |
| **Frontal air bag deployment time, driver** | Mandatory | Event | N/A | 0 to 250 ms | ±2ms | 1 ms | Planar |
| **Frontal air bag deployment time, front passenger** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar |
| **Multi-event crash, number of events** | If Recorded | Event | N/A | 1 or more | N/A | 1 or more | Planar, VRU, Rollover |
| **Time from event 1 to 2** | Mandatory | As needed | N/A | 0 to 5.0 sec | ±0.1 sec | 0.1 sec | Planar, Rollover |
| **Complete file recorded** | Mandatory | Following other data | N/A | Yes or No | N/A | Yes or No | Planar, VRU, Rollover |
| **Lateral acceleration** | If Recorded | 0–250 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | 500 | -50 to +50g | +/- 10% | 1 g | Planar, Rollover |
| **Longitudinal acceleration** | If Recorded | 0–250 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | 500 | -50 to +50g | +/- 10% | 1 g | Planar |
| **Normal acceleration** | If recorded | 0 to at least 250 ms | 10 | -5 g to +5 g | ± 10% | 0.5 g | Rollover |
| **Delta-V, lateral** | Mandatory - not required if lateral acceleration recorded at ≥500 Hz | 0–250 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | 100 | -100 km/h to +100 km/h | ±10% | 1 km/h | Planar |
| **Maximum delta-V, lateral** | Mandatory - not required if lateral acceleration recorded at ≥500 Hz | 0–300 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | N/A | -100 km/h to +100 km/h | ±10% | 1 km/h | Planar |
| **Time maximum delta-V, lateral** | Mandatory - not required if lateral acceleration recorded at ≥500 Hz | 0–300 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | N/A | 0–300 ms, or 0- End of Event Time plus 30 ms, whichever is shorter. | ±3 ms | 2.5 ms | Planar |
| **Time for maximum delta-V, resultant.** | Mandatory - not required if relevant acceleration recorded at ≥500 Hz | 0–300 ms or 0 to End of Event Time plus 30 ms, whichever is shorter. | N/A | 0–300 ms, or 0- End of Event Time plus 30 ms, whichever is shorter. | ±3 ms | 2.5 ms | Planar |
| **Engine rpm** | Mandatory | -5.0 to 0 sec | 2 | 0 to 10,000 rpm | ±100 rpm | 100 rpm | Planar, Rollover |
| **Vehicle roll angle** | If recorded | 0 to at least 250 ms | 10 | -1080 deg to +1080 deg | ±10% | 10 deg | Rollover |
| **Anti-lock braking system activity** | Mandatory | -5.0 to 0 sec | 2 | Faulted, Non-Engaged, Engaged | N/A | Faulted, Non-Engaged, Engaged | Planar, VRU, Rollover |
| **Stability control** | Mandatory | -5.0 to 0 sec | 2 | Faulted, On, Off, Engaged | N/A | Faulted, On, Off, Engaged | Planar, VRU, Rollover |
| **Steering input** | Mandatory | -5.0 to 0 sec | 2 | -250 deg CW to + 250 deg CCW | ±5% | ±1% | Planar, Rollover, VRU |
| **Safety belt status, front passenger** | Mandatory | -1.0 sec | N/A | Fastened, not fastened | N/A | Fastened, not fastened | Planar, Rollover |
| **Passenger air bag suppression status, front** | Mandatory | -1.0 sec | N/A | suppressed or not suppressed | N/A | suppressed or not suppressed | Planar, Rollover |
| **Frontal air bag deployment, time to nth stage, driver** | Mandatory if fitted with a driver’s frontal air bag with a multi-stage inflator. | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar |
| **Frontal air bag deployment, time to nth stage, front passenger** | Mandatory if fitted with a front passenger’s frontal air bag with a multi-stage inflator. | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar |
| **Side air bag deployment time, driver** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar |
| **Side air bag deployment time, front passenger** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar |
| **Side curtain/tube air bag deployment time, driver side** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar, Rollover |
| **Side curtain/tube air bag deployment time, passenger side** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar, Rollover |
| **Pretensioner deployment time, driver** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar, Rollover |
| **Pretensioner deployment time, front passenger** | Mandatory | Event | N/A | 0 to 250 ms | ±2 ms | 1 ms | Planar, Rollover |
| **Seat track position switch, foremost, status, driver** | Mandatory if fitted and used for deployment decision | -1.0 sec | N/A | Yes or No | N/A | Yes or No | Planar, Rollover |
| **Seat track position switch, foremost, status, front passenger** | Mandatory if fitted and used for deployment decision | -1.0 sec | N/A | Yes or No | N/A | Yes or No | Planar, Rollover |
| **Occupant size classification, driver** | If recorded | -1.0 sec | N/A | 5th percentile female or larger. | N/A | Yes or No | Planar, Rollover |
| **Occupant size classification, front passenger** | If recorded | -1.0 sec | N/A | 6yr old HIII US ATD or Q6 ATD or smaller | N/A | Yes or No | Planar, Rollover |

**Table Notes:**
1.  "If recorded" means if the data is recorded in non-volatile memory for the purpose of subsequent downloading.
2.  For rollover events, the recording interval is relative to the time at which the event is determined to have started as defined by the manufacturer.
3.  Pre-crash data and crash data are asynchronous. The sample time accuracy requirement for pre-crash time is -0.1 to 1.0 sec.
4.  For data elements with system states, the term “engaged” also means “actively controlling” or “actively intervening” and “non-engaged” also means “on but not controlling”. Likewise, “off” also means “deactivated”.
5.  Accuracy requirement only applies within the range of the physical sensor. If measurements captured by a sensor exceed the design range of the sensor, the reported element shall indicate when the measurement first exceeded the design range of the sensor.
6.  "Planar" includes triggered events in sections 5.3.1.1, 5.3.1.2, and 5.3.1.3 and “VRU” includes triggered events in section 5.3.1.4.
7.  The ignition cycle at the time of download is not required to be recorded at the time of the crash but shall be reported during the download process.
8.  The air bag warning lamp is the readiness indicator specified in national air bag requirements and may also illuminate to indicate a malfunction in another part of the deployable restraint system.
9.  List this element n times, once for each device (e.g., each front passenger air bag).
10. "If recorded" means if the data is recorded in non-volatile memory for the purpose of subsequent downloading.
11. For rollover events the time at which the event is determined to have started as defined by the manufacturer.
12. These elements (e.g., Engine rpm) do not need to meet the accuracy and resolution requirements in specified crash tests.
13. List this element n - 1 times, once for each stage of a multi-stage air bag system.
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 6 个
> - 公式 0 个
> - 图像 0 个
> - 全文 Markdown 14,041 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 6 个）

#### 表 1 (page 2)
**"Table 1 **

<table><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range4</td><td>Accuracy5</td><td>Resolution4</td><td>Event(s) recorded forb</td></tr><tr><td>Delta-V, longitudinal</td><td>Mandatory - not required if longitudinal acceleration recorded at ≥500 Hz with shorter. sufficient range and</td><td>0 to 250 ms or O to End of Event Time plus 30 ms, whichever is</td><td>100</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Maximum delta-V, longitudinal</td><td>Mandatory - not required if O to End of longitudinal acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>-100 km/h to +±10% 100 km/h.</td><td></td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Time, maximum delta-V, longitudinal</td><td>Mandatory - not required if O to End of longitudinal acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Speed, vehicle indicated</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 km/h to 250 km/h</td><td>±1 km/h</td><td>1 km/h.</td><td>Planar VRU</td></tr><tr><td>Engine throttle, % full (or accelerator pedal, % full)</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 to 100%</td><td>±5%</td><td>1%</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range4</td><td> Accuracy5</td><td>Resolution4</td><td>Event(s) recorded for</td></tr><tr><td rowspan="4">Service brake, on/off</td><td rowspan="4">Mandatory</td><td rowspan="4">-5.0 to 0 sec</td><td rowspan="4">2</td><td rowspan="4">On or Off</td><td rowspan="4">N/A</td><td>On or Off.</td><td>Planar</td></tr><tr><td></td><td>VRU</td></tr><tr><td></td><td>Rollover</td></tr><tr><td></td><td>Planar</td></tr><tr><td rowspan="3">crash</td><td rowspan="3">Ignition cycle， Mandatory</td><td rowspan="3">-1.0 sec</td><td rowspan="3">N/A</td><td rowspan="3">0 to 60,000</td><td rowspan="3">±1 cycle1 cycle.</td><td rowspan="3"></td><td></td></tr><tr><td>VRU</td></tr><tr><td>Rollover</td></tr><tr><td rowspan="2">download</td><td rowspan="2">Ignition cycle， Mandatory</td><td rowspan="2">At time of download7</td><td rowspan="2">N/A</td><td rowspan="2">0 to 60,000</td><td rowspan="2">±1 cycle</td><td rowspan="2">1 cycle.</td><td>Planar</td></tr><tr><td>VRU Rollover</td></tr><tr><td rowspan="2">Safety belt status, driver</td><td rowspan="2">Mandatory</td><td rowspan="2"> -1.0 sec</td><td rowspan="2">N/A</td><td rowspan="2">Fastened, not fastened</td><td rowspan="2">N/A</td><td rowspan="2">Fastened,</td><td>Planar</td></tr><tr><td>not fastened Rollover</td></tr><tr><td rowspan="2">Air bag warning lamp8</td><td rowspan="2">Mandatory</td><td rowspan="2"> -1.0 sec</td><td rowspan="2">N/A</td><td rowspan="2">On or Off</td><td rowspan="2">N/A</td><td rowspan="2">On or Off.</td><td>Planar</td></tr><tr><td>Rollover</td></tr><tr><td rowspan="4">deployment, time to deploy, in the case of a single stage air bag, or time to</td><td rowspan="4">Frontal air bag Mandatory</td><td rowspan="4">Event</td><td rowspan="4">N/A</td><td rowspan="4">0 to 250 ms</td><td rowspan="4">±2ms</td><td rowspan="4">1 ms.</td><td>Planar</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td rowspan="4">deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in</td><td rowspan="4">Frontal air bag Mandatory</td><td rowspan="4">Event</td><td rowspan="4">N/A</td><td rowspan="4">0 to 250 ms</td><td rowspan="4">±2 ms</td><td rowspan="4">1 ms.</td><td rowspan="4"></td></tr><tr><td>Planar</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range4</td><td>Accuracy</td><td>Resolution4</td><td colspan="2">Event(s) recorded for6</td></tr><tr><td>Multi-event crash, number of events</td><td>If Recorded10</td><td>Event</td><td>N/A</td><td>1 or more</td><td>N/A</td><td>1 or more.</td><td colspan="2">Planar VRU Rollover</td></tr><tr><td>Time from event 1 to 2</td><td>Mandatory</td><td>As needed</td><td>N/A</td><td>0 to 5.0 sec</td><td>±0.1 sec</td><td>0.1 sec.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Complete fileMandatory recorded</td><td></td><td>Following other data</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td colspan="2">Planar VRU Rollover</td></tr><tr><td>Lateral acceleration (post-crash)</td><td>If Recorded</td><td>0-250 ms or 0 to End of Event Time plus 30 ms, whichever is shorter.11</td><td>500</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td colspan="2">Planar Rollover</td></tr><tr><td>Longitudinal acceleration (post-crash)</td><td> If Recorded</td><td>0-250 ms or 0 to End of Event Time plus 30 ms, whichever is</td><td>500</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td colspan="2">Planar</td></tr><tr><td>Normal acceleration (post-crash)</td><td>If recorded</td><td>O to at least 250 ms11</td><td>10</td><td>-5 g to+5g</td><td>±10%</td><td>0.5g</td><td colspan="2">Rollover</td></tr><tr><td>lateral</td><td>Mandatory - 0-250 ms or not required if O to End of lateral acceleration recorded at ≥500 Hz and with sufficient range and resolution to</td><td>Event Time plus 30 ms, whichever is shorter.</td><td></td><td>100 km/h.</td><td></td><td></td><td colspan="2">Planar</td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range4</td><td>Accuracy5</td><td>Resolution4</td><td colspan="2">Event(s) recorded for</td></tr><tr><td>Maximum delta-V, lateral</td><td>Mandatory - lateral acceleration recorded at ≥500 Hz</td><td>0-300 ms or not required if O to End of Event Time plus 30 ms, whichever is</td><td>N/A</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td colspan="2">Planar</td></tr><tr><td>Time maximum delta-V,lateral lateral</td><td>Mandatory - acceleration recorded at ≥500 Hz</td><td>0-300 ms or not required if O to End of Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td colspan="2">Planar</td></tr><tr><td>Time for maximum delta-V, resultant.</td><td>Mandatory - not required if O to End of relevant acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td colspan="2">Planar</td></tr><tr><td>Engine rpm</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>0 to 10,000 rpm ±100</td><td>rpm12</td><td>100 rpm.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Vehicle roll angle</td><td>If recorded</td><td>O to at least 250 ms11</td><td>10</td><td>-1080 deg to + 1080 deg.</td><td>±10%</td><td>10 deg.</td><td colspan="2">Rollover</td></tr><tr><td>Anti-lock braking system activity</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, Non- Engaged, Engaged</td><td>N/A</td><td>Faulted, Non- Engaged, Engaged</td><td colspan="2">Planar VRU Rollover</td></tr><tr><td>Stability control</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, On, Off, Engaged</td><td>N/A</td><td>Faulted, On, Off, Engaged</td><td colspan="2">Planar VRU Rollover</td></tr><tr><td></td><td>Steering inputMandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>-250 deg CW to ±5% +250 deg CCW.</td><td></td><td>±1%.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Safety belt status, front passenger 9</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td colspan="2">Planar Rollover</td></tr><tr><td>Passenger air bag suppression status, front 9</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>suppressed or not suppressed</td><td>N/A</td><td>suppressed or not suppressed</td><td colspan="2">Planar Rollover</td></tr><tr><td rowspan="2">Data element Frontal air bag</td><td rowspan="2">Condition for requirement2 Mandatory if fitted with a</td><td rowspan="2">Recording interval/time (relative to time zero) Event N/A</td><td rowspan="2">Data sample rate (samples per second) Minimum range4</td><td rowspan="2">0 to 250 ms</td><td rowspan="2"> Accuracy5</td><td rowspan="2">Resolution4</td><td colspan="2" rowspan="2">Event(s) recorded for Planar</td></tr><tr><td>±2 ms 1 ms.</td></tr><tr><td>deployment, time to nth stage, driver13.</td><td>driver's frontal air bag with a multi- stage inflator.</td><td></td><td></td><td></td><td></td><td></td><td colspan="2"></td></tr><tr><td>Frontal air bag deployment, time to nth stage, front passenger13, 9.</td><td>Mandatory if Event fitted with a front passenger's frontal air bag with a multi- stage inflator.</td><td></td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td colspan="2">Planar</td></tr><tr><td>Side air bag deployment, time to deploy, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td colspan="2">Planar</td></tr><tr><td>Side air bag deployment, time to deploy, front passenger.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td colspan="2">Planar</td></tr><tr><td>Side curtain/tube air bag deployment, time to deploy,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms.</td><td colspan="2">Planar Rollover</td></tr><tr><td>driver side. Side curtain/tube air bag deployment, time to deploy,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td colspan="2">Planar Rollover</td></tr><tr><td>passenger side. Pretensioner deployment, time to fire, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Pretensioner deployment, time to fire, front passenger9.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range4</td><td> Accuracy5</td><td>Resolution4</td><td colspan="2">Event(s) recorded forb</td></tr><tr><td>Seat track position switch, foremost, status, driver.</td><td>Mandatory if -1.0 sec fitted and used for deployment decision</td><td></td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Seat track position switch, foremost, status, front passenger9.</td><td>Mandatory if-1.0 sec fitted and used for deployment decision</td><td></td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td colspan="2">Planar Rollover</td></tr><tr><td>Occupant size classification, driver</td><td>If recorded</td><td>-1.0 sec</td><td>N/A</td><td>5th percentile female or larger.</td><td>N/A</td><td>Yes or No.</td><td colspan="2">Planar Rollover</td></tr><tr><td>classification, front passenger9.</td><td>Occupant sizeIf recorded</td><td>-1.0 sec</td><td>N/A</td><td>6yr old HIII USN/A ATD or Q6 ATD or smaller</td><td></td><td>Yes or No.</td><td colspan="2">Planar Rollover</td></tr></table>

#### 表 2 (page 3)
#### 表 3 (page 4)
#### 表 4 (page 5)
#### 表 5 (page 6)
#### 表 6 (page 7)
