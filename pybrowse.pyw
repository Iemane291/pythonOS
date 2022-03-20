import sys
import json

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont

from pathlib import Path


def getOption(optionName):
    weirdPath = Path("data")
    with open(weirdPath / "settings.json", "r") as f:
        return json.load(f).get(optionName)


lang = getOption("language")


def launch():
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

            self.backName, self.forwardName, self.reloadName, self.homeName, self.quitName, self.searchName = (
                "Back",
                "Forward",
                "Reload",
                "Home",
                "Quit",
                "Search"
            )
            if lang == "spanish-gt":
                self.backName, self.forwardName, self.reloadName, self.homeName, self.quitName, self.searchName = (
                    "Atrás",
                    "Adelante",
                    "Recargar",
                    "Inicio",
                    "Salir",
                    "Búsqueda"
                )

            back_btn = QAction(QIcon("icons/pybrowse/back-icon.png"), self.backName, self)
            back_btn.triggered.connect(self.browser.back)
            navbar.addAction(back_btn)

            forward_btn = QAction(
                QIcon("icons/pybrowse/foward-icon.png"), self.forwardName, self
            )
            forward_btn.triggered.connect(self.browser.forward)
            navbar.addAction(forward_btn)

            reload_btn = QAction(
                QIcon("icons/pybrowse/reload-icon.png"), self.reloadName, self
            )
            reload_btn.triggered.connect(self.browser.reload)
            navbar.addAction(reload_btn)

            home_btn = QAction(QIcon("icons/pybrowse/home-icon.png"), self.homeName, self)
            home_btn.triggered.connect(self.navigate_home)
            navbar.addAction(home_btn)

            quit_btn = QAction(QIcon("icons/pybrowse/quit-icon.png"), self.quitName, self)
            quit_btn.triggered.connect(self.close)
            navbar.addAction(quit_btn)

            search_btn = QAction(QIcon("icons/pybrowse/search-icon.png"), self.searchName, self)
            search_btn.triggered.connect(self.searchDlg)
            navbar.addAction(search_btn)

            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.nav_url)

            self.urlBarShit = self.url_bar.font()
            self.urlBarShit.setPointSize(23)
            self.url_bar.setFont(self.urlBarShit)

            self.url_bar.setFont(QFont("Segoe UI"))

            navbar.addWidget(self.url_bar)

            self.browser.urlChanged.connect(self.update_url)

        def navigate_home(self):
            self.browser.setUrl(QUrl("https://google.com"))

        def nav_url(self):
            url = self.url_bar.text()
            if not url.startswith("https://"):
                if url.startswith("www"):
                    self.browser.setUrl(QUrl(url))
                else:
                    self.browser.setUrl(QUrl("https://" + url))
            else:
                self.browser.setUrl(QUrl(url))

        def update_url(self, q):
            self.url_bar.setText(q.toString())
        
        def searchDlg(self):
            self.dialog = QDialog(self)
            self.dialog.setWindowTitle(self.searchName)
            self.dialog.setFixedSize(350, 250)
            self.query = QLineEdit(self.dialog)
            self.query.move(self.query.rect().center())
            self.searchBtn = QPushButton(self.dialog, text=self.searchName)
            self.searchBtn.move(self.query.x(), self.query.y()+25)
            self.searchBtn.clicked.connect(self.searcher)
            self.daQuery = self.query.text().replace(" ", "+")
            self.dialog.exec_()

        def searcher(self):
            self.browser.setUrl(QUrl(f"https://www.google.com/search?q={self.query.text().replace(' ', '+')}"))
            self.dialog.hide()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    QApplication.setApplicationName("pyBrowse")

    app.setWindowIcon(QIcon("icons/pybrowse/window-icon.png"))
    app.exec_()


launch()
