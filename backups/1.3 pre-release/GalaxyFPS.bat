@echo off
mode 105,30
setlocal EnableDelayedExpansion
set local=1.3 pre-release [ Last before python ] 
echo x=msgbox("Note that you must run GalaxyFPS as an administrator for the changes to take effect on your system. Else there will be no changes on your system",16,"GalaxyFPS v1.2")> info.vbs
inf.vbs
del inf.vbs
:update
cls
setlocal EnableDelayedExpansion
set localtwo=%local%
if exist "%temp%\galaxyupdate.bat" DEL /S /Q /F "%temp%\galaxyupdate.bat" >nul 2>&1
curl -g -L -# -o "%temp%\galaxyupdate.bat" "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/version" >nul 2>&1
call "%temp%\galaxyupdate.bat"
if "%local%" gtr "%localtwo%" (

echo.
set string="[95m   _   _           _       _         _____                     _ 
set string2="[95m  | | | |_ __   __| | __ _| |_ ___  |  ___|__  _   _ _ __   __| |
set string3="[95m  | | | | '_ \ / _` |/ _` | __/ _ \ | |_ / _ \| | | | '_ \ / _` |       | Your Version: %localtwo%
set string4="[95m  | |_| | |_) | (_| | (_| | ||  __/ |  _| (_) | |_| | | | | (_| |       | New version: %local%
set string5="[95m   \___/| .__/ \__,_|\__,_|\__\___| |_|  \___/ \__,_|_| |_|\__,_|       | Note: You don't have to install pre-releases.
set string6="[95m        |_|                                   

for /f "useback tokens=*" %%g in ('!string!') do set string=%%~g       
for /f "useback tokens=*" %%g in ('!string2!') do set string2=%%~g   
for /f "useback tokens=*" %%g in ('!string3!') do set string3=%%~g   
for /f "useback tokens=*" %%g in ('!string4!') do set string4=%%~g   
for /f "useback tokens=*" %%g in ('!string5!') do set string5=%%~g    
for /f "useback tokens=*" %%g in ('!string6!') do set string6=%%~g  
echo !string!     
echo !string2!   
echo !string3! 
echo !string4!
echo !string5!  
echo !string6!
echo                [95m y - Update     
echo                [95m n - Go to Menu 
echo.
	%SystemRoot%\System32\choice.exe /c:YN /n /m "%DEL% >"                         
	set choice=!errorlevel!
	if !choice! == 1 (
		curl -L -o %0 "https://github.com/RivioxGaming/GalaxyFPS/releases/latest/GalaxyFPS.bat" >nul 2>&1
		call %0
		exit /b
	)
)


:menu
title GalaxyFPS v1.2
cls
echo.
echo.
echo [35m" ________  ________  ___       ________     ___    ___ ___    ___ ________ ________  ________      [0m
echo [35m"|\   ____\|\   __  \|\  \     |\   __  \   |\  \  /  /|\  \  /  /|\  _____\\   __  \|\   ____\     [0m
echo [35m"\ \  \___|\ \  \|\  \ \  \    \ \  \|\  \  \ \  \/  / | \  \/  / | \  \__/\ \  \|\  \ \  \___|_    [0m
echo [35m" \ \  \  __\ \   __  \ \  \    \ \   __  \  \ \    / / \ \    / / \ \   __\\ \   ____\ \_____  \   [0m
echo [35m"  \ \  \|\  \ \  \ \  \ \  \____\ \  \ \  \  /     \/   \/  /  /   \ \  \_| \ \  \___|\|____|\  \  [0m
echo [35m"   \ \_______\ \__\ \__\ \_______\ \__\ \__\/  /\   \ __/  / /      \ \__\   \ \__\     ____\_\  \ [0m
echo [35m"    \|_______|\|__|\|__|\|_______|\|__|\|__/__/ /\ __\\___/ /        \|__|    \|__|    |\_________\[0m
echo [35m"                                           |__|/ \|__\|___|/                           \|__________| [0m
echo [36m"               _________________________________________________________________________             [0m
echo [91m"                  
echo [91m"                                          logged in as [32m %USERNAME%                     [0m                                                                  
echo [91m" 
echo [91m"                                              1. Tweaks                                  [0m
echo [91m"                            2. Delete tweaks              3. Internet tweaks             [0m
echo [91m"                            4. Cleaner                    5. Info                        [0m                                                                                [0m
set /p"opt=>
if /i "%opt%"=="x" goto menu
if /i "%opt%"=="1" goto tweaks
if /i "%opt%"=="2" goto deletetweaks
if /i "%opt%"=="3" goto internet_tweaks
if /i "%opt%"=="4" goto cleaner
if /i "%opt%"=="5" goto info

:tweaks
cls
title Tweaking your pc!
Reg.exe add "HKCU\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d "0" /f
Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f
Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "FeatureSettings" /t REG_SZ /d "0" /f
Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "FeatureSettingsOverrideMask" /t REG_SZ /d "3" /f
Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f
Reg.exe add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "PoolUsageMaximum" /t REG_SZ /d "00000060" /f
Reg.exe add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\GameDVR" /v "AppCaptureEnabled" /t REG_SZ /d "0" /f
taskkill /f /im explorer.exe
start explorer.exe
goto menu

:deltweaks
title removing tweaks...
echo MAYBE IN NEXT UPDATE :O
timeout -t 1 >NUL
goto menu


:cleaner
cls
title cleaning...
echo [91mCleaning temporary files...[0m
timeout 3 >nul
del /s /f /q %SYSTEMDRIVE%\windows\temp\*.*
rd /s /q %SYSTEMDRIVE%\windows\temp 
md c:\windows\temp
del /s /f /q %SYSTEMDRIVE%\WINDOWS\Prefetch 
del /s /f /q %temp%\*.* 
rd /s /q %temp%
cls
echo [91mSuccesfull deleted temporary files![0m
timeout 1 >nul
cls
timeout 3 >nul
echo [91mCleaning logs...[0m
md %temp%
del /q /f /s %SYSTEMDRIVE%\Temp\*.* 
del /q /f /s %WINDIR%\Prefetch\*.* 
del /q /f /s %SYSTEMDRIVE%\*.log 
del /q /f /s %SYSTEMDRIVE%\*.bak 
del /q /f /s %SYSTEMDRIVE%\*.gid 
cls
echo [91mSuccesfull cleaned logs![0m
echo.
timeout 2 >nul
echo [91mReturning to menu...[0m
timeout 3 >nul
goto menu

:internet
ipconfig /flushdns
ipconfig /registerdns
ipconfig /release
ipconfig /renew
netsh winsock reset
goto menu

:info
echo [35m Version: %local%
echo [35m Author: RivioxGaming#4176
echo [35m Credits: caxzy#3907 for autoupdater from ZTweaks :trollface:
timeout -t 5 >> nul
cls
goto menu
pause