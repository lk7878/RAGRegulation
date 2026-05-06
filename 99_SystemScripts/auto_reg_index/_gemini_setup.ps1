# _gemini_setup.ps1 — Gemini CLI 代理探测 + 配置 + 烟雾测试
#
# 用法：
#   .\_gemini_setup.ps1              # 自动探测端口并测试
#   .\_gemini_setup.ps1 -Port 7890   # 指定端口
#   .\_gemini_setup.ps1 -Persist     # 永久保存到用户环境变量
#
# 覆盖的代理软件：
#   Clash / Clash Verge / Mihomo: 7890
#   V2rayN: 10809 / 10808
#   Shadowsocks / SSR: 1080
#   Qv2ray: 8889
#   Other: 8080 / 8118 / 7897 / 20171 / 7891

param(
    [int]$Port = 0,
    [switch]$Persist,
    [switch]$SkipTest
)

$ErrorActionPreference = "Continue"

$commonPorts = @(7890, 10809, 7897, 10808, 1080, 8080, 8118, 20171, 8889, 7891)

function Test-ProxyPort {
    param([int]$P)
    $c = New-Object System.Net.Sockets.TcpClient
    try {
        $r = $c.BeginConnect("127.0.0.1", $P, $null, $null)
        $ok = $r.AsyncWaitHandle.WaitOne(400)
        return ($ok -and $c.Connected)
    } catch { return $false } finally { $c.Close() }
}

# ====================================================================
# 1. 确定端口
# ====================================================================
if ($Port -gt 0) {
    Write-Host "Using specified port: $Port" -ForegroundColor Cyan
    if (-not (Test-ProxyPort $Port)) {
        Write-Host "ERROR: port $Port is not reachable." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "Scanning common proxy ports..." -ForegroundColor Cyan
    $found = $null
    foreach ($p in $commonPorts) {
        if (Test-ProxyPort $p) {
            Write-Host "  port $p OPEN" -ForegroundColor Green
            if (-not $found) { $found = $p }
        } else {
            Write-Host "  port $p closed" -ForegroundColor DarkGray
        }
    }
    if (-not $found) {
        Write-Host "`nERROR: no proxy port found. Start your proxy software and retry." -ForegroundColor Red
        Write-Host "Or use: .\_gemini_setup.ps1 -Port <port>" -ForegroundColor Yellow
        exit 1
    }
    $Port = $found
    Write-Host "`nSelected port: $Port" -ForegroundColor Cyan
}

$proxyUrl = "http://127.0.0.1:$Port"

# ====================================================================
# 2. 设置环境变量（当前 session）
# ====================================================================
$env:HTTPS_PROXY = $proxyUrl
$env:HTTP_PROXY = $proxyUrl
$env:ALL_PROXY = $proxyUrl
Write-Host "`nSession env set:" -ForegroundColor Green
Write-Host "  HTTPS_PROXY = $proxyUrl"
Write-Host "  HTTP_PROXY  = $proxyUrl"
Write-Host "  ALL_PROXY   = $proxyUrl"

# ====================================================================
# 3. 永久保存（可选）
# ====================================================================
if ($Persist) {
    Write-Host "`nPersisting to user environment..." -ForegroundColor Cyan
    [Environment]::SetEnvironmentVariable("HTTPS_PROXY", $proxyUrl, "User")
    [Environment]::SetEnvironmentVariable("HTTP_PROXY", $proxyUrl, "User")
    Write-Host "  Done. New PowerShell sessions will inherit these." -ForegroundColor Green
    Write-Host "  To undo: [Environment]::SetEnvironmentVariable('HTTPS_PROXY', `$null, 'User')" -ForegroundColor DarkYellow
}

# ====================================================================
# 4. 烟雾测试
# ====================================================================
if ($SkipTest) {
    Write-Host "`nSkipping smoke test (per --SkipTest flag)." -ForegroundColor Yellow
    exit 0
}

Write-Host "`n=== Smoke test: gemini -p 'reply OK only' ===" -ForegroundColor Cyan
Write-Host "(This uses 1 of your 1000 daily free quota)`n" -ForegroundColor DarkYellow

$testOutput = & gemini -p "reply OK only" -o text 2>&1 | Out-String
$testOutput = $testOutput.Trim()

if ($LASTEXITCODE -eq 0 -and $testOutput -match "OK") {
    Write-Host "SUCCESS — Gemini CLI is responding." -ForegroundColor Green
    Write-Host "`nResponse preview:" -ForegroundColor DarkGreen
    Write-Host $testOutput
    Write-Host "`nNext steps:" -ForegroundColor Cyan
    Write-Host "  1. Test RAG:"
    Write-Host "     cd D:\CcVault\99_SystemScripts\auto_reg_index"
    Write-Host "     .\.venv\Scripts\python.exe _ask.py ""GB 4785 规定了什么？"""
    Write-Host "  2. Interactive mode in vault:"
    Write-Host "     cd D:\CcVault; gemini"
    Write-Host "     Gemini auto-loads GEMINI.md"
    if (-not $Persist) {
        Write-Host "  3. Persist env vars (so new terminals work):"
        Write-Host "     .\_gemini_setup.ps1 -Port $Port -Persist" -ForegroundColor Yellow
    }
    exit 0
} else {
    Write-Host "FAILED — gemini did not respond correctly." -ForegroundColor Red
    Write-Host "`nExit code: $LASTEXITCODE" -ForegroundColor DarkRed
    Write-Host "`nOutput:" -ForegroundColor DarkRed
    Write-Host $testOutput
    Write-Host "`nCommon causes:" -ForegroundColor Yellow
    Write-Host "  1. Proxy does NOT handle Gemini (some China-optimized proxies block non-SS nodes)"
    Write-Host "  2. OAuth credentials expired: run 'gemini auth login' or 'gemini /auth'"
    Write-Host "  3. Rate limit hit (1000/day exceeded)"
    Write-Host "  4. Proxy port $Port is a different kind (SOCKS vs HTTP)"
    exit 1
}
