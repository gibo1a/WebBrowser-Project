import sys
from PyQt5.QtWidgets import QAction,QToolBar,QApplication, QWidget, QMainWindow,QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit,QMenu
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import urllib.request

class MainWindow_Tab(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: rgb(32,32,32);")

        self.web = QWebEngineView()
        self.web.setUrl(QUrl("https://www.google.com/"))
        self.setCentralWidget(self.web)

        nav_tab = QToolBar("Navigation")
        nav_tab.setMovable(False)
        nav_tab.resize(1280,450)
        self.addToolBar(nav_tab)

        back_button = QPushButton("Back",self)
        back_button.setStyleSheet("color:white;border:None;padding-left:10px;")
        back_button.clicked.connect(self.web.back)
        nav_tab.addWidget(back_button)

        forward_button = QPushButton("Forward",self)
        forward_button.setStyleSheet("color:white;border:None;padding-left:20px")
        forward_button.clicked.connect(self.web.forward)
        nav_tab.addWidget(forward_button)

        self.reload_button = QPushButton("Reload",self)
        self.reload_button.setStyleSheet("color:white;border:None;padding-left:20px;padding-right:10px;")
        self.reload_button.clicked.connect(self.web.reload)
        nav_tab.addWidget(self.reload_button)

        nav_tab.addSeparator()

        self.urlbar = QLineEdit()
        self.urlbar.setStyleSheet("color:white;background:rgb(64,64,64);border:None;")
        self.urlbar.returnPressed.connect(self._go_to_url)
        nav_tab.addWidget(self.urlbar)

        nav_tab.addSeparator()

        self.menu = QMenu()
        self.menu.addMenu("Dropdown")
        self.menu.setStyleSheet("color:white;")
        nav_tab.addWidget(self.menu)

    def _go_to_url(self):
        url = QUrl(self.urlbar.text())
        url.setScheme("http")
        self.web.setUrl(url)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")
        self.setStyleSheet("background-color: rgb(32,32,32);")
        self.resize(1280,720)

        tab_window = MainWindow_Tab()
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setStyleSheet("background:rgb(32,32,32);")
        self.tabs.addTab(tab_window,str(urllib.request.urlopen("https://www.google.com/").read()).split('<title>')[1].split('</title>')[0])
        self.tabs.tabCloseRequested.connect(self._close_tab)
        self.setCentralWidget(self.tabs)
        
        self.button = QPushButton("+",self.tabs)
        self.button.setStyleSheet("color: white;border:None;padding-top:5px;padding-left:5px")
        self.button.move(self.tabs.tabBar().tabRect(self.tabs.currentIndex()).x()+(self.tabs.tabBar().geometry().width()),0)
        self.button.clicked.connect(self._insertTab)

    def _insertTab(self,index):
        new_page = MainWindow_Tab()
        new_page.web.setUrl(QUrl("https://www.google.com/"))
        self.tabs.insertTab(index,new_page,str(urllib.request.urlopen("https://www.google.com/").read()).split('<title>')[1].split('</title>')[0])
        self.button.move(self.tabs.tabBar().tabRect(self.tabs.currentIndex()).x()+self.tabs.tabBar().tabRect(self.tabs.currentIndex()).width(),0)

    def _close_tab(self):
        self.tabs.removeTab(self.tabs.currentIndex())
        self.button.move(self.tabs.tabBar().geometry().width(),0)


app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()




