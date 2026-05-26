Stop-Process -Name java -Force -ErrorAction SilentlyContinue
Stop-Process -Name AutoHotkey64 -Force -ErrorAction SilentlyContinue
# relay.py is a child of java — dies with it, but kill stragglers
Get-CimInstance Win32_Process -Filter "CommandLine LIKE '%relay.py%'" | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
Write-Host "Killed."
