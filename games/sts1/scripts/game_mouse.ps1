# Move the real cursor over the game window (and optionally click).
# The game runs borderless fullscreen at 1920x1080, so game coords == screen coords.
# Used for menu recovery when CommunicationMod has no verb for the screen
# (e.g. the main menu's Continue button after a crash-to-menu).
# usage: powershell -File game_mouse.ps1 -X 232 -Y 304 [-Click] [-Title "Modded Slay the Spire"]
param(
    [Parameter(Mandatory=$true)][int]$X,
    [Parameter(Mandatory=$true)][int]$Y,
    [switch]$Click,
    [string]$Title = "Modded Slay the Spire"
)

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Mouse {
    [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
    [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, System.Text.StringBuilder s, int n);
    [DllImport("user32.dll")] public static extern bool EnumWindows(EnumWindowsProc cb, IntPtr lp);
    [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
    [DllImport("user32.dll")] public static extern void mouse_event(uint flags, uint dx, uint dy, uint data, UIntPtr extra);
    public delegate bool EnumWindowsProc(IntPtr h, IntPtr lp);
    public struct RECT { public int Left, Top, Right, Bottom; }
}
"@

[void][Win32Mouse]::SetProcessDPIAware()

$target = [IntPtr]::Zero
$cb = {
    param($h, $lp)
    if (-not [Win32Mouse]::IsWindowVisible($h)) { return $true }
    $sb = New-Object System.Text.StringBuilder 512
    [void][Win32Mouse]::GetWindowText($h, $sb, 512)
    if ($sb.ToString() -like "*$Title*") {
        Set-Variable -Name target -Value $h -Scope 1
        return $false
    }
    return $true
}
[void][Win32Mouse]::EnumWindows($cb, [IntPtr]::Zero)
if ($target -eq [IntPtr]::Zero) { Write-Error "window not found: *$Title*"; exit 1 }

$r = New-Object Win32Mouse+RECT
[void][Win32Mouse]::GetWindowRect($target, [ref]$r)
$sx = $r.Left + $X
$sy = $r.Top + $Y

[void][Win32Mouse]::SetForegroundWindow($target)
Start-Sleep -Milliseconds 150
[void][Win32Mouse]::SetCursorPos($sx, $sy)
Start-Sleep -Milliseconds 150
if ($Click) {
    # MOUSEEVENTF_LEFTDOWN = 0x02, LEFTUP = 0x04
    [Win32Mouse]::mouse_event(0x02, 0, 0, 0, [UIntPtr]::Zero)
    Start-Sleep -Milliseconds 60
    [Win32Mouse]::mouse_event(0x04, 0, 0, 0, [UIntPtr]::Zero)
    Write-Output "clicked ($sx, $sy) in window rect ($($r.Left),$($r.Top))-($($r.Right),$($r.Bottom))"
} else {
    Write-Output "hover ($sx, $sy) in window rect ($($r.Left),$($r.Top))-($($r.Right),$($r.Bottom))"
}
