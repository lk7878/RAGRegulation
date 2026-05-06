---
reg_id: ECE R83 Rev5 Am15
region: ece
type: type/amendment
title: Addendum 82 – UN Regulation No. 83 Revision 5 - Amendment 15
short_title: UN R83r5am15
description: Amendment 15 to Revision 5 of UN Regulation No. 83, concerning the approval
  of vehicles with regard to the emission of pollutants according to engine fuel requirements.
standard_body: UNECE
publication_date: 2023-06-20
implementation_date_new_vehicle: 2023-06-05
status: active
source_file: 国外法规\ECE标准\标准法规-UNECE\81~120\83\R083r5am15e.pdf
source_page: unknown
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\81~120\83\R083r5am15e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
reg_id_conf: low
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: reg_id
  status: normalized
  extracted: ECE R83 Rev5 Am15
  original: Addendum 82 – UN Regulation No. 83 Revision 5 - Amendment 15
  note: '[Auto-reclassified] Same reg_id after normalization (was: ''ECE R83 Rev5
    Am15'' vs ''Addendum 82 – UN Regulation No. 83 Revision 5 - Amendment 15'')'
- field: implementation_date_new_vehicle
  status: normalized
  extracted: 2023-06-05
  original: 5 June 2023
  note: '[Auto-reclassified] Same date after parsing: 2023-06-05 == 5 June 2023'
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B中未提及在用车辆的单独实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B中未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B中未提及替代关系。
stage2_reclassified:
- implementation_date_new_vehicle
- reg_id
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: 3a7a12d9e1072d5e
_mineru_outputs_dir: outputs/3a7a12d9e1072d5e
_mineru_blocks:
  tables: 1
  formulas: 1
  images: 0
_mineru_merged_at: '2026-04-22'
---

# UN Regulation No. 83 Revision 5 - Amendment 15

**Supplement 15 to the 07 series of amendments – Date of entry into force: 5 June 2023**

Uniform provisions concerning the approval of vehicles with regard to the emission of pollutants according to engine fuel requirements.

*This document is meant purely as documentation tool. The authentic and legal binding text is: ECE/TRANS/WP.29/2022/136.*

## 主要修订内容

### 1. 第9.3.5.1段修订
修订内容涉及应用统计程序（即针对尾气排放）时，样本批次数量应根据在适用本法规的缔约方销售的车辆年度生产量确定，具体见下表：

**表4 样本量**
| 生产量（每年，针对尾气排放测试） | 样本批次数量 |
| :--- | :--- |
| 不超过 100,000 辆 | 1 |
| 100,001 至 200,000 辆 | 2 |
| 超过 200,000 辆 | 3 |

### 2. 新增第9.3.5.3段
新增内容规定，如果上一个日历年，在适用本法规的缔约方销售的车辆年度生产量少于5,000辆，则I型测试（即尾气排放）的在用符合性检查不是强制性的。

### 3. 附录2第6段修订
修订了用于计算连续测试统计值的递归公式。

### 4. 附件2第2.4段修订
修订了烟雾不透明度测试结果的相关要求，并注明烟雾不透明度值应根据UN法规No. 24的规定。

### 5. 附件4a、附录1、2、3、4、5、6及附件7、附录1的修订
统一增加了关于测试和测量设备的条款：
- 对于符合UN法规No. 154原始系列或后续版本技术要求的设备，可以遵循UN法规No. 154中描述的技术设备要求。
- 在所有其他情况下，应适用本法规中的要求。

### 6. 附件11第3.2.1.2段修订
修订了关于OBD监控器在特定条件下（如低温、高海拔）停用的规定，并明确了在再生期间若OBD阈值被超过但无缺陷存在时，无需点亮故障指示灯(MI)。

### 7. 附件11附录1第6.5.3.2段修订
修订了用于传输OBD相关信息的标准清单，新增了可选标准：
- (e) ISO 27145 (2012-08-15)
- (f) SAE J 1979-2 (2021年4月)
标准(e)或(f)可作为选项替代标准(a)。
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 1 个
> - 公式 1 个
> - 图像 0 个
> - 全文 Markdown 8,638 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 1 个）

#### 表 1 (page 1)
**Table 4 Sample size **

<table><tr><td rowspan=1 colspan=1>Production Volume- per calendar year (for tailpipe emission tests),- of vehicles ofan OBD family with IUPR in thesampling period</td><td rowspan=1 colspan=1>Number of sample lots</td></tr><tr><td rowspan=1 colspan=1>Up to 100,000</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>100,001 to 200,000</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>Above 200,000</td><td rowspan=1 colspan=1>3</td></tr></table>

### 公式（取前 1 个）

**公式 1** (page 1):

$$
\begin{array} { l } { \displaystyle \bar { d } _ { n } = \left( 1 - \frac 1 n \right) \bar { d } _ { n - 1 } + \frac 1 n d _ { n } } \\ { \displaystyle V _ { n } ^ { 2 } = \left( 1 - \frac 1 n \right) V _ { n - 1 } ^ { 2 } + \frac { \left( \bar { d } _ { n } - d _ { n } \right) ^ { 2 } } { n - 1 } } \\ { \displaystyle \left( n = 2 , 3 , \ldots ; \bar { d } _ { 1 } = d _ { 1 } ; V _ { 1 } = 0 \right) } \end{array}
$$

