
import os
import colorama

os.system("clear" if os.name == "posix" else "cls")

colorama.init(autoreset=True)
print("pythonOS\nv0.0.3a\nLoading..")

import json
import time
import sys

# mf we needed that loading screen, because we are importing a billion things. the pyqt5 imports make this slow so we quickly make a loading screen

from datetime import datetime
from colorama import Fore, Back, Style
from pathlib import Path
from platform import system as usersOS

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QKeySequence

from lupa import LuaRuntime
from playsound import playsound


def update():
    os.system("git pull origin main --quiet")
    match usersOS():
        case 'Darwin': 
            os.system("python3 main.py")

        case 'Windows':
            os.system("py main.py")

        case 'Linux':
            os.system("python main.py")


def getOption(option):
    coolpath = Path("data")
    with open(coolpath / "settings.json", "r") as f:
        data = json.load(f)
        return data.get(option)


os.system("clear" if os.name == "posix" else "cls")
print("pythonOS")
print("v0.0.3a")
if getOption("colors"):
    print(Fore.YELLOW + "Loading..")
else:
    print("Loading..")


def setOption(optionName, option):
    weirdPath = Path("data")
    with open(weirdPath / "settings.json", "r") as f:
        data = json.load(f)
        data[optionName] = option
    with open(weirdPath / "settings.json", "w") as f:
        json.dump(data, f, indent=4)



os.system("clear" if os.name != "nt" else "cls")
while True is not False:
    try:
        match getOption("input-color").lower():
            case "white":

                msg = input(Fore.WHITE + os.getcwd() + " >>> ").lower()
            case "red":
                msg = input(Fore.RED + os.getcwd() + " >>> ").lower()
            case "blue":
                msg = input(Fore.BLUE + os.getcwd() + " >>> ").lower()
            case "yellow":
                msg = input(Fore.YELLOW + os.getcwd() + " >>> ").lower()
            case "green":
                msg = input(Fore.GREEN + os.getcwd() + " >>> ").lower()
            case "magenta":
                msg = input(Fore.MAGENTA + os.getcwd() + " >>> ").lower()
            case _:
                msg = input(os.getcwd() + " >>> ")
        if msg == "time":
            print(datetime.now())
        
        elif msg == "run-lua":
            lua = LuaRuntime()
            os.chdir("scripts")
            for luathing in os.listdir():
                with open(luathing, "r") as f:
                    lua.eval(f.read())
            os.chdir("..")
        



        elif msg.startswith("change"):
            if "--help" in msg.split(" "):
                print(
                    "colors - This affects if you want colored text or not, recommended to turn off incase this causes eyestrains or if your colorblind.\ninput-color - This changes the input color for typing stuff, possible options for this are: red, green, blue, magenta, yellow, white\ngit-installed - Whenever you run the update command, if this option is \"y\" then it won't ask if you have git installed, else it will ask.\nsecurity - This adds a little security features, it's recommended to turn this on, even if you think it does nothing."
                )
            else:
                newoption = None
                if (
                    msg.split(" ")[2].lower() == "false"
                    or msg.split(" ")[2].lower() == "on"
                ):
                    newoption = False
                elif (
                    msg.split(" ")[2].lower() == "true"
                    or msg.split(" ")[2].lower() == "off"
                ):
                    newoption = True
                if getOption(msg.split(" ")[1].lower()) is not None:
                    if msg.split(" ")[1].lower() != "input-color":
                        setOption(msg.split(" ")[1].lower(), newoption)
                        print("Changed option.")
                    else:
                        setOption(msg.split(" ")[1].lower(), msg.split(" ")[2].lower())
                else:
                    print("That is not a valid option.")
                    match msg.split(" ")[1].lower():
                        case "input-color":
                            setOption("input-color", "white")
                        case "colors":
                            setOption("colors", True)
                        case _:
                            pass
        elif msg == "update":
            if getOption("git-installed") == "UNDEFINED" or not getOption("git-installed"):
                if getOption("colors"):
                    print(Fore.RED + "This action requires Git, do you have it installed?")
                else:
                    print("This action requires Git, do you have it installed?")
                confirm = input().lower()
                if confirm == "y":
                    setOption("git-installed", True)
                    update()
                elif confirm == "n":
                    if not getOption("security"):
                        from webbrowser import open_new_tab
                        open_new_tab('https://git-scm.com/downloads')
                    setOption("git-installed", False)
            elif getOption("git-installed"):
                    update()
            

        elif msg == "exit":
            exit()

        elif msg.startswith("pyplay"):
            if "-bg" in msg.split(" "):
                if msg.split(" ")[1].endswith(".wav"):
                    playsound("pyPlay/sounds/"+msg.split(" ")[1], False)
                else:
                    print("Oops, that does not look like a .wav file, perhaps add .wav at the end of the filename or input a wav file instead of something else.")
            else:
                if msg.split(" ")[1].endswith(".wav"):
                    playsound("pyPlay/sounds/"+msg.split(" ")[1])
                else:
                    print("Oops, that does not look like a .wav file, perhaps add .wav at the end of the filename or input a wav file instead of something else.")

        elif msg == "memory":
            from psutil import Process

            curMemory = Process(os.getpid())
            print("Memory in kilobytes: " + str(curMemory.memory_info().rss / 1000))

        elif msg == "browser":

            match usersOS():
                case 'Darwin':
                    os.system("python3 program-files/pyBrowse/pybrowse.py")
                
                case 'Windows':
                    os.system("py program-files/pyBrowse/pybrowse.py")
                
                case 'Linux':
                    os.system("python program-files/pyBrowse/pybrowse.py")

                
        elif bool(msg) is not False:
            print(msg + " is not a command.")


        elif msg.startswith("run-luafile"):
            lua = LuaRuntime()
            os.chdir("scripts")
            for luathing in os.listdir():
                if msg.split(" ")[1] == luathing:
                    with open(msg.split(" ")[1], "r") as f:
                        lua.eval(f.read())
            os.chdir("..")
    except Exception as e:
        if getOption("colors"):
            print(Fore.RED + "Error: " + Fore.WHITE + str(e))
        else:
            print("Error: " + str(e))