# Build a standalone Windows executable for the Launch Email Sequencer.

$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
$python = Join-Path $root "venv\Scripts\python.exe"
$artifactDir = Join-Path $PSScriptRoot "windows"
$workDir = Join-Path $root "build\pyinstaller"
$specDir = Join-Path $root "build\pyinstaller-spec"
$exeName = "Launch Email Sequencer"

if (-not (Test-Path $python)) {
    Write-Host "venv missing; running setup.bat first..."
    & (Join-Path $root "setup.bat")
}

if (-not (Test-Path $python)) {
    throw "Python environment was not created. Run setup.bat and try again."
}

& $python -m pip install --upgrade pyinstaller

if (Test-Path $artifactDir) { Remove-Item -Recurse -Force $artifactDir }
if (Test-Path $workDir) { Remove-Item -Recurse -Force $workDir }
if (Test-Path $specDir) { Remove-Item -Recurse -Force $specDir }
New-Item -ItemType Directory -Path $artifactDir | Out-Null
New-Item -ItemType Directory -Path $workDir | Out-Null
New-Item -ItemType Directory -Path $specDir | Out-Null

$promptFile = Join-Path $root "launch_email_sequencer\system_prompt.md"
$entryPoint = Join-Path $root "launch_email_sequencer\agent.py"

& $python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --console `
    --name $exeName `
    --paths $root `
    --hidden-import shared.client `
    --hidden-import shared.keyloader `
    --add-data "$promptFile;launch_email_sequencer" `
    --distpath $artifactDir `
    --workpath $workDir `
    --specpath $specDir `
    $entryPoint

$exe = Join-Path $artifactDir "$exeName.exe"
if (-not (Test-Path $exe)) {
    throw "Build finished but executable was not found at $exe"
}

$size = (Get-Item $exe).Length
Write-Host "wrote $exe ($([math]::Round($size / 1MB, 2)) MB)"
