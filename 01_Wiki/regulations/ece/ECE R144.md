---
reg_id: ECE R144
region: ece
type: type/version
title: Uniform provisions concerning the Accident Emergency Call Systems (AECS)
status: active
publication_date: 2018-09-04
date_implemented: 2018-07-19
source: ECE/TRANS/505/Rev.3/Add.143
authentic_source: ECE/TRANS/WP.29/2017/132
scope: 'This Regulation applies to:

  (a) Part Ia: the approval of Accident Emergency Call Components (AECC) which are
  intended to be fitted as part of an Accident Emergency Call Device (AECD).

  (b) Part Ib: the approval of AECDs which are intended to be fitted to vehicles of
  categories M and N.

  (c) Part II: the approval of vehicles of categories M and N with regard to their
  Accident Emergency Call System (AECS) when equipped with an AECD which has been
  approved to Part Ib of this Regulation.

  (d) Part III: the approval of vehicles of categories M and N with regard to their
  AECS when equipped with an AECD which has not been separately approved according
  to Part Ib of this Regulation.

  It does not apply to communication module/antenna functionality (unless otherwise
  prescribed), additional data beyond the Minimum Set of Data (MSD), privacy/data
  protection, Periodical Technical Inspection (PTI), and automatic triggering in case
  of rollover. Certain vehicles (e.g., not in scope of UN R94/R95, M>3.5t, armoured
  vehicles) are excluded.

  '
keywords:
- AECS
- AECD
- AECC
- emergency call
- eCall
- GNSS
- PLMN
- PSAP
- MSD
- UN R94
- UN R95
- UN R10
- UN R121
- vehicle safety
- type approval
related_regulations:
- UN R10 (EMC)
- UN R94 (Frontal collision protection)
- UN R95 (Lateral collision protection)
- UN R121 (Location and identification of controls)
tags:
- type/version
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\144\R144e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: ece
  original: null
  note: B 未明确提及标准机构缩写，但文档来自 ECE。
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
  note: B 中未提及替代法规。
- field: 技术要求限值
  status: unsure
  extracted: 见A中“核心要求摘要”
  original: null
  note: B 提供的文本为法规目录和范围，未包含具体技术限值，无法核对。
_ocr_upgraded: mineru
_mineru_content_hash: d4735e78a9b7da3f
_mineru_outputs_dir: outputs/d4735e78a9b7da3f
_mineru_blocks:
  tables: 8
  formulas: 10
  images: 7
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 144 - Accident Emergency Call Systems (AECS)

## 概览
本法规规定了事故紧急呼叫系统（AECS）及其组件（AECC、AECD）的统一技术规定和型式批准要求。法规分为四个部分，分别针对组件、独立设备、以及安装在车辆上的系统（使用已批准或未批准的设备）。

## 法规结构
1.  **范围** (第1条)
2.  **定义 - 通用** (第2条)
3.  **第Ia部分：拟作为事故紧急呼叫设备（AECD）一部分安装的组件的批准**
    *   定义、申请、标记、批准、一般要求（数据/语音连接、EMC、定位、PLMN接入、信息/警告信号、电源、抗冲击）、修改与扩展、生产一致性等。
4.  **第Ib部分：拟安装在M类和N类车辆上的AECD的批准**
    *   定义、申请、标记、批准、要求（通用、EMC、定位、PLMN接入、信息/警告信号、电源、抗冲击）、修改与扩展、生产一致性等。
5.  **第II部分：配备已根据本法规第Ib部分批准的AECD的车辆关于其AECS的批准**
    *   定义、申请、批准、要求（通用、触发信号验证、定位、AECS控制、信息/警告信号、免提音频性能、电源性能验证）、修改与扩展、生产一致性等。
6.  **第III部分：配备未根据本法规第Ib部分单独批准的AECD的车辆关于其AECS的批准**
    *   定义、申请、批准、要求（通用、EMC、定位、PLMN接入、触发信号验证、AECS控制、信息/警告信号、免提音频性能、电源性能验证、抗冲击）、修改与扩展、生产一致性等。

## 核心要求摘要
*   **系统功能**：收到触发信号后，应能向公共安全应答点（PSAP）发送最小数据集（MSD）并建立语音连接。失败时应重试，并能在非易失性存储器中存储数据以备重传。
*   **电磁兼容性（EMC）**：需符合UN R10（04系列或更高）的要求。
*   **定位功能（可选）**：若配备GNSS接收机，应支持至少GLONASS、Galileo和GPS三个系统，并能处理SBAS信号。规定了在开阔天空和城市峡谷条件下的水平定位误差、灵敏度、首次定位时间、重捕获时间等性能指标。测试方法见附件10。
*   **PLMN接入**：必须配备允许在PLMN上注册/认证和接入的嵌入式硬件。
*   **信息与警告信号**：需提供紧急呼叫事务状态信息（处理中、传输失败）以及系统内部故障的警告信号。规定了自检功能需覆盖的组件和故障类型（见法规内表格）。
*   **电源**：若配备备用电源，需验证其在语音通信模式和回叫模式下的持续运行时间。抗冲击后电源应能继续为系统供电。
*   **抗冲击**：AECC/AECD/AECS的关键组件（控制模块、通信模块、备用电源、连接器、移动网络天线等）需通过附件9的测试（例如滑车测试），并在冲击后保持运行。需通过附件11的方法验证MSD发送和人机界面（HMI）功能。
*   **触发信号验证（车辆部分）**：对于M和N类车辆，根据车辆总质量、R点高度等参数，要求通过进行UN R94（正面碰撞）和/或UN R95（侧面碰撞）测试，或利用现有测试文档，来验证在严重碰撞中能产生触发信号且AECD/AECS安装不受影响。
*   **AECS控制**：控制装置的设计和安装需减少误触风险，符合UN R121的要求。如果嵌入多功能显示器，操作不应超过两个刻意动作。原则上不允许通过HMI停用AECS（维护和修理所需的临时停用除外）。
*   **免提音频性能（可选）**：可为驾驶员提供足够的语音清晰度。碰撞前性能可通过符合ITU-T P.1140标准来证明。碰撞后性能需通过主观测试验证，测试语言见附件11附录。
*   **批准与标记**：每个批准的型号都会被分配一个批准号，并需施加规定的国际批准标记（圆圈内带"E"和国家代码，后接法规号和批准号）。

## 附件列表
1.  关于根据UN R144第Ia部分批准的AECC的批准/扩展/拒绝/撤销或生产确定终止的通知书
2.  关于根据UN R144第Ib部分批准的AECD的批准/扩展/拒绝/撤销或生产确定终止的通知书
3.  关于根据UN R144第II部分批准的车辆的批准/扩展/拒绝/撤销或生产确定终止的通知书
4.  关于根据UN R144第III部分批准的车辆的批准/扩展/拒绝/撤销或生产确定终止的通知书
5.  事故紧急呼叫组件（AECC）型式批准信息文件
6.  事故紧急呼叫设备（AECD）型式批准信息文件
7.  关于安装已批准类型AECD的车辆型式批准信息文件
8.  关于配备非批准类型AECS的车辆型式批准信息文件
9.  抗机械冲击测试方法
10. 导航解决方案测试方法
11. AECD/AECS碰撞后性能测试方法
    *   附录：免提语音评估的语言和句子
12. 最小数据集（MSD）定义

## 备注
*   本法规基于《1958年协定》（修订版3）。
*   定位功能（第1.4条）和碰撞前免提音频性能（第1.5条）的批准是可选的。如果申请人不请求批准这些功能，则适用缔约方的国家要求。
*   法规中多次引用其他UN法规（如R10, R94, R95, R121），需结合理解。
*   文本中多处出现的上标"1"指向对M和N类车辆的定义（参考R.E.3）。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 17 个
> - 公式 10 个
> - 图像 7 个
> - 全文 Markdown 162,771 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 13)
**Table 1 Template of information for self-test function **

<table><tr><td rowspan=1 colspan=2>Item</td><td rowspan=2 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>Component</td><td rowspan=1 colspan=1>Failure type</td></tr><tr><td rowspan=1 colspan=1>Control module</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>Internal failure = e.g. hardware failure,watch-dog, software checksum, softwareimage integrity,...</td></tr><tr><td rowspan=1 colspan=1>Communicationmodule</td><td rowspan=1 colspan=1>Electrical connection /module communicationfailure</td><td rowspan=1 colspan=1>A failure in the module can be detected bythe absence of digital communicationbetween the control moduleand thecommunication module.</td></tr><tr><td rowspan=1 colspan=1>Mobile networkcommunicationdevice</td><td rowspan=1 colspan=1>internal failure</td><td rowspan=1 colspan=1>Item necessary because it is a basic function:a failure implies that the AECS cannotperform its function.</td></tr><tr><td rowspan=1 colspan=1>GNSS receiver</td><td rowspan=1 colspan=1>Electrical connection /module communicationfailure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>GNSS receiver</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mobile networkantenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>GNSS antenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Crash ControlUnit (CCU)</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>e.g. crash detection sensor system, triggeringdevice,...</td></tr><tr><td rowspan=1 colspan=1>CCU</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>If not in good condition, then the automaticemergency call is not possible. If CCUinternal failure verification is not part ofAECC approval (Part Ia), then it shall be subject to AECD approval (Part Ib)</td></tr><tr><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>Dedicated battery is connected</td></tr><tr><td rowspan=1 colspan=1>SIM</td><td rowspan=1 colspan=1>not present</td><td rowspan=1 colspan=1>This item only applies if a removable SIMcard is used.</td></tr><tr><td rowspan=1 colspan=1>Back-up powersupply (if fitted)</td><td rowspan=1 colspan=1>The state of charge,threshold for warning atthe discretion of themanufacturer</td><td rowspan=1 colspan=1>Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 2 (page 21)
**Table 2 Template of information for self-test function **

<table><tr><td rowspan=1 colspan=2>Item</td><td rowspan=2 colspan=1>Note</td></tr><tr><td rowspan=1 colspan=1>Component</td><td rowspan=1 colspan=1>Failure type</td></tr><tr><td rowspan=1 colspan=1>Control module</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>Internal failure means e.g. hardwarefailure, watch-dog,software checksum,software image integrity,...</td></tr><tr><td rowspan=2 colspan=1>Communicationmodule</td><td rowspan=1 colspan=1>Electrical connection /modulecommunication failure</td><td rowspan=1 colspan=1>A failure in the module can be detected bythe absence of digital communicationbetween the control module and thecommunication module.</td></tr><tr><td rowspan=1 colspan=1>internal failure</td><td rowspan=1 colspan=1>Item necessary because it is a basicfunction: a failure implies that the AECScannot perform its function.</td></tr><tr><td rowspan=2 colspan=1>GNSS receiver</td><td rowspan=1 colspan=1>Electrical connection /modulecommunication failure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mobile networkantenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>GNSS antenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>CCU</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>e.g. crash detection sensor system, triggeringdevice,...</td></tr><tr><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>If not in good condition, then theautomatic emergency call is not possible.If CCU internal failure verification is notpart of AECD approval (Part Ib), then it shall be subject to AECS approval(Part II).</td></tr><tr><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>Dedicated battery is connected.</td></tr><tr><td rowspan=1 colspan=1>SIM</td><td rowspan=1 colspan=1>not present</td><td rowspan=1 colspan=1>This item only applies if a removable SIMcard is used.</td></tr><tr><td rowspan=1 colspan=1>Back-up power supply(if fitted)</td><td rowspan=1 colspan=1>The state of charge,threshold for warningat the discretion of themanufacturer</td><td rowspan=1 colspan=1>Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 3 (page 30)
**Table 3 Template of information for self-test function **

<table><tr><td colspan="2" rowspan="1">Item</td><td colspan="1" rowspan="2">Notes</td></tr><tr><td colspan="1" rowspan="1">Component</td><td colspan="1" rowspan="1">Failure type</td></tr><tr><td colspan="1" rowspan="1">Control module</td><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">Internal failure means e.g. hardwarefailure, watch-dog,software checksum,software image integrity,...</td></tr><tr><td colspan="1" rowspan="2">Communicationmodule</td><td colspan="1" rowspan="1">Electrical connection /modulecommunication failure</td><td colspan="1" rowspan="1">A failure in the module can be detected bythe absence of digital communicationbetween the control moduleand the module.</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">Item necessary because itis a basicfunction: a failure implies that the AECScannot perform its function.</td></tr><tr><td colspan="1" rowspan="2">GNSS receiver</td><td colspan="1" rowspan="1">Electrical connection /modulecommunication failure</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Moble networkantenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">GNSS antenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">Crash Control Unit(CCU)</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">e.g. crash detection sensor system,triggering device,...</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">If not in good condition, then theautomatic emergency call is not possible.If CCU internal failure verification is not part of AECS approval (Part II), then it shall be subject to AECD approval (PartIb).When CCU is not part of the AECD, thisrequirement is deemed to be fulfilled if:(a) the indication of a malfunction for aninternal CCU failure is provided bythe vehicle; and(b） the warning strategy on AECD isexplained to the driver.</td></tr><tr><td colspan="1" rowspan="1">Power supply</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">dedicated power supply is connected</td></tr><tr><td colspan="1" rowspan="1">SIM</td><td colspan="1" rowspan="1">not present</td><td colspan="1" rowspan="1">This item only applies if a removable SIMcard is used.</td></tr><tr><td colspan="1" rowspan="1">Back-up power supply(if fitted)</td><td colspan="1" rowspan="1">The state of charge,threshold for warningat the discretion of themanufacturer</td><td colspan="1" rowspan="1">Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 4 (page 31)
#### 表 5 (page 40)
**Table 4 Template of information for self-test function **

<table><tr><td colspan="2" rowspan="1">Item</td><td colspan="1" rowspan="2">Notes</td></tr><tr><td colspan="1" rowspan="1">Component</td><td colspan="1" rowspan="1">Failure type</td></tr><tr><td colspan="1" rowspan="1">Control module</td><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">Internal failure means e.g. hardware failure,watch-dog, software checksum, softwareimage integrity,...</td></tr><tr><td colspan="1" rowspan="2">Communicationmodule</td><td colspan="1" rowspan="1">Electrical connection /module communicationfailure</td><td colspan="1" rowspan="1">A failure in the module can be detected bythe absence of digital communicationbetween the control module and thecommunication module.</td></tr><tr><td colspan="1" rowspan="1">internal failure</td><td colspan="1" rowspan="1">Item necessary because it is a basicfunction: a failure implies that the AECScannot perform its function.</td></tr><tr><td colspan="1" rowspan="2">GNSS receiver</td><td colspan="1" rowspan="1">Electrical connection /module communicationfailure</td><td colspan="1" rowspan="1">GNSS approval optional in this Regulation.</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">GNSS approval optional in this Regulation.</td></tr><tr><td colspan="1" rowspan="1">Mobile networkantenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">GNSS antenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">GNSS approval optional in this Regulation</td></tr><tr><td colspan="1" rowspan="2">CCU</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">e.g. crash detection sensor system,triggering device,...</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">If not in good condition, then the automatic</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">emergency call is not possible.</td></tr><tr><td colspan="1" rowspan="1">Power supply</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">Dedicated power supply is connected.</td></tr><tr><td colspan="1" rowspan="1">SIM</td><td colspan="1" rowspan="1">Not present</td><td colspan="1" rowspan="1">This item only applies if a removable SIMcard is used.</td></tr><tr><td colspan="1" rowspan="1">Back-up powersupply(if fitted)</td><td colspan="1" rowspan="1">The state of charge,threshold for warning atthe discretion of themanufacturer</td><td colspan="1" rowspan="1">Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 6 (page 41)
#### 表 7 (page 58)
**Table 5 for $\mathbf { M _ { 1 } }$ and $\mathbf { N _ { 1 } }$ vehicles: **

<table><tr><td rowspan=1 colspan=1>Point</td><td rowspan=1 colspan=1>Time (ms)</td><td rowspan=1 colspan=1>Acceleration (g)</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>65</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>65</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>46</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>77</td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>77</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>0</td></tr></table>

#### 表 8 (page 60)
**Table 6 Recommended list of measurement instruments, test and auxiliary equipment **

<table><tr><td rowspan=2 colspan=1>Equipment name</td><td rowspan=1 colspan=2>Required technical characteristics of test equipment</td></tr><tr><td rowspan=1 colspan=1>Scale range</td><td rowspan=1 colspan=1> Scale accuracy</td></tr><tr><td rowspan=1 colspan=1>Globalnavigationsatellite systemsimulator ofGLONASS,Galileo andGPS signals</td><td rowspan=1 colspan=1>Number of simulatedsignals: at least 18</td><td rowspan=1 colspan=1>Mean square deviation of randomaccuracy component of pseudo-range to GLONASS /Galileo /GPS satellites not more:stadiometric code phase: 0.1 m;communication carrier phase:0.001 m;pseudovelocity: 0.005 m/s.</td></tr><tr><td rowspan=1 colspan=1>Digitalstopwatch</td><td rowspan=1 colspan=1>Maximum count volume:9h 59 min. 59.99 s</td><td rowspan=1 colspan=1>Daily variation (at 25 ±5 C): notmore + 1.0 s;Time discreteness: 0.01 s</td></tr><tr><td rowspan=1 colspan=1>Vector networkanalyzer</td><td rowspan=1 colspan=1>Frequency range:300 kHz ... 4,000 kHzDynamic range:(minus 85 .. 40) dB</td><td rowspan=1 colspan=1>Accuracy F 1:10-6Accuracy D (0.1 ... 0.5) dB</td></tr><tr><td rowspan=1 colspan=1>Low-noiseamplifier</td><td rowspan=1 colspan=1>Frequency range:1200 ...1,700 MHzNoise coefficient: notmore 2.0 dBAmplifier gaincoefficient: 24 dB</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Attenuator 1</td><td rowspan=1 colspan=1>Dynamic range:(0 ... 11) dB</td><td rowspan=1 colspan=1>Accuracy ± 0.5 dB</td></tr><tr><td rowspan=1 colspan=1>Attenuator 2</td><td rowspan=1 colspan=1>Dynamic range:(0. ... 110) dB</td><td rowspan=1 colspan=1>Accuracy ± 0.5 dB</td></tr><tr><td rowspan=1 colspan=1>Power source</td><td rowspan=1 colspan=1>Range of direct current voltage setting from 0.1to 30VCurrent intensity of outputvoltage at least 3 A</td><td rowspan=1 colspan=1>Accuracy V ± 3 per centAccuracy A ± 1 per cent</td></tr></table>

#### 表 9 (page 61)
**Figure 1 Open sky definition **

<table><tr><td rowspan=1 colspan=1>Zone</td><td rowspan=1 colspan=1>Elevation range (deg)</td><td rowspan=1 colspan=1>Azimuth range (deg)</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>0-5</td><td rowspan=1 colspan=1>0 - 360</td></tr><tr><td rowspan=1 colspan=1>Background</td><td rowspan=1 colspan=2>Area out of Zone A</td></tr></table>

#### 表 10 (page 61)
**Figure 2 Diagram of test stand **

<table><tr><td></td><td>0dB</td></tr><tr><td>Zone A</td><td>-100 dB or signal is switched off</td></tr></table>

### 公式（取前 10 个）

**公式 1** (page 63):

$$
\Delta B ( j ) = B ( j ) - B _ { t r u e j , }
$$

**公式 2** (page 63):

$$
d B = \frac { 1 } { N } \cdot \sum _ { j = 1 } ^ { N } \Delta B ( j )
$$

**公式 3** (page 64):

$$
\sigma _ { \mathrm { B } } = \sqrt { \frac { \displaystyle \sum _ { \mathrm { j = 1 } } ^ { \mathrm { N } } ( \Delta \mathbf { B } ( \mathrm { j } ) - \mathbf { d } \mathbf { B } ) ^ { 2 } } { \quad \mathbf { N } - 1 } } ,
$$

**公式 4** (page 64):

$$
d B ( \boldsymbol { \mathscr { n } } ) = 2 \cdot \frac { a ( I - e ^ { 2 } ) } { ( I - e ^ { 2 } s i n ^ { 2 } \varphi ) ^ { 3 / 2 } } \cdot \frac { 0 , 5 ^ { \prime \prime } \cdot \pi } { I 8 0 \cdot 3 6 0 O ^ { \prime \prime } } \cdot d B ,
$$

**公式 5** (page 64):

$$
\sigma _ { _ { B } } ( \mathcal { M } ) = 2 \cdot \frac { a ( I - e ^ { 2 } ) } { ( I - e ^ { 2 } s i n ^ { 2 } \varphi ) ^ { 3 / 2 } } \cdot \frac { 0 , 5 ^ { \prime \prime } \cdot \pi } { I 8 0 \cdot 3 6 0 O ^ { \prime \prime } } \cdot \sigma _ { _ { B } } ,
$$

**公式 6** (page 64):

$$
\Delta \mathrm { B } ( j , { \mathcal { M } } ) = 2 \cdot \frac { a ( I - e ^ { 2 } ) } { ( I - e ^ { 2 } s i n ^ { 2 } \varphi ) ^ { 3 / 2 } } \cdot \frac { O , 5 ^ { \prime \prime } \cdot \pi } { I 8 O \cdot 3 6 O O ^ { \prime \prime } } \cdot \Delta \mathrm { B } ( j ) ,
$$

**公式 7** (page 64):

$$
d L ( w ) = 2 \cdot \frac { a \cdot c o s \varphi } { \sqrt { I - e ^ { 2 } s i n ^ { 2 } \varphi } } \cdot \frac { { \cal O } , 5 ^ { \prime \prime } \cdot \pi } { { \cal I } 8 0 \cdot 3 6 { \cal O } { \cal O } ^ { \prime \prime } } \cdot d { \cal L } ,
$$

**公式 8** (page 64):

$$
\sigma _ { L } ( \boldsymbol { m } ) = 2 \cdot \frac { a \cdot c o s \varphi } { \sqrt { I - e ^ { 2 } s i n ^ { 2 } \varphi } } \cdot \frac { O , 5 ^ { \prime \prime } \cdot \pi } { I 8 O \cdot 3 6 O O ^ { \prime \prime } } \cdot \sigma _ { L } ,
$$

**公式 9** (page 64):

$$
\Delta L ( j , \mathcal { M } ) = 2 \cdot \frac { a \cdot c o s \varphi } { \sqrt { I - e ^ { 2 } s i n ^ { 2 } \varphi } } \cdot \frac { O , 5 ^ { \prime \prime } \cdot \pi } { I 8 O \cdot 3 6 O O ^ { \prime \prime } } \cdot \Delta L ( j ) ,
$$

**公式 10** (page 65):

$$
\begin{array} { r l } & { \Pi = \sqrt { \mathrm { d } \mathrm { B } ^ { 2 } ( \mathrm { m } ) + \mathrm { d } \mathrm { L } ^ { 2 } ( \mathrm { m } ) } + 2 \cdot \sqrt { \sigma _ { \mathrm { B } } ^ { 2 } ( \mathrm { m } ) + \sigma _ { \mathrm { L } } ^ { 2 } ( \mathrm { m } ) } , } \\ & { \Delta X ( j , \boldsymbol { \mathscr { M } } ) = \sqrt { \Delta \mathrm { B } ^ { 2 } ( j , \boldsymbol { \mathscr { M } } ) + \Delta \mathrm { L } ^ { 2 } ( j , \boldsymbol { \mathscr { M } } ) } } \end{array}
$$

### 图像（取前 7 张）

![图 page 45](../_mineru_assets/ECE R144/31b111db799129b50541136405c6560e8edd91b7cd973937c9b94019e5366edc.jpg)  

![Figure 1 Generic description of test pulses ](../_mineru_assets/ECE R144/a90e7a8a982b7049a47b67e44e5e36d1d28185f2ccd1937305ea05fc0544a414.jpg)  
*Figure 1 Generic description of test pulses * (page 58)

![图 page 61](../_mineru_assets/ECE R144/0157daddfcef2d9368c2a1e5b70b634fddf3afb9efa6dc678b518ae4f4aeee0f.jpg)  

![图 page 61](../_mineru_assets/ECE R144/df7b9a5f3f6e248a52ba5ceb81482ebef1efb9dad35ab5de6abcec3dba0304be.jpg)  

![图 page 68](../_mineru_assets/ECE R144/c724ebb6fdc61e89848ec476c52c0e075ee468319451ada581a3b6d76e3f4cfe.jpg)  

![Figure 4 Diagram of path calibration ](../_mineru_assets/ECE R144/752331d9e79666f94c70911308d09a98ce86a9663a423cb5a871579d19a0d37c.jpg)  
*Figure 4 Diagram of path calibration * (page 70)

![Figure 5 Arrangement for evaluation of GNSS module sensitivity ](../_mineru_assets/ECE R144/cae3beb6e568d9ca4c99b27fe9c57066a1e96d030cb18391c7d0f74107b37cbb.jpg)  
*Figure 5 Arrangement for evaluation of GNSS module sensitivity * (page 70)

