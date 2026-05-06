"""
_merge_upgrade.py — 把 MinerU 结果合并进 CcVault notes（增补不替换）

策略：
  - CcVault 的 body 主体（LLM 整理好的中/英文摘要）不动
  - 在 body 末尾追加新节："## 原文参考（MinerU 云解析）"
  - 节内包括：
    * 表格（从 content_list.json 的 table blocks 抽 HTML）
    * 公式（formula blocks，含 LaTeX）
    * 关键图片引用（拷贝到 01_Wiki/regulations/_mineru_assets/<reg_id>/ 并插入 Markdown 图像链接）
    * 指向完整 full.md 的链接
  - FM 加标记：_ocr_upgraded: mineru, _mineru_blocks: {tables, formulas, images}

输入：_mineru_state.json 里所有 status=done 的条目（但 FM 尚无 _ocr_upgraded 的）

用法：
  python _merge_upgrade.py --dry-run       # 预览
  python _merge_upgrade.py                  # 正式合并
  python _merge_upgrade.py --limit 5        # 限数量
  python _merge_upgrade.py --min-assets 1   # 只处理至少有 N 个表格/公式/图的

安全：
  - 每次合并前在 note 末尾记录一行 hash，合并后可以用 git 或对比恢复
  - 不删除现有内容，只追加
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade")
OUTPUTS_DIR = ROOT / "outputs"
STATE_PATH = ROOT / "_mineru_state.json"

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
ASSETS_DIR = WIKI / "_mineru_assets"

MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")


@dataclass
class MergeStats:
    tables: int = 0
    formulas: int = 0
    images: int = 0
    text_blocks: int = 0
    note_body_old_len: int = 0
    note_body_new_len: int = 0
    action: str = "skipped"
    reason: str = ""


def load_content_list(out_dir: Path) -> list[dict] | None:
    candidates = list(out_dir.glob("*_content_list.json"))
    if not candidates:
        return None
    return json.loads(candidates[0].read_text(encoding="utf-8"))


def load_full_md(out_dir: Path) -> str | None:
    p = out_dir / "full.md"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return None


def extract_blocks(content_list: list[dict]) -> dict[str, list[dict]]:
    """按 type 分组：text / table / image / equation"""
    buckets = {"text": [], "table": [], "image": [], "equation": []}
    for blk in content_list:
        t = blk.get("type", "text")
        # MinerU 的 type: text / image / table / equation
        buckets.setdefault(t, []).append(blk)
    return buckets


def copy_image(src_rel: str, src_out_dir: Path, reg_id: str) -> str | None:
    """把 MinerU 输出的 images/xxx.jpg 拷贝到 _mineru_assets/<reg_id>/，返回相对 WIKI 的路径。"""
    if not src_rel or not src_rel.strip():
        return None  # 跳过空 img_path 条目（MinerU 偶尔返回空字符串）
    src = src_out_dir / src_rel
    if not src.exists() or not src.is_file():
        return None  # 必须是真实文件，不能是目录
    safe_reg_id = re.sub(r"[^A-Za-z0-9._\- ]", "_", reg_id or "unknown")
    dest_dir = ASSETS_DIR / safe_reg_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if not dest.exists():
        shutil.copy2(src, dest)
    # 返回 WIKI-relative path 用于 Markdown 引用
    return f"_mineru_assets/{safe_reg_id}/{src.name}"


def render_mineru_section(buckets: dict[str, list[dict]],
                          out_dir: Path,
                          reg_id: str,
                          full_md_chars: int,
                          *,
                          max_tables: int = 10,
                          max_formulas: int = 20,
                          max_images: int = 8) -> tuple[str, MergeStats]:
    """把 MinerU 抽到的结构化内容渲染成 Markdown 片段。"""
    stats = MergeStats()
    lines: list[str] = []

    today = date.today().isoformat()
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## 原文参考（MinerU 云解析 · {today}）")
    lines.append("")
    lines.append(f"> 本节由 MinerU 重新 OCR 原 PDF 所得，共解析到：")
    lines.append(f"> - 表格 {len(buckets.get('table', []))} 个")
    lines.append(f"> - 公式 {len(buckets.get('equation', []))} 个")
    lines.append(f"> - 图像 {len(buckets.get('image', []))} 个")
    lines.append(f"> - 全文 Markdown {full_md_chars:,} 字符（见 `outputs/<hash>/full.md`）")
    lines.append("")

    # 表格
    tables = buckets.get("table", [])[:max_tables]
    if tables:
        lines.append(f"### 表格（取前 {len(tables)} 个）")
        lines.append("")
        for i, tb in enumerate(tables, 1):
            cap = tb.get("table_caption") or []
            cap_str = " / ".join(cap) if isinstance(cap, list) else str(cap)
            page = tb.get("page_idx", "?")
            lines.append(f"#### 表 {i} (page {page})")
            if cap_str.strip():
                lines.append(f"**{cap_str}**")
                lines.append("")
            html = tb.get("table_body", "")
            if html:
                # 把 MinerU 的 HTML table 直接粘进 Markdown（Obsidian 支持）
                lines.append(html.strip())
                lines.append("")
                stats.tables += 1
            # 若 table_body 为空（MinerU 未能重建 HTML），不计入 FM stats
    # 公式
    eqs = buckets.get("equation", [])[:max_formulas]
    if eqs:
        lines.append(f"### 公式（取前 {len(eqs)} 个）")
        lines.append("")
        for i, eq in enumerate(eqs, 1):
            latex = eq.get("text", "").strip()
            page = eq.get("page_idx", "?")
            if latex:
                # MinerU 的 equation.text 通常是 $$ ... $$ 包裹的
                if not latex.startswith("$"):
                    latex = f"$$\n{latex}\n$$"
                lines.append(f"**公式 {i}** (page {page}):")
                lines.append("")
                lines.append(latex)
                lines.append("")
                stats.formulas += 1
    # 图像
    imgs = buckets.get("image", [])[:max_images]
    copied_imgs = []
    for img in imgs:
        img_path = img.get("img_path", "")
        caption = img.get("image_caption") or []
        cap_str = " / ".join(caption) if isinstance(caption, list) else str(caption)
        page = img.get("page_idx", "?")
        wiki_rel = copy_image(img_path, out_dir, reg_id)
        if wiki_rel:
            copied_imgs.append((wiki_rel, cap_str, page))
            stats.images += 1
    if copied_imgs:
        lines.append(f"### 图像（取前 {len(copied_imgs)} 张）")
        lines.append("")
        for wiki_rel, cap, page in copied_imgs:
            alt = cap if cap.strip() else f"图 page {page}"
            lines.append(f"![{alt}](../{wiki_rel})  ")
            if cap.strip():
                lines.append(f"*{cap}* (page {page})")
            lines.append("")

    return "\n".join(lines), stats


def merge_one(note_path: Path, out_dir: Path, content_hash: str,
              reg_id: str, *, dry_run: bool, min_assets: int) -> MergeStats:
    txt = note_path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(txt)
    if not m:
        return MergeStats(action="skipped", reason="no FM")
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return MergeStats(action="skipped", reason="bad FM")

    # 已升级过 → 跳
    if fm.get("_ocr_upgraded") == "mineru":
        return MergeStats(action="skipped", reason="already upgraded")

    body = txt[m.end():]

    content_list = load_content_list(out_dir)
    if not content_list:
        return MergeStats(action="skipped", reason="no content_list.json")

    buckets = extract_blocks(content_list)
    full_md = load_full_md(out_dir) or ""
    total_assets = (len(buckets.get("table", []))
                    + len(buckets.get("equation", []))
                    + len(buckets.get("image", [])))

    if total_assets < min_assets:
        return MergeStats(
            action="skipped",
            reason=f"assets={total_assets} < min_assets={min_assets}",
            tables=len(buckets.get("table", [])),
            formulas=len(buckets.get("equation", [])),
            images=len(buckets.get("image", [])),
            note_body_old_len=len(body),
        )

    section, stats = render_mineru_section(buckets, out_dir, reg_id or "unknown",
                                           full_md_chars=len(full_md))
    stats.note_body_old_len = len(body)
    stats.note_body_new_len = len(body) + len(section)

    if dry_run:
        stats.action = "dry_run_ok"
        return stats

    # 合并回 FM + body
    fm["_ocr_upgraded"] = "mineru"
    fm["_mineru_content_hash"] = content_hash
    fm["_mineru_outputs_dir"] = f"outputs/{content_hash}"
    fm["_mineru_blocks"] = {
        "tables": stats.tables,
        "formulas": stats.formulas,
        "images": stats.images,
    }
    fm["_mineru_merged_at"] = date.today().isoformat()

    new_fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    # 关键：closing --- 后必须有空行，否则下次 FM_RE 解析会把 body 吸进 FM
    body_clean = body.lstrip("\n")
    new_text = f"---\n{new_fm_str}---\n\n{body_clean.rstrip()}{section}\n"
    note_path.write_text(new_text, encoding="utf-8")
    stats.action = "merged"
    return stats


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"done": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def build_hash_to_note() -> dict[str, tuple[Path, str, str]]:
    """content_hash → (note_path, reg_id, source_pdf_rel)。"""
    # 先用 manifest 拿 hash → source_pdf 路径
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = manifest["records"]
    hash_to_pdf: dict[str, str] = {}
    hash_to_reg: dict[str, str] = {}
    for h, r in records.items():
        p = r.get("path")
        if p:
            hash_to_pdf[h] = p.replace("\\", "/")
            hash_to_reg[h] = r.get("reg_id") or ""

    # 再扫 notes 按 source_pdf/source_file 找 hash → note 的反向
    result: dict[str, tuple[Path, str, str]] = {}
    notes_by_pdf: dict[str, Path] = {}
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
        sp = fm.get("source_pdf") or fm.get("source_file")
        if sp:
            notes_by_pdf[str(sp).replace("\\", "/")] = p

    for h, pdf_rel in hash_to_pdf.items():
        note = notes_by_pdf.get(pdf_rel)
        if note:
            result[h] = (note, hash_to_reg.get(h, ""), pdf_rel)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--min-assets", type=int, default=1,
                    help="至少需要 N 个 table/formula/image 才合并（默认 1）")
    args = ap.parse_args()

    state = load_state()
    done = state.get("done", {})
    print(f"MinerU 已完成 PDF: {len(done)}")

    hash_to_note = build_hash_to_note()
    print(f"建立 hash→note 映射: {len(hash_to_note)} 条")

    candidates = []
    for chash, info in done.items():
        if info.get("status") != "done":
            continue
        out_dir_rel = info.get("outputs_dir", f"outputs/{chash}")
        out_dir = ROOT / out_dir_rel
        if not out_dir.exists():
            continue
        pair = hash_to_note.get(chash)
        if not pair:
            continue
        note_path, reg_id, pdf_rel = pair
        candidates.append((chash, out_dir, note_path, reg_id))

    print(f"可合并候选: {len(candidates)}")
    if args.limit:
        candidates = candidates[: args.limit]

    print("-" * 70)

    agg = {"merged": 0, "skipped": 0, "dry_run_ok": 0,
           "tables": 0, "formulas": 0, "images": 0}
    for chash, out_dir, note_path, reg_id in candidates:
        stats = merge_one(note_path, out_dir, chash, reg_id,
                          dry_run=args.dry_run, min_assets=args.min_assets)
        agg[stats.action] = agg.get(stats.action, 0) + 1
        agg["tables"] += stats.tables
        agg["formulas"] += stats.formulas
        agg["images"] += stats.images
        marker = "✓" if stats.action in ("merged", "dry_run_ok") else "·"
        print(f"  {marker} {reg_id:<28} {stats.action:<12} "
              f"t={stats.tables} f={stats.formulas} i={stats.images} "
              f"body {stats.note_body_old_len}→{stats.note_body_new_len}"
              + (f"  ({stats.reason})" if stats.reason else ""))

    print("-" * 70)
    print(f"合并: {agg.get('merged',0)}  |  跳过: {agg.get('skipped',0)}  "
          f"|  dry_run: {agg.get('dry_run_ok',0)}")
    print(f"累计新增: 表格 {agg['tables']} · 公式 {agg['formulas']} · 图像 {agg['images']}")
    if args.dry_run:
        print("\n[DRY RUN] 未修改任何 note")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
