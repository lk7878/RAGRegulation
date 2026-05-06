---
reg_id: ECE R159 Am1
type: type/amendment
region: ece
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Moving Off Information System for the Detection of Pedestrians and Cyclists
status: active
publication_date: 2022-09-23
implementation_date_new_vehicle: 2022-06-22
source_file: 国外法规\ECE标准\标准法规-UNECE\121~160\159\R159am1e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\159\R159am1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 中未提取 standard_body 字段，B 中未明确提及。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 中未提取该字段，B 中未提及。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 中未提取该字段，B 中未提及。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A 中未提取该字段，B 中未提及。
_ocr_upgraded: mineru
_mineru_content_hash: a71dc1c4b6e123bb
_mineru_outputs_dir: outputs/a71dc1c4b6e123bb
_mineru_blocks:
  tables: 1
  formulas: 0
  images: 1
_mineru_merged_at: '2026-04-22'
---

### 修订内容摘要
本修正案对联合国法规UN R159的特定条款进行了修改。

#### 1. 条款修订
- **5.2.2.3.3. 转向操作时的检测策略**:
    - 在执行转向操作时，可调整起步信息系统的检测策略。不要求根据转向角调整传感器。
    - 检测调整策略应在第6.1条所述信息中予以说明。
    - 技术服务机构可根据该策略验证系统操作。

- **5.5.1. 系统初始化**:
    - 如果起步信息系统在车速高于0 km/h的累计行驶时间达到15秒后仍未初始化，应向驾驶员指示此状态信息。
    - 该信息应持续存在，直至系统成功初始化。

- **5.8.3. 故障警告信号激活**:
    - 起步信息系统的故障警告信号应随车辆主控制开关的激活而激活。
    - 此要求不适用于在共用空间显示的故障警告信号。

- **6.4.1. 静态检查**:
    - 车辆静止时，检查光学故障警告信号是否符合上述第5.8条的要求。

#### 2. 附录修订
- **附录1，图1 - 静态穿越测试布置图**:
    - 提供了测试布置的示意图，定义了车辆平面、分离平面等关键尺寸和参考点。
    - 关键定义包括：
 - `d_w`: 车辆宽度。
 - `d_NSP`: 近侧车辆平面到近侧分离平面的距离，定义为0.5米。
 - `d_OSP`: 远侧车辆平面到远侧分离平面的距离，定义为0.5米。
 - `d_TC`: 每个测试用例的前向分离距离。
 - `d_FSP`: 车辆前端到最大前向分离平面的距离。

#### 3. 新增测试用例表
- **表1 - 静态穿越测试用例**:
    - 详细列出了6个测试用例，涵盖儿童行人、成人行人和成人骑行者。
    - 每个用例规定了测试距离(`d_TC`)、穿越方向（近侧/远侧）、软目标速度(`v`)以及到信息最后点(`LPI`)的距离(`d_LPI`)。
    - 关键定义包括 `d_LPI`：与信息最后点相关的距离。

| 测试用例 | 软目标 (T) | 测试用例距离 (`d_TC`) /m | 穿越方向 (c) | 软目标速度 (v) /km/h | 到信息最后点的距离 (`d_LPI`) /m |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 儿童行人 | 0.8 | 近侧 | 3 | `d_NSP` |
| 2 | 成人行人 | `d_FSP` | 近侧 | 3 | `d_NSP` |
| 3 | 成人骑行者 | 0.8 | 远侧 | 3 | `d_OSP` |
| 4 | 成人骑行者 | `d_FSP` | 近侧 | 5 | `d_NSP` |
| 5 | 成人行人 | 0.8 | 远侧 | 5 | `d_OSP` |
| 6 | 儿童行人 | `d_FSP` | 远侧 | 5 | `d_OSP` |
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 1 个
> - 公式 0 个
> - 图像 1 个
> - 全文 Markdown 4,875 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 1 个）

#### 表 1 (page 2)
**Table 1 Test Cases for Static Crossing Tests **

<table><tr><td rowspan=1 colspan=1>TestCase</td><td rowspan=1 colspan=1>Soft Target (T)</td><td rowspan=1 colspan=1>Test Case Distance(drc)/m</td><td rowspan=1 colspan=1>CrossingDirection (c)</td><td rowspan=1 colspan=1>Soft Target Speed (v)/km/h</td><td rowspan=1 colspan=1>Distance to Last Point ofInformation (dLP1) /m</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Child Pedestrian</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>Nearside</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>dNsP</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Adult Pedestrian</td><td rowspan=1 colspan=1>dFsP</td><td rowspan=1 colspan=1>Nearside</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>dNsP</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Adult Cyclist</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>Offside</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>dosp</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Adult Cyclist</td><td rowspan=1 colspan=1>dFsp</td><td rowspan=1 colspan=1>Nearside</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>dNsP</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Adult Pedestrian</td><td rowspan=1 colspan=1>0.8</td><td rowspan=1 colspan=1>Offside</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>dosp</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Child Pedestrian</td><td rowspan=1 colspan=1>dFsp</td><td rowspan=1 colspan=1>Offside</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>dosp</td></tr></table>

### 图像（取前 1 张）

![Figure 1 Set Up for Static Crossing Tests ](../_mineru_assets/ECE R159 Am1/8efdddcb5a532bdbcfa9f27964690ef9de1210bb91354e318f14c9afefa23f9e.jpg)  
*Figure 1 Set Up for Static Crossing Tests * (page 1)

