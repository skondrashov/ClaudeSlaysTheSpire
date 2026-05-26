$stsDir = "C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire"
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName Microsoft.VisualBasic

Start-Process -FilePath "$stsDir\jre\bin\java.exe" -ArgumentList "-jar `"$stsDir\mts-launcher.jar`"" -WorkingDirectory $stsDir

# Wait for mod window, press Play
while (-not ($w = Get-Process | Where-Object { $_.MainWindowTitle -like '*ModTheSpire*' })) { Start-Sleep 1 }
Start-Sleep 1
[Microsoft.VisualBasic.Interaction]::AppActivate($w.Id)
Start-Sleep -Milliseconds 500
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')

# Wait for relay
while (-not (Test-NetConnection 127.0.0.1 -Port 19284 -WarningAction SilentlyContinue).TcpTestSucceeded) { Start-Sleep 3 }
Write-Host "Ready."
