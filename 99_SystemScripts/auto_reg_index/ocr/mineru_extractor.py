"""
Layer 3: MinerU CPU 模式（复杂表格）

https://github.com/opendatalab/MinerU

Day 1 只写骨架。Day 2 遇到复杂表格法规时再完善。
"""
from __future__ import annotations

from pathlib import Path

from .router import OCRResult, OCR_LAYER


def extract(pdf_path: Path) -> OCRResult:
    """TODO(Day 2): 调用 MinerU (magic-pdf) 命令行或 Python API"""
    try:
        import magic_pdf  # noqa: F401
    except ImportError:
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.MINERU,
            markdown="",
            warnings=["MinerU (magic-pdf) not installed. pip install magic-pdf[full]"],
        )

    # TODO(Day 2):
    # 1. magic_pdf 的 Python API 调用
    # 2. 输出 markdown
    # 3. CPU 模式慢但免费
    return OCRResult(
        success=False,
        layer_used=OCR_LAYER.MINERU,
        markdown="",
        warnings=["TODO(Day 2): implement MinerU"],
    )
