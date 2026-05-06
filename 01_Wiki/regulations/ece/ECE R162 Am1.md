---
reg_id: ECE R162 Am1
type: type/amendment
region: ece
title: Uniform technical prescriptions concerning approval of immobilizers and approval
  of a vehicle with regard to its immobilizer
status: active
entry_into_force_date: 2022-10-08
source_file: 国外法规\ECE标准\标准法规-UNECE\161~\162\R162am1e.pdf
source_page: unknown
tags:
- type/amendment
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\161~\162\R162am1e.pdf
publication_date: 2023-03-20
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 中未明确提取 standard_body 字段，B 中未直接提及类似字段。
- field: implementation_date_new_vehicle
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及新车型实施日期。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及在用车型实施日期。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及等效法规。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未提及替代关系。
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-25'
_mineru_outputs_dir: outputs\9d714197d8566e42
---

### 主要修订内容

本修正案主要引入了关于“数字钥匙”的定义、要求和安全规定。

#### 1. 定义修订与新增
*   **2.9. "Key" (钥匙)**: 修订为指任何旨在提供操作锁定系统方法的机械和/或电子解决方案，该锁定系统专为被该机械和/或电子解决方案操作而设计和构造。
*   **新增 2.14. "Primary user" (主要用户)**: 指能够授权数字钥匙的用户。可以有多名主要用户。
*   **新增 2.15. "Digital key" (数字钥匙)**: 指旨在通过专门流程由主要用户传输到多个设备的钥匙。
*   **新增 2.12. "Close proximity" (近距离)**: 指小于6米的距离。

#### 2. 一般要求修订
*   **新增 5.1.11.**: 规定数字钥匙应符合附件9的规定。

#### 3. 新增附件
*   **新增附件8**: (保留)
*   **新增附件9**: 数字钥匙的安全规定

### 附件9：数字钥匙的安全规定

#### 1. 总则
本附件旨在规定用于操作车辆“防止未经授权使用装置”的数字钥匙的文件和验证要求。

#### 2. 定义
*   **2.1. "Authorization process" (授权流程)**: 提供可操作车辆“防止未经授权使用装置”的数字钥匙的任何方法。
*   **2.2. "Revocation process" (撤销流程)**: 阻止数字钥匙操作车辆“防止未经授权使用装置”的任何方法。
*   **2.3. "Boundary of functional operation" (功能操作边界)**: 定义数字钥匙能够操作车辆“防止未经授权使用装置”的外部物理限制（例如距离）边界。

#### 3. 文件
车辆制造商应为型式认证提供以下文件：
*   3.1. 授权流程的描述。
*   3.2. 撤销流程的描述。
*   3.3. 功能操作边界的描述。
*   3.4. 数字钥匙撤销流程内设计的安全措施描述，以确保车辆的安全操作。

#### 4. 安全操作要求
*   **4.1.**: 数字钥匙应仅通过授权流程传输到设备。
*   **4.2.**: 应存在撤销流程。
    *   **4.2.1.**: 数字钥匙的撤销不应导致不安全状况。应使用功能安全标准（如ISO 26262）和预期功能安全标准（如ISO/PAS 21448）进行风险降低分析，记录因数字钥匙撤销对车辆乘员造成的风险，并记录实施已识别的风险缓解功能或特性所带来的风险降低。
    *   **4.2.2.**: 主要用户应能够识别已授权的注册数字钥匙的数量。
*   **4.3. 防止未经授权使用装置的功能操作边界**:
    *   **4.3.1.**: 解锁防止未经授权使用装置要求检测到已授权的注册数字钥匙在车辆内部或车辆近距离内。
    *   **4.3.2.**: 第4.3.1段的要求不适用于UN Regulation No. 79中定义的远程控制操纵和远程控制泊车期间。
*   **4.4.**: 详细信息应包含在车辆的用户手册中，或通过车辆内的任何其他通信方式提供；至少，此信息应包括：
    *   (a) 数字钥匙的授权方法；
    *   (b) 数字钥匙的撤销方法。
*   **5.**: 系统的有效性不应受到网络攻击、网络威胁和漏洞的不利影响。安全措施的有效性应通过符合UN Regulation No. 155来证明。

#### 6. 验证
数字钥匙功能的验证应在制造商根据第3段规定的文件支持下进行。

#### 7. 审核员/评估员能力
本附件下的评估应仅由具备必要技术和行政知识的审核员/评估员进行。他们应特别具备作为ISO 26262-2018（道路车辆功能安全）和ISO/PAS 21448（道路车辆预期功能安全）审核员/评估员的能力；并且应能够根据UN Regulation No. 155和ISO/SAE 21434与网络安全方面建立必要的联系。此能力应通过适当的资格或其他等效的培训记录来证明。
