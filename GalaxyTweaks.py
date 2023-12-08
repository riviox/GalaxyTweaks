
import os
import sys
import subprocess
import ctypes
try:
    from colorama import Fore, init
    import requests
    import eel
    import json
except ModuleNotFoundError:
    os.system("pip install colorama")
    os.system("pip install eel[jinja2]")
    os.system("pip install requests")
    os.system("pip install json")

init(autoreset=True)
local = "3.7.1"

print(Fore.GREEN + "Loading...")
print(Fore.YELLOW + "This is GalaxyTweaks Output, do not close it!")

def get_html_from_github(file_url):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

embedded_menu_html = get_html_from_github("https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/menu/menu.html")

if not embedded_menu_html:
    print("Error: Failed to fetch HTML content from GitHub.")
    print("Exiting...")
username = os.getenv("username")
menu_folder = f"C:\\GalaxyTweaks"
menu = os.path.join(menu_folder, "menu.html")

if not os.path.exists(menu_folder):
    os.makedirs(menu_folder)

with open(menu, 'w', encoding='utf-8') as html_file:
    html_file.write(embedded_menu_html)

if not embedded_menu_html:
    print("Error: Failed to fetch HTML content from GitHub.")
    print("Exiting...")
    exit()

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

@eel.expose
def check_for_update():
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

                menu_html_url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyTweaks/main/beta/gui/menu.html"
                menu_html_response = requests.get(menu_html_url)
                
                if menu_html_response.status_code == 200:
                    menu_html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui", "menu.html")
                    with open(menu_html_file_path, 'wb') as menu_html_file:
                        menu_html_file.write(menu_html_response.content)

                python = sys.executable
                os.execl(python, python, *sys.argv)
                exit()

@eel.expose
def perform_update():
    update_url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/GalaxyTweaks.py"
    response = requests.get(update_url)

    if response.status_code == 200:
        with open(__file__, 'wb') as file:
            file.write(response.content)

        python = sys.executable
        os.execl(python, python, *sys.argv)
        exit()
        
@eel.expose
def mtw():
    print(Fore.YELLOW + "Applying Main Tweaks...")
    url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/tweaks/mtw.bat"
    response = requests.get(url)
    
    if response.status_code == 200:
        folder_path = "C:\\GalaxyTweaks\\Tweaks"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, "mtw.bat")

        with open(file_path, "wb") as file:
            file.write(response.content)

        print(Fore.GREEN + "Applied Main Tweaks!")
    else:
        print(Fore.RED + f"Failed to download file. Status code: {response.status_code}")

@eel.expose
def netw():
    print(Fore.YELLOW + "Applying Internet Tweaks!")
    os.system('ipconfig /flushdns')
    os.system('ipconfig /registerdns')
    os.system('ipconfig /release')
    os.system('ipconfig /renew')
    os.system('netsh winsock reset')
    print(Fore.GREEN + "Applied Internet Tweaks!")
    pass
    
@eel.expose
def cleaner():
    print(Fore.YELLOW + "Cleaning Temp Files...")
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
    print(Fore.GREEN + "Cleaned Temp files!")
    pass
    
@eel.expose
def ocmd():
    print(Fore.YELLOW + "Starting CMD.exe...")
    os.system("start")
    print(Fore.GREEN + "Started CMD.exe!")
    
@eel.expose
def adwt():
    print(Fore.YELLOW + "Applying Advanced Tweaks..")
    print(Fore.BLUE + "Downloading [advtweaks.reg]")
    reg_file_url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/regs/advtweaks.reg"
    reg_file_name = "%temp%\\advtweaks.reg"

    response = requests.get(reg_file_url)
    if response.status_code == 200:
        with open(reg_file_name, 'wb') as reg_file:
            reg_file.write(response.content)

        if os.path.exists(reg_file_name):
            print(Fore.YELLOW + "Running advtweaks.reg")
            subprocess.run(["regedit", "/s", reg_file_name])
            print(Fore.GREEN + "Applied Advanced Tweaks!")
        else:
            pass
    
@eel.expose
def regbckp():
    print(Fore.YELLOW + "Making registry backup...")
    os.system('regedit.exe /e "C:\GalaxyFPSregbckp.reg"')
    print(Fore.GREEN + "Registry backup is at `C:\\regbckp.reg`!")
        
@eel.expose
def dwmt():
    print(Fore.YELLOW + "Applying DWM Tweaks...")
    url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/tweaks/dwm.bat"
    response = requests.get(url)
    
    if response.status_code == 200:
        folder_path = "C:\\GalaxyTweaks\\Tweaks"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, "dwm.bat")

        with open(file_path, "wb") as file:
            file.write(response.content)

        print(Fore.GREEN + "Applied Main Tweaks!")
    else:
        print(Fore.RED + f"Failed to download file. Status code: {response.status_code}")
    pass

@eel.expose
def discord():
    os.system("start https://discord.gg/fpJxa2Gfa3")

if __name__ == '__main__':
    check_for_update()
    rp = os.path.abspath(menu.strip("menu.html"))
    eel.root_path = rp
    eel.init(rp)
    eel.start('menu.html', size=(600, 400))
