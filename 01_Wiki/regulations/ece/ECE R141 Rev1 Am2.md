---
reg_id: ECE R141 Rev1 Am2
region: ece
type: type/amendment
title: Addendum 140 – UN Regulation No. 141 Revision 1 – Amendment 2
entry_into_force_date: 2023-01-04
promulgation_date: 2023-02-24
source_file: 国外法规\ECE标准\标准法规-UNECE\121~160\141\R141r1am2e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\141\R141r1am2e.pdf
publication_date: 2023-02-24
status: active
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及 standard_body 字段。
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
  note: B 中未提及 equivalent_to 关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及本文件替代了哪个文件。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A 中未提取具体的技术要求限值，B 中虽有技术修订但未提供可核对的限值列表。
_ocr_upgraded: mineru
_mineru_content_hash: 5e4a3a73a76de4b6
_mineru_outputs_dir: outputs/5e4a3a73a76de4b6
_mineru_blocks:
  tables: 10
  formulas: 0
  images: 3
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 141 Revision 1 – Amendment 2

## 概述
本文件是《关于采用轮式车辆、可安装和/或用于轮式车辆的设备及部件的统一技术法规以及基于这些联合国法规批准相互认可条件的协定》的增补文件。具体为联合国法规第141号（UN Regulation No. 141）关于车辆轮胎压力监测系统（TPMS）批准的统一规定的第1修订版第2修正案。本修正案自2023年1月4日起生效。

## 主要修订内容
本修正案对UN R141进行了多处修订，主要涉及技术要求的更新、测试程序的细化以及通信接口规范的完善。

### 1. 法规文本修订
*   **第3.1条（批准申请）**：明确了车辆类型关于其TPMS的批准申请应由车辆制造商或其正式授权的代表提交。
*   **第5.1.1.1条（TPRS/CTIS等效性）**：规定当轮胎压力补充系统（TPRS）或中央轮胎充气系统（CTIS）满足特定条款和附件4的测试标准时，可被视为与TPMS等效用于型式批准，此时无需安装TPMS。
*   **第5.1.1.2条**：删除。
*   **第5.1.1.3条（重编号为5.1.1.2）**：修订为规定如果安装了多个系统（如TPMS、TPRS、CTIS），向驾驶员传递警告信息的系统应根据本法规要求获得批准。如果车辆安装了多个系统，必须确保不会向驾驶员显示矛盾信息（例如通过优先级设置）。
*   **第5.1.2条（电磁兼容性）**：修订了TPMS/TPRS/CTIS有效性的电磁兼容性要求，明确应通过满足UN法规第10号的技术要求和过渡条款来证明，并根据车辆是否配备牵引电池充电耦合系统，分别应用其第03或第06系列修正案。
*   **第5.1.6条（复位功能）**：针对特定车辆类别，详细规定了TPMS复位功能的设计要求，以减少误操作风险，并要求制造商在车辆手册或通过其他车内通信方式提供必要信息。
*   **第5.4.1至5.4.3条（故障指示）**：修订了TPMS/TPRS/CTIS故障指示信号的触发条件和时间要求。
*   **第5.5.6条（故障指示信号）**：修订了故障指示信号与低胎压警告信号共用时的闪烁和点亮逻辑。
*   **第5.6.1、5.6.1.1、5.6.1.2条（通信接口）**：修订了牵引车与挂车之间TPMS/TPRS/CTIS数据信息交换的通信接口要求，包括有线（基于ISO 11992和ISO 7638标准）和无线接口的兼容性要求，并引入了点对点链路中网关ECU的标准化接口规范。
*   **新增第5.7和5.7.1条（挂车替代程序）**：为O3和O4类车辆（挂车）的TPMS/TPRS/CTIS型式批准引入了基于附件8的替代程序。

### 2. 附件修订
*   **附件2（批准标记）**：更新了批准标记的示例说明文本。
*   **附件3（TPMS测试要求）**：
    *   修订了第1.5.1条（测试质量），明确了车辆负载条件、空载测试情形以及测试过程中允许的乘员。
    *   修订了第2.2条，规定了点火开关处于“运行”位置时，ECU应执行低胎压指示灯的功能检查。
*   **附件4（TPRS和CTIS测试要求）**：
    *   修订了标题、第1.2条（路面）、第1.3.1条（测试质量）。
    *   新增第1.3.3条（轮辋位置）和第1.3.4条（静止位置，由原1.3.3条重编号并修订）。
    *   修订了第1.5条（压力测量设备精度）。
    *   新增第2.1条（双轮胎变体测试）、第2.2条（轮胎充气前准备）、第2.3条（系统自检）。
    *   将原第2.1条和第2.2条重编号并修订为第2.4条（车辆调节）和第2.5条（检查系统补充功能）。
    *   新增第2.5.1条（根据图1检查补充）、第2.5.2条（根据图2检查补充）以及第2.6条（TPRS/CTIS故障检测）。
    *   更新了图1（补充检查）和图2（检查系统故障警告功能）的图示和说明。
    *   删除了原第2.3条。
*   **附件5（数据通信）**：
    *   **Part A（牵引车与挂车之间的TPMS/TPRS/CTIS数据通信）**：
 *   修订了标题。
 *   修订了第2.1.1、2.1.3、2.1.4条，更新了牵引车与挂车之间传输的消息参数列表和定义，并明确了时间/日期消息应使用SAE J1939DA 202110中的定义。
 *   修订了第2.2、2.3、2.3.1、2.4、2.5条，详细规定了触发驾驶员低胎压警告、TPMS/TPRS/CTIS故障指示、通信线路永久故障等情况的信号传输要求，并新增了数据暂时不可用时的传输规定。
    *   **Part B（挂车网关ECU与TPMS/TPRS/CTIS功能ECU之间的数据通信）**：
 *   修订了标题。
 *   修订了第1.2、2至2.4、3.1至3.3、4条，明确了挂车网关ECU与TPMS/TPRS/CTIS功能ECU之间接口的物理层、数据链路层（ISO 11898）、消息支持（ISO 11992-2）、诊断（ISO 11992-4）以及源地址使用（SAE J1939-71）等要求。
*   **附件6（测试）**：
    *   修订了第2.2.1.1.1、2.2.1.1.2、2.2.1.2.1、2.2.1.2.2、2.2.1.2.3、2.2.1.2.4条，更新了模拟挂车低胎压警告和TPMS/TPRS/CTIS故障时，控制线信号（EBS 23字节）的传输参数和测试验证要求。
    *   修订了图1和图2，更新了被测设备和车辆模拟器的布置示意图。
    *   修订了第3.2.2.2条，引用了附件3（TPMS）或附件4（TPRS/CTIS）的测试程序。

## 关联文件
*   本修正案基于UN Regulation No. 141 (Revision 1)。
*   引用了其他UN法规，如UN Regulation No. 10（电磁兼容性）和UN Regulation No. 13（制动系统）。
*   引用了多项国际标准，包括ISO 11992系列、ISO 7638系列、ISO 11898系列、SAE J1939系列等。

## 备注
本文件仅为文档工具。具有真实性和法律约束力的文本是：ECE/TRANS/WP.29/2022/87。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 11 个
> - 公式 0 个
> - 图像 3 个
> - 全文 Markdown 36,923 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 7)
<table><tr><td rowspan=1 colspan=1>Function /Parameter</td><td rowspan=1 colspan=1>ISO 11992-2: 2014 reference</td></tr><tr><td rowspan=1 colspan=1>Reverse gear status</td><td rowspan=1 colspan=1>EBS12Byte 2 Bit 5-6</td></tr><tr><td rowspan=1 colspan=1>Braking system wheel-based vehicle speed</td><td rowspan=1 colspan=1>EBS12Byte 7-8</td></tr><tr><td rowspan=1 colspan=1>Time/Date- Seconds</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 1</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Minutes</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 2</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Hours</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 3</td></tr><tr><td rowspan=1 colspan=1>Time/Date- Months</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 4</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Day</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 5</td></tr><tr><td rowspan=1 colspan=1>Time/Date- Year</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 6</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Local minute offset</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD Byte 7</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Local hour offset</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TD-Byte 8</td></tr><tr><td rowspan=1 colspan=1>Identification data index</td><td rowspan=1 colspan=1>RGE12 Byte 5</td></tr><tr><td rowspan=1 colspan=1>Identification data content</td><td rowspan=1 colspan=1>RGE12 Byte 6</td></tr></table>

#### 表 2 (page 8)
<table><tr><td rowspan=1 colspan=1>Function/Parameter</td><td rowspan=1 colspan=1>ISO 11992-2:2014 reference</td></tr><tr><td rowspan=1 colspan=1>Tyre/wheel identification (forEBS23 pressure)</td><td rowspan=1 colspan=1>EBS23 Byte 2</td></tr><tr><td rowspan=1 colspan=1>Tyre pressure</td><td rowspan=1 colspan=1>EBS23 Byte 5</td></tr><tr><td rowspan=1 colspan=1>Tyre/wheel identification(for RGE23)</td><td rowspan=1 colspan=1>RGE23 Byte 1</td></tr><tr><td rowspan=1 colspan=1>Tyre temperature</td><td rowspan=1 colspan=1>RGE23 Byte 2-3</td></tr><tr><td rowspan=1 colspan=1>Air leakage detection</td><td rowspan=1 colspan=1>RGE23 Byte 4-5</td></tr><tr><td rowspan=1 colspan=1>Tyre pressure threshold detection</td><td rowspan=1 colspan=1>RGE23Byte 6 Bit 1-3</td></tr><tr><td rowspan=1 colspan=1>Tyre module power supply status</td><td rowspan=1 colspan=1>RGE23Byte 6 Bit 4-5</td></tr><tr><td rowspan=1 colspan=1>Identification data index (l)</td><td rowspan=1 colspan=1>RGE23 Byte 7</td></tr><tr><td rowspan=1 colspan=1>Identification data content (l)</td><td rowspan=1 colspan=1>RGE23 Byte 8</td></tr></table>

#### 表 3 (page 8)
<table><tr><td rowspan=1 colspan=1>Function/Parameter</td><td rowspan=1 colspan=1>ISO 11992-2:2014 reference</td><td rowspan=1 colspan=1>Driverwarning required</td></tr><tr><td rowspan=1 colspan=1>Tyre Pressure Status(ForLow Tyre PressureWarning Indication)</td><td rowspan=1 colspan=1>EBS23 Byte 1Bit 1-2(002— tyre pressure insufficient) (1)</td><td rowspan=1 colspan=1>References to paragraph5.2.3., 5.2.4., 5.3.4., 5.3.5.and 5.5.2. in this UNRegulation</td></tr><tr><td rowspan=1 colspan=1>Tyre/wheel identification(corresponding to TyrePressure Status)</td><td rowspan=1 colspan=1>EBS23 Byte 2(XXXXXXXX2— actual Tyre/WheelID)OR(000000002— Tyre/Wheel ID notdefined or wheel not defined andaxle &gt; 1510)OR(111111112— Tyre/Wheel ID notavailable or wheel = 15io and axle =1510)</td><td rowspan=1 colspan=1>References to paragraph5.2.3., 5.2.4., 5.3.4., 5.3.5.and 5.5.2. in this UNRegulation</td></tr></table>

#### 表 4 (page 9)
<table><tr><td>Function /Parameter</td><td>ISO 11992-2:2014 reference</td><td>Driver warning required</td></tr><tr><td>Tyre Pressure Status (For TPMS/TPRS/CTIS Malfunction Indication)</td><td>EBS23 Byte 1 Bit 1-2 (102— error indicator)</td><td>Reference to paragraph 5.4.1., 5.4.2. and 5.5.2. in this UN Regulation</td></tr><tr><td>Tyre/wheel identification (corresponding to Tyre Pressure Status)</td><td>EBS23 Byte 2 XXXXXXXX2—actual Tyre/Wheel ID) OR (000000002— Tyre/Wheel ID not defined or wheel not defined and axle &gt;</td><td>Reference to paragraph 5.4.1., 5.4.2. and 5.5.2. in this UN Regulation</td></tr><tr><td rowspan="2"></td><td>1510) OR</td><td></td></tr><tr><td>(1111111lz— Tyre/Wheel ID not available or wheel = 15io and axle = 1510)</td><td></td></tr></table>

#### 表 5 (page 10)
<table><tr><td rowspan=1 colspan=1>Function/Parameter</td><td rowspan=1 colspan=1>ISO 11992-2:2014 reference</td><td rowspan=1 colspan=1>Driver warning required</td></tr><tr><td rowspan=1 colspan=1>Tyre Pressure Status(TPMS/TPRS/CTISdatatemporarily unavailable)</td><td rowspan=1 colspan=1>EBS23 Byte 1Bit 1-2(112— not available)</td><td rowspan=1 colspan=1>Not applicable</td></tr><tr><td rowspan=1 colspan=1>Tyre/wheel identification(corresponding to TyrePressure Status)</td><td rowspan=1 colspan=1>EBS23 Byte 2XXXXXXXX2—actual Tyre/WheelID)OR(000000002— Tyre/Wheel ID notdefined or wheel not defined and axle &gt;1510)OR(111111112— Tyre/Wheel ID notavailable or wheel = 151o and axle =1510)</td><td rowspan=1 colspan=1>Not applicable</td></tr></table>

#### 表 6 (page 11)
<table><tr><td rowspan=1 colspan=1>Function / Parameter</td><td rowspan=1 colspan=1> ISO 11992-2:2014 reference</td><td rowspan=1 colspan=1>Reference to paragraphs inthis UN Regulation</td></tr><tr><td rowspan=1 colspan=1> Reverse gear status (towingvehicle)</td><td rowspan=1 colspan=1>EBS12Byte 2 Bit 5-6</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Braking system wheel-basedvehicle speed (towing vehicle)</td><td rowspan=1 colspan=1>EBS12Byte 7-8</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Identification data index(towing vehicle)</td><td rowspan=1 colspan=1>RGE12 Byte 5</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Identification data content(towing vehicle)</td><td rowspan=1 colspan=1>RGE12 Byte 6</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Seconds (towingvehicle)</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TDByte 1</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1> Time/Date - Minutes (towingvehicle)</td><td rowspan=1 colspan=1> SAE J1939 PGN 65254 TDByte 2</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date- Hours (towingvehicle)</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TDByte 3</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date-Months (towingvehicle)</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TDByte 4</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date-Day (towing vehicle)</td><td rowspan=1 colspan=1> SAE J1939 PGN 65254 TDByte 5</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date- Year (towingvehicle)</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TDByte 6</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Local minute offset(towing vehicle)</td><td rowspan=1 colspan=1> SAE J1939 PGN 65254 TDByte 7</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Time/Date - Local hour offset(towing vehicle)</td><td rowspan=1 colspan=1>SAE J1939 PGN 65254 TDByte 8</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Braking system wheel-basedvehicle speed (towed vehicle)</td><td rowspan=1 colspan=1>EBS21Byte 3-4</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Lift axle 1 position(towed vehicle)</td><td rowspan=1 colspan=1>RGE21Byte 2 Bit 1-2</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr><tr><td rowspan=1 colspan=1>Lift axle 2 position(towed vehicle)</td><td rowspan=1 colspan=1>RGE21Byte 2 Bit 3-4</td><td rowspan=1 colspan=1>Paragraph 5.6.1.2.</td></tr></table>

#### 表 7 (page 12)
<table><tr><td rowspan=1 colspan=1>Control line signalling</td><td rowspan=1 colspan=1>EBS23Byte1Bits 1 - 2</td><td rowspan=1 colspan=1>EBS23Byte 2</td></tr><tr><td rowspan=1 colspan=1>Low Tyre Pressure Warning indication for tyre/wheelidentification number1,7 (Axle1,left inner)</td><td rowspan=1 colspan=1>002(tyre pressureinsufficient)</td><td rowspan=1 colspan=1>000101112(Tyre/Wheel“1,7&quot;)</td></tr></table>

#### 表 8 (page 13)
<table><tr><td rowspan=1 colspan=1>Control line signalling</td><td rowspan=1 colspan=1>EBS 23 Byte 1Bits 1 - 2</td><td rowspan=1 colspan=1>EBS 23 Byte 2</td></tr><tr><td rowspan=1 colspan=1>Low Tyre Pressure Warning indication (without knowntyre/wheel ID)</td><td rowspan=1 colspan=1>002(tyre pressureinsufficient)</td><td rowspan=1 colspan=1>000000002(Tyre/Wheel IDnot defined orwheel not definedand axle &gt;1510)OR111111112(Tyre/Wheel IDnot availableavailable orwheel = 151o andaxle =1510)</td></tr></table>

#### 表 9 (page 13)
<table><tr><td rowspan=1 colspan=1>Control line signalling</td><td rowspan=1 colspan=1>EBS 23 Byte 1Bits 1 - 2</td><td rowspan=1 colspan=1>EBS 23 Byte 2</td></tr><tr><td rowspan=1 colspan=1>TPMS/ TPRS/CTIS Malfunction for tyre/wheelidentification number 1,7 (Axle 1,left inner)</td><td rowspan=1 colspan=1>102(Error indicator)</td><td rowspan=1 colspan=1>000101112(Tyre/Wheel“1,7&quot;)</td></tr></table>

#### 表 10 (page 14)
<table><tr><td rowspan=1 colspan=1>Control line signalling</td><td rowspan=1 colspan=1>EBS 23 Byte1Bits 1 - 2</td><td rowspan=1 colspan=1>EBS 23 Byte 2</td></tr><tr><td rowspan=1 colspan=1>TPMS/ TPRS/ CTIS Malfunction (without knowntyre/wheel ID)</td><td rowspan=1 colspan=1>102(Error indicator)</td><td rowspan=1 colspan=1>000000002(Tyre/Wheel IDnot defined orwheel not definedand axle &gt;1510)OR111111112(Tyre/Wheel IDnot available orwheel = 151o andaxle = 1510)</td></tr></table>

### 图像（取前 3 张）

![“Figure 1 Refilling check ](../_mineru_assets/ECE R141 Rev1 Am2/79110b9f5f8f8cf9838c72b6e31df72858c7725dfe8c25710dd470933ab9d218.jpg)  
*“Figure 1 Refilling check * (page 6)

![“Figure 2 Checking system malfunction warning functionality. ](../_mineru_assets/ECE R141 Rev1 Am2/19efeff56cc08a34f886ec7903e63cddc3968cf9a1fab7c9b121a6b1db5e97f1.jpg)  
*“Figure 2 Checking system malfunction warning functionality. * (page 6)

![图 page 14](../_mineru_assets/ECE R141 Rev1 Am2/429034056b0d8190371dcd2e17111b4cae7d6756a8450ce1cbc02e62195ebd7d.jpg)  

