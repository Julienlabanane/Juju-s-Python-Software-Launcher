
# Program Init
import logging
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
import sys
import time
import xml.etree.ElementTree as ET
App = Tk()
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
Version_release_date = "19/12/24"
Tested_Python_version = "3.11.0, 3.12.5, 3.13.0rc2"
Tested_Pypy_version = "3.10.14"
isaRelease = False
ReleaseType = "BETA"
ReleaseName = "Maximus"
Program_version = ReleaseType + "-0.104"
ReleaseText = Program_version + "(" + ReleaseType + "," + Version_release_date + "," + "Tested Python Version : " + Tested_Python_version + "," + "Tested Pypy Version : " + Tested_Pypy_version + ")"
FNSmessagetext = "Sorry, your version of 451Launcher(" + Program_version + ") unsupport this feature"
App_website = root[0][0].text
App_Title = root[0][1].text
App_screensize = root[0][2].text
App_repo_source = root[0][3].text
websystem = root[0][4].text
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
App.config(background="black") #other setting

# Program Code
logging.info("<style>body {background-color: skyblue;}h3 {font-family: monospace;}</style>") #inject css
def Launch_Program():
    logging.info("Launch" + " " + App_Title)
def exit_scene():
    messagebox.showinfo(title="You are quitting the 451 Launcher", message='Goodbye <3')
    exit()
def src_screen_content():
        if websystem == 'webbrowser':
            webbrowser.open_new_tab(App_repo_source)
            logging.info("System's browser launch on : " + App_website)
        if websystem == 'pywebview':
            webview.create()
            webview.go(App_repo_source)
            logging.info("Webview's window launch on : " + App_website)
def dbg_screen_content():
    messagebox.showinfo(title="About",message=ReleaseText)
def viewlog_screen_content():
    print(logpath)
def website_screen_content():
    if websystem == 'webbrowser':
            webbrowser.open_new_tab(App_website)
            logging.info("System's browser launch on : " + App_website)
    if websystem == 'pywebview':
            webview.create()
            webview.go(App_website)
            logging.info("Webview's window launch on : " + App_website)
Title = Label(text="  " + "451 Launcher" + "  ",font="Terminal 24",relief="groove",background="yellow",borderwidth=7)
Title.pack()
Main_Button = Button(text="Launch" + " " + App_Title,width="24",command=Launch_Program,font="Arial 15",background="blue")
Main_Button.pack()
App_website_Button = Button(text=App_Title + "'s" + " " + "Website", width="24",font="Arial 15",background="blue",command=website_screen_content)
App_website_Button.pack()
SRC_Button = Button(text="Source",width="24",command=src_screen_content,font="Arial 15")
SRC_Button.pack()
DBG_Button = Button(text="About",width="24",command=dbg_screen_content,font="Arial 15")
DBG_Button.pack()
CLRLOG_Button = Button(text="View LOG",width="24",command=viewlog_screen_content,font="Arial 15",background="red")
CLRLOG_Button.pack()
CLOSE_Button = Button(text="Close",width="24",command=exit_scene,font="Arial 15",background="red")
CLOSE_Button.pack()
VER_Label = Label(text=ReleaseName + ' - ' + Program_version,background="black",font="Arial 13",foreground="white")
VER_Label.pack()

# Program Run
logging.info("App version: " + ReleaseText)
logging.info(sys.version + " " + "Running on" + " " + sys.platform)
App.mainloop()