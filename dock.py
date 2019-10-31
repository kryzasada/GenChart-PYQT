from PyQt5 import QtCore, QtWidgets
import chart

class Dock():
        def __init__(self, main_window):
                self.main_window_in_class = main_window

        def right_up(self):
                self.dockWidget_1 = QtWidgets.QDockWidget(self.main_window_in_class)

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
                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_1)

        def right_down(self):
                self.dockWidget_2 = QtWidgets.QDockWidget(self.main_window_in_class)

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
                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)

        def left_chart(self):
                self.dockWidgetChart = QtWidgets.QDockWidget(self.main_window_in_class)
                self.dockWidgetChart.setMinimumSize(QtCore.QSize(133, 163))
                self.dockWidgetChart.setObjectName("dockWidgetChart")

                self.dockWidgetChartContents = QtWidgets.QWidget()
                self.dockWidgetChartContents.setObjectName("dockWidgetChartContents")

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetChart)

                ss = chart.Chart(self.main_window_in_class, self.dockWidgetChartContents, self.dockWidgetChart)
                ss.pie_chart()


