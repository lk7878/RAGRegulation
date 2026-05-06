---
reg_id: ECE R131
region: ece
type: type/version
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Advanced Emergency Braking Systems (AEBS)
status: active
publication_date: 2013-08-07
implementation_date_new_vehicle: 2013-07-09
authority: UNECE
source_file: 国外法规\ECE标准\标准法规-UNECE\121~160\131\R131e.pdf
tags:
- type/version
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\131\R131e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: UNECE
  original: null
  note: B 中未明确提及发布机构名称，仅提及协定和联合国，无法核实。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及在用车辆的实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及替代法规。
_ocr_upgraded: mineru
_mineru_content_hash: 8504d5487a802ebc
_mineru_outputs_dir: outputs/8504d5487a802ebc
_mineru_blocks:
  tables: 1
  formulas: 0
  images: 1
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 131 (AEBS)

## 法规信息
*   **法规编号**: UN Regulation No. 131
*   **法规标题**: 关于批准配备高级紧急制动系统（AEBS）的机动车辆的统一规定
*   **发布机构**: 联合国欧洲经济委员会 (UNECE)
*   **发布日期**: 2013年8月7日
*   **生效日期**: 2013年7月9日 (作为《1958年协定》附件生效)

## 适用范围与目的
本法规适用于批准配备气动或气顶液制动系统的以下类别车辆，旨在避免或减轻车道内追尾碰撞的严重性：
*   (a) 总质量超过8吨的N2类车辆；
*   (b) M3类车辆；
*   (c) N3类车辆。

## 核心定义
*   **高级紧急制动系统 (AEBS)**: 能够自动检测潜在的前向碰撞并激活车辆制动系统以使车辆减速，旨在避免或减轻碰撞的系统。
*   **碰撞警告阶段**: 紧接紧急制动阶段之前的阶段，在此期间AEBS警告驾驶员潜在的前向碰撞。
*   **紧急制动阶段**: 从AEBS向车辆行车制动系统发出至少4 m/s²减速度的制动需求时开始的阶段。
*   **碰撞时间 (TTC)**: 在某一时刻，用主车与目标物之间的距离除以主车与目标物的相对速度所得到的时间值。

## 技术要求摘要
1.  **系统性能**:
    *   系统应在车速至少15 km/h至车辆最高设计速度的范围内，且在所有车辆负载条件下保持激活（除非手动停用）。
    *   系统应自动检测与前车（同车道、速度较慢、减速至停止或静止）发生碰撞的可能性，并向驾驶员提供警告。
    *   警告后，若驾驶员未响应，系统应启动紧急制动阶段，以显著降低主车速度。
    *   系统设计应尽量减少碰撞警告信号的产生，并避免在驾驶员不会识别即将发生的前向碰撞的情况下进行自主制动。
    *   系统有效性不得受磁场或电场的不利影响（需符合UN R10, 03系列修正案）。
    *   需配备符合UN R13附件13性能要求的防抱死制动功能。
    *   复杂电子控制系统的安全方面需符合本法规附件4的要求。

2.  **驾驶员干预**:
    *   系统应为驾驶员提供中断紧急制动阶段的手段。
    *   中断可由任何表明驾驶员意识到紧急情况的积极动作（如油门踩到底、操作转向指示灯控制）启动。

3.  **警告指示**:
    *   **碰撞警告**: 应至少从声学、触觉或光学模式中选择两种模式提供。警告时机应使驾驶员有可能对碰撞风险做出反应并控制局面。
    *   **故障警告**: 应为恒定的黄色光学警告信号。
    *   **系统停用警告**（如配备手动停用功能）: 应为恒定的光学警告信号（可使用故障警告信号）。
    *   所有光学警告信号在白天应清晰可见，且驾驶员能从驾驶座轻松验证其状态。

4.  **系统停用**:
    *   如果车辆配备手动停用AEBS功能的方法，则每次新的点火循环开始时，AEBS功能应自动重新启用。

## 测试程序摘要
1.  **测试条件**: 平坦、干燥的混凝土或沥青路面；环境温度0°C至45°C；无影响结果的风。
2.  **测试目标**: 使用M1类AA级轿车的量产乘用车，或使用在AEBS传感器系统识别特性上能代表此类车辆的“软目标”。
3.  **对静止目标的警告和激活测试**:
    *   主车以80±2 km/h的速度接近静止目标。
    *   至少一种触觉或声学警告模式应在紧急制动阶段开始前不晚于**1.4秒**提供。
    *   至少两种警告模式应在紧急制动阶段开始前不晚于**0.8秒**提供。
    *   与静止目标碰撞时，主车的总速度降低应不小于**10 km/h**。
    *   紧急制动阶段不得在TTC等于或小于**3.0秒**之前开始。
4.  **对移动目标的警告和激活测试**:
    *   主车以80±2 km/h的速度行驶，移动目标以32±2 km/h的速度行驶。
    *   警告时机要求与静止目标测试相同（至少一种模式不晚于1.4秒，至少两种模式不晚于0.8秒）。
    *   紧急制动阶段应导致主车**不撞击**移动目标。
    *   紧急制动阶段不得在TTC等于或小于**3.0秒**之前开始。
5.  **故障检测测试**: 模拟电气故障，故障警告信号应在车辆以大于15 km/h的速度行驶后不晚于10秒内激活。
6.  **误反应测试**: 主车以50±2 km/h的速度从两辆静止车辆中间穿过，AEBS不得提供碰撞警告或启动紧急制动阶段。

## 批准与符合性
*   车辆制造商或其授权代表提交批准申请。
*   满足要求的车型将获得批准，并分配一个批准编号。
*   获得批准的车辆应粘贴符合规定的国际批准标记。
*   规定了车型修改和批准扩展的程序。
*   规定了生产一致性要求和不符合生产要求的处罚措施。

## 附件
*   **附件1**: 通信表格
*   **附件2**: 批准标记的排列方式
*   **附件3**: 警告和激活测试要求 – 通过/失败值（包含测试参数表格）
*   **附件4**: 适用于复杂电子车辆控制系统安全方面的特殊要求（涉及安全概念、文档、故障策略和验证）
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 1 个
> - 公式 0 个
> - 图像 1 个
> - 全文 Markdown 42,079 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 1 个）

#### 表 1 (page 16)
<table><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>F</td><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=2>H</td><td rowspan=4 colspan=1></td></tr><tr><td rowspan=3 colspan=1></td><td rowspan=1 colspan=3>Stationary target</td><td rowspan=1 colspan=5>Moving target</td></tr><tr><td rowspan=1 colspan=2>Timing of warning modes</td><td rowspan=2 colspan=1>Speedreduction(ref.paragraph6.4.4.）</td><td rowspan=1 colspan=2>Timing of warning modes</td><td rowspan=2 colspan=2>Speed reduction(ref. paragraph6.5.3.</td><td rowspan=2 colspan=1>Target speed(ref. paragraph6.5.1.)</td></tr><tr><td rowspan=1 colspan=1>At least 1 hapticor acoustic(ref.paragraph6.4.2.1.)</td><td rowspan=1 colspan=1>At least2(ref.paragraph6.4.2.2.）</td><td rowspan=1 colspan=1>Atleast1haptic oracoustic(ref. paragraph6.5.2.1.)</td><td rowspan=1 colspan=1>At least 2(ref.paragraph6.5.2.2.)</td></tr><tr><td rowspan=1 colspan=1>M,N&gt;8tand N3</td><td rowspan=1 colspan=1>Not later than1.4 s. beforethe start ofemergencybraking phase</td><td rowspan=1 colspan=1>Not laterthan 0.8 s.before the start ofemergencybrakingphase</td><td rowspan=1 colspan=1>Not lessthan10 km/h</td><td rowspan=1 colspan=1>Not laterthan 1.4 s.before thestart ofemergencybrakingphase</td><td rowspan=1 colspan=1>Not laterthan 0.8 s.before thestart ofemergencybrakingphase</td><td rowspan=1 colspan=2>No impact</td><td rowspan=1 colspan=1>32 ± 2 km/h</td><td rowspan=1 colspan=1>1</td></tr></table>

### 图像（取前 1 张）

![a=8 mm min ](../_mineru_assets/ECE R131/1ce9bfc940f75e1e6b53278896d240dad479517169a49bc84089838d8c97de47.jpg)  
*a=8 mm min * (page 15)

