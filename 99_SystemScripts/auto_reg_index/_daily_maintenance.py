"""
一键维护脚本 —— 每日/每周/按需调用，自动完成：

  阶段 A · Ingest
    1. 扫 RAW_SOURCE_DIR 检测新 PDF
    2. S0 OCR 新文件
    3. S1 Extract 新文件
    4. 写入 Obsidian（ingest.py run --stage write）

  阶段 B · 质量复核
    5. _backfill_titles.py（补齐 title / date / status）
    6. _run_cross_check.py（DeepSeek 校对）
    7. _reclassify_false_mismatches.py（规则降级假告警）

  阶段 C · 导航层更新
    8. _cluster_topics.py（重聚类）
    9. _write_topic_pages.py（重生成主题页）
    10. _extract_topic_equivalences.py + _write_equivalence_page.py + _apply_equivalences_to_notes.py
    11. _build_supersession_chain.py（双向链）

  阶段 D · Stage 5 索引
    12. _build_graph.py + _graph_analytics.py
    13. _semantic_search.py --rebuild

  阶段 E · 变化报告
    14. 统计并打印前后差异

用法：
    python _daily_maintenance.py                 # 完整跑一遍
    python _daily_maintenance.py --dry-run       # 仅检测，不改动
    python _daily_maintenance.py --skip-ingest   # 只跑 BCDE（库内刷新）
    python _daily_maintenance.py --skip-llm      # 不调 DeepSeek（加快）
    python _daily_maintenance.py --only-index    # 只重建 BM25 + Graph
    python _daily_maintenance.py --log logs/maint_YYYYMMDD.log

日志位置：`logs/maintenance_YYYYMMDD_HHMMSS.log`（自动记录）
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
LOG_DIR = ROOT / "logs"
PY = ROOT / ".venv" / "Scripts" / "python.exe"

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
TOPICS_DIR = Path(r"D:\CcVault\04_Topics")
DASHBOARDS_DIR = Path(r"D:\CcVault\00_Dashboards")

# 各阶段的脚本清单（按顺序执行）
STAGE_B = [
    ("_backfill_titles.py", ["--also-dates", "--also-status"], "补齐 title/date/status"),
    ("_run_cross_check.py", ["--provider", "deepseek"], "Cross-check 质量校对"),
    ("_reclassify_false_mismatches.py", [], "假告警规则降级"),
]

STAGE_C = [
    ("_cluster_topics.py", [], "主题聚类"),
    ("_write_topic_pages.py", [], "生成主题页"),
    ("_extract_topic_equivalences.py", [], "提取跨区域映射"),
    ("_write_equivalence_page.py", [], "生成等价 MOC"),
    ("_apply_equivalences_to_notes.py", [], "回写 equivalent_to"),
    ("_build_supersession_chain.py", [], "Supersedes 双向链"),
]

STAGE_D = [
    ("_build_graph.py", [], "构建关系图"),
    ("_graph_analytics.py", [], "图分析 (PageRank/Betweenness)"),
    ("_semantic_search.py", ["--rebuild"], "重建 BM25 索引"),
]


def now_str() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def log_print(msg: str, log_file):
    """同时输出到 stdout 和日志文件（对 stdout 做 GBK 安全降级）"""
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    try:
        print(line, flush=True)
    except UnicodeEncodeError:
        # Windows GBK 控制台无法输出某些 Unicode 符号，降级为 ASCII
        safe = line.encode("gbk", errors="replace").decode("gbk")
        print(safe, flush=True)
    if log_file:
        log_file.write(line + "\n")
        log_file.flush()


def count_notes(folder: Path, pattern: str = "*.md") -> int:
    if not folder.exists():
        return 0
    return len(list(folder.rglob(pattern)))


def snapshot() -> dict:
    """快照当前库的状态"""
    return {
        "regulations": count_notes(WIKI),
        "cn": count_notes(WIKI / "cn"),
        "ece": count_notes(WIKI / "ece"),
        "topics": count_notes(TOPICS_DIR),
        "dashboards": count_notes(DASHBOARDS_DIR),
        "timestamp": now_str(),
    }


def run_script(name: str, args: list[str], desc: str, *, log_file, dry_run: bool = False) -> bool:
    """运行一个脚本，返回是否成功"""
    script = ROOT / name
    if not script.exists():
        log_print(f"  [SKIP] {name} (not found)", log_file)
        return True  # 不致命
    cmd = [str(PY), str(script), *args]
    if dry_run:
        log_print(f"  [DRY] {desc}: {' '.join(cmd)}", log_file)
        return True
    log_print(f"  ▶ {desc} ({name})", log_file)
    t0 = time.time()
    try:
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=3600,  # 1 小时上限
        )
        dt = time.time() - t0
        if result.returncode == 0:
            log_print(f"    ✓ Done in {dt:.1f}s", log_file)
            # 输出最后几行到日志
            tail = "\n".join(result.stdout.splitlines()[-5:]) if result.stdout else ""
            if tail.strip():
                for line in tail.splitlines():
                    log_file.write(f"      {line}\n")
            return True
        else:
            log_print(f"    ✗ FAILED rc={result.returncode} in {dt:.1f}s", log_file)
            if result.stderr:
                log_file.write(f"STDERR:\n{result.stderr[-2000:]}\n")
            if result.stdout:
                log_file.write(f"STDOUT (tail):\n{result.stdout[-1000:]}\n")
            return False
    except subprocess.TimeoutExpired:
        log_print(f"    ✗ TIMEOUT (>1h)", log_file)
        return False
    except Exception as e:
        log_print(f"    ✗ EXCEPTION {e}", log_file)
        return False


def stage_ingest(log_file, dry_run: bool, skip_llm: bool) -> tuple[int, int]:
    """阶段 A：OCR + Extract 新 PDF。返回 (new_ocr, new_extract)"""
    log_print("─ 阶段 A · Ingest (OCR + Extract) ─", log_file)

    ingest_py = ROOT / "ingest.py"
    if not ingest_py.exists():
        log_print("  [SKIP] ingest.py not found", log_file)
        return 0, 0

    # 1. 扫 manifest 看有多少 pending
    mf_path = ROOT / "manifest.json"
    pending_before = 0
    ocr_done_before = 0
    if mf_path.exists():
        try:
            mf = json.loads(mf_path.read_text(encoding="utf-8"))
            for rec in mf.get("records", {}).values():
                state = rec.get("state", "")
                if state == "pending":
                    pending_before += 1
                elif state == "ocr_done":
                    ocr_done_before += 1
        except Exception as e:
            log_print(f"  [WARN] manifest parse: {e}", log_file)

    log_print(f"  Manifest pre-check: pending={pending_before}, ocr_done_pending_extract={ocr_done_before}", log_file)

    # 如果没 pending 也没 ocr_done，直接跳（意味着没新文件）
    if pending_before == 0 and ocr_done_before == 0:
        log_print("  [SKIP] 无 pending / ocr_done 文件，跳过 S0/S1", log_file)
        return 0, 0

    if dry_run:
        log_print("  [DRY] 会跑 S0 和 S1", log_file)
        return pending_before, ocr_done_before

    # 2. S0 OCR
    if pending_before > 0:
        log_print(f"  ▶ S0 OCR ({pending_before} files)", log_file)
        if skip_llm:
            log_print("    [SKIP due to --skip-llm]", log_file)
        else:
            ok = run_script("ingest.py", ["run", "--stage", "0"], "S0 OCR", log_file=log_file, dry_run=False)
            if not ok:
                log_print("    [WARN] S0 有失败，继续 S1", log_file)

    # 3. S1 Extract
    if ocr_done_before > 0 or pending_before > 0:
        if skip_llm:
            log_print("    [SKIP S1 due to --skip-llm]", log_file)
        else:
            ok = run_script("ingest.py", ["run", "--stage", "1"], "S1 Extract", log_file=log_file, dry_run=False)
            if not ok:
                log_print("    [WARN] S1 有失败", log_file)

    # 4. Write to Obsidian
    if not skip_llm:
        run_script("ingest.py", ["run", "--stage", "write"], "Write to Obsidian", log_file=log_file, dry_run=False)

    return pending_before, ocr_done_before


def stage_quality(log_file, dry_run: bool, skip_llm: bool):
    """阶段 B：质量复核"""
    log_print("─ 阶段 B · Quality Recheck ─", log_file)
    for name, args, desc in STAGE_B:
        if skip_llm and name in ("_run_cross_check.py",):
            log_print(f"  [SKIP {name} due to --skip-llm]", log_file)
            continue
        run_script(name, args, desc, log_file=log_file, dry_run=dry_run)


def stage_navigation(log_file, dry_run: bool):
    """阶段 C：导航层（主题/等价/supersession）"""
    log_print("─ 阶段 C · Navigation Layer ─", log_file)
    for name, args, desc in STAGE_C:
        run_script(name, args, desc, log_file=log_file, dry_run=dry_run)


def stage_indices(log_file, dry_run: bool):
    """阶段 D：Stage 5 索引（图 + BM25）"""
    log_print("─ 阶段 D · Stage 5 Indices ─", log_file)
    for name, args, desc in STAGE_D:
        run_script(name, args, desc, log_file=log_file, dry_run=dry_run)


def stage_report(log_file, before: dict, after: dict):
    """阶段 E：打印变化报告"""
    log_print("─ 阶段 E · 变化报告 ─", log_file)
    for key in ("regulations", "cn", "ece", "topics", "dashboards"):
        b, a = before.get(key, 0), after.get(key, 0)
        diff = a - b
        sign = "+" if diff > 0 else ("" if diff == 0 else "")
        log_print(f"  {key:<15s}  {b:>5d} → {a:>5d}  ({sign}{diff:+d})" if diff else f"  {key:<15s}  {a:>5d}  (no change)", log_file)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只检测，不改动")
    ap.add_argument("--skip-ingest", action="store_true", help="跳过 A 阶段（库内刷新）")
    ap.add_argument("--skip-llm", action="store_true", help="不调 LLM（加快）")
    ap.add_argument("--skip-quality", action="store_true", help="跳过 B 阶段")
    ap.add_argument("--skip-navigation", action="store_true", help="跳过 C 阶段")
    ap.add_argument("--only-index", action="store_true", help="只重建 BM25 + Graph")
    ap.add_argument("--log", type=str, help="日志文件路径（默认 logs/maintenance_<ts>.log）")
    args = ap.parse_args()

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = Path(args.log) if args.log else LOG_DIR / f"maintenance_{now_str()}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    t_start = time.time()

    with open(log_path, "w", encoding="utf-8") as log_file:
        log_print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", log_file)
        log_print(f"CcVault 一键维护启动", log_file)
        log_print(f"  dry-run: {args.dry_run}", log_file)
        log_print(f"  skip-ingest: {args.skip_ingest}", log_file)
        log_print(f"  skip-llm: {args.skip_llm}", log_file)
        log_print(f"  only-index: {args.only_index}", log_file)
        log_print(f"  log: {log_path}", log_file)
        log_print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", log_file)

        before = snapshot()
        log_print(f"Before: {before}", log_file)

        if args.only_index:
            # 只跑 Stage D
            stage_indices(log_file, args.dry_run)
        else:
            # A. Ingest
            if not args.skip_ingest:
                stage_ingest(log_file, args.dry_run, args.skip_llm)
            else:
                log_print("─ [SKIP 阶段 A] ─", log_file)

            # B. Quality
            if not args.skip_quality:
                stage_quality(log_file, args.dry_run, args.skip_llm)
            else:
                log_print("─ [SKIP 阶段 B] ─", log_file)

            # C. Navigation
            if not args.skip_navigation:
                stage_navigation(log_file, args.dry_run)
            else:
                log_print("─ [SKIP 阶段 C] ─", log_file)

            # D. Indices
            stage_indices(log_file, args.dry_run)

        # E. Report
        after = snapshot()
        stage_report(log_file, before, after)

        dt = time.time() - t_start
        log_print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", log_file)
        log_print(f"完成 · 耗时 {dt/60:.1f} 分钟 · 日志 {log_path}", log_file)
        log_print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", log_file)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
