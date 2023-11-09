import subprocess
import sys
import os

installermdls = ['colorama==0.4.4', 'requests']

for module in installermdls:
    try:
        __import__(module)
    except ImportError:
        print(f"installing {module}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
        os.system("cls")

from colorama import Fore, init
import requests
required_modules = ['ctype', 'requests', 'colorama==0.4.4']

adj = (" " * 20)

def prtlogo():
    init(autoreset=True)
    logo = f"""{Fore.RED}

{adj}  ▄████  ▄▄▄       ██▓    ▄▄▄      ▒██   ██▒▓██   ██▓     █████▒██▓███    ██████ 
{adj} ██▒ ▀█▒▒████▄    ▓██▒   ▒████▄    ▒▒ █ █ ▒░ ▒██  ██▒   ▓██   ▒▓██░  ██▒▒██    ▒ 
{adj}▒██░▄▄▄░▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ░░  █   ░  ▒██ ██░   ▒████ ░▓██░ ██▓▒░ ▓██▄   
{adj}░▓█  ██▓░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██  ░ █ █ ▒   ░ ▐██▓░   ░▓█▒  ░▒██▄█▓▒ ▒  ▒   ██▒
{adj}░▒▓███▀▒ ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒ ▒██▒  ░ ██▒▓░   ░▒█░   ▒██▒ ░  ░▒██████▒▒
{adj} ░▒   ▒  ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░▒▒ ░ ░▓ ░   ██▒▒▒     ▒ ░   ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░
{adj}  ░   ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░░   ░▒ ░ ▓██ ░▒░     ░     ░▒ ░     ░ ░▒  ░ ░
{adj}░ ░   ░   ░   ▒     ░ ░    ░   ▒    ░    ░   ▒ ▒ ░░      ░ ░   ░░       ░  ░  ░  
{adj}      ░       ░  ░    ░  ░     ░  ░ ░    ░   ░ ░                              ░  
{adj}                                             ░ ░      """
    print(logo)
prtlogo()
print(Fore.BLUE + "Installing GalaxyFPS...")
print(Fore.YELLOW + "Installing modules...")
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"installing {module}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
        os.system("cls")
location = input(Fore.BLUE + "Location to install (Desktop): " + Fore.GREEN)

if location.strip() == "":
    desktop_path = os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"))
else:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", location.strip())

print(Fore.GREEN + f"Installing GalaxyFPS to: {desktop_path}")

galaxyfps_url = "https://raw.githubusercontent.com/RivioxGaming/GalaxyFPS/main/GalaxyFPS.py"
response = requests.get(galaxyfps_url)

if response.status_code == 200:
    with open(os.path.join(desktop_path, "GalaxyFPS.py"), "wb") as f:
        f.write(response.content)
    print(Fore.GREEN + f"GalaxyFPS.py downloaded successfully to {desktop_path}!")
else:
    print(Fore.RED + f"Failed to download GalaxyFPS.py. Status code: {response.status_code}")