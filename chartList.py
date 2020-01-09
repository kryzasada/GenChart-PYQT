# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import dock

class Chart:
    def __init__(self, *args):
        self.grid_chart_dock = args[0]
        self.dockWidget_1Contents = args[1]
        self.stacked_Widget_data = args[2]
        self.stacked_widget_settings = args[3]

        self.pie_chart()
        self.pie_page_2()

    def pie_chart(self):
        self.tab_widget  = QtWidgets.QToolBox()
        self.grid_chart_dock.addWidget(self.tab_widget)

        self.page_1 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_1, "Pie charts")

        self.page_1_layout = QtWidgets.QFormLayout(self.page_1)

        self.default_pie_button = QtWidgets.QPushButton(self.page_1)
        self.default_pie_button.setText("Basic")
        self.default_pie_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_1_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_pie_button)
        self.default_pie_button.clicked.connect(lambda: self.basic_click())

        self.default_pie_image = QtWidgets.QLabel(self.page_1)
        self.default_pie_image.setPixmap(QtGui.QPixmap('Image/Basic_pie_chart.png'))
        self.default_pie_image.setScaledContents(True)
        self.default_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_pie_image)

        self.donut_pie_button = QtWidgets.QPushButton(self.page_1)
        self.donut_pie_button.setText("Donut")
        self.donut_pie_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_1_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.donut_pie_button)
        self.donut_pie_button.clicked.connect(lambda: self.donut_click())

        self.donut_pie_image = QtWidgets.QLabel(self.page_1)
        self.donut_pie_image.setPixmap(QtGui.QPixmap('Image/Donut_pie_chart.png'))
        self.donut_pie_image.setScaledContents(True)
        self.donut_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.donut_pie_image)

    def pie_page_2(self):
        self.page_2 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_2, "Bar charts")

        self.page_2_layout = QtWidgets.QFormLayout(self.page_2)

        self.default_bar_button = QtWidgets.QPushButton(self.page_2)
        self.default_bar_button.setText("Basic")
        self.default_bar_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_2_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_bar_button)

        self.default_bar_image = QtWidgets.QLabel(self.page_2)
        self.default_bar_image.setPixmap(QtGui.QPixmap('Image/Basic_bar_chart.png'))
        self.default_bar_image.setScaledContents(True)
        self.default_bar_image.setMaximumSize(QtCore.QSize(28, 27))
        self.page_2_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_bar_image)

    def basic_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(1)
        dock.dock_data.chart_type = 'Basic'

        self.default_pie_button.setEnabled(False)
        if self.donut_pie_button.isEnabled() is False:
            self.donut_pie_button.setEnabled(True)


    def donut_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(1)
        dock.dock_data.chart_type = 'Donut'

        self.donut_pie_button.setEnabled(False)
        if self.default_pie_button.isEnabled() is False:
            self.default_pie_button.setEnabled(True)
