"""
Pipeline stages

s0_ocr        — OCR 分层（调 ocr/ 模块）
s1_extract    — DeepSeek V3 结构化抽取
s2_cross_check — Sonnet 4.6 cross-check
s3_equivalence — Opus 4.7 跨区等效关系判定
s4_topic_summary — Sonnet 4.6 topic 综述
s5_graphrag   — Opus 4.7 GraphRAG community summary (Phase 3)

TODO(Day 2-3): 实现各 stage 的 run_single() 和 run_batch()
"""
