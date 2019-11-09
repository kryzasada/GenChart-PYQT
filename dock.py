from PyQt5 import QtCore, QtWidgets
import chart, dockData


class Dock():
        def __init__(self, *args):
                self.main_window_in_class = args[0]
                self.central_layout = args[1]

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

                self.grid_dock = QtWidgets.QGridLayout(self.dockWidget_1Contents)
                self.grid_dock.setContentsMargins(0, 0, 0, 0)
                self.grid_dock.setObjectName("grid_dock")

                self.stacked_Widget = QtWidgets.QStackedWidget(self.dockWidget_1Contents)
                self.stacked_Widget.setObjectName("stacked_Widget")
                self.grid_dock.addWidget(self.stacked_Widget, 0, 0, 1, 1)


                self.page_1 = QtWidgets.QWidget()
                self.page_1.setObjectName("page_1")

                self.horizontal_layout = QtWidgets.QGridLayout(self.page_1)
                self.horizontal_layout.setObjectName("horizontal_layout")

                self.label_page_1 = QtWidgets.QLabel(self.page_1)
                self.label_page_1.setObjectName("chart_button")
                self.label_page_1.setText("Select chart")
                self.horizontal_layout.addWidget(self.label_page_1)


                self.page_2 = QtWidgets.QWidget()
                self.page_2.setObjectName("page_2")

                self.grid_page_2 = QtWidgets.QGridLayout(self.page_2)
                self.grid_page_2.setObjectName("grid_page_2")
                self.scroll_area = QtWidgets.QScrollArea(self.page_2)

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())

                self.scroll_area.setSizePolicy(sizePolicy)
                self.scroll_area.setWidgetResizable(True)
                self.scroll_area.setObjectName("scroll_area")
                self.scroll_area_widget_contents = QtWidgets.QWidget()
                self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 153, 523))
                self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
                self.grid_page_2.addWidget(self.scroll_area, 0, 0, 1, 1)

                self.form_layout = QtWidgets.QFormLayout(self.scroll_area_widget_contents)
                self.form_layout.setObjectName("form_layout")

                dock_data = dockData.Data(self.form_layout, self.scroll_area_widget_contents, self.stacked_Widget,
                                          self.central_layout)

                self.page_3 = QtWidgets.QWidget()
                self.page_3.setObjectName("page_3")


                self.stacked_Widget.addWidget(self.page_1)
                self.stacked_Widget.addWidget(self.page_2)
                self.stacked_Widget.addWidget(self.page_3)

                self.stacked_Widget.setCurrentIndex(0)
                self.scroll_area.setWidget(self.scroll_area_widget_contents)

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
                self.dock_widget_chart = QtWidgets.QDockWidget(self.main_window_in_class)
                self.dock_widget_chart.setMinimumSize(QtCore.QSize(133, 163))
                self.dock_widget_chart.setObjectName("dock_widget_chart")

                self.dock_widget_chart_contents = QtWidgets.QWidget()
                self.dock_widget_chart_contents.setObjectName("dockWidgetChartContents")

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget_chart)
                ss = chart.Chart(self.dock_widget_chart_contents, self.dock_widget_chart, self.dockWidget_1Contents,
                                 self.stacked_Widget)






