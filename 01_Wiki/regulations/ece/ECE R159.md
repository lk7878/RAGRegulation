---
reg_id: ECE R159
region: ece
type: type/version
title: Uniform provisions concerning the approval of motor vehicles with regard to
  the Moving Off Information System for the Detection of Pedestrians and Cyclists
status: active
publication_date: 2021-07-06
implementation_date_new_vehicle: 2021-06-10
source_file: R159e.pdf
tags:
- type/version
- reg/ece
- status/active
- status/verified
_continuation_passes: 1
extracted_by: deepseek-v3
source_pdf: 国外法规\ECE标准\标准法规-UNECE\121~160\159\R159e.pdf
verified_by: deepseek-v3
cross_check_overall_confidence: medium
publication_date_conf: low
cross_check_flags:
- field: standard_body
  status: unsure
  extracted: null
  original: null
  note: A 中未提取此字段，B 中未明确提及标准机构名称。
- field: publication_date
  status: normalized
  extracted: 2021-07-06
  original: 2021-06-10
  note: 'B 中 "Date of entry into force as an annex to the 1958 Agreement: 10 June
    2021" 是法规生效日期，但未明确给出发布日期。A 的 "2021-07-06" 可能对应 B 文件头部的 "6 July 2021"。由于 B 未明确说明
    "publication_date"，但文件日期为 7月6日，而 A 提取为发布日期，存在不匹配。'
  recheck_reason: 原文文件头部明确标注"6 July 2021"，抽取数据"2021-07-06"为规范化日期格式，实质一致
- field: implementation_date_in_use
  status: unsure
  extracted: null
  original: null
  note: B 中未提及在用车的实施日期。
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
- field: 技术要求限值
  status: unsure
  extracted: null
  original: null
  note: A 中未提取具体技术要求限值，B 中虽有技术描述但未在提供段落中给出具体限值数字。
recheck_at: '2026-04-18'
_ocr_upgraded: mineru
_mineru_content_hash: a12ec5407403a150
_mineru_outputs_dir: outputs/a12ec5407403a150
_mineru_blocks:
  tables: 2
  formulas: 0
  images: 5
_mineru_merged_at: '2026-04-22'
---

**UN Regulation No. 159**

**Uniform provisions concerning the approval of motor vehicles with regard to the Moving Off Information System for the Detection of Pedestrians and Cyclists**

**Contents**
0. Introduction
1. Scope
2. Definitions
3. Application for approval
4. Approval
5. Specifications
6. Test procedure
7. Modification of vehicle type and extension of approval
8. Conformity of production
9. Penalties for non-conformity of production
10. Production definitively discontinued
11. Names and addresses of Technical Services responsible for conducting approval tests, and of Type Approval Authorities
Appendix 1
Annexes
1 Communication
2 Arrangements of approval marks
3 Test method for determining blind spot boundary

**0. Introduction (for information)**
0.1. Low-speed moving off from rest manoeuvres that involve collisions between M2, M3, N2 and N3 vehicle category vehicles (subject vehicles) and pedestrians and cyclists have serious consequences for these vulnerable road users (VRUs). In the past, VRU safety was raised by increasing the number of mirrors to provide better visibility of the area in front of the vehicle. Since collisions with these characteristics still occur and advanced driver assistance systems have been introduced in a lot of vehicle segments, it is obvious to use such assistance systems for avoiding accidents between subject vehicles and VRUs.
0.2. Theoretical considerations show that the criticality of traffic situations that involve subject vehicles and VRUs can be significant due to the misunderstandings of the situation by the vehicle operators. In some cases, the increase in situation criticality can occur so suddenly that high-urgency warnings, intended to generate a driver reaction to the situation, cannot be activated early enough for the driver to react in time. In general, driver reactions to any information (high/low urgency signals) can be expected only after a certain reaction time. This response time, particularly during close-proximity manoeuvres, is much longer than the time required to avoid the accident in many situations – the accident cannot be avoided despite the warning.
0.3. High-urgency warnings during a driving situation are only justified should the probability for an accident be high – otherwise vehicle drivers tend to ignore the system alerts. Should lower urgency information signals be activated sufficiently early, however, it may help the driver rather than annoy them. It is assumed to be possible to design a human-machine interface (HMI) for moving-off driver assistance systems in a way that it does not annoy drivers when the information is not needed, for instance by requiring the use of a less intrusive signal mode.
0.4. Therefore, this Regulation requires the activation of a proximity information signal in case pedestrians or cyclists enter the critical blind spot area in front of the vehicle, should the subject vehicle either be preparing to move off from rest in a straight line or be travelling straight ahead at low-speeds. This signal shall be deactivated automatically in case of system failure or contamination of the sensors, whilst manual deactivation may also be possible through a sequence of actions by the driver to avoid unintentional deactivation.
0.5. Furthermore, this Regulation asks for an additional signal, which shall be given when the collision becomes imminent, e.g. when the vehicle accelerates from rest and the pedestrian or cyclist is located directly in front of the vehicle. The activation and deactivation strategy for this collision warning signal may be determined by the manufacturer; however, in case of system failure or sensor contamination, the proximity information signal and collision warning signal shall be deactivated together.
0.6. This Regulation defines a test procedure based on subject vehicles that are stationary, moving-off from rest and moving ahead at low-speeds in a straight line for speeds of 10 km/h or less. Collision analysis data shows that the provision of information and warnings during these vehicle manoeuvres is appropriate since the information signal needs to be present sufficiently early to alert the driver of pedestrians and cyclists in close-proximity to the front end of the vehicle.
0.7. This Regulation cannot cover all the traffic conditions and infrastructure features in the type-approval process; this Regulation recognises that the performances required in this Regulation cannot be achieved in all conditions (vehicle condition, road environment, weather conditions and traffic scenarios etc. may affect the system performances). Actual conditions and features in the real world should not result in false warnings to the extent that they encourage the driver to switch the system off.

**1. Scope**
1.1. This Regulation applies to the approval of vehicles of categories M2, M3, N2 and N3 with regard to an onboard system to detect and inform the driver of the presence of pedestrians and cyclists in the close-proximity forward blind-spot of the vehicle and, if deemed necessary based on manufacturer strategy, warn the driver of a potential collision.
1.2. The requirements of this Regulation are so worded as to apply to vehicles which are developed for right-hand traffic. In vehicles that are developed for left-hand traffic, these requirements shall be applied by inverting the criteria, where appropriate.
1.3. The following vehicles of category M and N shall be exempted from this Regulation: Vehicles where installation of any device for moving off information system is incompatible with their on-road use may be partly or fully exempted from this Regulation, subject to the decision of the Type Approval Authority.

**2. Definitions**
For the purposes of this Regulation:
2.1. "Moving Off Information System (MOIS)" means a system to detect and inform the driver of the presence of pedestrians and cyclists in the close-proximity forward blind-spot of the vehicle and, if deemed necessary based on manufacturer strategy, warn the driver of a potential collision.
2.2. "Approval of a vehicle type" means the full procedure whereby a Contracting Party to the Agreement certifies that a vehicle type meets the technical requirements of this Regulation.
2.3. "Vehicle type with regard to its Moving Off Information System" means a category of vehicles which do not differ in such essential respects as:
(a) The manufacturer's trade name or mark;
(b) Vehicle features which significantly influence the performances of the MOIS;
(c) The type and design of the MOIS.
2.4. "Subject vehicle" means the vehicle being tested.
2.5. "Vulnerable Road User (VRU)" means an adult or child pedestrian or an adult or child cyclist.
2.6. "Information signal" means a signal emitted by the MOIS with the purpose of informing the vehicle driver about a VRU in close-proximity to the front of the vehicle.
2.7. "Collision warning signal" means a signal emitted by the MOIS with the purpose of warning the vehicle driver when the MOIS has detected a potential frontal collision with a VRU in close-proximity to the front of the vehicle.
2.8. "Vehicle master control switch" means the device by which the vehicle's on-board electronics system is brought, from being switched off, as in the case where a vehicle is parked without the driver being present, to a normal operation mode.
2.9. "Initialisation" means the process of setting-up the operation of the MOIS after the vehicle master control switch is activated until it is fully functional.
2.10. "Common space" means an area on which two or more information functions (e.g. symbols) may be displayed, but not simultaneously.
2.11. "Ocular reference point" means the middle point between two points 65 mm apart and 635 mm vertically above the reference point which is specified in Annex 1 of ECE/TRANS/WP.29/78/Rev.6 on the driver's seat. The straight line joining the two points runs perpendicular to the vertical longitudinal median plane of the vehicle. The centre of the segment joining the two points is in a vertical longitudinal plane which shall pass through the centre of the driver's designated seating position, as specified by the vehicle manufacturer.
2.12. "Vehicle front" means the plane perpendicular to the median longitudinal plane of the vehicle and touching its foremost point, disregarding the projection of devices for indirect vision and any part of the vehicle greater than 2.0 m above the ground.
2.13. "Nearside" means the right side of the vehicle for right-hand traffic.
2.14. "Nearside vehicle plane" means the plane parallel to the median longitudinal plane of the vehicle and touching its most outboard point in the nearside direction forward of the driver ocular reference point, disregarding the projection of devices for indirect vision and any part of the subject vehicle higher than 2.0 m above the ground.
2.15. "Offside" means the left side of the vehicle for right-hand traffic
2.16. "Offside vehicle plane" means the plane parallel to the median longitudinal plane of the vehicle and touching its most outboard point in the offside direction forward of the driver ocular reference point, disregarding the projection of devices for indirect vision and any part of the subject vehicle higher than 2.0 m above the ground.
2.17. "Vehicle width" means the distance between the nearside and offside vehicle planes.
2.18. "Vehicle trajectory" means the connection of all positions within the vehicle width where the vehicle front has been or will be during the test runs.
2.19. "Soft target" means a target that will suffer minimum damage and cause minimum damage to the subject vehicle in the event of a collision.
2.20. "Pedestrian test target" means an adult or child sized pedestrian simulated by a soft target device specified according to ISO 19206-2:2018.
2.21. "Cyclist test target" means an adult sized cyclist and bicycle simulated by a soft target and bicycle device specified according to ISO (CD) 19206-4.
2.22. "Blind spot boundary" means the line, described as defined in Annex 3, that joins all points located at the boundaries of the visible areas forward of the vehicle front and in close-proximity to the subject vehicle.
2.23. "Collision point" means the position where the trajectory of any point of the vehicle front would intersect with any VRU soft target reference point should a moving off or low-speed manoeuvre be performed by the vehicle.
2.24. "Forward separation distance" means the distance in the forward direction between the vehicle front and the nearest point of the soft target.
2.25. "Maximum forward separation plane" means the plane perpendicular to the longitudinal plane of the vehicle representing the greatest forward separation distance that the MOIS is required to detect the presence of a VRU. The distance of this plane from the vehicle front shall be selected as either 3.7 m or the most forward point of the blind spot boundary at the manufacturer’s choosing, and shall be no less than 1.0 m.
2.26. "Minimum forward separation plane" means the plane perpendicular to the longitudinal plane of the vehicle representing the shortest forward separation distance that the MOIS is required to detect the presence of a VRU. The distance of this plane from the vehicle front shall be 0.8 m.
2.27. "Nearside separation plane" means the plane parallel to the longitudinal plane of the vehicle and located 0.5 m outboard from the nearside vehicle plane.
2.28. "Offside separation plane" means the plane parallel to the longitudinal plane of the vehicle and located 0.5 m outboard from the offside vehicle plane.
2.29. "Forward vehicle mode" means the vehicle mode when the powertrain moves the vehicle forward, on release of the brake system or by the application of pressure to the accelerator pedal (or activation of an equivalent control).
2.30. "Potential moving off manoeuvre" means the subject vehicle being stationary, the vehicle master control switch activated, the vehicle in a normal operation mode and with the forward vehicle mode or a forward gear engaged/selected.
2.31. "Low-speed manoeuvre" means the subject vehicle being in a normal operation mode, moving forward in a straight line at speeds of below 10 km/h.
2.32. "Last Point of Information (LPI)" means the point at which the information signal shall have been given.

**3. Application for approval**
3.1. The application for approval of a vehicle type with regard to the Moving Off Information Systems (MOIS) shall be submitted by the vehicle manufacturer or by their authorized representative.
3.2. It shall be accompanied by the documents mentioned below in triplicate and include the following particular:
3.2.1. A description of the vehicle type with regard to the items mentioned in paragraph 5., together with dimensional drawings and the documentation as referred to in paragraph 6.1. The numbers and/or symbols identifying the vehicle type shall be specified.
3.3. A vehicle representative of the vehicle type to be approved shall be submitted to the Technical Service conducting the approval tests.

**4. Approval**
4.1. If the vehicle type submitted for approval pursuant to this Regulation meets the requirements of paragraph 5. below, approval of that vehicle type shall be granted.
4.2. The conformity of the requirements in paragraph 5. shall be verified with the test procedure as defined in paragraph 6., however its operation shall not be limited to these specific test conditions.
4.3. An approval number shall be assigned to each vehicle type approved; its first two digits (00 for this Regulation in its initial form) shall indicate the series of amendments incorporating the most recent major technical amendments made to this Regulation at the time of issue of the approval. The same Contracting Party shall not assign the same number to the same vehicle type equipped with another type of MOIS, or to another vehicle type.
4.4. Notice of approval or of refusal or withdrawal of approval pursuant to this Regulation shall be communicated to the Parties to the Agreement applying this Regulation by means of a form conforming to the model in Annex 1 and photographs and/or plans supplied by the applicant being in a format not exceeding A4 (210 x 297 mm), or folded to that format, and on an appropriate scale.
4.5. There shall be affixed, conspicuously and in a readily accessible place specified on the approval form, to every vehicle conforming to a vehicle type approved under this Regulation, an international approval mark conforming to the model described in Annex 2, consisting of either:
4.5.1. A circle surrounding the letter "E" followed by:
(a) the distinguishing number of the country which has granted approval; and
(b) the number of this Regulation, followed by the letter "R", a dash and the approval number to the right of the circle prescribed in this paragraph;
or
4.5.2. An oval surrounding the letters "UI" followed by the Unique Identifier.
4.6. If the vehicle conforms to a vehicle type approved under one or more other UN Regulations annexed to the Agreement, in the country which has granted approval under this Regulation, the symbol prescribed in paragraph 4.5. above need not be repeated. In such a case, the UN Regulation and approval numbers and the additional symbols shall be placed in vertical columns to the right of the symbol prescribed in paragraph 4.5. above.
4.7. The approval mark shall be clearly legible and be indelible.
4.8. The approval mark shall be placed close to or on the vehicle data plate.

**5. Specifications**
5.1. General requirements
5.1.1. Any vehicle fitted with a MOIS complying with the definition of paragraph 2.1. above shall meet the requirements contained in paragraphs 5.2. to 5.8. of this Regulation.
5.1.2. The effectiveness of the MOIS shall not be adversely affected by magnetic or electrical fields. This shall be demonstrated by compliance with the technical requirements and transitional provisions of UN Regulation No. 10, 05 series of amendments or any later series of amendments.
5.2. Performance requirements
5.2.1. The MOIS shall at least operate during all potential moving off manoeuvres and low-speed manoeuvres, for ambient light conditions above 15 Lux with or without passing beam headlamps activated.
5.2.2. The MOIS shall inform the driver about VRUs in close-proximity to the vehicle front that might be endangered during a potential moving off manoeuvre or low-speed manoeuvre. This information shall be provided to the driver so that the vehicle may be prevented by the driver from interacting with the trajectory of the VRU.
5.2.2.1. The information signal shall be provided at least for as long as the conditions specified in paragraphs 5.2.2.2. and 5.2.2.3. are fulfilled.
5.2.2.2. Potential moving-off manoeuvre
5.2.2.2.1. When performing a potential moving-off manoeuvre, the MOIS shall provide an information signal for VRUs moving at speeds of between 3 km/h and 5 km/h, when travelling from the nearside and offside of the vehicle in a direction perpendicular to the vehicle median longitudinal plane and located within an area bounded by the maximum and minimum forward separation planes and the nearside and offside separation planes.
5.2.2.3. Low-speed manoeuvre
5.2.2.3.1. When performing a low-speed manoeuvre, the MOIS shall provide an information signal for adult and child cyclists that are stationary or moving forward in a direction parallel to the vehicle median longitudinal plane at speeds of between 0 km/h and 10 km/h and located within an area bounded by the nearside and offside vehicle planes and the maximum and minimum forward separation planes.
5.2.2.3.2. When a vehicle performing a low-speed manoeuvre has already detected an adult or child cyclist and provided an information signal in accordance with 5.2.2.3.1., the MOIS shall maintain the information signal even if the vehicle comes to a standstill. The information signal shall be maintained for as long as the cyclist remains within an area bounded by the nearside and offside vehicle planes and the maximum and minimum forward separation planes.
5.2.2.3.3. When performing a turning manoeuvre, the MOIS detection strategy may be adjusted. It is not required to adjust the sensors to the steering angle. The detection adjustment strategy shall be explained in the information referred to in paragraph 6.1. The Technical Service shall verify the operation of the system according to the strategy.
5.2.2.4. The information signal shall meet the requirements of paragraph 5.6.
5.2.3. The manufacturer shall demonstrate, to the satisfaction of the Technical Service and Type Approval Authority, through documentation, simulation or other means, that the MOIS is performing as specified for smaller cyclists and bicycles, similar in size to a child cyclist.
5.2.4. The manufacturer shall demonstrate, to the satisfaction of the Technical Service and Type Approval Authority, through documentation, simulation or other means, that the number of false reactions due to the detection of VRUs and static objects (such as cones, traffic signs, hedges and parked cars) located outside of the boundaries defined in 5.2.2.2 and 5.2.2.3 for the relevant vehicle manoeuvres are minimised.
5.3. Automatic Deactivation
5.3.1. The MOIS shall automatically deactivate if it malfunctions or cannot operate properly due to its sensor devices becoming contaminated by ice, snow, mud, dirt or similar material. The MOIS may also automatically deactivate due to ambient light conditions below that specified in paragraph 5.2.1.
5.3.2. Automatic deactivation shall be indicated by the failure warning signal specified in paragraph 5.8.
5.3.3. The MOIS shall automatically reactivate when the normal function of the sensors is verified. This shall be tested in accordance with the provisions of paragraphs 6.8 (failure detection test) and 6.9. (automatic deactivation test).
5.4. Manual deactivation
5.4.1. It may be possible to manually deactivate the MOIS.
5.4.2. Manual deactivation shall be through a sequence of intentional actions to be carried out by the driver, for example by requiring a single input exceeding a certain threshold of time or a double press, or two separate but simultaneous inputs.
5.4.3. It shall not be possible to manually deactivate any other system at the same time as the MOIS or through the same sequence of actions.
5.4.4. When manually deactivated, it shall be possible for the driver to easily manually reactivate the MOIS.
5.4.5. When manually deactivated, the MOIS shall automatically reactivate when the vehicle master control switch is activated.
5.5. System initialisation
5.5.1. If the MOIS has not been calibrated after a cumulative driving time of 15 seconds above a speed of 0 km/h (including stationary phases), information of this status shall be indicated to the driver. This information shall exist until the system has been successfully calibrated.
5.6. Information signal
5.6.1. The MOIS information signal referred to in paragraph 5.2.2. above shall be an optical information signal that is noticeable and easily verifiable by the driver from the driver's seat.
5.6.2. This information signal shall be visible by daylight and at night.
5.7. Collision warning signal
5.7.1. The MOIS shall warn the driver when the risk of a collision is imminent by providing the collision warning signal.
5.7.2. The collision warning signal shall be provided by the means of a combination of at least two modes selected from an optical signal, acoustic signal or haptic signal.
Where the collision warning signal is provided by using an optical mode, this shall be a signal differing in activation strategy from the information signal specified in paragraphs 5.2.2. and 5.6.
5.7.3. The collision warning signal shall be easily understandable for the driver to relate the warning signal to the potential collision. In case the warning signal is an optical signal this signal shall also be visible by daylight and at night.
5.7.4. The collision warning signal shall be activated according to the manufacturer strategy. The warning strategy shall be explained in the information referred to in paragraph 6.1.
The Technical Service shall verify the operation of the system according to the strategy.
5.7.5. The collision warning signal may be deactivated manually. In the case of a manual deactivation, it shall be reactivated on each activation of the vehicle master control switch.
5.8. Failure warning signals
5.8.1. The failure warning signal referred to in paragraph 5.3.2. above shall be a optical signal and shall be other than or clearly distinguishable from the information signal. The failure warning signal shall be visible by daylight and night and shall be easily verifiable by the driver from the driver's seat.
5.8.2. The failure warning signal shall remain active as long as the MOIS is unavailable.
5.8.3. The MOIS failure warning signal shall be activated with the activation of the vehicle master control switch. This requirement does not apply to collision warning signals shown in a common space to the failure warning signal.
5.9. Provisions for Periodic Technical Inspection
5.9.1. At a Periodic Technical Inspection, it shall be possible to confirm the correct operational status of the MOIS by a visible observation of the failure warning signal status.
In case of the failure warning signal being in a common space, the common space must be observed to be functional prior to the failure warning signal status check.

**6. Test procedure**
6.1. The manufacturer shall provide a documentation package which gives access to the basic design of the system and, if applicable, the means by which it is linked to other vehicle systems. The function of the system including its sensing and warning strategy shall be explained and the documentation shall describe how the operational status of the system is checked, whether there is an influence on other vehicle systems, and the method(s) used in establishing the situations which will result in a failure warning signal being displayed. The documentation package shall give sufficient information for the Type Approval Authority to identify the vehicle type and to aid decision-making on the selection of worst-case conditions.
6.2. Test conditions
6.2.1. The test shall be performed on a flat, dry asphalt or a concrete surface.
6.2.2. The ambient temperature shall be between 0° C and 45° C.
6.2.3. The test shall be performed under visibility conditions that allow the target to be observed throughout the test and that allows safe driving at the required test speeds.
6.2.4. Natural ambient illumination shall be homogeneous in the test area and in excess of 1000 lux. It should be ensured that testing is not performed whilst driving towards, or away from, the sun at a low angle.
6.3. Vehicle conditions
6.3.1. Test weight
The vehicle shall be tested in a condition of load to be agreed between the manufacturer and the Technical Service, with the distribution of mass among the axles stated by the manufacturer. No alteration shall be made once the test procedure has begun. The manufacturer shall demonstrate through the use of documentation that the system works at all conditions of load.
6.3.2. In the case where the MOIS is equipped with a user-adjustable information timing, the tests as specified in paragraphs 6.5., 6.6. and 6.7. below shall be performed for each test case with the information threshold set at the settings that generate the information signal closest to the collision point, i.e. worst-case setting. No alteration shall be made once the test procedure has begun.
6.3.3. Pre-Test Conditioning
6.3.3.1 If requested by the vehicle manufacturer, the subject vehicle may be driven a maximum of 100 km on a mixture of urban and rural roads with other traffic and roadside furniture to initialise the sensor system.
6.4. Verification of signals test
6.4.1. With the vehicle stationary check that the optical failure warning signals comply with the requirements of paragraph 5.6. above.
6.5. Static Crossing Tests
6.5.1. The subject vehicle shall remain in a potential moving off manoeuvre with the MOIS active and the test area marked out as shown in Figure 1 of Appendix 1.
The relevant test target (T) shall be manoeuvred such that it moves on a trajectory perpendicular to the longitudinal median plane of the subject vehicle at the test case distance (dTC) away from the vehicle front and from the relevant crossing direction (c) (Table 1 of Appendix 1). The pedestrian test target reference point shall be the H-point (as defined by ISO 19206-2:2018) nearest the subject vehicle. The cyclist test target reference point shall be at the intersection of a plane perpendicular to the test target centreline located at the most forward point of the bicycle and a plane parallel to the test target centreline located at the test target H-point nearest the subject vehicle (as defined by ISO (CD) 19206-4).
6.5.2. The test target shall be accelerated such that it reaches the test target speed (v) at a distance of no closer than 15 m from the plane relating to the subject vehicle side nearest the crossing direction. The test case speed shall be maintained until the plane relating to the opposite vehicle side is cleared by a distance of no less than 5 m.
6.5.3. In accordance with paragraph 5.2.2.2., the Technical Service shall verify the activation of the MOIS information signal before the test target (T) reaches a distance corresponding to the last point of information (dLPI) in Table 1 of Appendix 1, and that the MOIS information signal remains on until the test target has at least crossed the separation plane relating to the vehicle side opposite to the crossing direction. The collision warning signal shall not be activated.
6.5.4. The Technical Service shall repeat paragraphs 6.5.1. to 6.5.3. for two test cases from Table 1 of Appendix 1 to this Regulation and for one additional test case selected from the combination of a soft target and the range of VRU speeds, VRU travel directions and detection boundaries defined in paragraph 5.2.2.2.
Where deemed justified, the Technical Service may also select additional test cases within the range of the soft targets, VRU speeds, travel directions and detection boundaries defined in paragraph 5.2.2.2.
6.6. Longitudinal Stopping for Moving Off Cyclist Tests
6.6.1. The cyclist test target (T) shall be located within the test area marked out as shown in Figure 2 in Appendix 1. The cyclist test target shall be positioned at the relevant test target starting point (pcyc) in Table 2 of Appendix 1 and face in the direction of travel and parallel to the longitudinal median plane of the subject vehicle. The cyclist test target reference point shall be at the centre of the bottom bracket of the bicycle and on the centreline of the bicycle. Should there be less than 100 mm clearance between the vehicle front and the rear most point of the cyclist test target, then pcyc may be moved an additional clearance distance (dclear) away from the vehicle front, in a direction parallel to the longitudinal plane, such that there is 100 +10/-0 mm clearance between the vehicle front and the rear most point of the cyclist test target.
6.6.2. The subject vehicle shall be accelerated in a straight line to a constant speed of 10 +0/-0.5 km/h, before entering the stopping corridor. The subject vehicle shall maintain this constant speed until the vehicle front passes the braking plane (pbrake) shown in Figure 2 of Appendix 1, before braking to a stop such that the vehicle front is positioned at the stopping plane (pstop). The subject vehicle shall be considered to have stopped when it has come to a rest and the vehicle is either no longer in a forward vehicle mode or forward gear.
6.6.3. After a delay of no less than 10 seconds from the point at which the subject vehicle is considered to have stopped, the test target shall then be accelerated in a straight line on a trajectory parallel to the longitudinal median plane of the vehicle to a speed of 10 +0/-0.5 km/h within a distance of 5 m, before being brought to a stop. While accelerating, the lateral tolerance of the test target motion shall not exceed ± 0.05 m.
6.6.4. In accordance with paragraph 5.2.2.3., the Technical Service shall verify the activation of the MOIS information signal before the subject vehicle reaches a distance from the stopping plane (pstop) corresponding to the last point of information (dLPI) in Table 2 of Appendix 1, and the MOIS information signal remains on until the test target at least crosses a distance from the vehicle front relating to the maximum forward separation distance (dFSP) in Figure 2 of Appendix 1. The collision warning signal may be activated, as appropriate.
6.6.5. The Technical Service shall repeat paragraphs 6.6.1. to 6.6.4. for two test cases shown in Table 2 of Appendix 1 to this Regulation and for one additional test case by selecting a cyclist test target and cyclist starting point from within the detection boundaries defined in paragraph 5.2.2.3.
Where deemed justified, the Technical Service may also select additional test cases within the range of the cyclist test targets and the detection boundaries defined in paragraph 5.2.2.3.
6.7 Longitudinal Moving Off with Cyclist Tests
6.7.1. The cyclist test target (T) shall be located within the test area marked out as shown in Figure 2 of Appendix 1. The cyclist test target shall be positioned at the relevant test target starting point (pcyc) in Table 2 of Appendix 1 and face in the direction of travel and parallel to the longitudinal median plane of the subject vehicle. The cyclist test target reference point shall be at the centre of the bottom bracket of the bicycle and on the centreline of the bicycle. Should there be less than 100 mm clearance between the vehicle front and the rear most point of the cyclist test target, then pcyc may be moved an additional clearance distance (dclear) away from the vehicle front, in a direction parallel to the longitudinal plane, such that there is 100 +10/-0 mm clearance between the vehicle front and the rear most point of the cyclist test target.
6.7.2. The subject vehicle shall be accelerated in a straight line to a constant speed of 10 +0/-0.5 km/h, before entering the stopping corridor. The subject vehicle shall maintain a constant speed until the vehicle front passes the braking plane (pbrake) shown in Figure 2 of Appendix 1, before braking to a stop such that the vehicle front is positioned at the stopping plane (pstop). The subject vehicle shall be considered to have stopped when it has come to a rest and the vehicle is either no longer in a forward vehicle mode or forward gear.
6.7.3. After a delay of no less than 10 seconds from the point at which the subject vehicle is considered to have stopped, the test target and subject vehicle shall be accelerated at the same time and in a straight line, on a trajectory parallel to the longitudinal median plane of the subject vehicle, to a constant speed of 10 +0/-0.5 km/h in a distance of no greater than 5 m. The subject vehicle and test target shall maintain this constant speed until a total travel distance of no less than 15 m from the stopping point is traversed by the subject vehicle. The lateral tolerance of the subject vehicle shall not exceed ± 0.05 m, whilst the lateral tolerance of the test target motion shall not exceed ± 0.05 m. The forward separation distance between the vehicle front and test target while moving shall be maintained to be within the boundaries of the maximum and minimum forward separation planes.
6.7.4. In accordance with paragraph 5.2.2.3., the Technical Service shall verify the activation of the MOIS information signal before the subject vehicle reaches a distance from the stopping plane (pstop) corresponding to the last point of information (dLPI) in Table 2 of Appendix 1, and that the MOIS information signal remains on until the subject vehicle passes a distance of 15 m from the stopping point. The collision warning signal may be activated, as appropriate.
6.7.5. The Technical Service shall repeat paragraphs 6.7.1. to 6.7.4. for two test cases shown in Table 2 of Appendix 1 to this Regulation and for one additional test case by selecting a cyclist test target and cyclist starting point from within the detection boundaries defined in paragraph 5.2.2.3.
Where deemed justified, the Technical Service may also select additional test cases within the range of the cyclist test targets and the detection boundaries defined in paragraph 5.2.2.3.
6.8. Failure detection test
6.8.1. Simulate a MOIS failure, for example by disconnecting the power source to any MOIS component or disconnecting any electrical connection between the MOIS components. The electrical connections for the failure warning signal of paragraph 5.8. above shall not be disconnected when simulating a MOIS failure.
6.8.2. The failure warning signal specified in paragraph 5.8. shall be activated and remain activated while the vehicle is being driven and shall be reactivated upon each activation of the vehicle master control switch, as long as the simulated failure exists.
6.9. Automatic deactivation test
6.9.1. With the MOIS system active, contaminate any of the MOIS sensing devices completely with a substance comparable to snow, ice or mud (e.g. based on water). The MOIS shall automatically deactivate, indicating this condition as specified in paragraph 5.8.
6.9.2. Remove any contamination from the MOIS sensing devices completely and perform a reactivation of the vehicle master control switch. The MOIS shall automatically reactivate after a driving time not exceeding 60 seconds.

**7. Modification of vehicle type and extension of approval**
7.1. Every modification of the vehicle type as defined in paragraph 2.3. of this Regulation shall be notified to the Type Approval Authority which approved the vehicle type. The Type Approval Authority may then either:
7.1.1. Consider that the modifications made do not have an adverse effect on the conditions of the granting of the approval and grant an extension of approval;
7.1.2. Consider that the modifications made affect the conditions of the granting of the approval and require further tests or additional checks before granting an extension of approval.
7.2. Confirmation or refusal of approval, specifying the alterations, shall be communicated by the procedure specified in paragraph 4.4. above to the Contracting Parties to the Agreement applying this Regulation.
7.3. The Type Approval Authority shall inform the other Contracting Parties of the extension by means of the communication form which appears in Annex 1 to this Regulation. It shall assign a serial number to each extension, to be known as the extension number.

**8. Conformity of production**
8.1. Procedures for the conformity of production shall conform to the general provisions defined in Article 2 and Schedule 1 to the 1958 Agreement (E/ECE/TRANS/505/Rev.3) and meet the following requirements:
8.2. A vehicle approved pursuant to this Regulation shall be so manufactured as to conform to the type approved by meeting the requirements of paragraph 5. above;
8.3. The Type Approval Authority which has granted the approval may at any time verify the conformity of control methods applicable to each production unit. The normal frequency of such inspections shall be once every two years.

**9. Penalties for non-conformity of production**
9.1. The approval granted in respect of a vehicle type pursuant to this Regulation may be withdrawn if the requirements laid down in paragraph 8. above are not complied with.
9.2. If a Contracting Party withdraws an approval it had previously granted, it shall forthwith so notify the other Contracting Parties applying this Regulation by sending them a communication form conforming to the model in Annex 1 to this Regulation.

**10. Production definitively discontinued**
If

the holder of the approval completely ceases to manufacture a type of vehicle approved in accordance with this Regulation, they shall so inform the Type Approval Authority which granted the approval, which in turn shall forthwith inform the other Contracting Parties to the Agreement applying this Regulation by means of a communication form conforming to the model in Annex 1 to this Regulation.

**11. Names and addresses of the Technical Services responsible for conducting approval tests and of Type Approval Authorities**
The Contracting Parties to the Agreement applying this Regulation shall communicate to the United Nations Secretariat the names and addresses of the Technical Services responsible for conducting approval tests and of the Type Approval Authorities which grant approval and to which forms certifying approval or extension or refusal or withdrawal of approval are to be sent.

## Appendix 1

### Figure 1: Set Up for Static Crossing Tests
(图示描述：测试区域布置图，包含车辆、车辆前部、近侧/远侧车辆平面、近侧/远侧分离平面、最小/最大前向分离平面等要素及尺寸标注。)

**定义：**
*   **d_w:** 车辆宽度。
*   **d_25%:** 与车辆宽度25%相关的距离。
*   **d_NSP:** 从近侧车辆平面到近侧分离平面的距离，定义为0.5米。
*   **d_OSP:** 从远侧车辆平面到远侧分离平面的距离，定义为0.5米。
*   **d_TC:** 每个测试用例的前向分离距离。
*   **d_FSP:** 从车辆前部到最大前向分离平面的距离。
*   **d_LPI:** 与最后信息点(LPI)相关的距离。

### Table 1: Test Cases for Static Crossing Tests
| 测试用例 | 软目标 (T) | 测试用例距离 (d_TC) /m | 穿越方向 (c) | 速度 (v) /km/h | 到最后信息点的距离 (d_LPI) /m |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 儿童行人 | 0.8 | 近侧 | 3 | d_NSP |
| 2 | 成人行人 | d_FSP | 近侧 | 3 | d_NSP |
| 3 | 成人骑行者 | 0.8 | 远侧 | 3 | d_OSP |
| 4 | 成人骑行者 | d_FSP | 近侧 | 5 | d_NSP |
| 5 | 成人行人 | 0.8 | 远侧 | 5 | d_OSP |
| 6 | 儿童行人 | d_FSP | 远侧 | 5 | d_OSP |

### Figure 2: Set Up for Longitudinal Cyclist Tests
(图示描述：纵向骑行者测试布置图，包含停止走廊、车辆制动平面(p_brake)、车辆停止平面(p_stop)、骑行者测试目标起点(p_cyc)等要素及尺寸标注。)

**定义：**
*   **d_50%:** 与车辆宽度50%相关的距离。
*   **p_brake:** 车辆制动平面。
*   **p_stop:** 车辆停止平面。
*   **d_FSP:** 从车辆停止平面到最大前向分离平面的距离。
*   **d_clear:** 为确保车辆前部与骑行者测试目标最后点之间至少有100毫米间隙，骑行者测试目标额外移动的距离。
*   **p_cyc:** 骑行者测试目标起点，取自骑行者测试目标参考点。
*   **p_x:** 停止平面与骑行者测试目标起点之间的距离。
*   **p_y:** 车辆纵向中间平面与骑行者测试目标起点之间的距离，车辆近侧为正方向。
*   **d_LPI:** 最后信息点(LPI)线与车辆停止平面之间的距离。

### Table 2: Test Cases for Longitudinal Cyclist Tests
| 测试用例 | 测试目标 (T) | 到骑行者起点的距离 (p_x) /m | 到骑行者起点的横向距离 (p_y) /m | 到最后信息点的距离 (d_LPI) /m |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 成人骑行者 | 0.8 + d_clear | +d_50% | d_FSP – 0.8 – d_clear |
| 2 | 成人骑行者 | 0.8 + d_clear | 0.0 | d_FSP – 0.8 – d_clear |
| 3 | 成人骑行者 | 0.8 + d_clear | -d_50% | d_FSP – 0.8 – d_clear |
| 4 | 成人骑行者 | d_FSP – 0.1 | +d_50% | 0.1 |
| 5 | 成人骑行者 | d_FSP – 0.1 | 0.0 | 0.1 |
| 6 | 成人骑行者 | d_FSP – 0.1 | -d_50% | 0.1 |

## Annexes

### Annex 1: Communication
(最大格式：A4 (210 x 297 mm))

签发机构： (行政机构名称)
...
...
...

**关于：** 2 批准授予
批准延期
批准拒绝
批准撤销
生产确定已终止

关于根据UN法规第159号，车辆类型在起步信息系统(MOIS)方面的批准。

批准号： ...
1.  商标： ...
2.  类型和商品名： ...
3.  制造商名称和地址： ...
4.  如适用，制造商代表的名称和地址： ...
5.  车辆简要描述： ...
6.  提交车辆供批准的日期： ...
7.  执行批准测试的技术服务机构： ...
8.  该机构签发报告的日期： ...
9.  该机构签发报告的编号： ...
10. 延期原因（如适用）： ...
11. 关于MOIS的批准被授予/拒绝：2
12. 地点： ...
13. 日期： ...
14. 签名： ...
15. 附于本通讯的是以下文件，带有上述批准号： ...
16. 任何备注： ...

1 授予/延期/拒绝/撤销批准的国家的识别号（见本法规中的批准规定）。
2 划掉不适用项。

### Annex 2: Arrangements of approval marks
(见本法规第4.5.至4.5.2段)

```
6 X1X5X9RR -– 0 00108158 5
a = 8 mm min
```

上述贴在车辆上的批准标志表明，相关车辆类型已在比利时(E 6)根据UN法规第159号关于起步信息系统(MOIS)获得批准。批准号的前两位数字表示该批准是根据UN法规第159号原始版本的要求授予的。

```
UI
270650
2a/3 a/2 a/3
a ≥ 8 mm a
```

上述唯一标识符表明相关类型已获批准，并且可以通过使用270650作为唯一标识符在联合国安全互联网数据库上访问该型式批准的相关信息。唯一标识符中的任何前导零在批准标志中可以省略。

### Annex 3: Test method for determining blind spot boundary

#### 1. Blind spot boundary
本法规第2.22段定义的盲区边界可通过本附件所述方法确定。

#### 2. Test methods
2.1. 测试对象应为外径为50±2毫米的圆柱体，其上有一个颜色与测试对象其余部分形成对比的环，环高10±2毫米，其下边缘距测试对象底部900±2毫米。
2.2. 测试条件应符合本法规第6.2段的规定。
2.3. 车辆条件应符合本法规第6.3段的规定。
2.4. 测试区域应按本附件图1所示进行标记。

**Figure 1: Blind spot boundary test area**
(图示描述：盲区边界测试区域布置图，包含车辆、车辆前部、近侧/远侧车辆平面、近侧/远侧分离平面、最小/最大前向分离平面等要素及尺寸标注。)

**定义：**
*   **d_w:** 车辆宽度。
*   **d_NSP:** 从近侧车辆平面到近侧分离平面的距离，定义为0.5米。
*   **d_OSP:** 从远侧车辆平面到远侧分离平面的距离，定义为0.5米。
*   **d_FSP:** 从车辆前部到最大前向分离平面的距离。

2.5. 眼点应符合本法规第2.11段的规定。
2.6. 测试程序
    2.6.1. 将35毫米或更大画幅的静态相机、摄像机或数字等效设备定位，使相机成像平面的中心位于眼点。
 相机应能够查看所有潜在测试位置中的测试对象。如果相机需要重新定位以查看所有潜在测试位置，则应验证所有可能相机位置的相机成像平面中心均位于眼点。
    2.6.2. 应记录从眼点观察测试对象环的整个环的可见性，测试对象位置位于最小和最大前向分离平面以及近侧和远侧分离平面所限定的区域内。
    2.6.3. 从最小前向分离平面开始，将测试对象沿平行于车辆纵向中间平面的评估平面远离车辆前部移动，直至达到最大前向分离平面。
    2.6.4. 应沿评估平面以不大于150毫米的距离间隔记录测试对象环的可见性。
    2.6.5. 此过程应在近侧和远侧分离平面之间的评估平面上重复进行，每个评估平面之间的距离不大于150毫米。
    2.6.6. 其他方法，如基于CAD或基于激光的程序，如果提供文件证据证明已满足本附件所述测试程序的要求，技术服务机构可视为等效。

#### 3. Blind spot boundary definition
3.1. 盲区应由从眼点无法看到测试对象整个环的所有测试对象位置确定。
3.2. 盲区边界应在盲区外第一个从眼点可以看到测试对象整个环的位置确定。

<END>
---

## 原文参考（MinerU 云解析 · 2026-04-22）

> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：
> - 表格 2 个
> - 公式 0 个
> - 图像 5 个
> - 全文 Markdown 50,307 字符（见 `outputs/<hash>/full.md`）

### 表格（取前 2 个）

#### 表 1 (page 15)
**Table 1 Test Cases for Static Crossing Tests **

<table><tr><td>Test Case</td><td>Soft Target (T)</td><td>Test Case Distance (drc)/m</td><td>Crossing Direction (c)</td><td>Soft Target Speed (v) /km/h</td><td>Distance to Last Point of Information (dLPi) /m</td></tr><tr><td>1</td><td>Child Pedestrian</td><td>0.8</td><td>Nearside</td><td>3</td><td>dNsP</td></tr><tr><td>2</td><td>Adult Pedestrian</td><td>dFsP</td><td>Nearside</td><td>3</td><td>dNsP</td></tr><tr><td>3</td><td>Adult Cyclist</td><td>0.8</td><td>Offside</td><td>3</td><td>dosp</td></tr><tr><td>4</td><td>Adult Cyclist</td><td>dFsP</td><td>Nearside</td><td>5</td><td>dNsP</td></tr><tr><td>5</td><td>Adult Pedestrian</td><td>0.8</td><td>Offside</td><td>5</td><td>dosp</td></tr><tr><td>6</td><td>Child Pedestrian</td><td>dFsP</td><td>Offside</td><td>5</td><td>dosp</td></tr></table>

#### 表 2 (page 16)
**Table 2 Test Cases for Longitudinal Cyclist Tests **

<table><tr><td></td><td>Test Case Test Target (T)</td><td>Distance to Forward Cyclist Start Point (px) /m</td><td>Distance to Lateral Cyclist Start Point (py)/m Information (dLp1) /m</td><td>Distance to Last Point of</td></tr><tr><td>1</td><td>Adult Cyclist</td><td>0.8 + dclear</td><td>+d50%</td><td>dFsp - 0.8-dclear</td></tr><tr><td>2</td><td>Adult Cyclist</td><td>0.8 + dclear</td><td>0.0</td><td>dFsP - 0.8 - dclear</td></tr><tr><td>3</td><td>Adult Cyclist</td><td>0.8 + dclear</td><td>-d50%</td><td>dFsp - 0.8-dclear</td></tr><tr><td>4</td><td>Adult Cyclist</td><td>dFsp-0.1</td><td>+d50%</td><td>0.1</td></tr><tr><td>5</td><td>Adult Cyclist</td><td>dFsP-0.1</td><td>0.0</td><td>0.1</td></tr><tr><td>6</td><td>Adult Cyclist</td><td>dFsp-0.1</td><td>-d50%</td><td>0.1</td></tr></table>

### 图像（取前 5 张）

![Figure 1 Set Up for Static Crossing Tests ](../_mineru_assets/ECE R159/027b581d99c39ef8c61a5a5e11d65ad7b203123a17b38281382bd885d41a44c5.jpg)  
*Figure 1 Set Up for Static Crossing Tests * (page 15)

![Figure 2 Set Up for Longitudinal Cyclist Tests ](../_mineru_assets/ECE R159/aeb3a927231166d02cc4af903d318930c1ff6ed3ac5e2d4137ef3cd1e5907d1c.jpg)  
*Figure 2 Set Up for Longitudinal Cyclist Tests * (page 16)

![图 page 17](../_mineru_assets/ECE R159/dcd51fcb4d98690386a6693c7f66dc3b777962d52db1095c32324c162197577c.jpg)  

![图 page 17](../_mineru_assets/ECE R159/dc2e8c43cfd527389d9d4d350770bd5f9724ca0904ca69d226a402404f8a120f.jpg)  

![Figure 1 Blind spot boundary test area ](../_mineru_assets/ECE R159/68cdbd1e6777a4cad9348efcc9e64a0cae73203824e7e3eb68cde6f588454013.jpg)  
*Figure 1 Blind spot boundary test area * (page 19)

