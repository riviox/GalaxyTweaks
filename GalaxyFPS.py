import os
import requests
import ctypes
import sys
import subprocess
from colorama import Fore, init

init(autoreset=True)
local = "3.6.1"

print(Fore.GREEN + "Loading...")

def run_as_admin():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return

        script = os.path.abspath(sys.argv[0])
        params = ' '.join(sys.argv[1:])
        subprocess.run(['powershell', f'Start-Process -Verb RunAs "{sys.executable}" -ArgumentList "{script} {params}"'])
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
run_as_admin()

temp_folder = os.environ['TEMP']
temp_version_file = os.path.join(temp_folder, "gversion.txt")
versionurl = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/version"

if os.path.exists(temp_version_file):
    os.remove(temp_version_file)

response = requests.get(versionurl)
if response.status_code == 200:
    with open(temp_version_file, 'wb') as file:
        file.write(response.content)



def update(local):
    update_url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/GalaxyTweaks.py"
    response = requests.get(update_url)
    
    if response.status_code == 200:
        new_version = local
        script_lines = response.text.splitlines()
        for line in script_lines:
            if line.startswith('local ='):
                new_version = line.split('=')[1].strip().replace('"', '')
                break

        if local != new_version:
            print(f"Your Version: {local}")
            print(f"New version: {new_version}")
            print("Note: You don't have to install pre-releases.")
            choice = input("Do you want to update? (y/n): ")
            if choice.lower() == 'y':
                with open(__file__, 'wb') as file:
                    file.write(response.content)
                
                python = sys.executable
                os.execl(python, python, *sys.argv)
                exit()

adj = (" " * 10)
def prtlogo():
    logo = f"""{Fore.RED}
{adj}
{adj}  ▄████  ▄▄▄       ██▓    ▄▄▄      ▒██   ██▒▓██   ██▓▄▄▄█████▓ █     █░▓█████ ▄▄▄       ██ ▄█▀  ██████ 
{adj} ██▒ ▀█▒▒████▄    ▓██▒   ▒████▄    ▒▒ █ █ ▒░ ▒██  ██▒▓  ██▒ ▓▒▓█░ █ ░█░▓█   ▀▒████▄     ██▄█▒ ▒██    ▒ 
{adj}▒██░▄▄▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ░░  █   ░  ▒██ ██░▒ ▓██░ ▒░▒█░ █ ░█ ▒███  ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   
{adj}░▓█  ██▓░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██  ░ █ █ ▒   ░ ▐██▓░░ ▓██▓ ░ ░█░ █ ░█ ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄   ▒   ██▒
{adj}░▒▓███▀▒ ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒ ▒██▒  ░ ██▒▓░  ▒██▒ ░ ░░██▒██▓ ░▒████▒▓█   ▓██▒▒██▒ █▄▒██████▒▒
{adj}░▒   ▒  ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░▒▒ ░ ░▓ ░   ██▒▒▒   ▒ ░░   ░ ▓░▒ ▒  ░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
{adj}  ░   ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░░   ░▒ ░ ▓██ ░▒░     ░      ▒ ░ ░   ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░
{adj}░ ░   ░   ░   ▒     ░ ░    ░   ▒    ░    ░   ▒ ▒ ░░    ░        ░   ░     ░    ░   ▒   ░ ░░ ░ ░  ░  ░  
{adj}      ░       ░  ░    ░  ░     ░  ░ ░    ░   ░ ░                  ░       ░  ░     ░  ░░  ░         ░  
{adj}                                             ░ ░                   {Fore.GREEN} Version: {local}                               
                          """
    print(logo)

while True:
    os.system("title GalaxyTweaks")
    update(local)
    usr = os.getenv("USERNAME")
    user = Fore. YELLOW + usr
    os.system("cls")
    prtlogo()
    print(f"""
{adj}{Fore.BLUE}[ {Fore.GREEN}1 {Fore.BLUE}] {Fore.GREEN}Main Tweaks
{adj}{Fore.BLUE}[ {Fore.GREEN}2 {Fore.BLUE}] {Fore.GREEN}Delete Tweaks
{adj}{Fore.BLUE}[ {Fore.GREEN}3 {Fore.BLUE}] {Fore.GREEN}Internet Tweaks
{adj}{Fore.BLUE}[ {Fore.GREEN}4 {Fore.BLUE}] {Fore.GREEN}Cleaner
{adj}{Fore.BLUE}[ {Fore.GREEN}5 {Fore.BLUE}] {Fore.GREEN}Advanced Tweaks
{adj}{Fore.BLUE}[ {Fore.GREEN}6 {Fore.BLUE}] {Fore.GREEN}Info
{adj}{Fore.BLUE}[ {Fore.GREEN}7 {Fore.BLUE}] {Fore.GREEN}Registry backup [ RECOMMENDED ] """)
    choice = input(f"{adj}{Fore.BLUE}[ {Fore.GREEN}? {Fore.BLUE}] {Fore.GREEN}> {Fore.YELLOW}")

    if choice == "1":
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "FeatureSettings" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "FeatureSettingsOverrideMask" /t REG_SZ /d "3" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "PoolUsageMaximum" /t REG_SZ /d "00000060" /f')
        os.system('Reg.exe add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v "AppCaptureEnabled" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v "DisableExceptionChainValidation" /t REG_DWORD /d "1" /f')
        os.system('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v "DpcWatchdogProfileOffset" /t REG_DWORD /d "0" /f')
        os.system('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v "DpcWatchdogPeriod" /t REG_DWORD /d "0" /f')
        os.system('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v "KernelSEHOPEnabled" /t REG_DWORD /d "0" /f')
        os.system('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v "SerializeTimerExpiration" /t REG_DWORD /d "0" /f')
        os.system('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel" /v "InterruptSteeringDisabled" /t REG_DWORD /d "1" /f')
        os.system('Reg.exe add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\SettingSync" /v "SyncPolicy" /t REG_DWORD /d "5" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings" /v "Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials" /v "Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility" /v "Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows" /v "Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d "2" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\DirectX\UserGpuPreferences" /v "DirectXUserGlobalSettings" /t REG_SZ /d "VRROptimizeEnable=0;" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Accessibility\MouseKeys" /v "Flags" /t REG_SZ /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Accessibility\StickyKeys" /v "Flags" /t REG_SZ /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Accessibility\Keyboard Response" /v "Flags" /t REG_SZ /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Accessibility\ToggleKeys" /v "Flags" /t REG_SZ /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v "Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\International\User Profile" /v "HttpAcceptLanguageOptOut" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Start_TrackProgs" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SubscribedContent-338393Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v "SubscribedContent-353696Enabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Speech_OneCore\Settings\OnlineSpeechPrivacy" /v "HasAccepted" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Personalization\Settings" /v "AcceptedPrivacyPolicy" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\InputPersonalization" /v "RestrictImplicitInkCollection" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\InputPersonalization" /v "RestrictImplicitTextCollection" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore" /v "HarvestContacts" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack" /v "ShowedToastAtLevel" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy" /v "TailoredExperiencesWithDiagnosticDataEnabled" /t REG_DWORD /d "0" /f')
        os.system(r'Powercfg -h off')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Siuf\Rules" /v "NumberOfSIUFInPeriod" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe delete "HKCU\SOFTWARE\Microsoft\Siuf\Rules" /v "PeriodInNanoSeconds" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "PublishUserActivities" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "UploadUserActivities" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userNotificationListener" /v "Value" /t REG_SZ /d "Deny" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" /v "Value" /t REG_SZ /d "Deny" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics" /v "Value" /t REG_SZ /d "Deny" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userAccountInformation" /v "Value" /t REG_SZ /d "Deny" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v "BackgroundAppGlobalToggle" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MinAnimate" /t REG_SZ /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MaxAnimate" /t REG_SZ /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ExtendedUIHoverTime" /t REG_DWORD /d "196608" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DontPrettyPath" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ListviewShadow" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "TaskbarAnimations" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\DWM" /v "EnableAeroPeek" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DWM" /v "DWMWA_TRANSITIONS_FORCEDISABLED" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DWM" /v "DisallowAnimations" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoLowDiskSpaceChecks" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "LinkResolveIgnoreLinkInfo" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoResolveSearch" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoResolveTrack" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoInternetOpenWith" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoInstrumentation" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "EnergyEstimationEnabled" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Desktop" /v "FontSmoothing" /t REG_SZ /d "2" /f')
        os.system(r'Reg.exe add "HKCU\Control Panel\Desktop" /v "FontSmoothingType" /t REG_DWORD /d "2" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView" /v "AllUpView" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MultitaskingView\AllUpView" /v "Remove TaskView" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "ConvertibleSlateMode" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d "38" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\usbxhci\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\USBHUB3\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f')
        os.system(r'Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\NDIS\Parameters" /v "ThreadPriority" /t REG_DWORD /d "31" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "DisallowShaking" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "EnableBalloonTips" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v "StartupDelayInMSec" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKCU\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\PushNotifications" /v "NoTileApplicationNotification" /t REG_DWORD /d "1" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v "AllowDeviceNameInTelemetry" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Affinity" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Background Only" /t REG_SZ /d "False" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Clock Rate" /t REG_DWORD /d "10000" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d "8" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Priority" /t REG_DWORD /d "6" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d "High" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "SFIO Priority" /t REG_SZ /d "High" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "BackgroundPriority" /t REG_DWORD /d "0" /f')
        os.system(r'Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Latency Sensitive" /t REG_SZ /d "True" /f')
        os.system(r'''Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v "CoalescingTimerInterval" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Attributes" /t REG_DWORD /d "2" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Affinity" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Background Only" /t REG_SZ /d "False" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Clock Rate" /t REG_DWORD /d "10000" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "GPU Priority" /t REG_DWORD /d "8" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Priority" /t REG_DWORD /d "6" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Scheduling Category" /t REG_SZ /d "High" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "SFIO Priority" /t REG_SZ /d "High" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "BackgroundPriority" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\75b0ae3f-bce0-45a7-8c89-c9611c25e100" /v "Latency Sensitive" /t REG_SZ /d "True" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "DisableTaggedEnergyLogging" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxApplication" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy" /v "TelemetryMaxTagPerApplication" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Processor" /v "Cstates" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Processor" /v "Capabilities" /t REG_DWORD /d "516198" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "HighPerformance" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "HighestPerformance" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MinimumThrottlePercent" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MaximumThrottlePercent" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MaximumPerformancePercent" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "Class1InitialUnparkCount" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "InitialUnparkCount" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power" /v "MaximumPerformancePercent" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /v "PowerThrottlingOff" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WcmSvc\GroupPolicy" /v "fDisablePowerManagement" /t REG_DWORD /d "1" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PDC\Activators\Default\VetoPolicy" /v "EA:EnergySaverEngaged" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PDC\Activators\28\VetoPolicy" /v "EA:PowerStateDischarging" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Misc" /v "DeviceIdlePolicy" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "PerfEnergyPreference" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "PerfEnergyPreference" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMinCores" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMaxCores" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMinCores1" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPMaxCores1" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CpLatencyHintUnpark1" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPDistribution" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CpLatencyHintUnpark" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "MaxPerformance1" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "MaxPerformance" /t REG_DWORD /d "100" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPDistribution1" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPHEADROOM" /t REG_DWORD /d "0" /f
Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor" /v "CPCONCUR
Reg.exe add "HKCU\Control Panel\PowerCfg\GlobalPowerPolicy" /v "Policies" /t REG_BINARY /d "01000000020000000100000000000000020000000000000000000000000000002c0100003232030304000000040000000000000000000000840300002c01000000000000840300000001646464640000" /f
Reg.exe add "HKCU\Control Panel\PowerCfg\GlobalPowerPolicy" /v "Policies" /t REG_BINARY /d "01000000020000000100000000000000020000000000000000000000000000002c0100003232030304000000040000000000000000000000840300002c01000000000000840300000001646464640000" /f
''')
        os.system('Reg.exe add "HKCU\Control Panel\Desktop" /v "AutoEndTasks" /t REG_SZ /d "1" /f')
        os.system('Reg.exe add "HKCU\Control Panel\Desktop" /v "HungAppTimeout" /t REG_SZ /d "1000" /f')
        os.system('Reg.exe add "HKCU\Control Panel\Desktop" /v "WaitToKillAppTimeout" /t REG_SZ /d "2000" /f')
        os.system('Reg.exe add "HKCU\Control Panel\Desktop" /v "LowLevelHooksTimeout" /t REG_SZ /d "1000" /f')
        os.system('Reg.exe add "HKCU\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKLM\SYSTEM\CurrentControlSet\Control" /v "WaitToKillServiceTimeout" /t REG_SZ /d "2000" /f')
        os.system('taskkill /f /im explorer.exe')
        os.system('start explorer.exe')

    elif choice == "2":
        print("MAYBE IN NEXT UPDATE :O")

    elif choice == "3":
        os.system('ipconfig /flushdns')
        os.system('ipconfig /registerdns')
        os.system('ipconfig /release')
        os.system('ipconfig /renew')
        os.system('netsh winsock reset')

    elif choice == "4":
        os.system('cls')
        print("Cleaning temporary files...")
        os.system('timeout 3 >nul')
        os.system(f'del /s /f /q {os.environ["SYSTEMDRIVE"]}\\windows\\temp\\*.*')
        os.system(f'rd /s /q {os.environ["SYSTEMDRIVE"]}\\windows\\temp')
        os.system('md c:\\windows\\temp')
        os.system(f'del /s /f /q {os.environ["SYSTEMDRIVE"]}\\WINDOWS\\Prefetch')
        os.system(f'del /s /f /q {os.environ["temp"]}\\*.*')
        os.system(f'rd /s /q {os.environ["temp"]}')
        os.system('cls')
        print("Successful deleted temporary files!")
        os.system('timeout 1 >nul')
        os.system('cls')
        os.system('timeout 3 >nul')
        print("Cleaning logs...")
        os.system('md %temp%')
        os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\Temp\\*.*')
        os.system(f'del /q /f /s {os.environ["WINDIR"]}\\Prefetch\\*.*')
        os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\*.log')
        os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\*.bak')
        os.system(f'del /q /f /s {os.environ["SYSTEMDRIVE"]}\\*.gid')
        os.system('cls')
        print("Successful cleaned logs!")
        os.system('timeout 2 >nul')
        print("Returning to menu...")
        os.system('timeout 3 >nul')

    elif choice == "5":
        reg_file_url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/regs/advtweaks.reg"
        reg_file_name = "%temp%\\advtweaks.reg"

        response = requests.get(reg_file_url)
        if response.status_code == 200:
            with open(reg_file_name, 'wb') as reg_file:
                reg_file.write(response.content)

            if os.path.exists(reg_file_name):
                subprocess.run(["regedit", "/s", reg_file_name]) 
        else:
            print("Failed to download the .reg file")

    elif choice == "6":
        print("""
            Made by
         _       _           
    _ __(_)_   _(_) _____  __
   | '__| \ \ / / |/ _ \ \/ /
 _ | |  | |\ V /| | (_) >  < 
|_||_|  |_| \_/ |_|\___/_/\_\\
              """)
        print("Version: " + local)
        print("https://discord.gg/zZyfZnNh")
        os.system('pause >NUL')

    elif choice == "7":
        os.system('regedit.exe /e "C:\GalaxyFPSregbckp.reg"')
    else:
        print(f' [ {choice} ] is Invalid. Please try again.')
