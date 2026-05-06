"""
_daily_batch.py — 每日跑一批 PDF 经 MinerU 云 API，保存结果到 outputs/

用法：
  # 首次试跑 Day 1（只跑 5 个最高优先级，验证流程）
  python _daily_batch.py --target-pages 300 --dry-run
  python _daily_batch.py --target-pages 300

  # 正式每日跑（约 1800 页）
  python _daily_batch.py

  # 指定优先级（1..6）
  python _daily_batch.py --max-priority 3

  # 断点续跑
  python _daily_batch.py --resume

状态记录：
  _mineru_state.json
    {
      "updated_at": "...",
      "done": {
        "<content_hash>": {
          "date": "2026-04-22", "pages": 12, "reg_id": "...",
          "outputs_dir": "outputs/<hash>", "status": "done"
        }
      },
      "failed": { ... },
      "daily_pages_used": {"2026-04-22": 1750}
    }
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade")
sys.path.insert(0, str(ROOT))

from _mineru_client import FileUploadSpec, MineruClient, load_env
from _priority_selector import build_candidates, filter_by_page_budget, PdfCandidate

STATE_PATH = ROOT / "_mineru_state.json"
OUTPUTS_DIR = ROOT / "outputs"
LOGS_DIR = ROOT / "logs"


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {
            "updated_at": None,
            "done": {},
            "failed": {},
            "daily_pages_used": {},
        }
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2),
                          encoding="utf-8")


def log(msg: str, log_file) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    log_file.write(line + "\n")
    log_file.flush()


def process_batch(client: MineruClient,
                  batch_specs: list[tuple[PdfCandidate, FileUploadSpec]],
                  poll_interval: float,
                  max_minutes: float,
                  log_fh) -> list[dict]:
    """
    处理一个小批（上传 + 轮询 + 下载）。返回每个文件的结果 dict。
    """
    specs = [fus for _, fus in batch_specs]
    log(f"  请求 {len(specs)} 个预签上传 URL...", log_fh)
    batch_id, upload_urls = client.request_upload_urls(specs)
    log(f"  batch_id={batch_id}", log_fh)

    # 并行上传
    log(f"  并行上传 {len(specs)} 个文件...", log_fh)

    def _up(i: int):
        cand, fus = batch_specs[i]
        try:
            client.upload_one(fus.file_path, upload_urls[i])
            return i, None
        except Exception as e:
            return i, str(e)

    upload_errors: dict[int, str] = {}
    # 并发度：3 个足以充分利用带宽，同时减少给 MinerU 服务器的 connection reset 压力
    with ThreadPoolExecutor(max_workers=3) as ex:
        for fut in as_completed([ex.submit(_up, i) for i in range(len(specs))]):
            i, err = fut.result()
            if err:
                upload_errors[i] = err
                log(f"    上传失败 [{i}] {specs[i].file_path.name}: {err[:150]}", log_fh)
    log(f"  上传完成，{len(specs) - len(upload_errors)}/{len(specs)} 成功", log_fh)

    # 轮询
    log(f"  轮询 batch 结果（最多 {max_minutes} 分钟）...", log_fh)

    def _progress(elapsed, partial_results):
        states = {}
        for r in partial_results:
            states[r.state] = states.get(r.state, 0) + 1
        log(f"    [{elapsed}s] 状态: {states}", log_fh)

    results = client.poll_batch(batch_id,
                                poll_interval=poll_interval,
                                max_minutes=max_minutes,
                                progress_cb=_progress)

    # 对齐 data_id 到 candidate
    results_by_data_id = {r.data_id: r for r in results}

    # 下载完成的
    final: list[dict] = []
    for cand, fus in batch_specs:
        if fus.data_id in upload_errors.values():
            # shouldn't happen (values 是 error strings not data_id)
            pass
        idx = [i for i, (c, _) in enumerate(batch_specs) if c.content_hash == cand.content_hash][0]
        if idx in upload_errors:
            final.append({
                "content_hash": cand.content_hash,
                "reg_id": cand.reg_id,
                "status": "upload_error",
                "err": upload_errors[idx],
                "pages": 0,
            })
            continue
        r = results_by_data_id.get(cand.content_hash)
        if r is None:
            final.append({
                "content_hash": cand.content_hash,
                "reg_id": cand.reg_id,
                "status": "no_result",
                "err": "missing in poll response",
                "pages": 0,
            })
            continue
        if r.state == "failed":
            final.append({
                "content_hash": cand.content_hash,
                "reg_id": cand.reg_id,
                "status": "mineru_failed",
                "err": r.err_msg,
                "pages": r.pages or 0,
            })
            continue
        if r.state != "done":
            final.append({
                "content_hash": cand.content_hash,
                "reg_id": cand.reg_id,
                "status": "timeout",
                "err": f"last state: {r.state}",
                "pages": r.pages or 0,
            })
            continue
        # 下载
        try:
            out_dir = client.download_and_unzip(r, OUTPUTS_DIR)
            # MinerU API 偶尔 total_pages=None，后处理从 content_list.json 数
            pages = r.pages
            if not pages:
                cl_files = list(out_dir.glob("*_content_list.json"))
                if cl_files:
                    import json as _j
                    try:
                        cl = _j.loads(cl_files[0].read_text(encoding="utf-8"))
                        page_idx = [b.get("page_idx", 0) for b in cl if isinstance(b, dict)]
                        pages = max(page_idx) + 1 if page_idx else 1
                    except Exception:
                        pages = 1
                else:
                    pages = 1
            final.append({
                "content_hash": cand.content_hash,
                "reg_id": cand.reg_id,
                "status": "done",
                "pages": pages,
                "outputs_dir": str(out_dir.relative_to(ROOT)),
            })
            log(f"    ✓ {cand.reg_id} ({pages}p) → {out_dir.name}", log_fh)
        except Exception as e:
            final.append({
                "content_hash": cand.content_hash,
                "reg_id": cand.reg_id,
                "status": "download_error",
                "err": str(e),
                "pages": r.pages or 0,
            })
    return final


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target-pages", type=int, default=None,
                    help="今天目标页数（默认读 .env DAILY_PAGE_LIMIT=1800）")
    ap.add_argument("--max-priority", type=int, default=6,
                    help="只跑 priority <= N 的候选")
    ap.add_argument("--batch-size", type=int, default=None,
                    help="每批上传多少个文件（默认 .env BATCH_SIZE=20）")
    ap.add_argument("--dry-run", action="store_true",
                    help="只预览选中的 PDF，不实际上传")
    ap.add_argument("--force", action="store_true",
                    help="即使今天已消耗页数也继续")
    ap.add_argument("--max-minutes", type=float, default=None,
                    help="每批次轮询最大分钟数（默认 .env MAX_POLL_MINUTES=15）")
    ap.add_argument("--max-size-mb", type=float, default=10.0,
                    help="跳过大于此 MB 的 PDF（0=不过滤，默认 10MB 避免大书拖垮批次）")
    args = ap.parse_args()

    # load env
    cfg = load_env(ROOT / ".env")
    token = cfg.get("MINERU_API_TOKEN") or os.environ.get("MINERU_API_TOKEN", "")
    if not token:
        print("[ERROR] MINERU_API_TOKEN 未配置，请检查 .env")
        return 1
    api_base = cfg.get("MINERU_API_BASE", "https://mineru.net/api/v4")
    target_pages = args.target_pages or int(cfg.get("DAILY_PAGE_LIMIT", "1800"))
    batch_size = args.batch_size or int(cfg.get("BATCH_SIZE", "20"))
    poll_interval = float(cfg.get("POLL_INTERVAL_SECONDS", "10"))
    max_minutes = args.max_minutes if args.max_minutes is not None else \
        float(cfg.get("MAX_POLL_MINUTES", "15"))

    # init dirs
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    log_path = LOGS_DIR / f"{today}.log"

    # state
    state = load_state()
    already_done = set(state["done"].keys())
    # MinerU 明确拒绝的（超页 / retry limit reached）不再重试，省预算
    # 但网络类失败（timeout / upload_error / download_error）继续排队重试
    permanently_failed = {
        h for h, v in state["failed"].items()
        if v.get("status") == "mineru_failed"
    }
    excluded = already_done | permanently_failed
    daily_used = state["daily_pages_used"].get(today, 0)

    print(f"\n{'='*70}")
    print(f"  MinerU Daily Batch · {today}")
    print(f"{'='*70}")
    print(f"  已完成 PDF: {len(already_done)}")
    print(f"  永久失败（跳过）: {len(permanently_failed)}")
    print(f"  今日已用页数: {daily_used} / {target_pages}")

    if daily_used >= target_pages and not args.force:
        print(f"  [SKIP] 今日已达页数上限，用 --force 强制继续")
        return 0

    remaining_budget = max(0, target_pages - daily_used)
    print(f"  剩余预算: {remaining_budget} 页")
    print(f"  批量大小: {batch_size}")
    print(f"  最大优先级: P{args.max_priority}")
    print(f"{'='*70}\n")

    # select candidates
    print("[Step 1] 构建候选队列...")
    all_cands = build_candidates()
    filtered = [c for c in all_cands if c.priority <= args.max_priority]
    print(f"  总候选: {len(all_cands)}，优先级 ≤ P{args.max_priority}: {len(filtered)}")

    # 按 size 升序排：小文件成功率高，先跑完，避免大书拖垮整批
    filtered.sort(key=lambda c: (c.priority, c.size_mb))

    # 可选过滤：MinerU 服务器拥塞时跳过大书（--max-size-mb）
    if args.max_size_mb > 0:
        before = len(filtered)
        filtered = [c for c in filtered if c.size_mb <= args.max_size_mb]
        skipped = before - len(filtered)
        if skipped > 0:
            print(f"  [size filter] 跳过 {skipped} 个 > {args.max_size_mb}MB 的文件")

    selected = filter_by_page_budget(filtered, remaining_budget, excluded)
    print(f"  今天选中 {len(selected)} 个 PDF（估 {sum(max(1, int(c.size_mb * 30)) for c in selected)} 页）")

    if not selected:
        print("  没有候选可跑，退出")
        return 0

    print("\n  Top 10 选中预览:")
    for c in selected[:10]:
        print(f"    P{c.priority} [{c.reason:<22}] {c.reg_id or '?':<28} "
              f"{c.size_mb:.1f}MB  {c.pdf_path.name}")
    if len(selected) > 10:
        print(f"    ... 还有 {len(selected) - 10} 个")

    if args.dry_run:
        print("\n[DRY RUN] 不执行任何 API 调用，退出")
        return 0

    # 执行
    print("\n[Step 2] 调用 MinerU 云 API...")
    log_fh = log_path.open("a", encoding="utf-8")
    log(f"=== Daily batch {today} ===", log_fh)
    log(f"选中 {len(selected)} 个 PDF，批次大小 {batch_size}", log_fh)

    client = MineruClient(token, api_base)
    all_results: list[dict] = []
    total_pages_used = 0
    consecutive_failures = 0  # 连续批次失败计数（熔断用）

    try:
        # 分批跑
        for bi in range(0, len(selected), batch_size):
            batch = selected[bi:bi + batch_size]
            log(f"\n--- Batch {bi//batch_size + 1} / {(len(selected)-1)//batch_size + 1} "
                f"({len(batch)} files) ---", log_fh)

            specs = [(c, FileUploadSpec(file_path=c.pdf_path,
                                        data_id=c.content_hash,
                                        is_ocr=True))
                     for c in batch]
            try:
                batch_results = process_batch(
                    client, specs, poll_interval, max_minutes, log_fh)
                consecutive_failures = 0  # 成功就重置
            except Exception as e:
                log(f"  [ERROR] batch 失败: {e}", log_fh)
                consecutive_failures += 1
                # 熔断：连续 5 批完全失败 → MinerU 明显拒绝服务，整进程 sleep 10 分钟
                # 避免空转 85 批浪费 state 写入 + watchdog 日志噪声
                if consecutive_failures >= 5:
                    log(f"  [CIRCUIT-BREAKER] 连续 {consecutive_failures} 批失败，"
                        f"休眠 10 分钟等 MinerU 恢复...", log_fh)
                    time.sleep(600)
                    consecutive_failures = 0
                continue

            all_results.extend(batch_results)

            # 更新 state（每批后落盘）
            for rec in batch_results:
                if rec["status"] == "done":
                    state["done"][rec["content_hash"]] = {
                        "date": today,
                        "pages": rec["pages"],
                        "reg_id": rec["reg_id"],
                        "outputs_dir": rec.get("outputs_dir", ""),
                        "status": "done",
                    }
                    total_pages_used += rec["pages"]
                else:
                    state["failed"][rec["content_hash"]] = {
                        "date": today,
                        "reg_id": rec["reg_id"],
                        "status": rec["status"],
                        "err": rec.get("err", ""),
                    }
            state["daily_pages_used"][today] = daily_used + total_pages_used
            save_state(state)
            log(f"  批次汇总: done={sum(1 for r in batch_results if r['status']=='done')}/"
                f"{len(batch_results)}  累计页数={total_pages_used}", log_fh)

            # 节流，避免 rate limit
            if bi + batch_size < len(selected):
                time.sleep(5)
    finally:
        client._client.close()
        log(f"\n=== 结束 === 本次处理 {len(all_results)}，"
            f"成功 {sum(1 for r in all_results if r['status']=='done')}，"
            f"页数 {total_pages_used}", log_fh)
        log_fh.close()

    # 终汇总
    print(f"\n{'='*70}")
    done = [r for r in all_results if r["status"] == "done"]
    failed = [r for r in all_results if r["status"] != "done"]
    print(f"  成功: {len(done)}  |  失败: {len(failed)}  |  页数: {total_pages_used}")
    if failed:
        print(f"\n  失败样例（前 5）:")
        for r in failed[:5]:
            print(f"    {r.get('reg_id','?'):<30} {r['status']:<15} {r.get('err','')[:60]}")
    print(f"\n  日志: {log_path}")
    print(f"  状态: {STATE_PATH}")
    print(f"  累计完成 PDF: {len(state['done'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
