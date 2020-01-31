# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial
import random
import time

import dock, generateChart


class DataPage1:
    def __init__(self, *args):
        self.page = args[0]
        self.grid_page = args[1]
        self.central_layout = args[2]

        self.chart_type = 0

    def contain(self):
        self.scroll_area = QtWidgets.QScrollArea(self.page)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())

        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 153, 523))
        self.scroll_area_contents.setObjectName("scroll_area_contents")

        self.grid_page.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.data_scroll_layout = QtWidgets.QFormLayout(self.scroll_area_contents)
        self.data_scroll_layout.setContentsMargins(0, 5, 0, 0)
        self.data_scroll_layout.setHorizontalSpacing(2)
        self.data_scroll_layout.setVerticalSpacing(2)
        self.data_scroll_layout.setObjectName("data_scroll_layout")

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        """Create default menu in data/value dock"""

        " Upper main label layout"
        self.upper_first_layout = QtWidgets.QFormLayout()
        self.upper_first_layout.setObjectName("upper_first_layout")
        self.upper_first_layout.setContentsMargins(0, 0, 0, 0)
        self.upper_first_layout.setHorizontalSpacing(2)
        self.upper_first_layout.setVerticalSpacing(2)
        self.data_scroll_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.upper_first_layout)

        " Upper label layout - label name"
        self.upper__TextName_layout = QtWidgets.QFormLayout()
        self.upper__TextName_layout.setContentsMargins(0, 0, 0, 0)
        self.upper__TextName_layout.setHorizontalSpacing(5)
        self.upper__TextName_layout.setVerticalSpacing(2)
        self.upper__TextName_layout.setObjectName("upper__TextName_layout")
        self.upper_first_layout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.upper__TextName_layout)

        " Label Name and check"
        self.upper__TextName_label = QtWidgets.QLabel(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.upper__TextName_label.sizePolicy().hasHeightForWidth())
        self.upper__TextName_label.setSizePolicy(sizePolicy)
        self.upper__TextName_label.setMinimumSize(QtCore.QSize(65, 0))
        self.upper__TextName_label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.upper__TextName_label.setText("Name")
        self.upper__TextName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.upper__TextName_label.setObjectName("upper__TextName_label")
        self.upper__TextName_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.upper__TextName_label)

        self.upper__TextName_check = QtWidgets.QCheckBox(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.upper__TextName_check.sizePolicy().hasHeightForWidth())
        self.upper__TextName_check.setSizePolicy(sizePolicy)
        self.upper__TextName_check.setMinimumSize(QtCore.QSize(15, 20))
        self.upper__TextName_check.setMaximumSize(QtCore.QSize(15, 0))
        self.upper__TextName_check.setText("")
        self.upper__TextName_check.setChecked(True)
        self.upper__TextName_check.setObjectName("upper__TextName_check")
        self.upper__TextName_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.upper__TextName_check)
        self.upper__TextName_check.stateChanged.connect(lambda: self.check_display("Name"))

        " Upper label layout - label value"
        self.upper__TextValue_layout = QtWidgets.QFormLayout()
        self.upper__TextValue_layout.setContentsMargins(0, 0, 0, 0)
        self.upper__TextValue_layout.setHorizontalSpacing(5)
        self.upper__TextValue_layout.setVerticalSpacing(2)
        self.upper__TextValue_layout.setObjectName("upper__TextValue_layout")
        self.upper_first_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.upper__TextValue_layout)

        " Label Value and check"
        self.upper__TextValue_label = QtWidgets.QLabel(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.upper__TextValue_label.sizePolicy().hasHeightForWidth())
        self.upper__TextValue_label.setSizePolicy(sizePolicy)
        self.upper__TextValue_label.setMinimumSize(QtCore.QSize(50, 20))
        self.upper__TextValue_label.setMaximumSize(QtCore.QSize(20, 16777215))
        self.upper__TextValue_label.setText("Value")
        self.upper__TextValue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.upper__TextValue_label.setObjectName("upper__TextValue_label")
        self.upper__TextValue_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.upper__TextValue_label)

        self.upper_TextValue_check = QtWidgets.QCheckBox(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHeightForWidth(self.upper_TextValue_check.sizePolicy().hasHeightForWidth())
        self.upper_TextValue_check.setSizePolicy(sizePolicy)
        self.upper_TextValue_check.setMinimumSize(QtCore.QSize(15, 20))
        self.upper_TextValue_check.setMaximumSize(QtCore.QSize(15, 20))
        self.upper_TextValue_check.setText("")
        self.upper_TextValue_check.setChecked(True)
        self.upper_TextValue_check.setObjectName("upper_TextValue_check")
        self.upper__TextValue_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.upper_TextValue_check)
        self.upper_TextValue_check.stateChanged.connect(lambda: self.check_display("Value"))

        " Layout write name and check"
        self.upper_first_Name_layout = QtWidgets.QFormLayout()
        self.upper_first_Name_layout.setContentsMargins(0, 0, 0, 0)
        self.upper_first_Name_layout.setHorizontalSpacing(5)
        self.upper_first_Name_layout.setVerticalSpacing(2)
        self.upper_first_Name_layout.setObjectName("upper_first_Name_layout")
        self.upper_first_layout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.upper_first_Name_layout)

        " Line edit - write name and check"
        self.upper_first_Name_write = QtWidgets.QLineEdit(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.upper_first_Name_write.sizePolicy().hasHeightForWidth())
        self.upper_first_Name_write.setSizePolicy(sizePolicy)
        self.upper_first_Name_write.setMinimumSize(QtCore.QSize(65, 20))
        self.upper_first_Name_write.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.upper_first_Name_write.setText("def_1")
        self.upper_first_Name_write.setObjectName("upper_first_Name_write")
        self.upper_first_Name_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.upper_first_Name_write)

        self.upper_first_Name_check = QtWidgets.QCheckBox(self.scroll_area_contents)
        self.upper_first_Name_check.setSizePolicy(sizePolicy)
        self.upper_first_Name_check.setMinimumSize(QtCore.QSize(15, 20))
        self.upper_first_Name_check.setMaximumSize(QtCore.QSize(15, 20))
        self.upper_first_Name_check.setText("")
        self.upper_first_Name_check.setChecked(True)
        self.upper_first_Name_check.setObjectName("upper_first_Name_check")
        self.upper_first_Name_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.upper_first_Name_check)

        self.upper_first_Name_line = QtWidgets.QFrame(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.upper_first_Name_line.sizePolicy().hasHeightForWidth())
        self.upper_first_Name_line.setSizePolicy(sizePolicy)
        self.upper_first_Name_line.setMinimumSize(QtCore.QSize(65, 1))
        self.upper_first_Name_line.setMaximumSize(QtCore.QSize(120, 0))
        self.upper_first_Name_line.setLineWidth(-1)
        self.upper_first_Name_line.setObjectName("upper_first_Name_line")
        self.upper_first_Name_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.upper_first_Name_line)

        " Layout value and check"
        self.upper_first_value_layout = QtWidgets.QFormLayout()
        self.upper_first_value_layout.setContentsMargins(0, 0, 0, 0)
        self.upper_first_value_layout.setHorizontalSpacing(5)
        self.upper_first_value_layout.setVerticalSpacing(2)
        self.upper_first_value_layout.setObjectName("upper_first_value_layout")
        self.upper_first_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.upper_first_value_layout)
        self.data_scroll_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.upper_first_layout)

        " Spix Box - value name and check"
        self.upper_first_value_spinBox = QtWidgets.QDoubleSpinBox(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.upper_first_value_spinBox.sizePolicy().hasHeightForWidth())
        self.upper_first_value_spinBox.setSizePolicy(sizePolicy)
        self.upper_first_value_spinBox.setMinimumSize(QtCore.QSize(50, 20))
        self.upper_first_value_spinBox.setMinimum(-9999999999.99)
        self.upper_first_value_spinBox.setMaximum(9999999999.99)
        self.upper_first_value_spinBox.setValue(1.00)
        self.upper_first_value_spinBox.setObjectName("upper_first_value_spinBox")
        self.upper_first_value_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.upper_first_value_spinBox)

        self.upper_first_value_check = QtWidgets.QCheckBox(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHeightForWidth(self.upper_first_value_check.sizePolicy().hasHeightForWidth())
        self.upper_first_value_check.setSizePolicy(sizePolicy)
        self.upper_first_value_check.setMinimumSize(QtCore.QSize(15, 20))
        self.upper_first_value_check.setMaximumSize(QtCore.QSize(15, 20))
        self.upper_first_value_check.setText("")
        self.upper_first_value_check.setChecked(True)
        self.upper_first_value_check.setObjectName("upper_first_value_check")
        self.upper_first_value_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.upper_first_value_check)

        self.upper_first_value_line = QtWidgets.QFrame(self.scroll_area_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.upper_first_value_line.sizePolicy().hasHeightForWidth())
        self.upper_first_value_line.setSizePolicy(sizePolicy)
        self.upper_first_value_line.setMinimumSize(QtCore.QSize(50, 1))
        self.upper_first_value_line.setMaximumSize(QtCore.QSize(120, 0))
        self.upper_first_value_line.setLineWidth(-1)
        self.upper_first_value_line.setObjectName("upper_first_value_line")
        self.upper_first_value_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.upper_first_value_line)

        self.space = QtWidgets.QFrame(self.scroll_area_contents)
        self.space.setMinimumSize(QtCore.QSize(0, 5))
        self.space.setMaximumSize(QtCore.QSize(0, 5))
        self.space.setLineWidth(0)
        self.upper_first_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.space)

        self.add_data = []
        self.button_Add = QtWidgets.QPushButton(self.scroll_area_contents)
        self.button_Add.setSizePolicy(self.sizePolicy)
        self.button_Add.setObjectName("pushButton")
        self.button_Add.setMaximumSize(QtCore.QSize(65, 20))
        self.button_Add.setMinimumSize(QtCore.QSize(65, 20))
        self.button_Add.setText("ADD DATA")

        self.upper_first_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.button_Add)
        self.button_Add.clicked.connect(lambda: self.add_data.append(self.AddData()))
        self.button_Add.clicked.connect(lambda: self.add_data[-1].buttons_positions())

        self.button_Create = QtWidgets.QPushButton(self.scroll_area_contents)
        self.button_Create.setObjectName("button_Create")
        self.button_Create.setMinimumSize(QtCore.QSize(65, 20))
        self.button_Create.setMaximumSize(QtCore.QSize(65, 20))
        self.upper_first_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.button_Create)
        self.button_Create.setText("CREATE")

        self.button_Create.clicked.connect(lambda:
                                           True if not self.chart_type.count('pie')
                                           else generateChart.PieChart(self.chart_type))

        self.button_Create.clicked.connect(lambda:
                                           True if not self.chart_type.count('bar')
                                           else generateChart.BarChart(self.chart_type))

        self.button_Create.clicked.connect(lambda:
                                           True if not self.chart_type.count('line')
                                           else generateChart.LineChart(self.chart_type))

        self.add_data.append(self.AddData())
        self.add_data[-1].buttons_positions()

    def check_display(self, type):
        if type == "Name":
            if self.upper__TextName_check.checkState():
                self.upper_first_Name_check.setChecked(True)
                for x in self.add_data:
                    x.second_block_Name_check.setChecked(True)
            else:
                self.upper_first_Name_check.setChecked(False)
                for x in self.add_data:
                    x.second_block_Name_check.setChecked(False)

        elif type == "Value":
            if self.upper_TextValue_check.checkState():
                self.upper_first_value_check.setChecked(True)
                for x in self.add_data:
                    x.second_block_value_check.setChecked(True)
            else:
                self.upper_first_value_check.setChecked(False)
                for x in self.add_data:
                    x.second_block_value_check.setChecked(False)

    class AddData:
        def __init__(self):
            self.scroll_area_contents = dock.dock_data[1].scroll_area_contents
            self.data_scroll_layout = dock.dock_data[1].data_scroll_layout

            self.int = self.data_scroll_layout.rowCount()
            self.contein()

        def _dell(self):
            dock.dock_data[1].upper_first_layout.setWidget(4,
                                                           QtWidgets.QFormLayout.LabelRole,
                                                           dock.dock_data[1].button_Create)

            dock.dock_data[1].upper_first_layout.setWidget(3,
                                                           QtWidgets.QFormLayout.LabelRole,
                                                           dock.dock_data[1].button_Add)

            dock.dock_data[1].upper_first_layout.setWidget(2,
                                                           QtWidgets.QFormLayout.LabelRole,
                                                           dock.dock_data[1].space)

            self.data_scroll_layout.removeRow(self.int)

            int2 = self.data_scroll_layout.rowCount()
            self.int -= 1

            del dock.dock_data[1].add_data[self.int]

            int1 = self.int
            while int1 <= int2:
                try:
                    dock.dock_data[1].add_data[int1].int = int1 + 1
                    int1 += 1

                except :
                    break

            self.buttons_positions()

            """ Delete widget in settings: Page_1"""
            dock.dock_settings[1].scroll_color_layout.removeRow(self.int+1)
            del dock.dock_settings[1].label_color[self.int+1]
            del dock.dock_settings[1].buttons_color[self.int+1]

            dock.dock_settings[1].scroll_explode_layout.removeRow(self.int+1)
            del dock.dock_settings[1].label_explode[self.int+1]
            del dock.dock_settings[1].spin_box_explode[self.int+1]

        def contein(self):
            self.second_block_layout = QtWidgets.QFormLayout()
            self.second_block_layout.setObjectName("second_block_layout")
            self.second_block_layout.setContentsMargins(0, 0, 0, 0)
            self.second_block_layout.setHorizontalSpacing(2)
            self.second_block_layout.setVerticalSpacing(2)
            self.data_scroll_layout.setLayout(self.int, QtWidgets.QFormLayout.FieldRole, self.second_block_layout)

            """ Second block layout - line """
            self.button_X = QtWidgets.QPushButton(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHeightForWidth(self.button_X.sizePolicy().hasHeightForWidth())
            self.button_X.setSizePolicy(sizePolicy)
            self.button_X.setMinimumSize(QtCore.QSize(20, 24))
            self.button_X.setMaximumSize(QtCore.QSize(20, 24))
            self.button_X.setIcon(QtGui.QIcon('Image/Other/value_menu_X.png'))
            self.button_X.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: 0;")
            self.button_X.clicked.connect(lambda: self._dell())
            self.data_scroll_layout.setWidget(self.int, QtWidgets.QFormLayout.LabelRole, self.button_X)

            " Second block layout - line "
            self.second_block_line = QtWidgets.QFrame(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(self.second_block_line.sizePolicy().hasHeightForWidth())
            self.second_block_line.setSizePolicy(sizePolicy)
            self.second_block_line.setMinimumSize(QtCore.QSize(85, 1))
            self.second_block_line.setMaximumSize(QtCore.QSize(85, 1))
            self.second_block_line.setLineWidth(-1)
            self.second_block_line.setObjectName("second_block_line")
            self.second_block_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.second_block_line)

            " Layout write name and check in second block "
            self.second_block_Name_layout = QtWidgets.QFormLayout()
            self.second_block_Name_layout.setContentsMargins(0, 0, 0, 0)
            self.second_block_Name_layout.setHorizontalSpacing(5)
            self.second_block_Name_layout.setVerticalSpacing(2)
            self.second_block_Name_layout.setObjectName("second_block_Name_layout")
            self.second_block_layout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.second_block_Name_layout)

            " Line edit - write name and check in second block"
            self.second_block_Name_write = QtWidgets.QLineEdit(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHeightForWidth(self.second_block_Name_write.sizePolicy().hasHeightForWidth())
            self.second_block_Name_write.setSizePolicy(sizePolicy)
            self.second_block_Name_write.setMinimumSize(QtCore.QSize(65, 20))
            self.second_block_Name_write.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.second_block_Name_write.setText("def_" + str(self.int + 1))
            self.second_block_Name_write.setObjectName("second_block_Name_write")
            self.second_block_Name_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.second_block_Name_write)

            self.second_block_Name_check = QtWidgets.QCheckBox(self.scroll_area_contents)
            self.second_block_Name_check.setSizePolicy(sizePolicy)
            self.second_block_Name_check.setMinimumSize(QtCore.QSize(15, 20))
            self.second_block_Name_check.setMaximumSize(QtCore.QSize(15, 20))
            self.second_block_Name_check.setText("")
            self.second_block_Name_check.setChecked(True)
            self.second_block_Name_check.setObjectName("second_block_Name_check")
            self.second_block_Name_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_block_Name_check)

            self.second_block_Name_line = QtWidgets.QFrame(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(self.second_block_Name_line.sizePolicy().hasHeightForWidth())
            self.second_block_Name_line.setSizePolicy(sizePolicy)
            self.second_block_Name_line.setMinimumSize(QtCore.QSize(65, 1))
            self.second_block_Name_line.setMaximumSize(QtCore.QSize(65, 1))
            self.second_block_Name_line.setLineWidth(-1)
            self.second_block_Name_line.setObjectName("second_block_Name_line")
            self.second_block_Name_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.second_block_Name_line)

            " Layout spin Box and check in second block "
            self.second_block_value_layout = QtWidgets.QFormLayout()
            self.second_block_value_layout.setContentsMargins(0, 0, 0, 0)
            self.second_block_value_layout.setHorizontalSpacing(5)
            self.second_block_value_layout.setVerticalSpacing(2)
            self.second_block_value_layout.setObjectName("second_block_value_layout")
            self.second_block_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.second_block_value_layout)

            " Spin box - value and check in second block"
            self.second_block_value_spinBox = QtWidgets.QDoubleSpinBox(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHeightForWidth(self.second_block_value_spinBox.sizePolicy().hasHeightForWidth())
            self.second_block_value_spinBox.setSizePolicy(sizePolicy)
            self.second_block_value_spinBox.setMinimumSize(QtCore.QSize(50, 20))
            self.second_block_value_spinBox.setValue(1.00)
            self.second_block_value_spinBox.setMinimum(-9999999999.99)
            self.second_block_value_spinBox.setMaximum(9999999999.99)
            self.second_block_value_spinBox.setObjectName("second_block_value_spinBox")
            self.second_block_value_layout.setWidget(1,
                                                     QtWidgets.QFormLayout.LabelRole,
                                                     self.second_block_value_spinBox)

            self.second_block_value_check = QtWidgets.QCheckBox(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
            sizePolicy.setHeightForWidth(self.second_block_value_check.sizePolicy().hasHeightForWidth())
            self.second_block_value_check.setSizePolicy(sizePolicy)
            self.second_block_value_check.setMinimumSize(QtCore.QSize(15, 20))
            self.second_block_value_check.setMaximumSize(QtCore.QSize(15, 20))
            self.second_block_value_check.setText("")
            self.second_block_value_check.setChecked(True)
            self.second_block_value_check.setObjectName("second_block_value_check")
            self.second_block_value_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_block_value_check)

            self.second_block_value_line = QtWidgets.QFrame(self.scroll_area_contents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(self.second_block_value_line.sizePolicy().hasHeightForWidth())
            self.second_block_value_line.setSizePolicy(sizePolicy)
            self.second_block_value_line.setMinimumSize(QtCore.QSize(50, 1))
            self.second_block_value_line.setMaximumSize(QtCore.QSize(120, 1))
            self.second_block_value_line.setLineWidth(-1)
            self.second_block_value_line.setObjectName("second_block_value_line_2")
            self.second_block_value_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.second_block_value_line)

            """ Add widget in settings: Page_1"""
            try:
                dock.dock_settings[1].label_color.append(QtWidgets.QLabel())
                dock.dock_settings[1].label_color[-1].setText(self.second_block_Name_write.text())
                dock.dock_settings[1].scroll_color_layout.setWidget(self.int,
                                                                    QtWidgets.QFormLayout.LabelRole,
                                                                    dock.dock_settings[1].label_color[-1])
                self.second_block_Name_write.textChanged.connect(lambda:
                                                                 dock.dock_settings[1].label_color[self.int].setText(
                                                                     self.second_block_Name_write.text()))

                dock.dock_settings[1].buttons_color.append(QtWidgets.QPushButton())
                dock.dock_settings[1].buttons_color[-1].setMinimumSize(QtCore.QSize(35, 20))
                dock.dock_settings[1].buttons_color[-1].setMaximumSize(QtCore.QSize(35, 20))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                dock.dock_settings[1].buttons_color[-1].setSizePolicy(sizePolicy)
                dock.dock_settings[1].scroll_color_layout.setWidget(self.int,
                                                                    QtWidgets.QFormLayout.FieldRole,
                                                                    dock.dock_settings[1].buttons_color[-1])
                dock.dock_settings[1].buttons_color[-1].setStyleSheet("background-color: rgb(%s, %s, %s);"
                                                                      % (random.randint(0, 250),
                                                                         random.randint(0, 250),
                                                                         random.randint(0, 250)))
                dock.dock_settings[1].buttons_color[-1].clicked.connect(lambda:
                                                                        dock.dock_settings[1].button_color(self.int))

                dock.dock_settings[1].label_explode.append(QtWidgets.QLabel())
                dock.dock_settings[1].label_explode[-1].setText(self.second_block_Name_write.text())
                dock.dock_settings[1].scroll_explode_layout.setWidget(self.int,
                                                                      QtWidgets.QFormLayout.LabelRole,
                                                                      dock.dock_settings[1].label_explode[-1])
                self.second_block_Name_write.textChanged.connect(lambda:
                                                                 dock.dock_settings[1].label_explode[self.int].setText(
                                                                     self.second_block_Name_write.text()))

                dock.dock_settings[1].spin_box_explode.append(QtWidgets.QDoubleSpinBox())
                dock.dock_settings[1].spin_box_explode[-1].setMinimumSize(QtCore.QSize(50, 20))
                dock.dock_settings[1].spin_box_explode[-1].setMaximumSize(QtCore.QSize(50, 20))
                dock.dock_settings[1].spin_box_explode[-1].setSizePolicy(sizePolicy)
                dock.dock_settings[1].scroll_explode_layout.setWidget(self.int,
                                                                      QtWidgets.QFormLayout.FieldRole,
                                                                      dock.dock_settings[1].spin_box_explode[-1])
            except:
                pass

        def buttons_positions(self):
            number = self.data_scroll_layout.rowCount()
            if not dock.dock_data[1].add_data == []:
                if not number == 1:
                    dock.dock_data[1].add_data[-1].second_block_Name_layout.setWidget(5,
                                                                                      QtWidgets.QFormLayout.LabelRole,
                                                                                      dock.dock_data[1].button_Create)

                    dock.dock_data[1].add_data[-1].second_block_Name_layout.setWidget(4,
                                                                                      QtWidgets.QFormLayout.LabelRole,
                                                                                      dock.dock_data[1].button_Add)

                    dock.dock_data[1].add_data[-1].second_block_Name_layout.setWidget(3,
                                                                                      QtWidgets.QFormLayout.LabelRole,
                                                                                      dock.dock_data[1].space)


class SettingsPage1:
    def __init__(self, *args):
        self.page = args[0]
        self.grid_page = args[1]
        self.central_layout = args[2]

    def contain(self):

        self.tab_widget = QtWidgets.QTabWidget(self.page)
        self.tab_widget.setObjectName("tab_widget")
        self.grid_page.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.page_color = QtWidgets.QWidget()
        self.page_color.setObjectName("page_color")
        self.tab_widget.addTab(self.page_color, "Color")

        self.p_color()
        self.p_explode()
        self.p_settings()

    def p_color(self):
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

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.label_color = []
        self.buttons_color = []
        for array_position in range(0, 2):
            self.label_color.append(QtWidgets.QLabel(self.scroll_color_contents))
            self.scroll_color_layout.setWidget(
                                                array_position,
                                                QtWidgets.QFormLayout.LabelRole,
                                                self.label_color[array_position])

            self.buttons_color.append(QtWidgets.QPushButton(self.scroll_color_contents))
            self.buttons_color[array_position].setMinimumSize(QtCore.QSize(35, 20))
            self.buttons_color[array_position].setMaximumSize(QtCore.QSize(35, 20))
            self.scroll_color_layout.setWidget(
                                                array_position,
                                                QtWidgets.QFormLayout.FieldRole,
                                                self.buttons_color[array_position])
            self.buttons_color[array_position].setSizePolicy(sizePolicy)
            sizePolicy.setHeightForWidth(self.buttons_color[array_position].hasHeightForWidth())
            self.buttons_color[array_position].clicked.connect(partial(self.button_color, array_position))


            if array_position == 0:
                self.buttons_color[array_position].setStyleSheet("background-color: rgb(255, 167, 14);")
                self.label_color[array_position].setText(dock.dock_data[1].upper_first_Name_write.text())
                dock.dock_data[1].upper_first_Name_write.textChanged.connect(
                                                                    lambda: self.label_color[0].setText(
                                                                       dock.dock_data[1].upper_first_Name_write.text()))


            else:
                self.buttons_color[array_position].setStyleSheet("background-color: rgb(100, 150, 190);")
                self.label_color[array_position].setText(dock.dock_data[1].add_data[-1].second_block_Name_write.text())
                dock.dock_data[1].add_data[0].second_block_Name_write.textChanged.connect(
                                                        lambda: self.label_color[1].setText(
                                                          dock.dock_data[1].add_data[0].second_block_Name_write.text()))


    def p_explode(self):
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

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.label_explode = []
        self.spin_box_explode = []
        for array_position in range(0, 2):
            self.label_explode.append(QtWidgets.QLabel(self.scroll_explode_contents))
            self.scroll_explode_layout.setWidget(
                                                 array_position,
                                                 QtWidgets.QFormLayout.LabelRole,
                                                 self.label_explode[array_position])

            self.spin_box_explode.append(QtWidgets.QDoubleSpinBox(self.scroll_explode_contents))
            self.spin_box_explode[array_position].setMinimumSize(QtCore.QSize(50, 20))
            self.spin_box_explode[array_position].setMaximumSize(QtCore.QSize(50, 20))
            sizePolicy.setHeightForWidth(self.spin_box_explode[array_position].sizePolicy().hasHeightForWidth())
            self.spin_box_explode[array_position].setSizePolicy(sizePolicy)
            self.scroll_explode_layout.setWidget(
                                                 array_position,
                                                 QtWidgets.QFormLayout.FieldRole,
                                                 self.spin_box_explode[array_position])

            if array_position == 0:
                self.label_explode[array_position].setText(dock.dock_data[1].upper_first_Name_write.text())
                dock.dock_data[1].upper_first_Name_write.textChanged.connect(
                                                                    lambda: self.label_explode[0].setText(
                                                                       dock.dock_data[1].upper_first_Name_write.text()))
            else:
                self.label_explode[array_position].setText(
                                                          dock.dock_data[1].add_data[-1].second_block_Name_write.text())
                dock.dock_data[1].add_data[0].second_block_Name_write.textChanged.connect(
                                                        lambda: self.label_explode[1].setText(
                                                          dock.dock_data[1].add_data[0].second_block_Name_write.text()))

        self.spin_box_explode[0].setValue(1.0)

    def p_settings(self):
        self.page_settings = QtWidgets.QWidget()
        self.tab_widget.addTab(self.page_settings, "Settings")

        self.page_settings_layout = QtWidgets.QHBoxLayout(self.page_settings)

        self.scroll_area_settings = QtWidgets.QScrollArea(self.page_settings)
        self.scroll_area_settings.setWidgetResizable(True)
        self.page_settings_layout.addWidget(self.scroll_area_settings)

        self.scroll_settings_contents = QtWidgets.QWidget()
        self.scroll_settings_contents.setGeometry(QtCore.QRect(0, 0, 94, 450))
        self.scroll_area_settings.setWidget(self.scroll_settings_contents)

        self.scroll_settings_layout = QtWidgets.QFormLayout(self.scroll_settings_contents)

        self.line_edit_title = QtWidgets.QLineEdit(self.scroll_color_contents)
        self.line_edit_title.setMaximumSize(QtCore.QSize(95, 16777215))
        self.line_edit_title.setClearButtonEnabled(True)
        self.line_edit_title.setPlaceholderText('Set title')
        self.scroll_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_edit_title)

        self.check_box1_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
        self.check_box1_settings.setText("Shadow")
        self.scroll_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.check_box1_settings)

        self.check_box2_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
        self.check_box2_settings.setText("Rotate Labels")
        self.scroll_settings_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.check_box2_settings)

        self.check_box3_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
        self.check_box3_settings.setText("Frame")
        self.check_box3_settings.setTristate(True)
        self.scroll_settings_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.check_box3_settings)

        self.check_box4_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
        self.check_box4_settings.setText("Legend")
        self.scroll_settings_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.check_box4_settings)

        self.line_1 = QtWidgets.QFrame(self.scroll_settings_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_1.sizePolicy().hasHeightForWidth())
        self.line_1.setSizePolicy(sizePolicy)
        self.line_1.setMinimumSize(QtCore.QSize(110, 0))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scroll_settings_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.line_1)

        self.label_data_settings = QtWidgets.QLabel(self.scroll_settings_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_settings.sizePolicy().hasHeightForWidth())
        self.label_data_settings.setSizePolicy(sizePolicy)
        self.label_data_settings.setMinimumSize(QtCore.QSize(100, 0))
        self.label_data_settings.setMaximumSize(QtCore.QSize(155, 16777215))
        self.label_data_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_settings.setText("DATA SETTINGS")
        self.scroll_settings_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole,  self.label_data_settings)

        self.Data_settings_layout = QtWidgets.QFormLayout()

        self.check_box5_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
        self.check_box5_settings.setObjectName("check_box1_settings")
        self.check_box5_settings.setText("Show")
        self.Data_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check_box5_settings)
        self.check_box5_settings.setChecked(True)
        self.check_box5_settings.clicked.connect(self.show_data_setting)

        self.button_data_color = QtWidgets.QPushButton(self.scroll_settings_contents)
        self.button_data_color.setMinimumSize(QtCore.QSize(45, 22))
        self.button_data_color.setMaximumSize(QtCore.QSize(47, 22))
        self.button_data_color.setText("Color")
        self.button_data_color.clicked.connect(self.setting_button_color)
        self.button_data_color.setStyleSheet("background-color: #f0f0f0;" "color: rgb(0, 0, 0);")
        self.Data_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button_data_color)

        self.Data_autopct = QtWidgets.QComboBox(self.scroll_settings_contents)
        self.Data_autopct.addItem("100%")
        self.Data_autopct.addItem("100.0%")
        self.Data_autopct.addItem("100.00%")
        self.Data_autopct.addItem("----")
        self.Data_autopct.addItem("1")
        self.Data_autopct.addItem("----")
        self.Data_autopct.addItem("100%  (1)")
        self.Data_autopct.addItem("100.0%  (1)")
        self.Data_autopct.addItem("100.00%  (1)")
        self.Data_autopct.addItem("----")
        self.Data_autopct.addItem("100%     1")
        self.Data_autopct.addItem("100.0%    1")
        self.Data_autopct.addItem("100.00%    1")
        self.Data_autopct.setMinimumSize(QtCore.QSize(0, 23))
        self.Data_settings_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Data_autopct)

        self.scroll_settings_layout.setLayout(7, QtWidgets.QFormLayout.LabelRole, self.Data_settings_layout)
        self.tab_widget.setCurrentIndex(0)

    def setting_button_color(self):
        if self.button_data_color.palette().button().color().name() == '#f0f0f0':
            self.button_data_color.setStyleSheet("background-color: rgb(90, 90, 90);" "color: rgb(255, 255, 255);")
        else:
            self.button_data_color.setStyleSheet("background-color:#f0f0f0;" "color: rgb(0, 0, 0);")

    def show_data_setting(self):
        if self.check_box5_settings.checkState():
            self.button_data_color.setEnabled(True)
            self.Data_autopct.setEnabled(True)
            self.button_data_color.setStyleSheet("background-color: #f0f0f0;" "color: rgb(0, 0, 0);")
        else:
            self.button_data_color.setEnabled(False)
            self.Data_autopct.setEnabled(False)
            self.button_data_color.setStyleSheet("background-color: #f0f0f0;" "color: rgb(160, 160, 160);")

    @staticmethod
    def button_color(number):
        color = QtWidgets.QColorDialog.getColor()
        dock.dock_settings[1].buttons_color[number].setStyleSheet("background-color: %s;" % (str(color.name())))


class SettingsPage2:
    def __init__(self, *args):
        self.page = args[0]
        self.grid_page = args[1]
        self.central_layout = args[2]

    def contain(self):
        self.scroll_area = QtWidgets.QScrollArea(self.page)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())

        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 153, 523))

        self.grid_page.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.scroll_settings_layout = QtWidgets.QFormLayout(self.scroll_area_contents)

        self.line_edit_title = QtWidgets.QLineEdit()
        self.line_edit_title.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_title.setClearButtonEnabled(True)
        self.line_edit_title.setPlaceholderText('Set title')
        self.scroll_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_edit_title)

        self.line_edit_lineY = QtWidgets.QLineEdit()
        self.line_edit_lineY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_lineY.setClearButtonEnabled(True)
        self.line_edit_lineY.setPlaceholderText('Label Y')
        self.scroll_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_edit_lineY)

        self.line_edit_lineX = QtWidgets.QLineEdit()
        self.line_edit_lineX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_lineX.setClearButtonEnabled(True)
        self.line_edit_lineX.setPlaceholderText('Label X')
        self.scroll_settings_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.line_edit_lineX)

        self.line_1 = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_1.sizePolicy().hasHeightForWidth())
        self.line_1.setSizePolicy(sizePolicy)
        self.line_1.setMinimumSize(QtCore.QSize(100, 0))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scroll_settings_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line_1)

        self.check_box_label = QtWidgets.QCheckBox()
        self.check_box_label.setText("Value label ")
        self.scroll_settings_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.check_box_label)

        self.line_2 = QtWidgets.QFrame()
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(100, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scroll_settings_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.line_2)

        self.layout_settings_layout = QtWidgets.QFormLayout()

        self.spin_box_bar_color = QtWidgets.QSpinBox()
        self.spin_box_bar_color.setMinimum(5)
        self.spin_box_bar_color.setMaximum(100)
        self.spin_box_bar_color.setValue(60)
        self.layout_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.spin_box_bar_color)

        self.label_bar_size = QtWidgets.QLabel()
        self.label_bar_size.setText("Bar size")
        self.layout_settings_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_bar_size)

        self.button_bar_color = QtWidgets.QPushButton()
        self.button_bar_color.setMinimumSize(QtCore.QSize(40, 0))
        self.button_bar_color.setStyleSheet("background-color: #1f77b4; width: 0px;")
        self.button_bar_color.clicked.connect(lambda: self.button_color(self.button_bar_color))
        self.layout_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button_bar_color)

        self.label_bar_size = QtWidgets.QLabel()
        self.label_bar_size.setText("Bar color")
        self.layout_settings_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_bar_size)

        self.spin_box_edge_color = QtWidgets.QSpinBox()
        self.spin_box_edge_color.setMinimum(0)
        self.spin_box_edge_color.setMaximum(10)
        self.layout_settings_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.spin_box_edge_color)

        self.label_edge_size = QtWidgets.QLabel()
        self.label_edge_size.setText("Edge size")
        self.layout_settings_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_edge_size)

        self.button_edge_color = QtWidgets.QPushButton()
        self.button_edge_color.setMinimumSize(QtCore.QSize(40, 0))
        self.button_edge_color.setStyleSheet("background-color: #222; width: 0px;")
        self.button_edge_color.clicked.connect(lambda: self.button_color(self.button_edge_color))
        self.layout_settings_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.button_edge_color)

        self.label_edge_color = QtWidgets.QLabel()
        self.label_edge_color.setText("Edge color")
        self.layout_settings_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_edge_color)

        self.scroll_settings_layout.setLayout(6, QtWidgets.QFormLayout.LabelRole, self.layout_settings_layout)

    @staticmethod
    def button_color(number):
        color = QtWidgets.QColorDialog.getColor()
        number.setStyleSheet("background-color: %s;" % (str(color.name())))

class SettingsPage3:
    def __init__(self, *args):
        self.page = args[0]
        self.grid_page = args[1]
        self.central_layout = args[2]

    def contain(self):
        self.scroll_area = QtWidgets.QScrollArea(self.page)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())

        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 153, 523))

        self.grid_page.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.scroll_settings_layout = QtWidgets.QFormLayout(self.scroll_area_contents)

        self.line_edit_title = QtWidgets.QLineEdit()
        self.line_edit_title.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_title.setClearButtonEnabled(True)
        self.line_edit_title.setPlaceholderText('Set title')
        self.scroll_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_edit_title)

        self.line_edit_lineY = QtWidgets.QLineEdit()
        self.line_edit_lineY.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_lineY.setClearButtonEnabled(True)
        self.line_edit_lineY.setPlaceholderText('Label Y')
        self.scroll_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_edit_lineY)

        self.line_edit_lineX = QtWidgets.QLineEdit()
        self.line_edit_lineX.setMaximumSize(QtCore.QSize(100, 16777215))
        self.line_edit_lineX.setClearButtonEnabled(True)
        self.line_edit_lineX.setPlaceholderText('Label X')
        self.scroll_settings_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.line_edit_lineX)

        self.line_1 = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_1.sizePolicy().hasHeightForWidth())
        self.line_1.setSizePolicy(sizePolicy)
        self.line_1.setMinimumSize(QtCore.QSize(100, 0))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scroll_settings_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.line_1)

        self.line_edit_legend = QtWidgets.QLineEdit()
        self.line_edit_legend.setPlaceholderText("Legend ")
        self.line_edit_legend.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scroll_settings_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.line_edit_legend)

        self.line_2 = QtWidgets.QFrame()
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(100, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scroll_settings_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.line_2)

        self.layout_settings_layout = QtWidgets.QFormLayout()

        self.spin_box_line_size = QtWidgets.QSpinBox()
        self.spin_box_line_size.setMinimum(1)
        self.spin_box_line_size.setMaximum(15)
        self.spin_box_line_size.setValue(3)
        self.layout_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.spin_box_line_size)

        self.label_line_size = QtWidgets.QLabel()
        self.label_line_size.setText("Line size")
        self.layout_settings_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_line_size)

        self.button_line_color = QtWidgets.QPushButton()
        self.button_line_color.setMinimumSize(QtCore.QSize(40, 0))
        self.button_line_color.setStyleSheet("background-color: #1f77b4; width: 0px;")
        self.button_line_color.clicked.connect(lambda: self.button_color(self.button_line_color))
        self.layout_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button_line_color)

        self.label_line_size = QtWidgets.QLabel()
        self.label_line_size.setText("Line color")
        self.layout_settings_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_line_size)

        self.scroll_settings_layout.setLayout(6, QtWidgets.QFormLayout.LabelRole, self.layout_settings_layout)

    @staticmethod
    def button_color(number):
        color = QtWidgets.QColorDialog.getColor()
        number.setStyleSheet("background-color: %s;" % (str(color.name())))
