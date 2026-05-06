---
reg_id: ECE R115 Rev1 Am3
region: ece
title: Addendum 114 – UN Regulation No. 115 Revision 1 - Amendment 3
type: type/amendment
status: active
publication_date: '2020-01-20'
implementation_date_new_vehicle: '2020-01-11'
authority: UNECE
source: E/ECE/324/Rev.2/Add.114/Rev.1/Amend.3, E/ECE/TRANS/505/Rev.2/Add.114/Rev.1/Amend.3
source_url: https://unece.org/transport/documents/2020/01/standards/ece324rev2add114rev1amend3
summary: 对UN R115第1修订版第3次修正案，主要涉及LPG和CNG改装系统的排放测试要求，引入了WLTC测试循环，并更新了与UN R83、UN R101、UN
  GTR No. 15等法规的引用关系。
keywords:
- LPG
- CNG
- retrofit
- emissions
- NEDC
- WLTC
- UN R83
- UN R101
- UN GTR No.15
- UN R49
references:
- UN R83
- UN R101
- UN GTR No.15
- UN R49
- UN R85
- Directive 98/69/EC
- Directive 1999/96/EC
amend_target: UN R115r1
amend_type: partial
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\115\R115r1am3e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 中未明确提取此字段，B 中未直接提及“standard_body”。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: '2020-01-11'
  original: null
  note: '[Auto-reclassified] Insufficient evidence (was mismatch with null): ''2020-01-11''
    vs ''None'''
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及针对在用车型的单独生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及本修正案替代了哪个文件。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A 的概述中未提取具体限值数字，B 中主要描述测试程序和引用，未明确列出限值。
stage2_reclassified:
- implementation_date_new_vehicle
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-23'
_mineru_outputs_dir: outputs\ea5ffd0bd139284a
---

# UN Regulation No. 115 Revision 1 - Amendment 3

## 概述
本文件是《关于采用轮式车辆、其装备和部件的统一技术规定以及基于这些规定授予批准的互认条件的协定》下，UN法规第115号（关于LPG和CNG改装系统批准的统一规定）第1修订版的第3次修正案。本修正案自2020年1月11日起生效。

## 主要修订内容

### 1. 定义更新
- 新增定义：
    - **2.8. "NEDC"**: 指UN法规第83号（截至07系列修正案）中描述的用于验证冷启动后排气污染物的测试循环。
    - **2.9. "WLTC"**: 指UN全球技术法规第15号（UN GTR No. 15）中描述的用于验证冷启动后排气污染物的全球统一轻型车辆测试循环。

### 2. LPG改装系统测试要求 (第6.1.2节)
- **6.1.2.1.**: 更新了测试程序引用，明确LPG改装系统样品应按照UN法规第83号、第101号，或UN GTR第15号，或UN法规第49号（如适用）中描述的程序进行测试，并需进行最大功率对比测试（依据UN法规第85号或本法规6.1.3.）。
- **6.1.2.4.1.1.**: 更新了尾气排放测量要求，明确CO、HC、NOx的排放计算应依据UN法规第83号或UN GTR第15号（如适用）。
- **6.1.2.4.1.3. (排气排放测试 - 汽油模式)**: 明确测试循环（NEDC或WLTC）应根据车辆的初始型式批准来选择。装备改装系统的母车应符合原车型式批准的限值（包括原车型式批准时应用的劣化系数）。
- **6.1.2.4.1.4. (NEDC测试循环特定要求)**: 规定在满足6.1.2.4.1.4.2.要求的前提下，应使用基准汽油进行三次测试。
- **新增 6.1.2.4.1.5. (WLTC测试循环特定规定)**: 规定在满足6.1.2.4.1.5.1要求的前提下，应使用基准汽油进行两次测试。如果第一次测试中每种受限制污染物的结果小于或等于限值的0.9倍，测试次数可减少为一次。
- **6.1.2.4.1.6. (排气排放测试 - LPG模式)**: 更新了测试循环选择原则（同汽油模式）。根据车辆符合的法规系列（如UN R83 05系列、UN R49 04系列等），对测试中使用汽油的最长时间（90秒或60秒）做出了规定。对于采用WLTC循环批准的车辆，此时间段应预先设定且驾驶员不可更改。
- **6.1.2.4.1.7. (NEDC测试循环特定规定 - LPG模式)**: 规定在满足6.1.2.4.1.7.2要求的前提下，应使用每种基准LPG进行三次测试。允许三次结果中的一次超过限值不超过10%，但三次结果的算术平均值需低于限值。
- **新增 6.1.2.4.1.8. (WLTC测试循环特定规定 - LPG模式)**: 规定在满足6.1.2.4.1.8.1要求的前提下，应使用每种基准LPG进行两次测试。如果第一次测试中每种污染物或两种污染物的组合排放结果小于或等于限值的0.9倍，测试次数可减少为一次。
- **6.1.2.4.3.1.**: 更新了CO2排放计算依据，明确应根据UN法规第101号或UN GTR第15号（如适用）进行计算。

### 3. CNG改装系统测试要求 (第6.2.2节)
- 对CNG改装系统的测试要求进行了与LPG系统平行的修订，包括：
    - **6.2.2.1.**: 更新测试程序引用（同LPG部分）。
    - **6.2.2.4.1.1.**: 更新尾气排放测量要求（同LPG部分）。
    - **6.2.2.4.1.3., 6.2.2.4.1.4., 新增 6.2.2.4.1.5.**: 汽油模式测试的NEDC和WLTC循环规定（同LPG部分）。
    - **6.2.2.4.1.6.**: CNG模式测试的循环选择和使用汽油时间限制（同LPG部分）。
    - **6.2.2.4.1.7., 新增 6.2.2.4.1.8.**: CNG模式测试的NEDC和WLTC循环特定规定（同LPG部分）。
    - **6.2.2.4.3.1.**: 更新CO2排放计算依据（同LPG部分）。

### 4. 附录修订
- **附录2A (LPG能量比计算)**: 第2段更新了燃料消耗量(FC_norm)的计算依据，明确应根据UN法规第101号附录6第1.4.3.(b)段或UN GTR第15号附录7第6段（如适用）计算。如适用，计算FC_norm所用公式中的修正因子cf应使用气体燃料的H/C比计算。
- **附录2B (CNG能量比计算)**: 第2段更新了燃料消耗量(FC_norm)的计算依据，明确应根据UN法规第101号附录6第1.4.3.(c)段或UN GTR第15号附录7第6段（如适用）计算。

## 备注
- 本文件仅为文档工具。具有真实性和法律约束力的文本是：ECE/TRANS/WP.29/2019/45。
- 本修正案整合了截至2017年9月14日生效的修订。
