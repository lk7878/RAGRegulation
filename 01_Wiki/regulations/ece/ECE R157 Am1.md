---
reg_id: ECE R157 Am1
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to Automated
  Lane Keeping Systems
type: type/amendment
status: active
entry_into_force_date: 2021-09-30
standard_body: UNECE
source_file: R157am1e.pdf
source_page_count: 57
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\157\R157am1e.pdf
publication_date: 2022-01-13
verified_by: deepseek-v3
cross_check_overall_confidence: medium
reg_id_conf: low
cross_check_flags:
- field: reg_id
  status: normalized
  extracted: ECE R157 Am1
  original: ECE/TRANS/505/Rev.3/Add.156/Amend.1 (UN Regulation No. 157 Amendment 1)
  note: '[Auto-reclassified] Same reg_id after normalization (was: ''ECE R157 Am1''
    vs ''ECE/TRANS/505/Rev.3/Add.156/Amend.1 (UN Regulation No. 157 Amendment 1)'')'
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及新车型的实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未明确提及在用车型的实施日期。
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
stage2_reclassified:
- reg_id
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: 02c606738c167b7c
_mineru_outputs_dir: outputs/02c606738c167b7c
_mineru_blocks:
  tables: 8
  formulas: 0
  images: 8
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 157 - Automated Lane Keeping Systems (ALKS)

## 法规概述
本法规（UN R157）旨在建立关于**自动车道保持系统（ALKS）**车辆型式批准的统一规定。ALKS可在无需驾驶员进一步指令的情况下，长时间控制车辆的横向和纵向运动。这是针对自动驾驶系统的首个法规步骤，适用于最高运行速度不超过60 km/h的M1类乘用车。

## 核心定义
*   **自动车道保持系统（ALKS）**：由驾驶员激活，在车速不超过60 km/h时，通过控制车辆的横向和纵向运动，使车辆在其车道内行驶，且无需驾驶员进一步输入的系统。
*   **动态驾驶任务（DDT）**：车辆所有纵向和横向运动的控制和执行。
*   **接管请求（Transition Demand）**：系统将DDT从系统（自动控制）转移给人类驾驶员（手动控制）的逻辑和直观程序。
*   **最小风险 manoeuvre（MRM）**：在驾驶员未响应接管请求或发生严重ALKS/车辆故障时，由系统自动执行的、旨在最小化交通风险的程序。
*   **紧急 manoeuvre（EM）**：在车辆面临即将发生的碰撞风险时，由系统执行的、旨在避免或减轻碰撞的 manoeuvre。
*   **数据存储系统（DSSAD）**：用于确定ALKS与人类驾驶员之间交互的系统。

## 主要技术要求
### 1. 系统安全与故障安全响应（第5条）
*   **一般要求**：激活的系统应执行DDT，管理所有情况（包括故障），且不得对乘员或其他道路使用者造成不合理风险。应避免可合理预见和预防的碰撞。系统需遵守运营国的交通规则。
*   **动态驾驶任务**：
    *   将车辆保持在行驶车道内。
    *   检测前方和侧方车辆，并相应调整车速和/或横向位置。
    *   控制车速，最高运行速度不超过60 km/h。
    *   根据基础设施和环境条件（如弯道半径、恶劣天气）调整车速。
    *   与前车保持最小跟车距离（计算公式基于当前速度和最小时间间隔）。
    *   能够完全停止以避免与静止车辆、道路使用者或受阻车道的碰撞。
    *   在特定条件下（如前方车辆减速、车辆切入、行人横穿），应自动执行适当操作以避免碰撞。
*   **紧急 manoeuvre**：在即将发生碰撞风险时执行，可包括全力制动和/或自动规避 manoeuvre。
*   **接管请求与过渡阶段操作**：系统应识别所有需要将控制权交还给驾驶员的情况，并发出接管请求。在过渡阶段，系统应继续运行。
*   **最小风险 manoeuvre**：在驾驶员未响应接管请求或发生严重故障时启动，旨在将车辆减速至停止（目标减速度不大于4.0 m/s²），并激活危险警告灯。

### 2. 人机界面/驾驶员信息（第6条）
*   **驾驶员状态识别系统**：系统必须包含驾驶员状态识别系统，用于检测驾驶员是否在驾驶位置、安全带是否系好以及驾驶员是否可用以接管驾驶任务。
*   **激活与解除**：系统必须配备专用的激活和解除手段。默认状态为关闭。激活需满足一系列条件（如驾驶员在位且可用、系统自检正常、环境条件允许等）。
*   **系统覆盖**：驾驶员对转向、制动或加速控制的输入可以覆盖系统的控制，但系统在检测到即将发生的碰撞风险时可以减少或抑制驾驶员的输入。
*   **驾驶员信息**：必须向驾驶员清晰指示系统状态、故障、接管请求、最小风险 manoeuvre 和紧急 manoeuvre。光学信号应足够醒目，声音信号应响亮清晰。

### 3. 目标与事件检测及响应（OEDR）（第7条）
*   **感知要求**：ALKS车辆应配备感知系统，至少能够确定驾驶环境（如前方道路几何形状、车道标线）和交通动态。
*   **前向探测范围**：制造商声明的探测范围至少为46米（从车辆最前端测量）。
*   **侧向探测范围**：声明的范围应足以覆盖车辆紧邻左侧和右侧车道的全宽。

### 4. 自动驾驶数据存储系统（DSSAD）（第8条）
*   **安装**：每辆配备ALKS的车辆都应安装符合要求的DSSAD。
*   **记录事件**：DSSAD至少应记录系统激活、解除、接管请求、紧急 manoeuvre、最小风险 manoeuvre、严重故障等事件。
*   **数据元素**：对于每个事件，应记录事件标志、原因、日期、时间戳以及相关的软件标识号（R157 SWIN）。
*   **数据可用性与保护**：数据应可通过标准接口（如OBD端口）读取，并具有足够的防篡改保护。

### 5. 网络安全与软件更新（第9条）
*   **网络安全**：系统的有效性不得受到网络攻击、网络威胁和漏洞的不利影响。需通过符合UN R155来证明。
*   **软件更新**：如果系统允许软件更新，更新程序和流程的有效性需通过符合UN R156来证明。

## 批准与符合性
*   **型式批准**：车辆制造商或其授权代表提交申请，并附上所需文件（包括车辆描述、ALKS设计文档包等）。提交代表性车辆进行测试。
*   **批准标记**：获得批准的车辆应粘贴符合附录2规定的国际批准标记。
*   **生产一致性**：已批准的车辆应按照本法规的要求进行制造。批准机构可每两年进行一次生产一致性检查。
*   **车辆类型修改与批准扩展**：对已批准车辆类型的任何修改都应通知批准机构，机构将决定是授予新批准还是进行修订/扩展。

## 附录
*   **附录1**：通信（批准申请表及信息文件格式）。
*   **附录2**：批准标记的排列。
*   **附录3**：ALKS交通干扰关键场景指南（提供用于定义ALKS应避免碰撞条件的仿真程序和驾驶员模型）。
*   **附录4**：适用于ALKS功能和操作安全方面的特殊要求（规定了制造商需提供的文档包、安全概念及Type Approval Authority的评估流程）。
*   **附录5**：ALKS测试规范（规定了具体的测试要求）。
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 9 个
> - 公式 0 个
> - 图像 27 个
> - 全文 Markdown 125,869 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 9 个）

#### 表 1 (page 7)
<table><tr><td>Present speed of the ALKS vehicle</td><td>Minimum time gap</td><td>Minimum following distance</td></tr><tr><td>(km/h) (m/s)</td><td>(s)</td><td>(m)</td></tr><tr><td>7.2 2.0</td><td>1.0</td><td>2.0</td></tr><tr><td>10 2.78</td><td>1.1</td><td>3.1</td></tr><tr><td>20 5.56</td><td>1.2</td><td>6.7</td></tr><tr><td>30 8.33</td><td>1.3</td><td>10.8</td></tr><tr><td>40</td><td>11.11 1.4</td><td>15.6</td></tr><tr><td>50</td><td>13.89 1.5</td><td>20.8</td></tr><tr><td>60</td><td>16.67 1.6</td><td>26.7</td></tr></table>

#### 表 2 (page 25)
<table><tr><td>Country</td><td>Assessed</td><td>Comments on any restrictions</td></tr><tr><td>E 1 Germany</td><td>Yes/No</td><td></td></tr><tr><td>E 2 France</td><td></td><td></td></tr><tr><td>E 3 Italy</td><td></td><td></td></tr><tr><td>E 4 Netherlands</td><td></td><td></td></tr><tr><td>E 5 Sweden</td><td></td><td></td></tr><tr><td>E 6 Belgium</td><td></td><td></td></tr><tr><td>E 7 Hungary</td><td></td><td></td></tr><tr><td>E 8 Czech Republic</td><td></td><td></td></tr><tr><td>E 9 Spain</td><td></td><td></td></tr><tr><td>E 10 Serbia</td><td></td><td></td></tr><tr><td>E 11 United Kingdom</td><td></td><td></td></tr><tr><td>E 12 Austria</td><td></td><td></td></tr><tr><td>E 13 Luxembourg</td><td></td><td></td></tr><tr><td>E 14 Switzerland</td><td></td><td></td></tr><tr><td>E 16 Norway</td><td></td><td></td></tr><tr><td>E 17 Finland</td><td></td><td></td></tr><tr><td>E 18 Denmark</td><td></td><td></td></tr><tr><td>E 19 Romania</td><td></td><td></td></tr><tr><td>E 20 Poland</td><td></td><td></td></tr><tr><td>E 21 Portugal</td><td></td><td></td></tr><tr><td>E 22 Russian Federation</td><td></td><td></td></tr><tr><td>E 23 Greece</td><td></td><td></td></tr><tr><td>E 24 Ireland</td><td></td><td></td></tr><tr><td>E 25 Croatia</td><td></td><td></td></tr><tr><td>E 26 Slovenia</td><td></td><td></td></tr><tr><td>E 27 Slovakia</td><td></td><td></td></tr><tr><td>E 28 Belarus</td><td></td><td></td></tr></table>

#### 表 3 (page 26)
<table><tr><td>Country</td><td>Assessed</td><td>Comments on any restrictions</td></tr><tr><td>E 29 Estonia</td><td></td><td></td></tr><tr><td>E 30 Republic of Moldova</td><td></td><td></td></tr><tr><td>E 31 Bosnia and Herzegovina</td><td></td><td></td></tr><tr><td>E 32 Latvia</td><td></td><td></td></tr><tr><td>E 34 Bulgaria</td><td></td><td></td></tr><tr><td>E 35 Kazakhstan</td><td></td><td></td></tr><tr><td>E 36 Lithuania</td><td></td><td></td></tr><tr><td>E 37 Turkey</td><td></td><td></td></tr><tr><td>E 39 Azerbaijan</td><td></td><td></td></tr><tr><td>E 40 North Macedonia</td><td></td><td></td></tr><tr><td>E 43 Japan</td><td></td><td></td></tr><tr><td>E 45 Australia</td><td></td><td></td></tr><tr><td>E 46 Ukraine</td><td></td><td></td></tr><tr><td>E 47 South Africa</td><td></td><td></td></tr><tr><td>E 48 New Zealand</td><td></td><td></td></tr><tr><td>E 49 Cyprus</td><td></td><td></td></tr><tr><td>E 50 Malta</td><td></td><td></td></tr><tr><td>E 51 Republic of Korea</td><td></td><td></td></tr><tr><td>E 52 Malaysia</td><td></td><td></td></tr><tr><td>E 53 Thailand</td><td></td><td></td></tr><tr><td>E 54 Albania</td><td></td><td></td></tr><tr><td>E 55 Armenia</td><td></td><td></td></tr><tr><td>E 56 Montenegro</td><td></td><td></td></tr><tr><td>E 57 San Marino</td><td></td><td></td></tr><tr><td>E 58 Tunisia</td><td></td><td></td></tr><tr><td>E 60 Georgia</td><td></td><td></td></tr><tr><td>E 62 Egypt</td><td></td><td></td></tr><tr><td>E 63 Nigeria</td><td></td><td></td></tr><tr><td>E 64 Pakistan</td><td></td><td></td></tr></table>

#### 表 4 (page 29)
**Table 1 Performance model factors for vehicles **

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Factors</td></tr><tr><td rowspan=2 colspan=1>Risk perception point</td><td rowspan=1 colspan=1>Lane change (cutting in,cutting out)</td><td rowspan=1 colspan=1>Deviation of the center of a vehicle over 0.375mfrom the center of the driving lane(derived from research by Japan)</td></tr><tr><td rowspan=1 colspan=1>Deceleration</td><td rowspan=1 colspan=1>Deceleration ratio of preceding vehicle andfollowing distance of ego vehicle</td></tr><tr><td rowspan=1 colspan=2>Risk evaluation time</td><td rowspan=1 colspan=1>0.4 seconds(from research by Japan)</td></tr><tr><td rowspan=1 colspan=2>Time duration from having finished perception untilstarting deceleration</td><td rowspan=1 colspan=1>0.75 seconds(common data in Japan)</td></tr><tr><td rowspan=1 colspan=2>Jerking time to full deceleration (road friction 1.0)</td><td rowspan=1 colspan=1>0.6 seconds to 0.774G(from experiments by NHTSA and Japan)</td></tr><tr><td rowspan=1 colspan=2>Jerking time to full deceleration (after full wrap of egovehicle and cut-in vehicle, road friction 1.0)</td><td rowspan=1 colspan=1>0.6 seconds to 0.85G(derived from UN Regulation No. 152 onAEBS)</td></tr></table>

#### 表 5 (page 31)
**Table 2 Additional parameters **

<table><tr><td colspan="1" rowspan="2">Operatingconditions</td><td colspan="1" rowspan="1">Roadway</td><td colspan="1" rowspan="1">Number of lanes = The number of parallel and adjacentlanes in the same direction of travelLane Width= The width of each laneRoadway grade = The grade of the roadway in the areaof testRoadway condition = the condition of the roadway(dry,wet, icy, snow,new, worn) including coefficient offrictionLane markings = the type, colour, width, visibility oflane markings</td></tr><tr><td colspan="1" rowspan="1">Environmentalconditions</td><td colspan="1" rowspan="1">Lighting conditions = The amount of light anddirection (ie,day, night, sunny,cloudy)Weather conditions = The amount, type and intensityof wind,rain, snow etc.</td></tr><tr><td colspan="1" rowspan="6">Initialcondition</td><td colspan="1" rowspan="3">Initial velocity</td><td colspan="1" rowspan="1">Ve0 = Ego vehicle</td></tr><tr><td colspan="1" rowspan="1">Vo0 =Leading vehicle in lane or in adjacent lane</td></tr><tr><td colspan="1" rowspan="1">Vf0 = Vehicle in front of leading vehicle in lane</td></tr><tr><td colspan="1" rowspan="3">Initial distance</td><td colspan="1" rowspan="1">dx0 = Distance in Longitudinal direction between thefront end of the ego vehicle and the rear end of theleading vehicle in ego vehicle's lane or in adjacent lane</td></tr><tr><td colspan="1" rowspan="1">dyO = Inside Lateral distance between outside edge lineof ego vehicle in parallel to the vehicle's medianlongitudinal plane within lanes and outside edge line ofleading vehicle in parallel to the vehicle's medianlongitudinal plane in adjacent lines.</td></tr><tr><td colspan="1" rowspan="1">dy0_f= Inside Lateral distance between outside edgeline of leading vehicle in parallel to the vehicle's median</td></tr><tr><td colspan="1" rowspan="5"></td><td colspan="1" rowspan="5"></td><td colspan="1" rowspan="1">longitudinal plane within lanes and outside edge line ofvehicle in front of the leading vehicle in parallel to thevehicle's median longitudinal plane in adjacent lines.</td></tr><tr><td colspan="1" rowspan="1">dx0_f = Distance in longitudinal direction between frontend of leading vehicle and rear end of vehicle in front ofleading vehicle</td></tr><tr><td colspan="1" rowspan="1">dfy = Width of vehicle in front of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">doy = Width of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">dox = Length of the leading vehicle</td></tr><tr><td colspan="1" rowspan="3">Vehiclemotion</td><td colspan="1" rowspan="1">Lateral motion</td><td colspan="1" rowspan="1">Vy =Leading vehicle lateral velocity</td></tr><tr><td colspan="1" rowspan="2">Deceleration</td><td colspan="1" rowspan="1">Gx_max = Maximum deceleration of the leadingvehicle in G</td></tr><tr><td colspan="1" rowspan="1">dG/dt = Deceleration rate (Jerk) of the leading vehicle</td></tr></table>

#### 表 6 (page 32)
#### 表 7 (page 32)
**Figure 5 Visualisation **

<table><tr><td>Cut in</td><td>Ego dxo 口 VeO dyo↑ VoO</td><td></td></tr><tr><td></td><td>dx0 回 dx0 口 VeO VfO</td><td></td></tr><tr><td></td><td>Ego dx0 Vo0 口 VeO Gx_max Challenging dG/dt vehicle</td><td></td></tr></table>

#### 表 8 (page 33)
<table><tr><td rowspan="3">Initial condition</td><td rowspan="2">Initial velocity</td><td>VeO Ego vehicle velocity</td></tr><tr><td>Ve0-Vo0 Relative velocity</td></tr><tr><td rowspan="2">Initial distance</td><td>dyo</td><td>Latteral distancex</td></tr><tr><td>dx0</td><td>Longitudinal distance</td></tr><tr><td>Vehicle motion</td><td>Lateral motion</td><td>Vy</td><td>Lateral velocity</td></tr></table>

#### 表 9 (page 44)
**(Data sheet image) **

<table><tr><td>Ego dx0 O Ve0</td><td rowspan="3">Initial condition</td><td colspan="2">Initial Ve0 Ego vehicle velocity velocity</td></tr><tr><td rowspan="2">VoO 门 ← Gx_max Challenging</td><td rowspan="2">Vo0</td><td rowspan="2">Leading vehicle velocity1</td></tr><tr><td rowspan="3">dG/dt vehicle</td></tr><tr><td rowspan="2">Initial distance Vehicle Decelera</td><td rowspan="2">dx0</td><td>Longitudinal distance²</td></tr><tr><td>Maximum deceleration G</td></tr><tr><td></td><td rowspan="2">motion tion</td><td rowspan="2">dG/dt</td><td>Gx_max</td></tr><tr><td>Deceleration rate3</td></tr></table>

### 图像（取前 8 张）

![图 page 11](../_mineru_assets/ECE R157 Am1/68766500118e920cf7f48dc3107dc251baeab1ded7c7fb7cd32c0db86b8f6cc6.jpg)  

![Example1. ](../_mineru_assets/ECE R157 Am1/066f8c1798c3a633c12cff2755c4718401bf1c8a0e166765b2050fdd11b0a635.jpg)  
*Example1. * (page 15)

![Example2. ](../_mineru_assets/ECE R157 Am1/a4e78af1b164ab94d04b9971f216e5a9af1b3298939e3317ab5f3ce0b9cdfd64.jpg)  
*Example2. * (page 15)

![图 page 27](../_mineru_assets/ECE R157 Am1/f4e685152c1aae93d886fbb92598a1ea47d2d76ec6ab93784babc895a8ecde49.jpg)  

![Figure 1 Skilled human performance model ](../_mineru_assets/ECE R157 Am1/01c889860c7ae8788b6e072a6cc4df11cd7989150956d1b3d7ac6550fc31cb32.jpg)  
*Figure 1 Skilled human performance model * (page 29)

![Figure 2 Driver model for the cut-in scenario ](../_mineru_assets/ECE R157 Am1/a32f3f6e9c9fd15015128f48dd9dd689d9824e184de6055468943a1fb76eca13.jpg)  
*Figure 2 Driver model for the cut-in scenario * (page 30)

![Figure 3 Cut in scenario ](../_mineru_assets/ECE R157 Am1/bdb2cf5d58703717174bd7f19bca2772d88dbcbb2eec6204fefb2676a5b12bbb.jpg)  
*Figure 3 Cut in scenario * (page 30)

![Figure 4 Deceleration scenario ](../_mineru_assets/ECE R157 Am1/bb1b1fbe1936158b9777200e1a18c77938fb76e3e7a5243b48d3cf3839b999d1.jpg)  
*Figure 4 Deceleration scenario * (page 31)

