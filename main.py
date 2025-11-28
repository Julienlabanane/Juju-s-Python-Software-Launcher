
# import necessary libraries
import os
import ttkbootstrap as ttk
from tkinter import Tk,messagebox
import sys
from multiprocessing import Process
from FRAME.settings_frame import show_settings_main
from FRAME.market_frame import show_market
from LIB.config_sniffer import *
from LIB.better_command import better_command
os.system('color')
main_window = Tk()
main_frame = ttk.Frame(main_window, padding=10)
main_frame.grid()
main_window.iconbitmap(default='ASSET/ICON/JPSL main.ico')
release_date = "24.11.25"
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
    better_command("Launch " + program_name, "info")
def show_about():
    messagebox.showinfo(title="About", message=release_info)

# Define every UI elements
launch_button = ttk.Button(main_frame,text=button_launch_text + " " + program_name,bootstyle='success',width=24,command=launch_program)
market_button = ttk.Button(main_frame, text=button_market_text, width=24, bootstyle='secondary', command=show_market)
settings_button = ttk.Button(main_frame, text=settings_button_text, width=24,bootstyle='secondary', command=show_settings_main)
version_label = ttk.Label(main_frame, text=release_name + ' - ' + project_version)
separator = ttk.Separator(main_frame)
list_of_programs_listbox = ttk.Treeview(main_frame)
title_label = ttk.Label(main_frame, text="JPSL", font="arial 24")

# Place every UI elements
launch_button.grid(column=2, row=3, pady=0)
market_button.grid(column=1, row=3, pady=0)
settings_button.grid(column=0, row=3, pady=0, padx=0)
version_label.grid(column=2, row=0, padx=140)
separator.grid(column=0, row=2, columnspan=3, pady=10, sticky='ew')
list_of_programs_listbox.grid(column=0, row=1)
title_label.grid(column=0, row=0, padx=50)

# Log startup information
better_command("App version: " + release_info, "info")
better_command(sys.version + " Running on " + sys.platform, "info")

# Start the main loop, like my loop of my life (never ending)
main_window.mainloop()