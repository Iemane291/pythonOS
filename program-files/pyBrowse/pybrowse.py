import sys

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle("pyBrowse")
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

        quit_btn = QAction("Quit", self)
        quit_btn.triggered.connect(self.close)
        navbar.addAction(quit_btn)

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
window = MainWindow()
QApplication.setApplicationName("pyBrowse")


app.setWindowIcon(QIcon("icon.png"))
app.exec_()
