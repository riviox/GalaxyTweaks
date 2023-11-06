import os
import requests
import ctypes
import subprocess
import keyboard
from colorama import Fore, Back, Style, init

init(autoreset=True)

message = 'Note that you must run GalaxyFPS as an administrator for the changes to take effect on your system. Else there will be no changes on your system'
ctypes.windll.user32.MessageBoxW(0, message, 'GalaxyFPS v2.0', 0x10)

temp_folder = os.environ['TEMP']
versionurl = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/version"
temp_version_file = os.path.join(temp_folder, "gversion.txt")

if os.path.exists(temp_version_file):
    os.remove(temp_version_file)

response = requests.get(versionurl)
if response.status_code == 200:
    with open(temp_version_file, 'wb') as file:
        file.write(response.content)

# Otwarcie pliku z nową wersją i aktualizacja, jeśli jest nowa wersja dostępna
local = "2.0"
if os.path.exists(temp_version_file):
    with open(temp_version_file, "r") as file:
        new_version = file.read().strip()
        if local < new_version:
            print(f"Your Version: {local}")
            print(f"New version: {new_version}")
            print("Note: You don't have to install pre-releases.")
            choice = input("Do you want to update? (y/n): ")
            if choice.lower() == 'y':
                update_url = "https://github.com/RivioxGaming/GalaxyFPS/releases/latest/GalaxyFPS.py"
                response = requests.get(update_url)
                if response.status_code == 200:
                    with open(__file__, 'wb') as file:
                        file.write(response.content)
                    subprocess.call([__file__])
                    exit()
while True:
    os.system("cls")
    print(f"""{Fore.RED}  ▄████  ▄▄▄       ██▓    ▄▄▄      ▒██   ██▒▓██   ██▓     █████▒██▓███    ██████ 
 ██▒ ▀█▒▒████▄    ▓██▒   ▒████▄    ▒▒ █ █ ▒░ ▒██  ██▒   ▓██   ▒▓██░  ██▒▒██    ▒ 
▒██░▄▄▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ░░  █   ░  ▒██ ██░   ▒████ ░▓██░ ██▓▒░ ▓██▄   
░▓█  ██▓░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██  ░ █ █ ▒   ░ ▐██▓░   ░▓█▒  ░▒██▄█▓▒ ▒  ▒   ██▒
░▒▓███▀▒ ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒ ▒██▒  ░ ██▒▓░   ░▒█░   ▒██▒ ░  ░▒██████▒▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░▒▒ ░ ░▓ ░   ██▒▒▒     ▒ ░   ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░
  ░   ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░░   ░▒ ░ ▓██ ░▒░     ░     ░▒ ░     ░ ░▒  ░ ░
░ ░   ░   ░   ▒     ░ ░    ░   ▒    ░    ░   ▒ ▒ ░░      ░ ░   ░░       ░  ░  ░  
      ░       ░  ░    ░  ░     ░  ░ ░    ░   ░ ░                              ░  
                                             ░ ░                                 """)
    print(Fore.YELLOW + "Galaxy FPS v", local, "[ TEMP MENU ]")
    print(Fore.CYAN + "> 1. Tweaks")
    print("> 2. Delete Tweaks")
    print(Fore.GREEN + "> 3. Internet Tweaks")
    print(Fore.RED + "> 4. Cleaner")
    print(Fore.MAGENTA + "> 5. Info")
    choice = input(Fore.WHITE + ">>> ")

    if choice == "1":
        os.system('Reg.exe add "HKCU\Control Panel\Desktop" /v "MenuShowDelay" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "FeatureSettings" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "FeatureSettingsOverrideMask" /t REG_SZ /d "3" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "SystemPages" /t REG_SZ /d "0" /f')
        os.system('Reg.exe add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" /v "PoolUsageMaximum" /t REG_SZ /d "00000060" /f')
        os.system('Reg.exe add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v "AppCaptureEnabled" /t REG_SZ /d "0" /f')
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
        # Informacje
        print("Version: " + local)
        print("Author: RivioxGaming#4176")
        print("Credits: caxzy#3907 for autoupdater from ZTweaks :trollface:")
        os.system('timeout /t 5 >nul')
    else:
        print("Invalid choice. Please try again.")
