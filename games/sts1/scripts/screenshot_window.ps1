# Screenshot a window by title substring (default: the OBS preview projector).
# Uses PrintWindow (PW_RENDERFULLCONTENT) so the capture shows the window's own
# content even when other windows cover it — CopyFromScreen photographed
# whatever was visually on top of the target's rect.
# usage: powershell -ExecutionPolicy Bypass -File screenshot_window.ps1 [-Title "..."] [-Out path.png]
param(
    [string]$Title = "Projector - Preview",
    [string]$Out = "$env:TEMP\overlay_shot.png"
)

Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Shot {
    [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
    [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, System.Text.StringBuilder s, int n);
    [DllImport("user32.dll")] public static extern bool EnumWindows(EnumWindowsProc cb, IntPtr lp);
    [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
    [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr hdc, uint flags);
    public delegate bool EnumWindowsProc(IntPtr h, IntPtr lp);
    public struct RECT { public int Left, Top, Right, Bottom; }
}
"@

[void][Win32Shot]::SetProcessDPIAware()

$target = [IntPtr]::Zero
$cb = {
    param($h, $lp)
    if (-not [Win32Shot]::IsWindowVisible($h)) { return $true }
    $sb = New-Object System.Text.StringBuilder 512
    [void][Win32Shot]::GetWindowText($h, $sb, 512)
    if ($sb.ToString() -like "*$Title*") {
        Set-Variable -Name target -Value $h -Scope 1
        return $false
    }
    return $true
}
[void][Win32Shot]::EnumWindows($cb, [IntPtr]::Zero)

if ($target -eq [IntPtr]::Zero) {
    Write-Error "window not found: *$Title*"
    exit 1
}

$r = New-Object Win32Shot+RECT
[void][Win32Shot]::GetWindowRect($target, [ref]$r)
$w = $r.Right - $r.Left; $h = $r.Bottom - $r.Top
if ($w -le 0 -or $h -le 0) { Write-Error "degenerate rect ${w}x${h}"; exit 1 }

$bmp = New-Object System.Drawing.Bitmap $w, $h
$g = [System.Drawing.Graphics]::FromImage($bmp)
$hdc = $g.GetHdc()
# 2 = PW_RENDERFULLCONTENT (captures GPU-composited content, needed for OBS)
$ok = [Win32Shot]::PrintWindow($target, $hdc, 2)
$g.ReleaseHdc($hdc)
$g.Dispose()
if (-not $ok) { Write-Error "PrintWindow failed"; $bmp.Dispose(); exit 1 }
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Output "$Out (${w}x${h})"
