import logging
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
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(logpath + "log of " + time.strftime("%Y-%m-%d_%H-%M-%S") + ".451log"),
        logging.StreamHandler()
    ]
)
tree = ET.parse('451config.xml')
root = tree.getroot()
VRD = "15.01.25"
T_Python_V = "3.11.0, 3.12.5, 3.13.0rc2"
T_PyPy_V = "3.10.14"
iaR = False
RT = "BETA"
RN = "Maximus"
PV = RT + "-0.110"
RT = PV + "(" + RT + "," + VRD + "," + "Tested Python Version : " + T_Python_V + "," + "Tested Pypy Version : " + T_PyPy_V + ")"
FNS = root[0][4].text
apw = root[0][0].text
apt = root[0][1].text
apss = root[0][2].text
WS = root[0][3].text
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
MB_txt = root[0][5].text
MB = ttk.Button(frm, text=MB_txt + " " + apt, width="32", command=lp).grid(column=0, row=1)
AWB_txt = root[0][6].text
AWB = ttk.Button(frm, text=apt + AWB_txt, width="32", command=wsc).grid(column=0, row=2)
DBGB_txt = root[0][7].text
DBGB = ttk.Button(frm, text=DBGB_txt, width="32", command=dsc).grid(column=0, row=4)
ACCB = ttk.Button(frm, text="JPSLConnect", width="32", command=asc).grid(column=0, row=5)
CB_txt = root[0][8].text
CB = ttk.Button(frm, text=CB_txt, width="32", command=es).grid(column=0, row=6)
VL = ttk.Label(frm, text=RN + ' - ' + PV).grid(column=0, row=7)
logging.info("App version: " + RT)
logging.info(sys.version + " " + "Running on" + " " + sys.platform)
App.mainloop()