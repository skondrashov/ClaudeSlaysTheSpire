# Kill ONLY the Slay the Spire game and its relay.
#
# Two foot-guns this avoids:
#  - `Stop-Process -Name java` kills ALL java (IDEs, etc.) — scoped to StS by cmdline.
#  - `CommandLine LIKE '%relay.py%'` across ALL processes matches this very Claude Code
#    session, because its --system-prompt (AGENTS.md) literally contains "relay.py".
#    So the relay kill is restricted to python processes only.

# The StS game's java (ModTheSpire launcher + the game), matched by command line.
Get-CimInstance Win32_Process -Filter "Name = 'java.exe'" |
    Where-Object { $_.CommandLine -match 'SlayTheSpire|ModTheSpire|mts-launcher' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }

# relay.py — only python processes (never claude.exe / pwsh that merely mention it).
Get-CimInstance Win32_Process -Filter "Name = 'python.exe' OR Name = 'pythonw.exe'" |
    Where-Object { $_.CommandLine -match 'relay\.py' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }

Write-Host "Killed (Slay the Spire + relay only)."
