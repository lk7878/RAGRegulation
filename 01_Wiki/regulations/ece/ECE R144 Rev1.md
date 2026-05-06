---
reg_id: ECE R144 Rev1
title: Uniform provisions concerning the Accident Emergency Call Systems (AECS)
region: ece
type: type/version
status: active
publication_date: 2023-02-07
implementation_date_new_vehicle: 2020-09-25
authority: UNECE
source_file: R144r1e.pdf
topics:
- Accident Emergency Call System
- AECS
- AECD
- AECC
- eCall
- Vehicle Safety
- GNSS
- PLMN
tags:
- type/version
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\144\R144r1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
reg_id_conf: low
cross_check_flags:
- field: reg_id
  status: normalized
  extracted: ECE R144 Rev1
  original: UN Regulation No. 144 (Revision 1)
  note: '[Auto-reclassified] Same reg_id after normalization (was: ''ECE R144 Rev1''
    vs ''UN Regulation No. 144 (Revision 1)'')'
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: 结构化产出 A 中未提取此字段，原文 B 中也未明确提及“standard_body”这一概念。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 结构化产出 A 中未提取此字段，原文 B 中也未提及针对在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: 结构化产出 A 中未提取此字段，原文 B 中也未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: 结构化产出 A 中未提取此字段，原文 B 中也未明确提及替代关系。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: 结构化产出 A 中未提取具体的技术要求限值，原文 B 提供的片段也未包含具体限值。
stage2_reclassified:
- reg_id
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: 0c9321a2e7f2e4f6
_mineru_outputs_dir: outputs/0c9321a2e7f2e4f6
_mineru_blocks:
  tables: 8
  formulas: 10
  images: 6
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 144 - Accident Emergency Call Systems (AECS)

## 法规概述
本法规规定了关于事故紧急呼叫系统（AECS）的统一技术规定。法规分为四个部分：
*   **第Ia部分**：旨在作为事故紧急呼叫设备（AECD）一部分安装的事故紧急呼叫组件（AECC）的型式批准。
*   **第Ib部分**：旨在安装在M1和N1类车辆上的事故紧急呼叫设备（AECD）的型式批准。
*   **第II部分**：当配备已根据第Ib部分批准的AECD时，车辆关于其事故紧急呼叫系统（AECS）的批准。
*   **第III部分**：当配备未根据第Ib部分单独批准的AECD时，车辆关于其事故紧急呼叫系统（AECS）的批准。

## 适用范围 (第1条)
### 1.1 本联合国法规适用于：
*   (a) 第Ia部分：旨在作为AECD一部分安装的AECC的批准。
*   (b) 第Ib部分：
    *   (i) 旨在安装在M1和N1类车辆上的AECD的批准。
    *   (ii) 应申请人的要求，旨在安装在其他类别车辆上的AECD的批准。
*   (c) 第II部分：当配备已根据本法规第Ib部分批准的AECD时，M1和N1类车辆关于其AECS的批准。
*   (d) 第III部分：当配备未根据本法规第Ib部分单独批准的AECD时，M1和N1类车辆关于其AECS的批准。

### 1.2 本法规不适用于：
*   (a) 通信模块功能和通信天线功能，除非本法规另有规定；
*   (b) 除最小数据集（MSD）外需传送至公共安全应答点（PSAP）的附加数据、数据格式、数据传输机制和逻辑、数据交换协议、操作模式及模式间转换条件、测试呼叫和测试数据传输的性能、对从基础设施接收到的协议命令的响应以及网络注册逻辑；
*   (c) 隐私、数据保护和个人数据处理；
*   (d) 定期技术检查（PTI）；
*   (e) 车辆侧翻情况下AECS的自动触发。

### 1.3 以下车辆应排除在本法规范围之外：
*   (a) 既不在联合国第94号法规也不在第95号法规范围内且未配备AECS自动触发装置的车辆；
*   (b) 总质量超过3.5吨的M1类车辆；以及
*   (c) 装甲车辆。

### 1.4 全球导航卫星系统（GNSS）定位可根据申请人的请求进行批准。
但是，如果申请人选择请求批准不带本法规所述GNSS定位功能的AECD/AECS或AECC，则适用缔约方的国家要求。

### 1.5 碰撞前免提音频性能可根据申请人的请求进行批准。
但是，如果申请人选择请求批准不带本法规所述免提音频性能评估的AECS，则适用缔约方的国家要求。

## 定义 (第2条)
*   **通信模块**：设计用于语音通信并使用公共陆地移动网络（PLMN）传输事故数据的组件。
*   **人机界面（HMI）**：设计用于允许用户与设备交互的AECD/AECC/AECS的组件或功能，包括接收视觉信息、获取视觉信息和输入控制命令。
*   **数据交换协议**：定义AECC/AECD/AECS与PSAP设备之间交换的消息内容、格式、时间参数、顺序和错误检查的一组规则和约定。
*   **公共/私人安全应答点（PSAP）**：在公共机构或国家政府或主管当局认可的私人组织负责下首次接收紧急呼叫的物理位置。
*   **安全气囊**：在车辆受到严重冲击时，自动展开柔性结构以限制乘员身体一个或多个部位与乘客舱内部接触严重程度的装置。
*   **电源**：为AECC、AECD或AECS供电的组件。
*   **备用电源**：当主电源故障时为AECC/AECD/AECS供电的组件。
*   **全球导航卫星系统（GNSS）**：用于精确定位地球表面任何点用户接收器位置、速度和时间的基于卫星的系统。
*   **GNSS接收器**：设计用于利用全球导航卫星系统信号确定车辆定位和时间信息的组件。
*   **星基增强系统（SBAS）**：通过地面站网络确保纠正GNSS系统由于干扰产生的局部误差的系统（例如，欧洲地球静止导航覆盖服务（EGNOS）、广域增强系统（WAAS）或准天顶卫星系统（QZSS））。
*   **GLONASS**：俄罗斯联邦拥有的GNSS。
*   **GALILEO**：欧盟拥有的GNSS。
*   **GPS**：美利坚合众国拥有的GNSS。
*   **NMEA-0183协议**：美国国家海洋电子协会（NMEA）开发的基于ASCII和串行通信协议的电气和数据规范组合，因其简单性已被许多行业（包括GNSS接收器）采纳为自愿标准。
*   **位置精度衰减因子（PDOP）**：卫星位置几何形状对GNSS接收器最终位置确定产生负面影响的连续测量；结合水平和垂直误差分量。
*   **WGS-84坐标系**：最流行和推荐的地球全球大地测量参考系统；最初由美国国家地理空间情报局为GPS开发，并在GNSS接收器行业广泛使用。
*   **开阔天空**：再现农村和郊区卫星可见度条件的场景；其中GNSS信号不受建筑物、树木等影响，易于到达GNSS接收器。
*   **城市峡谷**：再现城市地区卫星可见度条件的场景；其中GNSS信号受建筑物、树木等影响，难以到达GNSS接收器。
*   **灵敏度**：评估GNSS接收器在能够定位的情况下，天线输入端每颗卫星信号最小功率的GNSS性能指标。
*   **L1/E1频段**：国际电信联盟（ITU）定义的用于无线电导航卫星服务的无线电频谱部分，介于1,559至1,591 MHz之间；中心频率为1,575.42 MHz。
*   **首次定位时间**：GNSS接收器激活与开始输出有效导航信息之间的时间延迟。
*   **冷启动模式**：GNSS接收器的位置、速度、时间、历书和星历数据未存储在接收器中的状态，因此需要通过全天空搜索计算导航解。
*   **事故紧急呼叫设备（AECD）**：执行至少以下功能的单元或一组组件：
    *   (a) 接收和/或生成自动和手动触发信号；以及
    *   (b) 发送最小数据集（MSD）。
    此外，它还可以执行以下任何功能：
    *   (a) 接收或确定车辆位置；
    *   (b) 提供警告信号；以及
    *   (c) 允许用于语音通信的双向音频信号，除非本法规另有规定。
*   **事故紧急呼叫系统（AECS）**：安装在车辆中的AECD。
*   **触发信号**：请求紧急呼叫事务的逻辑信号。
*   **最小数据集（MSD）**：如附件12所定义的一组数据。
*   **控制模块**：设计用于确保AECC/AECD/AECS所有组件协同运行的组件。
*   **信息信号装置**：提供紧急呼叫事务状态信息的设备。
*   **警告信号装置**：提供AECC/AECD/AECS故障指示的指示灯。
*   **移动网络天线**：确保数据和用于语音通信的双向音频信号传输的组件。
*   **多任务显示器**：可以同时显示多条消息的显示器。
*   **总质量**：制造商规定的车辆技术上允许的最大质量。
*   **R点**：制造商为每个座椅定义的相对于车辆结构的参考点，如联合国第94号法规附件8所示。

## 法规结构
本法规包含以下部分及附件：

### 第Ia部分：旨在作为事故紧急呼叫设备（AECD）一部分安装的组件的批准
*   第3条：定义
*   第4条：AECC的批准申请
*   第5条：AECC的标记
*   第6条：批准
*   第7条：一般要求（包括数据发送/语音连接、电磁兼容性、位置确定、PLMN接入方式、AECC信息和警告信号、电源、抗冲击性）
*   第8条：AECC类型的修改和扩展批准
*   第9条：生产一致性
*   第10条：生产不一致的处罚
*   第11条：生产完全停止
*   第12条：负责进行批准测试的技术服务机构和型式批准机构的名称和地址

### 第Ib部分：旨在安装在M1和N1类车辆上的AECD的批准
*   第13条：定义
*   第14条：AECD的批准申请
*   第15条：标记
*   第16条：批准
*   第17条：要求（包括一般要求、电磁兼容性、位置确定、PLMN接入方式、AECD信息和警告信号、电源、抗冲击性）
*   第18条：AECD类型的修改和扩展批准
*   第19条：生产一致性
*   第20条：生产不一致的处罚
*   第21条：生产完全停止
*   第22条：负责进行批准测试的技术服务机构和型式批准机构的名称和地址

### 第II部分：当配备已批准的AECD时，车辆关于其AECS的批准
*   第23条：定义
*   第24条：批准申请
*   第25条：批准
*   第26条：要求（包括一般要求、触发信号验证、位置确定、AECS控制、AECS信息和警告信号、免提音频性能、AECS电源性能验证）
*   第27条：配备已根据第Ib部分批准的AECD的车辆类型的修改和扩展批准
*   第28条：生产一致性
*   第29条：生产不一致的处罚
*   第30条：生产完全停止
*   第31条：负责进行批准测试的技术服务机构和型式批准机构的名称和地址

### 第III部分：当配备未单独批准的AECD时，车辆关于其AECS的批准
*   第32条：定义
*   第33条：配备AECS的车辆类型的批准申请
*   第34条：批准
*   第35条：要求（包括一般要求、电磁兼容性、位置确定、PLMN接入方式、触发信号验证、AECS控制、AECS信息和警告信号、免提音频性能、AECS电源性能验证、抗冲击性）
*   第36条：配备AECS的车辆类型的修改和扩展批准
*   第37条：生产一致性
*   第38条：生产不一致的处罚
*   第39条：生产完全停止
*   第40条：负责进行批准测试的技术服务机构和型式批准机构的名称和地址
*   第41条：过渡性规定

### 附件列表
1.  关于根据联合国第144号法规第Ia部分批准的、旨在安装在M1和N1类车辆AECD中的AECC类型的批准或扩展或拒绝或撤销批准或生产完全停止的通报
2.  关于根据联合国第144号法规第Ib部分批准的、旨在安装在M1和N1类车辆上的AECD类型的批准或扩展或拒绝或撤销批准或生产完全停止的通报
3.  关于根据联合国第144号法规第II部分批准的M1和N1类车辆类型的批准或扩展或拒绝或撤销批准或生产完全停止的通报
4.  关于根据联合国第144号法规第III部分批准的M1或N1类车辆类型的批准或扩展或拒绝或撤销批准或生产完全停止的通报
5.  事故紧急呼叫组件（AECC）型式批准的信息文件
6.  事故紧急呼叫设备（AECD）型式批准的信息文件
7.  关于安装已批准类型AECD的车辆型式批准的信息文件
8.  关于配备未批准类型AECS的车辆型式批准的信息文件
9.  抗机械冲击的测试方法
10. 导航解决方案的测试方法
11. AECD/AECS碰撞后性能的测试方法
    *   附录：免提语音评估的语言和句子
12. 最小数据集（MSD）的定义

## 关键要求摘要
*   **功能要求**：AECC/AECD/AECS在收到触发信号后，应发送数据并与PSAP建立语音连接。如果失败，应重试。如果无法使用PLMN，应将数据存储在非易失性存储器中并尝试重新传输和建立语音连接。
*   **电磁兼容性**：AECC/AECD/AECS的有效性不得受到磁场或电场的不利影响，应符合UN R10（04系列或更高系列修正案）的要求。
*   **位置确定（可选）**：如果配备GNSS接收器（支持至少三个GNSS，包括GLONASS、Galileo和GPS，并能接收和处理SBAS信号），则需满足特定的精度、灵敏度、首次定位时间等要求。测试方法见附件10。
*   **PLMN接入**：AECD/AECS应配备允许在PLMN上注册/认证和访问的嵌入式硬件。
*   **信息和警告信号**：应提供紧急呼叫事务状态信息（例如，系统正在处理、传输失败）和内部故障警告信号。具体要求因批准部分（Ia, Ib, II, III）而异。
*   **电源**：如果配备备用电源，AECC/AECD/AECS应能在语音通信模式（不少于5分钟）、回叫模式（空闲模式，60分钟）和再次语音通信模式（不少于5分钟）下自主运行。
*   **抗冲击性**：AECC/AECD/AECS在冲击后应保持可操作。测试方法见附件9，MSD和HMI功能验证见附件11。
*   **触发信号验证（车辆部分）**：AECS的安装应能在严重车辆碰撞期间接收触发信号。验证需通过UN R94（正面碰撞）和/或UN R95（侧面碰撞）测试，或通过现有文件证明。
*   **AECS控制**：车辆应配备AECS控制装置，其安装应符合UN R121的要求，设计/放置应减少意外激活的风险，如果是多任务显示器，操作应在两次或更少的刻意动作内完成，且不能通过HMI停用AECS（维护和修理的临时停用功能允许）。
*   **免提音频性能（可选）**：AECS应为车辆驾驶员提供足够的语音清晰度。碰撞前清晰度通过符合ITU-T P.1140 06/15标准来证明，碰撞后清晰度通过主观测试证明。
*   **生产一致性**：应符合协定书附录1（E/ECE/TRANS/505/Rev.3）中规定的要求。

## 过渡性规定 (第41条)
*   自01系列修正案正式生效之日起，适用本法规的任何缔约方不得拒绝根据经01系列修正案修订的本法规授予或接受批准。
*   自2022年9月1日起，适用本法规的缔约方没有义务接受在2022年9月1日之后首次颁发的、符合本法规原始文本的批准。
*   适用本法规的缔约方应继续接受在2022年9月1日之前首次颁发的、符合本法规原始文本的批准。
*   适用本法规的缔约方不得拒绝根据本法规原始文本或其扩展授予批准。

---
**注**：本摘要基于提供的OCR文本，可能不完整。完整要求请参阅法规原文及附件。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 19 个
> - 公式 10 个
> - 图像 6 个
> - 全文 Markdown 164,841 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 13)
**Table 1 Template of information for self-test function **

<table><tr><td rowspan=1 colspan=2>Item</td><td rowspan=2 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>Component</td><td rowspan=1 colspan=1>Failure type</td></tr><tr><td rowspan=1 colspan=1>Control module</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>Internal failure = e.g. hardware failure,watch-dog, software checksum, softwareimage integrity,...</td></tr><tr><td rowspan=1 colspan=1>Communicationmodule</td><td rowspan=1 colspan=1>Electrical connection /module communicationfailure</td><td rowspan=1 colspan=1>A failure in the module can be detected bythe absence of digital communicationbetween the control moduleand the communication module.</td></tr><tr><td rowspan=1 colspan=1>Mobile networkcommunicationdevice</td><td rowspan=1 colspan=1>internal failure</td><td rowspan=1 colspan=1>Item necessary because it is a basic function:a failure implies that the AECS cannotperform its function.</td></tr><tr><td rowspan=1 colspan=1>GNSS receiver</td><td rowspan=1 colspan=1>Electrical connection /module communicationfailure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>GNSS receiver</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mobile networkantenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>GNSS antenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Crash ControlUnit (CCU)</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>e.g. crash detection sensor system, triggeringdevice,...</td></tr><tr><td rowspan=1 colspan=1>CCU</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>If not in good condition, then the automaticemergency call is not possible. If CCUinternal failure verification is not part ofAECC approval (Part Ia), then it shall besubject to AECD approval (Part Ib)</td></tr><tr><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>Dedicated battery is connected</td></tr><tr><td rowspan=1 colspan=1>SIM</td><td rowspan=1 colspan=1>not present</td><td rowspan=1 colspan=1>This item only applies if a removable SIMcard is used.</td></tr><tr><td rowspan=1 colspan=1>Back-up powersupply (if fitted)</td><td rowspan=1 colspan=1>The state of charge,threshold for warning atthe discretion of themanufacturer</td><td rowspan=1 colspan=1>Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 2 (page 21)
**Table 2 Template of information for self-test function **

<table><tr><td rowspan=1 colspan=2>Item</td><td rowspan=2 colspan=1>Note</td></tr><tr><td rowspan=1 colspan=1>Component</td><td rowspan=1 colspan=1>Failure type</td></tr><tr><td rowspan=1 colspan=1>Control module</td><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>Internal failure means e.g. hardwarefailure, watch-dog, software checksum, software image integrity,...</td></tr><tr><td rowspan=2 colspan=1>Communicationmodule</td><td rowspan=1 colspan=1>Electrical connection /modulecommunication failure</td><td rowspan=1 colspan=1>A failure in the module can be detected bythe absence of digital communicationbetween the control module and thecommunication module.</td></tr><tr><td rowspan=1 colspan=1>internal failure</td><td rowspan=1 colspan=1>Item necessary because it is a basicfunction: a failure implies that the AECScannot perform its function.</td></tr><tr><td rowspan=2 colspan=1>GNSS receiver</td><td rowspan=1 colspan=1>Electrical connection /modulecommunication failure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mobile networkantenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>GNSS antenna</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>CCU</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>e.g. crash detection sensor system, triggeringdevice,...</td></tr><tr><td rowspan=1 colspan=1>Internal failure</td><td rowspan=1 colspan=1>If not in good condition, then theautomatic emergency call is not possible.If CCU internal failure verification is not part of AECD approval (Part Ib), then it shall be subject to AECS approval(Part II).</td></tr><tr><td rowspan=1 colspan=1>Power supply</td><td rowspan=1 colspan=1>Electrical connection</td><td rowspan=1 colspan=1>Dedicated battery is connected.</td></tr><tr><td rowspan=1 colspan=1>SIM</td><td rowspan=1 colspan=1>not present</td><td rowspan=1 colspan=1>This item only applies if a removable SIMcard is used.</td></tr><tr><td rowspan=1 colspan=1>Back-up power supply(if fitted)</td><td rowspan=1 colspan=1>The state of charge,threshold for warningat the discretion of themanufacturer</td><td rowspan=1 colspan=1>Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 3 (page 30)
**Table 3 Template of information for self-test function **

<table><tr><td colspan="2" rowspan="1">Item</td><td colspan="1" rowspan="2">Notes</td></tr><tr><td colspan="1" rowspan="1">Component</td><td colspan="1" rowspan="1">Failure type</td></tr><tr><td colspan="1" rowspan="1">Control module</td><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">Internal failure means e.g. hardwarefailure, watch-dog, software checksum,software image integrity,.</td></tr><tr><td colspan="1" rowspan="2">Communicationmodule</td><td colspan="1" rowspan="1">Electrical connection /modulecommunication failure</td><td colspan="1" rowspan="1">A failure in the module can be detected bythe absence of digital communicationbetween the control moduleand the module.</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">Item necessary because it is a basicfunction:a failure implies that the AECScannot perform its function.</td></tr><tr><td colspan="1" rowspan="2">GNSS receiver</td><td colspan="1" rowspan="1">Electrical connection /modulecommunication failure</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Moble networkantenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">GNSS antenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">Crash Control Unit(CCU)</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">e.g. crash detection sensor system,triggering device,...</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">If not in good condition, then theautomatic emergency call is not possible.If CCU internal failure verification is notpart of AECS approval (Part II), then itshall be subject to AECD approval (PartIb).When CCU is not part of the AECD, thisrequirement is deemed to be fulfilled if:(a) the indication of a malfunction for aninternal CCU failure is provided bythe vehicle; and(b） the warning strategy on AECD isexplained to the driver.</td></tr><tr><td colspan="1" rowspan="1">Power supply</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">dedicated power supply is connected</td></tr><tr><td colspan="1" rowspan="1">SIM</td><td colspan="1" rowspan="1">not present</td><td colspan="1" rowspan="1">This item only applies if a removable SIMcard is used.</td></tr><tr><td colspan="1" rowspan="1">Back-up power supply(if fitted)</td><td colspan="1" rowspan="1">The state of charge,threshold for warningat the discretion of themanufacturer</td><td colspan="1" rowspan="1">Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 4 (page 31)
#### 表 5 (page 40)
**Table 4 Template of information for self-test function **

<table><tr><td colspan="2" rowspan="1">Item</td><td colspan="1" rowspan="2">Notes</td></tr><tr><td colspan="1" rowspan="1">Component</td><td colspan="1" rowspan="1">Failure type</td></tr><tr><td colspan="1" rowspan="1">Control module</td><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">Internal failure means e.g. hardware failure,watch-dog,software checksum, softwareimage integrity,...</td></tr><tr><td colspan="1" rowspan="2">Communicationmodule</td><td colspan="1" rowspan="1">Electrical connection /module communicationfailure</td><td colspan="1" rowspan="1">A failure in the module can be detected bythe absence of digital communicationbetween the control module and thecommunication module.</td></tr><tr><td colspan="1" rowspan="1">internal failure</td><td colspan="1" rowspan="1">Item necessary because it is a basicfunction: a failure implies that the AECScannot perform its function.</td></tr><tr><td colspan="1" rowspan="2">GNSS receiver</td><td colspan="1" rowspan="1">Electrical connection /module communicationfailure</td><td colspan="1" rowspan="1">GNSS approval optional in this Regulation.</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">GNSS approval optional in this Regulation.</td></tr><tr><td colspan="1" rowspan="1">Mobile networkantenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">GNSS antenna</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">GNSS approval optional in this Regulation</td></tr><tr><td colspan="1" rowspan="2">CCU</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">e.g. crash detection sensor system,triggering device,..</td></tr><tr><td colspan="1" rowspan="1">Internal failure</td><td colspan="1" rowspan="1">If not in good condition, then the automaticemergency call is not possible.</td></tr><tr><td colspan="1" rowspan="1">Power supply</td><td colspan="1" rowspan="1">Electrical connection</td><td colspan="1" rowspan="1">Dedicated power supply is connected.</td></tr><tr><td colspan="1" rowspan="1">SIM</td><td colspan="1" rowspan="1">Not present</td><td colspan="1" rowspan="1">This item only applies if a removable SIMcard is used.</td></tr><tr><td colspan="1" rowspan="1">Back-up powersupply(if fitted)</td><td colspan="1" rowspan="1">The state of charge,threshold for warning atthe discretion of themanufacturer</td><td colspan="1" rowspan="1">Failure if the state of charge is at a criticallevel according to the manufacturer.</td></tr></table>

#### 表 6 (page 41)
#### 表 7 (page 49)
<table><tr><td>GNSS receiver: yes/no²</td><td>GNSS antenna: yes/no²</td></tr><tr><td></td><td>Warning signal device: yes/no²</td></tr><tr><td></td><td>Control module: yes/no²</td></tr><tr><td>10.</td><td>Components of AECD were tested according to paragraph 17.7 :</td></tr><tr><td></td><td>Warning signal device: yes/no²</td></tr><tr><td></td><td>Hands-free audio equipment (micros and speakers): yes/no²</td></tr><tr><td></td><td>Power supply other than back-up battery: yes/no²</td></tr><tr><td></td><td>Information signal device: yes/no²</td></tr><tr><td></td><td>GNSS antenna:yes/no²</td></tr><tr><td></td><td>GNSS receiver: yes/no²</td></tr><tr><td></td><td>Orientation of the AECD ：</td></tr><tr><td>11.</td><td>Back-up power supply performance was checked in accordance with paragraph 17.6.:</td></tr><tr><td>12.</td><td>yes/no² AECD was tested in accordance with paragraph 17.3. (Position determination):</td></tr><tr><td></td><td>yes/no²</td></tr><tr><td>13.</td><td>AECD was tested in accordance with paragraph 17.5.(information and warning signal): yes/no²</td></tr><tr><td>13.1.</td><td> Crash control unit is a part of the AECD: yes/no²</td></tr><tr><td>14.</td><td>Position of the approval mark:.</td></tr><tr><td>15.</td><td>Reason(s) for extension (if applicable): .</td></tr><tr><td>16.</td><td>Approval granted/refused/extended/withdrawn²</td></tr><tr><td>17.</td><td>Place:..</td></tr><tr><td>18.</td><td>Date:..</td></tr><tr><td>19.</td><td>Signature: .</td></tr><tr><td></td><td></td></tr><tr><td>20.</td><td>The list of documents deposited with the Type Approval Authority which has granted approval is annexed to this communication and may be obtained on request.</td></tr></table>

#### 表 8 (page 59)
**Table 5 for $\mathbf { M _ { 1 } }$ and $\mathbf { N _ { 1 } }$ vehicles: **

<table><tr><td rowspan=1 colspan=1>Point</td><td rowspan=1 colspan=1>Time (ms)</td><td rowspan=1 colspan=1>Acceleration (g)</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>65</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>65</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>46</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>77</td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>47</td><td rowspan=1 colspan=1>77</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>0</td></tr></table>

#### 表 9 (page 61)
**Table 6 Recommended list of measurement instruments, test and auxiliary equipment **

<table><tr><td rowspan=2 colspan=1>Equipment name</td><td rowspan=1 colspan=2>Required technical characteristics of test equipment</td></tr><tr><td rowspan=1 colspan=1>Scale range</td><td rowspan=1 colspan=1>Scale accuracy</td></tr><tr><td rowspan=1 colspan=1>Globalnavigationsatellite systemsimulator ofGLONASS,Galileo and GPS signals</td><td rowspan=1 colspan=1>Number of simulated signals: at least 18</td><td rowspan=1 colspan=1>Mean square deviation of randomaccuracy component of pseudo-range to GLONASS / Galileo /GPS satellites not more: stadiometric code phase: 0.1 m;communication carrier phase:0.001 m;pseudovelocity: 0.005 m/s.</td></tr><tr><td rowspan=1 colspan=1>Digital stopwatch</td><td rowspan=1 colspan=1>Maximum count volume:9h 59 min. 59.99 s</td><td rowspan=1 colspan=1>Daily variation (at 25 ±5 C): notmore + 1.0 s;Time discreteness: 0.01 s</td></tr><tr><td rowspan=1 colspan=1>Vector networkanalyzer</td><td rowspan=1 colspan=1>Frequency range:300 kHz ...4,000 kHzDynamic range:(minus 85 ... 40) dB</td><td rowspan=1 colspan=1>Accuracy F 1:10-6Accuracy D (0.1... 0.5) dB</td></tr><tr><td rowspan=1 colspan=1>Low-noiseamplifier</td><td rowspan=1 colspan=1>Frequency range:1200 ...1,700 MHzNoise coefficient: notmore 2.0 dBAmplifier gaincoefficient: 24 dB</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Attenuator 1</td><td rowspan=1 colspan=1>Dynamic range:(0... 11) dB</td><td rowspan=1 colspan=1>Accuracy ± 0.5 dB</td></tr><tr><td rowspan=1 colspan=1>Attenuator 2</td><td rowspan=1 colspan=1>Dynamic range:(0 ... 110) dB</td><td rowspan=1 colspan=1>Accuracy ± 0.5 dB</td></tr><tr><td rowspan=1 colspan=1>Power source</td><td rowspan=1 colspan=1>Range of direct currentvoltage setting from 0.1to 30VCurrent intensity of outputvoltage at least 3 A</td><td rowspan=1 colspan=1>Accuracy V ± 3 per centAccuracy A ± 1 per cent</td></tr></table>

#### 表 10 (page 62)
**Figure 1 Open sky definition **

<table><tr><td rowspan=1 colspan=1>Zone</td><td rowspan=1 colspan=1>Elevation range (deg)</td><td rowspan=1 colspan=1>Azimuth range (deg)</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>0-5</td><td rowspan=1 colspan=1>0 - 360</td></tr><tr><td rowspan=1 colspan=1>Background</td><td rowspan=1 colspan=2>Area out of Zone A</td></tr></table>

### 公式（取前 10 个）

**公式 1** (page 64):

$$
\Delta B ( j ) = B ( j ) - B _ { t r u e j } ,
$$

**公式 2** (page 64):

$$
d B = \frac { 1 } { N } \cdot \sum _ { j = 1 } ^ { N } \Delta B ( j )
$$

**公式 3** (page 65):

$$
\sigma _ { \mathrm { B } } = \sqrt { \frac { \displaystyle \sum _ { \mathrm { j = 1 } } ^ { \mathrm { N } } \left( \Delta \mathbf { B } ( \mathrm { j } ) - \mathbf { d } \mathbf { B } \right) ^ { 2 } } { \mathbf { N } - 1 } } ,
$$

**公式 4** (page 65):

$$
d B ( \boldsymbol { \mathscr { n } } ) = 2 \cdot \frac { a ( I - e ^ { 2 } ) } { ( I - e ^ { 2 } s i n ^ { 2 } \varphi ) ^ { 3 / 2 } } \cdot \frac { 0 , 5 ^ { \prime \prime } \cdot \pi } { I 8 0 \cdot 3 6 0 O ^ { \prime \prime } } \cdot d B ,
$$

**公式 5** (page 65):

$$
\sigma _ { _ B } ( \mathcal { M } ) = 2 \cdot \frac { a ( I - e ^ { 2 } ) } { ( I - e ^ { 2 } s i n ^ { 2 } \varphi ) ^ { 3 / 2 } } \cdot \frac { 0 , 5 ^ { \prime \prime } \cdot \pi } { I 8 0 \cdot 3 6 0 O ^ { \prime \prime } } \cdot \sigma _ { _ B } ,
$$

**公式 6** (page 65):

$$
\Delta \mathrm { B } ( j , { \cal M } ) = 2 \cdot \frac { a ( I - e ^ { 2 } ) } { ( I - e ^ { 2 } s i n ^ { 2 } \varphi ) ^ { 3 / 2 } } \cdot \frac { { \cal O } , 5 ^ { \prime \prime } \cdot \pi } { I 8 { \cal O } \cdot 3 6 { \cal O } { \cal O } ^ { \prime \prime } } \cdot \Delta \mathrm { B } ( j ) ,
$$

**公式 7** (page 65):

$$
d L ( w ) = 2 \cdot \frac { a \cdot c o s \varphi } { \sqrt { I - e ^ { 2 } s i n ^ { 2 } \varphi } } \cdot \frac { { \cal O } , 5 ^ { \prime \prime } \cdot \pi } { { \cal I } 8 0 \cdot 3 6 { \cal O } { \cal O } ^ { \prime \prime } } \cdot d { \cal L } ,
$$

**公式 8** (page 65):

$$
\sigma _ { L } ( \boldsymbol { m } ) = 2 \cdot \frac { a \cdot c o s \varphi } { \sqrt { I - e ^ { 2 } s i n ^ { 2 } \varphi } } \cdot \frac { O , 5 ^ { \prime \prime } \cdot \pi } { I 8 0 \cdot 3 6 O O ^ { \prime \prime } } \cdot \sigma _ { L } ,
$$

**公式 9** (page 65):

$$
\Delta L ( j , \mathcal { M } ) = 2 \cdot \frac { a \cdot c o s \varphi } { \sqrt { I - e ^ { 2 } s i n ^ { 2 } \varphi } } \cdot \frac { O , 5 ^ { \prime \prime } \cdot \pi } { I 8 O \cdot 3 6 O O ^ { \prime \prime } } \cdot \Delta L ( j ) ,
$$

**公式 10** (page 66):

$$
\begin{array} { r l } & { \Pi = \sqrt { \mathrm { d } \mathrm { B } ^ { 2 } ( \mathrm { m } ) + \mathrm { d } \mathrm { L } ^ { 2 } ( \mathrm { m } ) } + 2 \cdot \sqrt { \sigma _ { \mathrm { B } } ^ { 2 } ( \mathrm { m } ) + \sigma _ { \mathrm { L } } ^ { 2 } ( \mathrm { m } ) } , } \\ & { \Delta X ( j , \boldsymbol { \mathscr { M } } ) = \sqrt { \Delta \mathrm { B } ^ { 2 } ( j , \boldsymbol { \mathscr { M } } ) + \Delta \mathrm { L } ^ { 2 } ( j , \boldsymbol { \mathscr { M } } ) } } \end{array}
$$

### 图像（取前 6 张）

![Figure 1 Generic description of test pulses ](../_mineru_assets/ECE R144 Rev1/f4864e2635acd8ef6cceb035782372359daa168fb900420c1561de7a685ca724.jpg)  
*Figure 1 Generic description of test pulses * (page 59)

![图 page 62](../_mineru_assets/ECE R144 Rev1/cdf34afd37a71c7e2ecaa285e8066139b54f4ec93a3e571fa37a14d2f0a4cb2f.jpg)  

![图 page 62](../_mineru_assets/ECE R144 Rev1/3f77091557b201d615c7a3191ab66974e453ad04c58ede40fb98d26c22b8f5bf.jpg)  

![图 page 69](../_mineru_assets/ECE R144 Rev1/e83d8e2c0913997e27bed894a5da15df47fe34fbf5c0df52af776c28c685cef3.jpg)  

![Figure 4 Diagram of path calibration ](../_mineru_assets/ECE R144 Rev1/1586d4541cbe7a13f0d3f0ea8098b297e1c3220c8645f24cbe455df471bb572b.jpg)  
*Figure 4 Diagram of path calibration * (page 71)

![Figure 5 Arrangement for evaluation of GNSS module sensitivity ](../_mineru_assets/ECE R144 Rev1/23f8c0d1179a944c9641969796b7f595b67bad9af1cae3bdd8d1635a3f617031.jpg)  
*Figure 5 Arrangement for evaluation of GNSS module sensitivity * (page 71)

