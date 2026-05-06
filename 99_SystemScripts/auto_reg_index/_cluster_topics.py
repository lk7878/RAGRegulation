"""
Stage 4 准备：机械聚类分析。

- 扫描所有 note 的 FM（reg_id/title/keywords/scope）
- 根据关键词词典把 notes 映射到汽车安全/排放主题
- 输出 cluster_assignment.json：topic → [note_path...]
- 输出 unmatched_notes.txt 用于兜底检查

主题词典覆盖 ECE/GB 常见技术域；多标签时取匹配分最高者。
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
OUT_DIR = Path(__file__).parent / ".stage4"
OUT_DIR.mkdir(exist_ok=True)

# 主题词典：{topic_key: {label, keywords (regex), reg_prefixes}}
# keywords: 在 title/keywords/scope 中正则匹配
# reg_prefixes: 直接根据 reg_id 前缀/编号区间归类（零成本）
TOPICS = {
    "lighting_signaling": {
        "label": "照明与信号装置",
        "keywords": [r"照明", r"信号装置", r"前照灯", r"位置灯", r"转向灯", r"制动灯",
                     r"雾灯", r"倒车灯", r"牌照灯", r"反射器",
                     r"\blighting\b", r"\bsignal(ling|ing|s)?\b", r"\bheadlamp\b",
                     r"\b(pass|dipped|driving) beam\b", r"\bdirection indicator\b",
                     r"\bstop lamp\b", r"\bretro[- ]?reflector\b"],
        "reg_prefixes": [
            # 仅枚举确实是灯具/反射/信号的 ECE 号，避免误捕 R30/34/43/46/58/94/95 等
            ("ece_R", r"^R0?(1|2|3|4|5|6|7|8|18|19|20|23|27|28|37|38|45|48|50|53|56|57|65|69|70|74|76|77|82|86|87|91|98|99|112|113|119|123|128|148|149)\b"),
        ],
        "gb_prefixes": [r"^GB(?:/T)?\s+4599", r"^GB(?:/T)?\s+4785", r"^GB(?:/T)?\s+4660",
                        r"^GB(?:/T)?\s+5920", r"^GB(?:/T)?\s+11554",
                        r"^GB(?:/T)?\s+15235", r"^GB(?:/T)?\s+15741", r"^GB(?:/T)?\s+15766",
                        r"^GB(?:/T)?\s+17509",
                        r"^GB(?:/T)?\s+18099", r"^GB(?:/T)?\s+18408", r"^GB(?:/T)?\s+18409",
                        r"^GB(?:/T)?\s+19151", r"^GB(?:/T)?\s+21259",
                        r"^GB(?:/T)?\s+23255", r"^GB(?:/T)?\s+25991", r"^GB(?:/T)?\s+30036"],
    },
    "brakes": {
        "label": "制动系统",
        "keywords": [r"制动", r"刹车", r"ABS", r"EBS", r"\bbrak(e|ing)\b",
                     r"\bABS\b", r"\bdeceler"],
        "reg_prefixes": [("ece_R", r"^R0?(13|13H|78|90|131|139|140|152)\b")],
        "gb_prefixes": [r"^GB 12676", r"^GB 12981", r"^GB 13594", r"^GB 15763", r"^GB 17352",
                        r"^GB 20073", r"^GB 21670", r"^GB 22749", r"^GB 24407",
                        r"^GB 36590", r"^GB 38892", r"^GB 38900"],
    },
    "emissions_exhaust": {
        "label": "排放与燃料",
        "keywords": [r"排放", r"尾气", r"污染物", r"油耗", r"燃料消耗", r"蒸发",
                     r"曲轴箱", r"OBD", r"\bemission", r"\bpollut", r"\bexhaust\b",
                     r"\bfuel consumption\b", r"\bevaporative\b", r"\bCO2\b"],
        "reg_prefixes": [("ece_R", r"^R0?(15|24|40|47|49|83|84|85|96|101|103|115|120|132|133|143|154)\b")],
        "gb_prefixes": [r"^GB 3847", r"^GB 11340", r"^GB 14762", r"^GB 17691",
                        r"^GB 17930", r"^GB 18285", r"^GB 18352", r"^GB 18297", r"^GB 18322",
                        r"^GB 19578", r"^GB 19755", r"^GB 20890", r"^GB 20997",
                        r"^GB 25981", r"^GB 27887", r"^GB 27999", r"^GB 37340"],
    },
    "restraints_airbags": {
        "label": "安全带与乘员约束",
        "keywords": [r"安全带", r"儿童约束", r"头枕", r"座椅", r"气囊",
                     r"\bseat belt\b", r"\bsafety belt\b", r"\brestraint\b",
                     r"\bchild (restraint|seat)\b", r"\bhead restraint\b",
                     r"\bairbag\b", r"\bISOFIX\b"],
        "reg_prefixes": [("ece_R", r"^R0?(14|16|17|21|25|44|80|107|129|135|137|144)\b")],
        "gb_prefixes": [r"^GB 11550", r"^GB 11551", r"^GB 14166", r"^GB 14167", r"^GB 15083",
                        r"^GB 15086", r"^GB 20071", r"^GB 20072", r"^GB 27887", r"^GB 34422"],
    },
    "crash_impact": {
        "label": "碰撞与被动安全",
        "keywords": [r"碰撞", r"撞击", r"翻车", r"侧面碰撞", r"正面碰撞", r"追尾",
                     r"\bcrash\b", r"\bcollision\b", r"\bimpact\b", r"\brollover\b",
                     r"\bfrontal\b", r"\blateral\b", r"\brear(?!view)"],
        "reg_prefixes": [("ece_R", r"^R0?(12|32|33|42|66|73|93|94|95|123|127|135|137|153|158)\b")],  # R147 移到 trailer_coupling（它是联结装置）
        "gb_prefixes": [r"^GB 11551", r"^GB 17354", r"^GB 20071", r"^GB 20072", r"^GB 24550",
                        r"^GB 26134", r"^GB 26512"],
    },
    "tires_wheels": {
        "label": "轮胎与车轮",
        "keywords": [r"轮胎", r"车轮", r"胎面", r"\btyre\b", r"\btire\b", r"\bwheel\b",
                     r"\btread\b", r"\bstudded tyre\b", r"retroreflective tyre"],
        "reg_prefixes": [("ece_R", r"^R0?(30|54|64|75|88|106|108|109|117|124|141|142|145|146|164)\b")],
        "gb_prefixes": [r"^GB 9743", r"^GB 9744", r"^GB 26149"],
    },
    "adas_driver_assist": {
        "label": "ADAS/驾驶员辅助系统",
        "keywords": [r"LDWS", r"BSIS", r"车道偏离", r"盲点信息", r"事件数据记录", r"EDR",
                     r"event data recorder", r"lane departure",
                     r"blind spot information", r"moving off information",
                     r"\bACSF\b", r"\bLKAS\b", r"\bAEB\b",
                     r"drowsiness", r"distraction"],
        "reg_prefixes": [("ece_R", r"^R0?(130|151|157|158|159|160)\b")],
        "gb_prefixes": [r"^GB/T 39263", r"^GB/T 39901"],
    },
    "steering_suspension": {
        "label": "转向与悬挂",
        "keywords": [r"转向装置", r"转向系", r"方向盘",
                     r"\bsteering (system|device|equipment|column|wheel)\b",
                     r"\bsuspension\b"],
        "reg_prefixes": [("ece_R", r"^R0?79\b")],
        "gb_prefixes": [r"^GB 17675"],
    },
    "visibility_glazing": {
        "label": "视野/玻璃/雨刮",
        "keywords": [r"视野", r"玻璃", r"雨刮", r"除霜", r"除雾", r"后视镜",
                     r"\bglazing\b", r"\bmirror\b", r"\bwiper\b", r"\bdefrost\b",
                     r"\bfield of vision\b", r"\bvisibility\b"],
        "reg_prefixes": [("ece_R", r"^R0?(43|46|81|125)\b")],
        "gb_prefixes": [r"^GB 9656", r"^GB 11555", r"^GB 11562", r"^GB 15084",
                        r"^GB 20362"],
    },
    "electronics_emc": {
        "label": "电气电子与 EMC",
        "keywords": [r"电磁兼容", r"电磁辐射", r"EMC", r"无线电骨扰", r"电子路用状况", r"网安全",
                     r"\belectromagnetic\b", r"\bradio frequency\b",
                     r"\bcybersecurity\b", r"\bOTA\b", r"\bsoftware update\b", r"\bhigh[- ]voltage\b", r"\bREESS\b"],
        "reg_prefixes": [("ece_R", r"^R0?(10|100|134|136|155|156)\b")],
        "gb_prefixes": [r"^GB(?:/T)?\s+8410", r"^GB(?:/T)?\s+18384", r"^GB(?:/T)?\s+18655",
                        r"^GB(?:/T)?\s+24552", r"^GB(?:/T)?\s+28382", r"^GB(?:/T)?\s+30381",
                        r"^GB(?:/T)?\s+34660", r"^GB(?:/T)?\s+38031"],
    },
    "fuel_lpg_cng": {
        "label": "燃料装置（液体/气体）",
        "keywords": [r"燃料箱", r"LPG", r"CNG", r"天然气", r"液化气", r"氢燃料", r"加氢",
                     r"\bfuel tank\b", r"\bLPG\b", r"\bCNG\b", r"\bhydrogen\b",
                     r"\bLNG\b"],
        "reg_prefixes": [("ece_R", r"^R0?(34|67|110|115|134)\b")],
        "gb_prefixes": [r"^GB 17258", r"^GB 17259", r"^GB 17674", r"^GB 18296"],
    },
    "noise": {
        "label": "噪声",
        "keywords": [r"噪声", r"噪音", r"\bnoise\b", r"\bsound\b", r"\bacoustic\b"],
        "reg_prefixes": [("ece_R", r"^R0?(41|51|59|63|92|117|138)\b")],
        "gb_prefixes": [r"^GB 1495", r"^GB 3096"],
    },
    "dimensions_weights": {
        "label": "尺寸/质量/类别",
        "keywords": [r"车辆外廓", r"轴荷", r"车辆分类", r"硬点", r"前结构", r"后结构", r"载量",
                     r"术语和定义", r"准则", r"尺寸代码", r"质量分布",
                     r"\bdimensions?\b", r"\bmass\b", r"\bweight\b", r"\baxle load\b",
                     r"\bvehicle classification\b", r"\bterms and definitions\b"],
        "reg_prefixes": [("ece_R", r"^R0?(128|139|140)\b")],
        "gb_prefixes": [r"^GB(?:/T)?\s+1589", r"^GB(?:/T)?\s+7258",
                        r"^GB/T\s+3730(?:\.\d+)?", r"^GB/T\s+15089",
                        r"^GB/T\s+17347", r"^GB/T\s+5910",
                        r"^GB/T\s+22550", r"^GB/T\s+22552",
                        r"^GB/T\s+39896"],
    },
    "doors_mechanisms": {
        "label": "门锁/铰链/座椅机构",
        "keywords": [r"车门", r"门锁", r"铰链", r"罩盖锁", r"\bdoor\b", r"\block\b", r"\bhinge\b",
                     r"\bhood lock\b"],
        "reg_prefixes": [("ece_R", r"^R0?(11|21|95)\b")],
        "gb_prefixes": [r"^GB 15086", r"^GB 11568"],
    },
    "type_approval_general": {
        "label": "总体型式认证/通用要求",
        "keywords": [r"型式批准", r"型式认证", r"市场监督",
                     r"framework regulation", r"retained.*regulation",
                     r"\btype[- ]approval\b", r"\bwhole vehicle\b", r"\bmarket surveillance\b"],
        "reg_prefixes": [("ece_R", r"^R0?(0|122)\b")],
        "gb_prefixes": [],
        "special": ["EU 2018/858", "2007/46", "Regulation (EU) 2018/858"],
    },
    "identification": {
        "label": "车辆识别/标记",
        "keywords": [r"识别代号", r"VIN", r"制造厂代号", r"销售黑名单",
                     r"车辆标志", r"车辆标识",
                     r"\bvehicle identification\b", r"\bVIN\b", r"\bmanufacturer identifier\b"],
        "reg_prefixes": [],
        "gb_prefixes": [r"^GB 16735", r"^GB 16737", r"^GB 18410", r"^GB 20838",
                        r"^GB 25990", r"^GB 38262", r"^GB 7258"],
    },
    "anti_theft_security": {
        "label": "防盗与安全防护",
        "keywords": [r"防盗", r"身份认证", r"车辆安全", r"immobili[sz]er", r"retrieval",
                     r"\banti[- ]theft\b", r"\balarm system\b", r"\bimmobiliser\b",
                     r"protection.*against.*(cyber|unauthorized|manipulation)"],
        "reg_prefixes": [("ece_R", r"^R0?(18|62|97|116|161|162)\b")],
        "gb_prefixes": [r"^GB 15740", r"^GB 17676"],
    },
    "engine_power_performance": {
        "label": "发动机功率/性能测试",
        "keywords": [r"发动机净功率", r"功率测试", r"最大功率",
                     r"\bengine power\b", r"\bnet power\b", r"\brated power\b"],
        "reg_prefixes": [("ece_R", r"^R0?(85|68|84)\b")],
        "gb_prefixes": [r"^GB 17692", r"^GB 18297"],
    },
    "hv_battery_ev": {
        "label": "电动车/动力电池/充电保护",
        "keywords": [r"电动汽车", r"纯电动", r"动力电池", r"充电", r"动力锻造性能",
                     r"电驱动", r"REESS",
                     r"\belectric vehicle\b", r"\bBEV\b", r"\btraction battery\b",
                     r"\bREESS\b", r"\bcharging\b"],
        "reg_prefixes": [("ece_R", r"^R0?(100|136|148|156)\b")],
        "gb_prefixes": [r"^GB 18384", r"^GB 19751", r"^GB 19752", r"^GB 24552", r"^GB 27840",
                        r"^GB 28382", r"^GB 30381", r"^GB 30721", r"^GB 31467", r"^GB 31484",
                        r"^GB 31485", r"^GB 31486", r"^GB 38031", r"^GB 38032"],
    },
    "interior_protrusions": {
        "label": "内部凸出物/内饰",
        "keywords": [r"内部凸出物", r"仪表板", r"内饰",
                     r"隔断系统", r"partitioning system",
                     r"\binterior fittings\b", r"\binternal projections\b",
                     r"\bdashboard\b"],
        "reg_prefixes": [("ece_R", r"^R0?(21|26|61|126)\b")],
        "gb_prefixes": [r"^GB 11552", r"^GB 11569", r"^GB 8410", r"^GB 11566"],
    },
    "special_vehicles": {
        "label": "特种/危险车辆",
        "keywords": [r"危险货物", r"危险品", r"消防车", r"工业车辆", r"拖拉机",
                     r"农用", r"特种车辆", r"拶重车",
                     r"旅居车辆", r"旅居挂车", r"散装水泥车", r"冷藏车",
                     r"\bdangerous goods\b", r"\bADR\b", r"\btanker\b",
                     r"\bagricultural\b", r"\btractor\b", r"\bcaravan\b", r"\bmotorhome\b"],
        "reg_prefixes": [("ece_R", r"^R0?(73|105|111|142|144)\b")],  # R55 移到 trailer_coupling（它是机械联结装置）
        "gb_prefixes": [r"^GB 13392", r"^GB 13954", r"^GB 15369", r"^GB 1593",
                        r"^GB 10827", r"^GB 17761", r"^GB 17284", r"^GB 18428",
                        r"^GB 12514", r"^GB 12553", r"^GB 13495", r"^GB 17427", r"^GB 17835",
                        r"^GB 22127", r"^GB 29753", r"^GB/T 22550", r"^GB/T 22552"],
    },
    "bus_coach": {
        "label": "客车/公交车",
        "keywords": [r"客车结构", r"载客汽车", r"床位客车",
                     r"\bbus\b", r"\bcoach\b", r"\bM2\b", r"\bM3\b"],
        "reg_prefixes": [("ece_R", r"^R0?(36|52|66|107|118)\b")],
        "gb_prefixes": [r"^GB 13094", r"^GB 24407", r"^GB 26134"],
    },
    "motorcycle": {
        "label": "摩托车/L 类",
        "keywords": [r"摩托车", r"轻便摩托车", r"电动自行车",
                     r"\bhelmet\b", r"头盔",
                     r"\bmotorcycle\b", r"\bmoped\b", r"\bL[1-7]\b"],
        "reg_prefixes": [("ece_R", r"^R0?(22|40|41|47|57|72|76|78|81|113|153)\b")],
        "gb_prefixes": [r"^GB 19344", r"^GB 19482", r"^GB 20075", r"^GB 20904",
                        r"^GB 19152"],
    },
    "overview_directory": {
        "label": "目录/体系概览",
        "keywords": [r"目录", r"体系", r"概览", r"指南", r"产品市场准入",
                     r"市场准入", r"汽车技术法规", r"研究分析",
                     r"产品准入管理", r"管理和技术法规", r"法规概览",
                     r"汽车法规", r"汽车标准法规",
                     r"\btechnical regulations\b", r"\boverview\b", r"\bdirectory\b",
                     r"\bsecurity elements\b", r"\bmarket access\b"],
        "reg_prefixes": [],
        "gb_prefixes": [],
    },
    "lubricants_fluids": {
        "label": "润滑油/工作液",
        "keywords": [r"润滑油", r"齿轮油", r"冷却液", r"汽轮机油", r"涡轮机油",
                     r"机油", r"润滑脂", r"制动液", r"防冻液",
                     r"\blubricant", r"\bgear oil\b", r"\bcoolant\b",
                     r"\btransmission fluid\b", r"\bbrake fluid\b"],
        "reg_prefixes": [],
        "gb_prefixes": [r"^GB 11120", r"^GB 11121", r"^GB 11122", r"^GB 11124",
                        r"^GB 13895", r"^GB 15179", r"^GB 16629", r"^GB 23971",
                        r"^GB 29743"],
    },
    "fire_fighting_equipment": {
        "label": "消防器材/灭火系统",
        "keywords": [r"灭火", r"消防", r"泡沫", r"干粉", r"七氟丙烷", r"六氟丙烷",
                     r"消防给水", r"呼救器", r"排烟",
                     r"\bfire extinguish\b", r"\bfire[- ]fighting\b"],
        "reg_prefixes": [],
        "gb_prefixes": [r"^GB 12514", r"^GB 12553", r"^GB 13495", r"^GB 15308",
                        r"^GB 16668", r"^GB 17427", r"^GB 17835", r"^GB 18614",
                        r"^GB 19572", r"^GB 21976", r"^GB 25200", r"^GB 25202",
                        r"^GB 25204", r"^GB 25971", r"^GB 25972", r"^GB 27897",
                        r"^GB 27898", r"^GB 27900", r"^GB 27901"],
    },
    "speed_control_speedometer": {
        "label": "车速/限速装置",
        "keywords": [r"车速表", r"限速", r"速度控制",
                     r"\bspeedometer\b", r"\bspeed limit\b"],
        "reg_prefixes": [("ece_R", r"^R0?(39|89)\b")],
        "gb_prefixes": [r"^GB(?:/T)?\s+15082", r"^GB(?:/T)?\s+24545"],
    },
    "body_markings": {
        "label": "车身标识/反光标志",
        "keywords": [r"反光标识", r"车身标识", r"警示灯", r"限速标志", r"专用车道",
                     r"校车标识", r"标线",
                     r"\bconspicuity marking\b", r"\bretroreflective marking\b"],
        "reg_prefixes": [("ece_R", r"^R0?(27|70|104|150)\b")],
        "gb_prefixes": [r"^GB 21253", r"^GB 23254", r"^GB 23826", r"^GB 24315",
                        r"^GB 24965"],
    },
    "energy_labeling": {
        "label": "能耗/油耗标识",
        "keywords": [r"能源消耗量标识", r"油耗标识", r"能效标识",
                     r"\bfuel consumption label\b", r"\benergy label\b"],
        "reg_prefixes": [],
        "gb_prefixes": [r"^GB 22757", r"^GB 27887"],
    },
    "commercial_operations": {
        "label": "营运/商用车管理",
        "keywords": [r"营运车辆", r"道路运输车辆", r"综合性能",
                     r"商用车", r"前下部防护", r"侧倾稳定", r"起重尾板",
                     r"\bcommercial vehicle\b", r"\boperational\b", r"\btail[- ]lift\b"],
        "reg_prefixes": [("ece_R", r"^R0?(58|73|93|111)\b")],
        "gb_prefixes": [r"^GB(?:/T)?\s+18565", r"^GB(?:/T)?\s+26511", r"^GB(?:/T)?\s+28373",
                        r"^GB(?:/T)?\s+17578", r"^GB/T\s+37706"],
    },
    "certification_admin": {
        "label": "强制认证/管理制度",
        "keywords": [r"强制性产品认证", r"实施规则", r"CCC\b", r"认证制度",
                     r"\bcompulsory certification\b", r"\bconformity assessment\b"],
        "reg_prefixes": [],
        "gb_prefixes": [],  # CNCA-C* 不是 GB 号
    },
    "operator_controls_indicators": {
        "label": "操纵件/指示器位置",
        "keywords": [r"操纵件", r"指示器", r"信号装置.*位置", r"手控位置",
                     r"加速器控制", r"肢体残疾人", r"操纵辅助装置",
                     r"手控制区域", r"驾驶员手控",
                     r"\bhand control", r"\btell[- ]tales?\b",
                     r"\blocation.*(hand control|indicator|tell)"],
        "reg_prefixes": [("ece_R", r"^R0?(35|60|121)\b")],
        "gb_prefixes": [r"^GB(?:/T)?\s+4094", r"^GB(?:/T)?\s+15365",
                        r"^GB(?:/T)?\s+11561", r"^GB/T\s+21055", r"^GB/T\s+17867",
                        r"^GB/T\s+43402"],
    },
    "test_methods": {
        "label": "试验方法/测量规程",
        "keywords": [r"试验方法", r"测量方法", r"测定方法", r"测试方法",
                     r"道路试验", r"滑行试验", r"起动性能", r"爬陡坡", r"地形通过性",
                     r"冷却能力", r"热平衡", r"加速性能", r"最高车速试验", r"最低稳定车速",
                     r"行驶检查方法", r"定型试验", r"横向稳定性", r"底盘测功机", r"道路负载",
                     r"\btest method", r"\bmeasurement method"],
        "reg_prefixes": [],
        "gb_prefixes": [r"^GB/T\s+1253[4-9]", r"^GB/T\s+1254[0-9]", r"^GB/T\s+12673",
                        r"^GB/T\s+12674", r"^GB/T\s+12676", r"^GB/T\s+12677",
                        r"^GB/T\s+1332\b", r"^GB/T\s+29121", r"^GB/T\s+43404"],
    },
    "trailer_coupling": {
        "label": "挂车/联结装置",
        "keywords": [r"联结装置", r"紧密连结", r"鞍座", r"牵引销",
                     r"机械联结", r"紧密联结装置",
                     r"\bcoupling device\b", r"\bclose[- ]coupling\b",
                     r"\bkingpin\b", r"\bfifth wheel\b",
                     r"\bmechanical coupling\b", r"\bcoupling component"],
        "reg_prefixes": [("ece_R", r"^R0?(55|102|147)\b")],
        "gb_prefixes": [r"^GB 4606", r"^GB 15083", r"^GB/T 22551"],
    },
    "recycling_reuse": {
        "label": "回收/再制造/禁用物质",
        "keywords": [r"再制造", r"再利用", r"可回收", r"可回收利用性", r"拆解", r"禁用物质",
                     r"\brecycl", r"\breuse\b", r"\bremanufactur",
                     r"\bhazardous substances\b", r"\bELV\b"],
        "reg_prefixes": [],
        "gb_prefixes": [r"^GB/T 19514", r"^GB/T 19515", r"^GB/T 26987", r"^GB/T 26988",
                        r"^GB/T 26989", r"^GB/T 2867[3-9]", r"^GB/T 30512",
                        r"^GB/T 39895"],
    },
    "out_of_scope": {
        "label": "非汽车法规/越界",
        "keywords": [r"^自行车", r"塔式起重机", r"土方机械", r"工业过程测量",
                     r"转轴用唇形密封", r"tower crane", r"earth[- ]moving"],
        "reg_prefixes": [],
        # 只列明确非汽车的 GB 号（避免误伤电动自行车 GB 17761/42295+ 系列）
        "gb_prefixes": [r"^GB\s+3565\b", r"^GB\s+3565\.", r"^GB\s+5144\b",
                        r"^GB\s+6246\b",  # 消防水带
                        r"^GB\s+12837\b", r"^GB\s+12838\b",
                        r"^GB\s+25684", r"^JIS\s+B240"],
    },
    "reference_material": {
        "label": "参考资料（非法规）",
        "keywords": [r"汽车专业英语", r"汽车构造", r"操作说明", r"操作流程",
                     r"数据提交要求", r"提案申请"],
        "reg_prefixes": [],
        "gb_prefixes": [],
    },
    "misc": {
        "label": "其他/未归类",
        "keywords": [],
        "reg_prefixes": [],
        "gb_prefixes": [],
    },
}


def load_all_notes() -> list[dict]:
    """扫描所有 note，提取 FM 字段供聚类。"""
    notes = []
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if not txt.startswith("---"):
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        try:
            fm = yaml.safe_load(txt[4:end]) or {}
        except yaml.YAMLError:
            continue
        notes.append({
            "path": str(p),
            "reg_id": fm.get("reg_id") or "",
            "region": fm.get("region") or "",
            "type": fm.get("type") or "",
            "title": fm.get("title") or "",
            "title_en": fm.get("title_en") or "",
            "keywords": fm.get("keywords") or [],
            "scope": fm.get("scope") or "",
            "status": fm.get("status") or "",
            "publication_date": fm.get("publication_date") or "",
        })
    return notes


def classify_note(note: dict) -> list[tuple[str, int]]:
    """返回 [(topic_key, score), ...] 按分数降序。"""
    reg_id = note["reg_id"]
    region = note["region"]
    scores: dict[str, int] = defaultdict(int)

    # 拼接全文文本用于关键词匹配（含 reg_id，覆盖 OCR 未提取到 title 的情形）
    blob = " ".join([
        reg_id, note["title"], note["title_en"], note["scope"],
        " ".join(note["keywords"]) if isinstance(note["keywords"], list) else str(note["keywords"]),
    ]).lower()

    for topic_key, cfg in TOPICS.items():
        # 前缀匹配（高权重）
        for prefix_type, pat in cfg.get("reg_prefixes", []):
            if prefix_type == "ece_R" and region == "ece":
                # reg_id 形如 "ECE R094"/"UN R094"/"R-057-r1a2e"，抽 R 号数字
                m = re.search(r"R[- ]?0?(\d+[a-zA-Z]?)", reg_id, re.IGNORECASE)
                if m:
                    normalized = f"R{m.group(1).upper()}"
                    if re.match(pat, normalized):
                        scores[topic_key] += 10
        for pat in cfg.get("gb_prefixes", []):
            if region == "cn" and re.match(pat, reg_id):
                scores[topic_key] += 10

        # 特殊精确匹配（如 Framework Regulation / EU 2018/858 等）
        for keyword in cfg.get("special", []):
            if keyword.lower() in blob:
                scores[topic_key] += 10

        # 关键词匹配（低权重）
        for kw in cfg["keywords"]:
            try:
                if re.search(kw, blob, re.IGNORECASE):
                    scores[topic_key] += 2
            except re.error:
                continue

    if not scores:
        return []
    return sorted(scores.items(), key=lambda x: -x[1])


def main() -> int:
    notes = load_all_notes()
    print(f"Loaded {len(notes)} notes.")

    # topic → list of notes
    cluster: dict[str, list[dict]] = defaultdict(list)
    unmatched: list[dict] = []

    for n in notes:
        matches = classify_note(n)
        if not matches:
            unmatched.append(n)
            n["topic_primary"] = "misc"
            n["topic_scores"] = {}
            cluster["misc"].append(n)
            continue
        # 取最高分作为主主题
        primary = matches[0][0]
        n["topic_primary"] = primary
        n["topic_scores"] = dict(matches[:3])
        cluster[primary].append(n)

    # 排序每簇按 reg_id, date
    for k in cluster:
        cluster[k].sort(key=lambda x: (x["reg_id"], str(x.get("publication_date") or "")))

    # 输出
    out_cluster = {
        k: [
            {
                "path": n["path"],
                "reg_id": n["reg_id"],
                "region": n["region"],
                "type": n["type"],
                "title": n["title"],
                "publication_date": str(n["publication_date"]) if n["publication_date"] else "",
                "status": n["status"],
                "scores": n.get("topic_scores", {}),
            }
            for n in v
        ]
        for k, v in cluster.items()
    }
    (OUT_DIR / "cluster_assignment.json").write_text(
        json.dumps(out_cluster, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT_DIR / "unmatched_notes.txt").write_text(
        "\n".join(f"{n['reg_id']}\t{n['region']}\t{n['title'][:60]}" for n in unmatched),
        encoding="utf-8",
    )

    print("\nCluster distribution:")
    for k, v in sorted(cluster.items(), key=lambda x: -len(x[1])):
        label = TOPICS[k]["label"]
        print(f"  {k:30} {label:20} {len(v):4d}")
    print(f"\n  [UNMATCHED]                                      {len(unmatched):4d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
