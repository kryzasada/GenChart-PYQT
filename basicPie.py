from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

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

        self.default_data()

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


    def default_data(self):

        self.line_edit_data[0].setText("default_1")
        self.line_edit_data[2].setText("default_2")

        self.line_edit_data[1].setText("1")
        self.line_edit_data[3].setText("1")

    def add_data(self):
        self.horizontal_position_widgets_data += 2
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 4, QtWidgets.QFormLayout.LabelRole,
                                   self.button_Create)
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 3, QtWidgets.QFormLayout.LabelRole,
                                   self.button_Add)
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data + 2, QtWidgets.QFormLayout.LabelRole,
                                   self.space)

        self.line_edit_data.append(QtWidgets.QLineEdit(self.scroll_area_contents))
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data, QtWidgets.QFormLayout.LabelRole,
                                   self.line_edit_data[self.array_position_data + 3])
        self.line_edit_data.append(QtWidgets.QLineEdit(self.scroll_area_contents))
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets_data, QtWidgets.QFormLayout.FieldRole,
                                   self.line_edit_data[self.array_position_data + 4])

        self.line_edit_data[self.array_position_data + 3].setText("default_" + str(int(self.horizontal_position_widgets_data/2 + 1)))
        self.line_edit_data[self.array_position_data + 4].setText("1")

        self.sizePolicy.setHeightForWidth(self.line_edit_data[self.array_position_data + 4]
                                          .sizePolicy().hasHeightForWidth())
        self.line_edit_data[self.array_position_data + 4].setSizePolicy(self.sizePolicy)

        self.array_position_data += 2

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

        #print (str(dock.Dock.right_up(self).dock_data.data.line_edit_data[0].text()))
        self.buttons_color = []
        self.array_position_color= int()

        label_settings = []

        for self.array_position_color in range(0, 2):
            print(self.array_position_color)
            label_settings.append(QtWidgets.QLabel(self.scroll_color_contents))
            label_settings[self.array_position_color].setText(self.dock_data.line_edit_data[self.array_position_color*2].text())
            self.scroll_color_layout.setWidget(self.array_position_color, QtWidgets.QFormLayout.LabelRole, label_settings[self.array_position_color])

            self.buttons_color.append(QtWidgets.QPushButton(self.scroll_color_contents))
            self.scroll_color_layout.setWidget(self.array_position_color, QtWidgets.QFormLayout.FieldRole, self.buttons_color[self.array_position_color])
            self.buttons_color[self.array_position_color].setSizePolicy(sizePolicy)
            sizePolicy.setHeightForWidth(self.buttons_color[self.array_position_color].hasHeightForWidth())
            self.buttons_color[self.array_position_color].setStyleSheet("background-color: rgb(170, 0, 0);")




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

        self.tab_widget.setCurrentIndex(0)

    def pie_default(self):

        for i in reversed(range(self.central_layout.count())):
            self.central_layout.itemAt(i).widget().deleteLater()

        static_canvas = FigureCanvas(Figure())
        self.central_layout.addWidget(static_canvas)

        sizes = []
        for x in range(0, len(self.line_edit_data), 2):
            sizes.append(self.line_edit_data[x+1].text())


        labels = []
        for x in range(0, len(self.line_edit_data), 2):
            labels.append(str(self.line_edit_data[x].text()))


        # explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        self._static_ax = static_canvas.figure.subplots()
        '''explode=explode,'''
        self._static_ax.pie(sizes,labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)




