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

                ###
                self.tab_widget = QtWidgets.QTabWidget(self.features_page_2)
                self.tab_widget.setObjectName("tab_widget")
                self.features_grid_page_2.addWidget(self.tab_widget, 0, 0, 1, 1)


                self.page_color = QtWidgets.QWidget()
                self.page_color.setObjectName("page_color")
                self.tab_widget.addTab(self.page_color, "Color")

                self.page_color_layout = QtWidgets.QVBoxLayout(self.page_color)
                self.page_color_layout.setObjectName("page_color_layout")

                self.scroll_area_color = QtWidgets.QScrollArea(self.page_color)
                self.scroll_area_color.setWidgetResizable(True)
                self.scroll_area_color.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.scroll_area_color.setObjectName("scroll_area_color")
                self.page_color_layout.addWidget(self.scroll_area_color)

                self.scroll_color_contents = QtWidgets.QWidget()
                self.scroll_color_contents.setGeometry(QtCore.QRect(0, 0, 103, 450))
                self.scroll_color_contents.setObjectName("scroll_color_contents")
                self.scroll_area_color.setWidget(self.scroll_color_contents)

                self.scroll_color_layout = QtWidgets.QFormLayout(self.scroll_color_contents)
                self.scroll_color_layout.setObjectName("scroll_color_layout")

                ###
                self.label1_color = QtWidgets.QLabel(self.scroll_color_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label1_color.sizePolicy().hasHeightForWidth())
                self.label1_color.setSizePolicy(sizePolicy)
                self.label1_color.setObjectName("label1_color")
                self.label1_color.setText("123")
                self.scroll_color_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1_color)

                self.button1_color = QtWidgets.QPushButton(self.scroll_color_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.button1_color.sizePolicy().hasHeightForWidth())
                self.button1_color.setSizePolicy(sizePolicy)
                self.button1_color.setStyleSheet("background-color: rgb(170, 0, 0);")
                self.button1_color.setText("")
                self.button1_color.setObjectName("button1_color")
                self.scroll_color_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.button1_color)

                self.label2_color = QtWidgets.QLabel(self.scroll_color_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label2_color.sizePolicy().hasHeightForWidth())
                self.label2_color.setSizePolicy(sizePolicy)
                self.label2_color.setObjectName("label2_color")
                self.label2_color.setText("123")
                self.scroll_color_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2_color)

                self.button2_color = QtWidgets.QPushButton(self.scroll_color_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.button2_color.sizePolicy().hasHeightForWidth())
                self.button2_color.setSizePolicy(sizePolicy)
                self.button2_color.setStyleSheet("background-color: rgb(170, 0, 0);")
                self.button2_color.setText("")
                self.button2_color.setObjectName("button2_color")
                self.scroll_color_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.button2_color)

                self.page_explode = QtWidgets.QWidget()
                self.page_explode.setObjectName("page_explode")
                self.tab_widget.addTab(self.page_explode, "Explode")

                self.page_explode_layout = QtWidgets.QHBoxLayout(self.page_explode)
                self.page_explode_layout.setObjectName("page_explode_layout")

                self.scroll_area_explode = QtWidgets.QScrollArea(self.page_explode)
                self.scroll_area_explode.setWidgetResizable(True)
                self.scroll_area_explode.setObjectName("scroll_area_explode")
                self.page_explode_layout.addWidget(self.scroll_area_explode)

                self.scroll_explode_contents = QtWidgets.QWidget()
                self.scroll_explode_contents.setGeometry(QtCore.QRect(-58, 0, 126, 450))
                self.scroll_explode_contents.setObjectName("scroll_explode_contents")

                self.scroll_area_explode.setWidget(self.scroll_explode_contents)
                self.scroll_explode_layout = QtWidgets.QFormLayout(self.scroll_explode_contents)
                self.scroll_explode_layout.setObjectName("scroll_explode_layout")

                self.label1_explode = QtWidgets.QLabel(self.scroll_explode_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHeightForWidth(self.label1_explode.sizePolicy().hasHeightForWidth())
                self.label1_explode.setSizePolicy(sizePolicy)
                self.label1_explode.setObjectName("label1_explode")
                self.label1_explode.setText("TextLabel_1")
                self.scroll_explode_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1_explode)

                self.label2_explode = QtWidgets.QLabel(self.scroll_explode_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHeightForWidth(self.label2_explode.sizePolicy().hasHeightForWidth())
                self.label2_explode.setSizePolicy(sizePolicy)
                self.label2_explode.setObjectName("label2_explode")
                self.label2_explode.setText("TextLabel_2")
                self.scroll_explode_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2_explode)

                self.double_spin1_explode = QtWidgets.QDoubleSpinBox(self.scroll_explode_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.double_spin1_explode.sizePolicy().hasHeightForWidth())
                self.double_spin1_explode.setSizePolicy(sizePolicy)
                self.double_spin1_explode.setObjectName("double_spin1_explode")

                self.scroll_explode_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.double_spin1_explode)

                self.double_spin2_explode = QtWidgets.QDoubleSpinBox(self.scroll_explode_contents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.double_spin2_explode.sizePolicy().hasHeightForWidth())
                self.double_spin2_explode.setSizePolicy(sizePolicy)
                self.double_spin2_explode.setObjectName("double_spin2_explode")
                self.scroll_explode_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.double_spin2_explode)


                self.page_settings = QtWidgets.QWidget()
                self.page_settings.setObjectName("page_settings")
                self.tab_widget.addTab(self.page_settings, "Settings")

                self.page_settings_layout = QtWidgets.QHBoxLayout(self.page_settings)
                self.page_settings_layout.setObjectName("page_settings_layout")

                self.scroll_area_settings = QtWidgets.QScrollArea(self.page_settings)
                self.scroll_area_settings.setWidgetResizable(True)
                self.scroll_area_settings.setObjectName("scroll_area_settings")
                self.page_settings_layout.addWidget(self.scroll_area_settings)

                self.scroll_settings_contents = QtWidgets.QWidget()
                self.scroll_settings_contents.setGeometry(QtCore.QRect(0, 0, 94, 450))
                self.scroll_settings_contents.setObjectName("scroll_settings_contents")
                self.scroll_area_settings.setWidget(self.scroll_settings_contents)

                self.scroll_settings_layout = QtWidgets.QFormLayout(self.scroll_settings_contents)
                self.scroll_settings_layout.setObjectName("scroll_settings_layout")

                self.check_box1_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
                self.check_box1_settings.setObjectName("check_box1_settings")
                self.check_box1_settings.setText("CheckBox_1")
                self.scroll_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check_box1_settings)


                self.check_box2_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
                self.check_box2_settings.setObjectName("check_box2_settings")
                self.check_box2_settings.setText("CheckBox_2")
                self.scroll_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.check_box2_settings)


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
                self.tab_widget.setCurrentIndex(0)

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






