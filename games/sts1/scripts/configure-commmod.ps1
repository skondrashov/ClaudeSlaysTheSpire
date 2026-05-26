# Configure CommunicationMod to launch relay.py
#
# CommunicationMod reads its config from the game's preferences directory.
# We need to set the 'command' property to point at our relay.py.

$prefsDir = "$env:USERPROFILE\.prefs\com.megacrit.cardcrawl.helpers.SaveHelper"
$configFile = "$prefsDir\STSCommunicationMod"

# Also check alternate location
$altPrefsDir = "$env:LOCALAPPDATA\preferences\com.megacrit.cardcrawl.helpers.SaveHelper"
$altConfigFile = "$altPrefsDir\STSCommunicationMod"

# Find Python
$python = Get-Command python -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
if (-not $python) {
    $python = Get-Command python3 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
}
if (-not $python) {
    Write-Error "Python not found in PATH"
    exit 1
}

$relayPath = (Resolve-Path "$PSScriptRoot\..\relay.py").Path
# Escape backslashes for Java properties format
$escapedRelay = $relayPath -replace '\\', '\\\\'
$escapedPython = $python -replace '\\', '\\\\'

$config = @"
command=$escapedPython $escapedRelay
runAtGameStart=false
"@

# Try both locations — create if needed
$targetDir = $prefsDir
$targetFile = $configFile

# If alt location exists, use that
if (Test-Path $altPrefsDir) {
    $targetDir = $altPrefsDir
    $targetFile = $altConfigFile
}

if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

Set-Content -Path $targetFile -Value $config -Encoding UTF8
Write-Host "CommunicationMod configured:"
Write-Host "  Config: $targetFile"
Write-Host "  Python: $python"
Write-Host "  Relay:  $relayPath"
Write-Host ""
Write-Host "To use: Launch STS via ModTheSpire with CommunicationMod enabled."
Write-Host "The mod will launch relay.py automatically when you start a run."
Write-Host "(runAtGameStart=false means you need to trigger it from in-game settings)"
Write-Host ""
Write-Host "If the config location is wrong, CommunicationMod stores its config"
Write-Host "via Java Preferences API — check the game's log for the actual path."
