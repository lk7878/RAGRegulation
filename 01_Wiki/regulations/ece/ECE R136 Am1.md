---
reg_id: ECE R136 Am1
region: ece
title: Uniform provisions concerning the approval of vehicles of category L with regard
  to specific requirements for the electric power train
type: type/amendment
status: active
amend_to: UN R136
amend_type: 01 series of amendments
date_issue: 2023-02-24
date_enforce: 2023-01-04
source_file: R136am1e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\136\R136am1e.pdf
publication_date: 2023-02-24
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: ece
  original: null
  note: B 未明确提及标准机构名称，但文件来自 ECE。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 未提及针对新车型的具体实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及针对在用车型的具体实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未提及被替代的法规。
- field: 技术要求的限值
  status: unsure
  extracted: null
  original: null
  note: B 提供的文本片段未包含具体的限值数据。
_ocr_upgraded: mineru
_mineru_content_hash: 972bea30a759ca4d
_mineru_outputs_dir: outputs/972bea30a759ca4d
_mineru_blocks:
  tables: 0
  formulas: 8
  images: 6
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 136 - Amendment 1 (01 series of amendments)

## 概览
本文件是联合国第136号法规的第01系列修正案，于2023年1月4日生效。该修正案对关于L类车辆电动传动系统特定要求的统一规定进行了全面修订。

## 主要修订内容

### 1. 适用范围与定义 (第1、2条)
*   **第I部分**：适用于最大设计速度超过6 km/h的L1类车辆（不包括永久连接电网的车辆）的电动传动系统安全要求。明确不涵盖与电动传动系统高压母线非电连接的高压部件和系统。
*   **第II部分**：适用于最大设计速度超过6 km/h的L类车辆（不包括永久连接电网的车辆）的可充电储能系统安全要求。明确不适用于主要为启动发动机、照明或其他车辆辅助系统供电的电池。
*   **新增和修订了大量术语定义**，包括但不限于：
    *   `Aqueous electrolyte` (水性电解质)
    *   `Automatic disconnect` (自动断开装置)
    *   `Breakout harness` (测试用连接线束)
    *   `Electric power train` (电动传动系统)
    *   `Electrical protection barrier` (电气防护屏障)
    *   `Normal operating conditions` (正常运行条件)
    *   `Protection degree IPXXB/IPXXD` (防护等级IPXXB/IPXXD)
    *   `REESS subsystem` (REESS子系统)
    *   `Specific voltage condition` (特定电压条件)
    *   `Tested-Device` (被测装置)
    *   `Thermal event/runaway/propagation` (热事件/热失控/热蔓延)
    *   `Venting` (泄压)

### 2. 电动传动系统安全要求 (第5条)
*   **电击防护**：针对直接接触和间接接触的防护要求进行了详细规定和更新。
*   **绝缘电阻**：修订了针对不同类型电动传动系统（独立DC/AC总线、混合DC-AC总线、燃料电池车辆）的绝缘电阻要求及测量方法。增加了对REESS充电耦合系统的绝缘电阻要求。
*   **新增防水保护要求**：车辆在接触水（如清洗、涉水）后需保持绝缘电阻。制造商可选择通过文件证明、物理测试或提供绝缘电阻监控系统等方式满足要求。
*   **REESS相关要求**：
    *   明确了车辆安装已按第II部分型式批准的REESS，或REESS（包括相关车辆部件）需满足第6条要求。
    *   **新增REESS故障警告要求**：当车辆处于“可主动驾驶模式”时，若发生第6.13至6.15条所述事件，应向驾驶员提供警告。
    *   **新增纯电动车低电量警告要求**：当REESS电量状态过低时，应向驾驶员提供警告。
*   **防止意外移动**：对车辆启动、离车、外部充电时的防意外移动功能及功能安全要求（如模式选择/退出、功率降低指示、倒车控制）进行了修订。
*   **氢气排放**：更新了测试引用条款。

### 3. REESS安全要求 (第6条)
*   修订了**振动、热冲击和循环、机械冲击、跌落、机械完整性（侧倾）、外部短路保护、过充保护、过放保护、过热保护**等测试的适用条件、程序和验收标准。
*   **删除**了原有的`6.10. 浸水保护`测试。
*   **新增多项测试和要求**：
    *   **`6.10. 过流保护`**：适用于可通过外部直流电源充电的REESS。
    *   **`6.11. 低温保护`**：要求制造商提供文件，说明REESS在低温下的安全性能及监控控制措施。
    *   **`6.12. REESS排放气体管理`**：要求车辆乘员不会暴露于REESS排放气体造成的危险环境中。
    *   **`6.13. REESS安全管理控制装置故障警告`**：要求REESS或车辆系统在管理REESS安全运行的控制装置发生故障时提供警告信号。
    *   **`6.14. REESS内部热事件警告`**：要求REESS或车辆系统在发生热事件时提供警告信号。
    *   **`6.15. 热蔓延`**：对于含有易燃电解质的REESS，要求通过风险分析和功能设计，确保由单电池热失控引发的热蔓延不会对乘员造成危险环境，并能提供提前预警。

### 4. 管理条款 (第3, 4, 7, 8, 9, 10, 12条)
*   更新了**车辆和REESS的批准申请、批准、修改（修订与扩展）、生产一致性、批准撤销、生产终止**等流程的表述。
*   **新增过渡条款 (第12条)**：
    *   自本修正案正式生效之日起，缔约方不得拒绝按本修正案授予或接受型式批准。
    *   2025年9月1日后，缔约方无义务接受在该日期后首次颁发的先前系列修正案的批准。
    *   2027年9月1日前，缔约方应接受在2025年9月1日前首次颁发的先前系列修正案的批准。
    *   2027年9月1日后，缔约方无义务接受按本法规先前系列修正案颁发的批准。

### 5. 附录更新
*   **附录1**：更新了信息文件和沟通文件模板。
*   **附录2**：更新了批准标记的排列方式。
*   **附录3**：更新了防护等级测试条件，并替换了关节测试指的图示。
*   **新增附录4**：电位均衡验证方法。
*   **附录5A & 5B**：车辆和组件绝缘电阻测量方法（更新了电压符号等）。
*   **新增附录6**：车载绝缘电阻监控系统功能确认方法。
*   **新增附录7A & 7B**：
    *   `附录7A`：基于文件验证车辆电气设计防水后绝缘电阻符合性的方法。
    *   `附录7B`：车辆防水效应的测试程序（清洗和涉水）。
*   **附录8**：氢气排放测试（重编号并更新引用）。
*   **附录9系列**：将原附录8系列重编号为附录9系列，并进行了全面更新，包括：
    *   `附录9 - 附录1`：标准循环程序。
    *   `新增附录9 - 附录2`：SOC调整程序。
    *   `附录9A-9J`：分别对应振动、热冲击和循环、跌落、机械冲击、火烧、外部短路、过充保护、过放保护、过热保护、过流保护测试，更新了安装、测试条件和程序。
*   **附录10A & 10B**：车载充电器保护测试和车辆充电过程中的故障电流保护测试（由原附录9A/B重编号）。

---
**注**：本文件仅为文档工具。具有真实法律约束力的文本是：ECE/TRANS/WP.29/2022/72。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 0 个
> - 公式 8 个
> - 图像 6 个
> - 全文 Markdown 116,030 字符（见 `outputs/<hash>/full.md`）

### 公式（取前 8 个）

**公式 1** (page 21):

$$
\mathbf { a } = 8 \mathrm { m m } \mathrm { m i n } .
$$

**公式 2** (page 24):

$$
\mathbf { R } = \mathbf { U } / \mathbf { I }
$$

**公式 3** (page 25):

$$
\begin{array} { r l } & { \mathrm { R i } = \mathrm { R o ^ { * } U _ { b } } ^ { * } ( 1 / \mathrm { U _ { l } } ^ { \mathrm { ~ , ~ } } - 1 / \mathrm { U _ { l } } ) } \\ & { } \\ & { \qquad \ldots } \end{array}
$$

**公式 4** (page 26):

$$
\begin{array} { r l } & { \mathrm { R i } = \mathrm { R o ^ { * } U _ { b } } ^ { * } ( 1 / \mathrm { U } _ { 2 } ^ { \mathrm { ~ , ~ } } - 1 / \mathrm { U } _ { 2 } ) } \\ & { \qquad \cdots ^ { \mathrm { ~ } } } \end{array}
$$

**公式 5** (page 27):

$$
\begin{array} { r l } & { \mathrm { R i } = \mathrm { R o ^ { * } U _ { b } } ^ { * } ( 1 / \mathrm { U _ { l } } ^ { \mathrm { , } } - 1 / \mathrm { U _ { l } } ) } \\ & { } \\ & { \qquad \ldots } \end{array}
$$

**公式 6** (page 27):

$$
\begin{array} { r l } & { \mathrm { R i } = \mathrm { R o ^ { * } U _ { b } } ^ { * } ( 1 / \mathrm { U _ { 2 } } ^ { \mathrm { , } } - 1 / \mathrm { U _ { 2 } } ) } \\ & { \qquad \cdots ^ { \mathrm { u } } } \end{array}
$$

**公式 7** (page 28):

$$
1 / ( 1 / ( 9 5 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) \leq \mathrm { { R o } } < 1 / ( 1 / ( 1 0 0 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) } }
$$

**公式 8** (page 28):

$$
1 / ( 1 / ( 4 7 5 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) \leq \mathrm { { R o } } < 1 / ( 1 / ( 5 0 0 \mathrm { { x U } ) - 1 / \mathrm { { R i } } ) } }
$$

### 图像（取前 6 张）

![图 page 7](../_mineru_assets/ECE R136 Am1/b75344cbca161499eb72a9143b3882e93035acf03480f799e65398a2bd9e0170.jpg)  

![Figure 2 ](../_mineru_assets/ECE R136 Am1/432652818533e50509dc6d41d8e0eac89b3aa8d5047c2fd54696c129505c2a9b.jpg)  
*Figure 2 * (page 21)

![图 page 23](../_mineru_assets/ECE R136 Am1/d242d7104f53c532b1ee3214157a29e41e0944ff63c8c04e0221493f7ff91060.jpg)  

![Figure 1 Example of Test Method using DC Power Supply ](../_mineru_assets/ECE R136 Am1/526a63466cfd8b3dbf7f77f103331482a2df50594e021cb142001a54711be381.jpg)  
*Figure 1 Example of Test Method using DC Power Supply * (page 24)

![Figure 1 Standard Nozzle for the Test ](../_mineru_assets/ECE R136 Am1/b9ed7bab5c6170b3c1919954b5cc85044882c1d2d8a25075745d5cdf8bbf8e66.jpg)  
*Figure 1 Standard Nozzle for the Test * (page 30)

![Figure 2 Splashing Test Nozzle ](../_mineru_assets/ECE R136 Am1/c8e296fd88f9a382e4cfd597bd652fe4f76983f9d3fa9f568b0724b43c9933b8.jpg)  
*Figure 2 Splashing Test Nozzle * (page 31)

