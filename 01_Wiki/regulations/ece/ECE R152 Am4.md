---
reg_id: ECE R152 Am4
title: UN Regulation No. 152 - Amendment 4 - Advanced Emergency Braking System (AEBS)
  for M and N vehicles
type: type/amendment
region: ece
status: active
entry_into_force_date: 2021-09-30
source_file: R152am4e.pdf
source_url: E/ECE/TRANS/505/Rev.3/Add.151/Amend.4
standard_body: UNECE
version: Amendment 4
parent_regulation: '[[UN R152]]'
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\152\R152am4e.pdf
publication_date: 2021-12-21
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及在用车型实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及取代关系。
_ocr_upgraded: mineru
_mineru_content_hash: 8b9702122b496c0d
_mineru_outputs_dir: outputs/8b9702122b496c0d
_mineru_blocks:
  tables: 7
  formulas: 2
  images: 4
_mineru_merged_at: '2026-04-23'
---

# UN Regulation No. 152 - Amendment 4

**法规状态**: 生效
**生效日期**: 2021年9月30日
**发布机构**: 联合国欧洲经济委员会 (UNECE)
**文件编号**: E/ECE/TRANS/505/Rev.3/Add.151/Amend.4

## 概述
本文件是对联合国法规 UN R152（关于 M 类和 N 类车辆高级紧急制动系统 (AEBS) 的批准统一规定）的第 4 号修正案。

## 主要修订内容

### 1. 一般要求 (第 5 条)
*   **5.1.4.1.3.** 新增：检测到任何非电气故障条件（例如传感器失明或传感器错位）时，应点亮第 5.1.4.1 段定义的警告信号。
*   **5.1.4.3.** 删除。
*   **5.1.6. 误反应避免**：修订。系统应设计为尽量减少碰撞警告信号的产生，并避免在没有即将发生碰撞风险的情况下进行高级紧急制动。这应在附件 3 进行的评估中证明，且该评估应特别包括附件 3 附录 2 中列出的场景。
*   **5.2. 至 5.2.1.4. 特定要求 - 车对车场景**：修订，包括为 M1 类车辆表格添加缺失的标题。规定了在特定条件下（如平坦、干燥道路，环境照度至少 1000 Lux 等），AEBS 应能达到小于或等于下表中所示的最大相对碰撞速度。
    *   **最大相对碰撞速度表 (M1 车辆)**：
        | 相对速度 (km/h) | 静止/移动目标 | 最大质量 | 运行质量 |
        | :--- | :--- | :--- | :--- |
        | 10 | 0.00 | 0.00 |
        | ... | ... | ... |
        | 60 | 35.00 | 35.00 |
*   **5.2.2. 至 5.2.2.4. 车对行人场景**：修订。规定了在特定条件下（如行人垂直横穿，环境照度至少 2000 Lux 等），AEBS 应能达到小于或等于下表中所示的最大相对碰撞速度。
*   **5.4. 停用**：修订。
    *   **5.4.2.3.** 新增：如果 AEBS 功能的自动停用是驾驶员手动关闭车辆 ESC 功能的结果，则此 AEBS 停用应要求驾驶员至少进行两次有意的操作。
    *   **5.4.4.** 新增：当自动驾驶功能处于车辆的纵向控制时（例如 ALKS 激活），AEBS 功能可以在不向驾驶员提示的情况下暂停或其控制策略（即制动需求、警告时机）进行调整，只要确保车辆提供至少与手动操作期间 AEBS 功能相同的碰撞避免能力。
*   **5.5.7. 光学警告信号**：修订。当向驾驶员提供光学警告信号以指示 AEBS 暂时不可用时（例如由于恶劣天气条件），该信号应为常亮。上文第 5.5.4 段规定的故障警告信号可用于此目的。

### 2. 试验条件 (第 6 条)
*   **6.1.6.** 新增：应制造商要求并经技术服务机构同意，可在偏离的试验条件下（次优条件，例如非干燥路面；低于规定的最低环境温度）进行试验，同时仍需满足性能要求。
*   **6.3. 试验目标**：修订。用于车辆检测试验的目标应为符合 ISO 19206-3:2020 的 M1 类量产轿车或具有代表性的“软目标”。
*   **6.4.1. 静止目标场景的警告和激活试验**：修订，增加了 M1 和 N1 类别的试验速度表。
    *   **M1 类别试验速度 (静止目标)**：
        | 最大质量 | 运行质量 | 公差 |
        | :--- | :--- | :--- |
        | 20 | 20 | +2/-0 |
        | 40 | 42 | +0/-2 |
        | 60 | 60 | +0/-2 |
    *   **N1 类别试验速度 (静止目标)**：
        | 最大质量 | | 运行质量 | | 公差 |
        | :--- | :--- | :--- | :--- | :--- |
        | α >1.3 | α ≤1.3 | α >1.3 | α ≤1.3 | |
        | 20 | 20 | 20 | 20 | +2/-0 |
        | 38 | 30 | 42 | 35 | +0/-2 |
        | 60 | 60 | 60 | 60 | +0/-2 |
*   **6.5. 移动车辆目标的警告和激活试验**：修订，增加了 M1 和 N1 类别的试验速度表（目标车辆以 20 km/h 行驶）。
    *   **M1 类别试验速度 (移动目标)**：
        | 最大质量 | 运行质量 | 公差 |
        | :--- | :--- | :--- |
        | 30 | 30 | +2/-0 |
        | 60 | 60 | +0/-2 |
    *   **N1 类别试验速度 (移动目标)**：
        | 最大质量 | | 运行质量 | | 公差 |
        | :--- | :--- | :--- | :--- | :--- |
        | α >1.3 | α ≤1.3 | α >1.3 | α ≤1.3 | |
        | 30 | 30 | 30 | 30 | +2/-0 |
        | 58 | 50 | 60 | 55 | +0/-2 |
*   **6.6. 行人目标的警告和激活试验**：修订，增加了 M1 和 N1 类别的试验速度表（行人目标以 5 km/h 垂直横穿）。
    *   **M1 类别试验速度 (行人目标)**：
        | 最大质量 | 运行质量 | 公差 |
        | :--- | :--- | :--- |
        | 20 | 20 | +2/-0 |
        | 30 | 30 | +0/-2 |
        | 60 | 60 | +0/-2 |
    *   **N1 类别试验速度 (行人目标)**：
        | 最大质量 | | 运行质量 | | 公差 |
        | :--- | :--- | :--- | :--- | :--- |
        | α >1.3 | α ≤1.3 | α >1.3 | α ≤1.3 | |
        | 20 | 20 | 20 | 20 | +2/-0 |
        | 30 | N. A. | 30 | 25 | +0/-2 |
        | 60 | 60 | 60 | 60 | +0/-2 |

### 3. 附件 3 - 附录 2：误反应场景
*   删除了原第 1 至 3 段。
*   新增了介绍性段落，要求使用指定场景评估系统为尽量减少误反应而实施的策略。制造商应解释确保安全的基本策略，并提供系统在所述场景中行为的证据（例如仿真结果、真实世界试验数据、场地试验数据）。如果技术服务机构认为有必要演示该场景，则应使用每个场景第 2 子段中描述的参数作为指导。
*   定义了**重叠比**和**偏移比**的计算公式。
*   新增了 **4 个具体评估场景**：
    1.  **场景 1：交叉路口左转或右转** - 主车在交叉路口前左转或右转，对向有车辆停驻等待转弯。
    2.  **场景 2：前车右转或左转** - 主车跟随前车行驶，前车在拐角处转弯，主车直行。
    3.  **场景 3：带有护栏和静止物体的弯道** - 主车在小半径弯道行驶，弯道外侧设有护栏，护栏外有静止车辆、行人或自行车目标。
    4.  **场景 4：因道路施工变道** - 主车在车道中心设有指示车道减少的标志牌前变道。

## 备注
*   本文件纯属文献工具。具有真实性和法律约束力的文本是：ECE/TRANS/WP.29/2021/15。
---

## 原文参考（MinerU 云解析 · 2026-04-23）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 7 个
> - 公式 2 个
> - 图像 4 个
> - 全文 Markdown 21,237 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 7 个）

#### 表 1 (page 1)
<table><tr><td rowspan=2 colspan=1>Relative Speed(km/h)</td><td rowspan=1 colspan=2>Stationary/ Moving</td></tr><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in runningorder</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0.00</td><td rowspan=1 colspan=1>0.00</td></tr><tr><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>…</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>35.00</td><td rowspan=1 colspan=1>35.00</td></tr></table>

#### 表 2 (page 3)
**Subject vehicle test speed for $\mathbf { N _ { 1 } }$ category in stationary target scenario **

<table><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>+0/-2</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 3 (page 3)
<table><tr><td rowspan=1 colspan=2>Maximum mass</td><td rowspan=1 colspan=2>Massin running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>a&gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>α≤1.3</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>+0/-2</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 4 (page 4)
<table><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 5 (page 4)
<table><tr><td rowspan=1 colspan=2>Maximum mass</td><td rowspan=1 colspan=2>Mass in running order</td><td rowspan=2 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>α≤1.3</td><td rowspan=1 colspan=1>a &gt;1.3</td><td rowspan=1 colspan=1>a≤1.3</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>58</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 6 (page 4)
<table><tr><td rowspan=1 colspan=1>Maximum mass</td><td rowspan=1 colspan=1>Mass in running order</td><td rowspan=1 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>+0/-2</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

#### 表 7 (page 4)
**Subject vehicle test speed for $\mathbf { N _ { 1 } }$ category in pedestrian target scenario **

<table><tr><td rowspan=1 colspan=2>Maximum mass</td><td rowspan=1 colspan=2>Mass in running order</td><td rowspan=2 colspan=1>Tolerance</td></tr><tr><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>α≤1.3</td><td rowspan=1 colspan=1>α&gt;1.3</td><td rowspan=1 colspan=1>a ≤1.3</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>+2/-0</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>N. A.</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>+0/-2</td></tr><tr><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>+0/-2</td></tr></table>

### 公式（取前 2 个）

**公式 1** (page 5):

$$
\mathrm { R _ { o v e r l a p } = L _ { o v e r l a p } / W _ { v e h i c l e } \ast 1 0 0 }
$$

**公式 2** (page 5):

$$
\begin{array} { r l } & { \mathrm { \bf R } _ { \mathrm { o f f s e t } } = \mathrm { \bf L } _ { \mathrm { o f f s e t } } / \left( 0 . 5 ^ { * } \mathrm { \bf W } _ { \mathrm { v e h i c l e } } \right) ^ { * } 1 0 0 } \\ & { \mathrm { \bf { R } } _ { \mathrm { o f f s e t } } : \mathrm { O f f s e t r a t i o } \left[ \% \right] } \end{array}
$$

### 图像（取前 4 张）

![Figure 1 Left turn or right turn at the intersection ](../_mineru_assets/ECE R152 Am4/a91e469ef727f27deace845cddf64a002b3018a5931e6cada52c06166e5c75cd.jpg)  
*Figure 1 Left turn or right turn at the intersection * (page 6)

![Figure 2 Right turn or left turn of a forward vehicle ](../_mineru_assets/ECE R152 Am4/b79f94f874a178c04cbac9b2092952f30047f19b79e08f9479f0df0b90b0d582.jpg)  
*Figure 2 Right turn or left turn of a forward vehicle * (page 7)

![Figure 3 Curved road with guard pipes and a stationary object ](../_mineru_assets/ECE R152 Am4/46b5a90bc2ffce08c864eaecaeb94ab07dd16656e09e6feb9c48dd407c432384.jpg)  
*Figure 3 Curved road with guard pipes and a stationary object * (page 8)

![Figure 4 Lane change due to road construction ](../_mineru_assets/ECE R152 Am4/a916331da77cb461b9a8be1909965dc282b45e95d550d2f79745e8d743d63ae3.jpg)  
*Figure 4 Lane change due to road construction * (page 9)

