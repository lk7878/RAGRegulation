---
reg_id: ECE R160
region: ece
type: type/version
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Event Data Recorder
status: active
publication_date: 2021-10-21
implementation_date_new_vehicle: 2021-09-30
source_file: R160e.pdf
source_page_count: unknown
tags:
- type/version
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\160\R160e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: 结构化产出A中未提取此字段，原文B也未明确提及“standard_body”这一字段。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 结构化产出A中未提取此字段，原文B提供的片段中未提及此日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: 结构化产出A中未提取此字段，原文B提供的片段中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 结构化产出A中未提取此字段，原文B提供的片段中未提及替代法规。
- field: 技术要求限值
  status: unsure
  extracted: 见A中“核心要求”部分
  original: null
  note: 结构化产出A中总结了技术要求，但原文B提供的片段未包含附件4的具体限值表，无法核对。
_ocr_upgraded: mineru
_mineru_content_hash: d29bf1a337e42ce8
_mineru_outputs_dir: outputs/d29bf1a337e42ce8
_mineru_blocks:
  tables: 2
  formulas: 0
  images: 2
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 160 - Event Data Recorder (EDR)

## 法规概述
本法规旨在为M类和N1类机动车辆的事件数据记录器（EDR）制定统一的型式批准规定。其核心是规定车辆碰撞事件数据的最低收集、存储和碰撞幸存性要求，以支持有效的碰撞调查和安全设备性能分析。法规不涉及数据检索工具和方法的规范，这些由各国/地区层面的要求规定。

## 适用范围
*   **车辆类别**：适用于M类和N1类机动车辆的批准。
*   **数据排除**：明确排除车辆识别码（VIN）、相关车辆详细信息、位置/定位数据、驾驶员信息以及事件日期和时间等数据元素。
*   **系统前提**：如果车辆未设计安装能提供法规要求数据元素的系统或传感器，或该传感器/系统在记录时未运行，则无记录义务。但如果车辆安装了能提供规定格式数据的原厂传感器或系统，则当其运行时必须记录。

## 核心要求
### 1. 数据元素与格式
*   **数据元素**：配备EDR的车辆必须记录附件4表1中规定的强制性数据元素，以及在特定最低条件下要求的数据元素。
*   **数据格式**：每个记录的数据元素必须按照附件4表1规定的范围、精度和分辨率进行报告。
*   **加速度时程数据**：规定了纵向、横向和法向加速度时程数据的记录和过滤要求，包括时间步长（TS）、第一点编号（NFP）和最后一点编号（NLP）。

### 2. 数据捕获与存储
*   **触发记录的条件**：当满足或超过以下任一阈值时，EDR应记录事件：
    *   150毫秒或更短时间内纵向车速变化超过8 km/h。
    *   150毫秒或更短时间内横向车速变化超过8 km/h。
    *   不可逆乘员约束系统启动。
    *   弱势道路使用者二级安全系统启动。
*   **数据锁定条件**：在以下情况下，事件存储器应被锁定，防止被后续事件覆盖：
    *   任何不可逆乘员约束系统展开时。
    *   对于未配备用于正面碰撞的不可逆约束系统的车辆，当其在150毫秒或更短时间内X轴方向速度变化超过25 km/h时。
    *   弱势道路使用者二级安全系统启动时。
*   **时间零点确定**：规定了确定事件时间零点的具体条件。
*   **覆盖规则**：规定了非易失性存储器缓冲区已满时，当前事件数据对先前事件数据的覆盖策略，并明确了涉及约束系统展开的事件数据具有优先覆盖权。
*   **存储与检索**：EDR非易失性存储器缓冲区应至少能容纳两个不同事件的数据。存储在非易失性存储器中的数据在断电后应保留，并可根据国家或地区法规进行检索。

### 3. 碰撞测试性能与幸存性
*   车辆在完成符合UN法规No.94、95或137规定的严重程度级别的碰撞测试后，第5.1条要求的数据元素必须存在并可检索。
*   在碰撞测试中未正常运行的元件（如与发动机操作、制动等相关的元件）不需要满足精度或分辨率要求。

### 4. 其他要求
*   **不可停用**：事件数据记录器不得被停用。

## 批准与符合性
*   **申请与批准**：规定了车辆制造商或其授权代表向缔约方批准机构提交型式批准的申请流程、所需文件以及批准后的标记要求。
*   **生产一致性**：要求获得批准的车辆类型在生产中必须符合法规要求，批准机构应进行生产一致性核查。
*   **修改与扩展**：规定了车辆类型修改时的批准扩展程序。
*   **处罚**：如果不符合生产一致性要求，已授予的批准可被撤销。

## 附件
*   **附件1**：通信表格模板。
*   **附件2**：车辆类型关于其事件数据记录器（EDR）的型式批准信息文件模板。
*   **附件3**：批准标记的布置方式。
*   **附件4**：数据元素和格式（核心技术要求表）。详细列出了每个数据元素的记录条件、记录间隔/时间、数据采样率、最小范围、精度、分辨率以及所记录的事件类型（平面碰撞、弱势道路使用者事件、翻滚）。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 7 个
> - 公式 0 个
> - 图像 2 个
> - 全文 Markdown 41,362 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 7 个）

#### 表 1 (page 13)
<table><tr><td rowspan=1 colspan=1>Data element</td><td rowspan=1 colspan=1>Recordinginterval/time(relative to timezero)</td><td rowspan=1 colspan=1>Data sample rate(samples persecond)</td><td rowspan=1 colspan=1>Minimum range</td><td rowspan=1 colspan=1>Accuracy</td><td rowspan=1 colspan=1>Resolution</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 2 (page 15)
<table><tr><td colspan="7">Table 1</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Delta-V, longitudinal</td><td>Mandatory - not required if longitudinal acceleration recorded at ≥500 Hz with sufficient range and</td><td>0 to 250 ms or O to End of Event Time plus 30 ms, whichever is n shorter.</td><td>100</td><td>-100 km/h to+ 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Maximum delta-V, longitudinal</td><td>accuracy Mandatory - not required if O to End of longitudinal acceleration recorded at</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td>1 km/h.</td><td>Planar</td></tr><tr><td>Time, maximum delta-V, longitudinal</td><td>Mandatory - not required if O to End of longitudinal acceleration recorded at ≥500 Hz</td><td>0-300 ms or Event Time plus 30 ms, whichever is shorter.</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms,whichever is shorter.</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Speed, vehicle indicated</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 km/h to 250 km/h</td><td>±1 km/h</td><td>1 km/h.</td><td>Planar VRU</td></tr><tr><td>Engine throttle, % full (or accelerator pedal, % full)</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>0 to 100%</td><td>±5%</td><td>1%</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement2</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td> Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Service brake, on/off</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Planar VRU</td></tr><tr><td>crash</td><td>Ignition cycle， Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Rollover Planar VRU</td></tr><tr><td>Ignition cycle， Mandatory download</td><td></td><td>At time of download6</td><td>N/A</td><td>0 to 60,000</td><td>±1 cycle</td><td>1 cycle.</td><td>Rollover Planar VRU</td></tr><tr><td>Safety belt status, driver</td><td>Mandatory</td><td> -1.0 sec</td><td>N/A</td><td>Fastened, not fastened</td><td>N/A</td><td>Fastened, not fastened</td><td>Rollover Planar</td></tr><tr><td>Air bag warning lamp7</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td>On or Off</td><td>N/A</td><td>On or Off.</td><td>Rollover Planar Rollover</td></tr><tr><td>Frontal air bag deployment, time to deploy, in the case of a single stage air bag, or time to</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>multi-stage air bag, driver. deployment, time to deploy, in the case of a single stage air bag, or time to</td><td>Frontal air bag Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td></td><td></td><td>Recording interval/time</td><td>Data sample</td><td></td><td></td><td></td><td></td></tr><tr><td>Data element Multi-event crash, number of events</td><td>requirement² If Recorded8</td><td>zero) Event</td><td>per second) N/A</td><td>Minimum range 1 or more</td><td>Accuracy4 N/A</td><td>Resolution 1 or more.</td><td>recorded for5 Planar VRU</td></tr><tr><td>Time from event 1 to 2</td><td>Mandatory</td><td>As needed</td><td>N/A</td><td>0 to 5.0 sec</td><td>±0.1 sec</td><td>0.1 sec.</td><td>Rollover Planar Rollover</td></tr><tr><td>Complete file recorded (yes, no)</td><td>Mandatory</td><td>Following other data</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar VRU</td></tr><tr><td>Lateral acceleration (post-crash)</td><td>If Recorded</td><td>0-250 ms or O to End of Event Time plus 30 ms, whichever is</td><td>500</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Rollover Planar Rollover</td></tr><tr><td>Longitudinal acceleration (post-crash)</td><td> If Recorded</td><td>shorter. 0-250 ms or 0 to End of Event Time plus 30 ms,</td><td>500</td><td>-50 to +50g</td><td>+/- 10%</td><td>1g</td><td>Planar</td></tr><tr><td>Normal acceleration (post-crash)</td><td>If recorded</td><td>shorter. -1.0 to 5.0 sec9</td><td>10Hz</td><td>-5 gto +5g</td><td>±10%</td><td>0.5g</td><td>Rollover</td></tr><tr><td>Delta-V, lateral</td><td>Mandatory - not required if O to End of lateral acceleration recorded at ≥500 Hz and with sufficient range and</td><td>0-250 ms or Event Time plus 30 ms, whichever is shorter.</td><td></td><td>-100 km/h to + 100 km/h.</td><td>±10%</td><td></td><td>Planar</td></tr><tr><td></td><td>Condition for</td><td>Recording interval/time3 (relative to time</td><td>Data sample rate (samples</td><td></td><td></td><td></td><td>Event(s)</td></tr><tr><td>Data element Maximum delta-V, lateral</td><td>requirement² Mandatory - not required if O to End of lateral acceleration recorded at</td><td>zero) 0-300 ms or Event Time plus 30 ms,</td><td>per second) N/A</td><td>Minimum range -100 km/h to+ 100 km/h.</td><td>Accuracy4 ±10%</td><td>Resolution 1 km/h.</td><td>recorded for Planar</td></tr><tr><td>Time maximum</td><td>≥500 Hz Mandatory - not required if O to End of lateral acceleration</td><td>shorter. 0-300 ms or Event Time plus 30 ms,</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Time for maximum delta-V,</td><td>≥500 Hz Mandatory - not required if O to End of relevant acceleration</td><td>shorter. 0-300 ms or Event Time plus 30 ms,</td><td>N/A</td><td>0-300 ms,or 0- ±3 ms End of Event Time plus 30 ms, whichever</td><td></td><td>2.5 ms.</td><td>Planar</td></tr><tr><td>Engine rpm</td><td>≥500 Hz Mandatory</td><td>shorter. -5.0 to 0 sec</td><td></td><td>0 to 10,000 rpm ±100</td><td>rpm10</td><td>100 rpm.</td><td>Planar</td></tr><tr><td>Vehicle roll</td><td>If recorded</td><td>-1.0 up to 5.0</td><td>10</td><td>-1080 deg to +</td><td>±10%</td><td>10 deg.</td><td>Rollover Rollover</td></tr><tr><td>angle ABS activity</td><td>Mandatory</td><td>sec9 -5.0 to 0 sec</td><td>2</td><td>1080 deg. Faulted, Active, N/A Interveningl1</td><td></td><td>Faulted, Active, Intervening12</td><td>Planar</td></tr><tr><td>Stability</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Faulted, On, off,</td><td>N/A</td><td>Faulted, On, off,</td><td>Rollover Planar</td></tr><tr><td>Steering input</td><td>Mandatory</td><td>-5.0 to 0 sec</td><td>2</td><td>Intervening12 -250 deg CW to ±5% + 250 deg</td><td></td><td>Intervening12 ±1%.</td><td>Rollover Planar</td></tr><tr><td>Safety belt status, front</td><td>Mandatory</td><td> -1.0 sec</td><td></td><td>CCw. Fastened, not</td><td></td><td>Fastened,</td><td>Rollover VRU Planar</td></tr><tr><td>passenger Passenger air bag</td><td>Mandatory</td><td>-1.0 sec</td><td>N/A</td><td> suppressed or</td><td>N/A</td><td>suppressed</td><td>Planar</td></tr><tr><td colspan="8"></td></tr><tr><td>Data element Frontal air bag deployment,</td><td>Condition for requirement² Mandatory if fitted with a driver's</td><td>Recording interval/ime (relative to time zero) Event</td><td>Data sample rate (samples per second) N/A</td><td>Minimum range 0 to 250 ms</td><td>Accuracy4 ±2 ms</td><td>Resolution 1 ms.</td><td>Event(s) recorded for Planar</td></tr><tr><td>time to nth stage, driver4.</td><td>frontal air bag with a multi- stage inflator. Mandatory if Event</td><td></td><td></td><td></td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Frontal air bag deployment, time to nth stage, front passenger12.</td><td>fitted with a front passenger's frontal air bag with a multi- stage inflator.</td><td></td><td>N/A</td><td>0 to 250 ms</td><td></td><td></td><td></td></tr><tr><td>Side air bag deployment, time to deploy, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side air bag deployment, time to deploy, front passenger.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar</td></tr><tr><td>Side curtain/tube air bag deployment, time to deploy, driver side.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Side curtain/tube air bag deployment, time to deploy, passenger side.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Pretensioner deployment, time to fire, driver.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Pretensioner deployment, time to fire, front passenger.</td><td>Mandatory</td><td>Event</td><td>N/A</td><td>0 to 250 ms</td><td>±2 ms</td><td>1 ms.</td><td>Planar Rollover</td></tr><tr><td>Data element</td><td>Condition for requirement²</td><td>Recording interval/time3 (relative to time zero)</td><td>Data sample rate (samples per second)</td><td>Minimum range</td><td>Accuracy4</td><td>Resolution</td><td>Event(s) recorded for</td></tr><tr><td>Seat track position switch, foremost, status, driver.</td><td>Mandatory if fitted and used for deployment</td><td>-1.0 sec</td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Seat track position switch, foremost, status, front</td><td>Mandatory if -1.0 sec fitted and used for deployment decision</td><td></td><td>N/A</td><td>Yes or No</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Occupant size classification, driver</td><td>If recorded</td><td> -1.0 sec</td><td>N/A</td><td>5th percentile female or larger.</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr><tr><td>Occupant size classification, front passenger</td><td>If recorded</td><td> -1.0 sec</td><td>N/A</td><td>6yr old HII US ATD or Q6 ATD or smaller</td><td>N/A</td><td>Yes or No.</td><td>Planar Rollover</td></tr></table>

#### 表 3 (page 16)
#### 表 4 (page 17)
#### 表 5 (page 18)
#### 表 6 (page 19)
#### 表 7 (page 20)
### 图像（取前 2 张）

![图 page 12](../_mineru_assets/ECE R160/730801e2ec742a340c4c49847fc9a0c30c7b008413d30bc32533ade73e7aecee.jpg)  

![图 page 14](../_mineru_assets/ECE R160/2e2d084588df2eb0e296e08fa92e7eda330d2e7f5b76eb54779562d99758b95d.jpg)  

