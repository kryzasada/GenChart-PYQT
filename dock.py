# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
import linecache
import chartList, chartMenu

dock_data = []
dock_settings = []


class Dock:
    def __init__(self, *args):
        self.main_window_in_class = args[0]
        self.central_layout = args[1]

    def right_up(self):
        self.dockWidget_data = QtWidgets.QDockWidget(self.main_window_in_class)
        self.dockWidget_data.topLevelChanged.connect(lambda:
                                                     dock_title(self.dockWidget_data,
                                                                linecache.getline("Language/Language.txt", 102)[:-1]))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_data.sizePolicy().hasHeightForWidth())

        self.dockWidget_data.setSizePolicy(sizePolicy)
        self.dockWidget_data.setMinimumSize(QtCore.QSize(150, 250))
        self.dockWidget_data.setObjectName("dockWidget_data")

        self.dockWidget_data_contents = QtWidgets.QWidget()
        self.dockWidget_data_contents.setObjectName("dockWidget_data_contents")
        self.dockWidget_data.setWidget(self.dockWidget_data_contents)

        self.grid_data_dock = QtWidgets.QGridLayout(self.dockWidget_data_contents)
        self.grid_data_dock.setContentsMargins(0, 0, 0, 0)
        self.grid_data_dock.setObjectName("grid_data_dock")

        self.stacked_widget_data = QtWidgets.QStackedWidget(self.dockWidget_data_contents)
        self.stacked_widget_data.setObjectName("stacked_widget_data")
        self.grid_data_dock.addWidget(self.stacked_widget_data, 0, 0, 1, 1)

        """ Page 0 """
        self.data_page_0 = QtWidgets.QWidget()
        self.data_page_0.setObjectName("data_page_1")

        self.data_grid_page_0 = QtWidgets.QGridLayout(self.data_page_0)
        self.data_grid_page_0.setObjectName("horizontal_layout")

        self.label_data_page_0 = QtWidgets.QLabel(self.data_page_0)
        self.label_data_page_0.setObjectName("chart_button")
        self.label_data_page_0.setText(linecache.getline("Language/Language.txt", 103)[:-1])
        self.data_grid_page_0.addWidget(self.label_data_page_0)

        dock_data.append(0)

        """ Page 1 """
        self.data_page_1 = QtWidgets.QWidget()
        self.data_page_1.setObjectName("data_page_2")

        self.data_grid_page_1 = QtWidgets.QGridLayout(self.data_page_1)
        self.data_grid_page_1.setObjectName("data_grid_page_2")

        self.data_grid_page_1.setContentsMargins(3.5, 3.5, 3.5, 10)
        self.data_grid_page_1.setHorizontalSpacing(2)
        self.data_grid_page_1.setVerticalSpacing(2)

        dock_data.append(chartMenu.DataPage1(self.data_page_1, self.data_grid_page_1, self.central_layout))
        dock_data[1].contain()

        """ Adding and showing """
        self.stacked_widget_data.addWidget(self.data_page_0)
        self.stacked_widget_data.addWidget(self.data_page_1)

        self.stacked_widget_data.setCurrentIndex(0)

    def right_down(self):
        self.dockWidget_settings = QtWidgets.QDockWidget(self.main_window_in_class)
        self.dockWidget_settings.topLevelChanged.connect(lambda:
                                                         dock_title(self.dockWidget_settings,
                                                                    (linecache.getline(
                                                                        "Language/Language.txt", 108)[:-1])))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_settings.sizePolicy().hasHeightForWidth())

        self.dockWidget_settings.setSizePolicy(sizePolicy)
        self.dockWidget_settings.setMinimumSize(QtCore.QSize(150, 50))
        self.dockWidget_settings.setObjectName("dockWidget_settings")

        self.dockWidget_settings_contentsontents = QtWidgets.QWidget()
        self.dockWidget_settings_contentsontents.setObjectName("ddockWidget_settings_contentsontents")
        self.dockWidget_settings.setWidget(self.dockWidget_settings_contentsontents)

        self.grid_settings_dock = QtWidgets.QHBoxLayout(self.dockWidget_settings_contentsontents)
        self.grid_settings_dock.setObjectName("grid_settings_dock")

        self.grid_settings_dock.setContentsMargins(0, 3, 0, 0)
        self.grid_settings_dock.setSpacing(0)

        self.stacked_widget_settings = QtWidgets.QStackedWidget(self.dockWidget_settings_contentsontents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHeightForWidth(self.stacked_widget_settings.sizePolicy().hasHeightForWidth())
        self.stacked_widget_settings.setSizePolicy(sizePolicy)
        self.stacked_widget_settings.setObjectName("stacked_widget_settings")
        self.grid_settings_dock.addWidget(self.stacked_widget_settings)

        """ Page 1 """
        self.settings_page_0 = QtWidgets.QWidget()
        self.settings_page_0.setObjectName("settings_page_1")

        self.settings_grid_page_0 = QtWidgets.QVBoxLayout(self.settings_page_0)
        self.settings_grid_page_0.setObjectName("settings_grid_page_1")
        self.settings_grid_page_0.setSpacing(0)

        self.label_default = QtWidgets.QLabel(self.settings_page_0)
        self.label_default.setObjectName("label_default")
        self.label_default.setText(linecache.getline("Language/Language.txt", 109)[:-1])
        self.settings_grid_page_0.addWidget(self.label_default)

        dock_settings.append(0)

        """ Page 1 """
        self.settings_page_1 = QtWidgets.QWidget()
        self.settings_page_1.setObjectName("settings_page_1")

        self.settings_grid_page_1 = QtWidgets.QGridLayout(self.settings_page_1)
        self.settings_grid_page_1.setObjectName("settings_grid_page_1")

        self.settings_grid_page_1.setContentsMargins(0, 0, 0, 0)

        dock_settings.append(chartMenu.SettingsPage1(
            self.settings_page_1,
            self.settings_grid_page_1,
            self.central_layout))
        dock_settings[1].contain()

        """ Page 2 """
        self.settings_page_2 = QtWidgets.QWidget()
        self.settings_page_2.setObjectName("data_page_3")

        self.settings_grid_page_2 = QtWidgets.QGridLayout(self.settings_page_2)
        self.settings_grid_page_2.setObjectName("data_grid_page_3")
        self.settings_grid_page_2.setContentsMargins(0, 0, 0, 0)

        dock_settings.append(chartMenu.SettingsPage2(
            self.settings_page_2,
            self.settings_grid_page_2,
            self.central_layout))
        dock_settings[2].contain()

        """ Page 3 """
        self.settings_page_3 = QtWidgets.QWidget()
        self.settings_page_3.setObjectName("data_page_3")

        self.settings_grid_page_3 = QtWidgets.QGridLayout(self.settings_page_3)
        self.settings_grid_page_3.setObjectName("data_grid_page_3")
        self.settings_grid_page_3.setContentsMargins(0, 0, 0, 0)

        dock_settings.append(chartMenu.SettingsPage3(
            self.settings_page_3,
            self.settings_grid_page_3,
            self.central_layout))
        dock_settings[3].contain()

        """ Adding and showing """
        self.stacked_widget_settings.addWidget(self.settings_page_0)
        self.stacked_widget_settings.addWidget(self.settings_page_1)
        self.stacked_widget_settings.addWidget(self.settings_page_2)
        self.stacked_widget_settings.addWidget(self.settings_page_3)

        self.stacked_widget_settings.setCurrentIndex(0)

    def left_chart(self):
        self.dock_widget_chart = QtWidgets.QDockWidget(self.main_window_in_class)
        print(self.dock_widget_chart)
        self.dock_widget_chart.topLevelChanged.connect(lambda:
                                                       dock_title(self.dock_widget_chart,
                                                                  (linecache.getline(
                                                                      "Language/Language.txt", 114)[:-1])))

        self.dock_widget_chart.setMinimumSize(QtCore.QSize(145, 163))
        self.dock_widget_chart.setObjectName("dock_widget_chart")

        self.dock_widget_chart_contents = QtWidgets.QWidget()
        self.dock_widget_chart.setWidget(self.dock_widget_chart_contents)

        self.grid_chart_dock = QtWidgets.QHBoxLayout(self.dock_widget_chart_contents)

        chart_list = chartList.Chart(
                                     self.grid_chart_dock,
                                     self.dockWidget_data_contents,
                                     self.stacked_widget_data,
                                     self.stacked_widget_settings)

        self.docks_position()

    def docks_position(self):
        if linecache.getline("settings.txt", 9) == "Type of chart position = 2\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget_chart)
            type_position = 1
        elif linecache.getline("settings.txt", 9) == "Type of chart position = 0\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_widget_chart)
            type_position = 2
        elif linecache.getline("settings.txt", 9) == "Type of chart position = 1\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dock_widget_chart)
            type_position = 3
        elif linecache.getline("settings.txt", 9) == "Type of chart position = 3\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dock_widget_chart)
            type_position = 4

        if linecache.getline("settings.txt", 11) == "Value position = 2\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_data)
            value_position = 1
        elif linecache.getline("settings.txt", 11) == "Value position = 0\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_data)
            value_position = 2
        elif linecache.getline("settings.txt", 11) == "Value position = 1\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_data)
            value_position = 3
        elif linecache.getline("settings.txt", 11) == "Value position = 3\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_data)
            value_position = 4

        if linecache.getline("settings.txt", 13) == "Settings position = 2\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_settings)
            setting_position = 1
        elif linecache.getline("settings.txt", 13) == "Settings position = 0\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_settings)
            setting_position = 2
        elif linecache.getline("settings.txt", 13) == "Settings position = 1\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_settings)
            setting_position = 3
        elif linecache.getline("settings.txt", 13) == "Settings position = 3\n":
            self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_settings)
            setting_position = 4


        if (type_position == value_position and
                linecache.getline("settings.txt", 10)[linecache.getline("settings.txt", 10).find("=") + 2: -1] ==
                linecache.getline("settings.txt", 12)[linecache.getline("settings.txt", 12).find("=") + 2: -1] == "2"):
            self.main_window_in_class.tabifyDockWidget(self.dockWidget_data, self.dock_widget_chart)

        if (type_position == setting_position and
                linecache.getline("settings.txt", 10)[linecache.getline("settings.txt", 10).find("=") + 2: -1] ==
                linecache.getline("settings.txt", 14)[linecache.getline("settings.txt", 14).find("=") + 2: -1] == "2"):
            self.main_window_in_class.tabifyDockWidget(self.dockWidget_settings, self.dock_widget_chart)

        if (value_position == setting_position and
                linecache.getline("settings.txt", 12)[linecache.getline("settings.txt", 12).find("=") + 2: -1] ==
                linecache.getline("settings.txt", 14)[linecache.getline("settings.txt", 14).find("=") + 2: -1] == "2"):
            self.main_window_in_class.tabifyDockWidget(self.dockWidget_settings, self.dockWidget_data)

        if (type_position == value_position == setting_position and
                linecache.getline("settings.txt", 10)[linecache.getline("settings.txt", 10).find("=") + 2: -1] ==
                linecache.getline("settings.txt", 12)[linecache.getline("settings.txt", 12).find("=") + 2: -1] ==
                linecache.getline("settings.txt", 14)[linecache.getline("settings.txt", 14).find("=") + 2: -1] == "2"):
            self.main_window_in_class.tabifyDockWidget(self.dockWidget_settings, self.dock_widget_chart)
            self.main_window_in_class.tabifyDockWidget(self.dockWidget_data, self.dock_widget_chart)


def dock_title(dock, name):
    if dock.isWindow():
        dock.setWindowTitle(name)
    else:
        dock.setWindowTitle("")
