---
reg_id: ECE R144 Am1
title: Uniform provisions concerning Accident Emergency Call Components (AECC), Accident
  Emergency Call Devices (AECD) and Vehicles with regard to their Accident Emergency
  Call Systems (AECS)
region: ece
type: type/amendment
status: active
publication_date: 2020-11-03
implementation_date_new_vehicle: 2020-09-25
source_file: 国外法规\ECE标准\标准法规-UNECE\121~160\144\R144am1e.pdf
tags:
- type/amendment
- reg/ece
- status/active
- status/needs-review
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\144\R144am1e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
implementation_date_new_vehicle_conf: low
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 和 B 均未明确提及 standard_body 字段。
- field: implementation_date_new_vehicle
  status: mismatch
  extracted: 2020-09-25
  original: 25 September 2020
  note: 日期一致，但 B 中描述为“Date of entry into force”（生效日期），A 字段名为“implementation_date_new_vehicle”（新车型实施日期）。B
    未明确区分新车型和在用车型的实施日期，因此 A 的字段名与 B 的表述不完全对应，但日期值匹配。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 未提及针对在用车辆（in-use）的单独实施日期。
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
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-23'
_mineru_outputs_dir: outputs\c72ca7097e9c0ff0
---

# UN Regulation No. 144 - Amendment 1

**Supplement 1 to the original version of the Regulation**
**Date of entry into force:** 25 September 2020

**Authentic and legally binding text:** ECE/TRANS/WP.29/2020/24.

## Scope
This amendment provides uniform provisions concerning:
*   **Ia.** Accident Emergency Call Components (AECC)
*   **Ib.** Accident Emergency Call Devices (AECD) intended for vehicles of categories M1 and N1
*   **II.** Vehicles with regard to their Accident Emergency Call Systems (AECS) when equipped with an approved type AECD
*   **III.** Vehicles with regard to their Accident Emergency Call Systems (AECS) when equipped with a non-approved type AECD

## Key Amendments

### 1. Testing Procedures (Paragraph 7.3.11.)
*   The testing procedures in Annex 10 can be performed either on the AECC unit (including post-processing ability) or directly on the GNSS receiver as part of the AECC.

### 2. AECD Requirements
*   **Position Determination (Paragraph 17.3.):** AECD compliance regarding positioning capabilities must be demonstrated using the test methods in Annex 10 (Test methods for the navigation solutions). This must be indicated in Annex 2, item 12 of the communication document.
*   **Information and Warning Signal (Paragraph 17.5.):** At the applicant's request, verification of AECD information and warning signals may be part of the AECD type approval (Part Ib). If included, provisions 17.5.1. to 17.5.3. apply and must be indicated in Annex 2, item 13. If not part of Part Ib approval, it becomes subject to Part II (vehicle) approval.
*   **Back-up Power Supply (Paragraph 17.6.4.):** For an AECD with a back-up power supply, it must be verified (at applicant's request) that the AECD can operate autonomously for: first, ≥5 minutes in voice communication mode; followed by 60 minutes in call-back/idle mode (registered in a network); and finally, ≥5 minutes in voice communication mode. This must be indicated in Annex 2, item 11.

### 3. Vehicle Requirements (Part II & III) - Impact Test Documentation
For extending type approvals to this regulation, or approving vehicle types already approved under UN R94 or R95 prior to this regulation's entry into force, compliance can be demonstrated using existing documentation (report, images, simulation data, or equivalent) showing that during the relevant impact test:
*   A triggering signal was generated.
*   The installation of the AECD/AECS was not adversely affected by the impact.

Specific applications:
*   **UN R94 (Frontal Collision) - Paragraphs 26.2.1.2.2. & 35.5.1.2.2.**
*   **UN R95 (Lateral Collision) - Paragraphs 26.2.1.3.2., 26.2.2.1.2., 35.5.1.3.2., & 35.5.2.1.2.**

### 4. AECS Requirements (Paragraph 26.3.)
*   **Position Determination:** AECS compliance regarding positioning capabilities must be demonstrated by performing the test methods in Annex 10 (Test methods for the navigation module). This must be indicated in Annex 3, item 10.
*   **Data Output:** The AECS must be able to output the navigation solution in NMEA-0183 protocol format (RMC, GGA, VTG, GSA, and GSV messages). The setup for outputting these messages to external devices must be described in the operation manual.

### 5. AECS Malfunction Warning (Paragraph 26.5.3.)
*   A warning signal must be provided in case of AECS internal malfunction.
*   Visual indication of the malfunction must be displayed while the failure is present. It may be cancelled temporarily but must be repeated whenever the ignition or vehicle master control switch is activated (whichever is applicable).

### 6. Post-Impact Power Supply (Paragraph 26.7.2.3.)
*   After the relevant impact test under UN R94 and/or R95, the AECS power supply must be able to supply power to the AECS. Verification can use one of the methods described in Annex 11 of this regulation.

### 7. Vehicle Type Approval (Paragraph 34.1.)
*   Before granting approval, the competent authority must ensure all parts listed in paragraph 35.10.1 are tested according to Annex 9.
*   If the AECS is fed by a power supply other than the back-up supply described in paragraph 35.10.2, that power supply must also be tested according to Annex 9.
