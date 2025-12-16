
# import necessary libraries
import os
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
import sys
from multiprocessing import Process
from FRAME.settings_frame import show_settings_main
from FRAME.market_frame import show_market
from LIB.tempfolder_scheduler import TempFolder
from LIB.config_sniffer import *
from LIB.better_command import better_command
if not os.path.exists(TempFolder._path + "\cert.firstrun"):
    better_command("is probally firstrun (or user delete cert.firstrun file in the TEMP folder)", "info")
    main_window = tk.Tk()
    main_frame = ttk.Frame(main_window, padding=10)
    main_frame.grid()
    main_window.iconbitmap(default='ASSET/ICON/JPSL main.ico')
    main_window.title("Juju's Python Software Launcher (JPSL) : First run")
    show_settings_main()
    TempFolder.put("cert.firstrun", "")
    main_window.mainloop()
else:
    os.system('color')
    main_window = tk.Tk()
    main_frame = ttk.Frame(main_window, padding=10)
    main_frame.grid()
    main_window.iconbitmap(default='ASSET/ICON/JPSL main.ico')
    release_date = "01.12.25"
    is_a_release = False
    release_type = "BETA"
    release_name = "Maximus"
    project_version = release_type + "-0.113"
    release_info = (project_version+ " (" + release_type + ", " + release_date + ")")
    window_size = "780x400"
    program_name = ""
    main_window.geometry(window_size)
    main_window.title("Juju's Python Software Launcher (JPSL) : " + program_name)
    def launch_program():
        better_command("Launch " + program_name, "info")
    def show_about():
        messagebox.showinfo(title="About", message=release_info)

    # Define every UI elements
    launch_button = ttk.Button(main_frame, text=button_launch_text + " " + program_name,bootstyle='success',width=24,command=launch_program)
    market_button = ttk.Button(main_frame, text=button_market_text, width=24, bootstyle='secondary', command=show_market)
    settings_button = ttk.Button(main_frame, text=settings_button_text, width=24,bootstyle='secondary', command=show_settings_main)
    version_label = ttk.Label(main_frame, text=release_name + ' - ' + project_version)
    separator = ttk.Separator(main_frame)
    list_of_programs_listbox = ttk.Treeview(main_frame)
    photo = tk.PhotoImage(file="ASSET/ICON/JPSL main min.png", master=main_window)
    title_label = ttk.Label(main_frame, image=photo)
    title_label.image = photo

    # Place every UI elements
    launch_button.grid(column=2, row=3, pady=0)
    market_button.grid(column=1, row=3, pady=0)
    settings_button.grid(column=0, row=3, pady=0, padx=0)
    version_label.grid(column=2, row=0, padx=140)
    separator.grid(column=0, row=2, columnspan=3, pady=10, padx=0, sticky='ew')
    list_of_programs_listbox.grid(column=0, row=1)
    title_label.grid(column=0, row=0, padx=50)

    # Log startup information
    better_command("App version: " + release_info, "info")
    better_command(sys.version + " Running on " + sys.platform, "info")

    # Start the main loop
    main_window.mainloop()