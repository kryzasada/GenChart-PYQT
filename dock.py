from PyQt5 import QtCore, QtWidgets
import chart, dockData


class Dock():
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

                self.page_3 = QtWidgets.QWidget()
                self.page_3.setObjectName("page_3")

                self.stacked_widget_data.addWidget(self.data_page_1)
                self.stacked_widget_data.addWidget(self.data_page_2)
                self.stacked_widget_data.addWidget(self.page_3)

                self.stacked_widget_data.setCurrentIndex(0)

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_data)

        def right_down(self):
                self.dockWidget_2 = QtWidgets.QDockWidget(self.main_window_in_class)

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())

                self.dockWidget_2.setSizePolicy(sizePolicy)
                self.dockWidget_2.setMinimumSize(QtCore.QSize(150, 50))
                self.dockWidget_2.setObjectName("dockWidget_2")

                self.dockWidgetContents_2 = QtWidgets.QWidget()
                self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
                self.dockWidget_2.setWidget(self.dockWidgetContents_2)

                self.grid_features_dock = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
                self.grid_features_dock.setObjectName("horizontalLayout_2")

                self.stacked_widget_dock = QtWidgets.QStackedWidget(self.dockWidgetContents_2)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.stacked_widget_dock.sizePolicy().hasHeightForWidth())
                self.stacked_widget_dock.setSizePolicy(sizePolicy)
                self.stacked_widget_dock.setObjectName("stacked_widget_dock")

                self.page_2_stack = QtWidgets.QWidget()
                self.page_2_stack.setObjectName("page_2_stack")
                self.stacked_widget_dock.addWidget(self.page_2_stack)

                self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2_stack)
                self.gridLayout_3.setObjectName("gridLayout_3")

                ###
                self.tab_widget_features = QtWidgets.QTabWidget(self.page_2_stack)
                self.tab_widget_features.setObjectName("tab_widget_features")

                self.page_color = QtWidgets.QWidget()
                self.page_color.setObjectName("page_color")

                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_color)
                self.verticalLayout_2.setObjectName("verticalLayout_2")

                self.scroll_area_color = QtWidgets.QScrollArea(self.page_color)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.scroll_area_color.sizePolicy().hasHeightForWidth())
                self.scroll_area_color.setSizePolicy(sizePolicy)
                self.scroll_area_color.setWidgetResizable(True)
                self.scroll_area_color.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                self.scroll_area_color.setObjectName("scroll_area_color")

                self.scroll_contents_color = QtWidgets.QWidget()
                self.scroll_contents_color.setGeometry(QtCore.QRect(0, 0, 103, 450))
                self.scroll_contents_color.setObjectName("scroll_contents_color")

                self.formLayout = QtWidgets.QFormLayout(self.scroll_contents_color)
                self.formLayout.setObjectName("formLayout")

                '''    
                self.label1_col = QtWidgets.QLabel(self.scroll_contents_color)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label1_col.sizePolicy().hasHeightForWidth())
                self.label1_col.setSizePolicy(sizePolicy)
                self.label1_col.setObjectName("label1_col")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1_col) '''

                """                self.color_button1 = QtWidgets.QPushButton(self.scroll_contents_color)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.color_button1.sizePolicy().hasHeightForWidth())
                self.color_button1.setSizePolicy(sizePolicy)
                self.color_button1.setStyleSheet("background-color: rgb(170, 0, 0);")
                self.color_button1.setText("")
                self.color_button1.setObjectName("color_button1")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.color_button1)"""

                """self.label2_col = QtWidgets.QLabel(self.scroll_contents_color)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label2_col.sizePolicy().hasHeightForWidth())
                self.label2_col.setSizePolicy(sizePolicy)
                self.label2_col.setObjectName("label2_col")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2_col) """

                """self.color_button2 = QtWidgets.QPushButton(self.scroll_contents_color)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.color_button2.sizePolicy().hasHeightForWidth())
                self.color_button2.setSizePolicy(sizePolicy)
                self.color_button2.setStyleSheet("background-color: rgb(170, 0, 0);")
                self.color_button2.setText("")
                self.color_button2.setObjectName("color_button2")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.color_button2)"""

                self.scroll_area_color.setWidget(self.scroll_contents_color)
                self.verticalLayout_2.addWidget(self.scroll_area_color)
                self.tab_widget_features.addTab(self.page_color, "")
                self.page_explode = QtWidgets.QWidget()
                self.page_explode.setObjectName("page_explode")

                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_explode)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")

                self.scroll_area_explode = QtWidgets.QScrollArea(self.page_explode)
                self.scroll_area_explode.setWidgetResizable(True)
                self.scroll_area_explode.setObjectName("scroll_area_explode")

                self.scroll_contents_explode = QtWidgets.QWidget()
                self.scroll_contents_explode.setGeometry(QtCore.QRect(-58, 0, 126, 450))
                self.scroll_contents_explode.setObjectName("scroll_contents_explode")

                self.formLayout_2 = QtWidgets.QFormLayout(self.scroll_contents_explode)
                self.formLayout_2.setObjectName("formLayout_2")

                self.label2_expl = QtWidgets.QLabel(self.scroll_contents_explode)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label2_expl.sizePolicy().hasHeightForWidth())
                self.label2_expl.setSizePolicy(sizePolicy)
                self.label2_expl.setObjectName("label2_expl")

                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2_expl)

                self.label1_expl = QtWidgets.QLabel(self.scroll_contents_explode)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label1_expl.sizePolicy().hasHeightForWidth())
                self.label1_expl.setSizePolicy(sizePolicy)
                self.label1_expl.setObjectName("label1_expl")

                self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1_expl)

                self.double_spin_box2 = QtWidgets.QDoubleSpinBox(self.scroll_contents_explode)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.double_spin_box2.sizePolicy().hasHeightForWidth())
                self.double_spin_box2.setSizePolicy(sizePolicy)
                self.double_spin_box2.setObjectName("double_spin_box2")

                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.double_spin_box2)

                self.double_spin_box1 = QtWidgets.QDoubleSpinBox(self.scroll_contents_explode)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.double_spin_box1.sizePolicy().hasHeightForWidth())
                self.double_spin_box1.setSizePolicy(sizePolicy)

                self.double_spin_box1.setObjectName("double_spin_box1")
                self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.double_spin_box1)
                self.scroll_area_explode.setWidget(self.scroll_contents_explode)
                self.horizontalLayout_3.addWidget(self.scroll_area_explode)
                self.tab_widget_features.addTab(self.page_explode, "")
                self.page_settings = QtWidgets.QWidget()
                self.page_settings.setObjectName("page_settings")

                self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_settings)
                self.horizontalLayout.setObjectName("horizontalLayout")

                self.scroll_area_settings = QtWidgets.QScrollArea(self.page_settings)
                self.scroll_area_settings.setWidgetResizable(True)
                self.scroll_area_settings.setObjectName("scroll_area_settings")

                self.scroll_contents_settings = QtWidgets.QWidget()
                self.scroll_contents_settings.setGeometry(QtCore.QRect(0, 0, 94, 450))
                self.scroll_contents_settings.setObjectName("scroll_contents_settings")

                self.formLayout_3 = QtWidgets.QFormLayout(self.scroll_contents_settings)
                self.formLayout_3.setObjectName("formLayout_3")

                self.check_box1_set = QtWidgets.QCheckBox(self.scroll_contents_settings)
                self.check_box1_set.setObjectName("check_box1_set")

                self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check_box1_set)
                self.check_box2_set = QtWidgets.QCheckBox(self.scroll_contents_settings)
                self.check_box2_set.setObjectName("check_box2_set")

                self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.check_box2_set)

                self.scroll_area_settings.setWidget(self.scroll_contents_settings)

                self.horizontalLayout.addWidget(self.scroll_area_settings)

                self.tab_widget_features.addTab(self.page_settings, "")

                self.gridLayout_3.addWidget(self.tab_widget_features, 0, 0, 1, 1)

                self.button_create = QtWidgets.QPushButton(self.page_2_stack)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.button_create.sizePolicy().hasHeightForWidth())
                self.button_create.setSizePolicy(sizePolicy)
                self.button_create.setCheckable(False)
                self.button_create.setAutoDefault(False)
                self.button_create.setDefault(False)
                self.button_create.setFlat(False)
                self.button_create.setObjectName("button_create")

                self.gridLayout_3.addWidget(self.button_create, 1, 0, 1, 1, QtCore.Qt.AlignLeft)

                self.stacked_widget_dock.addWidget(self.page_2_stack)

                self.page_1_stack = QtWidgets.QWidget()
                self.page_1_stack.setObjectName("page_1_stack")

                self.verticalLayout = QtWidgets.QVBoxLayout(self.page_1_stack)
                self.verticalLayout.setObjectName("verticalLayout")
                self.default_label = QtWidgets.QLabel(self.page_1_stack)
                self.default_label.setObjectName("default_label")

                """dock_settings = dockData.Data(self.stacked_widget_data,
                                          self.central_layout,self.central_layout,self.central_layout )

                dock_settings.settings_chart()"""

                self.verticalLayout.addWidget(self.default_label)

                self.stacked_widget_dock.addWidget(self.page_1_stack)
                self.grid_features_dock.addWidget(self.stacked_widget_dock)
                self.dockWidget_2.setWidget(self.dockWidgetContents_2)

                self.retranslateUi(self.main_window_in_class)
                self.stacked_widget_dock.setCurrentIndex(0)
                self.tab_widget_features.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(self.main_window_in_class)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.tab_widget_features.setTabText(self.tab_widget_features.indexOf(self.page_color),
                                                    _translate("MainWindow", "Color"))
                self.label2_expl.setText(_translate("MainWindow", "TextLabel"))
                self.label1_expl.setText(_translate("MainWindow", "TextLabel"))
                self.tab_widget_features.setTabText(self.tab_widget_features.indexOf(self.page_explode),
                                                    _translate("MainWindow", "Explode"))
                self.check_box1_set.setText(_translate("MainWindow", "CheckBox"))
                self.check_box2_set.setText(_translate("MainWindow", "CheckBox"))
                self.tab_widget_features.setTabText(self.tab_widget_features.indexOf(self.page_settings),
                                                    _translate("MainWindow", "Settings"))
                self.button_create.setText(_translate("MainWindow", "CREATE"))
                self.default_label.setText(_translate("MainWindow", "TextLabel"))






                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)

        def left_chart(self):
                self.dock_widget_chart = QtWidgets.QDockWidget(self.main_window_in_class)
                self.dock_widget_chart.setMinimumSize(QtCore.QSize(133, 163))
                self.dock_widget_chart.setObjectName("dock_widget_chart")

                self.dock_widget_chart_contents = QtWidgets.QWidget()
                self.dock_widget_chart_contents.setObjectName("dockWidgetChartContents")

                self.main_window_in_class.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_widget_chart)
                ss = chart.Chart(self.dock_widget_chart_contents, self.dock_widget_chart, self.dockWidget_data_contents,
                                 self.stacked_widget_data)






