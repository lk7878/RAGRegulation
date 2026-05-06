"""
Layer 2: 百度云 OCR（扫描件）

API 文档: https://cloud.baidu.com/doc/OCR/s/Ok3h7xxva
定价: 高精度版 ¥0.007/页（每日前 1000 页免费）

实现：
  1. 用 pypdfium2 把 PDF 每页渲染为 PNG（~200 DPI）
  2. 调 AipOcr.accurate_basic(image_bytes)
  3. 把 words_result 汇总为 markdown，每页一个 `## Page N` 分隔
  4. 有 QPS 限制时 sleep 重试
"""
from __future__ import annotations

import io
import logging
import os
import time
from pathlib import Path

from .router import OCRResult, OCR_LAYER

logger = logging.getLogger(__name__)

# 百度 AipOcr accurate_basic 默认 QPS=2（免费/个人版），高级版可达 10
_DEFAULT_QPS = float(os.getenv("BAIDU_OCR_QPS", "2"))
_MIN_INTERVAL = 1.0 / _DEFAULT_QPS
# 单次请求最大重试次数
_MAX_RETRIES = 3
# 渲染 DPI（越高质量越好，但文件越大）
_RENDER_SCALE = 2.0  # ~144 DPI；accurate_basic 单图上限 4MB


def _render_pdf_pages(pdf_path: Path) -> list[bytes]:
    """用 pypdfium2 把 PDF 每页渲染为 PNG bytes。"""
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf_path))
    pages: list[bytes] = []
    try:
        for i, page in enumerate(doc):
            try:
                bitmap = page.render(scale=_RENDER_SCALE)
                pil = bitmap.to_pil()
                # 转为 RGB（去掉 alpha），减小文件
                if pil.mode != "RGB":
                    pil = pil.convert("RGB")
                buf = io.BytesIO()
                # JPEG 质量 85 → 大约单页 300-500KB
                pil.save(buf, format="JPEG", quality=85, optimize=True)
                pages.append(buf.getvalue())
            finally:
                page.close()
    finally:
        doc.close()
    return pages


def _call_baidu_accurate(client, image_bytes: bytes) -> tuple[bool, list[str], str]:
    """调一次 basicAccurate，带重试。返回 (success, words_list, error_msg)

    baidu-aip 4.x 方法名为 camelCase（basicAccurate = 高精度基础版）。
    ¥0.007/页，前 1000 页/日免费。
    """
    last_err = ""
    for attempt in range(_MAX_RETRIES):
        try:
            resp = client.basicAccurate(image_bytes)
            # 百度错误返回 {"error_code": N, "error_msg": "..."}
            if "error_code" in resp:
                code = resp["error_code"]
                msg = resp.get("error_msg", "")
                # QPS 超限 → sleep 重试
                if code in (18, 17):  # qps limit / daily limit
                    time.sleep(1.0 + attempt)
                    last_err = f"rate_limited({code}): {msg}"
                    continue
                return False, [], f"baidu_err({code}): {msg}"
            words = [w.get("words", "") for w in resp.get("words_result", [])]
            return True, words, ""
        except Exception as e:
            last_err = f"exception: {e}"
            time.sleep(0.5 * (attempt + 1))
    return False, [], last_err or "unknown"


def extract(pdf_path: Path) -> OCRResult:
    """调百度云 OCR 的高精度接口识别扫描件。"""
    app_id = os.getenv("BAIDU_OCR_APP_ID")
    api_key = os.getenv("BAIDU_OCR_API_KEY")
    secret_key = os.getenv("BAIDU_OCR_SECRET_KEY")

    if not (app_id and api_key and secret_key):
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.BAIDU,
            markdown="",
            warnings=["Baidu OCR keys not configured in .env (BAIDU_OCR_APP_ID/API_KEY/SECRET_KEY)"],
        )

    try:
        from aip import AipOcr
    except ImportError:
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.BAIDU,
            markdown="",
            warnings=["baidu-aip not installed; run `pip install baidu-aip`"],
        )

    # 渲染 PDF
    try:
        page_images = _render_pdf_pages(pdf_path)
    except Exception as e:
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.BAIDU,
            markdown="",
            warnings=[f"PDF render failed: {e}"],
        )

    if not page_images:
        return OCRResult(
            success=False,
            layer_used=OCR_LAYER.BAIDU,
            markdown="",
            warnings=["PDF rendered 0 pages"],
        )

    client = AipOcr(app_id, api_key, secret_key)
    # 可选：设置网络超时
    client.setConnectionTimeoutInMillis(8000)
    client.setSocketTimeoutInMillis(30000)

    markdown_parts: list[str] = []
    warnings: list[str] = []
    succeeded_pages = 0
    total_pages = len(page_images)

    for idx, img_bytes in enumerate(page_images, start=1):
        # 单图 4MB 限制；若超限则降级压缩
        if len(img_bytes) > 4 * 1024 * 1024:
            try:
                from PIL import Image
                pil = Image.open(io.BytesIO(img_bytes))
                buf = io.BytesIO()
                pil.save(buf, format="JPEG", quality=70, optimize=True)
                img_bytes = buf.getvalue()
            except Exception:
                warnings.append(f"page {idx}: exceeds 4MB, skipped")
                markdown_parts.append(f"## Page {idx}\n\n[OCR_SKIPPED: image too large]")
                continue

        t0 = time.monotonic()
        ok, words, err = _call_baidu_accurate(client, img_bytes)
        if ok:
            markdown_parts.append(f"## Page {idx}\n\n" + "\n".join(words))
            succeeded_pages += 1
        else:
            warnings.append(f"page {idx}: {err}")
            markdown_parts.append(f"## Page {idx}\n\n[OCR_ERROR: {err}]")

        # QPS 节流
        elapsed = time.monotonic() - t0
        if elapsed < _MIN_INTERVAL:
            time.sleep(_MIN_INTERVAL - elapsed)

    markdown = "\n\n".join(markdown_parts)
    # 成本估算：累计成功识别的页数 × ¥0.007
    cost_cny = succeeded_pages * 0.007

    return OCRResult(
        success=succeeded_pages > 0,
        layer_used=OCR_LAYER.BAIDU,
        markdown=markdown,
        page_count=total_pages,
        warnings=warnings,
        cost_cny=cost_cny,
    )
