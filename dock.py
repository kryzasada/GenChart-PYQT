# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import chartList, chartMenu

dock_data = 0
dock_settings = 0


class Dock:
        def __init__(self, *args):
                self.main_window_in_class = args[0]
                self.central_layout = args[1]

        def right_up(self):
                self.dockWidget_data = QtWidgets.QDockWidget(self.main_window_in_class)

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

                self.stacked_widget_data= QtWidgets.QStackedWidget(self.dockWidget_data_contents)
                self.stacked_widget_data.setObjectName("stacked_widget_data")
                self.grid_data_dock.addWidget(self.stacked_widget_data, 0, 0, 1, 1)


                self.data_page_1 = QtWidgets.QWidget()
                self.data_page_1.setObjectName("data_page_1")

                self.horizontal_layout = QtWidgets.QGridLayout(self.data_page_1)
                self.horizontal_layout.setObjectName("horizontal_layout")

                self.label_data_page_1 = QtWidgets.QLabel(self.data_page_1)
                self.label_data_page_1.setObjectName("chart_button")
                self.label_data_page_1.setText("Select chart")
                self.horizontal_layout.addWidget(self.label_data_page_1)

                self.data_page_2 = QtWidgets.QWidget()
                self.data_page_2.setObjectName("data_page_2")

                self.data_grid_page_2 = QtWidgets.QGridLayout(self.data_page_2)
                self.data_grid_page_2.setObjectName("data_grid_page_2")

                self.data_grid_page_2.setContentsMargins(3.5, 5, 3.5, 10)
                self.data_grid_page_2.setSpacing(0)

                global dock_data
                dock_data = chartMenu.Data(self.data_page_2, self.data_grid_page_2, self.central_layout)
                dock_data.contain()

                self.stacked_widget_data.addWidget(self.data_page_1)
                self.stacked_widget_data.addWidget(self.data_page_2)

                self.stacked_widget_data.setCurrentIndex(0)

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_data)

        def right_down(self):
                self.dockWidget_settings = QtWidgets.QDockWidget(self.main_window_in_class)

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

                self.settings_page_1 = QtWidgets.QWidget()
                self.settings_page_1.setObjectName("settings_page_1")

                self.settings_grid_page_1 = QtWidgets.QVBoxLayout(self.settings_page_1)
                self.settings_grid_page_1.setObjectName("settings_grid_page_1")

                self.label_default = QtWidgets.QLabel(self.settings_page_1)
                self.label_default.setObjectName("label_default")
                self.label_default.setText("Select chart")
                self.settings_grid_page_1.addWidget(self.label_default)

                self.settings_page_2 = QtWidgets.QWidget()
                self.settings_page_2.setObjectName("settings_page_2")

                self.settings_grid_page_2  = QtWidgets.QGridLayout(self.settings_page_2)
                self.settings_grid_page_2.setObjectName("settings_grid_page_2")

                self.settings_grid_page_2.setContentsMargins(0, 0, 0, 0)
                self.settings_grid_page_1.setSpacing(0)

                global dock_settings
                dock_settings = chartMenu.Settings(self.settings_page_2, self.settings_grid_page_2, self.central_layout)
                dock_settings.contain()

                self.stacked_widget_settings.addWidget(self.settings_page_1)
                self.stacked_widget_settings.addWidget(self.settings_page_2)

                self.stacked_widget_settings.setCurrentIndex(0)

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_settings)

        def left_chart(self):
                self.dock_widget_chart = QtWidgets.QDockWidget(self.main_window_in_class)
                self.dock_widget_chart.setMinimumSize(QtCore.QSize(145, 163))
                self.dock_widget_chart.setObjectName("dock_widget_chart")

                self.dock_widget_chart_contents = QtWidgets.QWidget()
                self.dock_widget_chart.setWidget(self.dock_widget_chart_contents)

                self.grid_chart_dock = QtWidgets.QHBoxLayout(self.dock_widget_chart_contents)


                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget_chart)
                chart_list = chartList.Chart(
                                             self.grid_chart_dock,
                                             self.dockWidget_data_contents,
                                             self.stacked_widget_data,
                                             self.stacked_widget_settings)




