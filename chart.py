from PyQt5 import QtCore, QtGui, QtWidgets



class Chart():
    def __init__(self, main_window_in_class, dockWidgetChartContents, dockWidgetChart):
        self.main_window_in_class = main_window_in_class
        self.dockWidgetChartContents = dockWidgetChartContents
        self.dockWidgetChart = dockWidgetChart

    def pie_chart(self):
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.dockWidgetChartContents)
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.tabbed_widget  = QtWidgets.QToolBox(self.dockWidgetChartContents)
        self.tabbed_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabbed_widget.setObjectName("tabbed_widget")

        self.pie_charm_tabbed = QtWidgets.QWidget()
        self.pie_charm_tabbed.setGeometry(QtCore.QRect(0, 0, 112, 463))
        self.pie_charm_tabbed.setObjectName("pie_charm_tabbed")

        self.tabbed_widget.addItem(self.pie_charm_tabbed, "")
        self.tabbed_widget.setItemText(self.tabbed_widget.indexOf(self.pie_charm_tabbed), "Pie chart")

        self.chart_button = QtWidgets.QPushButton(self.pie_charm_tabbed)
        self.chart_button.setGeometry(QtCore.QRect(20, 0, 75, 23))
        self.chart_button.setObjectName("chart_button")
        self.chart_button.setText("Basic")


        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 112, 463))
        self.page_2.setObjectName("page_2")
        self.tabbed_widget.addItem(self.page_2, "")

        self.horizontal_layout.addWidget(self.tabbed_widget)

        self.dockWidgetChart.setWidget(self.dockWidgetChartContents)
        self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetChart)

