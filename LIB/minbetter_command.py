from datetime import *
def min_better_command(txt, context):
    yellow_warning = '\033[33m'
    error_warning = '\033[91m'
    succes = '\033[32m'
    base = '\033[0m'
    libname = "Juju's Python Minimal Better Command"
    libver = '1'
    entry_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")
    if context == "error":
        print(error_warning + "[" + entry_time + "] → " + txt)
    if context == "warning":
        print(yellow_warning + "[" + entry_time + "] → " + txt)
    if context == "success":
        print(succes + "[" + entry_time + "] → " + txt)
    if context == "info":
        print(base + "[" + entry_time + "] → " + txt)
