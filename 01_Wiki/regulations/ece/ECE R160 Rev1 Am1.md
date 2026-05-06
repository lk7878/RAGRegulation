---
reg_id: ECE R160 Rev1 Am1
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Event Data Recorder
status: active
standard_body: UNECE
publication_date: 2022-11-24
implementation_date_new_vehicle: 2022-10-08
source_file: R160r1am1e.pdf
topics:
- Event Data Recorder
- EDR
- vehicle safety
- data recording
- crash data
amendments:
- UN R160 Revision 1
- 01 series of amendments
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\160\R160r1am1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及针对在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及取代关系。
_ocr_upgraded: mineru
_mineru_content_hash: e80028d38b8fd89a
_mineru_outputs_dir: outputs/e80028d38b8fd89a
_mineru_blocks:
  tables: 1
  formulas: 0
  images: 0
_mineru_merged_at: '2026-04-23'
---

**UN Regulation No. 160 - Event Data Recorder (Amendment 1 to Revision 1)**

This document constitutes **Amendment 1** to **Revision 1** of **UN Regulation No. 160**, supplementing the 01 series of amendments. The authentic legal text is referenced as `ECE/TRANS/WP.29/2022/26`.

**Key Amendments:**

**1. Scope Exclusion (Paragraph 1.3):**
   The following data elements are explicitly excluded from the regulation's scope:
   *   Vehicle Identification Number (VIN)
   *   Associated vehicle details
   *   Location/positioning data
   *   Information of the driver
   *   Date and time of an event

**2. New and Revised Definitions (Paragraph 2):**
   Numerous new definitions are inserted, and several existing ones are amended. Key additions include:
   *   **Accident Emergency Call System:** A system activated automatically or manually that transmits crash data and establishes an audio emergency channel.
   *   **Advanced emergency braking system status:** The operating status of a forward collision detection and automatic braking system.
   *   **Automatically commanded steering function categories (A through E):** Definitions for various levels of automated steering assistance, from low-speed/parking assistance (Cat A) to continuous lane change execution without driver confirmation (Cat E).
   *   **Corrective steering function:** A function that automatically adjusts steering to compensate for sudden side forces, improve stability, or correct lane departure.
   *   **Emergency Steering Function:** A function that automatically steers to avoid or mitigate an imminent collision.
   *   **Lane Departure Warning System**
   *   **Rollover:** Defined as any vehicle rotation of 90 degrees or more about any true longitudinal or lateral axis.
   *   **Tyre Pressure Monitoring System**
   *   Amended definitions for terms like **Anti-lock brake system activity**, **Ignition cycle (crash & download)**, and vehicle axis rates (**Vehicle roll rate**, **Vehicle yaw rate**, **X-direction**).

**3. Data Locking (Paragraph 5.3.2):**
   Specifies conditions under which the event data memory must be locked to prevent overwriting by subsequent events.

**4. Revised Data Element Specifications (Annex 4, Table 1):**
   The core data recording table is extensively amended, detailing for each data element:
   *   **Condition for requirement** (e.g., Mandatory, If recorded)
   *   **Recording interval/time** (relative to time zero)
   *   **Data sample rate**
   *   **Minimum range**
   *   **Accuracy**
   *   **Resolution**
   *   **Event(s) recorded for** (Planar, Rollover, VRU - Vulnerable Road User)

   The table includes a wide array of data elements, such as:
   *   **Delta-V and Acceleration** (longitudinal, lateral, normal)
   *   **Vehicle speed and engine parameters** (throttle, RPM)
   *   **System statuses:** Service brake, ABS, Stability control, Traction control, Cruise control, Adaptive cruise control, Lane departure warning, Various steering functions (Corrective, Emergency, Automatically Commanded A-E), Accident emergency call system.
   *   **Occupant Protection:** Safety belt status (driver, front passenger, rear), Air bag deployment times (frontal, side, curtain, pretensioners, far-side), Air bag warning lamp, Occupant size classification, Passenger air bag suppression.
   *   **Other:** Ignition cycles, Multi-event crash count, Complete file recorded, Tyre Pressure Monitoring System warning lamp status, Vulnerable road user safety system deployment and warning status.

**Notes:**
*   Pre-crash and crash data are asynchronous. Pre-crash time sample accuracy is -0.1 to +1.0 seconds.
*   For system states, "engaged" also means "actively controlling/intervening"; "not-engaged" means "on but not controlling"; "off" means "deactivated".
*   Accuracy requirements apply only within the physical sensor's design range. If exceeded, the data must indicate when the range was first exceeded.
*   "Planar" events refer to those triggered under sections 5.3.1.1 to 5.3.1.3. "VRU" events refer to those under section 5.3.1.4.
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 9 个
> - 公式 0 个
> - 图像 0 个
> - 全文 Markdown 23,321 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 9 个）

#### 表 1 (page 3)
**Table 1 **

<table><tr><td>Data element</td><td>Condition for requirementl</td><td>Recording interval/time2 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range3</td><td> Accuracy4</td><td>Resolution4</td><td>Event(s) recorded for5</td></tr><tr><td>Delta-V, longitudinal</td><td>Mandatory - longitudinal acceleration recorded at ≥500 Hz with sufficient range and resolution to</td><td>0 to 250 ms not required if or O to End of Event Time plus 30 ms, whichever is shorter.</td><td>100</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Maximum delta-V, longitudinal</td><td>Mandatory - not required if O to End of longitudinal acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Time, maximum delta-V, longitudinal</td><td>Mandatory - longitudinal acceleration recorded at</td><td>0-300 ms or not required if O to End of Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Speed, vehicle indicated</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>0 km/h to 250 km/h</td><td>±1 km/h</td><td>1 km/h.</td><td>Planar Rollover</td></tr><tr><td>Engine throttle, % full (or accelerator pedal, % full)</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>0 to 100%</td><td>±5%</td><td>1%</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirementl</td><td>Recording interval/time² (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range3</td><td> Accuracy4</td><td>Resolution4</td><td>Event(s) recorded for</td></tr><tr><td>Service brake, on/off</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar VRU Rollover</td></tr><tr><td>Ignition cycle, Mandatory crash</td><td></td><td> -1.0 sec</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Planar VRU Rollover</td></tr><tr><td>Ignition cycle, download</td><td>Mandatory</td><td>At time of download6</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Planar VRU Rollover</td></tr><tr><td>Safety belt status, driver</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Air bag warning lamp7,</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar Rollover</td></tr><tr><td>deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in the case of a</td><td>Frontal air bag Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>bag, driver. Frontal air bag Mandatory deployment, time to deploy, in the case of a single stage air bag, or time to first stage deployment, in the case of a multi-stage air bag, front</td><td></td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Multi-event crash, number of event</td><td>If Recorded9</td><td>Event</td><td>N/A</td><td>1 or more</td><td>N/A</td><td>1 or more.</td><td>Planar VRU Rollover</td></tr><tr><td>Time from event 1 to 2</td><td>Mandatory</td><td>As needed</td><td>N/A</td><td>0 to 5.0 sec</td><td>±0.1 sec</td><td>0.1 sec.</td><td>Planar Rollover</td></tr><tr><td>Complete file recorded</td><td>Mandatory</td><td>Following other data</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar VRU Rollover</td></tr><tr><td>Lateral acceleration (post-crash)</td><td>If Recorded</td><td>0-250 ms or O to End of Event Time plus 30 ms, whichever is</td><td>500</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Planar Rollover</td></tr><tr><td>Longitudinal acceleration (post-crash)</td><td> If Recorded</td><td>shorter.11 0-250 ms or O to End of Event Time plus 30 ms, whichever is</td><td>500</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Planar</td></tr><tr><td>Normal acceleration (post-crash)</td><td>If recorded</td><td>O to at least 250ms10</td><td>10</td><td>-5 g to +5g</td><td>±10%</td><td>0.5g</td><td>Rollover</td></tr><tr><td>Delta-V, lateral</td><td>Mandatory - lateral acceleration recorded at ≥500 Hz and with sufficient range and</td><td>0-250 ms or not required if O to End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>-100 km/h to+ 100 km/h.</td><td></td><td></td><td>Planar</td></tr><tr><td>Maximum delta-V,lateral</td><td>Mandatory - lateral acceleration recorded at</td><td>0-300 ms or not required if O to End of Event Time plus 30 ms, whichever is</td><td>N/A</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Time maximum delta-V,lateral lateral</td><td>Mandatory - not required if O to End of acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Time for maximum delta-V, resultant.</td><td>Mandatory - not required if O to End of relevant acceleration recorded at ≥500 Hz shorter.</td><td>0-300 ms or Event Time plus 30 ms, whichever is</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Engine rpm</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 to 10,000 rpm</td><td>±100 rpml1</td><td>100 rpm.</td><td>Planar Rollover</td></tr><tr><td>Vehicle roll angle</td><td>If recorded</td><td>O to at least 250 ms 11</td><td>10</td><td>-1080 deg to + 1080 deg.</td><td>±10%</td><td>10 deg.</td><td>Rollover</td></tr><tr><td>Vehicle roll ratel2</td><td>Mandatory if fitted and used for rollover protection system control</td><td>O to at least 250 ms 11</td><td>10</td><td>-240 to + 240 deg/sec</td><td>+/- 10%13</td><td>4 deg/sec</td><td>Rollover</td></tr><tr><td>Anti-lock braking system activity</td><td> Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, Non- Engaged, Engaged</td><td>N/A</td><td>Faulted, Non- Engaged, Engaged</td><td>Planar VRU</td></tr><tr><td>Stability control</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, On, Off, Engaged</td><td>N/A</td><td>Faulted, On, Off, Engaged</td><td>Planar VRU</td></tr><tr><td>Steering input</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>-250 deg CW to ±5% + 250 deg ccw.</td><td></td><td>±1%.</td><td>Planar VRU</td></tr><tr><td>Safety belt status, front passenger 9</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Passenger air bag suppression status, front 9</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>Suppressed or not suppressed</td><td>N/A</td><td>Suppressed or Planar not suppressed</td><td>Rollover</td></tr><tr><td>Frontal air bag deployment, time to nth stage, driver15.</td><td>Mandatory if fitted with a driver's frontal air bag with a multi- stage inflator.</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Frontal air bag deployment, time to nth stage, front passenger14, 9.</td><td>Mandatory if fitted with a front passenger's frontal air bag with a multi- stage inflator.</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side air bag deployment, time to deploy, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side air bag deployment, time to deploy, front</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>passenger. Side curtain/tube air bag deployment, time to deploy,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>driver side. Side curtain/tube air bag deployment, time to deploy, passenger side.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Pretensioner deployment, time to fire, driver.</td><td> Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirementl</td><td>Recording interval/time² (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range3</td><td> Accuracy4</td><td>Resolution4</td><td>Event(s) recorded for5</td></tr><tr><td>Pretensioner deployment, time to fire, front passenger9.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Seat track position switch, foremost, status, driver.</td><td>Mandatory if fitted and used for deployment decision</td><td>-1.0 sec</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Seat track position switch, foremost,</td><td>Mandatory if fitted and used for deployment</td><td>-1.0 sec</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>status, front passenger 9. Occupant size classification,</td><td>decision If recorded</td><td>-1.0 sec</td><td>N/A</td><td>5th percentile female or larger.</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>driver Occupant size classification, front</td><td>If recorded</td><td>-1.0 sec</td><td>N/A</td><td>6yr old HIII USN/A ATD or Q6</td><td></td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>passenger9 Safety belt status, rear</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>ATD or smaller Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>passengers15 Tyre Pressure Monitoring System</td><td>Mandatory</td><td>-1.0 second relative to time zero</td><td>N/A</td><td>N/A</td><td>N/A</td><td>On, Off</td><td>Planar Rollover</td></tr><tr><td>Warning Lamp Status Longitudinal acceleration</td><td>Mandatory</td><td>-5.0 to 0 second</td><td>2</td><td>-1.5g to +1.5g</td><td>+/- 10%</td><td>0.1g</td><td>Planar</td></tr><tr><td>(pre -crash) Lateral acceleration</td><td>Mandatory</td><td>relative to time zero -5.0 to 0 second</td><td>2</td><td>-1.0g to +1.0g</td><td>+/- 10%</td><td>0.1g</td><td>VRU Planar</td></tr><tr><td>(pre -crash) Yaw Rate13</td><td>Mandatory</td><td>relative to time zero -5 to 0 seconds</td><td>2</td><td>-75 to +75 degrees / second the full</td><td>±10% of0.1</td><td></td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirementl</td><td>Recording interval/time² (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range3</td><td> Accuracy4</td><td>Resolution4</td><td>Event(s) recorded for</td></tr><tr><td>Traction Control Status</td><td>Mandatory if not fitted with second Stability control</td><td>-5.0 to 0 relative to time zero</td><td>2</td><td>Faulted, On, Off, Engaged</td><td>N/A</td><td>Faulted, On, Off, Engaged</td><td>Planar Rollover</td></tr><tr><td>Advanced emergency braking system status</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Deactivated, On but Non- engaged, Warning but Non-engaged,</td><td>Planar VRU Rollover</td></tr><tr><td>Cruise Control System Status</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Engaged Engaged, Faulted, Off, Non-engaged</td><td>Planar VRU</td></tr><tr><td>Adaptive Cruise Control Status (driving automation system level 1)</td><td>Mandatory</td><td>-5.0 to 0 second relative to time zero</td><td>2</td><td>N/A</td><td>N/A</td><td>Engaged, Faulted, Off, Non-engaged</td><td>Planar VRU Rollover</td></tr><tr><td>Vulnerable road user secondary safety system deployment,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms</td><td>VRU</td></tr><tr><td>time to deploy Vulnerable road Mandatory user secondary safety system warning</td><td></td><td>-1.1 to 0 relative to time zero</td><td>N/A</td><td>N/A</td><td>N/A</td><td>On or Off</td><td>VRU</td></tr><tr><td>indicator status16 Safety belt status mid- position front</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Planar Rollover</td></tr><tr><td>Far-side impact centre air bag deployment,</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>+/-2 ms</td><td>1ms</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirementl</td><td>Recording interval/time² (relative to time zero)</td><td>Data sample rate (samples per second)</td><td> Minimum range3</td><td> Accuracy4</td><td>Resolution4</td><td>Event(s) recorded for5</td></tr><tr><td>Lane departure Mandatory warning system status</td><td></td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, On but not warning, On - Warning</td><td>Planar Rollover</td></tr><tr><td>Corrective steering function status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>right Faulted, Off, On but not</td><td>Planar Rollover</td></tr><tr><td>Emergency steering function status</td><td>Mandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>engaged, Engaged Faulted, Off, On but not engaged,</td><td>Planar Rollover</td></tr><tr><td>Automatically commanded steering function category A</td><td>yMandatory</td><td> -5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Engaged Faulted, Off, Stand-By</td><td>Planar Rollover</td></tr><tr><td>status commanded steering function category B1</td><td>AutomaticallyMandatory</td><td>-5.0 to 0 sec</td><td></td><td>N/A</td><td>N/A</td><td>Active17 Faulted, Off, Stand-By</td><td>Planar Rollover</td></tr><tr><td>status Automatically commanded steering function category B2</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Active17 Faulted, Off, Stand-By</td><td>Planar Rollover</td></tr><tr><td>status Automatically commanded steering function category C</td><td>Mandatory</td><td>-5.0 to 0sec 2</td><td></td><td>N/A</td><td>N/A</td><td>Active17 Faulted, Off, Stand-By</td><td>Planar Rollover</td></tr><tr><td>Automatically commanded steering function category D status</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, Stand-By</td><td>Planar Rollover</td></tr><tr><td colspan="2">Condition for</td><td>Recording interval/time² (relative to time</td><td>Data sample rate (samples Minimum range3</td><td></td><td>Accuracy4</td><td>Resolution4</td><td>Event(s) recorded for5</td></tr><tr><td>Data element Automatically commanded steering function</td><td>requirementl Mandatory</td><td>zero) -5.0 to 0 sec</td><td>per second) 2</td><td>N/A</td><td>N/A</td><td>Faulted, Off, Stand-By</td><td>Planar Rollover</td></tr><tr><td>category E status Accident emergency call system status</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Active17 Faulted, On but emergency call not</td><td>Planar VRU</td></tr></table>

#### 表 2 (page 4)
#### 表 3 (page 5)
#### 表 4 (page 6)
#### 表 5 (page 7)
#### 表 6 (page 8)
#### 表 7 (page 9)
#### 表 8 (page 10)
#### 表 9 (page 11)
