---
extracted_by: deepseek-v3
region: ece
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\157\R157am3e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
type: type/amendment
reg_id: ECE R157 Am3
title: Uniform provisions concerning the approval of vehicles with regard to Automated
  Lane Keeping Systems
publication_date: 2022-09-29
status: active
verified_by: deepseek-v3
cross_check_overall_confidence: medium
reg_id_conf: low
cross_check_flags:
- field: reg_id
  status: normalized
  extracted: ECE R157 Rev157 Am3
  original: UN Regulation No. 157 Amendment 3
  note: '[Auto-reclassified] Same reg_id after normalization (was: ''ECE R157 Rev157
    Am3'' vs ''UN Regulation No. 157 Amendment 3'')'
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: 双方均未明确提及标准机构字段。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B中未提及新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B中未提及在用车型实施日期。
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
- reg_id
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: 0a86dbd2f3b9e0d3
_mineru_outputs_dir: outputs/0a86dbd2f3b9e0d3
_mineru_blocks:
  tables: 1
  formulas: 1
  images: 0
_mineru_merged_at: '2026-04-25'
---

id: UN R157am3e
region: ece
type: type/regulation
title: Uniform provisions concerning the approval of vehicles with regard to Automated Lane Keeping Systems
status: amendment
date_issued: 2022-09-29
date_effective: 2022-06-22
source: E/ECE/TRANS/505/Rev.3/Add.156/Amend.3
source_url: https://unece.org/transport/documents/2022/09/standards/ece-trans505rev3add156amend3
description: Amendment 3 to UN Regulation No. 157 concerning the approval of vehicles with regard to Automated Lane Keeping Systems (ALKS).
keywords: [ALKS, Automated Lane Keeping System, UN Regulation 157, amendment, vehicle approval, lane keeping]
```

- **法规编号**: UN R157am3e (UN Regulation No. 157 Amendment 3)
- **发布机构**: 联合国欧洲经济委员会 (UNECE)
- **发布/生效日期**: 发布于2022年9月29日，于2022年6月22日生效。
- **法规状态**: 修订案 (Amendment 3, Supplement 3 to the original version)。
- **适用范围**: 适用于M类和N1类车辆关于其自动车道保持系统(ALKS)的型式批准。
- **核心修订内容摘要**:
    - **引言**: 明确了本法规旨在建立关于自动车道保持系统(ALKS)车辆批准的统一规定。ALKS可在特定条件下激活，这些道路禁止行人和骑行者，且通过设计具备物理隔离带分隔对向车流并防止车辆横穿。在第一步中，法规原文将运行速度限制在最高60公里/小时。
    - **定义 (第2.5条)**: 修订了“非计划事件”的定义，指事先未知但假定极可能发生并需要发出接管请求的情况。这可能包括：道路施工、恶劣天气、接近的应急/执法车辆、缺失的车道标线、从卡车上掉落的货物。
    - **系统安全要求 (第5章)**:
 - **5.1.2**: 激活的系统应遵守运营国关于动态驾驶任务(DDT)的交通规则，包括对应急/执法车辆的响应。
 - **5.2.3.3**: 详细规定了激活系统应检测与前车的距离并调整车速以避免碰撞的要求，包括最小跟车距离的计算公式 `d_min = v_ALKS * t_front`，并提供了不同车速下的最小时间间隔和最小跟车距离表格。对于表格中未列出的速度值，应采用线性插值法。此外，规定当前速度低于2米/秒时，M1、N1类车的最小跟车距离不得小于2米，M2、M3、N2、N3类车不得小于2.4米。
 - **5.2.5.2**: 规定了激活系统应避免与切入车辆的碰撞，需满足特定条件，并给出了计算切入时间(TTCLaneIntrusion)的公式。
 - **5.3.4**: 车辆应实施一个指示紧急制动的逻辑信号，具体规定参照UN Regulation No. 13-H或13（视情况而定）。
    - **感知要求 (第7.1条)**:
 - 规定了ALKS车辆应配备感知系统，至少能确定驾驶环境（如前方道路几何形状、车道标线）和交通动态，覆盖范围包括自车车道全宽、紧邻左右车道的全宽（直至前向探测范围极限），以及车辆或列车组合的全长（直至横向探测范围极限）。
 - **7.1.2**: 制造商应声明横向探测范围，该范围应足以覆盖车辆或列车组合紧邻左侧和右侧车道的全宽。技术服务机构应在附件5的相关测试中验证车辆感知系统能检测到车辆。
 - **7.1.5**: 规定了第7.1条及其子条款的符合性应向技术服务机构证明，并根据附件5的相关测试进行。如果ALKS可与车辆组合（如挂车）一起运行，制造商应在型式批准时向技术服务机构证明所实施的策略，以确保感知能力始终足以应对所连接挂车的长度。
    - **数据存储系统 (第8.4.3条)**:
 - **8.4.3.1**: 对于M1和N1类车辆，第8.3.1条所列数据元素即使在遭受UN法规No. 94、95或137（如适用）设定的严重程度级别的撞击后也应可检索。
 - **8.4.3.2**: 对于M2、M3、N2和N3类车辆，第8.3.1条所列数据元素在撞击后也应可检索。为证明该能力，需满足特定要求（如通过机械冲击测试或结构完整性证明）。
 - **8.4.3.3**: 如果车载主电源不可用，仍应能按照国家和地区法律的要求检索DSSAD上记录的所有数据。
- **关联文件**: 本文件仅为文档工具。具有真实性和法律约束力的文本是: ECE/TRANS/WP.29/2021/143/Rev.1。引用了UN Regulation No. 13, 13-H, 94, 95, 100, 137以及《车辆结构统一决议》(R.E.3.)。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 1 个
> - 公式 1 个
> - 图像 0 个
> - 全文 Markdown 9,638 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 1 个）

#### 表 1 (page 2)
**minimum time gap in seconds between the ALKS vehicle and a leading vehicle in front as per the table below: **

<table><tr><td colspan="2"></td><td colspan="2">Minimum time gap Minimum M1/N1</td><td colspan="2">Minimum time gap following distance M/M3//N/N3</td><td colspan="2">Minimum following distance M/M3//N/N3</td></tr><tr><td>Present speed of the ALKS vehicle</td><td></td><td></td><td>M1/N1</td><td></td><td></td><td></td></tr><tr><td>(km/h)</td><td>(m/s)</td><td>(s)</td><td>(m)</td><td></td><td>(s)</td><td>(m)</td></tr><tr><td>7.2</td><td>2.0</td><td>1.0</td><td>2.0</td><td></td><td>1.2</td><td>2.4</td></tr><tr><td>10</td><td>2.78</td><td>1.1</td><td>3.1 6.7</td><td></td><td>1.4</td><td>3.9</td></tr><tr><td>20</td><td>5.56</td><td>1.2</td><td>10.8</td><td></td><td>1.6</td><td>8.9</td></tr><tr><td>30</td><td>8.33</td><td>1.3</td><td>15.6</td><td></td><td>1.8</td><td>15.0</td></tr><tr><td>40</td><td>11.11</td><td>1.4 1.5</td><td>20.8</td><td></td><td>2.0</td><td>22.2</td></tr><tr><td>50 60</td><td>13.89 16.67</td><td>1.6</td><td>26.7</td><td></td><td>2.2 2.4</td><td>30.6 40.0</td></tr></table>

### 公式（取前 1 个）

**公式 1** (page 2):

$$
T T C L a n e I n t r u s i o n > v r e l / ( 2 \cdot \times 6 \mathrm { m } / \mathrm { s } ^ { 2 } ) + 0 . 3 5 s
$$

