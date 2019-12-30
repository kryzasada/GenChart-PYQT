# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMenuBar, QAction, QStatusBar, QMessageBox, QPushButton, QLabel
from PyQt5.QtGui import QIcon
import webbrowser


class MenuBar:
    def __init__(self, *args):
        self.main_window_in_class = args[0]

        self.contain()

    def contain(self):
        self.main_manu = QMenuBar(self.main_window_in_class)
        self.main_manu.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.main_window_in_class.setMenuBar(self.main_manu)

        file = self.main_manu.addMenu("Report")
        file.addAction("Report your problem")
        file.triggered.connect(lambda: self.message_report())

    def message_report(self):
        message = QMessageBox()
        message.setWindowTitle("Report your problem")
        message.setText(" If you found bugs, inform me:                  ")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ignore)
        message.addButton(QPushButton('Gtihub'), QMessageBox.YesRole)
        message.setInformativeText("\n -Email: chart.bugreport@gmail.com \n \n -Gtihub: (click the button)")
        message.buttonClicked.connect(self.github_link)
        message.exec_()

    def github_link(self, i):
        if i.text() == 'Gtihub':
            webbrowser.open('https://github.com/kryzasada/Chart')


class StatusBar:
    def __init__(self, *args):
        self.main_window_in_class = args[0]

        self.contain()

    def contain(self):
        self.status_bar = QStatusBar(self.main_window_in_class)
        self.main_window_in_class.setStatusBar(self.status_bar)

        version = QLabel(self.main_window_in_class)
        version.setText("v. 0.1.0")

        self.status_bar.addWidget(version)