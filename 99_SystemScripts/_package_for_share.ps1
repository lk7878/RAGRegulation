<#
.SYNOPSIS
  把 CcVault 打包为可分享的 zip，自动排除敏感和冗余文件。

.PARAMETER Mode
  A = 只分享知识库 (~35MB)
  B = 知识库 + 脚本 (~90MB)
  C = 完整副本含 PDFs (~2.3GB)

.PARAMETER OutPath
  输出 zip 路径，默认 D:\CcVault_share_{mode}_{date}.zip

.EXAMPLE
  # 最常用：A 模式
  powershell -File _package_for_share.ps1 -Mode A

.EXAMPLE
  # B 模式含脚本但排除密钥
  powershell -File _package_for_share.ps1 -Mode B -OutPath "D:\share.zip"
#>
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("A", "B", "C")]
    [string]$Mode,

    [string]$OutPath
)

$ErrorActionPreference = "Stop"
$src = "D:\CcVault"
$date = Get-Date -Format "yyyyMMdd"
if (-not $OutPath) {
    $OutPath = "D:\CcVault_share_${Mode}_${date}.zip"
}

# 临时暂存目录（复制白名单内容）
$tmp = "$env:TEMP\CcVault_pkg_$date"
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory -Path $tmp | Out-Null

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  CcVault 分享打包 · 模式 $Mode" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

function Copy-WithExclusions {
    param($SrcDir, $DestDir, [string[]]$Exclude)
    $excludeArgs = @()
    foreach ($e in $Exclude) { $excludeArgs += @("/XD", $e) }
    # 使用 robocopy 以支持排除
    & robocopy $SrcDir $DestDir /E /MT:16 /NFL /NDL /NJH /NJS /NP $excludeArgs | Out-Null
}

# === 所有模式都包含的核心内容 ===
Write-Host "[1/N] 复制 01_Wiki (笔记 + 图片资产)..." -ForegroundColor Green
Copy-WithExclusions "$src\01_Wiki" "$tmp\01_Wiki" @()

Write-Host "[2/N] 复制辅助目录 (Schema, Topics, Audit)..." -ForegroundColor Green
Copy-Item "$src\02_Schema" "$tmp\02_Schema" -Recurse
if (Test-Path "$src\02_Wiki") { Copy-Item "$src\02_Wiki" "$tmp\02_Wiki" -Recurse }
if (Test-Path "$src\04_Topics") { Copy-Item "$src\04_Topics" "$tmp\04_Topics" -Recurse }
if (Test-Path "$src\05_Audit") { Copy-Item "$src\05_Audit" "$tmp\05_Audit" -Recurse }
if (Test-Path "$src\03_Equivalence") { Copy-Item "$src\03_Equivalence" "$tmp\03_Equivalence" -Recurse }
if (Test-Path "$src\00_Dashboards") { Copy-Item "$src\00_Dashboards" "$tmp\00_Dashboards" -Recurse }

Write-Host "[3/N] 复制根目录手册 (.md)..." -ForegroundColor Green
Get-ChildItem "$src" -Filter "*.md" -File | Copy-Item -Destination $tmp
Copy-Item "$src\.gitignore" $tmp -ErrorAction SilentlyContinue

Write-Host "[4/N] 复制 .obsidian 配置 (去工作区)..." -ForegroundColor Green
Copy-WithExclusions "$src\.obsidian" "$tmp\.obsidian" @()
# 删除工作区特定配置
Remove-Item "$tmp\.obsidian\workspace.json" -ErrorAction SilentlyContinue
Remove-Item "$tmp\.obsidian\workspace-mobile.json" -ErrorAction SilentlyContinue

# === B / C 模式：包含脚本 ===
if ($Mode -in @("B", "C")) {
    Write-Host "[5/N] 复制 99_SystemScripts (排除 .venv/.env/.staging/outputs/logs)..." -ForegroundColor Green
    Copy-WithExclusions "$src\99_SystemScripts" "$tmp\99_SystemScripts" @(
        ".venv",
        ".staging",
        ".stage3",
        ".stage4",
        ".stage5",
        "__pycache__",
        "cache",
        "logs",
        "outputs"      # MinerU outputs (数百 MB，对方重新跑就有)
    )
    # 删除所有 .env 文件（含 API key）
    Get-ChildItem "$tmp\99_SystemScripts" -Recurse -Filter ".env" -Force | Remove-Item -Force
    # 删除所有 cross_check 日志（含 LLM raw response）
    Get-ChildItem "$tmp\99_SystemScripts" -Recurse -Filter ".cross_check_*.log" -Force | Remove-Item -Force
    # 保留 .env.template 作为示例
    Write-Host "  - 删除了所有 .env（API key）" -ForegroundColor Yellow
    Write-Host "  - 保留了 .env.template 让对方参照" -ForegroundColor Yellow
}

# === C 模式：完整原始 PDFs ===
if ($Mode -eq "C") {
    Write-Host "[6/N] 复制 00_Raw/标准库 (1.8GB 原始 PDFs)..." -ForegroundColor Green
    Copy-WithExclusions "$src\00_Raw" "$tmp\00_Raw" @()
    Write-Host "  ⚠️ 注意 GB 强标可能有版权限制，仅分享给信任方" -ForegroundColor Red
}

# === 最后检查：确保没有 .env 残留 ===
$leakCheck = Get-ChildItem $tmp -Recurse -Filter ".env" -Force -ErrorAction SilentlyContinue
if ($leakCheck) {
    Write-Host "`n❌ 安全检查失败：发现残留 .env 文件" -ForegroundColor Red
    $leakCheck | ForEach-Object { Write-Host "  $($_.FullName)" -ForegroundColor Red }
    throw "打包中止"
}
Write-Host "`n[✓] 安全检查通过：无 .env 泄漏" -ForegroundColor Green

# === 压缩 ===
Write-Host "`n[最后] 压缩为 zip..." -ForegroundColor Green
if (Test-Path $OutPath) { Remove-Item $OutPath -Force }
Compress-Archive -Path "$tmp\*" -DestinationPath $OutPath -CompressionLevel Optimal

# 清理
Remove-Item $tmp -Recurse -Force

# 报告
$size = (Get-Item $OutPath).Length / 1MB
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  完成！" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  输出: $OutPath" -ForegroundColor White
Write-Host "  大小: $([math]::Round($size, 1)) MB" -ForegroundColor White
Write-Host ""
Write-Host "  对方使用说明：" -ForegroundColor Yellow
switch ($Mode) {
    "A" {
        Write-Host "    1. 解压"
        Write-Host "    2. 装 Obsidian 1.5+"
        Write-Host "    3. 用 '打开文件夹作为库' 选择解压根目录"
        Write-Host "    4. 读 README.md / _使用说明.md 开始"
    }
    "B" {
        Write-Host "    1. 解压"
        Write-Host "    2. Obsidian 打开同 A"
        Write-Host "    3. 跑 pipeline: cd 99_SystemScripts/auto_reg_index"
        Write-Host "    4. 复制 .env.template 为 .env 并填入自己的 API key"
        Write-Host "    5. python -m venv .venv && .venv\Scripts\pip install -r requirements.txt"
    }
    "C" {
        Write-Host "    同 B，外加 00_Raw/ 里有完整 1.8GB PDFs"
        Write-Host "    可以从头重跑整个 OCR → extract → write pipeline"
    }
}
Write-Host ""
