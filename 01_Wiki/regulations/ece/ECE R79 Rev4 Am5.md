---
reg_id: ECE R79 Rev4 Am5
type: type/amendment
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to steering
  equipment
status: active
publication_date: 2022-03-17
implementation_date_new_vehicle: 2022-01-07
source: ECE/TRANS/WP.29/2021/72
source_url: null
topics:
- steering equipment
- vehicle approval
- ACSF
- lane keeping
- lane change
tags:
- type/amendment
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\41～80\79\R079r4am5e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: implementation_date_new_vehicle
  status: mismatch
  extracted: 2022-01-07
  original: 7 January 2022
  note: 日期一致，但字段名可能不准确。B 中为“Date of entry into force”，A 命名为“implementation_date_new_vehicle”，但日期值匹配。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及此日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效关系。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未提及替代关系。
_ocr_upgraded: mineru
_mineru_content_hash: 79264d234e71386b
_mineru_outputs_dir: outputs/79264d234e71386b
_mineru_blocks:
  tables: 0
  formulas: 1
  images: 0
_mineru_merged_at: '2026-04-22'
---

**法规文件信息**
*   **法规编号:** UN Regulation No. 79, Revision 4, Amendment 5
*   **发布机构:** UNECE
*   **发布日期:** 2022年3月17日
*   **生效日期:** 2022年1月7日
*   **关联文件:** 本文件为03系列修正案的第5次补充。正式法律文本为: ECE/TRANS/WP.29/2021/72。

**修订内容摘要**
本修正案对UN R79法规（关于转向设备）进行了修订，主要涉及自动转向功能（ACSF）的要求。

**主要修订条款**
1.  **条款重编号:** 将原段落2.3.4.18. 重新编号为段落2.4.18.
2.  **5.6.4.1.2 (ACSF B1待机模式):** 当C类ACSF处于待机模式时，B1类ACSF应旨在使车辆在车道内居中，除非由于特定情况或驾驶员输入（例如，当另一辆车紧邻行驶时）导致不同的车道位置被认为是合理的。此要求需由车辆制造商在型式批准期间向技术服务机构证明。
3.  **5.6.4.2.3 (系统运行条件):** 系统应...这些条件应通过至少两种独立的方法来确保。在从允许C类ACSF运行的道路类型过渡到不允许C类ACSF运行的道路类型时，系统应自动停用（关闭模式），除非未满足的**唯一**条件是行驶方向上缺少第二条车道（例如，两条高速公路之间的连接道）。
4.  **5.6.4.3 (驾驶员超控):** 驾驶员的转向输入应能超控系统的转向动作。超控系统提供的方向控制所需的转向控制力不得超过50 N。在超控期间，只要优先权给予驾驶员，系统可以保持激活状态。
5.  **5.6.4.7 (临界情况):** 定义了在变道操作开始时被视为“临界”的情况：即当变道开始0.4秒后，目标车道内的接近车辆需要以高于3 m/s²的减速度减速，才能确保两车之间的距离始终不小于变道车辆在1秒内行驶的距离。同时提供了计算变道操作开始时的临界距离 `S_critical` 的公式及相关参数说明。
6.  **附件8，第2段 (测试条件):** 测试应在平坦、干燥、具有良好附着力的沥青或混凝土表面进行。环境温度应在0°C至45°C之间。应制造商要求并经技术服务机构同意，可在偏离的测试条件下（次优条件，例如非干燥路面；低于规定的最低环境温度）进行测试，但仍需满足性能要求。
7.  **附件8，第3.5.1.2段 (测试要求):** 修订了测试要求，包括：
    *   (a) 朝向车道标线的横向移动不得早于变道程序启动后1秒开始。
    *   (b) 接近车道标线的横向移动和完成变道操作所需的横向移动应作为一个连续动作完成。
    *   ...
    *   (j) 在变道操作自动启动且转向灯控制未完全啮合（锁定位置）的情况下，转向灯应在变道操作结束时或B1类ACSF恢复后不迟于0.5秒内关闭。
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 0 个
> - 公式 1 个
> - 图像 0 个
> - 全文 Markdown 4,865 字符（见 `outputs/<hash>/full.md`）

### 公式（取前 1 个）

**公式 1** (page 1):

$$
\mathbf { S } _ { c r i t i c a l } = ( \nu _ { r e a r } - \nu _ { A C S F } ) * t _ { B } + ( \nu _ { r e a r } - \nu _ { A C S F } ) ^ { 2 } / ( 2 * a ) + \nu _ { A C S F } * t _ { G }
$$

