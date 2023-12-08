@ECHO OFF
REM BFCPEOPTIONSTART
REM Advanced BAT to EXE Converter www.BatToExeConverter.com
REM BFCPEEXE=C:\Users\rivio\OneDrive\Dokumenty\GitHub\GalaxyTweaks\GTweaksInstaller.exe
REM BFCPEICON=C:\Program Files (x86)\Advanced BAT to EXE Converter v4.61\ab2econv461\icons\icon12.ico
REM BFCPEICONINDEX=1
REM BFCPEEMBEDDISPLAY=0
REM BFCPEEMBEDDELETE=1
REM BFCPEADMINEXE=0
REM BFCPEINVISEXE=0
REM BFCPEVERINCLUDE=1
REM BFCPEVERVERSION=1.0.0.0
REM BFCPEVERPRODUCT=GalaxyTweaks Installer
REM BFCPEVERDESC=Installs GalaxyTweaks to desktop
REM BFCPEVERCOMPANY=.riviox
REM BFCPEVERCOPYRIGHT=.riviox
REM BFCPEWINDOWCENTER=1
REM BFCPEDISABLEQE=0
REM BFCPEWINDOWHEIGHT=30
REM BFCPEWINDOWWIDTH=120
REM BFCPEWTITLE=GalaxyTweaks Installer
REM BFCPEOPTIONEND
@echo off
title GalaxyTweaks Installer
echo Downloading GalaxyTweaks
curl -L -o GalaxyTweaks.py "https://raw.githubusercontent.com/RivioxGaming/GalaxyTweaks/main/GalaxyTweaks.py"
pause
