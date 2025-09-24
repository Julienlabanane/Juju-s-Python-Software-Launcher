
# Program Init
import logging
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
import sys
import time
import xml.etree.ElementTree as ET
#import http
App = Tk()
frm = ttk.Frame(App, padding=10)
frm.grid()
style = ttk.Style()
logpath = "LOG/"
logging.basicConfig(
    level=logging.INFO,
    format="<h3>%(asctime)s [%(levelname)s] %(message)s</h3>",
    handlers=[
        logging.FileHandler(logpath + "log of " + time.strftime("%Y-%m-%d_%H-%M-%S") + ".htm"),
        logging.StreamHandler()
    ]
)
tree = ET.parse('451config.xml')
root = tree.getroot()

# Program info
Version_release_date = "10.01.25"
Tested_Python_version = "3.11.0, 3.12.5, 3.13.0rc2"
Tested_Pypy_version = "3.10.14"
isaRelease = False
ReleaseType = "BETA"
ReleaseName = "Maximus"
Program_version = ReleaseType + "-0.107"
ReleaseText = Program_version + "(" + ReleaseType + "," + Version_release_date + "," + "Tested Python Version : " + Tested_Python_version + "," + "Tested Pypy Version : " + Tested_Pypy_version + ")"
FNSmessagetext = "Sorry, your version of 451Launcher(" + Program_version + ") unsupport this feature"
App_website = root[0][0].text
App_Title = root[0][1].text
App_screensize = root[0][2].text
websystem = root[0][3].text
if websystem == 'webbrowser':
    import webbrowser
if websystem == 'pywebview':
    import webview

# By
#            /|       ----------       /|              ----------       ----------       |          |       |----------       |       |----------|
#           / |       |               / |              |                     |           |          |       |          \      |       |          |
#          /  |       |              /  |              |                     |           |          |       |           \             |          |
#         /   |       |             /   |              |                     |           |          |       |            \    |       |          |
#        /    |       ----------   /    |              ----------            |           |          |       |             |   |       |          |
#       /-----|--               |       |                       |            |           |          |       |            /    |       |          |
#             |                 |       |                       |            |           |          |       |           /     |       |          |
#             |                 |       |                       |            |           |          |       |          /      |       |          |
#             |       ----------        |              ----------            |           |----------|       |----------       |       |----------|

# Program Config
App.geometry(App_screensize) #size of the launcher
App.title("451 Launcher" + " " + ":" + " " + App_Title) #title of the launcher
App.resizable(width=False,height=False) #if the window is resizable

# Program Code
logging.info("<style>body {background-color: skyblue;}h3 {font-family: monospace;}</style>") #inject css
def Launch_Program():
    logging.info("Launch" + " " + App_Title)
def exit_scene():
    messagebox.showinfo(title="You are quitting the 451 Launcher", message='Goodbye <3')
    exit()
def dbg_screen_content():
    messagebox.showinfo(title="About",message=ReleaseText)
def website_screen_content():
        if websystem == 'webbrowser':
            webbrowser.open_new_tab(App_website)
            logging.info("System's browser launch on : " + App_website)
        if websystem == 'pywebview':
            webview.create()
            webview.go(App_website)
            logging.info("Webview's window launch on : " + App_website)
def accountconnect_screen_content():
        messagebox.showerror(title="451 Connect is comming soon",message=FNSmessagetext)
Title = ttk.Label(frm,text="  " + "451 Launcher" + "  ",font="Arial 24",borderwidth=7).grid(column=0, row=0)
Main_Button = ttk.Button(frm,text="Launch" + " " + App_Title,width="32",command=Launch_Program).grid(column=0, row=1)
App_website_Button = ttk.Button(frm,text=App_Title + "'s" + " " + "Website", width="32",command=website_screen_content).grid(column=0, row=2)
DBG_Button = ttk.Button(frm,text="About",width="32",command=dbg_screen_content).grid(column=0, row=4)
ACC_Button = ttk.Button(frm,text="451Connect",width="32",command=accountconnect_screen_content).grid(column=0, row=5)
CLOSE_Button = ttk.Button(frm,text="Close",width="32",command=exit_scene).grid(column=0, row=6)
VER_Label = ttk.Label(frm,text=ReleaseName + ' - ' + Program_version).grid(column=0, row=7)

# Program Run
logging.info("App version: " + ReleaseText)
logging.info(sys.version + " " + "Running on" + " " + sys.platform)
App.mainloop()