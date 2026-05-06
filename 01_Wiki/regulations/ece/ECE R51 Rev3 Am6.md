---
reg_id: ECE R51 Rev3 Am6
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of motor vehicles having at least
  four wheels with regard to their sound emissions
description: 本文件是联合国第51号法规（关于至少四轮机动车辆噪声排放认证的统一规定）的第3版修订本的第6号修正案。它包含了对法规正文、附件及附录中多项条款的修订，主要涉及车辆参考点定义、符号表、稳定加速条件、测试齿轮比选择、功率质量比计算、静止和行驶车辆噪声测试程序、结果解释以及新增的过渡条款等。
status: active
entry_into_force_date: 2020-09-25
version: Revision 3 - Amendment 6 - Supplement 6 to the 03 series of amendments
source_file: R051r3am6e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\51\R051r3am6e.pdf
publication_date: 2020-11-02
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 中均未明确提及标准机构（如 UNECE/WP.29），但 B 的页眉和脚注暗示了 UNECE 背景。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 中未提及针对新车型的具体实施日期，仅提及生效日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及针对在用车型的具体实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及本修正案替代了哪个具体文件。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A 的摘要中未提取具体的限值数字（如 dB(A) 值），B 中也未提供完整的限值表，无法核对。
_ocr_upgraded: mineru
_mineru_content_hash: 5b33c93348ac10dd
_mineru_outputs_dir: outputs/5b33c93348ac10dd
_mineru_blocks:
  tables: 1
  formulas: 5
  images: 7
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 51 - Revision 3 - Amendment 6

**法规状态**: 本修正案自 **2020年9月25日** 起生效。

**过渡条款**: 根据新增的第11.12条，在本修正案（即Supplement 6）生效之日起的12个月内，**不适用于**对在Supplement 6生效日期之前最初授予的现有批准的扩展。

## 主要修订内容摘要

本修正案对UN R51法规的多个部分进行了修订，主要包括定义、测试程序和数据处理。

### 1. 定义修订
*   **2.11.1. 参考点**: 明确了对于具有多个推进源的车辆，参考点由功率最高的推进源位置决定。若多个推进源功率相当，则以最靠前的推进源位置为准。
*   **2.24. 符号表**: 更新了关于齿轮比 `i`、`i+1`、`i+2`... 以及齿轮比加权因子 `k` 的定义。
*   **2.26. 稳定加速**: 细化了三种“稳定加速”条件的定义，分别适用于低发动机转速条件、M1/N1及M2<3500kg类别车辆（避免因发动机控制应用导致的加速延迟），以及附件7的测试目的（假设在AA'和BB'之间加车长的整个测量距离内加速度恒定）。

### 2. 附件1 附录修订
*   **2.1. 和 2.2. 信息记录**: 修订了车辆噪声测试结果在批准文件中的记录格式要求。

### 3. 附件3 测试程序修订（行驶车辆噪声）
*   **3.1.2.1.1. 功率质量比指数 (PMR)**: 修订了PMR计算公式，并明确对于在测试条件下并行工作的多个推进源，发动机净功率 `P_n` 应为各并行推进发动机功率的算术和。非燃烧发动机的功率以制造商声明的为准。
*   **3.1.2.1.4.1. 使用锁定齿轮比测试的车辆**: 全面修订了手动、自动、自适应或CVT变速箱车辆测试齿轮比的选择逻辑和条件，包括单齿轮测试、双齿轮测试（计算加权因子 `k`）、加速度超过2.0 m/s²时的处理、发动机额定转速超限时的处理，以及无合适齿轮比可用时制造商可采取的措施。
*   **3.1.2.2. 类别 M2>3500kg, M3, N2, N3 车辆**: 修订了测试通过BB'线时的目标发动机转速和车速要求，并强调在AA'和BB'线之间必须确保符合定义2.26.1的稳定加速条件。
*   **3.1.2.2.1.1. 使用锁定齿轮比测试的车辆**: 修订了为满足目标条件而选择齿轮的详细逻辑流程图和条件（a至f）。
*   **3.1.3. 结果解释**: 明确了对于M1、M2≤3500kg和N1类车辆，每次通过的声压级最大值应四舍五入到小数点后第一位。
*   **新增流程图**: 在附录中更新了图4a（总流程图）、图4b（锁定齿轮选择流程图第一部分），并新增了图6（静止噪声测量与数据处理流程图）。

### 4. 附件3 测试程序修订（静止车辆噪声）
*   **3.2.5.3. 排气口附近噪声测量**: 修订了测量位置的规定，特别是当参考点因车辆部件（如备胎、油箱）遮挡而无法接近时，麦克风位置的选择标准（Case 1和Case 2）。
*   **3.2.5.3.2.1. 目标发动机转速**: 修订了目标发动机转速的定义，并规定了无法达到目标转速、发动机转速固定（如串联混合动力）等特殊情况下的处理方式。
*   **3.2.6. 静止车辆噪声结果及 3.2.7. 车型代表值**: 系统修订了单测试点、多测试点、多模式情况下的测量次数、结果有效性判断、平均值计算、取整规则以及最终确定车型代表声压级别的逻辑。

### 5. 附件6 生产一致性修订
*   **2.1.**: 明确了对于M1、N1和M2≤3500kg类车辆，在一致性检查时，可以使用型式批准过程中确定的相同模式、齿轮（比）、齿轮加权因子k和部分功率因子k_p，前提是该信息可从该车型系列适用变体的型式批准测试报告中获得。否则需重新确定。

### 6. 附件7 附加声发射规定 (ASEP) 修订
*   **2.4. 目标条件**: 修订了测试点的定义、稳定加速的验证方法（比较AA'-BB'与PP'-BB'区间的加速度），以及非锁定变速箱条件下发动机转速超限时的处理措施。
*   **2.5.1. 和 2.5.2. 测试程序**: 修订了测试行驶路径、油门操作、预加速使用、非锁定条件下换挡规则，并允许制造商采取措施防止换挡导致不满足边界条件。明确了每个测试点进行单次运行，声压级取左右侧较高值，并四舍五入到小数点后第一位。

**注**: 本文件仅为文档工具。具有真实法律效力的文本是: ECE/TRANS/WP.29/2020/4。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 1 个
> - 公式 5 个
> - 图像 7 个
> - 全文 Markdown 27,884 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 1 个）

#### 表 1 (page 1)
<table><tr><td rowspan=1 colspan=1>gear ratio i</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Annex 3</td><td rowspan=1 colspan=1>3.1.2.1.4.1.</td><td rowspan=1 colspan=1>gear ratio which provides an accelerationwithin the 5 per cent tolerance of thereference acceleration awot_ref or greaterthan the reference acceleration awot_ref</td></tr><tr><td rowspan=1 colspan=1>gear ratio i+1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Annex 3</td><td rowspan=1 colspan=1>3.1.2.1.4.1.</td><td rowspan=1 colspan=1>second of two gear ratios，with anacceleration lower than gear ratio i</td></tr><tr><td rowspan=1 colspan=1>gear ratio i+2, i+3.,...</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Annex 3</td><td rowspan=1 colspan=1>3.1.2.1.4.1.</td><td rowspan=1 colspan=1>gear ratios selectable for the pass-by testof Annex 3,if gear ratio i and gear ratioi+1 exceed an acceleration of 2.0 m/s²</td></tr><tr><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Annex 3</td><td rowspan=1 colspan=1>3.1.2.1.4.1.</td><td rowspan=1 colspan=1>gear ratio weighting factor; value to bereported and used for calculations to thesecond decimal place</td></tr></table>

### 公式（取前 5 个）

**公式 1** (page 2):

$$
\mathrm { k } = ( \mathrm { a _ { w o t r e f } - \mathrm { a _ { w o t ( i + 1 ) } ) / ( \mathrm { a _ { w o t ( i ) } - \mathrm { a _ { w o t ( i + 1 ) } ) } } } }
$$

**公式 2** (page 4):

$$
\left( \mathbf { v _ { t a r g e t \ B B } } , - \mathbf { v _ { B B } } , \mathbf { g e a r i } \right) = \left( \mathbf { v _ { B B } } , \mathbf { g e a r i } + 1 - \mathbf { v _ { t a r g e t \ B B } } , \right)
$$

**公式 3** (page 4):

$$
2 5 \mathrm { k m } \mathrm { / h } \leq \mathrm { v _ { B B } } \mathrm { , } \leq 3 0 \mathrm { k m } \mathrm { / h }
$$

**公式 4** (page 4):

$$
4 0 \mathrm { k m } / \mathrm { h } \leq \mathrm { v } _ { \mathrm { B B } ^ { \prime } \mathrm { y } } \leq 4 5 \mathrm { k m } / \mathrm { h }
$$

**公式 5** (page 4):

$$
\begin{array} { r l } { \mathrm { \mathbf { V } B B ^ { \prime } ~ g e a r ~ i = ~ \mathbf { V } t a r g e t ~ B B } , } & { { } } \\ { \mathrm { \mathbf { I } B B ^ { \prime } ~ g e a r ~ i \le ~ \mathbf { n } _ { t a r g e t ~ B B } , } } \end{array}
$$

### 图像（取前 7 张）

!["Figure 3a ](../_mineru_assets/ECE R51 Rev3 Am6/5a20115594197f656b77d96f9a0997bb0a460a0affdd43a01ae0f583adc43384.jpg)  
*"Figure 3a * (page 7)

![Figure 3b ](../_mineru_assets/ECE R51 Rev3 Am6/8b76633012fcbd33cc7ac0d1b2255354faa37de9c41237480bd269b811064403.jpg)  
*Figure 3b * (page 8)

![Figure 3c ](../_mineru_assets/ECE R51 Rev3 Am6/daf7be698163b6e8a08e205fe1bb468aaf9a1bbb069a33d0edece7057926d57b.jpg)  
*Figure 3c * (page 9)

![Figure 3d ](../_mineru_assets/ECE R51 Rev3 Am6/8b0f1c0faed0f5e5d8c56be81f8cff617a1a95bceca0f0b3332b31f8fbfc4519.jpg)  
*Figure 3d * (page 10)

![图 page 11](../_mineru_assets/ECE R51 Rev3 Am6/8cbd5200a7d8ced0de1678c223fe99cdfa1b63fdce64e99f1899fc536f3ce408.jpg)  

![图 page 12](../_mineru_assets/ECE R51 Rev3 Am6/f1c5d8ee49f88ab89643072d4e10cfd09a126d3ed1eb6a52caeba708aac7c970.jpg)  

!["Figure 6 Flowchart for measurement and data processing of stationary sound according to Puiug-up" v.-. ](../_mineru_assets/ECE R51 Rev3 Am6/9cd4c7117ce3f8549b9377a2ee5788b07e428ecc4087bad407e63f07a4798a07.jpg)  
*"Figure 6 Flowchart for measurement and data processing of stationary sound according to Puiug-up" v.-. * (page 13)

