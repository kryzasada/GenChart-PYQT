from PyQt5 import QtCore, QtWidgets


class Bar():
    def __init__(self, *args):
        self.main_window_in_class = args[0]

    def menu_bar(self):
        self.menubar = QtWidgets.QMenuBar(self.main_window_in_class)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.main_window_in_class.setMenuBar(self.menubar)

    def status_bar(self):
        self.statusbar = QtWidgets.QStatusBar(self.main_window_in_class)
        self.statusbar.setObjectName("statusbar")
        self.main_window_in_class.setStatusBar(self.statusbar)