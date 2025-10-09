import time
class better_command():
    yellow_warning = '\033[33m'
    error_warning = '\033[91m'
    succes = '\033[32m'
    base = '\033[0m'
    libname = "Juju's Python Better Command"
    libver = '1'
    def hello():
        print(better_command.yellow_warning + "◼" + better_command.error_warning + "◼" + better_command.succes + "◼" + better_command.base + "  " + better_command.libname + " v" + better_command.libver)
    def error():
        print(better_command.error_warning + time.asctime())
    def warning():
        print(better_command.error_warning + "[" + time.asctime() + "] --> ")
better_command.hello()