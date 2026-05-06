# -----------------------------------------------------------------------------
# CcVault 导师版打包脚本
# 生成物：D:\CcVault_导师版_<date>.zip
# 策略：白名单拷贝到 staging → 放入导师 README → Compress-Archive → 清理 staging
# -----------------------------------------------------------------------------

$ErrorActionPreference = "Stop"

$sourceRoot  = "D:\CcVault"
$stagingRoot = "D:\CcVault_export_staging"
$packRoot    = Join-Path $stagingRoot "CcVault"
$dateTag     = Get-Date -Format "yyyy-MM-dd"
$targetZip   = "D:\CcVault_导师版_${dateTag}.zip"

Write-Host "[1/5] 准备 staging 目录 $packRoot" -ForegroundColor Cyan
if (Test-Path $stagingRoot) { Remove-Item -Recurse -Force $stagingRoot }
New-Item -ItemType Directory -Path $packRoot -Force | Out-Null

# 白名单目录 - 整目录复制（robocopy 的排除清单兜底再保护一次）
$whitelistDirs = @(
    '01_Wiki',
    '00_Dashboards',
    '02_Schema',
    '02_Wiki',
    '03_Equivalence',
    '04_Topics',
    '05_Audit',
    'copilot',
    '.obsidian'
)

# robocopy 的兜底排除（防止白名单目录里意外混入的敏感/大文件/缓存）
$excludeDirs  = @('__pycache__', '.trash', 'node_modules', '.venv', 'outputs', 'logs', '.staging')
$excludeFiles = @('*.pyc', '*.log', '.env', '*.ps1', '_mineru_state.json', '*.tmp')

Write-Host "[2/5] robocopy 白名单目录 ..." -ForegroundColor Cyan
foreach ($d in $whitelistDirs) {
    $src = Join-Path $sourceRoot $d
    $dst = Join-Path $packRoot $d
    if (Test-Path $src) {
        $rcArgs = @($src, $dst, '/E', '/NFL', '/NDL', '/NJH', '/NJS', '/NC', '/NS', '/NP')
        if ($excludeDirs.Count -gt 0)  { $rcArgs += '/XD'; $rcArgs += $excludeDirs }
        if ($excludeFiles.Count -gt 0) { $rcArgs += '/XF'; $rcArgs += $excludeFiles }
        & robocopy @rcArgs | Out-Null
        if ($LASTEXITCODE -ge 8) {
            throw "robocopy failed: $src -> $dst (exit $LASTEXITCODE)"
        }
        Write-Host "    [OK] $d" -ForegroundColor Green
    } else {
        Write-Host "    [skip] $d (not found)" -ForegroundColor Yellow
    }
}

# 顶层 md 白名单
$topFiles = @(
    'README.md',
    'CLAUDE.md',
    '_INDEX.md',
    '_CHANGELOG.md',
    '_MINERU_UPGRADE_LOG.md',
    '_使用说明.md',
    '_升级路线图.md',
    '_完整手册.md',
    '_审计报告.md'
)
Write-Host "[3/5] 复制顶层文档 ..." -ForegroundColor Cyan
foreach ($f in $topFiles) {
    $src = Join-Path $sourceRoot $f
    if (Test-Path $src) {
        Copy-Item $src -Destination $packRoot -Force
        Write-Host "    [OK] $f" -ForegroundColor Green
    } else {
        Write-Host "    [skip] $f" -ForegroundColor Yellow
    }
}

Write-Host "[4/5] 生成导师导览 README ..." -ForegroundColor Cyan
$readmeTemplate = Join-Path $sourceRoot "_advisor_readme_template.md"
$readmePath = Join-Path $packRoot "_给导师_阅读指南.md"
if (Test-Path $readmeTemplate) {
    Copy-Item $readmeTemplate -Destination $readmePath -Force
    Write-Host "    [OK] _给导师_阅读指南.md" -ForegroundColor Green
} else {
    Write-Host "    [warn] 未找到模板 $readmeTemplate" -ForegroundColor Yellow
}

# 安全扫描：staging 里是否意外混入 .env
Write-Host "    [scan] 扫描 staging 内 .env 文件 ..." -ForegroundColor Cyan
$leakedEnv = Get-ChildItem -Path $packRoot -Recurse -Force -File -ErrorAction SilentlyContinue |
             Where-Object { $_.Name -eq '.env' -or $_.Name -like '*.env.*' -or $_.Name -like '*secret*' -or $_.Name -like '*.pem' }
if ($leakedEnv) {
    Write-Host "    [ERROR] 检出敏感文件，中止打包:" -ForegroundColor Red
    $leakedEnv | ForEach-Object { Write-Host "      $($_.FullName)" -ForegroundColor Red }
    throw "敏感文件未被排除"
} else {
    Write-Host "    [OK] 无敏感文件泄露" -ForegroundColor Green
}

Write-Host "[5/5] 压缩 → $targetZip" -ForegroundColor Cyan
if (Test-Path $targetZip) { Remove-Item $targetZip -Force }
Compress-Archive -Path $packRoot -DestinationPath $targetZip -CompressionLevel Optimal

# 汇报
$zipSize = (Get-Item $targetZip).Length / 1MB
$stagingFileCount = (Get-ChildItem -Path $packRoot -Recurse -File).Count
$stagingSize = (Get-ChildItem -Path $packRoot -Recurse -File | Measure-Object -Property Length -Sum).Sum / 1MB

Write-Host ""
Write-Host "==== 打包完成 ====" -ForegroundColor Green
Write-Host "压缩包路径  : $targetZip"
Write-Host "压缩前体积  : $([math]::Round($stagingSize, 1)) MB"
Write-Host "压缩包体积  : $([math]::Round($zipSize, 1)) MB"
Write-Host "压缩包文件数: $stagingFileCount"
Write-Host ""

# 清理 staging
Write-Host "清理 staging 目录..." -ForegroundColor Cyan
Remove-Item -Recurse -Force $stagingRoot
Write-Host "Done." -ForegroundColor Green
