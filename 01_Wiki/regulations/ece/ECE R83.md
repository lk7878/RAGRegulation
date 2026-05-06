---
reg_id: ECE R83
region: ece
type: type/version
title: 关于车辆污染物排放和发动机燃油要求认证的统一规定
source_file: 国外法规\ECE标准\11.ECE法规（中文）\法规83号\83.pdf
source_page_count: unknown
tags:
- type/version
- reg/ece
- status/active
- status/needs-review
_truncated_input: true
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\11.ECE法规（中文）\法规83号\83.pdf
status: active
verified_by: deepseek-v3
cross_check_overall_confidence: medium
技术要求限值_conf: low
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段，B中未明确提及“标准机构”信息。
- field: publication_date
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段。B中提及“2005年6月14日”等，但未明确是法规发布日期。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段。B中提及多个修正本生效日期，但未明确新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段。B中未明确提及在用车型实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段。B中未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段。B中提及“第三版”、“修正本”，但未明确取代哪个版本。
- field: 技术要求限值
  status: mismatch
  extracted: 'A类限值（2000）: 基准质量 (RW) kg | CO (g/km) | HC (g/km) | NOx (g/km) | HC+NOx
    (g/km) | PM (g/km)

    所有 (RW≤1305) | 2.3 (汽油) / 0.64 (柴油) | 0.20 (汽油) / - | 0.15 (汽油) / 0.50 (柴油) |
    - / 0.56 (柴油) | - / 0.05 (柴油)

    1305 < RW ≤ 1760 | 4.17 (汽油) / 0.80 (柴油) | 0.25 (汽油) / - | 0.18 (汽油) / 0.65 (柴油)
    | - / 0.72 (柴油) | - / 0.07 (柴油)

    1760 < RW | 5.22 (汽油) / 0.95 (柴油) | 0.29 (汽油) / - | 0.21 (汽油) / 0.78 (柴油) | -
    / 0.86 (柴油) | - / 0.10 (柴油)

    B类限值（2005）: 未提供具体数值'
  original: '原文第21页表格：

    A类（2000）限值：

    基准质量(RW) kg | CO (g/km) | HC (g/km) | NOx (g/km) | HC+NOx (g/km) | PM (g/km)

    所有 RW≤1,305 kg | 2.3 (汽油) / 0.64 (柴油) | 0.20 (汽油) / - | 0.15 (汽油) / 0.50 (柴油)
    | - / 0.56 (柴油) | 0.05 (柴油)

    1,305<RW≤1,760kg | 4.17 (汽油) / 0.80 (柴油) | 0.25 (汽油) / - | 0.18 (汽油) / 0.65 (柴油)
    | - / 0.72 (柴油) | 0.07 (柴油)

    1,760<RW | 5.22 (汽油) / 0.95 (柴油) | 0.29 (汽油) / - | 0.21 (汽油) / 0.78 (柴油) | - /
    0.86 (柴油) | 0.10 (柴油)

    B类（2005）限值：

    所有 RW≤1,305 kg | 1.0 (汽油) / 0.50 (柴油) | 0.10 (汽油) / - | 0.08 (汽油) / 0.25 (柴油)
    | - / 0.30 (柴油) | 0.025 (柴油)

    1,305<RW≤1,760 kg | 1.81 (汽油) / 0.63 (柴油) | 0.13 (汽油) / - | 0.10 (汽油) / 0.33 (柴油)
    | - / 0.39 (柴油) | 0.04 (柴油)

    1,760<RW | 2.27 (汽油) / 0.74 (柴油) | 0.16 (汽油) / - | 0.11 (汽油) / 0.39 (柴油) | - /
    0.46 (柴油) | 0.05 (柴油)'
  note: A中B类限值表格不完整（仅标题），且A类限值表格中PM限值标注位置与原文表格结构不完全一致（原文PM列明确为柴油机）。A中B类限值缺失具体数值，构成不匹配。
  recheck_verdict: confirmed_mismatch
_low_conf_recheck_source: stage3_llm_opus
_low_conf_recheck_verdict: upgrade
_low_conf_recheck_reason: body内容结构完整，覆盖适用范围、核心定义、试验类型与方法、排放限值（含A类/B类具体数值表）、生产一致性、认证扩展及过渡规定等核心条款，内容充实、逻辑清晰。标题与reg_id高度吻合，适用范围明确。主要缺失为publication_date无法从body字面确认精确日期，版本/修正本信息亦不完整，因此升至medium而非high。
publication_date: 2005-06-14
_ocr_upgraded: mineru_split
_mineru_split_parts:
- part: 1
  pages: 180
  outputs_dir: outputs\ECE_R83__part1
- part: 2
  pages: 94
  outputs_dir: outputs\ECE_R83__part2
_mineru_blocks:
  tables: 15
  formulas: 25
  images: 12
_mineru_merged_at: '2026-04-25'
---

# ECE R83 法规：关于车辆污染物排放和发动机燃油要求认证的统一规定

## 法规概述
本法规（ECE R83）规定了关于车辆污染物排放和发动机燃油要求认证的统一技术规定。它适用于《1958年日内瓦协议》框架下，对轮式车辆及其装备和零部件进行型式认证的相互认可。

## 适用范围
1.1 本法规适用于：
- 1.1.1 装有点燃式（P.I.）发动机，至少有4个车轮的车辆在正常和低温环境下的排放、蒸发排放、曲轴箱排放、排放控制装置耐久性和车载诊断（OBD）系统。
- 1.1.2 最大质量不超过3500kg，至少有4个车轮，装有压燃式（C.I.）发动机的M1类和N1类车辆的排放、排放控制装置耐久性和OBD系统。
- 1.1.3 装有点燃式发动机的混合动力车辆（HEV）在正常和低温环境下的排放、蒸发排放、曲轴箱排放、排放控制装置耐久性和OBD系统。
- 1.1.4 最大载重不超过3500kg，具有至少四个车轮及装备压燃式发动机的M1类和N1类混合动力车辆（HEV）的排放、排放控制装置耐久性和OBD系统。
- 1.1.6 允许将装有已认证压燃式发动机的M1或N1类车辆的认证，扩展到满足特定条件且基准质量不超过2840kg的M2和N2类车辆（扩展认证）。
- 1.1.7 装有压燃式发动机或燃用天然气（NG）/液化石油气（LPG）的点燃式发动机的N1类车辆，若其发动机已按ECE R49认证，则不受本法规限制。

1.2 本法规不适用于：
- 最大质量小于400kg、最大设计速度低于50km/h的车辆。
- 特定卸载重量和功率限制下的车辆。
- 装有点燃式发动机且燃用NG或LPG，最大质量超过3500kg的M1类车辆（适用ECE R49）。

## 核心定义
- **车辆类型**：在主要方面（如与基准质量相关的当量惯量、发动机和车辆特性）无差异的机动车辆。
- **基准质量**：车辆的“空载质量”统一增加100kg。
- **最大质量**：制造厂标称的技术允许最大质量。
- **气体污染物**：一氧化碳（CO）、以二氧化氮（NO2）当量表示的氮氧化物（NOx）和特定碳氢比率的碳氢化合物（HC）。
- **微粒排放（PM）**：从稀释排气中滤除的排放组分。
- **排放**：对于点燃式发动机指气体排放；对于压燃式发动机指气体排放和微粒排放。
- **蒸发排放**：从燃油系统泄漏的碳氢蒸气。
- **车载诊断（OBD）系统**：用于排放控制的车载诊断系统。
- **车辆认证类别**：
    - **B类认证**：针对燃用无铅汽油或汽油/LPG/NG的车辆，限制气体排放、蒸发排放、曲轴箱排放、污染物控制装置耐久性、冷起动排放和OBD。
    - **C类认证**：针对燃用柴油的车辆，限制气体和微粒排放、曲轴箱排放、排气污染物控制装置耐久性和OBD。
    - **D类认证**：针对燃用LPG或天然气的车辆，限制气体排放、曲轴箱排放、污染物控制装置耐久性、冷起动排放和OBD。
- **混合动力车辆（HEV）**：从车载燃料和电能/功率存储装置中提取能量以产生机械推力的车辆。
- **单燃料车辆**：设计主要长久使用LPG或NG，汽油系统仅用于紧急启动（汽油箱容量≤15升）。
- **双燃料车辆**：可部分时间用汽油，另一部分时间用LPG或NG。

## 认证与试验要求
### 认证申请与批准
- 认证申请由车辆制造厂或其代理商提交，需提供包括OBD系统详细信息在内的技术文件。
- 提交代表性车辆进行试验。
- 若满足法规要求，则批准认证并授予认证号。认证标志需包含国家代号、法规号（如“83R”）、认证号及区分排放限值的附加字符（如“I”或“II”）。

### 试验类型与方法
试验类型根据发动机类型和燃料有所不同，汇总如下表：

| 试验类型 | 点燃式发动机车辆 (汽油) | 点燃式发动机车辆 (双燃料) | 点燃式发动机车辆 (单燃料) | 压燃式发动机车辆 |
| :--- | :--- | :--- | :--- | :--- |
| **I型试验** (冷起动后平均排放) | 是 (最大质量≤3.5t) | 是 (对两种燃料) (最大质量≤3.5t) | 是 (最大质量≤3.5t) | 是 (最大质量≤3.5t) |
| **II型试验** (怠速CO) | 是 | 是 (对两种燃料) | - | - |
| **III型试验** (曲轴箱排放) | 是 | 是 (仅对汽油) | 是 | - |
| **IV型试验** (蒸发排放) | 是 (最大质量≤3.5t) | 是 (仅对汽油) (最大质量≤3.5t) | - | - |
| **V型试验** (耐久性) | 是 (最大质量≤3.5t) | 是 (仅对汽油) (最大质量≤3.5t) | 是 (最大质量≤3.5t) | 是 (最大质量≤3.5t) |
| **VI型试验** (低温冷起动) | 是 (最大质量≤3.5t) | 是 (仅对汽油) (最大质量≤3.5t) | - | - |
| **OBD系统试验** | 是 | 是 | 是 | 是 |

**主要试验说明：**
- **I型试验**：在底盘测功机上进行模拟冷起动后的排放测试，循环由市区部分（4个基本循环）和市郊部分组成。需测量CO、HC、NOx和（对压燃式发动机）PM。结果需乘以劣化系数（DF）。
- **II型试验**：测量怠速工况下排气中的CO体积含量。
- **III型试验**：验证曲轴箱通风系统不允许气体排入大气。
- **IV型试验**：确定蒸发排放量，限值为2g/试验。
- **V型试验**：排放控制装置耐久性试验（80,000km老化），或使用规定的劣化系数。
- **VI型试验**：在低温（-7°C）下进行冷起动后的CO和HC排放测试。
- **OBD系统试验**：验证OBD系统的功能。

### 排放限值（I型试验）
试验结果需满足下表限值（乘以劣化系数后）：

**A类限值（2000）**
| 基准质量 (RW) kg | CO (g/km) | HC (g/km) | NOx (g/km) | HC+NOx (g/km) | PM (g/km) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **所有** (RW≤1305) | 2.3 (汽油) / 0.64 (柴油) | 0.20 (汽油) / - | 0.15 (汽油) / 0.50 (柴油) | - / 0.56 (柴油) | - / 0.05 (柴油) |
| 1305 < RW ≤ 1760 | 4.17 (汽油) / 0.80 (柴油) | 0.25 (汽油) / - | 0.18 (汽油) / 0.65 (柴油) | - / 0.72 (柴油) | - / 0.07 (柴油) |
| 1760 < RW | 5.22 (汽油) / 0.95 (柴油) | 0.29 (汽油) / - | 0.21 (汽油) / 0.78 (柴油) | - / 0.86 (柴油) | - / 0.10 (柴油) |

**B类限值（2005）**
| 基准质量 (RW) kg | CO (g/km) | HC (g/km) | NOx (g/km) | HC+NOx (g/km) | PM (g/km) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **所有** (RW≤1305) | 1.0 (汽油) / 0.50 (柴油) | 0.10 (汽油) / - | 0.08 (汽油) / 0.25 (柴油) | - / 0.30 (柴油) | - / 0.025 (柴油) |
| 1305 < RW ≤ 1760 | 1.81 (汽油) / 0.63 (柴油) | 0.13 (汽油) / - | 0.10 (汽油) / 0.33 (柴油) | - / 0.39 (柴油) | - / 0.04 (柴油) |
| 1760 < RW | 2.27 (汽油) / 0.74 (柴油) | 0.16 (汽油) / - | 0.11 (汽油) / 0.39 (柴油) | - / 0.46 (柴油) | - / 0.05 (柴油) |

*注：M1类车辆（除最大质量>2500kg者）和N1类车辆适用。燃用气体燃料的车辆，气体排放限值同汽油机车辆。*

### 劣化系数（V型试验）
| 发动机类型 | CO | HC | NOx | HC+NOx | PM |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 点燃式发动机 | 1.2 | 1.2 | 1.2 | - | - |
| 压燃式发动机 | 1.1 | - | 1.0 | 1.0 | 1.2 |

## 生产一致性
- 带有认证标志的车辆，其影响排放的部件应与已认证车型一致。
- 生产一致性检查包括对排放（I、II、III、IV型试验）和使用中车辆一致性的验证。
- I型试验生产一致性检查需从系列中抽取车辆进行测试，并应用统计方法（附录1、2）进行判定。
- OBD系统生产一致性检查需从系列中抽取车辆，验证其是否符合功能要求。

## 车型更改与认证扩展
- 车型的任何更改必须通知认证部门，可能需要进一步的试验报告。
- 在满足特定条件下，认证可以扩展到不同基准质量、传动比、蒸发排放系统、排放控制装置耐久性或OBD系统的车型。

## 过渡规定
- 规定了从旧版（如04系列修正本）向新版（05系列修正本）认证过渡的时间表和条件。
- 明确了不同类型车辆（按质量、座位数、燃料）开始适用新限值和新要求（如OBD）的具体日期。

## 附录清单
法规包含多个附录，详细规定了试验程序、技术要求和文件格式：
- **附录1**：发动机和车辆特性信息（用于指导试验）。
- **附录2**：认证通知书格式及OBD相关信息。
- **附录3**：认证标志布置示例。
- **附录4**：I型试验（确定冷起动后排放物）的详细规程，包括运转循环、设备要求、取样分析程序和计算示例。
- **附录5**：II型试验（怠速CO排放）。
- **附录6**：III型试验（曲轴箱气体排放）。
- **附录7**：IV型试验（蒸发排放）。
- **附录8**：VI型试验（低温冷起动排放）。
- **附录9**：V型试验（排放控制装置耐久性）。
- **附录10**：基准燃料技术要求。
- **附录10a**：气体基准燃料技术要求。
- **附录11**：车载诊断（OBD）系统要求。
- **附录12**：燃用LPG或天然气车辆的认证。
- **附录13**：周期性再生系统车辆的排放测试流程。
- **附录14**：混合动力车辆的排放测试流程。
- **生产一致性验证附录**：附录1（制造厂提供标准偏差满意时）、附录2（制造厂提供标准偏差不满意或不适用时）、附录3（使用一致性检查）、附录4（用于使用一致性试验的统计方法）。
---

## 原文参考（MinerU 云解析 · 多分块合并 · 2026-04-25）

> 本 PDF 因超过 MinerU 200 页限制被拆为 2 块分别 OCR，再合并：
> part1 (180p) + part2 (94p)
>
> 共解析到：
> - 表格 43 个
> - 公式 45 个
> - 图像 23 个
> - 全文 Markdown 合计 243,627 字符

### 表格（取前 15 个）

#### 表 1 (page 18, part1)
<table><tr><td rowspan=1 colspan=1>类型认证试验</td><td rowspan=1 colspan=3>M 类和N类的点燃式发动机车辆</td><td rowspan=1 colspan=1>M1类和N，类的压燃式发动机车辆</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>汽油燃料车辆</td><td rowspan=1 colspan=1>双燃料车辆</td><td rowspan=1 colspan=1>单燃料车辆</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>I型试验</td><td rowspan=1 colspan=1>是（最大质量≤3.5t)</td><td rowspan=1 colspan=1>是（对两种燃料类型的试验） (最大质量≤3.5t)</td><td rowspan=1 colspan=1>是（最大质量≤3.5t)</td><td rowspan=1 colspan=1>是 (最大质量≤3.5t)</td></tr><tr><td rowspan=1 colspan=1>ⅡI型试验</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是(两种燃料类型的试验)</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>ⅢI型试验</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1>是 (只对汽油进行试验)</td><td rowspan=1 colspan=1>是</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>IV型试验</td><td rowspan=1 colspan=1>是（最大质量≤3.5t)</td><td rowspan=1 colspan=1>是 (只对汽油进行试验)(最大质量≤3.5t)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>V型试验</td><td rowspan=1 colspan=1>是(最大质量≤3.5t)</td><td rowspan=1 colspan=1>是(只对汽油进行试验)(最大质量≤3.5t)</td><td rowspan=1 colspan=1>是（最大质量≤3.5t)</td><td rowspan=1 colspan=1>是 (最大质量≤3.5t)</td></tr><tr><td rowspan=1 colspan=1>VI型试验</td><td rowspan=1 colspan=1>是(最大质量≤3.5t)</td><td rowspan=1 colspan=1>是(只对汽油进行试验)(最大质量≤3.5t)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>认证扩展</td><td rowspan=1 colspan=1>第7条</td><td rowspan=1 colspan=1>第7条</td><td rowspan=1 colspan=1>第7条</td><td rowspan=1 colspan=1>第7条；M2 和N2 类车辆(基准质量≤2840kg)</td></tr><tr><td rowspan=1 colspan=1>车载诊断系统</td><td rowspan=1 colspan=1>是，遵照第11.1.5.1.1或11.1.5.3条说明</td><td rowspan=1 colspan=1>是，遵照第11.1.5.1.2或11.1.5.3条说明</td><td rowspan=1 colspan=1>是，遵照第11.1.5.1.2或11.1.5.3条说明</td><td rowspan=1 colspan=1>是，遵照第11.1.5.2.1或11.1.5.2.2或11.1.5.2.3或11.1.5.3条说明</td></tr></table>

#### 表 2 (page 20, part1)
<table><tr><td rowspan=2 colspan=3></td><td rowspan=2 colspan=1>基准质量(RW)（kg)</td><td rowspan=1 colspan=2>一氧化碳质量(CO)</td><td rowspan=1 colspan=2>碳氢质量(HC)</td><td rowspan=1 colspan=2>氮氧化物质量(NOx)</td><td rowspan=1 colspan=2>碳氢和氮氧化物组合质量(HC+NOx)</td><td rowspan=1 colspan=1>微粒(1)质量(PM)</td></tr><tr><td rowspan=1 colspan=2>L（g/km)</td><td rowspan=1 colspan=2>L(g/km)</td><td rowspan=1 colspan=2>L（g/km)</td><td rowspan=1 colspan=2>L+L(g/km)</td><td rowspan=1 colspan=1>L4(g/km)</td></tr><tr><td rowspan=1 colspan=2>类型</td><td rowspan=1 colspan=1>组</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>汽油机</td><td rowspan=1 colspan=1>柴油机</td><td rowspan=1 colspan=1>汽油机</td><td rowspan=1 colspan=1>柴油机</td><td rowspan=1 colspan=1>汽油机</td><td rowspan=1 colspan=1>柴油机</td><td rowspan=1 colspan=1>汽油机</td><td rowspan=1 colspan=1>柴油机</td><td rowspan=1 colspan=1>柴油机</td></tr><tr><td rowspan=4 colspan=1>A(2000)</td><td rowspan=1 colspan=1>M2</td><td rowspan=1 colspan=1>：</td><td rowspan=1 colspan=1>所有</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>0.64</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.50</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0.56</td><td rowspan=1 colspan=1>0.05</td></tr><tr><td rowspan=3 colspan=1>N3（</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>RW≤1,305kg</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>0.64</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.50</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.56</td><td rowspan=1 colspan=1>0.05</td></tr><tr><td rowspan=1 colspan=1>II</td><td rowspan=1 colspan=1>1,305&lt;RW≤1,760kg</td><td rowspan=1 colspan=1>4.17</td><td rowspan=1 colspan=1>0.80</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1>0.65</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0.72</td><td rowspan=1 colspan=1>0.07</td></tr><tr><td rowspan=1 colspan=1>Ⅲ</td><td rowspan=1 colspan=1>1,760&lt;RW</td><td rowspan=1 colspan=1>5.22</td><td rowspan=1 colspan=1>0.95</td><td rowspan=1 colspan=1>0.29</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.21</td><td rowspan=1 colspan=1>0.78</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.86</td><td rowspan=1 colspan=1>0.10</td></tr><tr><td rowspan=4 colspan=1>B(2005)</td><td rowspan=1 colspan=1>M2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>所有</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.50</td><td rowspan=1 colspan=1>0.10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.08</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1>0.025</td></tr><tr><td rowspan=3 colspan=1>N3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RW≤1,305 kg</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>0.50</td><td rowspan=1 colspan=1>0.10</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.08</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1>0.025</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1,305&lt;RW≤1,760 kg</td><td rowspan=1 colspan=1>1.81</td><td rowspan=1 colspan=1>0.63</td><td rowspan=1 colspan=1>0.13</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.10</td><td rowspan=1 colspan=1>0.33</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.39</td><td rowspan=1 colspan=1>0.04</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1,760&lt;RW</td><td rowspan=1 colspan=1>2.27</td><td rowspan=1 colspan=1>0.74</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1>0.39</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.46</td><td rowspan=1 colspan=1>0.05</td></tr></table>

#### 表 3 (page 24, part1)
<table><tr><td rowspan=1 colspan=1>试验温度</td><td rowspan=1 colspan=1>一氧化碳L1(g/km)</td><td rowspan=1 colspan=1>碳氢L2(g/km)</td></tr><tr><td rowspan=1 colspan=1>266 K (-7 C)</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>1.8</td></tr></table>

#### 表 4 (page 25, part1)
<table><tr><td rowspan=1 colspan=1>发动机类型</td><td rowspan=1 colspan=5>劣化系数</td></tr><tr><td rowspan=1 colspan=1>污染物</td><td rowspan=1 colspan=1>CO</td><td rowspan=1 colspan=1>HC</td><td rowspan=1 colspan=1>NOx</td><td rowspan=1 colspan=1>HC+Nox(</td><td rowspan=1 colspan=1>微粒</td></tr><tr><td rowspan=1 colspan=1>点燃式发动机</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>:</td></tr><tr><td rowspan=1 colspan=1>压燃式发动机</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1.2</td></tr></table>

#### 表 5 (page 48, part1)
**表1/1**

<table><tr><td rowspan=1 colspan=1>试验样品的累计数量(当前样品数量)</td><td rowspan=1 colspan=1>“合格&quot;判定临界值</td><td rowspan=1 colspan=1>“不合格&quot;判定临界值</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3.327</td><td rowspan=1 colspan=1>-4.724</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3.261</td><td rowspan=1 colspan=1>-4.79</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>3.195</td><td rowspan=1 colspan=1>-4.856</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>3.129</td><td rowspan=1 colspan=1>-4.922</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>3.063</td><td rowspan=1 colspan=1>-4.988</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>2.997</td><td rowspan=1 colspan=1>-5.054</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>2.931</td><td rowspan=1 colspan=1>-5.12</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>2.865</td><td rowspan=1 colspan=1>-5.185</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>2.799</td><td rowspan=1 colspan=1>-5.251</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>2.733</td><td rowspan=1 colspan=1>-5.317</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>2.667</td><td rowspan=1 colspan=1>-5.383</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>2.601</td><td rowspan=1 colspan=1>-5.449</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>2.535</td><td rowspan=1 colspan=1>-5.515</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>2.469</td><td rowspan=1 colspan=1>-5.581</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>2.403</td><td rowspan=1 colspan=1>-5.647</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>2.337</td><td rowspan=1 colspan=1>-5.713</td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>2.271</td><td rowspan=1 colspan=1>-5.779</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>2.205</td><td rowspan=1 colspan=1>-5.845</td></tr><tr><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>2.139</td><td rowspan=1 colspan=1>-5.911</td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>2.139</td><td rowspan=1 colspan=1>-5.911</td></tr><tr><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>2.007</td><td rowspan=1 colspan=1>-6.043</td></tr><tr><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>1.941</td><td rowspan=1 colspan=1>-6.109</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>1.875</td><td rowspan=1 colspan=1>-6.175</td></tr><tr><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>1.809</td><td rowspan=1 colspan=1>-6.241</td></tr><tr><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>1.743</td><td rowspan=1 colspan=1>-6.307</td></tr><tr><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>1.677</td><td rowspan=1 colspan=1>-6.373</td></tr><tr><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>1.611</td><td rowspan=1 colspan=1>-6.439</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>1.545</td><td rowspan=1 colspan=1>-6.505</td></tr><tr><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>1.479</td><td rowspan=1 colspan=1>-6.571</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>-2.112</td><td rowspan=1 colspan=1>-2.112</td></tr></table>

#### 表 6 (page 51, part1)
**表1/2最小样本数 $\dot { = } 3$ **

<table><tr><td rowspan=1 colspan=1>试验样品的累计数量(n)</td><td rowspan=1 colspan=1>“合格&quot;判定临界值(An)</td><td rowspan=1 colspan=1>“不合格&quot;判定临界值(Bn)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>-0.80381</td><td rowspan=1 colspan=1>16.64743</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-0.76339</td><td rowspan=1 colspan=1>7.68627</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>-0.72982</td><td rowspan=1 colspan=1>4.67136</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>-0.69962</td><td rowspan=1 colspan=1>3.25573</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>-0.67129</td><td rowspan=1 colspan=1>2.45431</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>-0.64406</td><td rowspan=1 colspan=1>1.94369</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>-0.61750</td><td rowspan=1 colspan=1>1.59105</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>-0.59135</td><td rowspan=1 colspan=1>1.33295</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>-0.56542</td><td rowspan=1 colspan=1>1.13566</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>-0.53960</td><td rowspan=1 colspan=1>0.97970</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>-0.51379</td><td rowspan=1 colspan=1>0.85307</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>-0.48791</td><td rowspan=1 colspan=1>0.74801</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>-0.46191</td><td rowspan=1 colspan=1>0.65928</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>-0.43573</td><td rowspan=1 colspan=1>0.58321</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>-0.40933</td><td rowspan=1 colspan=1>0.51718</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>-0.38266</td><td rowspan=1 colspan=1>0.45922</td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>-0.35570</td><td rowspan=1 colspan=1>0.40788</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>-0.32840</td><td rowspan=1 colspan=1>0.36203</td></tr><tr><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>-0.30072</td><td rowspan=1 colspan=1>0.32078</td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>-0.27263</td><td rowspan=1 colspan=1>0.28343</td></tr><tr><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>-0.24410</td><td rowspan=1 colspan=1>0.24943</td></tr><tr><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>-0.21509</td><td rowspan=1 colspan=1>0.21831</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>-0.18557</td><td rowspan=1 colspan=1>0.18970</td></tr><tr><td rowspan=1 colspan=1>26</td><td rowspan=1 colspan=1>-0.15550</td><td rowspan=1 colspan=1>0.16328</td></tr><tr><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>-0.12483</td><td rowspan=1 colspan=1>0.13880</td></tr><tr><td rowspan=1 colspan=1>28</td><td rowspan=1 colspan=1>-0.09354</td><td rowspan=1 colspan=1>0.11603</td></tr><tr><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>-0.06159</td><td rowspan=1 colspan=1>0.09480</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>-0.02892</td><td rowspan=1 colspan=1>0.07493</td></tr><tr><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>0.00449</td><td rowspan=1 colspan=1>0.05629</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>0.03876</td><td rowspan=1 colspan=1>0.03876</td></tr></table>

#### 表 7 (page 61, part1)
**合格/不合格取样计划特征表格**

<table><tr><td rowspan=1 colspan=1>累积样车数量(n)</td><td rowspan=1 colspan=1>合格判定临界值</td><td rowspan=1 colspan=1>不合格判定临界值</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=12 colspan=1>-5667889910</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=3 colspan=1>8910</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=2 colspan=1>1112</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>11</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>11</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=2 colspan=1>1718</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>12</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>12</td></tr></table>

#### 表 8 (page 74, part1)
<table><tr><td rowspan=1 colspan=1>部件</td><td rowspan=1 colspan=1>缺陷代码</td><td rowspan=1 colspan=1>监测策略</td><td rowspan=1 colspan=1>缺陷探测标准</td><td rowspan=1 colspan=1>MI激活标准</td><td rowspan=1 colspan=1>二级参数</td><td rowspan=1 colspan=1>预处理</td><td rowspan=1 colspan=1>示范试验</td></tr><tr><td rowspan=1 colspan=1>催化剂</td><td rowspan=1 colspan=1>PO402</td><td rowspan=1 colspan=1>氧化传感器1和2的信号</td><td rowspan=1 colspan=1>传感器1和2的信号差异</td><td rowspan=1 colspan=1>第3次循环</td><td rowspan=1 colspan=1>发动机速度，发动机装载,A/F模式,催化剂温度</td><td rowspan=1 colspan=1>两个I类循环</td><td rowspan=1 colspan=1>类</td></tr></table>

#### 表 9 (page 77, part1)
<table><tr><td rowspan=1 colspan=1>档位</td><td rowspan=1 colspan=1>变速器内部速比</td><td rowspan=1 colspan=1>主传动比</td><td rowspan=1 colspan=1>总传动比</td></tr><tr><td rowspan=1 colspan=1>CVT时最大值(*)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4，5，其它</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>CVT时最小值(*)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>倒档</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 10 (page 81, part1)
<table><tr><td rowspan=1 colspan=1>污染物</td><td rowspan=1 colspan=1>CO (g/km)</td><td rowspan=1 colspan=1>HC (g/km)</td><td rowspan=1 colspan=1>NOx(g/km)</td><td rowspan=1 colspan=1>(HC+NOx)、(1） (g/km)</td><td rowspan=1 colspan=1>微粒(1)(g/km)</td></tr><tr><td rowspan=3 colspan=1>测量值</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>乘以劣化系数(DF)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 11 (page 82, part1)
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>CO (g/km)</td><td rowspan=1 colspan=1>HC (g/km)</td></tr><tr><td rowspan=1 colspan=1>测量值</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 12 (page 82, part1)
<table><tr><td>16.7</td><td>车载诊断系统试验</td></tr><tr><td>16.7.1</td><td>故障指示器（MI）的书面说明或图：</td></tr><tr><td>16.7.2</td><td>由车载诊断系统监控的所有部件和功能一览：</td></tr><tr><td>16.7.3</td><td>书面说明 (一般工作原理)</td></tr><tr><td>16.7.3.1</td><td>失火探测：</td></tr><tr><td>16.7.3.2</td><td>催化剂监控：</td></tr><tr><td>16.7.3.3</td><td>氧传感器监测：</td></tr><tr><td>16.7.3.4</td><td>由车载诊断系统所监测的其它部件：</td></tr><tr><td>16.7.3.5</td><td>微粒捕集器监控：.</td></tr><tr><td>16.7.3.6</td><td>电控燃油系统调节器监控：</td></tr><tr><td>16.7.3.7</td><td>由车载诊断系统所监测的其它部件：</td></tr><tr><td>16.7.4</td><td>故障指示器激励标准（固定的驾驶循环数或统计方法）：</td></tr><tr><td>16.7.5</td><td>所有车载诊断系统代码和所使用的格式一览（附带每种说明）：</td></tr></table>

#### 表 13 (page 83, part1)
<table><tr><td rowspan=1 colspan=1>试验</td><td rowspan=1 colspan=1>CO值(%体积比)</td><td rowspan=1 colspan=1>入 (1)</td><td rowspan=1 colspan=1>发动机转速(min-1)</td><td rowspan=1 colspan=1>发动机机油温度（℃)</td></tr><tr><td rowspan=1 colspan=1>低怠速试验</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>高怠速试验</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

#### 表 14 (page 84, part1)
<table><tr><td rowspan=1 colspan=1>部件</td><td rowspan=1 colspan=1>缺陷代码</td><td rowspan=1 colspan=1>监测策略</td><td rowspan=1 colspan=1>缺陷探测标准</td><td rowspan=1 colspan=1>MI激活标准</td><td rowspan=1 colspan=1>二级参数</td><td rowspan=1 colspan=1>预处理</td><td rowspan=1 colspan=1>演示试验</td></tr><tr><td rowspan=1 colspan=1>催化剂</td><td rowspan=1 colspan=1>P0420</td><td rowspan=1 colspan=1>氧化传感器1和2的信号</td><td rowspan=1 colspan=1>传感器1和2信号差别</td><td rowspan=1 colspan=1>第3个循环</td><td rowspan=1 colspan=1>发动机速度，发动机装载，A/F模式,催化剂温度</td><td rowspan=1 colspan=1>两次I类循环</td><td rowspan=1 colspan=1>楼</td></tr></table>

#### 表 15 (page 99, part1)
<table><tr><td rowspan=1 colspan=1>车辆基准质量RW（kg)</td><td rowspan=1 colspan=1>当量惯量I (kg)</td></tr><tr><td rowspan=1 colspan=1>RW≤480</td><td rowspan=1 colspan=1>455</td></tr><tr><td rowspan=1 colspan=1>480&lt;RW≤540</td><td rowspan=1 colspan=1>510</td></tr><tr><td rowspan=1 colspan=1>540&lt;RW≤595</td><td rowspan=1 colspan=1>570</td></tr><tr><td rowspan=1 colspan=1>595&lt;RW≤650</td><td rowspan=1 colspan=1>625</td></tr><tr><td rowspan=1 colspan=1>650&lt;RW≤710</td><td rowspan=1 colspan=1>680</td></tr><tr><td rowspan=1 colspan=1>710&lt;RW≤765</td><td rowspan=1 colspan=1>740</td></tr><tr><td rowspan=1 colspan=1>765&lt;RW≤850</td><td rowspan=1 colspan=1>800</td></tr><tr><td rowspan=1 colspan=1>850&lt;RW≤965</td><td rowspan=1 colspan=1>910</td></tr><tr><td rowspan=1 colspan=1>965&lt;RW≤1080</td><td rowspan=1 colspan=1>1020</td></tr><tr><td rowspan=1 colspan=1>1080&lt;RW≤1190</td><td rowspan=1 colspan=1>1130</td></tr><tr><td rowspan=1 colspan=1>1190&lt;RW≤1305</td><td rowspan=1 colspan=1>1250</td></tr><tr><td rowspan=1 colspan=1>1305&lt;RW≤1420</td><td rowspan=1 colspan=1>1360</td></tr><tr><td rowspan=1 colspan=1>1420&lt;RW≤1530</td><td rowspan=1 colspan=1>1470</td></tr><tr><td rowspan=1 colspan=1>1530&lt;RW≤1640</td><td rowspan=1 colspan=1>1590</td></tr><tr><td rowspan=1 colspan=1>1640&lt;RW≤1760</td><td rowspan=1 colspan=1>1700</td></tr><tr><td rowspan=1 colspan=1>1760&lt;RW≤1870</td><td rowspan=1 colspan=1>1810</td></tr><tr><td rowspan=1 colspan=1>1870&lt;RW≤1980</td><td rowspan=1 colspan=1>1930</td></tr><tr><td rowspan=1 colspan=1>1980&lt;RW≤2100</td><td rowspan=1 colspan=1>2040</td></tr><tr><td rowspan=1 colspan=1>2100&lt;RW≤2210</td><td rowspan=1 colspan=1>2150</td></tr><tr><td rowspan=1 colspan=1>2210&lt;RW≤2380</td><td rowspan=1 colspan=1>2270</td></tr><tr><td rowspan=1 colspan=1>2380&lt;RW≤2610</td><td rowspan=1 colspan=1>2270</td></tr><tr><td rowspan=1 colspan=1>2610&lt;RW≤</td><td rowspan=1 colspan=1>2270</td></tr></table>

### 公式（取前 25 个）

**公式 1** (page 26, part1):

$$
\frac { \left. \cos _ { 1 } \right. + \frac { \left. \cos _ { 1 } \right. } { 2 } + \left. \mathbf { 0 } _ { 2 } \right. + \left( \frac { \mathrm { H } \times * } { 4 } , \frac { 1 . 5 } { 3 5 + \frac { \left. \cos _ { 1 } \right. } { \left. \cos _ { 1 } \right. } } - \frac { 0 \le v } { 2 } \right) } { \left( 1 + \frac { \mathrm { H } \kappa } { 4 } - \frac { 0 \le v } { 2 } \right) \left( \left. \cos _ { 2 } \right. + \left. \cos _ { 1 } \right. + \left. \cos _ { 1 } \right. \right) } , \left( \left. \mathrm { C O } _ { 2 } \right. + \left. \mathrm { C O } \right. \right)
$$

**公式 2** (page 28, part1):

$$
\Xi = { \frac { | \mathrm { N } _ { 2 } - \mathrm { V } _ { 1 } | } { \mathrm { V } _ { 1 } } }
$$

**公式 3** (page 47, part1):

$$
{ \frac { 1 } { s } } \sum _ { i = 1 } ^ { n } ( L - x _ { i } )
$$

**公式 4** (page 49, part1):

$$
{ \hat { \mathbf { z } } } _ { 1 } = \mathbf { \mathbf { z } } _ { 1 } - \mathbf { \mathbf { L } }
$$

**公式 5** (page 49, part1):

$$
\overline { { \vec { u } } } _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } d _ { i }
$$

**公式 6** (page 49, part1):

$$
V _ { n } ^ { 2 } = { \frac { 1 } { n } } { \sum _ { i = 1 } ^ { n } { { { \left( { d _ { i } - { \overline { { d } } } _ { n } } \right) } ^ { 2 } } } }
$$

**公式 7** (page 50, part1):

$$
\begin{array} { r l } & { \overline { { \mathrm { d } } } _ { \mathrm { s } } = \left( 1 - \frac { 1 } { n } \right) \overline { { \mathrm { d } } } _ { \mathrm { s } - 1 } + \frac { 1 } { n } \mathrm { d } _ { \mathrm { s } } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \mathrm { V } _ { n } ^ { 2 } = \left( 1 - \frac { 1 } { n } \right) \mathrm { V } _ { - 1 } ^ { 2 } + \left[ \frac { \overline { { \mathrm { d } } } _ { \mathrm { n } } - \mathrm { d } _ { \mathrm { s } } } { \mathrm { n } - 1 } \right] ^ { 2 } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

**公式 8** (page 85, part1):

$$
\sqrt [ 3 ] { \frac { \overline { { \alpha } } } { \varepsilon } \sqrt { ( E _ { 1 1 } ) ^ { \frac { \circ } { \varepsilon } } \left\{ 8 3 , 7 , 8 \right\} } }
$$

**公式 9** (page 85, part1):

$$
\sqrt [ 3 ] { \frac { - 5 } { 2 } \int \limits _ { c } ^ { \infty } \frac { - 1 } { d } \int \frac { - 3 d } { \sqrt { 2 } } } \frac { - 2 \sqrt { 2 } } { \sqrt { 2 } }  { 8 } 3 . 0 1 1 - 0 . 5 2 4 3 9
$$

**公式 10** (page 86, part1):

$$
\sqrt [ 3 ] { \frac { \frac { 3 } { 2 } } { 2 } \int _ { x } \left( \right)} \mathsf { E } _ { 1 1 }  \frac { \frac { 3 } { 2 } \sqrt [ 3 ] { 1 } } { \sqrt { \frac { 3 } { 2 } } } \ 8 3 \ R 1 1 - 0 5 2 4 3 9
$$

**公式 11** (page 87, part1):

$$
\sqrt [ 3 ] { \frac { \alpha } { 2 } \int \limits _ { c } ^ { \overline { { c } } } ( \sum \limits _ { i = 1 } ^ { \infty } ) ^ { \frac { \alpha } { 3 } } \sum \limits _ { i = 1 } ^ { \infty } 0 }
$$

**公式 12** (page 87, part1):

$$
\sqrt [ 3 ] { \frac { 3 } { 2 } \int \limits _ { c } ^ { \frac { 1 } { 2 } } \frac { d } { d t } \int \frac { 3 } { 2 } \frac { 3 } { 2 } d 3 } \sqrt { 3 } \geq 0
$$

**公式 13** (page 94, part1):

$$
\mathrm { M } = { \frac { \mathrm { V } _ { \mathrm { m a x } } } { \mathrm { V } _ { \mathrm { m a x } } \mathrm { d } } } \cdot \mathrm { m }  \mathrm { m } = \mathrm { M } \mathrm { d } { \frac { \mathrm { V } _ { \mathrm { m } } } { \mathrm { V } _ { \mathrm { m i x } } } }
$$

**公式 14** (page 118, part1):

$$
\begin{array} { r l r l r l } { { 1 } = \mathrm { F } = \mathbf { a } + \mathbf { b } \cdot \mathbf { V } ^ { 2 } } & { \quad } & { \bullet = ( \mathbf { a } + \mathbf { b } \mathbf { V } ^ { 2 } ) \cdot 0 . 1 \cdot \mathrm { F } _ { 8 0 } } & { \quad } & { } & { \triangle = ( \mathbf { a } + \mathbf { b } \cdot \mathbf { V } ^ { 2 } ) + 0 . 1 \cdot \mathrm { F } _ { 8 0 } } \end{array}
$$

**公式 15** (page 119, part1):

$$
\mathrm { F } = \frac { \mathrm { M } _ { \mathrm { i } } . \Delta \mathrm { V } } { \mathrm { t } }
$$

**公式 16** (page 127, part1):

$$
\mathrm { K } = \frac { R _ { \mathrm { R } } } { R _ { T } } \Big [ \mathrm { I } + K _ { R } \big ( \dot { \psi } - \dot { \psi _ { 0 } } \big ) \Big ] + \frac { R _ { \mathrm { R _ { R } } } } { R _ { T } } \Bigg ( \frac { P _ { 0 } } { P } \Bigg )
$$

**公式 17** (page 127, part1):

$$
\frac { \mathrm { R } _ { \mathrm { R } } } { \mathrm { R } _ { \mathrm { T } } } = \mathrm { a } \mathrm { M } + \mathrm { b }
$$

**公式 18** (page 129, part1):

$$
\mathbf { C _ { \mathrm { 1 1 } } } = \frac { 1 } { \Delta t } \int ^ { \mathrm { i } + \Delta t } \mathbf { C } ( \mathrm { t } ) \mathrm { d t }
$$

**公式 19** (page 131, part1):

$$
\gamma = \mathbb { I } _ { T } \gamma = \mathbb { I } _ { M } : T + \mathbb { F }
$$

**公式 20** (page 157, part1):

$$
\mathbf { x _ { \eta _ { 0 } } } = \frac { 1 } { \ln \sqrt { \frac { \Delta \mathbf { P _ { p } } } { \mathbf { P _ { z } } } } }
$$

**公式 21** (page 159, part1):

$$
\mathrm { Q } _ { s } = \frac { \mathrm { K } _ { \mathrm { v } } \mathrm { P } } { \sqrt { \mathrm { T } } }
$$

**公式 22** (page 160, part1):

$$
\mathbf { K } _ { \mathrm { v } } = { \frac { \mathbf { Q } _ { \mathrm { s } } { \sqrt { \mathrm { T } _ { \mathrm { v } } } } } { \mathbf { P _ { \mathrm { v } } } } }
$$

**公式 23** (page 162, part1):

$$
\mathrm { M _ { i } = \frac { V _ { m i x } \mathrm { , 0 _ { i } , k _ { h } , C _ { i } . 1 0 ^ { - 6 } } } { d } eqno ( 1 ) }
$$

**公式 24** (page 163, part1):

$$
\mathbf { v } = \mathbf { v } _ { \bar { \mathbf { u } } } \cdot \mathbf { h }
$$

**公式 25** (page 163, part1):

$$
\mathrm { V _ { r i s t } = V , K _ { 1 } , \left( \frac { P _ { B } - P _ { l } } { T _ { p } } \right) } \eqno ( 2 )
$$

### 图像（取前 12 张）

![图1 / 认证I型试验流程图(参看第5.3.1条)](../_mineru_assets/ECE R83/19e30aec872681fe46964da8f44444b1da1f857665dd0197c756d5f646b8a3e3.jpg)  
*图1 / 认证I型试验流程图(参看第5.3.1条)* (page 22, part1)

![图2](../_mineru_assets/ECE R83/15fc817cccde3295820fd9d3a95164a2f50d913fd9b39330dda37bcb94196022.jpg)  
*图2* (page 37, part1)

![图4/1](../_mineru_assets/ECE R83/0020c20d9cb549f9830f00ee76cd1f23bdd367b3c6f8693ee4b852681273c992.jpg)  
*图4/1* (page 62, part1)

![图4/2](../_mineru_assets/ECE R83/122d20a85ef62fb194651f0cc4095336768ff253134612eab649eebb6799a6f6.jpg)  
*图4/2* (page 63, part1)

![图/1](../_mineru_assets/ECE R83/ff2884455a0f52ab83981b112f3eb3412f47f030c0525a88233635a7b8aef529.jpg)  
*图/1* (page 107, part1)

![图 page 110](../_mineru_assets/ECE R83/996110c488d40c7742a0a618f7502a2f5620ac5404d05b313e1f9bfe4d56e90c.jpg)  
*page 110, part1*

![图1/3 / I型试验市郊运转循环 (II部) ](../_mineru_assets/ECE R83/afd904adfff197c1527bf78b79d82f9d52016e642143c49284fe9a6ce5e0dafb.jpg)  
*图1/3 / I型试验市郊运转循环 (II部) * (page 115, part1)

![图2/1](../_mineru_assets/ECE R83/cf0f01a4be450ea5c8258f515e13b1cad12fe8acbee0d5113a345f7935ac54b9.jpg)  
*图2/1* (page 118, part1)

![图2/2](../_mineru_assets/ECE R83/d28a79f249160114ff5db8a8b7d81d38c2270310585e1a7e5e68248a2bf8e65a.jpg)  
*图2/2* (page 119, part1)

![图5/1](../_mineru_assets/ECE R83/30befc353be6d808faa794c6b464d979dd21dbde2435c5b2581efa65c6a54de7.jpg)  
*图5/1* (page 135, part1)

![图5/2](../_mineru_assets/ECE R83/a45ab57c3828b2d315885b9c57ee75de62138cff98de2c61606d843bf068a621.jpg)  
*图5/2* (page 140, part1)

![图5/3](../_mineru_assets/ECE R83/cde86d790964de2edcdeb5ef9e3f6872a8dd968915623341862b06402403a1f1.jpg)  
*图5/3* (page 145, part1)

