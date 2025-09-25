import logging
import os
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
import sys
import time
import xml.etree.ElementTree as ET
App = Tk()
frm = ttk.Frame(App, padding=10)
frm.grid()
logpath = "LOG/"
if not os.path.exists(logpath):
    os.makedirs(logpath)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(logpath + "log of " + time.strftime("%Y-%m-%d_%H-%M-%S") + ".451log"),
        logging.StreamHandler()
    ]
)
if os.path.exists('ETC/451config.xml') is False:
    FNS = "Sorry, your version of 451Launcher unsupport this feature"
    apw = "http://example.com"
    apt = ""
    apss = "260x240"
    WS = "webbrowser"
    MB_txt = "Launch"
    AWB_txt = "'s Website"
    DBGB_txt = "About"
    CB_txt = "Close"
    logging.warning("Configuration file not found, default configuration loaded")
else:
    config_tree = ET.parse('ETC/451config.xml')
    config_root = config_tree.getroot()
    apw = config_root[0][0].text
    apt = config_root[0][1].text
    apss = config_root[0][2].text
    WS = config_root[0][3].text
    LG = config_root[0][4].text
    if os.path.exists('LOCAL/local-' + LG + '.xml'):
        lang_tree = ET.parse('LOCAL/local-' + LG + '.xml')
        lang_root = lang_tree.getroot()
        MB_txt = lang_root[0][1].text
        AWB_txt = lang_root[0][2].text
        DBGB_txt = lang_root[0][3].text
        CB_txt = lang_root[0][4].text
VRD = "25.09.25"
T_Python_V = "3.11.0, 3.12.5, 3.13.0rc2"
T_PyPy_V = "3.10.14"
iaR = False
RT = "BETA"
RN = "Maximus"
PV = RT + "-0.110"
RT = PV + "(" + RT + "," + VRD + "," + "Tested Python Version : " + T_Python_V + "," + "Tested Pypy Version : " + T_PyPy_V + ")"

if WS == 'webbrowser':
    import webbrowser
if WS == 'pywebview':
    import webview
style = ttk.Style()
App.geometry(apss)
App.title("Juju's Python Software Launcher (JPSL)" + " " + ":" + " " + apt)
App.resizable(width=False, height=False)
def lp():
    logging.info("Launch" + " " + apt)
def es():
    exit() 
def dsc():
    messagebox.showinfo(title="About", message=RT)
def wsc():
        if WS == 'webbrowser':
            webbrowser.open_new_tab(apw)
            logging.info("System's browser launch on : " + apw)
        if WS == 'pywebview':
            webview.create_window("App Website", apw)
            webview.start()
            logging.info("Webview's window launch on : " + apw)
        else:
            messagebox.showerror(message=FNS)
def asc():
        webview.create_window("451Connect Panel")
        webview.start()
        logging.info("Webview's window launch on 451Connect Panel")
Title = ttk.Label(frm, text="  " + "JPSL" + "  ", font="Cursive 24", borderwidth=7).grid(column=0, row=0)
MB = ttk.Button(frm, text=MB_txt + " " + apt, width="32", command=lp).grid(column=0, row=1)
AWB = ttk.Button(frm, text=AWB_txt + " " + apt, width="32", command=wsc).grid(column=0, row=2)
DBGB = ttk.Button(frm, text=DBGB_txt, width="32", command=dsc).grid(column=0, row=4)
ACCB = ttk.Button(frm, text="JPSLConnect", width="32", command=asc).grid(column=0, row=5)
CB = ttk.Button(frm, text=CB_txt, width="32", command=es).grid(column=0, row=6)
VL = ttk.Label(frm, text=RN + ' - ' + PV).grid(column=0, row=7)
logging.info("App version: " + RT)
logging.info(sys.version + " " + "Running on" + " " + sys.platform)
App.mainloop()