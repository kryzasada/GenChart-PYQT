# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import linecache

import dock

class Chart:
    def __init__(self, *args):
        self.grid_chart_dock = args[0]
        self.dockWidget_1Contents = args[1]
        self.stacked_Widget_data = args[2]
        self.stacked_widget_settings = args[3]

        self.tab_widget = QtWidgets.QToolBox()
        self.grid_chart_dock.addWidget(self.tab_widget)

        self.pie_chart()
        self.bar_chart()
        self.line_chart()

    def pie_chart(self):
        self.page_1 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_1, linecache.getline("Language/Language.txt", 202)[:-1])

        self.page_1_layout = QtWidgets.QFormLayout(self.page_1)

        self.default_pie_button = QtWidgets.QPushButton(self.page_1)
        self.default_pie_button.setText(linecache.getline("Language/Language.txt", 203)[:-1])
        self.default_pie_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_1_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_pie_button)
        self.default_pie_button.clicked.connect(lambda: self.chart_click("basic_pie"))

        self.default_pie_image = QtWidgets.QLabel(self.page_1)
        self.default_pie_image.setPixmap(QtGui.QPixmap('Image/Chart_images/Basic_pie_chart.png'))
        self.default_pie_image.setScaledContents(True)
        self.default_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_pie_image)

        self.donut_pie_button = QtWidgets.QPushButton(self.page_1)
        self.donut_pie_button.setText(linecache.getline("Language/Language.txt", 204)[:-1])
        self.donut_pie_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_1_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.donut_pie_button)
        self.donut_pie_button.clicked.connect(lambda: self.chart_click("donut_pie"))

        self.donut_pie_image = QtWidgets.QLabel(self.page_1)
        self.donut_pie_image.setPixmap(QtGui.QPixmap('Image/Chart_images/Donut_pie_chart.png'))
        self.donut_pie_image.setScaledContents(True)
        self.donut_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.donut_pie_image)

        self.percent_pie_button = QtWidgets.QPushButton(self.page_1)
        self.percent_pie_button.setText(linecache.getline("Language/Language.txt", 205)[:-1] +
                                        "\n" +
                                        linecache.getline("Language/Language.txt", 204)[:-1].lower())
        self.percent_pie_button.setMaximumSize(QtCore.QSize(110, 46))
        self.page_1_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.percent_pie_button)
        self.percent_pie_button.clicked.connect(lambda: self.chart_click("percent_pie"))

        self.percent_pie_image = QtWidgets.QLabel(self.page_1)
        self.percent_pie_image.setPixmap(QtGui.QPixmap('Image/Chart_images/Percentage_donut_pie_chart.png'))
        self.percent_pie_image.setScaledContents(True)
        self.percent_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.percent_pie_image)

    def bar_chart(self):
        self.page_2 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_2, linecache.getline("Language/Language.txt", 210)[:-1])

        self.page_2_layout = QtWidgets.QFormLayout(self.page_2)

        self.default_bar_button = QtWidgets.QPushButton(self.page_2)
        self.default_bar_button.setText(linecache.getline("Language/Language.txt", 211)[:-1])
        self.default_bar_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_2_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_bar_button)
        self.default_bar_button.clicked.connect(lambda: self.chart_click("basic_bar"))

        self.default_bar_image = QtWidgets.QLabel(self.page_2)
        self.default_bar_image.setPixmap(QtGui.QPixmap('Image/Chart_images/Basic_bar_chart.png'))
        self.default_bar_image.setScaledContents(True)
        self.default_bar_image.setMaximumSize(QtCore.QSize(28, 27))
        self.page_2_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_bar_image)

    def line_chart(self):
        self.page_3 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_3, linecache.getline("Language/Language.txt", 217)[:-1])

        self.page_3_layout = QtWidgets.QFormLayout(self.page_3)

        self.default_line_button = QtWidgets.QPushButton(self.page_3)
        self.default_line_button.setText(linecache.getline("Language/Language.txt", 218)[:-1])
        self.default_line_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_3_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_line_button)
        self.default_line_button.clicked.connect(lambda: self.chart_click("basic_line"))

        self.default_line_image = QtWidgets.QLabel(self.page_3)
        self.default_line_image.setPixmap(QtGui.QPixmap('Image/Chart_images/Basic_line_chart.png'))
        self.default_line_image.setScaledContents(True)
        self.default_line_image.setMaximumSize(QtCore.QSize(28, 27))
        self.page_3_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_line_image)

        self.tab_widget.setCurrentIndex(2)

        self.page_3.setHidden(True)
        self.tab_widget.currentChanged.connect(lambda: self.page_3.setHidden(False))

        findWidget = self.tab_widget.findChildren(QtWidgets.QAbstractButton)
        findWidget2 = self.page_3.findChildren(QtWidgets.QAbstractButton)
        findWidget[(len(findWidget2)*-1)-1].clicked.connect(lambda: self.page_3.setHidden(False))

    def chart_click(self, type):
        for object in (self.default_pie_button,
                       self.donut_pie_button,
                       self.percent_pie_button,
                       self.default_bar_button,
                       self.default_line_button):

            if object.isEnabled() is False:
                object.setEnabled(True)

        if type == "basic_pie":
            self.stacked_Widget_data.setCurrentIndex(1)
            self.stacked_widget_settings.setCurrentIndex(1)
            dock.dock_data[1].chart_type = 'Basic_pie'
            self.default_pie_button.setEnabled(False)

            name_display = True
            value_display = False

        elif type == "donut_pie":
            self.stacked_Widget_data.setCurrentIndex(1)
            self.stacked_widget_settings.setCurrentIndex(1)
            dock.dock_data[1].chart_type = 'Donut_pie'
            self.donut_pie_button.setEnabled(False)

            name_display = True
            value_display = False

        elif type == "percent_pie":
            self.stacked_Widget_data.setCurrentIndex(1)
            self.stacked_widget_settings.setCurrentIndex(4)
            dock.dock_data[1].chart_type = 'Percent_pie'
            self.percent_pie_button.setEnabled(False)

            name_display = True
            value_display = False

        elif type == "basic_bar":
            self.stacked_Widget_data.setCurrentIndex(1)
            self.stacked_widget_settings.setCurrentIndex(2)
            dock.dock_data[1].chart_type = 'Basic_bar'
            self.default_bar_button.setEnabled(False)

            name_display = False
            value_display = True

        elif type == "basic_line":
            self.stacked_Widget_data.setCurrentIndex(1)
            self.stacked_widget_settings.setCurrentIndex(3)
            dock.dock_data[1].chart_type = 'Basic_line'
            self.default_line_button.setEnabled(False)

            name_display = False
            value_display = False

        else:
            name_display = False
            value_display = False

        dock.dock_data[1].upper__TextName_check.setEnabled(name_display)
        dock.dock_data[1].upper_first_Name_check.setEnabled(name_display)
        for x in dock.dock_data[1].add_data:
            x.second_block_Name_check.setEnabled(name_display)

        dock.dock_data[1].upper_TextValue_check.setEnabled(value_display)
        dock.dock_data[1].upper_first_value_check.setEnabled(value_display)
        for x in dock.dock_data[1].add_data:
            x.second_block_value_check.setEnabled(value_display)

