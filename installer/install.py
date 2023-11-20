import os
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tqdm
import shutil
from pathlib import Path

class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Installer")
        self.root.geometry("400x150")

        self.urls = [
            "https://github.com/RivioxGaming/GalaxyTweaks/raw/main/GalaxyTweaks.py",
            "https://github.com/RivioxGaming/GalaxyTweaks/raw/main/GalaxyTweaks.lnk"
        ]

        self.url_label = Label(root, text="Installer URLs:")
        self.url_label.pack(pady=5)

        self.url_text = Text(root, height=5, width=40)
        self.url_text.insert(END, "\n".join(self.urls))
        self.url_text.pack(pady=5)

        self.install_button = Button(root, text="Install", command=self.install_app)
        self.install_button.pack(pady=10)

    def download_file(self, url, save_path):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading')

        with open(save_path, 'wb') as file, progress_bar:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

    def install_app(self):
        urls = self.url_text.get("1.0", "end-1c").split("\n")

        for url in urls:
            url = url.strip()
            if not url:
                continue

            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error connecting to URL {url}:\n{e}")
                return

            save_path = os.path.basename(url)

            try:
                self.download_file(url, save_path)
                messagebox.showinfo("Success", f"Download of {save_path} completed successfully.")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error downloading {save_path}:\n{e}")
                return

            if "GalaxyTweaks.py" in url:
                install_location = "C:/GalaxyTweaks/GalaxyTweaks.py"
                Path("C:/GalaxyTweaks").mkdir(parents=True, exist_ok=True)
                shutil.move(save_path, install_location)
                messagebox.showinfo("Success", f"Installed {os.path.basename(url)} to {install_location}")
            elif "GalaxyTweaks.lnk" in url:
                install_location = os.path.join(os.path.expanduser("~"), "Desktop", os.path.basename(url))
                shutil.move(save_path, install_location)
                messagebox.showinfo("Success", f"Installed {os.path.basename(url)} to {install_location}")

        # Add additional installation steps here if needed

        messagebox.showinfo("Success", "Installation completed successfully.")

if __name__ == "__main__":
    root = Tk()
    app = InstallerApp(root)
    root.mainloop()
