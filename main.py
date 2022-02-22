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
    elif msg == "browser":
        import sys
        from PyQt5.QtWidgets import *
        from PyQt5.QtWebEngineWidgets import QUrl, QWebEngineView

        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl("https://google.com"))
                self.setCentralWidget(self.browser)
                self.showMaximized()

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
        QApplication.setApplicationName("Chungle")
        window = MainWindow()
        app.exec_()
    else:
        print(msg + " is not a command.")
