# Build the buyer-facing zip for Course Creator Pack.
# "dist" is excluded wholesale; the one buyer-facing file in it
# (launch_week_playbook.md) is copied to the bundle ROOT below, where the README
# tells buyers to find it. Root-level creator artifacts (cover art, build/scratch
# files) are excluded by pattern so they never reach a buyer.

$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
$staging = Join-Path $env:TEMP "course-creator-pack-build"
$bundle = Join-Path $staging "course-creator-pack"
$zipOut = Join-Path $PSScriptRoot "course-creator-pack.zip"
$launchExe = Join-Path $PSScriptRoot "windows\Launch Email Sequencer.exe"

if (Test-Path $staging) { Remove-Item -Recurse -Force $staging }
New-Item -ItemType Directory -Path $bundle | Out-Null

if (-not (Test-Path $launchExe)) {
    & (Join-Path $PSScriptRoot "build_launch_exe.ps1")
}

$exclude = @("venv", "build_venv", "build", "__pycache__", ".env", "output", ".claude", ".git", "dist", ".playwright-mcp")
# Root-level files matching these patterns are creator artifacts (cover art,
# guides, build/scratch files) and must never reach a buyer.
$rootExcludePatterns = @("*.png", "*.jpg", "*.pptx", "*.zip", "*.exe", "_*", "~`$*")

Get-ChildItem -Path $root -Recurse -Force | Where-Object {
    $rel = $_.FullName.Substring($root.Length + 1)
    $parts = $rel -split "[\\/]"
    $isRootFile = ($parts.Count -eq 1) -and (-not $_.PSIsContainer)
    $rootPatternHit = $isRootFile -and ($rootExcludePatterns | Where-Object { $parts[0] -like $_ })
    -not ($parts | Where-Object { $exclude -contains $_ }) -and
    -not $rootPatternHit
} | ForEach-Object {
    $rel = $_.FullName.Substring($root.Length + 1)
    $dest = Join-Path $bundle $rel
    if ($_.PSIsContainer) {
        if (-not (Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
    } else {
        $destDir = Split-Path $dest -Parent
        if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
        Copy-Item -Path $_.FullName -Destination $dest -Force
    }
}

# Ship the playbook at the bundle root (README references it there).
Copy-Item -Path (Join-Path $PSScriptRoot "launch_week_playbook.md") -Destination (Join-Path $bundle "launch_week_playbook.md") -Force
Copy-Item -Path (Join-Path $PSScriptRoot "CourseCreatorPack-START-HERE.txt") -Destination (Join-Path $bundle "START-HERE.txt") -Force
Copy-Item -Path $launchExe -Destination (Join-Path $bundle "Launch Email Sequencer.exe") -Force

if (Test-Path $zipOut) { Remove-Item -Force $zipOut }
Compress-Archive -Path $bundle -DestinationPath $zipOut -CompressionLevel Optimal

$size = (Get-Item $zipOut).Length
Write-Host "wrote $zipOut ($([math]::Round($size/1KB,1)) KB)"
Write-Host ""
Write-Host "Contents:"
$entries = [System.IO.Compression.ZipFile]::OpenRead($zipOut).Entries
$entries | Sort-Object FullName | ForEach-Object { Write-Host "  $($_.FullName)" }
