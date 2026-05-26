# Install CommunicationMod from Steam Workshop
# The other 3 mods (ModTheSpire, BaseMod, SuperFastMode) are already installed.
#
# This script opens the Steam Workshop page for CommunicationMod.
# Subscribe to it, then run configure-commmod.ps1 to point it at relay.py.

Write-Host "Opening CommunicationMod Steam Workshop page..."
Write-Host "Click 'Subscribe' to install the mod."
Write-Host ""
Start-Process "steam://url/CommunityFilePage/2131373661"

Write-Host "After subscribing, run: .\scripts\configure-commmod.ps1"
