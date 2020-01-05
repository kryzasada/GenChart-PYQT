# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMenuBar, QAction, QStatusBar, QMessageBox, QPushButton, QLabel
from PyQt5.QtGui import QIcon
import webbrowser


class MenuBar:
    def __init__(self, *args):
        self.main_window_in_class = args[0]
        self.showDock = args[1]

        self.contain()

    def contain(self):
        self.main_manu = QMenuBar(self.main_window_in_class)
        self.main_manu.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.main_window_in_class.setMenuBar(self.main_manu)

        report = self.main_manu.addMenu("Report")
        report.addAction("Report your problem")
        report.triggered.connect(lambda: self.message_report())

        docks = self.main_manu.addMenu("Docks")
        docks_visiable = docks.addMenu("Visiable")

        self.list_charts = docks_visiable.addAction("List of charts")
        self.list_charts.setCheckable(True)
        self.list_charts.setChecked(True)
        self.list_charts.triggered.connect(lambda: self.show_dock(0))

        self.Data = docks_visiable.addAction("Data")
        self.Data.setCheckable(True)
        self.Data.setChecked(True)
        self.Data.triggered.connect(lambda: self.show_dock(1))

        self.Settings = docks_visiable.addAction("Settings")
        self.Settings.setCheckable(True)
        self.Settings.setChecked(True)
        self.Settings.triggered.connect(lambda: self.show_dock(2))

        self.showDock.dock_widget_chart.visibilityChanged.connect(lambda: self.change_checked_docks(0))
        self.showDock.dockWidget_data.visibilityChanged.connect(lambda: self.change_checked_docks(1))
        self.showDock.dockWidget_settings.visibilityChanged.connect(lambda: self.change_checked_docks(2))

    def message_report(self):
        message = QMessageBox()
        message.setWindowTitle("Report your problem")
        message.setText(" If you found bugs, inform me:                  ")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ignore)
        message.addButton(QPushButton('GtiHub'), QMessageBox.YesRole)
        message.setInformativeText("\n -Email: chart.bugreport@gmail.com \n \n -GtiHub: (click the button)")
        message.buttonClicked.connect(self.github_link)
        message.exec_()

    def github_link(self, i):
        if i.text() == 'GtiHub':
            webbrowser.open('https://github.com/kryzasada/Chart')

    def show_dock(self, number):
        if self.showDock.dock_widget_chart.isVisible() is False and number == 0:
            self.showDock.dock_widget_chart.show()
        elif number == 0:
            self.showDock.dock_widget_chart.hide()

        elif self.showDock.dockWidget_data.isVisible() is False and number == 1:
            self.showDock.dockWidget_data.show()
        elif number == 1:
            self.showDock.dockWidget_data.hide()

        elif self.showDock.dockWidget_settings.isVisible() is False and number == 2:
            self.showDock.dockWidget_settings.show()
        elif number == 2:
            self.showDock.dockWidget_settings.hide()

    def change_checked_docks(self, number):
        if self.showDock.dock_widget_chart.isVisible() is False and number == 0:
            self.list_charts.setChecked(False)
        elif self.showDock.dock_widget_chart.isVisible() is True and number == 0:
            self.list_charts.setChecked(True)

        elif self.showDock.dockWidget_data.isVisible() is False and number == 1:
            self.Data.setChecked(False)
        elif self.showDock.dockWidget_data.isVisible() is True and number == 1:
            self.Data.setChecked(True)

        elif self.showDock.dockWidget_settings.isVisible() is False and number == 2:
            self.Settings.setChecked(False)
        elif self.showDock.dockWidget_settings.isVisible() is True and number == 2:
            self.Settings.setChecked(True)


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