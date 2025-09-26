import logging
import os
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
import sys
import time
import xml.etree.ElementTree as ET
main_window = Tk()
main_frame = ttk.Frame(main_window, padding=10)
main_frame.grid()
if os.path.exists("ART/AZURE/azure.tcl"):
    main_frame.tk.call("source", "ART/AZURE/azure.tcl")
    style = ttk.Style()
else:
    style = ttk.Style()
log_directory = "LOG/"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_directory + "log_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".log"),
        logging.StreamHandler()
    ]
)
if not os.path.exists('ETC/JPSLconfig.xml'):
    theme_choice = "light"
    language_code = "en"
    button_launch_text = "Launch"
    button_about_text = "About"
    button_market_text = "Market"
    button_close_text = "Close"
    logging.warning("Configuration file not found, default configuration loaded")
else:
    config_tree = ET.parse('ETC/JPSLconfig.xml')
    config_root = config_tree.getroot()
    language_code = config_root[0][0].text
    theme_choice = config_root[0][1].text
    if os.path.exists('LOCAL/local-' + language_code + '.xml'):
        lang_tree = ET.parse('LOCAL/local-' + language_code + '.xml')
        lang_root = lang_tree.getroot()
        localization = lang_root.find('localization')
        button_launch_text = localization.find('button_launch').text
        button_about_text = localization.find('button_about').text
        button_market_text = localization.find('button_market').text
        button_close_text = localization.find('button_close').text
    else:
        button_launch_text = "Launch"
        button_about_text = "About"
        button_market_text = "Market"
        button_close_text = "Close"
try:
    main_frame.tk.call("set_theme", theme_choice)
except Exception:
    logging.warning("Azure theme not available, using default")
release_date = "26.09.25"
tested_python_versions = "3.11.0, 3.12.5, 3.13.0rc2, 3.13.6"
tested_pypy_version = "3.10.14"
is_a_release = False
release_type = "BETA"
release_name = "Maximus"
project_version = release_type + "-0.112"
release_info = (
    project_version
    + " (" + release_type
    + ", " + release_date
    + ", Tested Python Version : " + tested_python_versions
    + ", Tested Pypy Version : " + tested_pypy_version + ")"
)
window_size = "720x480"
program_name = ""
main_window.geometry(window_size)
main_window.title("Juju's Python Software Launcher (JPSL) : " + program_name)
main_window.resizable(width=False, height=False)
def launch_program():
    logging.info("Launch " + program_name)
def close_app():
    logging.info("Close application")
    main_window.destroy()
def show_about():
    messagebox.showinfo(title="About", message=release_info)
def show_market():
    market_window = Tk()
    market_window.title("Market")
    market_window.geometry("550x550")
    ttk.Label(market_window, text="Market Placeholder").pack(pady=20)
    market_window.mainloop()
launch_button = ttk.Button(
    main_frame,
    text=button_launch_text + " " + program_name,
    style='Accent.TButton',
    width=24,
    command=launch_program
)
market_button = ttk.Button(main_frame, text=button_market_text, width=24, command=show_market)
version_label = ttk.Label(main_frame, text=release_name + ' - ' + project_version)
title_label = ttk.Label(main_frame, text="JPSL", font="arial 24")
title_label.grid(column=0, row=0, padx=50)
launch_button.grid(column=2, row=2, pady=390)
market_button.grid(column=1, row=2, pady=390)
version_label.grid(column=2, row=0, padx=120)
logging.info("App version: " + release_info)
logging.info(sys.version + " Running on " + sys.platform)
main_window.mainloop()