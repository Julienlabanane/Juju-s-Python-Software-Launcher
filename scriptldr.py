
# Welcome to scriptldr, scriptldr is a loader for the 451 Launcher
# Please change the App_website, App_Title and Launch_Program when you create a script
# for those don't know ldr = loader
#❗Don't change this when you update 451 launcher❗

# Program init
import logging

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
App_website = "http://www.null-editor.exmple/Test" #enter the link of the game's webpage
App_Title = "Test" #title of the game

# Program Code
def Launch_Program():
    logging.info("Launch" + " " + App_Title)
