import os
import json
import colorama

from pathlib import Path


def getSettings() -> dict:
    coolPath = Path("data")
    with open(coolPath / "settings.json") as f:
        return json.load(f)


def getOption(option):
    coolpath = Path("data")
    with open(coolpath / "settings.json", "r") as f:
        data = json.load(f)
        return data.get(option)


language = getOption("language")

if os.name == "nt" and getOption("use-size-settings"):
    os.system(
        f"mode con: cols={getOption('size-columns')} lines={getOption('size-lines')}"
    )


if os.name == "nt":
    os.system("title pythonOS")
os.system("clear" if os.name == "posix" else "cls")

colorama.init(autoreset=True)
print(
    """     _   _                  ____   _____ 
             | | | |                / __ \ / ____|
  _ __  _   _| |_| |__   ___  _ __ | |  | | (___  
 | '_ \| | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
 | |_) | |_| | |_| | | | (_) | | | | |__| |____) |
 | .__/ \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
 | |     __/ |                                    
 |_|    |___/                                     
"""
)
print("v0.0.6a")
if language == "english":
    print("Loading..")
elif language == "spanish-gt":
    print("Cargando..")


import json
import sys

# mf we needed that loading screen, because we are importing a billion things. the pyqt5 imports make this slow so we quickly make a loading screen

from datetime import datetime
from colorama import Fore, Back, Style
from platform import system as usersOS

from lupa import LuaRuntime
from webbrowser import open_new_tab as openNewTab
from rich.markdown import Markdown

from rich.console import Console
from rich import print as richPrint
from psutil import Process

console = Console()


def reloadOS():
    os.execl(sys.executable, sys.executable, *sys.argv)


def update():
    os.system("git pull origin main --quiet")


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

pygame.mixer.init()
os.system("clear" if os.name == "posix" else "cls")
print(
    """     _   _                  ____   _____ 
             | | | |                / __ \ / ____|
  _ __  _   _| |_| |__   ___  _ __ | |  | | (___  
 | '_ \| | | | __| '_ \ / _ \| '_ \| |  | |\___ \ 
 | |_) | |_| | |_| | | | (_) | | | | |__| |____) |
 | .__/ \__, |\__|_| |_|\___/|_| |_|\____/|_____/ 
 | |     __/ |                                    
 |_|    |___/                                                                      
"""
)
print("v0.0.6a")
if getOption("colors"):
    if language == "english":
        print(Fore.YELLOW + "Loading..")
    elif language == "spanish-gt":
        print(Fore.YELLOW + "Cargando..")
else:
    if language == "english":
        print("Loading..")
    elif language == "spanish-gt":
        print("Cargando..")


def setOption(optionName, option):
    weirdPath = Path("data")
    with open(weirdPath / "settings.json", "r") as f:
        data = json.load(f)
        data[optionName] = option
    with open(weirdPath / "settings.json", "w") as f:
        json.dump(data, f, indent=4)


killMe = os.getcwd()
if getOption("security"):
    if language == "english":
        globals()["killMe"] = "dir@user"
    elif language == "spanish-gt":
        globals()["killMe"] = "dir@usuario"


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
                msg = input(Fore.YELLOW + killMe + " >>> ")
            case "green":
                msg = input(Fore.GREEN + killMe + " >>> ")
            case "magenta":
                msg = input(Fore.MAGENTA + killMe + " >>> ")
            case _:
                msg = input(killMe + " >>> ")
        if msg.lower() == "time":
            print(datetime.now())

        elif msg == "cls":
            os.system("cls" if os.name == "nt" else "clear")

        elif (msg.lower().startswith("edit") and language == "english") or (msg.lower().startswith("editar") and language == "spanish-gt"):
            try:
                if getOption("error-warning"):
                    if getOption("colors"):
                        if language == "english":
                            richPrint(
                                "[yellow]WARNING: Editing system variables may result in a ton of errors or a crash, if error messages are filling up pythonOS. Immediately close pythonOS and reopen it.[/yellow]"
                            )
                        elif language == "spanish-gt":
                            richPrint(
                                "[yellow]ADVERTENCIA: la edición de variables del sistema puede provocar un bloqueo o un montón de errores. Si los errores llenan pythonOS, cierre pythonOS y vuelva a abrirlo.[/yellow]"
                            )
                    else:
                        if language == "english":
                            print(
                                "WARNING: Editing system variables may result in a ton of errors or a crash, if error messages are filling up pythonOS. Immediately close pythonOS and reopen it."
                            )
                        elif language == "spanish-gt":
                            print(
                                "ADVERTENCIA: la edición de variables del sistema puede provocar un bloqueo o un montón de errores. Si los errores llenan pythonOS, cierre pythonOS y vuelva a abrirlo."
                            )
                if msg.split(" ")[1] in globals() or msg.split(" ")[1] in locals():
                    isLocal = False if msg.split(" ")[1] in globals() else True
                    if language == "spanish-gt":
                        print("¿Cuál es el tipo de valor?")
                    elif language == "english":
                        print("What is the type of value?")
                    if not getOption("colors"):
                        if language == "english":
                            print("[0] Number\n[1] Text/String")
                        elif language == "spanish-gt":
                            print("[0] Número\n[1] Texto/Cadena")
                    elif getOption("colors"):
                        if language == "english":
                            richPrint("[blue][0][/blue] - Number")
                            richPrint("[blue][1][/blue] - Text/String")
                        elif language == "spanish-gt":
                            richPrint("[blue][0][/blue] - Número")
                            richPrint("[blue][1][/blue] - Texto/Cadena")
                    chosentype = int(input())
                    if type(chosentype) is int:
                        match chosentype:
                            case 0:
                                if language == "english":
                                    newValue = int(
                                        input(
                                            f"What do you want to edit {msg.split(' ')[1]} to? "
                                        )
                                    )
                                elif language == "spanish-gt":
                                    newValue = int(
                                        input(
                                            f"Que queires editar {msg.split(' ')[1]} para? "
                                        )
                                    )
                            case 1:
                                if language == "english":
                                    newValue = input(
                                        f"What do you want to edit {msg.split(' ')[1]} to? "
                                    )
                                elif language == "spanish-gt":
                                    newValue = input(
                                        f"Que queires editar {msg.split(' ')[1]} para? "
                                    )
                            case _:
                                if language == "english":
                                    print("That is a not valid number!")
                                elif language == "spanish-gt":
                                    print("¡Ese no es un número válido!")
                    if not isLocal:
                        globals()[msg.split(" ")[1]] = newValue
                    if isLocal:
                        locals()[msg.split(" ")[1]] = newValue
                else:
                    if language == "english":
                        raise ValueError(f"could not find \"{msg.split(' ')[1]}\"")
                    elif language == "spanish-gt":
                        raise ValueError(f"no pudo encontrar \"{msg.split(' ')[1]}\"")
            except NameError as e:
                if str(e) == "name 'newValue' is not defined":
                    pass
                else:
                    raise ValueError(str(e))

        elif msg.lower() == "pyconf":
            match usersOS():
                case "Windows":
                    os.system("py pyconf.pyw")
                case "Darwin":
                    os.system("python3 pyconf.pyw")
                case "Linux":
                    os.system("python3 pyconf.pyw")

        elif msg.lower().split(" ")[0] in ("md", "mkdir"):
            try:
                os.mkdir(msg.split(" ")[1])
            except FileExistsError:
                if language == "spanish-gt":
                    raise FileExistsError("ese directorio ya existe")
                elif language == "english":
                    raise FileExistsError("That directory already exists")

        elif (language == "spanish-gt" and msg.lower() == "correr-lua") or (
            language == "english" and msg.lower() == "run-lua"
        ):
            lua = LuaRuntime()
            weirdPath = Path("scripts")
            if len(os.listdir("scripts")) > 1:
                for luaFile in os.listdir("scripts"):
                    if luaFile.endswith(".lua"):
                        with open(weirdPath / luaFile, "r") as f:
                            lua.eval(f.read())
            else:
                if language == "english":
                    print(
                        'Seems that you have no Lua scripts. Please add one in the "scripts" folder.'
                    )
                elif language == "spanish-gt":
                    print(
                        'Parece que no tiene ninguna secuencia de comandos de Lua, agregue secuencias de comandos de Lua en la carpeta "scripts"'
                    )

        elif msg.lower() == "readme":
            if getOption("colors"):
                with open("README.md", "r") as mdFile:
                    textRead = Markdown(mdFile.read())
                console.print(textRead)

        elif msg.lower().startswith("pyconf"):
            if ("--help" in msg.split(" ") and language == "english") or (
                "--ayuda" in msg.split(" ") and language == "spanish-gt"
            ):
                if language == "english":
                    print(
                        "\nOptions:\n\tcolors - This toggles if you will see colors or not.\n\tinput-color - This changes the input color, possible options are: green, blue, magenta, red, white, yellow.\n\tsecurity - This will not display your private information.\n\tgit-installed - Whenever you update, this may trigger if you'll be asked if you have git installed or not.\n\tedit-warning - This will show a warning if you are running the edit command, even if an error occured.\n\tuse-size-settings - This will change the command window columns to size-columns and lines to to size-lines every restart.\n\tsize-lines - This is how much lines the command window is.\n\tsize-columns - This is how much columns the command window is."
                    )
                elif language == "spanish-gt":
                    print(
                        "\nOpciones:\n\tcolores: esto cambia si verá colores o no.\n\tinput-color: esto cambia el color de entrada, las opciones posibles son: verde, azul, magenta, rojo, blanco, amarillo.\n\t security: esto no mostrará su información privada.\n\tgit-installed: cada vez que actualice, si esta opción se establece en verdadero, no le preguntará si tiene Git instalado; de lo contrario, aparecerá\n\tedit-warning: esto mostrará una advertencia si está ejecutando el comando de edición, incluso si ocurre un error.\n\tuse-size-settings: esto cambiará las columnas de la ventana de comandos al tamaño de columna y líneas a tamaño de línea en cada reinicio. \n\tsize-lines: este es el número de líneas que tiene la ventana de comandos.\n\tsize-columns: este es el número de columnas que tiene la ventana de comandos."
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
                if msg.split(" ")[1].lower() in getSettings().keys():
                    if msg.split(" ")[1].lower() not in (
                        "input-color",
                        "size-columns",
                        "size-lines",
                        "language",
                    ):
                        setOption(msg.split(" ")[1].lower(), newoption)
                    elif msg.split(" ")[1].lower() == "input-color":
                        setOption(
                            "input-color",
                            msg.split(" ")[2]
                            .lower()
                            .replace("azul", "blue")
                            .replace("verde", "green")
                            .replace("rojo", "red")
                            .replace("blanco", "white")
                            .replace("amarillo", "yellow"),
                        )
                    elif msg.split(" ")[1].lower() == "language":
                        setOption("language", msg.split(" ")[2].lower())
                        language = getOption("language")
                        if msg.split(" ")[2].lower() == "spanish-gt":
                            print(
                                'Reinicie pythonOS usando el comando "reiniciar" para que estos cambios surtan efecto.'
                            )
                        elif msg.split(" ")[2].lower() == "english":
                            print(
                                'Please restart pythonOS using the "restart" command for your changes to take effect.'
                            )
                    elif (
                        msg.split(" ")[1].lower() == "size-columns"
                        or msg.split(" ")[1].lower() == "size-lines"
                    ):
                        setOption(msg.split(" ")[1].lower(), int(msg.split(" ")[2]))
                        language = getOption("language")
                        if getOption("colors"):
                            richPrint(
                                "[yellow]Please restart pythonOS and make sure the use-size-settings option is turned on for these changes to take effect[/yellow]"
                            )
                        else:
                            print(
                                "Please restart pythonOS and make sure the use-size-settings option is turned on for these changes to take effect"
                            )
                    else:
                        setOption(msg.split(" ")[1].lower(), msg.split(" ")[2].lower())
                    if language == "english":
                        print("Successfully changed option.")
                    elif language == "spanish-gt":
                        print("Opción cambiada con éxito.")
                else:
                    if language == "english":
                        print(
                            'That is not an existing option, please read the settings.json or do "pyconf --help" to see what options you can change.'
                        )
                    elif language == "spanish-gt":
                        print(
                            'Esa no es una opción existente, lea settings.json o haga "pyconf --help" para ver qué opciones puede cambiar.'
                        )
        elif (msg.lower() == "update" and language == "english") or (msg.lower() == "actualizar" and language == "spanish-gt"):

            if not getOption("git-installed"):
                if getOption("colors"):
                    if language == "english":
                        print(
                            Fore.RED
                            + "This action requires Git, do you have it installed?"
                        )
                    elif language == "spanish-gt":
                        print(
                            Fore.RED + "Esta acción requiere Git, ¿lo tienes instalado?"
                        )
                else:
                    if language == "english":
                        print("This action requires Git, do you have it installed?")
                    elif language == "spanish-gt":
                        print("Esta acción requiere Git, ¿lo tienes instalado?")
                confirm = input().lower()
                if confirm == "y":
                    setOption("git-installed", True)
                    update()
                    reloadOS()
                elif confirm == "n":
                    if not getOption("security"):
                        openNewTab("https://git-scm.com/downloads")
                    setOption("git-installed", False)
            elif getOption("git-installed"):
                update()
                reloadOS()

        elif msg.lower() == "exit":
            break


        elif msg.lower() == "pyplay":
            match usersOS():
                case "Windows":
                    os.system("py pyplay.pyw")
                case "Darwin":
                    os.system("python3 pyplay.pyw")
                case "Linux":
                    os.system("python3 pyplay.pyw")

        elif msg.lower().startswith("pyplay "):
            if (
                msg.split(" ")[1].endswith(".mp3")
                or msg.split(" ")[1].endswith(".wav")
                or msg.split(" ")[1].endswith(".ogg")
            ):
                pygame.mixer.music.load("pyPlay/sounds/" + msg.split(" ")[1])
                pygame.mixer.music.play()
            else:
                if language == "english":
                    print("That does not seem like an OGG, WAVE or an MP3 sound file.")
                elif language == "spanish-gt":
                    print("Eso no parece un archivo de sonido OGG, WAVE o MP3.")

        elif msg.lower() in ("mem", "memory"):

            curMemory = Process(os.getpid())
            if language == "english":
                print(
                    "Memory in megabytes: "
                    + str(int(curMemory.memory_info().rss / 1e6))
                    + "MB"
                )
            elif language == "spanish-gt":
                print(
                    "Memoria en megabytes: "
                    + str(int(curMemory.memory_info().rss / 1e6))
                    + "MB"
                )

        elif msg.lower() == "pyedit":
            match usersOS():
                case "Darwin":
                    os.system("python3 pyedit.pyw")

                case "Windows":
                    os.system("py pyedit.pyw")

                case "Linux":
                    os.system("python3 pyedit.pyw")

        elif (msg.lower() == "browser" and language == "english") or (msg.lower() == "navegador" and language == "spanish-gt"):

            match usersOS():
                case "Darwin":
                    os.system("python3 pybrowse.pyw")

                case "Windows":
                    os.system("py pybrowse.pyw")

                case "Linux":
                    os.system("python3 pybrowse.pyw")

        elif (language == "english" and msg.split(" ")[0] == "echo") or (
            language == "spanish-gt" and msg.split(" ")[0] == "eco"
        ):
            print(msg.split(" ")[1])

        elif (language == "english" and msg.lower() == "restart") or (
            language == "spanish-gt" and msg.lower() == "reiniciar"
        ):
            if getOption("colors"):
                if language == "english":
                    richPrint("[bold red]Restarting..[/bold red]")
                elif language == "spanish-gt":
                    richPrint("[bold red]Reiniciando..[/bold red]")
            else:
                if language == "english":
                    print("Restarting..")
                elif language == "spanish-gt":
                    print("Reiniciando..")
            reloadOS()

        elif msg.lower().startswith("ejecutar-luafile"):
            if not msg.endswith(".lua"):
                if language == "english":
                    raise ValueError("could not identify as .lua file")
                elif language == "spanish-gt":
                    raise ValueError("no se pudo identificar como un archivo .lua")
            else:
                lua = LuaRuntime()
                scriptsPath = Path("scripts")
                for luathing in os.listdir("scripts"):
                    if msg.split(" ")[1] == luathing:
                        with open(scriptsPath / msg.split(" ")[1], "r") as f:
                            lua.eval(f.read())

        elif bool(msg) is not False:
            if language == "english":
                print(
                    f"\"{msg.split(' ')[0]}\" could not be recognized as a command. Double-check if you have spelt the command correctly."
                )
            elif language == "spanish-gt":
                print(
                    f"\"{msg.split(' ')[0]}\" no podía ser reconocido como un comando. Vuelva a verificar si ha escrito el comando correctamente."
                )

    except Exception as e:
        if getOption("colors"):
            richPrint(f"[bold red]Error: [/bold red]{str(e)}")
        else:
            print("Error: " + str(e))
