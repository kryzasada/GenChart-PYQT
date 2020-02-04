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
        self.tab_widget.addItem(self.page_1, linecache.getline("Language/Language.txt", 46)[:-1])

        self.page_1_layout = QtWidgets.QFormLayout(self.page_1)

        self.default_pie_button = QtWidgets.QPushButton(self.page_1)
        self.default_pie_button.setText(linecache.getline("Language/Language.txt", 47)[:-1])
        self.default_pie_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_1_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_pie_button)
        self.default_pie_button.clicked.connect(lambda: self.basic_pie_click())

        self.default_pie_image = QtWidgets.QLabel(self.page_1)
        self.default_pie_image.setPixmap(QtGui.QPixmap('Image/Basic_pie_chart.png'))
        self.default_pie_image.setScaledContents(True)
        self.default_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_pie_image)

        self.donut_pie_button = QtWidgets.QPushButton(self.page_1)
        self.donut_pie_button.setText(linecache.getline("Language/Language.txt", 48)[:-1])
        self.donut_pie_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_1_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.donut_pie_button)
        self.donut_pie_button.clicked.connect(lambda: self.donut_pie_click())

        self.donut_pie_image = QtWidgets.QLabel(self.page_1)
        self.donut_pie_image.setPixmap(QtGui.QPixmap('Image/Donut_pie_chart.png'))
        self.donut_pie_image.setScaledContents(True)
        self.donut_pie_image.setMaximumSize(QtCore.QSize(27, 27))
        self.page_1_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.donut_pie_image)

    def bar_chart(self):
        self.page_2 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_2, linecache.getline("Language/Language.txt", 54)[:-1])

        self.page_2_layout = QtWidgets.QFormLayout(self.page_2)

        self.default_bar_button = QtWidgets.QPushButton(self.page_2)
        self.default_bar_button.setText(linecache.getline("Language/Language.txt", 55)[:-1])
        self.default_bar_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_2_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_bar_button)
        self.default_bar_button.clicked.connect(lambda: self.basic_bar_click())

        self.default_bar_image = QtWidgets.QLabel(self.page_2)
        self.default_bar_image.setPixmap(QtGui.QPixmap('Image/Basic_bar_chart.png'))
        self.default_bar_image.setScaledContents(True)
        self.default_bar_image.setMaximumSize(QtCore.QSize(28, 27))
        self.page_2_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_bar_image)

    def line_chart(self):
        self.page_3 = QtWidgets.QWidget()
        self.tab_widget.addItem(self.page_3, linecache.getline("Language/Language.txt", 61)[:-1])

        self.page_3_layout = QtWidgets.QFormLayout(self.page_3)

        self.default_line_button = QtWidgets.QPushButton(self.page_3)
        self.default_line_button.setText(linecache.getline("Language/Language.txt", 62)[:-1])
        self.default_line_button.setMaximumSize(QtCore.QSize(110, 23))
        self.page_3_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.default_line_button)
        self.default_line_button.clicked.connect(lambda: self.basic_line_click())

        self.default_line_image = QtWidgets.QLabel(self.page_3)
        self.default_line_image.setPixmap(QtGui.QPixmap('Image/Basic_line_chart.png'))
        self.default_line_image.setScaledContents(True)
        self.default_line_image.setMaximumSize(QtCore.QSize(28, 27))
        self.page_3_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_line_image)

        self.tab_widget.setCurrentIndex(0)

        #self.page_3.setHidden(True)
        #self.tab_widget.currentChanged.connect(lambda: self.page_3.setHidden(False))

    def basic_pie_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(1)
        dock.dock_data[1].chart_type = 'Basic_pie'

        dock.dock_data[1].upper_TextValue_check.setEnabled(False)
        dock.dock_data[1].upper_first_value_check.setEnabled(False)
        for x in dock.dock_data[1].add_data:
            x.second_block_value_check.setEnabled(False)

        dock.dock_data[1].upper__TextName_check.setEnabled(True)
        dock.dock_data[1].upper_first_Name_check.setEnabled(True)
        for x in dock.dock_data[1].add_data:
            x.second_block_Name_check.setEnabled(True)

        self.default_pie_button.setEnabled(False)

        if self.donut_pie_button.isEnabled() is False:
            self.donut_pie_button.setEnabled(True)

        elif self.default_bar_button.isEnabled() is False:
            self.default_bar_button.setEnabled(True)

        elif self.default_line_button.isEnabled() is False:
            self.default_line_button.setEnabled(True)

    def donut_pie_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(1)
        dock.dock_data[1].chart_type = 'Donut_pie'

        dock.dock_data[1].upper_TextValue_check.setEnabled(False)
        dock.dock_data[1].upper_first_value_check.setEnabled(False)
        for x in dock.dock_data[1].add_data:
            x.second_block_value_check.setEnabled(False)

        dock.dock_data[1].upper__TextName_check.setEnabled(True)
        dock.dock_data[1].upper_first_Name_check.setEnabled(True)
        for x in dock.dock_data[1].add_data:
            x.second_block_Name_check.setEnabled(True)

        self.donut_pie_button.setEnabled(False)

        if self.default_pie_button.isEnabled() is False:
            self.default_pie_button.setEnabled(True)

        elif self.default_bar_button.isEnabled() is False:
            self.default_bar_button.setEnabled(True)

        elif self.default_line_button.isEnabled() is False:
            self.default_line_button.setEnabled(True)

    def basic_bar_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(2)
        dock.dock_data[1].chart_type = 'Basic_bar'

        dock.dock_data[1].upper_TextValue_check.setEnabled(True)
        dock.dock_data[1].upper_first_value_check.setEnabled(True)
        for x in dock.dock_data[1].add_data:
            x.second_block_value_check.setEnabled(True)

        dock.dock_data[1].upper__TextName_check.setEnabled(False)
        dock.dock_data[1].upper_first_Name_check.setEnabled(False)
        for x in dock.dock_data[1].add_data:
            x.second_block_Name_check.setEnabled(False)

        self.default_bar_button.setEnabled(False)

        if self.default_pie_button.isEnabled() is False:
            self.default_pie_button.setEnabled(True)

        elif self.donut_pie_button.isEnabled() is False:
            self.donut_pie_button.setEnabled(True)

        elif self.default_line_button.isEnabled() is False:
            self.default_line_button.setEnabled(True)

    def basic_line_click(self):
        self.stacked_Widget_data.setCurrentIndex(1)
        self.stacked_widget_settings.setCurrentIndex(3)
        dock.dock_data[1].chart_type = 'Basic_line'

        dock.dock_data[1].upper_TextValue_check.setEnabled(True)
        dock.dock_data[1].upper_first_value_check.setEnabled(True)
        for x in dock.dock_data[1].add_data:
            x.second_block_value_check.setEnabled(True)

        dock.dock_data[1].upper__TextName_check.setEnabled(False)
        dock.dock_data[1].upper_first_Name_check.setEnabled(False)
        for x in dock.dock_data[1].add_data:
            x.second_block_Name_check.setEnabled(False)

        self.default_line_button.setEnabled(False)

        if self.default_pie_button.isEnabled() is False:
            self.default_pie_button.setEnabled(True)

        elif self.donut_pie_button.isEnabled() is False:
            self.donut_pie_button.setEnabled(True)

        elif self.default_bar_button.isEnabled() is False:
            self.default_bar_button.setEnabled(True)



