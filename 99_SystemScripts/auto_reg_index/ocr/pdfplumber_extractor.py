"""
Layer 1: pdfplumber 原生文本提取

适用：电子 PDF（大多数）
不适用：扫描件（无 text 层）
"""
from __future__ import annotations

from pathlib import Path

from .router import OCRResult, OCR_LAYER


def extract(
    pdf_path: Path,
    *,
    min_text_per_page_chars: int = 50,
    skip_tables_above_pages: int = 150,
) -> OCRResult:
    """
    用 pdfplumber 提取每页文本，组成 markdown。

    参数：
      skip_tables_above_pages: 页数超过此值时跳过表格抽取（表格抽取很慢）

    判定失败（应 fallback 到百度云）：
    - 超过 50% 的页面文本 < min_text_per_page_chars
    - 或总文本 < 200 chars
    """
    try:
        import pdfplumber
    except ImportError:
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.PDFPLUMBER,
            markdown="",
            warnings=["pdfplumber not installed"],
        )

    try:
        with pdfplumber.open(pdf_path) as pdf:
            page_count = len(pdf.pages)
            extract_tables_enabled = page_count <= skip_tables_above_pages
            parts: list[str] = []
            sparse_pages = 0
            total_chars = 0
            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text() or ""
                text = text.strip()
                if len(text) < min_text_per_page_chars:
                    sparse_pages += 1
                total_chars += len(text)

                # 表格抽取（短文档才做，避免 500+ 页文档卡死）
                tables_md = ""
                if extract_tables_enabled:
                    try:
                        tables = page.extract_tables()
                        for t_idx, table in enumerate(tables or [], 1):
                            tables_md += f"\n\n### Page {i} Table {t_idx}\n\n"
                            tables_md += _table_to_markdown(table)
                    except Exception:
                        pass

                parts.append(f"## Page {i}\n\n{text}{tables_md}")

            sparse_ratio = sparse_pages / max(page_count, 1)

            # 判定扫描件：多数页面文本稀疏
            if sparse_ratio > 0.5 or total_chars < 200:
                return OCRResult(
                    success=False,
                    layer_used=OCR_LAYER.PDFPLUMBER,
                    markdown="",
                    page_count=page_count,
                    warnings=[
                        f"Likely scanned PDF: {sparse_pages}/{page_count} "
                        f"pages have <{min_text_per_page_chars} chars"
                    ],
                )

            warnings: list[str] = []
            if not extract_tables_enabled:
                warnings.append(f"skipped table extraction (page_count={page_count} > {skip_tables_above_pages})")
            markdown = "\n\n".join(parts)
            return OCRResult(
                success=True,
                layer_used=OCR_LAYER.PDFPLUMBER,
                markdown=markdown,
                page_count=page_count,
                warnings=warnings,
            )

    except Exception as e:
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.PDFPLUMBER,
            markdown="",
            warnings=[f"pdfplumber error: {e}"],
        )


def _table_to_markdown(table: list[list[str | None]]) -> str:
    """List-of-lists 转 Markdown 表格"""
    if not table or not table[0]:
        return ""
    # 清洗 None
    def clean(x):
        return (x or "").replace("|", "\\|").replace("\n", " ").strip()

    header = [clean(c) for c in table[0]]
    body = [[clean(c) for c in row] for row in table[1:]]

    lines = []
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    for row in body:
        # 对齐列数
        row = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(row[: len(header)]) + " |")
    return "\n".join(lines)
