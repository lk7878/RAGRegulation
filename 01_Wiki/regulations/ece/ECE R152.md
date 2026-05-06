---
reg_id: ECE R152
region: ece
type: type/version
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles
status: active
publication_date: '2020-01-22'
implementation_date_new_vehicle: 2020-01-22
authority: UNECE
source: E/ECE/TRANS/505/Rev.3/Add.151
source_url: null
topics:
- Advanced Emergency Braking System (AEBS)
- Vehicle Safety
- Active Safety
- Braking Systems
- Pedestrian Protection
vehicle_categories:
- M1
- N1
compliance: type_approval
related_regulations:
- UN R13
- UN R13-H
- UN R10
- UN R121
- ISO 19206-1:2018
- ISO 19206-2:2018
tags:
- type/version
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\152\R152e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
title_conf: low
cross_check_flags:
- field: title
  status: mismatch
  extracted: Uniform provisions concerning the approval of motor vehicles with regard
    to the Advanced Emergency Braking System (AEBS) for M1 and N1 vehicles
  original: Uniform provisions concerning the approval of motor vehicles with regard
    to the Advanced Emergency Braking System (AEBS) for M and N vehicles
  note: A 中为 "M1 and N1"，B 中为 "M and N"，不一致。B 的脚注1说明 M1 和 N1 的定义，但标题本身未写数字。
  recheck_verdict: confirmed_mismatch
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及 standard_body 字段。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及针对在用车的实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未提及替代法规。
_low_conf_recheck_source: stage3_llm_opus
_low_conf_recheck_verdict: upgrade
_low_conf_recheck_reason: body内容覆盖法规核心条款较为完整，包括适用范围、主要定义、技术要求、测试程序、批准标识等结构清晰。标题中明确注明M1和N1车辆，生效日期有文字支撑。但publication_date现值2020-02-04与body所载生效日期（2020年1月22日）存在差异，且文件说明其为文档工具版而非原始法律文本，细节确定性略有不足，升至medium为宜。
_ocr_upgraded: mineru
_mineru_content_hash: 1f4152af0b946d39
_mineru_outputs_dir: outputs/1f4152af0b946d39
_mineru_blocks:
  tables: 4
  formulas: 0
  images: 2
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 152 - Advanced Emergency Braking System (AEBS) for M1 and N1 Vehicles

## 法规概述
本法规为M1和N1类车辆的高级紧急制动系统（AEBS）制定了统一规定。该系统旨在自动检测潜在的前向碰撞，向驾驶员提供适当警告，并在驾驶员未对警告作出反应时激活车辆制动系统，以减速车辆，从而避免或减轻碰撞的严重性。

## 适用范围
本法规适用于M1和N1类车辆，针对其车载系统在以下方面的批准：
(a) 避免或减轻与同车道内乘用车的追尾碰撞严重性；
(b) 避免或减轻与行人碰撞的严重性。

## 主要定义
- **高级紧急制动系统 (AEBS)**: 可自动检测即将发生的前向碰撞并激活车辆制动系统以使车辆减速，旨在避免或减轻碰撞的系统。
- **紧急制动**: AEBS向车辆行车制动系统发出的制动请求。
- **碰撞警告**: 当AEBS检测到潜在前向碰撞时向驾驶员发出的警告。
- **车辆类型（关于其AEBS）**: 在AEBS性能显著影响的车辆特征、以及AEBS的类型和设计等基本方面无差异的车辆类别。
- **时间到碰撞 (TTC)**: 在任何时刻，主车与目标之间的纵向距离除以主车与目标的纵向相对速度所得的时间值。
- **干路面**: 标称峰值制动系数为0.9的路面。

## 技术要求摘要

### 一般要求
- AEBS的有效性不得受磁场或电场的不利影响（需符合UN R10要求）。
- 电子控制系统的安全方面需符合本法规附件3的要求。
- 系统需提供故障警告、手动停用警告等。
- 系统设计应尽量减少碰撞警告信号的产生，并避免在驾驶员不会识别即将发生碰撞的情况下进行自主制动。

### 车对车场景要求
- **碰撞警告**: 当可以预见到与同车道前车（M1类）发生碰撞，且相对速度高于主车能够避免碰撞的速度时，应在紧急制动开始前至少0.8秒发出碰撞警告。
- **紧急制动**: 当系统检测到即将发生碰撞的可能性时，应向车辆行车制动系统发出至少5.0 m/s²的制动请求。
- **速度范围**: 系统至少在10 km/h至60 km/h的车速范围内激活。
- **减速性能**: 系统需能在特定条件下（干路面、满载/空载等）达到法规中表格规定的最大相对碰撞速度要求（针对静止和移动目标）。

### 车对行人场景要求
- **碰撞警告**: 当AEBS检测到可能与以5 km/h恒定速度横穿道路的行人发生碰撞时，应提供碰撞警告，且不晚于紧急制动干预开始。
- **紧急制动**: 当系统检测到即将发生碰撞的可能性时，应向车辆行车制动系统发出至少5.0 m/s²的制动请求。
- **速度范围**: 系统至少在20 km/h至60 km/h的车速范围内激活。
- **减速性能**: 系统需能在特定条件下（干路面、满载/空载、环境照度至少2000 Lux等）达到法规中表格规定的最大碰撞速度要求（针对横穿行人）。

### 驾驶员干预
- AEBS应提供驾驶员中断碰撞警告和紧急制动的手段。
- 中断可由任何表明驾驶员意识到紧急情况的积极动作（如急踩油门、操作转向指示灯控制）启动。

### 手动停用
- 如果车辆配备了手动停用AEBS功能的方法，则AEBS功能应在每次新的点火循环开始时自动恢复。
- 手动停用控制的设计应使得停用至少需要两个刻意动作。
- 不得在车速高于10 km/h时停用AEBS。

### 警告指示
- 碰撞警告应通过至少两种模式（声学、触觉或光学）提供。
- 故障警告应为恒定的黄色光学警告信号。

## 测试程序摘要
- **测试条件**: 平坦、干燥的混凝土或沥青路面，标称峰值制动系数为0.9。环境温度0°C至45°C。车对车场景环境照度至少1000 Lux，车对行人场景至少2000 Lux。
- **车辆条件**: 至少在空载和满载条件下测试。
- **测试目标**:
    - 车辆检测测试：使用M1类量产轿车或符合ISO 19206-1:2018的“软目标”。
    - 行人检测测试：使用符合ISO 19206-2:2018的“软目标”。
- **具体测试**:
    - 对静止车辆目标的警告和激活测试（车速：20、42、60 km/h等）。
    - 对移动车辆目标的警告和激活测试（主车车速：30、60 km/h；目标车速：20 km/h）。
    - 对行人目标的警告和激活测试（使用6岁儿童行人软目标，车速：20、30、60 km/h等）。
    - 故障检测测试。
    - 停用测试（如适用）。

## 批准与标识
- 批准的车辆应附有符合附件2模型的国际批准标记，包括圆圈内字母"E"、批准国识别号、本法规编号"152R"、短划和批准号。
- 批准标记应清晰易读、不可擦除，并靠近或置于车辆数据牌上。

## 符合性生产与处罚
- 生产一致性程序应符合1958年协定附录1的规定。
- 授予的批准可因不符合生产一致性要求而被撤销。

## 附件
- **附件1**: 通讯表格模型。
- **附件2**: 批准标记的排列方式。
- **附件3**: 适用于电子控制系统安全方面的特殊要求（包括安全概念、文档、验证和测试，以及误反应场景附录）。

---
**文档说明**: 本文件纯属文档工具。真实且具有法律约束力的文本是：ECE/TRANS/WP.29/2019/61。
**修订历史**: 本法规作为1958年协定附件于2020年1月22日生效。文件基于包括2017年9月14日生效的修正案在内的第3修订版。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 4 个
> - 公式 0 个
> - 图像 2 个
> - 全文 Markdown 66,016 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 4 个）

#### 表 1 (page 7)
<table><tr><td rowspan=2 colspan=1>Relative Speed(km/h)</td><td rowspan=1 colspan=2>Stationary</td><td rowspan=1 colspan=2>Moving</td></tr><tr><td rowspan=1 colspan=1>Laden</td><td rowspan=1 colspan=1>Unladen</td><td rowspan=1 colspan=1>Laden</td><td rowspan=1 colspan=1>Unladen</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td></tr></table>

#### 表 2 (page 8)
**Maximum relative Impact Speed $\mathbf { ( k m / h ) }$ for $\mathbf { N _ { 1 } }$ vehicles **

<table><tr><td rowspan=3 colspan=1>RelativeSpeed(km/h)</td><td rowspan=1 colspan=4>Stationary</td><td rowspan=1 colspan=4>Moving</td></tr><tr><td rowspan=1 colspan=2>Laden</td><td rowspan=1 colspan=2>Unladen</td><td rowspan=1 colspan=2>Laden</td><td rowspan=1 colspan=2>Unladen</td></tr><tr><td rowspan=1 colspan=1>a&gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td><td rowspan=1 colspan=1>a &gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td><td rowspan=1 colspan=1>a&gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td><td rowspan=1 colspan=1>a&gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>=</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>二</td><td rowspan=1 colspan=1>二</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td></tr></table>

#### 表 3 (page 9)
<table><tr><td rowspan=1 colspan=1>Subject vehicle speed(km/h)</td><td rowspan=1 colspan=1>Laden</td><td rowspan=1 colspan=1>Unladen</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>20.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>40.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>45.00</td></tr></table>

#### 表 4 (page 9)
<table><tr><td rowspan=2 colspan=1>Subjectvehicle speed(km/h)</td><td rowspan=1 colspan=2>Laden</td><td rowspan=1 colspan=2>Unladen</td></tr><tr><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>α≤1.3</td><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>α≤1.3</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>10.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>15.00</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>20.00</td><td rowspan=1 colspan=1>20.00</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>25.00</td><td rowspan=1 colspan=1>25.00</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>30.00</td><td rowspan=1 colspan=1>30.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr><tr><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>40.00</td><td rowspan=1 colspan=1>45.00</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>50.00</td><td rowspan=1 colspan=1>45.00</td><td rowspan=1 colspan=1>50.00</td></tr></table>

### 图像（取前 2 张）

![图 page 16](../_mineru_assets/ECE R152/3a58afdef5c2623141dbffa71d9d1217f714f80c282378442fb006b98696773b.jpg)  

![图 page 16](../_mineru_assets/ECE R152/615fb7c5bb8c322b708a470f255cf0e3066e5d500a45d98d9bfe869cf66badb6.jpg)  

