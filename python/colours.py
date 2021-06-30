import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLACK + "This is black!")
print(style.RED + "This is red!")
print(style.GREEN + "This is green!")
print(style.YELLOW + "This is yellow!")
print(style.BLUE + "This is blue!")
print(style.MAGENTA + "This is magenta!")
print(style.CYAN + "This is cyan!")
print(style.WHITE + "This is white!")
print(style.RESET + style.UNDERLINE + "This is underlined!")
print(style.RESET + "This is none!")

input("")
