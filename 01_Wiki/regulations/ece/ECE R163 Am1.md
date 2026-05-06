---
reg_id: ECE R163 Am1
type: type/amendment
region: ece
title: Uniform provisions concerning the approval of vehicle alarm system and approval
  of a vehicle with regard to its vehicle alarm system
description: Amendment 1 to UN Regulation No. 163, introducing provisions for digital
  keys within vehicle alarm systems.
source_file: 国外法规\ECE标准\标准法规-UNECE\161~\163\R163am1e.pdf
entry_into_force: 2022-10-08
status: active
version: Amendment 1
standard_body: UNECE
tags:
- type/amendment
- regulation/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\161~\163\R163am1e.pdf
publication_date: 2022-11-16
verified_by: deepseek-v3
cross_check_overall_confidence: medium
publication_date_conf: low
cross_check_flags:
- field: publication_date
  status: normalized
  extracted: 2022-11-16
  original: 2022-11-16 (原文为“16 November 2022”)
  note: '[Auto-reclassified] Same date after parsing: 2022-11-16 == 2022-11-16 (原文为“16
    November 2022”)'
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: B 未提及新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及在用车型实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: B 未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: B 未提及替代关系。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: 此修正案主要涉及定义和程序要求，无具体数值限值。
stage2_reclassified:
- publication_date
stage2_reclassified_at: '2026-04-18'
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-22'
_mineru_outputs_dir: outputs\8fb8dea432b8f4d0
---

### 主要修订摘要

本修正案 (Amendment 1) 对 **UN Regulation No. 163**（关于车辆报警系统及其安装车辆型式批准的统一规定）进行了补充，主要引入了与**数字钥匙**相关的条款。

#### 1. 新增定义 (第2条)
- **2.14. 主要用户**: 能够授权数字钥匙的用户。可以存在多个主要用户。
- **2.15. 数字钥匙**: 指可由主要用户通过特定流程传输到多个设备的钥匙。

#### 2. 新增一般要求 (第5条与第10条)
- **5.10.** 数字钥匙应符合附件9的规定。
- **10.7.** 数字钥匙应符合附件9的规定。

#### 3. 新增附件9：数字钥匙的安全规定

**目的**: 规定用于操作车辆“报警系统”的数字钥匙的文件和验证要求。

**主要内容**:
- **定义**:
    - **授权流程**: 提供可操作车辆“报警系统”的数字钥匙的任何方法。
    - **撤销流程**: 阻止数字钥匙操作车辆“报警系统”的任何方法。
- **文件要求**: 车辆制造商需为型式批准提供以下文件：
    1.  授权流程的描述。
    2.  撤销流程的描述。
    3.  数字钥匙撤销流程中为确保车辆安全运行而设计的安全措施描述。
- **安全操作要求**:
    1.  数字钥匙只能通过授权流程传输到设备。
    2.  必须存在撤销流程。
 - 数字钥匙的撤销不得导致不安全状况。需使用功能安全标准（如ISO 26262）和预期功能安全标准（如ISO/PAS 21448）进行风险降低分析，以记录因撤销数字钥匙对乘员造成的风险及实施风险缓解措施后的风险降低情况。
 - 主要用户应能识别已授权的注册数字钥匙的数量。
    3.  车辆用户手册或车内其他通信方式中应包含详细信息，至少包括：
 - (a) 数字钥匙的授权方法
 - (b) 数字钥匙的撤销方法
- **网络安全**: 系统的有效性不得受到网络攻击、网络威胁和漏洞的不利影响。安全措施的有效性应通过符合 **UN Regulation No. 155** 来证明。
- **验证**: 数字钥匙功能的验证应在制造商根据第3条提供的文件支持下进行。
- **审核员/评估员能力**: 本附件的评估只能由具备必要技术和行政知识的审核员/评估员进行。他们应特别具备ISO 26262-2018和ISO/PAS 21448的审核/评估能力，并能根据UN R155和ISO/SAE 21434建立与网络安全方面的必要联系。此能力应通过适当的资格或等效培训记录来证明。

**关联法规**:
- 本修正案引用了 **UN Regulation No. 155**（网络安全与网络安全管理系统）以及 **ISO/SAE 21434**（道路车辆网络安全工程）作为网络安全合规的依据。
- 要求安全分析参考 **ISO 26262**（功能安全）和 **ISO/PAS 21448**（预期功能安全）标准。
