import os
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
import sys
import time
from LIB.settings_window import show_settings
from LIB.market_window import show_market
from LIB.config_sniffer import *
os.system('color')
main_window = Tk()
main_frame = ttk.Frame(main_window, padding=10)
main_frame.grid()
if os.path.exists("ASSET/AZURE/azure.tcl"):
    main_frame.tk.call("source", "ASSET/AZURE/azure.tcl")
    style = ttk.Style()
else:
    style = ttk.Style()
try:
    main_frame.tk.call("set_theme", theme_choice)
except Exception:
    print("Azure theme not available, using default")
release_date = "26.09.25"
tested_python_versions = "3.11.0, 3.12.5, 3.13.0rc2, 3.13.6"
tested_pypy_version = "3.10.14"
is_a_release = False
release_type = "BETA"
release_name = "Maximus"
project_version = release_type + "-0.113"
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
    print("Launch " + program_name)
def show_about():
    messagebox.showinfo(title="About", message=release_info)
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
settings_button = ttk.Button(main_frame, text=settings_button_text, width=24, command=show_settings)
title_label.grid(column=0, row=0, padx=50)
launch_button.grid(column=2, row=2, pady=390)
market_button.grid(column=1, row=2, pady=390)
settings_button.grid(column=0, row=2, pady=390, padx=10)
version_label.grid(column=2, row=0, padx=120)
print("App version: " + release_info)
print(sys.version + " Running on " + sys.platform)
main_window.mainloop()