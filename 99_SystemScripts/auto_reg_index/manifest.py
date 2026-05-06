"""
Manifest · 文件清单 + 状态机

每份源文件在 pipeline 中的生命周期：
    pending → ocr_done → extracted → verified|needs_review → written
              → equivalence_linked → topic_summarized → graph_included

支持断点续传：读取 manifest.json，跳过已完成状态的文件。
"""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    import xxhash
    _use_xxhash = True
except ImportError:
    _use_xxhash = False


ROOT = Path(__file__).parent
MANIFEST_PATH = ROOT / "manifest.json"
RAW_ROOT = Path(os.getenv("RAW_SOURCE_DIR", "D:/CcVault/00_Raw/标准库"))

STATES = [
    "pending",
    "ocr_done",
    "extracted",
    "verified",
    "needs_review",
    "written",
    "equivalence_linked",
    "topic_summarized",
    "graph_included",
    "failed",
    "skipped",
]


# =============================================================
# Data class
# =============================================================
@dataclass
class FileRecord:
    """单份源文件的 manifest 记录"""
    path: str                       # 相对 RAW_ROOT 的路径
    size_bytes: int
    content_hash: str               # xxhash 或 sha1 前 16 字符
    state: str = "pending"
    reg_id: Optional[str] = None    # 从文件名推断或抽取后填
    region: Optional[str] = None    # cn/ece/eu/us/...
    duplicate_of: Optional[str] = None  # 若是重复副本，指向原始文件 hash
    last_updated: str = ""
    stage_history: list = field(default_factory=list)
    error: Optional[str] = None

    def advance_to(self, new_state: str, note: str = ""):
        """状态前进"""
        if new_state not in STATES:
            raise ValueError(f"Invalid state: {new_state}")
        self.stage_history.append({
            "from": self.state,
            "to": new_state,
            "ts": datetime.now(timezone.utc).isoformat(),
            "note": note,
        })
        self.state = new_state
        self.last_updated = datetime.now(timezone.utc).isoformat()
        self.error = None

    def mark_failed(self, error: str):
        """标为失败"""
        self.state = "failed"
        self.error = error
        self.last_updated = datetime.now(timezone.utc).isoformat()


# =============================================================
# Manifest
# =============================================================
class Manifest:
    def __init__(self, records: dict[str, FileRecord]):
        self.records: dict[str, FileRecord] = records

    # ---------- Load / Save ----------
    @classmethod
    def load_or_create(cls) -> "Manifest":
        if MANIFEST_PATH.exists():
            data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            records = {
                h: FileRecord(**rec)
                for h, rec in data.get("records", {}).items()
            }
            return cls(records)
        return cls({})

    def save(self):
        data = {
            "version": "0.1",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "records": {h: asdict(rec) for h, rec in self.records.items()},
        }
        MANIFEST_PATH.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # ---------- Scan ----------
    def scan_raw_dir(self, raw_root: Path = RAW_ROOT) -> int:
        """扫描源目录，新文件加入 manifest。返回新增数。"""
        added = 0
        for path in raw_root.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx"}:
                continue
            rel = path.relative_to(raw_root).as_posix()
            content_hash = self._hash_file(path)
            if content_hash in self.records:
                continue
            self.records[content_hash] = FileRecord(
                path=rel,
                size_bytes=path.stat().st_size,
                content_hash=content_hash,
                last_updated=datetime.now(timezone.utc).isoformat(),
            )
            added += 1
        self._detect_duplicates()
        return added

    def _detect_duplicates(self):
        """基于文件名相似度标记疑似副本"""
        from collections import defaultdict
        name_groups = defaultdict(list)
        for h, rec in self.records.items():
            # 去除 (1)(2)(3) 副本编号后的基础名
            base = Path(rec.path).stem
            for suffix in ["(1)", "(2)", "(3)", "(4)", "(5)"]:
                base = base.replace(suffix, "")
            base = base.strip()
            name_groups[base].append(h)
        for base, hashes in name_groups.items():
            if len(hashes) > 1:
                # 第一个作为 canonical，其余标为 duplicate_of
                canonical = hashes[0]
                for h in hashes[1:]:
                    self.records[h].duplicate_of = canonical

    # ---------- Hash ----------
    @staticmethod
    def _hash_file(path: Path, chunk_size: int = 65536) -> str:
        """内容 hash。优先 xxhash（快 10 倍），否则 sha1。"""
        if _use_xxhash:
            h = xxhash.xxh64()
        else:
            h = hashlib.sha1()
        with path.open("rb") as f:
            while chunk := f.read(chunk_size):
                h.update(chunk)
        return h.hexdigest()[:16]

    # ---------- Query ----------
    def summary(self) -> dict[str, int]:
        """按 state 统计"""
        c = Counter(rec.state for rec in self.records.values())
        # 保持 STATES 顺序
        return {s: c.get(s, 0) for s in STATES}

    def find_files_for_regulation(self, reg_id_prefix: str) -> list[FileRecord]:
        """按法规编号匹配。支持多种命名格式：
          - 'GB 4785'   → 'GB 4785-2007_xxx.pdf' / '4785-1998-gb-e-300_...pdf' / 'gb4785-2019.pdf'
          - 'ECE R48'   → 'R048r12am10e.pdf'（ECE 零填充 3 位）
          - 'ECE R 48'  → 同上
          - 'FMVSS 208' → 'fmvss208-...pdf' / 'FMVSS_208.pdf'
          - 'UN R94'    → 'R094...pdf'
        规则：
          1. 拆分 reg_id 为 letter_tokens + digit_tokens
          2. 所有字母 token 必须出现在**完整路径**（不区分大小写）
          3. 主数字（最后一个数字 token）或其 3/4 位零填充形式必须出现在路径
        """
        import re
        s = reg_id_prefix.strip().lower()
        letter_tokens = [t for t in re.findall(r"[a-z]+", s) if t]
        digit_tokens = re.findall(r"\d+", s)
        if not digit_tokens:
            # 纯字母：fallback 用 substring in filename
            prefix = s.replace(" ", "")
            return sorted(
                [rec for rec in self.records.values()
                 if not rec.duplicate_of
                 and prefix in Path(rec.path).name.lower().replace(" ", "")],
                key=lambda r: r.path,
            )
        main_num = digit_tokens[-1]
        # 候选数字写法：3/4 位零填充；若本身>=3位则也包含原样。
        # 仅用零填充避免 "48" 误匹配 "R148"（"48" 是 "148" 子串）
        num_patterns: set[str] = set()
        if len(main_num) >= 3:
            num_patterns.add(main_num)
        for width in (3, 4):
            if len(main_num) <= width:
                num_patterns.add(main_num.zfill(width))

        matches: list[FileRecord] = []
        for rec in self.records.values():
            if rec.duplicate_of:
                continue
            path_lower = rec.path.lower()
            # 所有字母 token 都必须出现
            if letter_tokens and not all(lt in path_lower for lt in letter_tokens):
                continue
            # 数字（任一 padding）必须出现
            if not any(p in path_lower for p in num_patterns):
                continue
            matches.append(rec)
        return sorted(matches, key=lambda r: r.path)

    def files_in_state(self, state: str) -> list[FileRecord]:
        return [rec for rec in self.records.values() if rec.state == state]

    def __len__(self) -> int:
        return len(self.records)
