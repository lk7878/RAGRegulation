---
reg_id: ECE R79-04e6 Rev4 Am6
type: type/amendment
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to steering
  equipment
short_title: UN Regulation No. 79
status: active
publication_date: 2022-03-17
implementation_date_new_vehicle: 2022-01-07
version: Revision 4 - Amendment 6
series: 04 series of amendments
standard_body: UNECE
source_file: R079r4am6e.pdf
topics:
- Steering equipment
- Risk Mitigation Function (RMF)
- Lane Change Procedure
- Automated driving functions
- Vehicle safety
- Type approval
tags:
- type/amendment
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\79\R079r4am6e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: implementation_date_new_vehicle
  status: mismatch
  extracted: 2022-01-07
  original: '2022-01-07 (原文为“Date of entry into force: 7 January 2022”)'
  note: 原文“生效日期”为2022年1月7日，但A中字段名为“implementation_date_new_vehicle”（新车型实施日期），原文未明确区分新车型和在用车型的实施日期。A的值与原文生效日期一致，但字段名可能不精确。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段，B中也未提及在用车型的特殊实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A和B中均未提及等效法规信息。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A和B中均未明确提及取代的法规版本。
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-25'
_mineru_outputs_dir: outputs\4079829279898494
---

**UN Regulation No. 79 (Revision 4, Amendment 6) - Steering Equipment**

**法规状态与版本**
*   **发布机构:** 联合国欧洲经济委员会 (UNECE)
*   **发布日期:** 2022年3月17日
*   **生效日期:** 2022年1月7日
*   **法规系列:** 第04系列修正案
*   **当前版本:** 第4修订版，第6修正案
*   **文件性质:** 本文档仅为记录工具。具有真实法律约束力的文本是: ECE/TRANS/WP.29/2021/82（根据报告第99段修订）。

**核心修订内容摘要**
本次修正案主要引入了关于**风险缓解功能 (Risk Mitigation Function, RMF)** 的详细技术要求。RMF是一种在驾驶员失去反应能力时，能自动控制车辆转向系统，旨在将车辆安全停放在目标停车区域的紧急功能。

**主要新增与修订条款**

1.  **新增定义 (第2章):**
    *   **2.3.4.5. 风险缓解功能 (RMF):** 定义了该功能的目的和触发条件。
    *   **2.4.19. 目标停车区域:** 定义了可能的停车区域（如应急车道、硬路肩、路旁、最慢车道、本车道）。
    *   **2.4.20. 路旁:** 定义了车道边界之外、非硬路肩或避险区的路面区域。
    *   **修订 2.4.16. 车道变更程序:** 明确了从开启转向灯到关闭转向灯的完整过程。

2.  **RMF 系统要求 (第5.1.6.3条及子条款):**
    *   **触发条件 (5.1.6.3.1):** RMF仅在驾驶员被评估为无反应（直接或间接）或手动激活时启动干预。手动激活装置需防误操作。
    *   **警告信号 (5.1.6.3.2):** 每次RMF干预前（除非情况紧急）需向驾驶员发出光学警告，以及附加的声学和/或触觉警告，警告阶段至少持续5秒。干预期间需持续向驾驶员发出警告信号。警告信号需有明显区别和高紧迫性。
    *   **系统交互 (5.1.6.3.3):** RMF干预不应不合理地停用或抑制已激活的辅助系统（如AEBS）。
    *   **危险警告灯 (5.1.6.3.4):** 干预开始时需自动激活危险警告灯。
    *   **驾驶员超控 (5.1.6.3.5):** 驾驶员必须能通过明确动作随时超控RMF干预。系统需设计策略防止对驾驶控制输入的意外超控，并在型式批准时向技术服务机构演示。
    *   **减速要求 (5.1.6.3.6):** 干预期间，车辆减速需求不应大于4 m/s²，除非周围交通所需。更高减速度值允许极短时间出现（如作为触觉警告）。
    *   **停车后状态 (5.1.6.3.7):** RMF将车辆安全停至目标区域后，车辆不得在没有人工输入的情况下自行移动。
    *   **故障指示 (5.1.6.3.8):** 若RMF系统检测到妨碍其执行干预的故障，必须向驾驶员发出信号。
    *   **旨在将车辆停至本车道之外的系统附加规定 (5.1.6.3.9):**
 *   仅当车辆具备前、侧、后方探测能力时，才允许RMF变道 (5.1.6.3.9.1)。
 *   变道程序需以非关键方式进行，确保不会导致碰撞，且对其他道路使用者是可预测和可管理的 (5.1.6.3.9.2, 5.1.6.3.9.7, 5.1.6.3.9.8)。
 *   规定了变道期间的横向加速度限制、对后方车辆的影响评估、空间要求等具体安全准则 (5.1.6.3.9.8.1 - 5.1.6.3.9.8.5)。
 *   变道需通过激活相应转向灯（而非危险警告灯）提前向其他道路使用者指示 (5.1.6.3.9.13)。
 *   制造商需声明前、侧、后方的探测范围，技术服务机构需评估其与变道策略的对应关系 (5.1.6.3.9.17)。
    *   **停车后吸引外部注意 (5.1.6.3.10):** 当车辆停稳后驾驶员仍无反应时，系统应实施策略吸引外部注意（如触发紧急呼叫、鸣喇叭、保持危险警告灯激活）。
    *   **M2/M3类车辆特殊规定 (5.1.6.3.11):** 涉及乘客手动激活时的指示，以及对特定类别车辆乘客的声光警告要求。
    *   **系统信息数据 (5.1.6.3.12):** 型式批准时需向技术服务机构提供一系列系统设计信息，包括驾驶员无反应确认方式、变道能力、环境感知手段、适用道路类型、超控方式、警告策略、目标区域选择逻辑、不同环境下的最高运行速度等。

3.  **过渡性条款 (第12.3条):**
    *   明确了第04系列修正案的强制接受和逐步淘汰先前系列修正案型式批准的时间表。
    *   关键时间点：2023年9月1日（可拒收此后首次签发的前系列批准），2025年9月1日（可拒收所有前系列批准）。
    *   对于不受本次新增的5.1.6.3.9条（变道相关）规定影响的车辆，缔约方应继续接受根据前系列修正案签发的UN型式批准。

4.  **新增测试规范 (附件8，第3.6条):**
    *   新增了针对RMF的测试要求。
    *   **3.6.1 旨在将车辆停在本车道内的RMF测试:** 验证干预指示、危险警告灯激活、减速度限制和停车后状态。
    *   **3.6.2 旨在将车辆停在本车道外的RMF测试:** 分为两种场景：
 *   **场景A (变道可行):** 验证系统在满足安全条件时执行变道。
 *   **场景B (变道不可行):** 验证系统在目标车道有车辆阻碍时，不启动变道，并保持在当前车道内停车。
    *   测试条件和速度需在制造商声明的系统运行范围内，具体测试细节需由制造商与技术服务机构协商确定。制造商还需通过文件证明其系统在整个运行范围内满足第5.1.6.3条的要求。
