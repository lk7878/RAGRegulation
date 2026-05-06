"""
_merge_split_mineru.py — Phase 3：把 reg_id 的所有 part outputs 合并成单条 note 的 "原文参考" 段

输入：
  - `_oversized_state.json` 中 status=done 的 part 条目
  - `_split_work/_split_manifest.json` 知道每个 reg_id 的预期 part 数量
  - `outputs/<safe_reg_id>__partN/` 各 part 的 MinerU 解析

输出：
  - 把所有 ready 的 reg_id（即 done 的 part 数 == 预期 part 数）合并到对应 note：
    - 拼接 part1 + part2 + ... 的 tables / formulas / images
    - page_idx 累加偏移（part2 的 page 0 = part1 的总页数 + 0）
    - 图像从各 part 目录拷贝到 `01_Wiki/regulations/_mineru_assets/<reg_id>/`
    - 在 note 末尾追加 "## 原文参考（MinerU 云解析）" 段
    - FM 加 `_ocr_upgraded: mineru_split`、`_mineru_split_parts` 列表

用法：
    python _merge_split_mineru.py --dry-run                # 预览
    python _merge_split_mineru.py                          # 跑全部 ready
    python _merge_split_mineru.py --reg-id "ECE R37 Rev8"  # 只跑一条
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# 复用 _merge_upgrade.py 的工具函数
from _merge_upgrade import (
    extract_blocks,
    copy_image,
    FM_RE,
    WIKI,
    ASSETS_DIR,
)

OUTPUTS_DIR = ROOT / "outputs"
WORK = ROOT / "_split_work"
SPLIT_MANIFEST = WORK / "_split_manifest.json"
OVERSIZED_STATE = ROOT / "_oversized_state.json"


def safe_name(reg_id: str) -> str:
    """与 _split_large_pdfs.py 保持一致"""
    return re.sub(r"[\\/\(\)\s]+", "_", reg_id).strip("_")


def load_split_manifest() -> dict:
    return json.loads(SPLIT_MANIFEST.read_text(encoding="utf-8"))


def load_oversized_state() -> dict:
    return json.loads(OVERSIZED_STATE.read_text(encoding="utf-8"))


def collect_ready_reg_ids(split_manifest: dict, oversized_state: dict) -> dict[str, list[dict]]:
    """
    返回 {reg_id: [part_info, ...]}，仅当所有 parts 都 done 时才返回该 reg_id
    每个 part_info: {part_idx, file, pages, page_range, outputs_dir, actual_pages}
    """
    # 先建预期：每个 reg_id 的 part 数量和文件名
    expected: dict[str, list[dict]] = defaultdict(list)
    for r in split_manifest.get("results", []):
        if r.get("status") not in ("split_ok", "split_planned"):
            continue
        for p in r.get("parts", []):
            data_id = Path(p["file"]).stem
            expected[r["reg_id"]].append({
                "data_id": data_id,
                "part_idx": p["idx"],
                "file": p["file"],
                "pages": p["pages"],
                "page_range": p.get("page_range"),
            })

    done = oversized_state.get("done", {})
    ready: dict[str, list[dict]] = {}

    for reg_id, parts in expected.items():
        # 检查是否所有 part 都 done
        all_done = all(p["data_id"] in done for p in parts)
        if not all_done:
            continue
        merged_parts = []
        for p in sorted(parts, key=lambda x: x["part_idx"]):
            d = done[p["data_id"]]
            merged_parts.append({
                **p,
                "outputs_dir": d["outputs_dir"],
                "actual_pages": d["pages"],
            })
        ready[reg_id] = merged_parts

    return ready


def find_note_by_reg_id(reg_id: str) -> Path | None:
    """扫 WIKI 找 reg_id 对应的 note 路径"""
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = FM_RE.match(txt)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if fm.get("reg_id") == reg_id:
            return p
    return None


def merge_parts_buckets(parts: list[dict]) -> tuple[dict, int, list[Path]]:
    """
    把所有 part 的 content_list 合并成单一 buckets，page_idx 累加偏移
    返回：(buckets, total_full_md_chars, list_of_part_out_dirs)
    """
    merged_buckets = {"text": [], "table": [], "image": [], "equation": []}
    total_full_md = 0
    part_dirs: list[Path] = []

    page_offset = 0
    for p in parts:
        out_dir = ROOT / p["outputs_dir"]
        if not out_dir.exists():
            print(f"  [WARN] part{p['part_idx']} 目录不存在: {out_dir}")
            continue
        part_dirs.append(out_dir)

        # content_list
        cl_files = list(out_dir.glob("*_content_list.json"))
        if not cl_files:
            print(f"  [WARN] part{p['part_idx']} 缺 content_list.json")
            continue
        try:
            cl = json.loads(cl_files[0].read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  [WARN] part{p['part_idx']} content_list.json 解析失败: {e}")
            continue

        # full.md 字符数
        full_md_path = out_dir / "full.md"
        if full_md_path.exists():
            try:
                total_full_md += len(full_md_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        # 把每个 block 的 page_idx 加 page_offset
        buckets = extract_blocks(cl)
        for typ, blocks in buckets.items():
            for blk in blocks:
                if isinstance(blk.get("page_idx"), int):
                    blk["page_idx"] = blk["page_idx"] + page_offset
                # 标注 part 来源（用于调试，不渲染）
                blk["_part_idx"] = p["part_idx"]
            merged_buckets.setdefault(typ, []).extend(blocks)

        page_offset += p.get("actual_pages", p["pages"])

    return merged_buckets, total_full_md, part_dirs


def render_split_section(buckets: dict[str, list[dict]],
                         part_dirs: list[Path],
                         reg_id: str,
                         total_full_md_chars: int,
                         parts_summary: list[dict],
                         *,
                         max_tables: int = 15,
                         max_formulas: int = 25,
                         max_images: int = 12) -> tuple[str, dict]:
    """渲染合并后的 "原文参考" 段，比 _merge_upgrade 版本上限更宽（因合并结果更大）"""
    stats = {"tables": 0, "formulas": 0, "images": 0}
    lines: list[str] = []

    today = date.today().isoformat()
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## 原文参考（MinerU 云解析 · 多分块合并 · {today}）")
    lines.append("")

    # 分块说明
    parts_str = " + ".join(
        f"part{p['part_idx']} ({p['actual_pages']}p)" for p in parts_summary
    )
    lines.append(f"> 本 PDF 因超过 MinerU 200 页限制被拆为 {len(parts_summary)} 块分别 OCR，再合并：")
    lines.append(f"> {parts_str}")
    lines.append(f">")
    lines.append(f"> 共解析到：")
    lines.append(f"> - 表格 {len(buckets.get('table', []))} 个")
    lines.append(f"> - 公式 {len(buckets.get('equation', []))} 个")
    lines.append(f"> - 图像 {len(buckets.get('image', []))} 个")
    lines.append(f"> - 全文 Markdown 合计 {total_full_md_chars:,} 字符")
    lines.append("")

    # 表格（取页数前列）
    tables = buckets.get("table", [])[:max_tables]
    if tables:
        lines.append(f"### 表格（取前 {len(tables)} 个）")
        lines.append("")
        for i, tb in enumerate(tables, 1):
            cap = tb.get("table_caption") or []
            cap_str = " / ".join(cap) if isinstance(cap, list) else str(cap)
            page = tb.get("page_idx", "?")
            part = tb.get("_part_idx", "?")
            lines.append(f"#### 表 {i} (page {page}, part{part})")
            if cap_str.strip():
                lines.append(f"**{cap_str}**")
                lines.append("")
            html = tb.get("table_body", "")
            if html:
                lines.append(html.strip())
                lines.append("")
                stats["tables"] += 1

    # 公式
    eqs = buckets.get("equation", [])[:max_formulas]
    if eqs:
        lines.append(f"### 公式（取前 {len(eqs)} 个）")
        lines.append("")
        for i, eq in enumerate(eqs, 1):
            latex = eq.get("text", "").strip()
            page = eq.get("page_idx", "?")
            part = eq.get("_part_idx", "?")
            if latex:
                if not latex.startswith("$"):
                    latex = f"$$\n{latex}\n$$"
                lines.append(f"**公式 {i}** (page {page}, part{part}):")
                lines.append("")
                lines.append(latex)
                lines.append("")
                stats["formulas"] += 1

    # 图像（关键：图像的 src_out_dir 取决于 part_idx，要从对应 part_dirs 里找）
    imgs = buckets.get("image", [])[:max_images]
    copied_imgs = []
    # 建立 part_idx → out_dir 索引
    part_idx_to_dir: dict[int, Path] = {}
    for d in part_dirs:
        # part_dirs 里的目录名形如 ECE_R37_Rev8__part1
        m = re.search(r"__part(\d+)$", d.name)
        if m:
            part_idx_to_dir[int(m.group(1))] = d

    for img in imgs:
        img_path = img.get("img_path", "")
        caption = img.get("image_caption") or []
        cap_str = " / ".join(caption) if isinstance(caption, list) else str(caption)
        page = img.get("page_idx", "?")
        part = img.get("_part_idx")
        src_dir = part_idx_to_dir.get(part)
        if not src_dir:
            continue
        wiki_rel = copy_image(img_path, src_dir, reg_id)
        if wiki_rel:
            copied_imgs.append((wiki_rel, cap_str, page, part))
            stats["images"] += 1

    if copied_imgs:
        lines.append(f"### 图像（取前 {len(copied_imgs)} 张）")
        lines.append("")
        for wiki_rel, cap, page, part in copied_imgs:
            alt = cap if cap.strip() else f"图 page {page}"
            lines.append(f"![{alt}](../{wiki_rel})  ")
            if cap.strip():
                lines.append(f"*{cap}* (page {page}, part{part})")
            else:
                lines.append(f"*page {page}, part{part}*")
            lines.append("")

    return "\n".join(lines), stats


def merge_one_reg(reg_id: str, parts: list[dict], dry_run: bool) -> dict:
    """合并单个 reg_id 的所有 parts 到对应 note"""
    result = {
        "reg_id": reg_id,
        "n_parts": len(parts),
        "tables": 0,
        "formulas": 0,
        "images": 0,
        "body_old": 0,
        "body_new": 0,
        "action": "",
        "reason": "",
        "note_path": "",
    }

    # 找 note
    note_path = find_note_by_reg_id(reg_id)
    if not note_path:
        result["action"] = "skipped"
        result["reason"] = "note 未找到（可能 reg_id 不在 vault）"
        return result
    result["note_path"] = str(note_path.relative_to(WIKI))

    txt = note_path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(txt)
    if not m:
        result["action"] = "skipped"
        result["reason"] = "no FM"
        return result
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        result["action"] = "skipped"
        result["reason"] = "bad FM"
        return result

    if fm.get("_ocr_upgraded") in ("mineru", "mineru_split"):
        result["action"] = "skipped"
        result["reason"] = "already upgraded"
        return result

    body = txt[m.end():]
    result["body_old"] = len(body)

    # 合并各 part
    buckets, total_full_md, part_dirs = merge_parts_buckets(parts)
    section, stats = render_split_section(buckets, part_dirs, reg_id,
                                           total_full_md, parts)
    result["tables"] = stats["tables"]
    result["formulas"] = stats["formulas"]
    result["images"] = stats["images"]
    result["body_new"] = len(body) + len(section)

    if dry_run:
        result["action"] = "dry_run_ok"
        return result

    # 写回
    fm["_ocr_upgraded"] = "mineru_split"
    fm["_mineru_split_parts"] = [
        {"part": p["part_idx"], "pages": p["actual_pages"],
         "outputs_dir": p["outputs_dir"]}
        for p in parts
    ]
    fm["_mineru_blocks"] = stats
    fm["_mineru_merged_at"] = date.today().isoformat()

    new_fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    body_clean = body.lstrip("\n")
    new_text = f"---\n{new_fm_str}---\n\n{body_clean.rstrip()}{section}\n"
    note_path.write_text(new_text, encoding="utf-8")
    result["action"] = "merged"
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reg-id", help="只合并指定 reg_id")
    args = ap.parse_args()

    if not SPLIT_MANIFEST.exists():
        print(f"[ERROR] 缺 {SPLIT_MANIFEST}，请先跑 _split_large_pdfs.py")
        return 1
    if not OVERSIZED_STATE.exists():
        print(f"[ERROR] 缺 {OVERSIZED_STATE}，请先跑 _mineru_oversized.py")
        return 1

    sm = load_split_manifest()
    state = load_oversized_state()

    ready = collect_ready_reg_ids(sm, state)

    if args.reg_id:
        ready = {k: v for k, v in ready.items() if k == args.reg_id}

    print(f"\n{'='*72}")
    print(f"  Phase 3 · 合并多分块 MinerU 结果")
    print(f"{'='*72}")
    print(f"  全 ready 的 reg_id（所有 part 都 OCR 完）: {len(ready)}")
    if not ready:
        # 显示哪些差几个 part
        all_expected = defaultdict(int)
        for r in sm.get("results", []):
            if r.get("status") in ("split_ok", "split_planned"):
                all_expected[r["reg_id"]] = len(r.get("parts", []))
        done_ids = set(state.get("done", {}).keys())
        print(f"\n  各 reg_id 进度（done / total）:")
        for reg_id, total in sorted(all_expected.items()):
            done_count = sum(
                1 for p in (sm["results"] and next(
                    (rr["parts"] for rr in sm["results"] if rr["reg_id"] == reg_id), []))
                if Path(p["file"]).stem in done_ids
            )
            mark = "✓" if done_count == total else " "
            print(f"    [{mark}] {reg_id:<25} {done_count}/{total}")
        return 0

    print(f"  目标 reg_id 清单:")
    for rid, parts in ready.items():
        total_p = sum(p["actual_pages"] for p in parts)
        print(f"    · {rid:<25}  {len(parts)} parts · 共 {total_p}p")
    print(f"{'='*72}\n")

    results = []
    for reg_id, parts in ready.items():
        print(f"▶ {reg_id}")
        r = merge_one_reg(reg_id, parts, args.dry_run)
        results.append(r)
        marker = "✓" if r["action"] in ("merged", "dry_run_ok") else "·"
        print(f"  {marker} {r['action']:<12}  "
              f"t={r['tables']} f={r['formulas']} i={r['images']}  "
              f"body {r['body_old']}→{r['body_new']}"
              + (f"  ({r['reason']})" if r["reason"] else ""))
        if r["note_path"]:
            print(f"    note: {r['note_path']}")
        print()

    print(f"{'='*72}")
    merged = sum(1 for r in results if r["action"] == "merged")
    skipped = sum(1 for r in results if r["action"] == "skipped")
    dryrun = sum(1 for r in results if r["action"] == "dry_run_ok")
    total_t = sum(r["tables"] for r in results)
    total_f = sum(r["formulas"] for r in results)
    total_i = sum(r["images"] for r in results)
    print(f"  合并: {merged} · 跳过: {skipped} · dry_run: {dryrun}")
    print(f"  累计: 表格 {total_t} · 公式 {total_f} · 图像 {total_i}")
    if args.dry_run:
        print(f"\n  [DRY-RUN] 未写入 note")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
