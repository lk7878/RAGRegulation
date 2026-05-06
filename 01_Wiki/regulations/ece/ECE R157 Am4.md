---
reg_id: ECE R157 Am4
region: ece
title: Uniform provisions concerning the approval of vehicles with regard to Automated
  Lane Keeping Systems
type: type/amendment
status: active
publication_date: 2023-03-03
implementation_date_new_vehicle: 2023-01-04
amendments: 01 series of amendments
authority: UNECE
source_file: R157am4e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\157\R157am4e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
reg_id_conf: low
cross_check_flags:
- field: reg_id
  status: normalized
  extracted: ECE R157 Am4
  original: UN Regulation No. 157 (Amendment 4)
  note: '[Auto-reclassified] Same reg_id after normalization (was: ''ECE R157 Am4''
    vs ''UN Regulation No. 157 (Amendment 4)'')'
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 中均未明确提及 "standard_body" 字段。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及 "implementation_date_in_use"。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 中未提及 "equivalent_to" 信息。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 中未提及 "supersedes" 信息。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A 中未提取具体的技术要求限值，B 中虽有技术描述但未提供结构化限值。
stage2_reclassified:
- reg_id
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: eb32d3002d7795a4
_mineru_outputs_dir: outputs/eb32d3002d7795a4
_mineru_blocks:
  tables: 9
  formulas: 8
  images: 8
_mineru_merged_at: '2026-04-25'
---

# UN Regulation No. 157 - Automated Lane Keeping Systems (ALKS)

## 法规概述
本法规旨在建立关于车辆自动车道保持系统（ALKS）型式批准的统一规定。ALKS可在无需驾驶员进一步指令的情况下，长时间控制车辆的横向和纵向运动。这是针对自动驾驶系统的首个法规步骤，包含了适用于型式批准的管理规定、技术要求、审核和报告规定以及测试规定。

## 适用范围与目的
1.1. 本法规适用于M类和N1类车辆关于其自动车道保持系统的型式批准。

## 关键定义
- **自动车道保持系统 (ALKS)**：由驾驶员激活的系统，通过控制车辆的横向和纵向运动，在不超过130公里/小时的速度下，使车辆保持在车道内行驶，无需驾驶员进一步输入。
- **过渡请求**：将动态驾驶任务从系统（自动控制）转移给人类驾驶员（手动控制）的逻辑和直观程序。
- **最小风险操作 (MRM)**：在驾驶员未响应过渡请求或发生严重ALKS或车辆故障时，由系统自动执行的旨在最小化交通风险的程序。
- **紧急操作 (EM)**：在车辆面临即将发生的碰撞风险时，由系统执行的旨在避免或减轻碰撞的操作。
- **动态驾驶任务 (DDT)**：车辆所有纵向和横向运动的控制和执行。
- **自动驾驶数据存储系统 (DSSAD)**：用于确定ALKS与人类驾驶员之间交互的系统。

## 系统安全与故障安全响应 (第5条)
### 一般要求
- 激活的系统应执行DDT，管理所有情况（包括故障），且不得对车辆乘员或其他道路使用者造成不合理风险。
- 激活的系统应遵守运营国与DDT相关的交通规则。
- 如果驾驶员在过渡阶段未能恢复对DDT的控制，系统应执行最小风险操作。
- 系统应进行自检以检测故障并确认系统性能。
- 制造商应采取防范措施，防止驾驶员可合理预见的误用和系统篡改。
- 当系统无法再满足本法规要求时，应无法激活系统。

### 动态驾驶任务 (DDT)
- 激活的系统应将车辆保持在行驶车道内，并确保车辆不会无意中穿越任何车道标线。
- 在特定条件下（如执行车道变更程序、紧急操作期间进行规避性车道穿越、为应急和执法车辆形成通道、为绕行部分阻塞车道的障碍物而部分进入相邻车道），允许有意识地穿越车道标线。
- 激活的系统应控制车速，根据基础设施和环境条件调整车速，并调整与前车的安全跟车距离以避免碰撞。
- 激活的系统应能够将车辆完全停在前方静止车辆、静止道路使用者或被阻塞的车道后面以避免碰撞。
- 激活的系统应检测碰撞风险（特别是与前方或侧方其他道路使用者），并自动执行适当操作以最小化对车辆乘员和其他道路使用者安全的风险。
- 对于车道变更程序，系统必须确保不会对车辆乘员和其他道路使用者的安全造成不合理风险，且变更过程可预测且易于其他车辆或道路使用者管理。

### 紧急操作
- 在发生即将碰撞风险时应执行紧急操作。
- 该操作应在必要时使车辆减速至其最大制动性能，并可在适当时执行自动规避操作。
- 紧急操作期间，除非系统能够满足特定规定，否则ALKS车辆不应穿越车道标线。

### 过渡请求和过渡阶段的系统操作
- 激活的系统应识别所有需要将控制权交还给驾驶员的情况。
- 过渡请求的启动应提供足够时间以安全过渡到手动驾驶。
- 在过渡阶段，系统应继续运行，并可降低车速以确保安全操作，但除非情况需要（例如车辆或障碍物阻塞路径），否则不应使车辆停止。
- 如果驾驶员未通过停用系统来响应过渡请求，则应在过渡请求开始后最早10秒启动最小风险操作。在发生严重ALKS或严重车辆故障时，可立即启动最小风险操作。

### 最小风险操作
- 最小风险操作应使车辆停止，除非驾驶员在操作期间停用系统。
- 停止应在目标停车区域进行，该区域被认为是在给定情况下可实现的最大风险最小化区域。
- 最小风险操作期间，车辆应以目标减速度不大于4.0 m/s²的方式减速。
- 最小风险操作结束后，系统应被停用，危险警告灯应保持激活状态，除非手动停用，且车辆在停止后不应在没有手动输入的情况下移动。

## 人机界面/操作员信息 (第6条)
### 驾驶员可用性识别系统
- 系统应包括驾驶员可用性识别系统，用于检测驾驶员是否在驾驶位置、驾驶员安全带是否系好以及驾驶员是否可用以接管驾驶任务。
- 当检测到驾驶员离开座位超过一秒或驾驶员安全带未系时，应启动过渡请求。
- 系统应通过监控驾驶员来检测驾驶员是否可用并处于适当的驾驶位置以响应过渡请求。
- 当ALKS激活时，驾驶员可通过车载显示屏进行的"驾驶以外的其他活动"，应在系统发出过渡请求或系统停用（以先发生者为准）时自动暂停。

### 激活、停用和驾驶员输入
- 车辆应配备供驾驶员激活（激活模式）和停用（关闭模式）系统的专用装置。
- 系统的默认状态应为每个新发动机启动/运行周期开始时的关闭模式。
- 系统仅在驾驶员有意识的操作且满足所有条件（如驾驶员在驾驶座且系好安全带、驾驶员可用、无影响ALKS安全运行或功能的故障、DSSAD可运行、环境和基础设施条件允许运行等）时才变为激活状态。
- 应可通过驾驶员使用与激活系统相同的装置进行有意识的操作来手动停用系统。
- 系统不得因除特定驾驶员输入（如通过驾驶控制输入、在持续的过渡请求或最小风险操作期间、在持续的紧急操作期间、在严重车辆故障或严重ALKS故障情况下）之外的任何驾驶员输入而停用。

### 系统覆盖
- 驾驶员对转向控制的输入应在超过旨在防止无意覆盖的合理阈值时覆盖系统的横向控制功能。
- 导致比系统诱导减速度更高减速度或通过任何制动系统使车辆保持静止的驾驶员对制动控制的输入，应覆盖系统的纵向控制功能。
- 驾驶员对加速器控制的输入可以覆盖系统的纵向控制功能，但此类输入不得导致系统不再满足本法规的要求。
- 当驾驶员对加速器或制动控制的输入超过旨在防止无意输入的合理阈值时，应立即启动过渡请求。
- 驾驶员对方向指示器的任何激活应在输入超过旨在防止无意激活的合理阈值时启动过渡请求。

### 驾驶员信息
- 应向驾驶员指示以下信息：系统状态、任何影响系统满足本法规要求的故障（至少通过光信号）、过渡请求（至少通过光信号以及声学和/或触觉警告信号）、最小风险操作（至少通过光信号以及声学和/或触觉警告信号）、紧急操作（通过光信号），以及如果ALKS能够执行LCP，则通过至少光信号指示LCP。
- 系统状态应在激活时通过专用光信号显示给驾驶员，并在停用时通过至少光警告信号指示。
- 在过渡阶段和最小风险操作期间，系统应以直观且明确的方式指示驾驶员接管车辆的手动控制。

## 物体和事件检测与响应 (OEDR) (第7条)
### 感知要求
- ALKS车辆应配备感知系统，使其至少能够确定驾驶环境（例如前方道路几何形状、车道标线）和交通动态。
- 如果ALKS能够执行LCP，则感知系统应额外能够确定至少从ALKS车辆中心线向两侧各9米宽度内，从前向探测范围极限到后向探测范围极限的交通动态。

### 前向探测范围
- 制造商应声明从前车辆最前点测量的前向探测范围。对于60公里/小时的指定最高速度，声明值应至少为46米。
- 只有当声明的前向探测范围满足基于5m/s²减速度的相应最小值时，制造商才能声明高于60公里/小时的指定最高速度。

### 侧向探测范围
- 制造商应声明侧向探测范围。声明范围应足以覆盖车辆左侧和右侧紧邻车道的全宽。
- 如果ALKS能够执行LCP，制造商还应声明侧向探测范围，该范围应足以覆盖从ALKS车辆中心线向ALKS执行LCP的一侧至少9米的区域。

### 后向探测范围
- 如果ALKS能够执行LCP，则适用本段要求。
- 制造商应声明从车辆最后点测量的后向探测范围。声明范围应足以覆盖从ALKS车辆中心线向ALKS执行LCP的一侧至少9米的区域。

### 方向指示器状态检测区域
- 制造商应声明系统能够评估其他车辆方向指示器状态的区域（如果有）。这应考虑系统运营国在PVPA内通常运行的车辆上方向指示器的不同位置。

## 自动驾驶数据存储系统 (第8条)
### 配备
- 每辆配备ALKS的车辆应配备符合下述要求的DSSAD。

### 记录的事件
- 每辆配备DSSAD的车辆至少应在系统激活时记录以下每个事件的条目：系统激活、系统停用、系统发出的过渡请求、驾驶员输入的减少或抑制、紧急操作开始、紧急操作结束、事件数据记录器触发输入、涉及检测到的碰撞、系统启动最小风险操作、严重ALKS故障、严重车辆故障、车道变更程序开始、车道变更程序结束、车道变更程序中止、有意识车道穿越开始、有意识车道穿越结束。

### 数据元素
- 对于第8.2条中列出的每个事件，DSSAD应至少以清晰可识别的方式记录以下数据元素：事件标志、事件原因（如适用）、日期、时间戳。
- 对于第8.2条中列出的每个事件，ALKS的R157 SWIN或与ALKS相关的软件版本（指示事件发生时存在的软件）应清晰可识别。

### 数据可用性
- DSSAD数据应根据国家和地区法律的要求提供。
- 一旦达到DSSAD的存储限制，应遵循先进先出程序覆盖现有数据，并遵守数据可用性的相关要求。
- 对于M1和N1类车辆，即使在发生UN法规第94、95或137号（如适用）设定的严重程度的碰撞后，也应能检索第8.3.1条中列出的数据元素。
- 如果车载主电源不可用，仍应能检索DSSAD上记录的所有数据（根据国家和地区法律要求）。
- DSSAD中存储的数据应易于通过电子通信接口以标准化方式读取，至少通过标准接口（OBD端口）。
- 对于配备符合UN法规第160号的EDR的车辆，应能通过标准接口（OBD端口）检索在"事件数据记录器触发输入"事件标志最后一次设置前至少30秒内记录的DSSAD数据元素（如第8.3.1(a)和8.3.1(b)条所述），以及UN法规第160号附件4中规定的数据元素（EDR数据）。

## 网络安全与软件更新 (第9条)
### 网络安全和网络安全管理体系
- 系统的有效性不得受到网络攻击、网络威胁和漏洞的不利影响。安全措施的有效性应通过符合UN法规第155号来证明。

### 软件更新和软件更新管理体系
- 如果系统允许软件更新，软件更新程序和流程的有效性应通过符合UN法规第156号来证明。

### 软件识别要求
- 车辆制造商应根据UN法规第156号（软件更新和软件更新管理体系）拥有有效的批准。
- 车辆制造商应在本法规的沟通表中提供以下信息：R157 SWIN；在R157 SWIN未保存在车辆上的情况下，如何读取R157 SWIN或软件版本。
- 车辆制造商可在本法规的沟通表中提供相关参数列表，以便识别哪些车辆可以使用由R157 SWIN表示的软件进行更新。

## 过渡性规定 (第15条)
- 自01系列修正案正式生效之日起，任何适用本法规的缔约方不得拒绝根据经01系列修正案修订的本法规授予或接受型式批准。
- 自2023年9月1日起，适用本法规的缔约方没有义务接受在2023年9月1日之后首次颁发的本法规原始版本的型式批准。
- 直至2027年9月1日，适用本法规的缔约方应接受在2023年9月1日之前首次颁发的本法规原始版本的型式批准。
- 自2027年9月1日起，适用本法规的缔约方没有义务接受根据本法规先前系列修正案颁发的型式批准。
- 适用本法规的缔约方可根据本法规的任何先前系列修正案授予型式批准。
- 适用本法规的缔约方应继续根据本法规的任何先前系列修正案对现有批准进行扩展。

## 附件
- **附件1**: 沟通（包括附录1和2）
- **附件2**: 批准标记的布置
- **附件3**: ALKS交通干扰关键场景指南
- **附件4**: 适用于自动车道保持系统功能和安全方面的特殊要求
- **附件5**: ALKS车辆赛道测试规范
- **附件6**: ALKS公共道路测试规范
---

## 原文参考（MinerU 云解析 · 2026-04-25）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 15 个
> - 公式 8 个
> - 图像 47 个
> - 全文 Markdown 204,659 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 10 个）

#### 表 1 (page 10)
**minimum time gap in seconds between the ALKS vehicle and a leading vehicle in front as per the table below: **

<table><tr><td colspan="2"></td><td colspan="2">Minimum time gap Minimum M1/N1</td><td colspan="2">Minimum time gap following distance M/M3//N/N3</td><td colspan="2">Minimum following distance</td></tr><tr><td>Present speed of the ALKS vehicle</td><td></td><td></td><td>M1/N1</td><td></td><td></td><td>M2/M3//N2/N3</td></tr><tr><td>(km/h)</td><td>(m/s)</td><td>(s)</td><td>(m)</td><td>(s)</td><td></td><td>(m)</td></tr><tr><td>7.2</td><td>2.0</td><td>1.0</td><td>2.0</td><td></td><td>1.2</td><td>2.4</td></tr><tr><td>10</td><td>2.78</td><td>1.1</td><td>3.1</td><td></td><td>1.4</td><td>3.9</td></tr><tr><td>20</td><td>5.56</td><td>1.2</td><td>6.7</td><td></td><td>1.6</td><td>8.9</td></tr><tr><td>30</td><td>8.33</td><td>1.3</td><td>10.8</td><td></td><td>1.8</td><td>15.0</td></tr><tr><td>40</td><td>11.11</td><td>1.4</td><td>15.6 20.8</td><td></td><td>2.0</td><td>22.2</td></tr><tr><td>50</td><td>13.89</td><td>1.5</td><td>26.7</td><td></td><td>2.2</td><td>30.6</td></tr><tr><td>60</td><td>16.67</td><td>1.6</td><td></td><td></td><td>2.4</td><td>40.0</td></tr></table>

#### 表 2 (page 24)
<table><tr><td></td><td>Minimum forward detection</td></tr><tr><td>Specified maximum speed /</td><td>range /</td></tr><tr><td>km/h</td><td>m</td></tr><tr><td>0...60</td><td>46</td></tr><tr><td>70</td><td>50</td></tr><tr><td>80</td><td>60</td></tr><tr><td>90</td><td>75</td></tr><tr><td>100</td><td>90</td></tr><tr><td>110</td><td>110</td></tr><tr><td>120</td><td>130</td></tr><tr><td>130</td><td>150</td></tr></table>

#### 表 3 (page 36)
<table><tr><td>Country</td><td>Assessed</td><td>Comments on any restrictions</td></tr><tr><td>E1 Germany</td><td>Yes/No**</td><td></td></tr><tr><td>E 2 France</td><td></td><td></td></tr><tr><td>E 3 Italy</td><td></td><td></td></tr><tr><td>E 4 Netherlands</td><td></td><td></td></tr><tr><td>E5 Sweden</td><td></td><td></td></tr><tr><td>E 6 Belgium</td><td></td><td></td></tr><tr><td>E 7 Hungary</td><td></td><td></td></tr><tr><td>E 8 Czech Republic</td><td></td><td></td></tr><tr><td>E 9 Spain</td><td></td><td></td></tr><tr><td>E 10 Serbia</td><td></td><td></td></tr><tr><td>E 11 United Kingdom</td><td></td><td></td></tr><tr><td>E 12 Austria</td><td></td><td></td></tr><tr><td>E 13 Luxembourg</td><td></td><td></td></tr><tr><td>E 14 Switzerland</td><td></td><td></td></tr><tr><td>E 16 Norway</td><td></td><td></td></tr><tr><td>E 17 Finland</td><td></td><td></td></tr><tr><td>E 18 Denmark</td><td></td><td></td></tr><tr><td>E 19 Romania</td><td></td><td></td></tr><tr><td>E 20 Poland</td><td></td><td></td></tr><tr><td>E 21 Portugal</td><td></td><td></td></tr><tr><td>E 22 Russian Federation</td><td></td><td></td></tr><tr><td>E 23 Greece</td><td></td><td></td></tr><tr><td>E 24 Ireland</td><td></td><td></td></tr><tr><td>E 25 Croatia</td><td></td><td></td></tr><tr><td>E 26 Slovenia</td><td></td><td></td></tr><tr><td>E 27 Slovakia</td><td></td><td></td></tr><tr><td>E 28 Belarus</td><td></td><td></td></tr></table>

#### 表 4 (page 37)
<table><tr><td>Country</td><td>Assessed</td><td>Comments on any restrictions</td><td></td></tr><tr><td>E 29 Estonia</td><td></td><td></td><td></td></tr><tr><td>E 30 Republic of Moldova</td><td></td><td></td><td></td></tr><tr><td>E 31 Bosnia and Herzegovina</td><td></td><td></td><td></td></tr><tr><td>E 32 Latvia</td><td></td><td></td><td></td></tr><tr><td>E 34 Bulgaria</td><td></td><td></td><td></td></tr><tr><td>E 35 Kazakhstan</td><td></td><td></td><td></td></tr><tr><td>E 36 Lithuania</td><td></td><td></td><td></td></tr><tr><td>E 37 Turkey</td><td></td><td></td><td></td></tr><tr><td>E 39 Azerbaijan</td><td></td><td></td><td></td></tr><tr><td>E 40 North Macedonia</td><td></td><td></td><td></td></tr><tr><td>E 43 Japan</td><td></td><td></td><td></td></tr><tr><td>E 45 Australia</td><td></td><td></td><td></td></tr><tr><td>E 46 Ukraine</td><td></td><td></td><td></td></tr><tr><td>E 47 South Africa</td><td></td><td></td><td></td></tr><tr><td>E 48 New Zealand</td><td></td><td></td><td></td></tr><tr><td>E 49 Cyprus</td><td></td><td></td><td></td></tr><tr><td>E 50 Malta</td><td></td><td></td><td></td></tr><tr><td>E 51 Republic of Korea</td><td></td><td></td><td></td></tr><tr><td>E 52 Malaysia</td><td></td><td></td><td></td></tr><tr><td>E 53 Thailand</td><td></td><td></td><td></td></tr><tr><td>E 54 Albania</td><td></td><td></td><td></td></tr><tr><td>E 55 Armenia</td><td></td><td></td><td></td></tr><tr><td>E 56 Montenegro</td><td></td><td></td><td></td></tr><tr><td>E 57 San Marino</td><td></td><td></td><td></td></tr><tr><td>E 58 Tunisia</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>E 60 Georgia</td><td></td><td></td><td></td></tr><tr><td>E 62 Egypt</td><td></td><td></td><td></td></tr><tr><td>E 63 Nigeria</td><td></td><td></td><td></td></tr><tr><td>E 64 Pakistan *</td><td></td><td></td><td></td></tr></table>

#### 表 5 (page 40)
**Table 1 Performance model factors for vehicles **

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Factors</td></tr><tr><td rowspan=2 colspan=1>Risk perception point</td><td rowspan=1 colspan=1>Lane change (cutting in,cutting out)</td><td rowspan=1 colspan=1>Deviation of the centre of a vehicle over 0.375mfrom the centre of the driving lane</td></tr><tr><td rowspan=1 colspan=1>Deceleration</td><td rowspan=1 colspan=1>Deceleration ratio of preceding vehicle andfollowing distance of ego vehicle</td></tr><tr><td rowspan=1 colspan=2>Risk evaluation time</td><td rowspan=1 colspan=1>0.4 seconds</td></tr><tr><td rowspan=1 colspan=2>Time duration from having finished perception until|O.75 secondsstarting deceleration</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2>Jerking time to full deceleration (road friction 1.0)</td><td rowspan=1 colspan=1>0.6 seconds to 0.774g</td></tr><tr><td rowspan=1 colspan=2> Jerking time to full deceleration (after full wrap of ego|O.6 seconds to 0.85gvehicle and cut-in vehicle, road friction 1.0)</td><td rowspan=1 colspan=1></td></tr></table>

#### 表 6 (page 42)
**Table 2 Additional parameters **

<table><tr><td colspan="1" rowspan="2">Operatingconditions</td><td colspan="1" rowspan="1">Roadway</td><td colspan="1" rowspan="1">Number of lanes = The number of parallel and adjacentlanes in the same direction of travelLane Width = The width of each laneRoadway grade = The grade of the roadway in the areaof testRoadway condition = the condition of the roadway (dry,wet, icy，snow，new，worn） including coefficient offrictionLane markings = the type,colour, width, visibility oflane markings</td></tr><tr><td colspan="1" rowspan="1">Environmentalconditions</td><td colspan="1" rowspan="1">Lighting conditions = The amount of light and direction(i.e., day, night, sunny, cloudy)Weather conditions = The amount, type and intensity ofwind, rain, snow etc.</td></tr><tr><td colspan="1" rowspan="10">Initialcondition</td><td colspan="1" rowspan="3">Initial velocity</td><td colspan="1" rowspan="1">Ve0 = Ego vehicle</td></tr><tr><td colspan="1" rowspan="1">Vo0 = Leading vehicle in lane or in adjacent lane</td></tr><tr><td colspan="1" rowspan="1">Vf0 = Vehicle in front of leading vehicle in lane</td></tr><tr><td colspan="1" rowspan="7">Initial distance</td><td colspan="1" rowspan="1">dx0 = Distance in Longitudinal direction between thefront end of the ego vehicle and the rear end of the leadingvehicle in ego vehicle's lane or in adjacent lane</td></tr><tr><td colspan="1" rowspan="1">dy0 = Inside Lateral distance between outside edge lineof ego vehicle in parallel to the vehicle's medianlongitudinal plane within lanes and outside edge line ofleading vehicle in parallel to the vehicle's medianlongitudinal plane in adjacent lines.</td></tr><tr><td colspan="1" rowspan="1">dy0_f= Inside Lateral distance between outside edge lineof leading vehicle in parallel to the vehicle's medianlongitudinal plane within lanes and outside edge line ofvehicle in front of the leading vehicle in parallel to thevehicle's median longitudinal plane in adjacent lines.</td></tr><tr><td colspan="1" rowspan="1">dx0_f = Distance in longitudinal direction between frontend of leading vehicle and rear end of vehicle in front ofleading vehicle</td></tr><tr><td colspan="1" rowspan="1">dfy = Width of vehicle in front of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">doy = Width of leading vehicle</td></tr><tr><td colspan="1" rowspan="1">dox = Length of the leading vehicle</td></tr><tr><td colspan="1" rowspan="2">Vehiclemotion</td><td colspan="1" rowspan="1">Lateral motion</td><td colspan="1" rowspan="1">Vy =Leading vehicle lateral velocity</td></tr><tr><td colspan="1" rowspan="1">Deceleration</td><td colspan="1" rowspan="1">Gx_max = Maximum deceleration of the leading vehicleing</td></tr><tr><td></td><td></td><td>dG/dt = Deceleration rate (Jerk) of the leading vehicle</td></tr><tr><td></td><td></td><td></td></tr></table>

#### 表 7 (page 43)
#### 表 8 (page 43)
**Figure 5 Visualisation **

<table><tr><td>Cut in</td><td>Ego Idxo ￥国 VeO dyot VoO Challenging vehicle</td><td></td></tr><tr><td></td><td>Ego VoO Challenging vehicle dx0 回 dx0 VeO VfO</td><td></td></tr><tr><td></td><td>Ego dx0 Vo0 C 口 VeO Gx_max Challenging dG/dt vehicle</td><td></td></tr></table>

#### 表 9 (page 43)
<table><tr><td rowspan=4 colspan=1>Initialcondition</td><td rowspan=2 colspan=1>Initialvelocity</td><td rowspan=1 colspan=1>Ve0      Ego vehicle velocity</td></tr><tr><td rowspan=1 colspan=1>Ve0-Vo0Relative velocity</td></tr><tr><td rowspan=2 colspan=1>Initialdistance</td><td rowspan=1 colspan=1>dyo      Latteral distancex</td></tr><tr><td rowspan=1 colspan=1>dx0      Longitudinal distance</td></tr><tr><td rowspan=1 colspan=1>Vehiclemotion</td><td rowspan=1 colspan=1>Lateralmotion</td><td rowspan=1 colspan=1>Vy        Lateral velocity</td></tr></table>

#### 表 10 (page 52)
<table><tr><td rowspan="4">Initial condition Initial</td><td rowspan="4">Initial, velocity</td><td colspan="2">Ve0</td><td>Ego vehicle velocity</td></tr><tr><td colspan="3">Vo0</td><td>Leading vehicle velocity1</td></tr><tr><td colspan="3">vfo</td><td>Vehicle in front of leading vehicle²</td></tr><tr><td colspan="3">dxo distance</td><td>Longitudinal distance³</td></tr><tr><td>Vehicle</td><td>Lateral</td><td colspan="3">dx0_f</td><td>Front of lead distance</td></tr><tr><td rowspan="2">motion</td><td>motion</td><td>Vy</td><td>1</td><td>Lateral velocity Vo0 = Veo(Same speed as the leading vehicle)</td><td rowspan="2"></td></tr><tr><td colspan="3"></td><td>2 3</td><td>Vf0 = 0 (stop vehicle) Follow the leading vehicle in THW=2sec</td></tr></table>

### 公式（取前 8 个）

**公式 1** (page 10):

$$
T T C L a n e I n t r u s i o n > v r e l / ( 2 \cdot \times 6 \mathrm { m } / \mathrm { s } ^ { 2 } ) + 0 . 3 5 s
$$

**公式 2** (page 56):

$$
\begin{array} { r } { \frac { d i s t _ { l a t } } { u _ { c u t - i n , l a t } } < \frac { d i s t _ { l o n } + l e n g t h _ { e g o } + l e n g t h _ { c u t - i n } } { u _ { e g o , l o n } - u _ { c u t - i n , l o n } } + 0 . 1 \ } \end{array}
$$

**公式 3** (page 57):

$$
P F S ( d i s t _ { l o n } ) = \left\{ \begin{array} { c c } { 1 } & { \mathrm { i f } \ 0 < d i s t _ { l o n } - d _ { 1 } < d _ { u n s a f e } } \\ { 0 } & { \mathrm { i f } \ d i s t _ { l o n } - d _ { 1 } > d _ { s a f e } } \\ { \frac { d i s t _ { l o n } - d _ { s a f e } - d _ { 1 } } { d _ { u n s a f e } - d _ { s a f e } } } & { \mathrm { i f } \ d _ { u n s a f e } < d i s t _ { l o n } - d _ { 1 } < d _ { s a f e } } \end{array} \right.
$$

**公式 4** (page 57):

$$
\begin{array} { r l } & { d _ { s a f e } = u _ { e g o , l o n } \tau + \frac { u _ { e g o , l o n } ^ { 2 } } { 2 b _ { e g o , c o m f } } - \frac { u _ { c u t - i n , l o n } ^ { 2 } } { 2 b _ { c u t - i n , m a x } } + d _ { 1 } } \\ & { d _ { u n s a f e } = u _ { e g o , l o n } \tau + \frac { u _ { e g o , l o n } ^ { 2 } } { 2 b _ { e g o , m a x } } - \frac { u _ { c u t - i n , l o n } ^ { 2 } } { 2 b _ { c u t - i n , m a x } } } \end{array}
$$

**公式 5** (page 57):

$$
C F S ( d i s t _ { l o n } ) = \left\{ \begin{array} { c c } { 1 } & { \mathrm { ~ i f ~ } 0 < d i s t _ { l o n } < d _ { u n s a f e } } \\ { 0 } & { \mathrm { ~ i f ~ } d i s t _ { l o n } \geq d _ { s a f e } } \\ { \frac { d i s t _ { l o n } - d _ { s a f e } } { d _ { u n s a f e } - d _ { s a f e } } } & { \mathrm { ~ i f ~ } d _ { u n s a f e } \leq d i s t _ { l o n } < d _ { s a f e } } \end{array} \right.
$$

**公式 6** (page 57):

$$
\begin{array} { r l r } & { } & { d _ { s a f e } = \left\{ \begin{array} { l l } { \frac { \left( u _ { e g o , l o n } - u _ { c u t - i n , l o n } \right) ^ { 2 } } { 2 { a } _ { e g o } ^ { 2 } } } & { \mathrm { i f ~ } u _ { e g o , l o n , N E X T } \leq u _ { c u t - i n , l o n } } \\ { d _ { n e w } + \frac { \left( u _ { e g o , l o n , N E X T } - u _ { c u t - i n , l o n } \right) ^ { 2 } } { 2 b _ { e g o , c o n } f } } & { \mathrm { i f ~ } u _ { e g o , l o n , N E X T } > u _ { c u t - i n , l o n } } \end{array} \right. } \\ & { } & { d _ { u n s a f e } = \left\{ \begin{array} { l l } { \frac { \left( u _ { e g o , l o n } - u _ { c u t - i n , l o n } \right) ^ { 2 } } { 2 { a } _ { e g o } ^ { 2 } } } & { \mathrm { i f ~ } u _ { e g o , l o n , N E X T } \leq u _ { c u t - i n , l o n } } \\ { \qquad 2 { \frac { \left( u _ { e g o , l o n } - u _ { c u t - i n , l o n } \right) ^ { 2 } } { 2 b _ { e g o , l o n } } } } & { \mathrm { i f ~ } u _ { e g o , l o n , N E X T } > u _ { c u t - i n , l o n } } \end{array} \right. } \\ & { } & { d _ { n e w } + \frac { \left( u _ { e g o , l o n } , 0 . 0 8 \right) T - u _ { c u t - i n , l o n } } { 2 b _ { e g o , m a x } } \mathrm { i f ~ } u _ { e g o , l o n , N E X T } > u _ { c u t - i n , l o n } } \end{array}
$$

**公式 7** (page 57):

$$
\begin{array} { r l } & { a _ { e g o } ^ { \prime } = m a x \left( a _ { e g o } , - b _ { e g o , c o m f } \right) } \\ & { { u } _ { e g o , l o n , N E X T } = u _ { e g o , l o n } + a _ { e g o } ^ { \prime } \tau } \\ & { d _ { n e w } = \left( \frac { \left( u _ { e g o , l o n } + u _ { e g o , l o n , N E X T } \right) } { 2 } - \ u _ { c u t - i n , l o n } \right) \tau } \end{array}
$$

**公式 8** (page 58):

$$
b _ { r e a c t i o n } = \left\{ \begin{array} { c l } { C F S \cdot \left( b _ { e g o , m a x } - b _ { e g o , c o m f } \right) + b _ { e g o , c o m f } } & { \mathrm { i f } \ C F S > 0 } \\ { P F S \cdot b _ { e g o , c o m f } } & { \mathrm { i f } \ C F S = 0 } \end{array} \right.
$$

### 图像（取前 8 张）

![图 page 19](../_mineru_assets/ECE R157 Am4/2aaa2bf8751b75737952860ba4f36a54d10e5a3cb18cdfc5e585c30ca0fb213b.jpg)  

![Example1.  / Example2. ](../_mineru_assets/ECE R157 Am4/9e949db1cfa81d1b6882737588ba5582dc99d6ab95781330a3a88d7ecaf482ba.jpg)  
*Example1.  / Example2. * (page 23)

![图 page 38](../_mineru_assets/ECE R157 Am4/a6f71c0671de33a41efb80030835458dbb5713bd4098ee9a4cce1517b61449dd.jpg)  

![Figure 1 Competent and careful human performance model ](../_mineru_assets/ECE R157 Am4/a19d911b7a2b723f621df3ee180b8ef778b5e8ebc0d29a4e4487699682075bb0.jpg)  
*Figure 1 Competent and careful human performance model * (page 40)

![Figure 2 Driver model for the cut-in scenario ](../_mineru_assets/ECE R157 Am4/dc831030986dc888549c554673b50b80f84b33272d5d250da71594da34d12b79.jpg)  
*Figure 2 Driver model for the cut-in scenario * (page 41)

![Figure 3 Cut in scenario ](../_mineru_assets/ECE R157 Am4/d181055cf0bd3d57774e15849b3ad4898166860fda7ea474bf26d552784596f3.jpg)  
*Figure 3 Cut in scenario * (page 41)

![Figure 4 Deceleration scenario ](../_mineru_assets/ECE R157 Am4/0dc47a53cbdf11a47963328b49473615569b2cfbeac2410e5fa05c7cead5a5c7.jpg)  
*Figure 4 Deceleration scenario * (page 41)

![Figure 6 Parameters ](../_mineru_assets/ECE R157 Am4/d658fa118a55a1bbb09c7d594d007603655f4be135b89edf0dd0124d84645a3b.jpg)  
*Figure 6 Parameters * (page 43)

