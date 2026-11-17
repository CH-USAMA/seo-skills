# Installs the three standalone skills into ~/.claude/skills (or the folder given with -Dest).
# Existing copies are moved to <dest>\..\skills-backups first. BeyondSEO is not installed by this script (see README).
param([string]$Dest = (Join-Path $env:USERPROFILE ".claude\skills"))
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$bkRoot = Join-Path (Split-Path -Parent $Dest) "skills-backups"
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
foreach ($s in @("ghulamali-seo-master", "seo-combined-master", "seo-site-audit")) {
    $src = Join-Path $here $s
    if (-not (Test-Path (Join-Path $src "SKILL.md"))) { throw "missing $src\SKILL.md" }
    $target = Join-Path $Dest $s
    if (Test-Path $target) {
        New-Item -ItemType Directory -Force -Path $bkRoot | Out-Null
        Move-Item $target (Join-Path $bkRoot ("{0}-{1}" -f $s, (Get-Date -Format "yyyyMMdd-HHmmss")))
        Write-Host "previous $s saved to $bkRoot"
    }
    Copy-Item $src $target -Recurse
    Get-ChildItem $target -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
    Write-Host "installed $s -> $target"
}
Write-Host "Done. Start a new Claude Code conversation to load them."
