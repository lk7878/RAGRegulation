"""
分析 _mineru_state.json 里的失败样本，按错误类型/日期/PDF 大小分组，输出报告。
用途：判断失败原因是服务器拥塞还是 PDF 本身问题，为重跑策略提供依据。
"""
from __future__ import annotations
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

STATE_PATH = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_state.json")


def short_err(err: str) -> str:
    """把长 err 归成短分类。"""
    if not err:
        return "(空)"
    if "SSL" in err or "EOF" in err:
        return "SSL_EOF"
    if "ConnectError" in err or "ConnectTimeout" in err:
        return "connect_error"
    if "last state: pending" in err:
        return "mineru_pending_timeout"
    if "last state: running" in err:
        return "mineru_running_timeout"
    if "last state: failed" in err:
        return "mineru_parse_failed"
    if "last state: converting" in err:
        return "mineru_converting_timeout"
    if "after 3 retries" in err:
        return "upload_3_retries_exhausted"
    return err[:40]


def main():
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    failed = state.get("failed", {})

    print(f"总失败数: {len(failed)}")
    print()

    # 1) 按日期分组
    by_date = Counter(info.get("date", "?") for info in failed.values())
    print("— 按日期 —")
    for d, n in sorted(by_date.items()):
        print(f"  {d}  {n}")
    print()

    # 2) 按 status 分组
    by_status = Counter(info.get("status", "?") for info in failed.values())
    print("— 按顶层 status —")
    for s, n in sorted(by_status.items(), key=lambda x: -x[1]):
        print(f"  {s:<25} {n}")
    print()

    # 3) 按错误类型（从 err 提炼）分组
    by_err = Counter(short_err(info.get("err", "")) for info in failed.values())
    print("— 按错误细类（short_err） —")
    for e, n in sorted(by_err.items(), key=lambda x: -x[1]):
        print(f"  {e:<30} {n}")
    print()

    # 4) 列表样本（每个错误类各 2 条示例）
    samples_per_err: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for h, info in failed.items():
        key = short_err(info.get("err", ""))
        if len(samples_per_err[key]) < 2:
            samples_per_err[key].append(
                (info.get("reg_id", "?"), info.get("err", "")[:80])
            )

    print("— 各错误类典型样本 (最多 2 条) —")
    for err_key, samples in sorted(samples_per_err.items(), key=lambda x: -by_err[x[0]]):
        print(f"\n  [{err_key}]  (共 {by_err[err_key]} 条)")
        for reg_id, err in samples:
            print(f"    {reg_id:<35}  {err}")

    # 5) 按日期 + 错误类交叉
    print("\n\n— 日期 × 错误类交叉 —")
    cross: dict[tuple[str, str], int] = Counter()
    for info in failed.values():
        cross[(info.get("date", "?"), short_err(info.get("err", "")))] += 1
    dates = sorted({k[0] for k in cross})
    err_keys = sorted({k[1] for k in cross}, key=lambda x: -sum(cross[(d, x)] for d in dates))
    print(f"{'日期':<12} " + "  ".join(f"{e:<22}" for e in err_keys))
    for d in dates:
        row = [f"{d:<12} "]
        for e in err_keys:
            row.append(f"{cross.get((d, e), 0):<22}")
        print("  ".join(row))


if __name__ == "__main__":
    main()
