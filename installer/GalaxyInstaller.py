import tkinter as tk
from tkinter import ttk
import urllib.request
import os

class Installer:
    def __init__(self, master):
        self.master = master
        master.title("GalaxyTweaks Installer")

        self.label = ttk.Label(master, text="Welcome to GalaxyTweaks Installer!", font=('Arial', 14))
        self.label.pack(pady=10)

        self.progressbar = ttk.Progressbar(master, length=300, mode="determinate")
        self.progressbar.pack(pady=10)

        self.button = ttk.Button(master, text="Install", command=self.install)
        self.button.pack(pady=10)

        self.status_label = ttk.Label(master, text="", font=('Arial', 10))
        self.status_label.pack(pady=10)

        self.note_label = ttk.Label(master, text="Note: This installer will download GalaxyTweaks.py to your desktop.", font=('Arial', 9))
        self.note_label.pack(pady=5)

    def install(self):
        self.label.config(text="Downloading GalaxyTweaks...", font=('Arial', 12, 'bold'))
        self.progressbar["value"] = 0
        self.progressbar.start()

        file_url = "https://github.com/riviox/GalaxyTweaks/raw/main/GalaxyTweaks.py"
        self.label.config(text="Downloading dependencies...", font=('Arial', 12, 'bold'))
        os.system("pip install colorama eel requests")
        desktop_location = os.path.expanduser("~/Desktop")

        destination_path = os.path.join(desktop_location, 'GalaxyTweaks.py')
        if os.path.exists(destination_path):
            self.label.config(text="GalaxyTweaks.py already exists on the desktop.", font=('Arial', 12, 'bold'))
            self.progressbar.stop()
        else:
            self.download_and_install(file_url, desktop_location)
            self.label.config(text="Installation complete!", font=('Arial', 12, 'bold'))
            self.progressbar.stop()
            self.status_label.config(text=f'File downloaded to {destination_path}', font=('Arial', 10, 'italic'))

    def download_and_install(self, url, location):
        response = urllib.request.urlopen(url)
        total_size = int(response.headers['Content-Length'])
        chunk_size = 8192  # 8 KB
        downloaded = 0

        with open(os.path.join(location, 'GalaxyTweaks.py'), 'wb') as file:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                file.write(chunk)
                downloaded += len(chunk)
                progress = (downloaded / total_size) * 100
                self.progressbar["value"] = progress
                self.master.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    installer_app = Installer(root)
    root.mainloop()
