from PyQt5 import QtCore, QtWidgets
import chart, dockData


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

                dock_data = dockData.Data(self.data_page_2, self.data_grid_page_2, self.central_layout)
                dock_data.write_data()

                self.stacked_widget_data.addWidget(self.data_page_1)
                self.stacked_widget_data.addWidget(self.data_page_2)

                self.stacked_widget_data.setCurrentIndex(0)

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_data)

        def right_down(self):
                self.dockWidget_features = QtWidgets.QDockWidget(self.main_window_in_class)

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.dockWidget_features.sizePolicy().hasHeightForWidth())

                self.dockWidget_features.setSizePolicy(sizePolicy)
                self.dockWidget_features.setMinimumSize(QtCore.QSize(150, 50))
                self.dockWidget_features.setObjectName("dockWidget_features")

                self.dockWidget_features_contentsontents = QtWidgets.QWidget()
                self.dockWidget_features_contentsontents.setObjectName("ddockWidget_features_contentsontents")
                self.dockWidget_features.setWidget(self.dockWidget_features_contentsontents)

                self.grid_features_dock = QtWidgets.QHBoxLayout(self.dockWidget_features_contentsontents)
                self.grid_features_dock.setObjectName("grid_features_dock")

                self.stacked_widget_features = QtWidgets.QStackedWidget(self.dockWidget_features_contentsontents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
                sizePolicy.setHeightForWidth(self.stacked_widget_features.sizePolicy().hasHeightForWidth())
                self.stacked_widget_features.setSizePolicy(sizePolicy)
                self.stacked_widget_features.setObjectName("stacked_widget_features")
                self.grid_features_dock.addWidget(self.stacked_widget_features)

                self.features_page_1 = QtWidgets.QWidget()
                self.features_page_1.setObjectName("features_page_1")

                self.features_grid_page_1 = QtWidgets.QVBoxLayout(self.features_page_1)
                self.features_grid_page_1.setObjectName("features_grid_page_1")

                self.label_default = QtWidgets.QLabel(self.features_page_1)
                self.label_default.setObjectName("label_default")
                self.label_default.setText("Select chart")
                self.features_grid_page_1.addWidget(self.label_default)


                self.features_page_2 = QtWidgets.QWidget()
                self.features_page_2.setObjectName("features_page_2")


                self.features_grid_page_2  = QtWidgets.QGridLayout(self.features_page_2)
                self.features_grid_page_2.setObjectName("features_grid_page_2")

                dock_data2 = dockData.Data(self.features_page_2, self.features_grid_page_2, self.central_layout)
                dock_data2.futures_chart()

                self.button_create = QtWidgets.QPushButton(self.features_page_2)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHeightForWidth(self.button_create.sizePolicy().hasHeightForWidth())
                self.button_create.setSizePolicy(sizePolicy)
                self.button_create.setObjectName("button_create")
                self.button_create.setText("Create")
                self.features_grid_page_2.addWidget(self.button_create, 1, 0, 1, 1, QtCore.Qt.AlignLeft)

                self.stacked_widget_features.addWidget(self.features_page_1)
                self.stacked_widget_features.addWidget(self.features_page_2)

                self.stacked_widget_features.setCurrentIndex(1)

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_features)

        def left_chart(self):
                self.dock_widget_chart = QtWidgets.QDockWidget(self.main_window_in_class)
                self.dock_widget_chart.setMinimumSize(QtCore.QSize(133, 163))
                self.dock_widget_chart.setObjectName("dock_widget_chart")

                self.dock_widget_chart_contents = QtWidgets.QWidget()
                self.dock_widget_chart_contents.setObjectName("dockWidgetChartContents")

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget_chart)
                ss = chart.Chart(self.dock_widget_chart_contents, self.dock_widget_chart, self.dockWidget_data_contents,
                                 self.stacked_widget_data)






