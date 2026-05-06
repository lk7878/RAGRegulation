---
target_file: 01_Wiki/regulations/cn/GB 4785-2006_dup2.md
target_reg_id: GB 4785-2006
target_section: ""
target_anchor: ""

severity: medium
category: completeness
status: resolved

created: 2026-04-19T10:35:27
resolved: 2026-04-19T10:50:00
resolver: cascade

tags:
  - audit/resolved
  - audit/severity-medium
  - audit/category-completeness
---

## Issue

摘要段只有 2 句，建议扩展到 3-5 句，提一下适用车辆类别。

## Expected

补充 1-2 句 scope 细节。

## Resolution

已扩展 `summary` 字段从 1 句到 3 句：
1. **原句保留**：规定了汽车及挂车外部照明和光信号装置的安装技术要求、试验方法和检验规则
2. **新增适用范围**：适用于 M、N 和 O 类汽车及挂车（依据正文 4.1 段）
3. **新增覆盖装置清单**：前照灯、前/后雾灯、前/后位灯、制动灯、倒车灯、转向信号灯、驻车灯、侧标志灯、回复反射器及后牌照板照明装置（依据正文 4.2.1-4.2.16 段）
4. **新增等价信息**：技术内容上等同采用 ECE R48（已在 FM `equivalent_to` 字段记录）

**备注**：
- 用户原 category 填为 `classification`，实际更符合 `completeness`（内容完整性），已改为 completeness
- 本次只改 summary，未触碰 `cross_check_overall_confidence: low` 和 `cross_check_flags`（这些是 Phase 2 数据质量问题，需单独处理）

## Related

- Target: `@D:\CcVault\01_Wiki\regulations\cn\GB 4785-2006_dup2.md`
- Equivalent: ECE R48（见 equivalent_to 字段）
