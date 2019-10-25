# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2wersja.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.gridLayout_2.addWidget(self.quickWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetChart = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetChart.setMinimumSize(QtCore.QSize(130, 163))
        self.dockWidgetChart.setObjectName("dockWidgetChart")
        self.dockWidgetChartContents = QtWidgets.QWidget()
        self.dockWidgetChartContents.setObjectName("dockWidgetChartContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetChartContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PieCharm = QtWidgets.QToolBox(self.dockWidgetChartContents)
        self.PieCharm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PieCharm.setObjectName("PieCharm")
        self.inPieCharm = QtWidgets.QWidget()
        self.inPieCharm.setGeometry(QtCore.QRect(0, 0, 112, 463))
        self.inPieCharm.setObjectName("inPieCharm")
        self.ChartButton = QtWidgets.QPushButton(self.inPieCharm)
        self.ChartButton.setGeometry(QtCore.QRect(20, 0, 75, 23))
        self.ChartButton.setObjectName("ChartButton")
        self.PieCharm.addItem(self.inPieCharm, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 112, 463))
        self.page_2.setObjectName("page_2")
        self.PieCharm.addItem(self.page_2, "")
        self.horizontalLayout.addWidget(self.PieCharm)
        self.dockWidgetChart.setWidget(self.dockWidgetChartContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetChart)
        self.dockWidget_1 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_1.sizePolicy().hasHeightForWidth())
        self.dockWidget_1.setSizePolicy(sizePolicy)
        self.dockWidget_1.setMinimumSize(QtCore.QSize(130, 20))
        self.dockWidget_1.setObjectName("dockWidget_1")
        self.dockWidget_1Contents = QtWidgets.QWidget()
        self.dockWidget_1Contents.setObjectName("dockWidget_1Contents")
        self.dockWidget_1.setWidget(self.dockWidget_1Contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_1)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(130, 20))
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        self.PieCharm.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidgetChart.setAccessibleName(_translate("MainWindow", "ss"))
        self.ChartButton.setText(_translate("MainWindow", "ChartButton"))
        self.PieCharm.setItemText(self.PieCharm.indexOf(self.inPieCharm), _translate("MainWindow", "Pie chart"))
        self.PieCharm.setItemText(self.PieCharm.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
from PyQt5 import QtQuickWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
