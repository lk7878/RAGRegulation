---
reg_id: ECE R49 Rev6 Am1
region: ece
type: type/amendment
title: Addendum 48 – Regulation No. 49, Revision 6 - Amendment 1
standard_body: UNECE
publication_date: 2013-08-06
implementation_date_new_vehicle: 2013-07-15
status: active
scope: This amendment introduces comprehensive provisions for dual-fuel engines and
  vehicles (using diesel and gaseous fuels) into UN Regulation No. 49, concerning
  measures against the emission of gaseous and particulate pollutants from compression-ignition
  and positive ignition engines for use in vehicles.
keywords:
- dual-fuel
- diesel-gas
- natural gas
- biomethane
- LPG
- LNG
- CNG
- emission limits
- type-approval
- OBD
- PEMS
- WHTC
- WHSC
- HDDF
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\49\R049r6am1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及替代关系。
- field: 技术要求限值
  status: unsure
  extracted: 有描述性说明
  original: null
  note: A 中描述了限值应用规则，但未给出具体数值；B 中未提供具体限值数值。
_ocr_upgraded: mineru
_mineru_content_hash: 1f7b5ea8fb104036
_mineru_outputs_dir: outputs/1f7b5ea8fb104036
_mineru_blocks:
  tables: 9
  formulas: 18
  images: 7
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 49, Revision 6 - Amendment 1

## 概览
本修正案是对UN法规第49号（关于压燃式和点燃式发动机污染物排放）的修订，主要引入了针对柴油-气体双燃料发动机和车辆的全面技术要求。修正案于2013年8月6日发布，2013年7月15日生效。

## 主要修订内容

### 1. 新增定义
新增了与双燃料发动机相关的关键定义，包括：
*   **双燃料发动机 (Dual-fuel engine)**：设计为同时使用柴油和气体燃料的发动机系统，两种燃料分别计量，消耗比例可根据运行工况变化。
*   **柴油模式 (Diesel mode)**：双燃料发动机的正常运行模式之一，在此模式下发动机在任何工况下均不使用气体燃料。
*   **双燃料模式 (Dual-fuel mode)**：双燃料发动机的正常运行模式之一，在此模式下发动机在某些工况下同时使用柴油和气体燃料。
*   **双燃料车辆 (Dual-fuel vehicle)**：由双燃料发动机驱动，并通过独立的车载存储系统供应发动机所用燃料的车辆。
*   **服务模式 (Service mode)**：双燃料发动机的一种特殊模式，当双燃料模式无法操作时（例如气罐空），为维修或将车辆移出交通而激活。
*   **气体能量比 (Gas Energy Ratio, GER)**：气体燃料能量占两种燃料（柴油和气体）总能量的百分比。

### 2. 双燃料发动机分类
根据在WHTC热循环部分的气体能量比（GER）和怠速/运行特性，将重型双燃料发动机分为五种类型：
*   **HDDF Type 1A**: GER ≥ 90%，怠速不使用纯柴油，无柴油模式。
*   **HDDF Type 1B**: GER ≥ 90%，怠速在双燃料模式下不使用纯柴油，有柴油模式。
*   **HDDF Type 2A**: 10% < GER < 90%，或GER ≥ 90%但怠速使用纯柴油，无柴油模式。
*   **HDDF Type 2B**: 10% < GER < 90%，或GER ≥ 90%但可在双燃料模式下怠速使用纯柴油，有柴油模式。
*   **HDDF Type 3B**: GER ≤ 10%，有柴油模式。（Type 3A未定义且不允许）

### 3. 型式认证要求
*   为获得双燃料发动机或发动机族作为独立技术单元的型式认证，制造商必须证明其符合本法规及新增的**附件15**中规定的要求。
*   新增了针对使用液化天然气/液化生物甲烷的发动机的**燃料特定型式认证**要求，规定了申请条件和特定的测试要求。
*   修订了批准标记的要求，为双燃料发动机增加了特定的数字代码（如1A, 1B, 2A, 2B, 3B）以区分发动机类型和批准的气体范围。

### 4. 排放限值
根据双燃料发动机的类型和运行模式，规定了相应的排放限值：
*   **Type 1A 和 Type 1B (双燃料模式)**：适用点燃式发动机的限值。
*   **Type 1B (柴油模式)**：适用压燃式发动机的限值。
*   **Type 2A 和 Type 2B**：在WHSC循环上，双燃料模式适用压燃式发动机限值。在WHTC循环上，CO、NOx、NH3和PM质量限值适用压燃/点燃式发动机限值，HC和PN限值需根据GER进行计算（线性插值或特定公式）。
*   **Type 3B**：无论双燃料模式还是柴油模式，均适用压燃式发动机限值。

### 5. 测试与演示要求
*   规定了各类双燃料发动机在实验室需进行的测试（WHTC, WHSC, WNTE），并区分了双燃料模式和柴油模式。
*   增加了**PEMS（实际行驶排放）测试**要求，在认证时需对双燃料模式进行测试，对于Type 1B, 2B, 3B发动机，还需额外进行柴油模式的PEMS测试。
*   提供了双燃料发动机排放测试的额外程序要求（附件15-附录4）和PEMS测试的额外要求（附件15-附录5）。

### 6. 车载诊断要求
*   双燃料发动机和车辆必须符合适用于柴油发动机的OBD要求。
*   增加了对**气体供应系统**的监控（组件监控）和对**气体燃料消耗异常**的监控（性能监控）要求。
*   对于Type 1B, 2B, 3B发动机，规定了运行模式对OBD机制（如计数器、DTC状态）影响的处理要求。

### 7. 指示器、警告系统和操作限制
*   要求向驾驶员提供**视觉指示**，显示发动机当前运行模式（双燃料、柴油或服务模式）。
*   必须配备**气体燃料罐空警告系统**。
*   对于Type 1A和2A发动机，当检测到气体燃料用尽、气体供应系统故障或气体消耗异常时，应激活**服务模式**并伴随**操作性限制**（例如车速限制）。
*   对于Type 1B, 2B和3B发动机，在上述情况下应切换到**柴油模式**。
*   详细说明了计数器机制、警告系统和操作限制的激活/停用逻辑（附件15-附录2）。

### 8. 新增附件
本修正案的核心是新增了**附件15：柴油-气体双燃料发动机和车辆的技术要求**。该附件详细规定了：
*   范围、定义和缩写。
*   双燃料发动机的附加认证要求（发动机族、父发动机选择）。
*   一般要求（运行模式条件、服务模式、指示器、通信扭矩等）。
*   性能要求（排放限值）。
*   演示要求（实验室测试、PEMS测试、安装验证）。
*   OBD要求。
*   NOx控制措施正确运行的要求。
*   在用符合性检查要求。
*   附加测试程序。
*   文件要求。
*   包含具体计算方法和示例的6个附录。

### 9. 其他修订
*   更新了信息文件、型式认证通讯、燃料技术数据等多个附件中的表格和内容，以纳入双燃料发动机的相关信息。
*   修订了排放计算中的若干公式。

## 影响
本修正案为柴油-气体双燃料发动机和车辆建立了一套完整的法规框架，涵盖了定义、分类、认证、测试、限值、OBD和在用符合性等全方面要求，旨在确保这类技术在实际使用中的排放控制有效性。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 15 个
> - 公式 18 个
> - 图像 7 个
> - 全文 Markdown 121,049 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 5)
**"Approval for dual-fuel engines fuelled with natural gas/biomethane or LPG **

<table><tr><td rowspan=2 colspan=1>Dual-fueltype</td><td rowspan=2 colspan=1>Diesel mode</td><td rowspan=1 colspan=4>Dual-fuelmode</td></tr><tr><td rowspan=1 colspan=1>CNG</td><td rowspan=1 colspan=1>LNG</td><td rowspan=1 colspan=1>LNG20</td><td rowspan=1 colspan=1>LPG</td></tr><tr><td rowspan=1 colspan=1>1A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td><td rowspan=1 colspan=1>Universal(2 tests)</td><td rowspan=1 colspan=1>Fuel specific(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td></tr><tr><td rowspan=1 colspan=1>1B</td><td rowspan=1 colspan=1>Universal(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td><td rowspan=1 colspan=1>Universal(2 tests)</td><td rowspan=1 colspan=1>Fuel specific(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td></tr><tr><td rowspan=1 colspan=1>2A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td><td rowspan=1 colspan=1>Universal(2 tests)</td><td rowspan=1 colspan=1>Fuel specific(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td></tr><tr><td rowspan=1 colspan=1>2B</td><td rowspan=1 colspan=1>Universal(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td><td rowspan=1 colspan=1>Universal(2 tests)</td><td rowspan=1 colspan=1>Fuel specific(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td></tr><tr><td rowspan=1 colspan=1>3B</td><td rowspan=1 colspan=1>Universal(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td><td rowspan=1 colspan=1>Universal(2 tests)</td><td rowspan=1 colspan=1>Fuel specific(1 test)</td><td rowspan=1 colspan=1>Universal orrestricted(2 tests)</td></tr></table>

#### 表 2 (page 6)
<table><tr><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="2"></td><td colspan="1" rowspan="2">Parentengine orenginetype</td><td colspan="5" rowspan="1">Engine family members</td></tr><tr><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1">B</td><td colspan="1" rowspan="1">C</td><td colspan="1" rowspan="1">D</td><td colspan="1" rowspan="1">E</td></tr><tr><td colspan="1" rowspan="1">·</td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.1.1.</td><td colspan="1" rowspan="1">Working principle: positive ignition/compressionignition/dual-fuellCycle four stroke / two stroke/ rotary1</td><td colspan="6" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.1.1.1.</td><td colspan="1" rowspan="1">Type of dual-fuel engine:Type 1A/Type 1B/Type 2A/Type 2B/Type 3B 1,14Gas Energy Ratio over the hot part of the WHTCtest-cycle14:              .%</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.1.6.2.</td><td colspan="1" rowspan="1">Idle on Diesel: yes/no1,14</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.2.2.</td><td colspan="1" rowspan="1">Heavy duty vehicles Diesel/Petrol/LPG/NG-H/NG-L/NG-HL/Ethanol (ED95)/Ethanol (E85)/dual-fuel1,15</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.4.2.</td><td colspan="1" rowspan="1">By fuel injection (only compression ignition ordual-fuel): yes/nol</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.12.7.0.6.</td><td colspan="1" rowspan="1">When appropriate,manufacturer reference of thedocumentation for installing the dual-fuel enginein a vehicle</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.2.17.</td><td colspan="1" rowspan="1">Specific information related to gas fuelled enginesand dual-fuel engines for heavy-duty vehicles (inthe case of systems laid out in a different manner,supply equivalent information)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">·</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.4.1.</td><td colspan="1" rowspan="1">CO2 mass emissions WHSC test6:(g/kWh)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.4.1.1.</td><td colspan="1" rowspan="1">For dual-fuel engines, COz mass emissionsWHSC test in diesel mode13:.g/kWhFor dual-fuel engines,COz mass emissionsWHSC test in dual-fuel mode13 (if applicable):g/kWh</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.4.2.</td><td colspan="1" rowspan="1">CO2   mass   emissions   WHTC   testT:(g/kWh)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.4.2.1.</td><td colspan="1" rowspan="1">For dual-fuel engines,CO2 mass emissionsWHTC test in diesel mode13:...../kWhFor dual-fuel engines, CO2 mass emissionsWHTC test in dual-fuel mode13:</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">g/kWh</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.5.</td><td colspan="1" rowspan="1">Fuel consumption for heavy duty engines</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.5.1.</td><td colspan="1" rowspan="1">Fuel consumption WHSC test16:(g/kWh)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.5.1.1.</td><td colspan="1" rowspan="1">For dual-fuel engines, fuel consumption WHSCtest in diesel mode13.g/kWhFor dual-fuel engines, fuel consumption WHSCtest in dual-fuel mode13:g/kWh</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.5.2.</td><td colspan="1" rowspan="1">Fuel consumption WHTC test, 16:(g/kWh)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3.5.5.2.1.</td><td colspan="1" rowspan="1">For dual-fuel engines, fuel consumption WHTCtest in diesel mode13:g/kWhFor dual-fuel engines, fuel consumption WHTCtest in dual-fuel mode13:g/kWh</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr></table>

#### 表 3 (page 7)
#### 表 4 (page 9)
**Table 4 WHSC test **

<table><tr><td rowspan=1 colspan=8>WHSC test (if applicable)</td></tr><tr><td rowspan=2 colspan=1>DFMult/add1</td><td rowspan=1 colspan=1>Co</td><td rowspan=1 colspan=1>THC</td><td rowspan=1 colspan=1>NMHC**</td><td rowspan=1 colspan=1>NOx</td><td rowspan=1 colspan=1>PM Mass</td><td rowspan=1 colspan=1>NH3</td><td rowspan=1 colspan=1>PMNumber</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Emissions</td><td rowspan=1 colspan=1>Co(mg/kWh)</td><td rowspan=1 colspan=1>THC(mg/kWh)</td><td rowspan=1 colspan=1>NMHC**(mg/kWh)</td><td rowspan=1 colspan=1>NOx(mg/kWh)</td><td rowspan=1 colspan=1>PM Mass(mg/kWh)</td><td rowspan=1 colspan=1>NHppm</td><td rowspan=1 colspan=1>PMNumber(#/kWh)</td></tr><tr><td rowspan=1 colspan=1>Test result</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Calculatedwith DF</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=8>CO2 emissions mass emission**                                   ..g/kWhFuel consumption***                                               ..g/kWh</td></tr></table>

#### 表 5 (page 9)
**Table 5 WHTCTest **

<table><tr><td rowspan=1 colspan=9>WHTC test</td></tr><tr><td rowspan=2 colspan=1>DF Mult/add1</td><td rowspan=1 colspan=1>Co</td><td rowspan=1 colspan=1>THC**</td><td rowspan=1 colspan=1>NMHC**</td><td rowspan=1 colspan=1>CH4**</td><td rowspan=1 colspan=1>NOx</td><td rowspan=1 colspan=1>PM Mass</td><td rowspan=1 colspan=1>NH</td><td rowspan=1 colspan=1>PMNumber</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Emissions</td><td rowspan=1 colspan=1>Co(mg/kWh)</td><td rowspan=1 colspan=1>THC**(mg/kWh)</td><td rowspan=1 colspan=1>NMHC**(mg/kWh)</td><td rowspan=1 colspan=1>CH4(mg/kWh)</td><td rowspan=1 colspan=1>NOx(mg/kWh)</td><td rowspan=1 colspan=1>PM Mass(mg/kWh)</td><td rowspan=1 colspan=1>NHppm</td><td rowspan=1 colspan=1>PMNumber(#/kWh)</td></tr><tr><td rowspan=1 colspan=1>Cold start</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Hot start w/oregeneration</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Hot start withregeneration(1)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>kr,u (mult/add)kr,d (mult/add)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Weighted testresult</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Final testresult with DF</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=9>CO2 emissions mass emission*                                 ..g/kWhFuel consumption***                                                ..g/kWh</td></tr></table>

#### 表 6 (page 10)
**"Table 2 Engine type codes for approval marks **

<table><tr><td rowspan=1 colspan=1>Engine type</td><td rowspan=1 colspan=1>Code</td></tr><tr><td rowspan=1 colspan=1>Diesel fuelled CI engine</td><td rowspan=1 colspan=1>D</td></tr><tr><td rowspan=1 colspan=1>Ethanol (ED95) fuelled CI engine</td><td rowspan=1 colspan=1>ED</td></tr><tr><td rowspan=1 colspan=1>Ethanol (E85) fuelled PI engine</td><td rowspan=1 colspan=1>E85</td></tr><tr><td rowspan=1 colspan=1>Petrol fuelled PI engine</td><td rowspan=1 colspan=1>P</td></tr><tr><td rowspan=1 colspan=1>LPG fuelled PI engine</td><td rowspan=1 colspan=1>Q</td></tr><tr><td rowspan=1 colspan=1>Natural gas fuelled PI engine</td><td rowspan=1 colspan=1>See paragraph 4.12.3.3.6.of this Regulation</td></tr><tr><td rowspan=1 colspan=1>Dual-fuel engines</td><td rowspan=1 colspan=1>See paragraph 4.12.3.3.7. of this Regulation</td></tr></table>

#### 表 7 (page 11)
<table><tr><td rowspan=2 colspan=1>Characteristics</td><td rowspan=2 colspan=1>Units</td><td rowspan=2 colspan=1>Basis</td><td rowspan=1 colspan=2>Limits</td><td rowspan=2 colspan=1>Test method</td></tr><tr><td rowspan=1 colspan=1>minimum</td><td rowspan=1 colspan=1>maximum</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=3>Reference fuel G20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Composition:</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Methane</td><td rowspan=1 colspan=1>% mole</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>99</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>ISO 6974</td></tr><tr><td rowspan=1 colspan=1>Balance (1)</td><td rowspan=1 colspan=1>% mole</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ISO 6974</td></tr><tr><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>% mole</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ISO 6974</td></tr><tr><td rowspan=1 colspan=1>Sulphur content</td><td rowspan=1 colspan=1>mg/m3 (2)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>ISO 6326-5</td></tr><tr><td rowspan=1 colspan=1>Wobbe Index(net)</td><td rowspan=1 colspan=1>MJ/m3 (3)</td><td rowspan=1 colspan=1>48.2</td><td rowspan=1 colspan=1>47.2</td><td rowspan=1 colspan=1>49.2</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=6>( Inerts (different from N2) + C + C2+.(2) Value to be determined at 293,2 K (20 C) and 101,3 kPa.(3 Value to be determined at 273.2 K (0 C) and 101,3 kPa.</td></tr></table>

#### 表 8 (page 13)
<table><tr><td>Monitoring The monitors comply with the requirements of section 4.2. of this</td><td>YES /NO</td></tr></table>

#### 表 9 (page 23)
**Table 1 Laboratory tests to be performed by a dual-fuel engine  / Demonstrations in case of installation of type-approved HDDF engines **

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Type 1A</td><td rowspan=1 colspan=1>Type 1B</td><td rowspan=1 colspan=1>Type 2A</td><td rowspan=1 colspan=1>Type 2B</td><td rowspan=1 colspan=1>Type 3B</td></tr><tr><td rowspan=2 colspan=1>WHTC</td><td rowspan=2 colspan=1>NMHC;CH4; CO;NOx; PM;PN; NH3</td><td rowspan=1 colspan=1>Dual-fuel mode:NMHC; CH4;CO; NOx; PM;PN; NH3</td><td rowspan=2 colspan=1>THC;NMHC;CH4; CO;NOx; PM;PN; NH3</td><td rowspan=1 colspan=1>Dual-fuel mode:THC; NMHC;CH4; CO; NOx;PM; PN; NH3</td><td rowspan=2 colspan=1>THC; CO;NOx; PM;PN; NH3</td></tr><tr><td rowspan=1 colspan=1>Diesel mode:THC; CO; NOx;PM; PN; NH3</td><td rowspan=1 colspan=1>Diesel mode:THC; CO; NOx;PM; PN; NH3</td></tr><tr><td rowspan=2 colspan=1>WHSC</td><td rowspan=2 colspan=1>no test</td><td rowspan=1 colspan=1>Dual-fuel mode:no test</td><td rowspan=2 colspan=1>NMHC;CO; NOx;PM; PN;NH3</td><td rowspan=1 colspan=1>Dual-fuel mode:NMHC; CO;NOX; PM; PN;NH3</td><td rowspan=2 colspan=1>THC; CO;NOx; PM;PN; NH3</td></tr><tr><td rowspan=1 colspan=1>Diesel mode:THC; CO; NOx;PM; PN; NH3</td><td rowspan=1 colspan=1>Diesel mode:THC; CO; NOx;PM; PN; NH3</td></tr><tr><td rowspan=2 colspan=1>WNTElaboratorytest</td><td rowspan=2 colspan=1>no test</td><td rowspan=1 colspan=1>Dual-fuel mode:no test</td><td rowspan=2 colspan=1>[HC]; CO;NOx; PM</td><td rowspan=1 colspan=1>Dual-fuel mode:[HC]; CO; NOx;PM</td><td rowspan=2 colspan=1>THC; CO;NOx; PM</td></tr><tr><td rowspan=1 colspan=1>Diesel mode:THC; CO; NOx;PM</td><td rowspan=1 colspan=1>Diesel mode:THC; CO; NOx;PM</td></tr></table>

#### 表 10 (page 25)
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Freeze frame</td><td rowspan=1 colspan=1>Data stream</td></tr><tr><td rowspan=1 colspan=1>In case of Type 1B,Type 2B andType 3B dual-fuel engines,operationmode of the Dual-fuel Engine (dual-fuel or diesel)</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr></table>

### 公式（取前 18 个）

**公式 1** (page 10):

$$
\mathbf { \tilde { \Gamma } } _ { \mathbf { k } _ { \mathrm { w , r } } } = \left( 1 - \frac { 1 , 2 4 4 2 \times \mathrm { H _ { a } } + 1 1 1 , 1 9 \times \mathbf { w } _ { \mathrm { A L F } } \times \frac { \mathbf { q } _ { \mathrm { m f , i } } } { \mathbf { q } _ { \mathrm { m a d , i } } } } { 7 7 3 , 4 + 1 , 2 4 4 2 \times \mathrm { H _ { a } } + \frac { \mathbf { q } _ { \mathrm { m f , i } } } { \mathbf { q } _ { \mathrm { m a d , i } } } \times \mathbf { k } _ { \mathrm { f , w } } \times 1 0 0 0 } \right) \times 1 , 0 0 8
$$

**公式 2** (page 10):

$$
\mathbf { \tilde { \Gamma } } _ { \mathbf { k } _ { \mathrm { w , r } } } = \left( 1 - \frac { 1 , 2 4 4 2 \times \mathrm { H _ { a } } + 1 1 1 , 1 9 \times \mathbf { w } _ { \mathrm { A L F } } \times \frac { \mathbf { q } _ { \mathrm { m f , i } } } { \mathbf { q } _ { \mathrm { m a d , i } } } } { 7 7 3 , 4 + 1 , 2 4 4 2 \times \mathrm { H _ { a } } + \frac { \mathbf { q } _ { \mathrm { m f , i } } } { \mathbf { q } _ { \mathrm { m a d , i } } } \times \mathbf { k } _ { \mathrm { f , w } } \times 1 0 0 0 } \right) \Bigg / \left( 1 - \frac { \mathrm { P _ { r } } } { \mathrm { P _ { b } } } \right)
$$

**公式 3** (page 10):

$$
" \mathbf { k } _ { \mathrm { w , r } } = \left( \frac { 1 } { 1 + \mathbf { a } \times 0 , 0 0 5 \times \left( \mathbf { c } _ { \mathrm { C O 2 } } + \mathbf { c } _ { \mathrm { C O } } \right) } - \mathbf { k } _ { \mathrm { w 1 } } \right) \times 1 , 0 0 8
$$

**公式 4** (page 10):

$$
\begin{array} { r } { \mathbf { \ddot { \mu } } \mathbf { k } _ { \mathrm { f , w } } = 0 , 0 5 5 5 9 4 \times \mathbf { W } _ { \mathrm { A L F } } + 0 , 0 0 8 0 0 2 1 \times \mathbf { W } _ { \mathrm { D E L } } + 0 , 0 0 7 0 0 4 6 \times \mathbf { W } _ { \mathrm { E P S } } } \end{array}
$$

**公式 5** (page 10):

$$
\mathrm { \ " } \mathbf { k } _ { \mathrm { w 1 } } = \frac { 1 , 6 0 8 \times \mathrm { H _ { a } } } { 1 0 0 0 + \left( 1 , 6 0 8 \times \mathrm { H _ { a } } \right) }
$$

**公式 6** (page 10):

$$
\mathrm { " \mathbf { k } _ { w , e } = \left[ \left( 1 - \frac { \mathbf { a } \times \mathbf { c } _ { C O 2 w } } { 2 0 0 } \right) - \mathbf { k } _ { w 2 } \right] \times 1 , 0 0 8 }
$$

**公式 7** (page 11):

$$
\mathrm { ~ \ " ~ } \mathbf { k } _ { \mathrm { w , e } } = \left[ \left( \begin{array} { c } { \left( 1 - \mathbf { k } _ { \mathrm { w 2 } } \right) } \\ { 1 + \frac { \mathbf { a } \times \mathbf { c } _ { \mathrm { C O 2 d } } } { 2 0 0 } } \end{array} \right) \right] \times 1 , 0 0 8
$$

**公式 8** (page 11):

$$
\ " \mathbf { k } _ { \mathrm { w } 2 } = \frac { 1 , 6 0 8 \times \left[ \mathrm { H } _ { \mathrm { d } } \times \left( 1 - \displaystyle \frac { 1 } { \mathrm { D } } \right) + \mathrm { H } _ { \mathrm { a } } \times \left( \frac { 1 } { \mathrm { D } } \right) \right] } { 1 0 0 0 + \left\{ 1 , 6 0 8 \times \left[ \mathrm { H } _ { \mathrm { d } } \times \left( 1 - \displaystyle \frac { 1 } { \mathrm { D } } \right) + \mathrm { H } _ { \mathrm { a } } \times \left( \frac { 1 } { \mathrm { D } } \right) \right] \right\} }
$$

**公式 9** (page 11):

$$
\ " \mathbf { k } _ { \mathrm { w , d } } = \left( 1 - \mathbf { k } _ { \mathrm { w } 3 } \right) \times 1 , 0 0 8
$$

**公式 10** (page 11):

$$
\mathrm { \ " } \mathbf { k } _ { \mathrm { w } 2 } = \frac { 1 , 6 0 8 \times \mathrm { H } _ { \mathrm { d } } } { 1 0 0 0 + \left( 1 , 6 0 8 \times \mathrm { H } _ { \mathrm { d } } \right) }
$$

**公式 11** (page 20):

$$
\mathrm { T H C } _ { \mathrm { G E R } } = \mathrm { N M H C } _ { \mathrm { P I } } + ( \mathrm { C H 4 } _ { \mathrm { P I } } \mathrm { \mathrm { ^ * G E R } _ { \mathrm { W H T C } } } )
$$

**公式 12** (page 28):

$$
\begin{array} { r l } & { \mathbf { m } _ { \mathrm { f u e l , c o r r } } = \mathbf { m } _ { \mathrm { f u e l } } - ( \mathbf { m } _ { \mathrm { T H C } } + \cfrac { \mathbf { A } _ { \mathrm { C } } + \mathbf { a } \times \mathbf { A } _ { \mathrm { H } } } { \mathbf { M } _ { \mathrm { C O } } } \times \mathbf { m } _ { \mathrm { C O } } + \frac { \mathbf { W } _ { \mathrm { G A M } } + \mathbf { W } _ { \mathrm { D E L } } + \mathbf { W } _ { \mathrm { E P S } } } { 1 0 0 } \times \mathbf { m } _ { \mathrm { f u e l } } ) } \\ & { \mathbf { m } _ { \mathrm { C O _ { 2 } , f u e l } } = \cfrac { \mathbf { M } _ { \mathrm { C O _ { 2 } } } } { \mathbf { A } _ { \mathrm { C } } + \mathbf { a } \times \mathbf { A } _ { \mathrm { H } } } \times \mathbf { m } _ { \mathrm { f u e l , c o r r } } } \end{array}
$$

**公式 13** (page 28):

$$
\bf { \Pi } _ { \mathrm { { C O } _ { 2 } , u r e a } } ^ { \mathrm { { C } _ { \ u r e a } } } = \frac { \bf { C } _ { \mathrm { { u r e a } } } } { 1 0 0 } \times \frac { \bf { M } _ { \mathrm { { C O } _ { 2 } } } } { \bf { M } _ { \mathrm { { C O } ( N H _ { 2 } ) _ { 2 } } } } \times \bf { m } _ { \mathrm { { u r e a } } }
$$

**公式 14** (page 28):

$$
\mathrm { ~ \ m ~ } _ { _ { \mathrm { C O } _ { _ 2 } } } = \mathrm { ~ m ~ } _ { _ { \mathrm { C O } _ { _ 2 } , \mathrm { f u e l } } } + \mathrm { ~ m ~ } _ { _ { \mathrm { C O } _ { _ 2 } , \mathrm { u r e a } } }
$$

**公式 15** (page 41):

$$
\mathbf { k } _ { \mathrm { h , D } } = { \frac { 1 5 , 6 9 8 \times \mathbf { H } _ { \mathrm { a } } } { 1 0 0 0 } } + 0 { , } 8 3 2
$$

**公式 16** (page 45):

$$
\begin{array} { r l } & { W _ { A , E } = \frac { W _ { A , \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } } { q _ { \mathrm { o r f } } } \times q _ { \mathrm { o r f } } \times \mathcal { W } _ { A , \mathrm { o r f } } \times q _ { \mathrm { o r f } } } \\ & { W _ { B , \mathrm { o r f } } = \frac { W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } + W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } } { q _ { \mathrm { o r f } } + q _ { \mathrm { o r f } } } } \\ & { W _ { A , \mathrm { o r f } } = \frac { W _ { A , \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } + W _ { A , \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } } { q _ { \mathrm { o r f } } + q _ { \mathrm { o r f } } } } \\ & { W _ { B , \mathrm { o r f } } = \frac { W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } + W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } } { q _ { \mathrm { o r f } } + q _ { \mathrm { o r f } } } } \\ & { W _ { B , \mathrm { o r f } } = \frac { W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } + W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } } { q _ { \mathrm { o r f } } + q _ { \mathrm { o r f } } } } \\ & { W _ { B , E } = \frac { W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } + W _ { \mathrm { o r f } } \times \mathcal { A } _ { \mathrm { o r f } } } { q _ { \mathrm { o r f } } + q _ { \mathrm { o r f } } } } \end{array}
$$

**公式 17** (page 45):

$$
\alpha = 1 1 . 9 1 6 4 \times \frac { w _ { A L F } } { w _ { B E T } }
$$

**公式 18** (page 46):

$$
\varepsilon = 0 . 7 5 0 7 2 \times \frac { w _ { E P S } } { w _ { B E T } }
$$

### 图像（取前 7 张）

![Figure 1 Illustration of the HC limits in the case of a HDDF Type2 engine operating in dual-fuel mode during the WHTC cycle (natural gas dual-fuel engines) ](../_mineru_assets/ECE R49 Rev6 Am1/0477c1e06be446a6e2d2f1481e9ba268ad4c46d402f4daf5ace7adedac0e5132.jpg)  
*Figure 1 Illustration of the HC limits in the case of a HDDF Type2 engine operating in dual-fuel mode during the WHTC cycle (natural gas dual-fuel engines) * (page 21)

![Figure 2 Illustration of the PN limits in the case of a HDDF Type 2 engine operating in dual-fuel mode during the WHTC cycle ](../_mineru_assets/ECE R49 Rev6 Am1/e4c85e5c8923587da6ebbc1daaabc892bf6fac1cde2d1d56c0eaf3e49f0ea02b.jpg)  
*Figure 2 Illustration of the PN limits in the case of a HDDF Type 2 engine operating in dual-fuel mode during the WHTC cycle * (page 22)

![Figure A2.1.1 Illustration of the gas supply counter mechanism (Type A HDDF) - use-case 1 ](../_mineru_assets/ECE R49 Rev6 Am1/fe325dbf9eb3cc9b31a69b8810bc280a20a70cb6feef23942553edcc2631c05a.jpg)  
*Figure A2.1.1 Illustration of the gas supply counter mechanism (Type A HDDF) - use-case 1 * (page 32)

![Figure A2.1.2 Illustration of the gas supply counter mechanism (Type A HDDF) - use-case 2 ](../_mineru_assets/ECE R49 Rev6 Am1/cf6d4c8928a4fc749ed6a042c7e068257916bd22857d3562e4a5686b4577d8c0.jpg)  
*Figure A2.1.2 Illustration of the gas supply counter mechanism (Type A HDDF) - use-case 2 * (page 33)

![Figure A2.1.3 Illustration of the gas supply counter mechanism (Type A HDDF) - use-case 3 ](../_mineru_assets/ECE R49 Rev6 Am1/041423de77c8fdbf02ebede0e83f4e87dd45b36e8177a41acd5335b5b614efe3.jpg)  
*Figure A2.1.3 Illustration of the gas supply counter mechanism (Type A HDDF) - use-case 3 * (page 34)

![图 page 35](../_mineru_assets/ECE R49 Rev6 Am1/3edab0fb8593fef633269eb2f244d9eede1ff02c1a0c6346ec9d6a5b7ba07fca.jpg)  

![Figure A2.3 Illustration of the events occurring in case of a malfunctioning gas supply system (Types A and B HDDF) ](../_mineru_assets/ECE R49 Rev6 Am1/f1970777edca3fbe7c51eca67d418b3ea364e11544dc03435c5d216b84ad551c.jpg)  
*Figure A2.3 Illustration of the events occurring in case of a malfunctioning gas supply system (Types A and B HDDF) * (page 36)

