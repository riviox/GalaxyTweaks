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
echo [91mSuccesfully cleaned logs![0m
echo.
timeout 2 >nul
echo [91mReturning to menu...[0m
timeout 3 >nul
goto menu