from tkinter import Tk
from tkinter import ttk
from LIB.config_sniffer import *
def show_market():
    market_window = Tk()
    market_window.title("Market")
    market_window.geometry("550x550")
    market_window.tk.call("source", "ART/AZURE/azure.tcl")
    market_window.tk.call("set_theme", theme_choice)
    ttk.Label(market_window, text="Market Placeholder").pack(pady=20)
    market_window.mainloop()