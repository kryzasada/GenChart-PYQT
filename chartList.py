# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Chart():
    def __init__(self, *args):
        self.dockWidgetChartContents = args[0]
        self.dockWidgetChart = args[1]
        self.dockWidget_1Contents = args[2]
        self.stacked_Widget_data = args[3]
        self.stacked_widget_settings = args[4]


        self.horizontal_layout = QtWidgets.QHBoxLayout(self.dockWidgetChartContents)
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.pie_chart()
        self.pie_page_2()

        self.dockWidgetChart.setWidget(self.dockWidgetChartContents)

    def pie_chart(self):

        self.tabbed_widget  = QtWidgets.QToolBox(self.dockWidgetChartContents)
        self.tabbed_widget.setObjectName("tabbed_widget")

        self.pie_charm_tabbed = QtWidgets.QWidget()
        self.pie_charm_tabbed.setGeometry(QtCore.QRect(0, 0, 112, 463))
        self.pie_charm_tabbed.setObjectName("pie_charm_tabbed")

        self.tabbed_widget.addItem(self.pie_charm_tabbed, "")
        self.tabbed_widget.setItemText(self.tabbed_widget.indexOf(self.pie_charm_tabbed), "Pie chart")

        self.chart_button = QtWidgets.QPushButton(self.pie_charm_tabbed)
        self.chart_button.setGeometry(QtCore.QRect(37, 4, 75, 23))
        self.chart_button.setObjectName("chart_button")
        self.chart_button.setText("Basic")
        self.chart_button.clicked.connect(lambda: self.on_click())


        self.test_button = QtWidgets.QPushButton(self.dockWidget_1Contents)
        self.test_button.setGeometry(QtCore.QRect(37, 40, 75, 23))
        self.test_button.setObjectName("test_button")
        self.test_button.setText("test_button")
        self.test_button.setVisible(False)


        self.label = QtWidgets.QLabel(self.pie_charm_tabbed)
        self.label.setPixmap(QtGui.QPixmap('Image/Basic_pie_chart.png'))
        self.label.setScaledContents(True)
        self.label.setGeometry(2, 2, 27, 27)

    def pie_page_2(self):
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 112, 463))
        self.page_2.setObjectName("page_2")
        self.tabbed_widget.addItem(self.page_2, "")
        self.horizontal_layout.addWidget(self.tabbed_widget)


    def on_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(1)

