from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class Data():
    def __init__(self, *args):
        self.form_layout = args[0]
        self.scroll_area_widget_contents = args[1]
        self.central_layout = args[3]

        self.write_data()
    def write_data(self):
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.label_def = []
        self.line_edit = []
        self.array_position = int()
        self.horizontal_position_widgets = int()
        for self.horizontal_position_widgets in range(0, 4, 2):
            for self.array_position in range(0, 2):
                self.label_def.append(QtWidgets.QLabel(self.scroll_area_widget_contents))
                self.line_edit.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))

                if self.array_position == 0:
                    if (self.horizontal_position_widgets+1) < 2:
                        self.form_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.LabelRole,
                                                   self.label_def[self.horizontal_position_widgets + self.array_position])
                        self.label_def[self.horizontal_position_widgets+self.array_position].setText("NAME")

                    self.form_layout.setWidget(self.horizontal_position_widgets + 1, QtWidgets.QFormLayout.LabelRole,
                                               self.line_edit[self.horizontal_position_widgets + self.array_position])

                if self.array_position == 1:
                    if (self.horizontal_position_widgets + 1) < 2:
                        self.form_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.FieldRole,
                                                   self.label_def[self.horizontal_position_widgets + self.array_position])
                        self.label_def[self.horizontal_position_widgets+self.array_position].setText("VALUE")

                    self.form_layout.setWidget(self.horizontal_position_widgets + 1, QtWidgets.QFormLayout.FieldRole,
                                               self.line_edit[self.horizontal_position_widgets + self.array_position])
                    self.sizePolicy.setHeightForWidth(self.line_edit[
                                                          self.horizontal_position_widgets + self.array_position
                                                      ].sizePolicy().hasHeightForWidth())
                    self.line_edit[self.horizontal_position_widgets+self.array_position].setSizePolicy(self.sizePolicy)

        self.button_add = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_add.setSizePolicy(self.sizePolicy)
        self.button_add.setObjectName("pushButton")
        self.form_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.button_add)
        self.button_add.clicked.connect(self.add_data)
        self.button_add.setText("ADD DATA")

        self.space = QtWidgets.QFrame(self.scroll_area_widget_contents)
        self.form_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.space)

        self.button_create = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_create.setObjectName("button_create")
        self.form_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.button_create)
        self.button_create.setText("CREATE")
        self.button_create.clicked.connect(lambda: self.pie_default())


    def add_data(self):
        self.horizontal_position_widgets += 2
        print("123: " + str(self.horizontal_position_widgets))
        self.form_layout.setWidget(self.horizontal_position_widgets + 4, QtWidgets.QFormLayout.LabelRole,
                                   self.button_create)
        self.form_layout.setWidget(self.horizontal_position_widgets + 3, QtWidgets.QFormLayout.LabelRole,
                                   self.button_add)
        self.form_layout.setWidget(self.horizontal_position_widgets + 2, QtWidgets.QFormLayout.LabelRole,
                                   self.space)

        self.line_edit.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))
        self.form_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.LabelRole,
                                   self.line_edit[self.array_position + 3])
        self.line_edit.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))
        self.form_layout.setWidget(self.horizontal_position_widgets, QtWidgets.QFormLayout.FieldRole,
                                   self.line_edit[self.array_position + 4])

        self.sizePolicy.setHeightForWidth(self.line_edit[self.array_position + 4]
                                          .sizePolicy().hasHeightForWidth())
        self.line_edit[self.array_position + 4].setSizePolicy(self.sizePolicy)

        self.array_position += 2


    def pie_default(self):
        sizes = [15, 30]
        labels = 'Frogs', 'Hogs'
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        static_canvas = FigureCanvas(Figure())

        self.central_layout.addWidget(static_canvas)

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)


