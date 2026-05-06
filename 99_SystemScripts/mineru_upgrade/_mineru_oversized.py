"""
_mineru_oversized.py — Phase 2：把拆好的 22 个 part PDF 上传到 MinerU 并下载结果

依赖：
  - Phase 1 产物：`_split_work/<reg_id>__partN.pdf`
  - Phase 1 manifest：`_split_work/_split_manifest.json`

输出：
  - `outputs/<reg_id>__partN/` 每个 part 的 MinerU 解析结果
  - `_oversized_state.json` 跟踪上传/下载状态（独立于 _mineru_state.json）

设计要点：
  - **不**使用 _mineru_state.json，避免和正常 daily_batch 互相干扰
  - 用 `<safe_reg_id>__partN` 作为 data_id（避免 hash 冲突）
  - 默认 batch_size=20，22 parts 分 2 批
  - 每日页数预算独立控制（默认 1500p，留余量给 daily_batch）
  - 失败的 part 不影响其他 part 的处理

用法：
    python _mineru_oversized.py --dry-run         # 预览
    python _mineru_oversized.py                   # 跑全部 22 parts
    python _mineru_oversized.py --max-parts 10    # 只跑前 10 个（页数预算紧时）
    python _mineru_oversized.py --reg-id "ECE R83"  # 只跑某 reg_id 的所有 part
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

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from _mineru_client import FileUploadSpec, MineruClient, load_env

WORK = ROOT / "_split_work"
MANIFEST_PATH = WORK / "_split_manifest.json"
OUTPUTS_DIR = ROOT / "outputs"
LOGS_DIR = ROOT / "logs"
STATE_PATH = ROOT / "_oversized_state.json"


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {
        "updated_at": None,
        "done": {},      # data_id -> {date, pages, reg_id, part_idx, outputs_dir}
        "failed": {},
        "daily_pages_used": {},
    }


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


def expand_parts(manifest: dict) -> list[dict]:
    """
    把 manifest['results'] 展开成 part 级别清单
    每个 part 加 data_id（用文件 stem 作 id，独立于 _mineru_state.json）
    """
    parts = []
    for r in manifest.get("results", []):
        if r.get("status") not in ("split_ok", "split_planned"):
            continue
        for p in r.get("parts", []):
            file_stem = Path(p["file"]).stem  # e.g. "ECE_R83__part1"
            parts.append({
                "data_id": file_stem,
                "reg_id": r["reg_id"],
                "part_idx": p["idx"],
                "file": p["file"],
                "file_path": WORK / p["file"],
                "pages": p["pages"],
                "page_range": p.get("page_range"),
            })
    return parts


def process_batch(client: MineruClient,
                  batch_specs: list[tuple[dict, FileUploadSpec]],
                  poll_interval: float,
                  max_minutes: float,
                  log_fh) -> list[dict]:
    """处理一个小批：上传、轮询、下载"""
    specs = [fus for _, fus in batch_specs]
    log(f"  请求 {len(specs)} 个预签上传 URL...", log_fh)
    batch_id, upload_urls = client.request_upload_urls(specs)
    log(f"  batch_id={batch_id}", log_fh)

    log(f"  并行上传 {len(specs)} 个文件...", log_fh)

    def _up(i: int):
        part, fus = batch_specs[i]
        try:
            client.upload_one(fus.file_path, upload_urls[i])
            return i, None
        except Exception as e:
            return i, str(e)

    upload_errors: dict[int, str] = {}
    with ThreadPoolExecutor(max_workers=3) as ex:
        for fut in as_completed([ex.submit(_up, i) for i in range(len(specs))]):
            i, err = fut.result()
            if err:
                upload_errors[i] = err
                log(f"    上传失败 [{i}] {specs[i].file_path.name}: {err[:150]}", log_fh)
    log(f"  上传完成，{len(specs) - len(upload_errors)}/{len(specs)} 成功", log_fh)

    log(f"  轮询 batch（最多 {max_minutes} 分钟）...", log_fh)

    def _progress(elapsed, partial_results):
        states = {}
        for r in partial_results:
            states[r.state] = states.get(r.state, 0) + 1
        log(f"    [{elapsed}s] 状态: {states}", log_fh)

    results = client.poll_batch(batch_id,
                                poll_interval=poll_interval,
                                max_minutes=max_minutes,
                                progress_cb=_progress)

    results_by_data_id = {r.data_id: r for r in results}
    final: list[dict] = []
    for part, fus in batch_specs:
        idx = [i for i, (p, _) in enumerate(batch_specs) if p["data_id"] == part["data_id"]][0]
        if idx in upload_errors:
            final.append({**part, "status": "upload_error",
                          "err": upload_errors[idx], "actual_pages": 0})
            continue
        r = results_by_data_id.get(part["data_id"])
        if r is None:
            final.append({**part, "status": "no_result",
                          "err": "missing in poll response", "actual_pages": 0})
            continue
        if r.state == "failed":
            final.append({**part, "status": "mineru_failed",
                          "err": r.err_msg, "actual_pages": r.pages or 0})
            continue
        if r.state != "done":
            final.append({**part, "status": "timeout",
                          "err": f"last state: {r.state}", "actual_pages": r.pages or 0})
            continue
        # 下载
        try:
            out_dir = client.download_and_unzip(r, OUTPUTS_DIR)
            actual_pages = r.pages
            if not actual_pages:
                cl_files = list(out_dir.glob("*_content_list.json"))
                if cl_files:
                    try:
                        cl = json.loads(cl_files[0].read_text(encoding="utf-8"))
                        page_idx = [b.get("page_idx", 0) for b in cl if isinstance(b, dict)]
                        actual_pages = max(page_idx) + 1 if page_idx else 1
                    except Exception:
                        actual_pages = part["pages"]
                else:
                    actual_pages = part["pages"]
            final.append({**part,
                          "status": "done",
                          "actual_pages": actual_pages,
                          "outputs_dir": str(out_dir.relative_to(ROOT))})
            log(f"    ✓ {part['reg_id']} part{part['part_idx']} ({actual_pages}p) "
                f"→ {out_dir.name}", log_fh)
        except Exception as e:
            final.append({**part, "status": "download_error",
                          "err": str(e), "actual_pages": r.pages or 0})
    return final


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target-pages", type=int, default=1500,
                    help="今日目标页数（默认 1500，给 daily_batch 留余量）")
    ap.add_argument("--batch-size", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-parts", type=int, help="只跑前 N 个 part")
    ap.add_argument("--reg-id", help="只跑某个 reg_id 的所有 part")
    ap.add_argument("--max-minutes", type=float, default=15.0)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if not MANIFEST_PATH.exists():
        print(f"[ERROR] manifest 不存在，请先跑 _split_large_pdfs.py")
        print(f"  期望: {MANIFEST_PATH}")
        return 1

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    parts = expand_parts(manifest)

    if args.reg_id:
        parts = [p for p in parts if p["reg_id"] == args.reg_id]
        if not parts:
            print(f"[ERROR] reg_id={args.reg_id} 没有 part")
            return 1

    cfg = load_env(ROOT / ".env")
    token = cfg.get("MINERU_API_TOKEN") or os.environ.get("MINERU_API_TOKEN", "")
    if not token:
        print("[ERROR] MINERU_API_TOKEN 未配置")
        return 1
    api_base = cfg.get("MINERU_API_BASE", "https://mineru.net/api/v4")
    poll_interval = float(cfg.get("POLL_INTERVAL_SECONDS", "10"))

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    log_path = LOGS_DIR / f"{today}_oversized.log"

    state = load_state()
    already_done = set(state["done"].keys())
    daily_used = state["daily_pages_used"].get(today, 0)

    print(f"\n{'='*72}")
    print(f"  超页 PDF Phase 2 · MinerU 上传 · {today}")
    print(f"{'='*72}")
    print(f"  manifest 中 parts 总数: {len(parts)}")
    print(f"  已完成 parts: {len(already_done)}")
    print(f"  今日 oversized 已用页数: {daily_used} / {args.target_pages}")

    # 过滤未完成
    remaining = [p for p in parts if p["data_id"] not in already_done]
    print(f"  剩余 parts: {len(remaining)}")

    # 按页数预算挑
    selected = []
    used = 0
    for p in remaining:
        if used + p["pages"] > (args.target_pages - daily_used) and selected:
            break
        selected.append(p)
        used += p["pages"]
        if args.max_parts and len(selected) >= args.max_parts:
            break

    print(f"  本次选中: {len(selected)} parts, 估 {used} 页")
    print(f"{'='*72}\n")

    if not selected:
        print("  无候选可跑，退出")
        return 0

    print("  Top 10 选中预览:")
    for p in selected[:10]:
        print(f"    {p['reg_id']} part{p['part_idx']:<2}  {p['pages']:>3}p  → {p['file']}")
    if len(selected) > 10:
        print(f"    ... 还有 {len(selected) - 10} 个")

    if args.dry_run:
        print("\n[DRY RUN] 不调用 API，退出")
        return 0

    # 实跑
    print("\n[Step] 调用 MinerU 云 API...")
    log_fh = log_path.open("a", encoding="utf-8")
    log(f"=== Oversized batch {today} ===", log_fh)
    log(f"选中 {len(selected)} parts，批次大小 {args.batch_size}", log_fh)

    client = MineruClient(token, api_base)
    all_results: list[dict] = []
    total_pages_used = 0

    try:
        for bi in range(0, len(selected), args.batch_size):
            batch = selected[bi:bi + args.batch_size]
            log(f"\n--- Batch {bi//args.batch_size + 1} / "
                f"{(len(selected) - 1)//args.batch_size + 1} "
                f"({len(batch)} parts) ---", log_fh)
            specs = [(p, FileUploadSpec(file_path=p["file_path"],
                                        data_id=p["data_id"],
                                        is_ocr=True))
                     for p in batch]
            try:
                rs = process_batch(client, specs, poll_interval,
                                   args.max_minutes, log_fh)
            except Exception as e:
                log(f"  [ERROR] batch 失败: {e}", log_fh)
                continue

            all_results.extend(rs)
            for rec in rs:
                if rec["status"] == "done":
                    state["done"][rec["data_id"]] = {
                        "date": today,
                        "pages": rec["actual_pages"],
                        "reg_id": rec["reg_id"],
                        "part_idx": rec["part_idx"],
                        "outputs_dir": rec.get("outputs_dir", ""),
                        "status": "done",
                    }
                    total_pages_used += rec["actual_pages"]
                else:
                    state["failed"][rec["data_id"]] = {
                        "date": today,
                        "reg_id": rec["reg_id"],
                        "part_idx": rec["part_idx"],
                        "status": rec["status"],
                        "err": rec.get("err", ""),
                    }
            state["daily_pages_used"][today] = daily_used + total_pages_used
            save_state(state)

            log(f"  批次汇总: done="
                f"{sum(1 for r in rs if r['status']=='done')}/{len(rs)}  "
                f"累计页数={total_pages_used}", log_fh)

            if bi + args.batch_size < len(selected):
                time.sleep(5)
    finally:
        client._client.close()
        log(f"\n=== 结束 === 处理 {len(all_results)} parts，"
            f"成功 {sum(1 for r in all_results if r['status']=='done')}，"
            f"页数 {total_pages_used}", log_fh)
        log_fh.close()

    print(f"\n{'='*72}")
    done = [r for r in all_results if r["status"] == "done"]
    failed = [r for r in all_results if r["status"] != "done"]
    print(f"  成功: {len(done)}  失败: {len(failed)}  页数: {total_pages_used}")
    if failed:
        print(f"\n  失败明细:")
        for r in failed[:10]:
            print(f"    {r['reg_id']} part{r['part_idx']}  {r['status']:<15} "
                  f"{r.get('err', '')[:60]}")
    print(f"\n  日志: {log_path}")
    print(f"  状态: {STATE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
