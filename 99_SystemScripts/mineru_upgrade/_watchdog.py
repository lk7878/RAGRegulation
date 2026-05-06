"""
Watchdog for _daily_batch.py.

职责：
    1. 启动 _daily_batch.py 作为子进程
    2. 子进程一旦退出（正常或异常），自动重启
    3. 频繁崩溃时指数退避，避免烧 API 预算
    4. 独立 watchdog.log 记录重启事件
    5. 接收 Ctrl+C 平滑退出（不重启）

用法（强烈建议 detached 启动，不要占当前终端）：
    Start-Process -WindowStyle Hidden -FilePath "D:\CcVault\99_SystemScripts\auto_reg_index\.venv\Scripts\pythonw.exe" `
        -ArgumentList "D:\CcVault\99_SystemScripts\mineru_upgrade\_watchdog.py"

停止：
    Get-WmiObject Win32_Process -Filter "Name='python.exe' OR Name='pythonw.exe'" |
        Where-Object { $_.CommandLine -like "*_watchdog*" -or $_.CommandLine -like "*_daily_batch*" } |
        ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

PY = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.venv\Scripts\python.exe")
SCRIPT = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_daily_batch.py")
ARGS = [
    "--target-pages", "80000",
    "--max-priority", "6",
    "--batch-size", "10",
    "--max-minutes", "10",
    "--max-size-mb", "10",
]
LOG_DIR = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\logs")
WATCHDOG_LOG = LOG_DIR / "watchdog.log"


def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    try:
        print(line, flush=True)
    except Exception:
        pass
    WATCHDOG_LOG.parent.mkdir(parents=True, exist_ok=True)
    with WATCHDOG_LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> int:
    log("=" * 60)
    log("=== Watchdog 启动 ===")
    log(f"PY={PY}")
    log(f"SCRIPT={SCRIPT}")
    log(f"ARGS={' '.join(ARGS)}")

    crash_count = 0
    last_crash_time = 0.0
    CRASH_WINDOW = 300  # 5 min 内频繁崩溃视为连环崩
    MAX_CONSECUTIVE_CRASHES = 5

    while True:
        start_ts = time.time()
        log(f"▶ 启动 daily_batch（累计重启 {crash_count} 次）")
        try:
            completed = subprocess.run(
                [str(PY), str(SCRIPT), *ARGS],
                cwd=str(SCRIPT.parent),
            )
            elapsed = int(time.time() - start_ts)
            log(f"⏹ daily_batch 退出 code={completed.returncode}，运行 {elapsed}s")
        except KeyboardInterrupt:
            log("⚠ KeyboardInterrupt，watchdog 退出")
            return 0
        except Exception as e:
            elapsed = int(time.time() - start_ts)
            log(f"✗ 异常: {type(e).__name__}: {e}（运行 {elapsed}s）")

        # 连环崩溃检测
        now = time.time()
        if now - last_crash_time < CRASH_WINDOW:
            crash_count += 1
        else:
            crash_count = 1
        last_crash_time = now

        if crash_count >= MAX_CONSECUTIVE_CRASHES:
            log(f"! 连续崩溃 {crash_count} 次，退避 10 分钟")
            time.sleep(600)
            crash_count = 0
        else:
            # 正常重启：等 30 秒再起（给网络 / state 落盘的余地）
            log("↻ 30 秒后重启")
            time.sleep(30)


if __name__ == "__main__":
    sys.exit(main())
