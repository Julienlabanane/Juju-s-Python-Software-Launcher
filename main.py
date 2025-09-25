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
main_frame.tk.call("source", "AZURE/azure.tcl")
main_frame.tk.call("set_theme", "light")
log_directory = "LOG/"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_directory + "log of " + time.strftime("%Y-%m-%d_%H-%M-%S") + ".log"),
        logging.StreamHandler()
    ]
)
if not os.path.exists('ETC/JPSLconfig.xml'):
    website_url = "http://example.com"
    program_name = ""
    window_size = "320x320"
    button_launch_text = "Launch"
    button_website_text = "'s Website"
    button_about_text = "About"
    logging.warning("Configuration file not found, default configuration loaded")
else:
    config_tree = ET.parse('ETC/JPSLconfig.xml')
    config_root = config_tree.getroot()
    website_url = config_root[0][0].text
    program_name = config_root[0][1].text
    window_size = config_root[0][2].text
    language_code = config_root[0][3].text
    if os.path.exists('LOCAL/local-' + language_code + '.xml'):
        lang_tree = ET.parse('LOCAL/local-' + language_code + '.xml')
        lang_root = lang_tree.getroot()
        localization = lang_root.find('localization')
        button_launch_text = localization.find('button_launch').text
        button_about_text = localization.find('button_about').text
        button_close_text = localization.find('button_close').text
release_date = "25.09.25"
tested_python_versions = "3.11.0, 3.12.5, 3.13.0rc2, 3.13.6"
tested_pypy_version = "3.10.14"
is_a_release = False
release_type = "BETA"
release_name = "Maximus"
project_version = release_type + "-0.111"
release_info = project_version + "(" + release_type + "," + release_date + "," + "Tested Python Version : " + tested_python_versions + "," + "Tested Pypy Version : " + tested_pypy_version + ")"
style = ttk.Style()
main_window.geometry(window_size)
main_window.title("Juju's Python Software Launcher (JPSL) : " + program_name)
main_window.resizable(width=False, height=False)
def launch_program():
    logging.info("Launch " + program_name)
def close_app():
    exit()
def show_about():
    messagebox.showinfo(title="About", message=release_info)
title_label = ttk.Label(main_frame, text="  JPSL  ", font="Cursive 24")
title_label.grid(column=0, row=0)
launch_button = ttk.Button(main_frame, text=button_launch_text + " " + program_name, style='Accent.TButton', width=32, command=launch_program)
launch_button.grid(column=1, row=2, pady=220, padx=15)
about_button = ttk.Button(main_frame, text=button_about_text, width=32, command=show_about)
about_button.grid(column=0, row=2, pady=220, padx=15)
version_label = ttk.Label(main_frame, text=release_name + ' - ' + project_version)
version_label.grid(column=1, row=0)
logging.info("App version: " + release_info)
logging.info(sys.version + " Running on " + sys.platform)
main_window.mainloop()