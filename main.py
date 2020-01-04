# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.0
#

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5 import QtQuickWidgets
import sys
import dock, menuStatusBar, chartList


class UiMainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 598)
        main_window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        main_window.setTabShape(QtWidgets.QTabWidget.Triangular)

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

        self.retranslateUi(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
