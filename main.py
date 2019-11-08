# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.0
#

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5 import QtQuickWidgets
import sys
import dock, menuStatusBar, chart

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure


class UiMainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 598)
        main_window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        main_window.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)


        self.central_layout = QtWidgets.QHBoxLayout(self.centralwidget)

        sizes = [15, 30, 45, 10]
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        static_canvas = FigureCanvas(Figure())

        self.central_layout.addWidget(static_canvas)

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)



        status_bar = menuStatusBar.Bar(main_window)
        status_bar.menu_bar()
        status_bar.status_bar()

        showDock = dock.Dock(main_window)
        showDock.right_up()
        showDock.right_down()
        showDock.left_chart()


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
