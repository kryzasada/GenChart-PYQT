from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from functools import partial
import random
import time

import dock

class Data():
    def __init__(self, *args):
        self.page_2 = args[0]
        self.grid_page_2 = args[1]
        self.central_layout = args[2]


    def write_data(self, dock_data):
        self.dock_data = dock_data
        self.scroll_area = QtWidgets.QScrollArea(self.page_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())

        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 153, 523))
        self.scroll_area_contents.setObjectName("scroll_area_contents")

        self.grid_page_2.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.data_scroll_layout = QtWidgets.QFormLayout(self.scroll_area_contents)
        self.data_scroll_layout.setObjectName("data_scroll_layout")

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.label_data = []
        self.line_edit_data = []
        self.array_position_data = int()
        self.horizontal_position_widgets_data = int()
        for self.horizontal_position_widgets_data in range(0, 4, 2):
            for self.array_position_data in range(0, 2):
                self.label_data.append(QtWidgets.QLabel(self.scroll_area_contents))
                self.line_edit_data.append(QtWidgets.QLineEdit(self.scroll_area_contents))

                if self.array_position_data == 0:
                    if (self.horizontal_position_widgets_data+1) < 2:
                        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data, QtWidgets.QFormLayout.LabelRole,
                                                   self.label_data[self.horizontal_position_widgets_data + self.array_position_data])
                        self.label_data[self.horizontal_position_widgets_data+self.array_position_data].setText("NAME")

                    self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 1, QtWidgets.QFormLayout.LabelRole,
                                               self.line_edit_data[self.horizontal_position_widgets_data + self.array_position_data])

                    self.line_edit_data[self.horizontal_position_widgets_data].setText(
                        "default_" + str(int(self.horizontal_position_widgets_data/2+1)))

                if self.array_position_data == 1:
                    if (self.horizontal_position_widgets_data + 1) < 2:
                        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data, QtWidgets.QFormLayout.FieldRole,
                                                   self.label_data[self.horizontal_position_widgets_data + self.array_position_data])
                        self.label_data[self.horizontal_position_widgets_data+self.array_position_data].setText("VALUE")

                    self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 1, QtWidgets.QFormLayout.FieldRole,
                                               self.line_edit_data[self.horizontal_position_widgets_data + self.array_position_data])
                    self.sizePolicy.setHeightForWidth(self.line_edit_data[
                                                          self.horizontal_position_widgets_data + self.array_position_data
                                                      ].sizePolicy().hasHeightForWidth())
                    self.line_edit_data[self.horizontal_position_widgets_data+self.array_position_data].setSizePolicy(self.sizePolicy)

                    self.line_edit_data[self.horizontal_position_widgets_data+self.array_position_data].setText("1")

        self.line_edit_data[0].textChanged.connect(lambda: dock.dock_data2.label_color[0].setText(
                self.line_edit_data[0].text()))

        self.line_edit_data[2].textChanged.connect(lambda: dock.dock_data2.label_color[1].setText(
            self.line_edit_data[2].text()))

        self.line_edit_data[0].textChanged.connect(lambda: dock.dock_data2.label_explode[0].setText(
                self.line_edit_data[0].text()))

        self.line_edit_data[2].textChanged.connect(lambda: dock.dock_data2.label_explode[1].setText(
            self.line_edit_data[2].text()))

        self.button_Add = QtWidgets.QPushButton(self.scroll_area_contents)
        self.button_Add.setSizePolicy(self.sizePolicy)
        self.button_Add.setObjectName("pushButton")
        self.data_scroll_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.button_Add)
        self.button_Add.clicked.connect(self.add_data)
        self.button_Add.setText("ADD DATA")

        self.space = QtWidgets.QFrame(self.scroll_area_contents)
        self.data_scroll_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.space)

        self.button_Create = QtWidgets.QPushButton(self.scroll_area_contents)
        self.button_Create.setObjectName("button_Create")
        self.data_scroll_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.button_Create)
        self.button_Create.setText("CREATE")
        self.button_Create.clicked.connect(lambda: self.pie_default())


    def add_data(self):

        self.horizontal_position_widgets_data += 2
        self.array_position_data += 2
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 4, QtWidgets.QFormLayout.LabelRole,
                                   self.button_Create)
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 3, QtWidgets.QFormLayout.LabelRole,
                                   self.button_Add)
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 2, QtWidgets.QFormLayout.LabelRole,
                                   self.space)

        self.line_edit_data.append(QtWidgets.QLineEdit(self.scroll_area_contents))
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data, QtWidgets.QFormLayout.LabelRole,
                                   self.line_edit_data[self.array_position_data + 1])
        self.line_edit_data.append(QtWidgets.QLineEdit(self.scroll_area_contents))
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data, QtWidgets.QFormLayout.FieldRole,
                                   self.line_edit_data[self.array_position_data + 2])

        self.line_edit_data[self.array_position_data + 1].setText("default_" + str(int(self.horizontal_position_widgets_data/2 + 1)))
        self.line_edit_data[self.array_position_data + 2].setText("1")

        self.sizePolicy.setHeightForWidth(self.line_edit_data[self.array_position_data + 2]
                                          .sizePolicy().hasHeightForWidth())
        self.line_edit_data[self.array_position_data + 2].setSizePolicy(self.sizePolicy)


        dock.dock_data2.label_color.append(QtWidgets.QLabel(dock.dock_data2.scroll_color_contents))
        dock.dock_data2.label_color[int(self.horizontal_position_widgets_data / 2)].setText(dock.dock_data.line_edit_data[self.horizontal_position_widgets_data].text())
        dock.dock_data2.scroll_color_layout.setWidget(int(self.horizontal_position_widgets_data/2), QtWidgets.QFormLayout.LabelRole,
                                           dock.dock_data2.label_color[int(self.horizontal_position_widgets_data/2)])

        self.line_edit_data[self.horizontal_position_widgets_data].textChanged.connect(
            lambda: dock.dock_data2.label_color[int(self.horizontal_position_widgets_data / 2)].setText(
                self.line_edit_data[self.horizontal_position_widgets_data].text()))

        time.sleep(0.1)
        self.line_edit_data[self.horizontal_position_widgets_data].textChanged.connect(partial(self.label_name, self.horizontal_position_widgets_data))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        dock.dock_data2.buttons_color.append(QtWidgets.QPushButton(dock.dock_data2.scroll_color_contents))
        dock.dock_data2.scroll_color_layout.setWidget(int(self.horizontal_position_widgets_data/2),
                    QtWidgets.QFormLayout.FieldRole,dock.dock_data2.buttons_color[
                     int(self.horizontal_position_widgets_data/2)])
        dock.dock_data2.buttons_color[int(self.horizontal_position_widgets_data/2)].setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(dock.dock_data2.buttons_color[int(
                    self.horizontal_position_widgets_data/2)].hasHeightForWidth())
        dock.dock_data2.buttons_color[int(self.horizontal_position_widgets_data/2)].clicked.connect(partial(
                    self.button_color, int(self.horizontal_position_widgets_data/2)))

        if self.horizontal_position_widgets_data/2 == 2.0:
            dock.dock_data2.buttons_color[2].setStyleSheet("background-color: rgb(44, 180, 44);")

        elif self.horizontal_position_widgets_data/2 == 3.0:
            dock.dock_data2.buttons_color[3].setStyleSheet("background-color: rgb(164, 70, 74);")

        else:
            dock.dock_data2.buttons_color[int(self.horizontal_position_widgets_data/2)].setStyleSheet(
                    "background-color: rgb(%s, %s, %s);" % (random.randint(0, 250), random.randint(0, 250),
                                                            random.randint(0, 250)))

        dock.dock_data2.label_explode.append(QtWidgets.QLabel(dock.dock_data2.scroll_explode_contents))
        dock.dock_data2.label_explode[int(self.horizontal_position_widgets_data/2)].setText(
                                            dock.dock_data.line_edit_data[self.horizontal_position_widgets_data].text())
        dock.dock_data2.scroll_explode_layout.setWidget(int(self.horizontal_position_widgets_data/2),
                                                        QtWidgets.QFormLayout.LabelRole,dock.dock_data2.label_explode[
                                                        int(self.horizontal_position_widgets_data/2)])

        self.line_edit_data[self.horizontal_position_widgets_data].textChanged.connect(
            lambda: dock.dock_data2.label_explode[int(self.horizontal_position_widgets_data / 2)].setText(
                self.line_edit_data[self.horizontal_position_widgets_data].text()))

        dock.dock_data2.spin_box_explode.append(QtWidgets.QDoubleSpinBox(dock.dock_data2.scroll_explode_contents))
        sizePolicy.setHeightForWidth(dock.dock_data2.spin_box_explode[int(self.horizontal_position_widgets_data/2)].sizePolicy().hasHeightForWidth())
        dock.dock_data2.spin_box_explode[int(self.horizontal_position_widgets_data/2)].setSizePolicy(sizePolicy)
        dock.dock_data2.scroll_explode_layout.setWidget(int(self.horizontal_position_widgets_data/2),
                                                        QtWidgets.QFormLayout.FieldRole,
                                                        dock.dock_data2.spin_box_explode[int(
                                                            self.horizontal_position_widgets_data/2)])

        dock.dock_data2.scroll_color_contents.update()

    def label_name(self, position):
        dock.dock_data2.label_color[int(position / 2)].setText(
                self.line_edit_data[position].text())

    def settings_chart(self, dock_data):

        self.dock_data=dock_data

        self.tab_widget = QtWidgets.QTabWidget(self.page_2)
        self.tab_widget.setObjectName("tab_widget")
        self.grid_page_2.addWidget(self.tab_widget, 0, 0, 1, 1)

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

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.label_color = []
        self.buttons_color = []
        for array_position in range(0, 2):
            self.label_color.append(QtWidgets.QLabel(self.scroll_color_contents))
            self.label_color[array_position].setText(dock.dock_data.line_edit_data[array_position*2].text())
            self.scroll_color_layout.setWidget(array_position, QtWidgets.QFormLayout.LabelRole, self.label_color[array_position])

            self.buttons_color.append(QtWidgets.QPushButton(self.scroll_color_contents))
            self.scroll_color_layout.setWidget(array_position, QtWidgets.QFormLayout.FieldRole, self.buttons_color[array_position])
            self.buttons_color[array_position].setSizePolicy(sizePolicy)
            sizePolicy.setHeightForWidth(self.buttons_color[array_position].hasHeightForWidth())
            self.buttons_color[array_position].clicked.connect(partial(self.button_color, array_position))

            if array_position == 0:
                self.buttons_color[array_position].setStyleSheet("background-color: rgb(255, 167, 14);")
            else:
                self.buttons_color[array_position].setStyleSheet("background-color: rgb(100, 150, 190);")


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
            self.label_explode[array_position].setText(dock.dock_data.line_edit_data[array_position*2].text())
            self.scroll_explode_layout.setWidget(array_position, QtWidgets.QFormLayout.LabelRole, self.label_explode[array_position])

            self.spin_box_explode.append(QtWidgets.QDoubleSpinBox(self.scroll_explode_contents))
            sizePolicy.setHeightForWidth(self.spin_box_explode[array_position].sizePolicy().hasHeightForWidth())
            self.spin_box_explode[array_position].setSizePolicy(sizePolicy)
            self.scroll_explode_layout.setWidget(array_position, QtWidgets.QFormLayout.FieldRole, self.spin_box_explode[array_position])

        self.spin_box_explode[0].setValue(1.0)

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
        self.check_box1_settings.setText("Shadow")
        self.scroll_settings_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.check_box1_settings)

        self.check_box2_settings = QtWidgets.QCheckBox(self.scroll_settings_contents)
        self.check_box2_settings.setObjectName("check_box2_settings")
        self.check_box2_settings.setText("Rotate Labels")
        self.scroll_settings_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.check_box2_settings)

        self.tab_widget.setCurrentIndex(0)

    def button_color(self, number):
        color = QtWidgets.QColorDialog.getColor()
        dock.dock_data2.buttons_color[number].setStyleSheet("background-color: %s;" % (str(color.name())))

    def pie_default(self):

        static_canvas = FigureCanvas(Figure())
        self.central_layout.addWidget(static_canvas)

        for i in reversed(range(self.central_layout.count())):
            self.central_layout.itemAt(i).widget().deleteLater()

        outer_sizes = []
        for x in range(0, len(self.line_edit_data), 2):
            outer_sizes.append(self.line_edit_data[x+1].text())

        outer_labels = []
        for x in range(0, len(self.line_edit_data), 2):
            outer_labels.append(str(self.line_edit_data[x].text()))

        outer_colors = []
        for x in range(0, len(dock.dock_data2.buttons_color)):
           outer_colors.append(dock.dock_data2.buttons_color[x].palette().button().color().name())

        outer_explode = []
        for x in range(0, len(dock.dock_data2.spin_box_explode)):
            outer_explode.append(float(dock.dock_data2.spin_box_explode[x].value()/10))

        outer_shadow = 0
        if dock.dock_data2.check_box1_settings.checkState():
            outer_shadow = dock.dock_data2.check_box1_settings.checkState()

        outer_rotatelabels = 0
        if dock.dock_data2.check_box2_settings.checkState():
            outer_rotatelabels = dock.dock_data2.check_box2_settings.checkState()

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.pie(outer_sizes,labels=outer_labels, colors=outer_colors, explode=outer_explode,
                            autopct='%1.1f%%', shadow=outer_shadow, startangle=90, rotatelabels=outer_rotatelabels)





