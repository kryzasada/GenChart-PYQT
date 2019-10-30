from PyQt5 import QtCore, QtGui, QtWidgets



class Chart():
    def __init__(self, main_window_in_class, dockWidgetChartContents, dockWidgetChart):
        self.main_window_in_class = main_window_in_class
        self.dockWidgetChartContents = dockWidgetChartContents
        self.dockWidgetChart = dockWidgetChart

    def pie_chart(self):
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
        self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetChart)

