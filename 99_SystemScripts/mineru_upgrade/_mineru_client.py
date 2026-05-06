"""
_mineru_client.py — MinerU 云 API 封装（批量上传 / 轮询 / 下载）

API 文档：https://mineru.net/apiManage
核心流程：
  1. POST /file-urls/batch  请求预签上传 URL（batch 可包含多文件）
  2. PUT 上传到预签 URL（并行）
  3. GET /extract-results/batch/{batch_id}  轮询直到 state=done 或 failed
  4. GET result.full_zip_url  下载 ZIP，解压到本地
"""
from __future__ import annotations

import io
import json
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx


@dataclass
class FileUploadSpec:
    file_path: Path
    data_id: str          # 自定义 id，用于回溯（用 content_hash）
    is_ocr: bool = True   # 需要 OCR


@dataclass
class FileResult:
    data_id: str
    file_name: str
    state: str            # done / failed / running / pending
    zip_url: str | None
    pages: int | None
    err_msg: str | None


class MineruClient:
    def __init__(self, token: str, api_base: str = "https://mineru.net/api/v4",
                 timeout: float = 120.0):
        self.token = token
        self.base = api_base.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self._client.close()

    # ----------------------------------------------------------------
    # Step 1: batch upload URL
    # ----------------------------------------------------------------
    def request_upload_urls(self, specs: list[FileUploadSpec],
                            enable_formula: bool = True,
                            enable_table: bool = True,
                            language: str = "ch") -> tuple[str, list[str]]:
        """
        returns (batch_id, list_of_upload_urls_aligned_to_specs)
        """
        files_payload = [
            {
                "name": s.file_path.name,
                "data_id": s.data_id,
                "is_ocr": s.is_ocr,
            }
            for s in specs
        ]
        body = {
            "files": files_payload,
            "enable_formula": enable_formula,
            "enable_table": enable_table,
            "language": language,
        }
        # 对 SSL EOF / 连接重置做 3 次重试 + 指数退避（10s / 30s / 60s）
        # 原因：MinerU 服务器拥塞时会持续返回 SSL EOF，快速失败会让 daily_batch
        # 几分钟内空跑完 85 批，watchdog 拉起后又继续空跑，浪费资源。
        last_err: Exception | None = None
        for attempt in range(3):
            try:
                r = self._client.post(f"{self.base}/file-urls/batch",
                                      headers=self.headers, json=body)
                r.raise_for_status()
                j = r.json()
                if j.get("code") != 0:
                    raise RuntimeError(f"MinerU upload url failed: {j.get('msg')} "
                                       f"(trace_id={j.get('trace_id')})")
                return j["data"]["batch_id"], j["data"]["file_urls"]
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteError,
                    httpx.RemoteProtocolError, httpx.ConnectTimeout,
                    httpx.PoolTimeout, OSError) as e:
                last_err = e
                if attempt < 2:
                    backoff = [10, 30, 60][attempt]
                    time.sleep(backoff)
        raise RuntimeError(
            f"request_upload_urls 失败（3 次重试后）: "
            f"{type(last_err).__name__}: {str(last_err)[:150]}")

    # ----------------------------------------------------------------
    # Step 2: upload files (parallel recommended outside)
    # ----------------------------------------------------------------
    def upload_one(self, file_path: Path, upload_url: str,
                   retries: int = 3) -> None:
        """
        上传单个文件到预签 URL，失败重试 N 次（指数退避 2s / 4s / 8s）。
        面对 MinerU 服务器的 SSL EOF / 连接重置，能显著提升成功率。
        """
        last_err: str | None = None
        content = file_path.read_bytes()  # 只读一次，避免重试时重读
        for attempt in range(retries):
            try:
                # 注意：PUT 不带 Authorization（预签 URL 自带授权）
                r = httpx.put(upload_url, content=content, timeout=120.0)
                if r.status_code in (200, 201):
                    return
                last_err = f"HTTP {r.status_code}: {r.text[:120]}"
            except (httpx.ConnectError, httpx.WriteError, httpx.ReadTimeout,
                    httpx.RemoteProtocolError, httpx.ConnectTimeout,
                    OSError) as e:
                last_err = f"{type(e).__name__}: {str(e)[:120]}"
            # 重试前退避
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
        raise RuntimeError(
            f"Upload {file_path.name} failed after {retries} retries: {last_err}")

    # ----------------------------------------------------------------
    # Step 3: poll batch results
    # ----------------------------------------------------------------
    def poll_batch(self, batch_id: str,
                   poll_interval: float = 10.0,
                   max_minutes: float = 15.0,
                   progress_cb=None) -> list[FileResult]:
        """
        轮询直到所有文件 state 终态 (done / failed) 或超时。
        progress_cb(elapsed, results) 每轮回调一次。
        """
        deadline = time.time() + max_minutes * 60
        last_results: list[FileResult] = []  # 保底：SSL/网络连续崩时仍能返回快照
        while True:
            elapsed = (deadline - (deadline - time.time()))  # 时间戳
            # 网络层故障自愈：SSL/ConnectError/ReadTimeout 等不终止 polling
            try:
                r = self._client.get(
                    f"{self.base}/extract-results/batch/{batch_id}",
                    headers=self.headers,
                )
                r.raise_for_status()
            except (httpx.HTTPStatusError, httpx.ConnectError,
                    httpx.ReadTimeout, httpx.WriteError,
                    httpx.RemoteProtocolError, OSError) as e:
                # 偶发 502 / 504 / SSL EOF / 连接重置，退避重试
                time.sleep(poll_interval)
                if time.time() > deadline:
                    # 超时则返回已有快照，由上层处理未完成文件
                    return last_results
                continue
            j = r.json()
            if j.get("code") != 0:
                raise RuntimeError(f"Poll failed: {j.get('msg')}")
            raw_results = j.get("data", {}).get("extract_result", []) or []
            results = [
                FileResult(
                    data_id=x.get("data_id", ""),
                    file_name=x.get("file_name", ""),
                    state=x.get("state", "pending"),
                    zip_url=x.get("full_zip_url"),
                    pages=(x.get("extract_progress") or {}).get("total_pages"),
                    err_msg=x.get("err_msg"),
                )
                for x in raw_results
            ]
            last_results = results  # 成功拉到一轮快照就更新保底
            if progress_cb:
                progress_cb(int(time.time() - (deadline - max_minutes * 60)),
                            results)
            if results and all(fr.state in ("done", "failed") for fr in results):
                return results
            if time.time() > deadline:
                return results  # 返回最后快照，上层决定怎么处理未完成的
            time.sleep(poll_interval)

    # ----------------------------------------------------------------
    # Step 4: download + unzip
    # ----------------------------------------------------------------
    def download_and_unzip(self, result: FileResult, out_dir: Path) -> Path:
        """解压到 out_dir/{data_id}/, 返回解压目录路径。"""
        if not result.zip_url:
            raise RuntimeError(f"{result.file_name}: no zip_url")
        target = out_dir / result.data_id
        target.mkdir(parents=True, exist_ok=True)
        r = httpx.get(result.zip_url, timeout=300.0)
        r.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
            zf.extractall(target)
        return target


def load_env(env_path: Path) -> dict[str, str]:
    """简单 .env 解析（KEY=VALUE，不支持多行 / 注释行）。"""
    cfg: dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        cfg[k.strip()] = v.strip().strip('"').strip("'")
    return cfg
