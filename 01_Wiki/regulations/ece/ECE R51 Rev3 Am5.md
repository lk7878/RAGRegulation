---
reg_id: ECE R51 Rev3 Am5
region: ece
type: type/amendment
title: Addendum 50 – UN Regulation No. 51, Revision 3 - Amendment 5, Supplement 5
  to 03 series of amendments
subject: Noise of M and N categories of vehicles
status: active
standard_body: UNECE
publication_date: 2019-11-11
implementation_date_new_vehicle: 2019-10-15
source: ECE/TRANS/WP.29/2019/4/Rev.1
source_file: 国外法规\ECE标准\标准法规-UNECE\41～80\51\R051r3am5e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\51\R051r3am5e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: 原文B未提及在用车辆的实施日期。
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
_ocr_upgraded: mineru
_mineru_content_hash: e1ddf4ba22646e3d
_mineru_outputs_dir: outputs/e1ddf4ba22646e3d
_mineru_blocks:
  tables: 1
  formulas: 0
  images: 1
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 51 - Amendment 5 (Supplement 5 to 03 series)

**法规编号**: UN R051
**修订版本**: Revision 3
**修正案**: Amendment 5 (Supplement 5 to the 03 series of amendments)
**生效日期**: 2019年10月15日
**发布机构**: 联合国欧洲经济委员会 (UNECE)
**官方/法律约束文本**: ECE/TRANS/WP.29/2019/4/Rev.1

## 概述
本文件是《关于采用轮式车辆、可安装和/或用于轮式车辆的设备及部件的统一技术法规以及基于这些联合国法规批准相互认可条件的协定》下，联合国法规第51号（M类和N类车辆噪声）的修订案。
本修正案为第03系列修正案的补充5。

## 主要内容

### 1. 过渡条款
新增段落11.10和11.11，规定：
*   **11.10**: 在2020年5月1日之前，补充4不适用于在补充4生效日期之前最初批准的现有型式认证。
*   **11.11**: 在2020年5月1日之前，补充5不适用于在补充5生效日期之前最初批准的现有型式认证。

### 2. 附件3附录修订
修订了图4c，标题为：
> "Figure 4c
> Flowchart for vehicles tested according to paragraph 3.1.2.1. of Annex 3 to this Regulation – Gear selection using locked gear PART 2"

图4c内容描述了根据法规附件3第3.1.2.1段进行测试的车辆（使用锁定档位）的档位选择流程图，包含两种主要情况（Case 1和Case 2）的判断逻辑，涉及稳定加速度、发动机转速与参考加速度（`a_wot ref`）、城市加速度（`a_urban`）及转速阈值（`S`）的比较。

### 3. 表1修订
修订了表1，标题为："Table 1. Examples for Devices and Measures to Enable a Vehicle Tested within the Acceleration Boundaries"（表1. 使车辆在加速度边界内进行测试的装置和措施示例）。

该表列出了四种主要措施及其子类，用于确保车辆能在规定的加速度边界内进行测试：

| 编号 | 影响/措施类型 | 子类 | 具体措施 | 附加要求 |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **锁定离散档位比** | 1* | 驾驶员可以锁定一个离散档位比 | 无 |
| | | 2 | 车辆上存在一个离散档位比，但驾驶员无法使用。制造商可以通过车载（隐藏）功能或外部设备激活锁定。 | 无 |
| **2** | **受控换档管理**<br>（适用于无法锁定的变速箱，或锁定档位无法提供有效测试结果的情况） | 1* | 强制降档（Kickdown）功能被停用 | 无 |
| | | 2 | 测试过程中可能发生换档，换档通过激活内部功能或外部设备来控制。 | 加速度**应在`a_urban`和`a_wot,ref`之间，且不超过2.0 m/s²。 |
| **3** | **定义的部分负荷驾驶****** | 1 | 通过机械装置限制加速度 | 定义的加速度**应在`a_urban`和`a_wot,ref`之间，且不超过2.0 m/s²。<br>对于ASEP**，锚点参数计算如下：<br>`L_anchor = (L_test - k_p * L_crs) / (1 - k_p)`<br>其中 `k_p = 1 - a_test / a_wot,ref`<br>且 `a_wot,ref` 根据第3.1.2.1.2.4段确定。 |
| | | 2 | 用于部分负荷加速度的外部编程*** | 加速度不超过2.0 m/s²。<br>`n_anchor = n_bb,test * 3.6 / v_bb,test * (a_wot,ref * (20 + 2 * l) + 192.9)^0.5` |
| **4** | **混合解决方案（模式）**<br>（此措施将是上述解决方案在特定模式下的组合） | 1* | 模式在车辆上可用，可由驾驶员选择。 | 无 |
| | | 2 | 模式在车辆上可用，但只能由制造商通过隐藏功能或外部设备激活。 | 无 |
| | | 3 | 模式在车辆上不可用，外部软件覆盖内部软件。 | 加速度**应在`a_urban`和`a_wot,ref`之间，且不超过2.0 m/s²。 |

**表注**:
*   **\***: 注释：这是标准情况，已包含在法规文本中。
*   **\****: 适用于M1、N1类及总质量≤3,500 kg的M2类车辆。
*   **\*****: 部分负荷应通过模拟加速踏板行程限制来实现。不允许干扰发动机控制管理。
*   **\******: 适用于M1、N1类及总质量≤3,500 kg的M2类车辆。对于附件3中`L_urban`的进一步计算，部分负荷下测量的声级应取代全油门下的声级。测试期间达到的部分负荷加速度应用于计算部分功率因子`k_P`，以替代`a_wot ref`。测试程序和数据处理遵循相同的原则。尽管是在部分负荷下测试，但仍应使用符号`x_wot`（例如`L_wot`, `a_wot`, …）。

### 4. 附件7修订
修订了附件7第5.2段，关于档位α的确定：
*   **5.2**. 档位α的确定如下：
    *   α = 3，适用于手动变速箱以及在锁定位置测试且档位数不超过5的自动变速箱。
    *   α = 4，适用于手动变速箱以及在锁定位置测试且档位数为6或更多的自动变速箱。**如果**在4档下从AA线到BB线加车辆长度计算的加速度超过1.9 m/s²，则应选择第一个更高档位（α > 4）且其加速度低于或等于1.9 m/s²。
    *   对于在非锁定条件下测试的车辆，用于进一步计算的传动比应根据附件3中的加速度测试结果，使用报告的BB'线处的发动机转速和车速来确定。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 1 个
> - 公式 0 个
> - 图像 1 个
> - 全文 Markdown 6,316 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 1 个）

#### 表 1 (page 3)
**"Table 1. Examples for Devicesand Measures to Enable a Vehicle Tested within the Acceleration Boundaries **

<table><tr><td rowspan=1 colspan=1>No.</td><td rowspan=1 colspan=1>Impact</td><td rowspan=1 colspan=1>SubNo.</td><td rowspan=1 colspan=1>Measure</td><td rowspan=1 colspan=1>Additional Requirements</td></tr><tr><td rowspan=2 colspan=1>1</td><td rowspan=2 colspan=1>Lock of a discrete gear ratio</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>A discrete gear ratio can be locked bythe driver</td><td rowspan=1 colspan=1>none</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>A discrete gear ratio is availableonboard, but is not available to thedriver.Locking can be activated by themanufacturer with an on board (hidden)function or with an external device</td><td rowspan=1 colspan=1>none</td></tr><tr><td rowspan=2 colspan=1>2</td><td rowspan=2 colspan=1>Controlled gear shiftmanagement:Applicable totransmissions whichcannot be locked,orwhere no locked gearprovides a valid testresult</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Kickdown is deactivated</td><td rowspan=1 colspan=1>none</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Gear shift change(s) can happen duringthe test, gear shift is controlled byactivation of an internal function orexternal device</td><td rowspan=1 colspan=1>Acceleration** shall be between aurbanand awot,ref, not exceeding 2.0 m/s2.</td></tr><tr><td rowspan=2 colspan=1>3</td><td rowspan=2 colspan=1>Defined partial loaddriving****</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Acceleration is limited by a mechanicaldevice</td><td rowspan=2 colspan=1>Defined acceleration** shall bebetween aurban and awot,ref, notexceeding 2.0 m/s2.For ASEP**, the anchor pointparameter are calculated by:Lanchor =(Lest -kp*Lers)/(1-kp)with kp=1-atest/awot,refand awot.ref according to 3.1.2.1.2.4.but not higher than 2.0 m/s²Ianchor=btes *3.6/Vbtest*(awotrer*(20+2*1)+192,9)0.5</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>External Programming for partial loadacceleration*</td></tr><tr><td rowspan=3 colspan=1>4</td><td rowspan=3 colspan=1>Mixed Solution(Mode):This measure will bea mix of the abovesolutions combinedin a specific mode</td><td rowspan=1 colspan=1>1*</td><td rowspan=1 colspan=1>Mode is available onboard and can beselected by the driver</td><td rowspan=1 colspan=1>none</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Mode is available onboard and canonly be activated by the manufacturerwith a hidden function or an externaldevice</td><td rowspan=1 colspan=1>none</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Mode is not available onboard,anexternal software overrides the internalsoftware</td><td rowspan=1 colspan=1>Acceleration** shall be between aurbanand awo,ref, not exceeding 2.0 m/s².</td></tr></table>

### 图像（取前 1 张）

![图 page 2](../_mineru_assets/ECE R51 Rev3 Am5/5243dfca06cc380cdb8d1437f54e514b1b210a6f9924f2d2df037a2387748648.jpg)  

