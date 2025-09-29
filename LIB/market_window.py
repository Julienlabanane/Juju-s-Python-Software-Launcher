from tkinter import Tk
from tkinter import ttk
from LIB.config_sniffer import *
def show_market():
    market_window = Tk()
    market_window.title(market_window_title_text)
    market_window.geometry("550x550")
    market_window.tk.call("source", "ASSET/AZURE/azure.tcl")
    market_window.tk.call("set_theme", theme_choice)
    ttk.Label(market_window, text=market_placeholder_text).pack(pady=20)
    market_window.mainloop()