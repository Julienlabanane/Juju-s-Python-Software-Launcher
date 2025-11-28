import os
import tempfile
import requests
import platform
from tkinter import Tk, scrolledtext, messagebox
import ttkbootstrap as ttk
from LIB.config_sniffer import *
from LIB.better_command import *
BACKEND_URL = "https://www.amazon.fr/"
project_version = "BETA-0.113"
headers = {
    "User-Agent": "JPSL/" + project_version + " (" + platform.system() + " " + platform.release() + "; " + platform.architecture()[0] + ";" + " Python " + platform.python_version() + ")"
}

# Function to download XML and save to temp file
def download_xml_to_temp():
    try:
        response = requests.get(BACKEND_URL, headers=headers)
        response.raise_for_status()
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "index.xml")
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        return temp_path
    except requests.exceptions.RequestException as e:
        better_command(f"Error downloading XML: {e}", "error")
        messagebox.showerror("Connection Error", f"{e}")
        return None
def show_market():
    market_window = Tk()
    market_window.title(market_window_title_text)
    market_window.geometry("550x550")
    ttk.Label(market_window, text=market_placeholder_text, font=("Segoe UI", 12)).pack(pady=10)
    text_box = scrolledtext.ScrolledText(market_window, wrap="word", width=60, height=25)
    text_box.pack(padx=10, pady=10)
    temp_file_path = {"path": None}
    def fetch_and_display():
        temp_path = download_xml_to_temp()
        if temp_path:
            temp_file_path["path"] = temp_path
            with open(temp_path, "r", encoding="utf-8") as f:
                xml_data = f.read()
            text_box.delete(1.0, "end")
            text_box.insert("end", xml_data)
    fetch_and_display()
    def on_close():
        if temp_file_path["path"] and os.path.exists(temp_file_path["path"]):
            try:
                os.remove(temp_file_path["path"])
                print(f"Deleted temp file: {temp_file_path['path']}")
            except Exception as e:
                print(f"Could not delete temp file: {e}")
        market_window.destroy()
    market_window.protocol("WM_DELETE_WINDOW", on_close)
    market_window.mainloop()
if __name__ == "__main__":
    show_market()