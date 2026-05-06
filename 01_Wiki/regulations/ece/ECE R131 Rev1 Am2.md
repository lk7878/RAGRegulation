---
reg_id: ECE R131 Rev1 Am2
region: ece
type: type/amendment
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Advanced Emergency Braking Systems (AEBS)
status: active
publication_date: 2023-02-21
implementation_date_new_vehicle: 2023-01-04
series_of_amendments: 2
version: Rev.1/Amend.2
authentic_text_ref: ECE/TRANS/WP.29/2022/76
source_file: R131r1am2e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\131\R131r1am2e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: ece
  original: null
  note: B 未明确提及“standard_body”字段，但法规是 UNECE 框架下的。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及针对在用车辆的生效日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确列出“equivalent_to”字段。B 的 Scope 脚注提及与 UN R152 的批准等效，但未以结构化字段形式出现。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未明确提及本修正案替代了哪个具体版本。
- field: 技术要求限值
  status: unsure
  extracted: 见法规表1和表2
  original: 见法规第5条及后续表格
  note: A 概括了性能要求，但未提取具体限值数字。B 中限值在法规正文第5条及后续表格中，但提供的原文片段未包含具体表格数据，无法核实。
_ocr_upgraded: mineru
_mineru_content_hash: 1b5acaf434a7d26e
_mineru_outputs_dir: outputs/1b5acaf434a7d26e
_mineru_blocks:
  tables: 2
  formulas: 3
  images: 7
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 131 - Advanced Emergency Braking Systems (AEBS)

## 法规概述
本法规规定了关于**高级紧急制动系统 (AEBS)** 的车辆型式批准统一规定。适用于 M2、M3、N2 和 N3 类车辆。本版本（02 系列修正案）将适用范围扩展至城市驾驶等新场景。

## 适用范围
本法规适用于 M2、M3、N2 和 N3 类车辆上安装的、旨在实现以下功能的车载系统的批准：
1.  避免或减轻与前方同车道车辆的追尾碰撞。
2.  避免或减轻与行人的碰撞。

> **注**：对于配备液压制动的 M2 类车辆，以及最大质量 ≤ 8 吨的 M3/N2 类车辆，同时是 UN R152 和本法规缔约方的国家，应承认依据任一法规授予的批准具有同等效力。

## 核心要求

### 1. 系统性能
*   **车对车场景**：
    *   **速度范围**：系统至少在 10 km/h 至车辆最高设计速度之间激活。
    *   **碰撞警告**：当检测到与前方 M、N 或 O 类车辆即将发生碰撞时，应提供碰撞警告，最迟在紧急制动开始前 0.8 秒触发。
    *   **紧急制动**：系统应发出至少 4 m/s² 的制动需求。
    *   **速度降低要求**：在特定理想条件下（如干燥高附着力路面、良好天气、无外部传感干扰等），系统应能将相对碰撞速度降低至不超过规定值（见法规表 1）。要求根据车辆类型（是否源自 M1/N1、是否配备液压制动、质量是否 >8t 等）和相对速度而异。
*   **车对行人场景**：
    *   **速度范围**：系统至少在 20 km/h 至 60 km/h 之间激活。
    *   **碰撞警告**：当检测到可能与以 ≤5 km/h 速度横穿道路的行人发生碰撞时，应提供碰撞警告，最迟在紧急制动开始时发出。
    *   **紧急制动**：系统应发出至少 4 m/s² 的制动需求。
    *   **速度降低要求**：在特定理想条件下，系统应能将碰撞速度（车辆行驶方向）降低至不超过规定值（见法规表 2）。要求根据车辆类型和车辆速度而异。

### 2. 系统特性
*   **误反应避免**：系统设计应尽量减少碰撞警告信号的产生，并避免在无迫在眉睫碰撞风险的情况下进行高级紧急制动。必须根据附件 3 进行评估，并特别包括附件 3 附录 2 中列出的场景。
*   **驾驶员干预**：系统必须提供适当且可靠的方式，供驾驶员中断碰撞警告和紧急制动。中断可由任何表明驾驶员意识到紧急情况的主动动作（如急踩油门或足以改变方向避开目标的转向动作）启动。
*   **停用**：
    *   **手动停用**：如果配备手动停用功能，必须通过至少两个有意的操作才能实现。系统应在每次新的点火循环时自动恢复，或在手动停用后最多 15 分钟自动恢复。
    *   **自动停用**：对于特定情况（如越野、被牵引等），可自动停用。制造商需提供停用情况和标准的清单。一旦导致停用的条件不再存在，系统应自动重新激活。
    *   **停用警告**：必须通过恒定的光学警告信号告知驾驶员 AEBS 功能已停用。
*   **警告指示**：
    *   **碰撞警告**：必须通过至少两种模式（声学、触觉或光学）提供。
    *   **故障警告**：当 AEBS 存在妨碍满足本法规要求的故障时，应提供恒定的黄色光学警告信号。
    *   **系统未初始化警告**：如果系统在车速高于 10 km/h 累计行驶 15 秒后仍未初始化，应向驾驶员指示此状态。

### 3. 测试程序
*   **测试条件**：规定了测试路面、环境温度、能见度、风速、环境照度等要求。
*   **车辆条件**：规定了测试质量（最大质量或运行质量）、测试前预处理、轮胎等要求。
*   **测试目标**：
    *   **车辆目标**：使用 M1 类量产乘用车或符合 ISO 19206-3:2021 的代表乘用车的“软目标”。
    *   **行人目标**：使用符合 ISO 19206-2:2018 的代表儿童行人的“铰接式软目标”。
*   **具体测试**：
    *   对静止车辆目标的警告和激活测试。
    *   对移动车辆目标的警告和激活测试。
    *   对行人目标的警告和激活测试。
    *   故障检测测试。
    *   停用测试。
    *   系统鲁棒性测试（允许一定比例的测试失败）。
    *   误反应测试（车辆以 50 km/h 从两辆静止车辆中间穿过，系统不应触发警告或制动）。

### 4. 批准与符合性
*   **批准标记**：获得批准的车辆应粘贴符合附件 2 规定的国际批准标记。
*   **型式修改与扩展**：对车辆型式的任何修改都应通知型式批准机构，该机构可决定是否扩展批准。
*   **生产一致性**：要求已批准的车辆生产必须符合已批准型式的技术要求。型式批准机构应至少每两年进行一次生产一致性检查。

### 5. 过渡性条款 (02 系列修正案)
*   自 02 系列修正案正式生效之日起，缔约方不得拒绝根据该修正案授予或接受型式批准。
*   2025年9月1日之后，缔约方无义务接受在此日期之后首次颁发的、针对先前系列修正案的型式批准。
*   2028年9月1日之前，缔约方应接受在2025年9月1日之前首次颁发的、针对先前系列修正案的型式批准。
*   自2028年9月1日起，缔约方无义务接受针对本法规先前系列修正案颁发的型式批准。

## 附件
1.  **附件 1**：信息交流文件（批准/扩展/拒绝/撤销/生产终止的通信表格）。
2.  **附件 2**：批准标记的排列方式。
3.  **附件 3**：适用于电子控制系统安全方面的特殊要求。
    *   定义了文件、故障策略和验证方面的要求。
    *   要求制造商提供安全概念说明，并进行危害/风险分析、失效模式与影响分析（FMEA）等。
    *   包括附录 1（电子系统评估模型表格）和附录 2（误反应场景，用于评估系统最小化误反应的策略）。

## 关联法规
*   **UN R10**：关于电磁兼容性的法规。AEBS 的有效性不应受磁场或电场的不利影响，应通过符合 UN R10 的 05 或更高系列修正案来证明。
*   **UN R13**：关于制动系统的法规。配备 AEBS 的车辆必须满足 UN R13 第 11 系列修正案对 M2、M3、N2、N3 类车辆的性能要求，并配备符合 UN R13 附件 13 第 11 系列修正案性能要求的防抱死系统。
*   **UN R121**：关于控制装置、信号装置和指示器的法规。AEBS 停用控制装置的位置应符合 UN R121 第 01 或更高系列修正案的相关要求。
*   **UN R152**：关于 M1 和 N1 类车辆自动紧急制动（AEB）系统的法规。对于某些车辆，批准 UN R152 或 UN R131 具有同等效力。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 2 个
> - 公式 3 个
> - 图像 7 个
> - 全文 Markdown 87,061 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 2 个）

#### 表 1 (page 9)
**Table 1 Maximum relative Impact Speed $\mathbf { ( k m / h ) }$ (regardless whether target stationary or moving)\* **

<table><tr><td rowspan=3 colspan=1>Relative Speed(km/h)</td><td rowspan=1 colspan=3>M2,M≤8t and N≤8t</td><td rowspan=1 colspan=1>M3&gt;8t,N&gt;8t,N3</td></tr><tr><td rowspan=2 colspan=1>Vehiclederivedfrom M/N **</td><td rowspan=1 colspan=2>Other vehicles</td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Vehicles notequipped withhydraulicbraking(e.g. pneumatic,Air overhydraulic(AOH))</td><td rowspan=1 colspan=1>Vehicles with hydraulicbraking</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>49</td><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>61</td><td rowspan=1 colspan=1>28</td></tr><tr><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>71</td><td rowspan=1 colspan=1>42</td></tr><tr><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>71</td><td rowspan=1 colspan=1>54</td><td rowspan=1 colspan=1>82</td><td rowspan=1 colspan=1>54***</td></tr></table>

#### 表 2 (page 11)
**Table 2 Maximum Impact Speed in the direction of travel of the vehicle $( \mathbf { k m } / \mathbf { h } ) \mathrel { \ast }$ **

<table><tr><td rowspan=3 colspan=1>Subject vehiclespeed(km/h)</td><td rowspan=1 colspan=3>M,M≤8t and N2≤8t</td><td rowspan=1 colspan=1>M&gt;8t,N&gt;8t,N</td></tr><tr><td rowspan=2 colspan=1>Vehicle derivedfrom M/N **</td><td rowspan=1 colspan=2>Other vehicles</td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Vehicles notequipped withhydraulicbraking (e.g.pneumatic,AOH)</td><td rowspan=1 colspan=1>Vehicles with hydraulicbraking</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>18</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>29</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>39</td><td rowspan=1 colspan=1>39</td><td rowspan=1 colspan=1>39</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>46</td><td rowspan=1 colspan=1>49</td><td rowspan=1 colspan=1>49</td><td rowspan=1 colspan=1>49</td></tr></table>

### 公式（取前 3 个）

**公式 1** (page 4):

$$
d _ { m } = \frac { v _ { b } ^ { 2 } - v _ { e } ^ { 2 } } { 2 5 . 9 2 ( s _ { e } - s _ { b } ) }
$$

**公式 2** (page 31):

$$
\mathrm { R _ { o v e r l a p } = L _ { o v e r l a p } / W _ { v e h i c l e } \ast 1 0 0 }
$$

**公式 3** (page 31):

$$
\mathrm { R _ { o f f s e t } = L _ { o f f s e t } / \left( 0 . 5 ^ { \ast } W _ { v e h i c l e } \right) ^ { \ast } 1 0 0 }
$$

### 图像（取前 7 张）

![图 page 21](../_mineru_assets/ECE R131 Rev1 Am2/96670a0114ae95324c840dbfced60841425a5407c2f4ba9764681c1b2dc53e83.jpg)  

![a = 8 mm min ](../_mineru_assets/ECE R131 Rev1 Am2/ac17f955297abe4b06f461e3a19072e4b29a49dafe5037e4fe4d8d4ade78bf3d.jpg)  
*a = 8 mm min * (page 22)

![Figure 1 Left turn or right turn at the intersection ](../_mineru_assets/ECE R131 Rev1 Am2/2982e0b1be350b38b52488bd1044be0383f7192281f601d4ddba7bfd3b5a3adc.jpg)  
*Figure 1 Left turn or right turn at the intersection * (page 32)

![Figure 2 Right turn or left turn of a forward vehicle ](../_mineru_assets/ECE R131 Rev1 Am2/183f0a2b402ed80db3ff8fdef1e23784772c8621853a2af2ac24156569db3dd5.jpg)  
*Figure 2 Right turn or left turn of a forward vehicle * (page 33)

![Figure 3 Curved road with guard pipes and a stationary object ](../_mineru_assets/ECE R131 Rev1 Am2/e34f09def1bd09095472eec122ebeee28b0b76f38fd941121fca79ce326ff369.jpg)  
*Figure 3 Curved road with guard pipes and a stationary object * (page 34)

![Figure 4 Lane change due to road construction ](../_mineru_assets/ECE R131 Rev1 Am2/8ca0eed3333f9ef7bc522a35475f98ee39819d873327f1923f7eaa337315be88.jpg)  
*Figure 4 Lane change due to road construction * (page 35)

![图 page 36](../_mineru_assets/ECE R131 Rev1 Am2/1349b9659b93ac08d3df9736f5cdceb00470f8bfb0b58e4cd30668f6cff05e54.jpg)  

