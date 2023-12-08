@echo off
setlocal
set "file_url=https://raw.githubusercontent.com/RivioxGaming/GalaxyTweaks/main/GalaxyTweaks.py"
set "desktop_path=%USERPROFILE%\Desktop"
set "destination_path=%desktop_path%\GalaxyTweaks.py"
certutil -urlcache -split -f "%file_url%" "%destination_path%"
if exist "%destination_path%" (
    echo Downloaded GalaxyTweaks to %destination_path%
) else (
    echo Error while downloading
)
endlocal
