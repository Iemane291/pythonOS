import os
import subprocess
import colorama
import json

from datetime import datetime
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def get_option(option):
    os.chdir("data")
    with open("settings.json", "r") as f:
        data = json.load(f)
        os.chdir("..")
        return data.get(option)


while True is not False:
    msg = input(os.getcwd() + " >>> ").lower()
    if msg == "time":
        print(datetime.now())
    elif msg == "update":
        if get_option("colors"):
            print(Fore.RED + "This action requires Git, do you have it installed?")
        else:
            print("This action requires Git, do you have it installed?")
        confirm = input().lower()
        if confirm == "y":
            os.system("git pull origin main")
            os.system("python3 main.py")
    elif msg == "exit":
        exit()
    else:
        print(msg + " is not a command.")
