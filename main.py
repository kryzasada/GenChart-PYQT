# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.0
#

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
import sys, linecache
import dock, menuStatusBar, chartList




class UiMainWindow(object):
    def setupUi(self, main_window):

        if 0:
            style_css = "Theme/darkorange.css"
            style = open(style_css, "r")
            app.setStyleSheet(style.read())

        try:
            file_line = linecache.getline("settings.txt", 3)
            if file_line == "First start = 1\n":
                print("Open first time configuration window")

                old_file = open("settings.txt").read()
                old_file = old_file.replace('First start = 1', 'First start = 0')
                new_file = open("settings.txt", 'w')
                new_file.write(old_file)
                new_file.close()

        finally:
            linecache.clearcache()

        main_window.resize(800, 600)
        main_window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        main_window.setTabShape(QtWidgets.QTabWidget.Triangular)
        main_window.setWindowIcon(QtGui.QIcon("Image/Icons/blank-logo.ico"))
        main_window.setWindowTitle("GenChart")

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)

        self.central_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        showDock = dock.Dock(main_window, self.central_layout)
        showDock.right_up()
        showDock.right_down()
        showDock.left_chart()

        menu_bar = menuStatusBar.MenuBar(main_window, showDock)
        status_bar = menuStatusBar.StatusBar(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
