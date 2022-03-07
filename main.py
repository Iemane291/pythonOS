
import os
import colorama

if os.name == 'nt':
<<<<<<< HEAD
    os.system("title pythonOS")
=======
    os.system('title pythonOS')
>>>>>>> 5380bbc934937aa06d2d698af8cb73a9015a8e46
os.system("clear" if os.name == "posix" else "cls")

colorama.init(autoreset=True)
print("""     _   _                  ____   _____ 
             | | | |                / __ \ / ____|
  _ __  _   _| |_| |__   ___  _ __ | |  | | (___  
 | '_ \| | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
 | |_) | |_| | |_| | | | (_) | | | | |__| |____) |
 | .__/ \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
 | |     __/ |                                    
 |_|    |___/                                     
""")
print("v0.0.5a")
print("Loading..")

import json
import sys
import inquirer
import urllib.request
# mf we needed that loading screen, because we are importing a billion things. the pyqt5 imports make this slow so we quickly make a loading screen

from datetime import datetime
from colorama import Fore, Back, Style
from pathlib import Path
from platform import system as usersOS

from lupa import LuaRuntime
from playsound import playsound
from webbrowser import open_new_tab as openNewTab
from rich.markdown import Markdown

from rich.console import Console
from rich import print as richPrint

console = Console()

def reloadOS():
    os.execl(sys.executable, sys.executable, *sys.argv)


def update():
    os.system("git pull origin main --quiet")


def getOption(option):
    coolpath = Path("data")
    with open(coolpath / "settings.json", "r") as f:
        data = json.load(f)
        if data.get(option) == "on": return True
        elif data.get(option) == "off": return False
        else: return data.get(option)



os.system("clear" if os.name == "posix" else "cls")
print("""     _   _                  ____   _____ 
             | | | |                / __ \ / ____|
  _ __  _   _| |_| |__   ___  _ __ | |  | | (___  
 | '_ \| | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
 | |_) | |_| | |_| | | | (_) | | | | |__| |____) |
 | .__/ \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
 | |     __/ |                                    
 |_|    |___/                                                                      
""")
print("v0.0.5a")
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


killMe = os.getcwd()
if getOption("security"):
    killMe = "dir@user"



os.system("clear" if os.name != "nt" else "cls")
while True is not False:
    try:
        match getOption("input-color").lower():
            case "white":

                msg = input(Fore.WHITE + killMe + " >>> ")
            case "red":
                msg = input(Fore.RED + killMe + " >>> ")
            case "blue":
                msg = input(Fore.BLUE + killMe + " >>> ")
            case "yellow":
                msg = input(Fore.YELLOW +  killMe + " >>> ")
            case "green":
                msg = input(Fore.GREEN + killMe + " >>> ")
            case "magenta":
                msg = input(Fore.MAGENTA + killMe + " >>> ")
            case _:
                msg = input(os.getcwd() + " >>> ")
        if msg.lower() == "time":
            print(datetime.now())
        
        elif msg.lower().startswith("edit "):
            try:
                if getOption("error-warning"):
                    if getOption("colors"):
                        richPrint("[yellow]WARNING: Editing system variables may result in an error or a crash, if one occurs immediately close pythonOS. use this at your own risk.[/yellow]")
                    else:
                        print("WARNING: Editing system variables may result in an error, use this at your own risk.")
                if msg.split(' ')[1] in globals():
                    print("What is the type of the value? ")
                    if not getOption("colors"):
                        print("[0] Number\n[1] Text/String")
                    elif getOption("colors"):
                        richPrint("[blue][0][/blue] - Number")
                        richPrint("[blue][1][/blue] - Text/String")
                    chosentype = int(input())
                    if type(chosentype) is int:
                        match chosentype:
                            case 0:
                                newValue = int(input(f"What do you want to edit {msg.split(' ')[1]} to? "))
                            case 1:
                                newValue = input(f"What do you want to edit {msg.split(' ')[1]} to? ")
                            case _:
                                print("That is a not valid number!")
                    globals()[msg.split(" ")[1]] =  newValue
                else:
                    raise ValueError(f"could not find \"{msg.split(' ')[1]}\"")
            except Exception as e:
                print(str(e))

        elif msg.lower().startswith("mkdir"):
            try:
                os.mkdir(msg.split(" ")[1])
            except FileExistsError:
                if getOption("colors"):
                    richPrint("[bold red]Error: [/bold red]That directory already exists.")
                else:
                    print("Error: That directory already exists.")
        
        elif msg.lower() == "run-lua":
            lua = LuaRuntime()
            weirdPath = Path("scripts")
            if len(os.listdir("scripts")) > 1:
                for luaFile in os.listdir("scripts"):
                    if luaFile.endswith(".lua"):
                        with open(weirdPath / luaFile, "r") as f:
                            lua.eval(f.read())
            else:
                print("Seems that you have no Lua scripts. Please add one in the \"scripts\" folder.")
        

        elif msg.lower() == "readme":
            if getOption("colors"):
                with open("README.md", "r") as mdFile:
                    textRead = Markdown(mdFile.read())
                console.print(textRead)


        elif msg.lower().startswith("change"):
            if "--help" in msg.split(" "):
                print(
                    "colors - This affects if you want colored text or not, recommended to turn off incase this causes eyestrains or if your colorblind.\ninput-color - This changes the input color for typing stuff, possible options for this are: red, green, blue, magenta, yellow, white\ngit-installed - Whenever you run the update command, if this option is \"y\" then it won't ask if you have git installed, else it will ask.\nsecurity - This adds a little security features, it's recommended to turn this on, even if you think it does nothing."
                )
            else:
                newoption = None
                if (
                    msg.split(" ")[2].lower() == "false"
                    or msg.split(" ")[2].lower() == "off"
                ):
                    newoption = False
                elif (
                    msg.split(" ")[2].lower() == "true"
                    or msg.split(" ")[2].lower() == "on"
                ):
                    newoption = True
                if getOption(msg.split(" ")[1].lower()) is not None:
                    if msg.split(" ")[1].lower() != "input-color":
                        setOption(msg.split(" ")[1].lower(), newoption)
                        print("Changed option.")
                    else:
                        setOption(msg.split(" ")[1].lower(), msg.split(" ")[2].lower())
                else:
                    print("That is not an existing option, please read the settings.json or do \"change --help\" to see what options you can change.")
                    match msg.split(" ")[1].lower():
                        case "input-color":
                            setOption("input-color", "white")
                        case "colors":
                            setOption("colors", True)
                        case _:
                            pass
        elif msg.lower() == "update":
            if getOption("git-installed") == "UNDEFINED" or not getOption("git-installed"):
                if getOption("colors"):
                    print(Fore.RED + "This action requires Git, do you have it installed?")
                else:
                    print("This action requires Git, do you have it installed?")
                confirm = input().lower()
                if confirm == "y":
                    setOption("git-installed", True)
                    update()
                    reloadOS()
                elif confirm == "n":
                    if not getOption("security"):
                        openNewTab('https://git-scm.com/downloads')
                    setOption("git-installed", False)
            elif getOption("git-installed"):
                    update()
                    reloadOS()
            

        elif msg.lower() == "exit":
            break

        elif msg.lower() == "privacy":
            print(f"We keep all of your private information unused, we don't use them at all. You can even check the code right now.\n\nAll we use is multiple libraries, Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} and that is it.\n\nIf you still do not feel secure/safe using this, turn on the security option. ")

        elif msg.lower() == "pyplay":
            soundList = []
            for i in os.listdir('pyPlay/sounds'):
                if i != "readme.txt" or i.endswith(".wav") or i.endswith(".mp3"):
                    soundList.append(i)
            if len(soundList) < 1:
                print("You do not have any sounds/songs to play.")
            else:
                if getOption("colors"):
                    soundChose = inquirer.prompt([
                        inquirer.List('sound-chosen', 'What sound do you want to play from here?', soundList)
                    ])
                    playsound("pyPlay/sounds/"+soundChose.get("sound-chosen"))
                else:
                    print("Enter the filename of the sound file you want to play")
                    print("\n".join(soundList))
                    soundChose = input()
                    if soundChose.endswith(".wav") or soundChose.endswith(".mp3"):
                        if soundChose not in soundList:
                            print("That doesn't seem like a valid sound file (that is an .wav or .mp3 file).")
                        else:
                            playsound("pyPlay/sounds/"+soundChose)


        elif msg.lower().startswith("pyplay "):
            if "-bg" in msg.split(" "):
                if msg.split(" ")[1].endswith(".wav") or msg.split(" ")[1].endswith(".mp3"):
                    playsound("pyPlay/sounds/"+msg.split(" ")[1], False)
                else:
                    print("Oops, that does not look like a .wav or .mp3  file, perhaps add .wav at the end of the filename or input a wav file instead of something else.")
            else:
                if msg.split(" ")[1].endswith(".mp3") or msg.split(" ")[1].endswith(".wav"):
                    playsound("pyPlay/sounds/"+msg.split(" ")[1])
                else:
                    print("Oops, that does not look like a .wav or .mp3 file, perhaps add .wav at the end of the filename or input a wav file instead of something else.")

        elif msg.lower() == "memory":
            from psutil import Process

            curMemory = Process(os.getpid())
            print("Memory in megabytes: " + str(int(curMemory.memory_info().rss / 1000000)) + "MB")
        
        elif msg.lower() == "pyedit":
            match usersOS():
                case 'Darwin':
                    os.system("python3 pyedit.pyw")
                
                case 'Windows':
                    os.system("py pyedit.pyw")
                
                case 'Linux':
                    os.system("python pyedit.pyw")

        elif msg.lower() == "browser":

            match usersOS():
                case 'Darwin':
                    os.system("python3 pybrowse.pyw")
                
                case 'Windows':
                    os.system("py pybrowse.pyw")
                
                case 'Linux':
                    os.system("python pybrowse.pyw")


        elif msg.lower() == "restart":
            if getOption("colors"):
                richPrint("[bold red]Restarting..[/bold red]")
            else:
                print("Restarting...")
            reloadOS()
        
        elif msg.lower().startswith("run-luafile"):
            if not msg.endswith(".lua"):
                raise ValueError("could not identify as .lua file")
            else:
                lua = LuaRuntime()
                scriptsPath = Path("scripts")
                for luathing in os.listdir("scripts"):
                    if msg.split(" ")[1] == luathing:
                        with open(scriptsPath / msg.split(" ")[1], "r") as f:
                            lua.eval(f.read())
                
        elif bool(msg) is not False:
            print(f"\"{msg.split(' ')[0]}\" could not be recognized as a command. Double-check if you have spelt the command correctly.")


    except Exception as e:
            if getOption("colors"):
                richPrint(f"[bold red]Error: [/bold red]{str(e)}")
            else:
                print("Error: " + str(e))

