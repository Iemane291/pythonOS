import os
import subprocess
import colorama
import json

from datetime import datetime
from colorama import Fore, Back, Style
from pathlib import Path

colorama.init(autoreset=True)


def getOption(option):
    os.chdir("data")
    with open("settings.json", "r") as f:
        data = json.load(f)
        os.chdir("..")
        return data.get(option)


def setOption(optionName, option):
    weirdPath = Path("data")
    with open(weirdPath / "settings.json", "r") as f:
        data = json.load(f)
        data[optionName] = option
    with open(weirdPath / "settings.json", "w") as f:
        json.dump(data, f)


while True is not False:
    try:
        msg = input(os.getcwd() + " >>> ").lower()
        if msg == "time":
            print(datetime.now())
        elif msg.startswith("change"):
            if msg.split(" ")[1] == "--help":
                print(
                    "colors - This affects if you want colored text or not, recommended to turn off incase this causes eyestrains or if your colorblind."
                )
            else:
                newoption = None
                if msg.split(" ")[2].lower() == "false":
                    newoption = False
                elif msg.split(" ")[2].lower() == "true":
                    newoption = True
                if getOption(msg.split(" ")[1].lower()) is not None:
                    setOption(msg.split(" ")[1].lower(), newoption)
                    print("Changed option.")
                else:
                    print("That is not a valid option.")
        elif msg == "update":
            if getOption("colors"):
                print(Fore.RED + "This action requires Git, do you have it installed?")
            else:
                print("This action requires Git, do you have it installed?")
            confirm = input().lower()
            if confirm == "y":
                os.system("git pull origin main")
                os.system("python3 main.py")
        elif msg == "exit":
            exit()
        elif msg == "browser":
            try:
                import sys
                from PyQt5.QtWidgets import *
                from PyQt5.QtWebEngineWidgets import *
                from PyQt5.QtCore import *

                class MainWindow(QMainWindow):
                    def __init__(self):
                        super(MainWindow, self).__init__()
                        self.setWindowTitle("Revrit")
                        self.browser = QWebEngineView()
                        self.browser.setUrl(QUrl("https://google.com"))
                        self.setCentralWidget(self.browser)
                        if getOption("browser_automaximize"):
                            self.showMaximized()
                        else:
                            self.setFixedSize(15)

                        navbar = QToolBar()
                        self.addToolBar(navbar)

                        back_btn = QAction("Back", self)
                        back_btn.triggered.connect(self.browser.back)
                        navbar.addAction(back_btn)

                        forward_btn = QAction("Foward", self)
                        forward_btn.triggered.connect(self.browser.forward)
                        navbar.addAction(forward_btn)

                        reload_btn = QAction("Reload", self)
                        reload_btn.triggered.connect(self.browser.reload)
                        navbar.addAction(reload_btn)

                        home_btn = QAction("Home", self)
                        home_btn.triggered.connect(self.navigate_home)
                        navbar.addAction(home_btn)

                        self.url_bar = QLineEdit()
                        self.url_bar.returnPressed.connect(self.nav_url)
                        navbar.addWidget(self.url_bar)

                    def navigate_home(self):
                        self.browser.setUrl(QUrl("https://google.com"))

                    def nav_url(self):
                        url = self.url_bar.text()
                        if url[0:7] != "https://":
                            self.browser.setUrl(QUrl("https://" + url))
                        else:
                            self.browser.setUrl(QUrl(url))
                            for i in range(2):
                                print(url)

                app = QApplication(sys.argv)
                QApplication.setApplicationName("Revrit")
                window = MainWindow()
                app.exec_()
            except Exception as e:
                if getOption("colors"):
                    print(Fore.RED + "Error: " + Fore.WHITE + str(e))
                    app.quit()
                else:
                    print("Error: " + str(e))
                    app.quit()
        elif bool(msg) is not False:
            print(msg + " is not a command.")
    except Exception as e:
        if getOption("colors"):
            print(Fore.RED + "Error: " + Fore.WHITE + str(e))
        else:
            print("Error: " + str(e))
