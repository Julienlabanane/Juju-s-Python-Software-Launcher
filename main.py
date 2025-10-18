import os
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
import sys
import time
from LIB.settings_window import show_settings_main
from LIB.market_window import show_market
from LIB.config_sniffer import *
from LIB.better_command import better_command
os.system('color')
main_window = Tk()
main_frame = ttk.Frame(main_window, padding=10)
main_frame.grid()
main_window.iconbitmap(default='ASSET/ICON/JPSL main.ico')
if os.path.exists("ASSET/AZURE/azure.tcl"):
    main_frame.tk.call("source", "ASSET/AZURE/azure.tcl")
    style = ttk.Style()
else:
    style = ttk.Style()
try:
    main_frame.tk.call("set_theme", theme_choice)
except Exception:
    print("Azure theme not available, using default")
release_date = "13.10.25"
tested_python_versions = "3.11.0, 3.12.5, 3.13.0rc2, 3.13.6"
tested_pypy_version = "3.10.14"
is_a_release = False
release_type = "BETA"
release_name = "Maximus"
project_version = release_type + "-0.113"
release_info = (project_version+ " (" + release_type + ", " + release_date + ", Tested Python Version : " + tested_python_versions + ", Tested Pypy Version : " + tested_pypy_version + ")")
window_size = "780x400"
program_name = ""
main_window.geometry(window_size)
main_window.title("Juju's Python Software Launcher (JPSL) : " + program_name)
def launch_program():
    print("Launch " + program_name)
def show_about():
    messagebox.showinfo(title="About", message=release_info)
launch_button = ttk.Button(main_frame,text=button_launch_text + " " + program_name,style='Accent.TButton',width=24,command=launch_program)
market_button = ttk.Button(main_frame, text=button_market_text, width=24, command=show_market)
version_label = ttk.Label(main_frame, text=release_name + ' - ' + project_version)
separator = ttk.Separator(main_frame)
list_of_programs_listbox = ttk.Treeview(main_frame)
title_label = ttk.Label(main_frame, text="JPSL", font="arial 24")
settings_button = ttk.Button(main_frame, text=settings_button_text, width=24, command=show_settings_main)
version_label.grid(column=2, row=0, padx=140)
title_label.grid(column=0, row=0, padx=50)
list_of_programs_listbox.grid(column=0, row=1)
separator.grid(column=0, row=2, columnspan=3, pady=10, sticky='ew')
launch_button.grid(column=2, row=3, pady=0)
market_button.grid(column=1, row=3, pady=0)
settings_button.grid(column=0, row=3, pady=0, padx=0)
print("App version: " + release_info)
print(sys.version + " Running on " + sys.platform)
main_window.mainloop()