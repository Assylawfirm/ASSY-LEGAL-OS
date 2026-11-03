# Windows PowerShell 5.1+ bootstrap for ASSY LAW FIRM — no sending.
# This script STAGES source and checks prerequisites. It DOES NOT install dependencies,
# authenticate, run discovery, start heartbeat, or send messages.
$ErrorActionPreference = "Stop"
$upstream = "https://github.com/ethanplusai/harvey.git"
$target = Join-Path $HOME "ASSY-Harvey-Pilot"
Write-Host "ASSY Harvey pilot: source staging only"
foreach ($exe in @("git","py")) {
  if (-not (Get-Command $exe -ErrorAction SilentlyContinue)) { throw "Missing prerequisite: $exe" }
}
$pyver = & py -3 -c "import sys;print(sys.version_info.major*100+sys.version_info.minor)"
if ([int]$pyver -lt 311) { throw "Python 3.11+ required" }
if (Test-Path $target) { throw "Target already exists; inspect it manually: $target" }
& git clone --depth 1 $upstream $target
if ($LASTEXITCODE -ne 0) { throw "Clone failed" }
Set-Location $target
$sha = & git rev-parse HEAD
Write-Host "Upstream commit: $sha"
& py -3 -m venv .venv
if ($LASTEXITCODE -ne 0) { throw "venv failed" }
Copy-Item ".env.example" ".env"
# No credentials and no outbound mail. These values are appended to effective YAML
# by the operator only after reviewing the upstream schema.
Write-Host "STAGED. Review source, dependencies, and copy pilot YAML manually."
Write-Host "DO NOT run harvey run, harvey discover, or email auth."
Write-Host "No email credentials configured; no messages sent."
