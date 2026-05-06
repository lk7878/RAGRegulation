---
reg_id: ECE R109 Rev1 Am4
region: ece
type: type/amendment
title: Addendum 108 – UN Regulation No. 109 Revision 1 - Amendment 4
subject: Uniform provisions concerning the approval for the production of retreaded
  pneumatic tyres for commercial vehicles and their trailers
standard_body: UNECE
publication_date: 2021-02-02
implementation_date_new_vehicle: 2021-01-03
source_file: R109r1am4e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\109\R109r1am4e.pdf
status: active
verified_by: deepseek-v3
cross_check_overall_confidence: medium
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: implementation_date_new_vehicle
  status: mismatch
  extracted: 2021-01-03
  original: 3 January 2021
  note: 日期一致，但字段名含义可能不匹配。B 中为“Date of entry into force”（生效日期），A 中字段名为“implementation_date_new_vehicle”（新车型实施日期），但值相同。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中也未提及。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中也未提及。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中也未提及。
_ocr_upgraded: mineru
_mineru_content_hash: 25474a08b70373c7
_mineru_outputs_dir: outputs/25474a08b70373c7
_mineru_blocks:
  tables: 6
  formulas: 9
  images: 0
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 109 Revision 1 - Amendment 4

## 法规信息
*   **法规编号**: UN R109r1am4e
*   **发布机构**: 联合国欧洲经济委员会 (UNECE)
*   **发布日期**: 2021年2月2日
*   **生效日期**: 2021年1月3日
*   **法规类型**: 修正案 (Amendment)
*   **主题**: 关于商用车及其挂车翻新充气轮胎生产认证的统一规定

## 修正内容摘要
本修正案对UN R109法规（商用车及其挂车翻新充气轮胎）进行了修订，主要涉及雪地轮胎在严重积雪条件下的性能要求和测试方法。

### 主要修订条款：
1.  **第2.47条 (定义 - 标准参考测试轮胎 SRTT)**: 更新了SRTT的定义，明确了其依据的美国材料与试验协会 (ASTM) 标准及对应的轮胎规格：
    *   E1136-17 (P195/75R14, SRTT14)
    *   F2872-16 (225/75 R 16 C, SRTT16C)
    *   F2871-16 (245/70R19.5, SRTT19.5)
    *   F2870-16 (315/70R22.5, SRTT22.5)

2.  **第4.3条 (样品提交)**: 修订了翻新轮胎制造商应认证机构要求提交测试样品或测试报告副本的规定。

3.  **第7.2条 (严重积雪条件用雪地轮胎分类)**: 明确了翻新轮胎要归类为“严重积雪条件用雪地轮胎”，必须满足第7.2.1条的雪地抓着性能要求。性能通过附录10的测试方法评估，将候选轮胎与标准参考测试轮胎 (SRTT) 在制动、牵引或加速测试中的表现进行对比，结果以雪地抓着指数表示。

4.  **第7.2.1条 (雪地抓着指数最低要求)**: 规定了C2和C3类轮胎相对于相应SRTT的最低雪地抓着指数值。
    *   **C2类轮胎**:
 *   制动法 (参考SRTT16C): ≥ 1.02
 *   牵引法 (参考SRTT14): ≥ 1.10
 *   加速法: 不适用
    *   **C3类轮胎**:
 *   制动法: 不适用
 *   牵引法: 不适用
 *   加速法 (参考SRTT19.5或SRTT22.5): ≥ 1.25

5.  **附录10 (雪地抓着性能测试方法)**:
    *   **第3.2.1条 (ABS制动测试程序)**: 详细规定了ABS制动测试的重复次数（至少6次）、测试轨迹要求（避免重叠）以及测试路面重新处理的条件。
    *   **第3.4.1.1条 (数据处理 - 算术平均值与标准差)**: 规定了计算平均完全制动减速度 (mfdd) 的算术平均值、修正样本标准差和变异系数 (CV) 的公式。
    *   **第3.4.1.2条 (加权平均值计算)**: 规定了根据候选轮胎测试顺序计算SRTT加权平均值 (wa_SRTT) 的方法。
    *   **第3.4.1.3条 (雪地抓着指数计算)**: 规定了候选轮胎雪地抓着指数 (SG) 的计算公式：SG(Tn) = (候选轮胎Tn的mfdd算术平均值) / (适用的SRTT加权平均值)。
    *   **第3.4.2条 (统计验证)**: 要求检查测试数据的正态性、漂移和异常值，并验证SRTT连续测试结果的一致性。引入了验证系数 (CVal) 的概念，要求CVal(SRTT) 差异不超过5%，且任何制动测试的变异系数 (CVa) 应小于6%。
    *   **第4.1条**: 已省略。
    *   **第4.2条 (雪地抓着指数测量方法)**: 明确了C3类轮胎的雪地性能基于加速测试，其平均加速度相对于SRTT19.5或SRTT22.5至少应为1.25倍。
    *   **第4.7条 (C3类轮胎雪地加速测试程序)**: 标题修订。
    *   **第4.7.5.4条 (加速测试重复与变异系数)**: 规定加速测试至少重复6次，且平均加速度的变异系数 (CV_AA) 应≤6%。
    *   **第4.8.2条 (结果验证)**: 规定了候选轮胎和参考轮胎测试结果的验证标准（CV_AA ≤ 6%， CVal_AA(SRTT) ≤ 6%），不满足条件需重新测试。
    *   **第4.8.3条 (加权平均值计算 - 加速法)**: 通过表格详细列出了不同测试顺序（R-T1-R, R-T1-T2-R, R-T1-T2-T3-R）下，用于计算各候选轮胎雪地抓着指数的SRTT加权平均值公式。
    *   **第4.8.4条**: 删除。
    *   **第4.8.5条 (重编号为4.8.4，雪地抓着指数计算)**: 规定了基于加速测试的雪地抓着指数计算公式：SG(Tn) = (候选轮胎Tn的平均加速度算术平均值) / (适用的SRTT加权平均值)。
    *   **第4.8.6条**: 重编号为4.8.5。
    *   **第4.9.2条 (使用控制轮胎和两台车辆的方法原理)**: 描述了使用控制轮胎和两台不同车辆评估候选轮胎相对于参考轮胎性能的方法原理。最终雪地抓着指数为两次比较结果的乘积 (SG1 × SG2)。

6.  **附录2和附录3 (测试报告模板)**:
    *   更新了报告格式，增加了雪地抓着指数相关信息的填写要求。
    *   修订了测试数据表格，以包含SRTT和候选轮胎的详细信息及测试结果（如平均完全制动减速度、标准差、变异系数、验证系数、加权平均值和雪地抓着指数）。
    *   增加了关于C2类轮胎充气压力和负载的脚注说明。

## 备注
*   本文件仅为记录工具。具有真实法律效力的文本是: ECE/TRANS/WP.29/2020/74。
*   本修正案是UN R109法规第1修订版 (Revision 1) 的第4次修正 (Amendment 4)。
*   主要技术修订聚焦于雪地抓着性能的测试方法、数据分析和最低要求，特别是引入了更详细的统计验证程序和针对C3类轮胎的加速测试方法。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 6 个
> - 公式 9 个
> - 图像 0 个
> - 全文 Markdown 24,895 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 6 个）

#### 表 1 (page 1)
<table><tr><td rowspan=1 colspan=1>Classoftyre</td><td rowspan=1 colspan=1>Snow grip index(brake on snow method) (a)</td><td rowspan=1 colspan=1>Snow grip index(spin traction method) (b)</td><td rowspan=1 colspan=1>Snow grip index(acceleration method) (c)</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Ref. = SRTT16C</td><td rowspan=1 colspan=1>Ref. = SRTT14</td><td rowspan=1 colspan=1>Ref.= SRTT19.5, SRTT22.5</td></tr><tr><td rowspan=1 colspan=1>C2</td><td rowspan=1 colspan=1>1.02</td><td rowspan=1 colspan=1>1.10</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>C3</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>1.25</td></tr></table>

#### 表 2 (page 4)
**Table 1 **

<table><tr><td rowspan=1 colspan=1>If the number ofsets of candidatetyres between two successive runsof thereference tyre is:</td><td rowspan=1 colspan=1>and theset ofcandidatetyres to be qualified is:</td><td rowspan=1 colspan=1>then&quot;wasrrr is calculated by applyingthe following:</td></tr><tr><td rowspan=1 colspan=1>1|R-T1-R</td><td rowspan=1 colspan=1>T1</td><td rowspan=1 colspan=1>WasRTT =（AAR1+AAR2）</td></tr><tr><td rowspan=1 colspan=1>2|R-T1-T2-R</td><td rowspan=1 colspan=1>T1T2</td><td rowspan=1 colspan=1>WasRTT =AAR1+AAR233WasRTT =AAR1+AAR223</td></tr><tr><td rowspan=1 colspan=1>3|R-T1-T2-T3-R</td><td rowspan=1 colspan=1>T1T2T3</td><td rowspan=1 colspan=1>WasRTT  AAR1+AAR244WasRTT =（AAR1+AAR2）2AAR1 AAR2WasRTT+44</td></tr></table>

#### 表 3 (page 5)
**Part 2 - Test data **

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SRTT(1&#x27; test)</td><td rowspan=1 colspan=1>Candidate 1</td><td rowspan=1 colspan=1>Candidate 2</td><td rowspan=1 colspan=1>SRTT (2nd test)</td></tr><tr><td rowspan=1 colspan=1>Brand name</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Trade Description/commercial name</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre sizedesignation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Service description</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Test rim width code</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Reference (test) inflationpressure(） (kPa)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre loads F/R (kg)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre LoadsF/R(% of load associated to LI(2))</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre pressure F/R(kPa)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 4 (page 6)
<table><tr><td rowspan=1 colspan=1>Run number</td><td rowspan=1 colspan=1>Specification</td><td rowspan=1 colspan=1>SRTT (lst test)</td><td rowspan=1 colspan=1>Candidate 1</td><td rowspan=1 colspan=1>Candidate 2</td><td rowspan=1 colspan=1>SRTT (2nd test)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mean</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Standard deviation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Coefficient of variation</td><td rowspan=1 colspan=1>CVa ≤6%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Coefficient of Validation</td><td rowspan=1 colspan=1>CVala(SRTT)≤5%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SRTT weighted average</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Snow grip index</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 5 (page 7)
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SRTT(1 test)</td><td rowspan=1 colspan=1>Candidate 1</td><td rowspan=1 colspan=1>Candidate 2</td><td rowspan=1 colspan=1>Candidate 3</td><td rowspan=1 colspan=1>SRTT (2nd test)</td></tr><tr><td rowspan=1 colspan=1>Brand name</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Trade Description/commercial name</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre sizedesignation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Service description</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Test rim width code</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Reference (test) inflationpressure(1） (kPa)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre loads F/R (kg)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre Loads F/R(% of load associated to LI(2))</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Tyre pressure F/R(kPa)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 6 (page 8)
<table><tr><td rowspan=1 colspan=1>Run number</td><td rowspan=1 colspan=1>Specification</td><td rowspan=1 colspan=1>SRTT(lst test)</td><td rowspan=1 colspan=1>Candidate1</td><td rowspan=1 colspan=1>Candidate 2</td><td rowspan=1 colspan=1>Candidate 3</td><td rowspan=1 colspan=1> SRTT (2nd test)</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Mean</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Standard deviation</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Coefficient of variation</td><td rowspan=1 colspan=1>CVa≤6%</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Coefficient of Validation</td><td rowspan=1 colspan=1>CVala(SRTT)≤6%</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SRTT weighted average</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Snow grip index</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

### 公式（取前 9 个）

**公式 1** (page 2):

$$
C V _ { a } = 1 0 0 \% \cdot \frac { \sigma _ { a } } { \bar { a } }
$$

**公式 2** (page 2):

$$
\sigma _ { a } = \sqrt { \frac { 1 } { N - 1 } \sum _ { i = 1 } ^ { N } ( a _ { i } - \bar { a } ) ^ { 2 } }
$$

**公式 3** (page 2):

$$
w a _ { \mathrm { S R T T } } = \textstyle { \frac { 1 } { 2 } } ( \overline { { a _ { R 1 } } } + \overline { { a _ { R 2 } } } )
$$

**公式 4** (page 2):

$$
S G ( \mathrm { T n } ) = \frac { \overline { { a _ { \mathrm { T n } } } } } { w a _ { \mathrm { S R T T } } }
$$

**公式 5** (page 3):

$$
C V a l _ { a } ( \mathrm { S R T T } ) = 1 0 0 \% \ \times \ \bigg | \frac { \overrightarrow { a _ { R 2 } } - \overrightarrow { a _ { R 1 } } } { \overrightarrow { a _ { R 1 } } } \bigg |
$$

**公式 6** (page 3):

$$
C V _ { A A } = 1 0 0 \% \cdot \frac { \sigma _ { A A } } { A A }
$$

**公式 7** (page 4):

$$
C V a l _ { A A } ( \mathrm { S R T T } ) = 1 0 0 \% \times \left| \frac { \overline { { A A _ { 2 } } } - \overline { { A A _ { 1 } } } } { \overline { { A A _ { 1 } } } } \right|
$$

**公式 8** (page 4):

$$
S G ( \mathrm { T n } ) = \frac { \overline { { A A _ { \mathrm { T n } } } } } { w a _ { \mathrm { S R T T } } }
$$

**公式 9** (page 5):

$$
\mathrm { S n o w \ G r i p \ I n d e x = S G 1 \times S G 2 " }
$$

