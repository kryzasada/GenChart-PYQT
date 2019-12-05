from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class Data():
    def __init__(self, *args):
        self.page_2 = args[0]
        self.grid_page_2 = args[1]
        self.central_layout = args[2]

    def write_data(self):
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
        self.line_edit = []
        self.array_position = int()
        self.horizontal_position_widgets = int()
        for self.horizontal_position_widgets in range(0, 4, 2):
            for self.array_position in range(0, 2):
                self.label_data.append(QtWidgets.QLabel(self.scroll_area_contents))
                self.line_edit.append(QtWidgets.QLineEdit(self.scroll_area_contents))

                if self.array_position == 0:
                    if (self.horizontal_position_widgets+1) < 2:
                        self.data_scroll_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.LabelRole,
                                                   self.label_data[self.horizontal_position_widgets + self.array_position])
                        self.label_data[self.horizontal_position_widgets+self.array_position].setText("NAME")

                    self.data_scroll_layout.setWidget(self.horizontal_position_widgets + 1, QtWidgets.QFormLayout.LabelRole,
                                               self.line_edit[self.horizontal_position_widgets + self.array_position])

                if self.array_position == 1:
                    if (self.horizontal_position_widgets + 1) < 2:
                        self.data_scroll_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.FieldRole,
                                                   self.label_data[self.horizontal_position_widgets + self.array_position])
                        self.label_data[self.horizontal_position_widgets+self.array_position].setText("VALUE")

                    self.data_scroll_layout.setWidget(self.horizontal_position_widgets + 1, QtWidgets.QFormLayout.FieldRole,
                                               self.line_edit[self.horizontal_position_widgets + self.array_position])
                    self.sizePolicy.setHeightForWidth(self.line_edit[
                                                          self.horizontal_position_widgets + self.array_position
                                                      ].sizePolicy().hasHeightForWidth())
                    self.line_edit[self.horizontal_position_widgets+self.array_position].setSizePolicy(self.sizePolicy)

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
        self.line_edit[0].setText("default_1")
        self.line_edit[2].setText("default_2")

        self.line_edit[1].setText("1")
        self.line_edit[3].setText("1")

    def add_data(self):
        self.horizontal_position_widgets += 2
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets + 4, QtWidgets.QFormLayout.LabelRole,
                                   self.button_Create)
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets + 3, QtWidgets.QFormLayout.LabelRole,
                                   self.button_Add)
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets + 2, QtWidgets.QFormLayout.LabelRole,
                                   self.space)

        self.line_edit.append(QtWidgets.QLineEdit(self.scroll_area_contents))
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.LabelRole,
                                   self.line_edit[self.array_position + 3])
        self.line_edit.append(QtWidgets.QLineEdit(self.scroll_area_contents))
        self.data_scroll_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.FieldRole,
                                   self.line_edit[self.array_position + 4])

        self.line_edit[self.array_position + 3].setText("default_" + str(int(self.horizontal_position_widgets/2 + 1)))
        self.line_edit[self.array_position + 4].setText("1")

        self.sizePolicy.setHeightForWidth(self.line_edit[self.array_position + 4]
                                          .sizePolicy().hasHeightForWidth())
        self.line_edit[self.array_position + 4].setSizePolicy(self.sizePolicy)

        self.array_position += 2

    def settings_chart(self):

        self.label1_col = QtWidgets.QLabel(self.scroll_contents_color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1_col.sizePolicy().hasHeightForWidth())
        self.label1_col.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1_col)
        self.label1_col.setText("TextLabel")

        self.label2_col = QtWidgets.QLabel(self.scroll_contents_color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label2_col.sizePolicy().hasHeightForWidth())
        self.label2_col.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2_col)
        self.label2_col.setText("TextLabel")

        self.color_button1 = QtWidgets.QPushButton(self.scroll_contents_color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_button1.sizePolicy().hasHeightForWidth())
        self.color_button1.setSizePolicy(sizePolicy)
        self.color_button1.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.color_button1.setText("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.color_button1)

        self.color_button2 = QtWidgets.QPushButton(self.scroll_contents_color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_button2.sizePolicy().hasHeightForWidth())
        self.color_button2.setSizePolicy(sizePolicy)
        self.color_button2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.color_button2.setText("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.color_button2)

    def pie_default(self):

        for i in reversed(range(self.central_layout.count())):
            self.central_layout.itemAt(i).widget().deleteLater()

        static_canvas = FigureCanvas(Figure())
        self.central_layout.addWidget(static_canvas)

        sizes = []
        for x in range(0, len(self.line_edit), 2):
            sizes.append(self.line_edit[x+1].text())

        labels = []
        for x in range(0, len(self.line_edit), 2):
            labels.append(str(self.line_edit[x].text()))


        # explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        self._static_ax = static_canvas.figure.subplots()
        '''explode=explode,'''
        self._static_ax.pie(sizes,labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)





