---
reg_id: ECE R156
region: ece
type: type/version
title: Uniform provisions concerning the approval of vehicles with regards to software
  update and software updates management system
status: active
publication_date: 2021-03-04
implementation_date_new_vehicle: 2021-01-22
source: E/ECE/TRANS/505/Rev.3/Add.155
authentic_source: ECE/TRANS/WP.29/2020/80
jurisdiction: United Nations Economic Commission for Europe (UNECE)
topics:
- software update
- software update management system (SUMS)
- vehicle type approval
- over-the-air (OTA) update
- cybersecurity
- conformity of production
vehicle_categories:
- M
- N
- O
- R
- S
- T
tags:
- type/version
- reg/ece
- status/active
- status/verified
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\156\R156e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: high
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段，B中未明确提及标准机构名称。
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段，B中未提及。
- field: equivalent_to
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段，B中未提及。
- field: supersedes
  status: unsure
  extracted: null
  original: null
  note: A中未提取此字段，B中未提及。
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A中未提取具体技术要求的数值限值，B中亦未提供具体限值。
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-22'
_mineru_outputs_dir: outputs\1f07ecb4aa51e8be
---

**UN Regulation No. 156 - Software Update and Software Update Management System**

**1. Scope**
This Regulation applies to vehicles of Categories M, N, O, R, S, and T (as defined in Consolidated Resolution R.E.3) that permit software updates.

**2. Definitions**
Key definitions include:
*   **Vehicle type:** Vehicles sharing the manufacturer's designation and essential aspects of software update process design.
*   **RX Software Identification Number (RXSWIN):** A manufacturer-defined identifier for type-approval-relevant software in an Electronic Control System related to Regulation X.
*   **Software update:** A package to upgrade software, including configuration parameter changes.
*   **Software Update Management System (SUMS):** A systematic approach defining organizational processes and procedures to comply with software update delivery requirements.
*   **Over-the-Air (OTA) update:** Wireless data transfer for updates.
*   **Integrity validation data:** Data representation (e.g., checksums, hash values) to detect errors or changes in digital data.

**3. Application for Approval**
The vehicle manufacturer or representative submits the application, accompanied by required documents in triplicate, a description per Annex 1, and a **Certificate of Compliance for SUMS** (see para. 6). A representative vehicle must be submitted. Documentation is split into a formal package for the authority and additional material open for inspection, both to be retained for at least 10 years after production ends.

**4. Markings**
Approved vehicles must bear an international approval mark (a circle with "E" and country code, plus "156R" and approval number). The mark must be legible, indelible, and placed on or near the vehicle data plate. Examples are in Annex 3.

**5. Approval**
Approval Authorities grant type approval for software update procedures only to compliant vehicle types. Verification is done via testing. Notices of approval/extension/refusal are communicated to contracting parties using the form in Annex 2. Approval requires the manufacturer to have satisfactory SUMS arrangements.

**6. Certificate of Compliance for Software Update Management System**
*   Contracting Parties appoint an Approval Authority to assess the manufacturer and issue this certificate.
*   The manufacturer applies with documents describing the SUMS and a signed declaration (model in Annex 1, Appendix 1).
*   The certificate is valid for a maximum of **three years** and can be withdrawn for non-compliance.
*   The manufacturer must inform the authority of any changes affecting the certificate's relevance.
*   Expiry of the manufacturer's SUMS certificate does not invalidate existing vehicle type approvals.

**7. General Specifications**
*   **7.1 Requirements for the Manufacturer's SUMS:** Details processes to be verified (e.g., documentation, identification of software/hardware, target vehicle identification, compatibility checks, impact assessment on type-approved/safety systems, user notification). Requires recording specific information for each update. Mandates security processes to protect updates and verification/validation procedures. For OTA updates, requires processes to assess safety during driving and ensure skilled actions are performed by qualified personnel.
*   **7.2 Requirements for the Vehicle Type:**
    *   **Software Updates:** Authenticity and integrity must be protected. If using RXSWIN, it must be uniquely identifiable, updatable, and easily readable via OBD port (or software versions declared). RXSWIN/software versions must be protected against unauthorized modification.
    *   **OTA Updates:** The vehicle must be able to restore systems or enter a safe state after a failed update. Updates must only execute with sufficient power. Safety during execution must be ensured. The user must be informed before execution (purpose, changes, duration, unavailable functionalities, instructions). The vehicle must prevent driving during unsafe updates. The user must be informed of success/failure and changes after execution. Preconditions must be met before execution.

**8. Modification and Extension of Vehicle Type**
Modifications affecting performance or documentation must be notified. The authority may confirm compliance, require further tests, or extend/refuse approval. Extensions are communicated via Annex 2 form.

**9. Conformity of Production**
Procedures must comply with the 1958 Agreement. Test results and documents must be retained (max 10 years after production ends). The Approval Authority verifies control methods periodically (normally every 3 years) and validates the manufacturer's processes and decisions, including cases where updates were not notified.

**10. Penalties for Non-Conformity**
Approval may be withdrawn for non-compliance or if samples fail. Withdrawal is communicated to contracting parties via Annex 2 form.

**11. Production Definitively Discontinued**
The approval holder must inform the authority, which then notifies other parties.

**12. Names and Addresses of Technical Services and Approval Authorities**
Contracting parties communicate these to the UN Secretariat.

**Annexes**
*   **Annex 1:** Information document required for application.
*   **Appendix 1:** Model declaration of compliance for SUMS.
*   **Annex 2:** Model communication form for approval/extension/refusal/withdrawal.
*   **Annex 3:** Examples of approval mark arrangement.
*   **Annex 4:** Model Certificate of Compliance for SUMS.
