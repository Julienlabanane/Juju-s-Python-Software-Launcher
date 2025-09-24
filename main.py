
# Program Init
import logging
from scriptldr import *
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
import sys
import time
import webbrowser
App = Tk()
logpath = "LOG/"
logging.basicConfig(
    level=logging.INFO,
    format="<h3>%(asctime)s [%(levelname)s] %(message)s<h3>",
    handlers=[
        logging.FileHandler(logpath + "log of " + time.strftime("%Y-%m-%d_%H-%M-%S") + ".htm"),
        logging.StreamHandler()
    ]
)

# Program info
Version_release_date = "02/12/24"
Tested_Python_version = "3.11.0, 3.12.5, 3.13.0rc2"
Tested_Pypy_version = "3.10.14"
isaRelease = False
ReleaseType = "BETA"
ReleaseName = "Maximus"
Program_version = ReleaseType + "-0.102"
ReleaseText = Program_version + "(" + ReleaseType + "," + Version_release_date + "," + "Tested Python Version : " + Tested_Python_version + "," + "Tested Pypy Version : " + Tested_Pypy_version + ")"
DevMSG = "❤❤❤Thank you for read my code. Read the code is like this program, fork the code is love this program❤❤❤"
FNSmessagetext = "Sorry, your version of 451Launcher(" + Program_version + ") unsupport this feature"
App_repo_source = "x"

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
App.geometry("480x360") #size of the launcher
App.title("451 Launcher" + " " + ":" + " " + App_Title) #title of the launcher
App.resizable(width=False,height=False) #if the window is resizable
App.config(background="black") #other setting

# Program Code
def src_screen_content():
    messagebox.showinfo(title="Source",message=DevMSG)
    webbrowser.open_new_tab(App_repo_source)
def dbg_screen_content():
    messagebox.showinfo(title="About",message=ReleaseText)
def viewlog_screen_content():
    print(logpath)
def website_screen_content():
    webbrowser.open_new_tab(App_website)
Title = Label(text="  " + "451 Launcher" + "  ",font="Terminal 24",relief="groove",background="yellow",borderwidth=7)
Title.pack()
Main_Button = Button(text="Launch" + " " + App_Title,width="11",command=Launch_Program,font="Arial 18",background="blue")
Main_Button.pack()
App_website_Button = Button(text=App_Title + "'s" + " " + "Website", width="11",font="Arial 18",background="blue",command=website_screen_content)
App_website_Button.pack()
SRC_Button = Button(text="Source",width="11",command=src_screen_content,font="Arial 18")
SRC_Button.pack()
DBG_Button = Button(text="About",width="11",command=dbg_screen_content,font="Arial 18")
DBG_Button.pack()
CLRLOG_Button = Button(text="View LOG",width="11",command=viewlog_screen_content,font="Arial 18",background="red")
CLRLOG_Button.pack()
CLOSE_Button = Button(text="Close",width="11",command=exit,font="Arial 18",background="red")
CLOSE_Button.pack()
VER_Label = Label(text=ReleaseName + ' - ' + Program_version,background="black",font="Arial 13",foreground="white")
VER_Label.pack()

# Program Run
print("            /|       ----------       /|              ----------       ----------       |          |       |----------       |       |----------|")
print("           / |       |               / |              |                     |           |          |       |          \      |       |          |")
print("          /  |       |              /  |              |                     |           |          |       |           \             |          |")
print("         /   |       |             /   |              |                     |           |          |       |            \    |       |          |")
print("        /    |       ----------   /    |              ----------            |           |          |       |             |   |       |          |")
print("       /-----|--               |       |                       |            |           |          |       |            /    |       |          |")
print("             |                 |       |                       |            |           |          |       |           /     |       |          |")
print("             |                 |       |                       |            |           |          |       |          /      |       |          |")
print("             |       ----------        |              ----------            |           |----------|       |----------       |       |----------|")
logging.info("App version: " + ReleaseText)
logging.info(sys.version + " " + "Running on" + " " + sys.platform)
App.mainloop()