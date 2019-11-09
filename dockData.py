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

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        label_def = []
        line_edit = []
        for x in range(0, 4, 2):
            for i in range(0, 2):
                label_def.append(QtWidgets.QLabel(self.scroll_area_widget_contents))
                line_edit.append(QtWidgets.QLineEdit(self.scroll_area_widget_contents))

                if i == 0:
                    if (x+1) < 2:
                        self.form_layout.setWidget(x, QtWidgets.QFormLayout.LabelRole, label_def[x+i])
                        label_def[x+i].setText("NAME")

                    self.form_layout.setWidget(x+1, QtWidgets.QFormLayout.LabelRole, line_edit[x+i])

                if i == 1:
                    if (x + 1) < 2:
                        self.form_layout.setWidget(x, QtWidgets.QFormLayout.FieldRole, label_def[x+i])
                        label_def[x+i].setText("VALUE")

                    self.form_layout.setWidget(x+1, QtWidgets.QFormLayout.FieldRole, line_edit[x+i])
                    sizePolicy.setHeightForWidth(line_edit[x+i].sizePolicy().hasHeightForWidth())
                    line_edit[x+i].setSizePolicy(sizePolicy)




        self.button_add = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setObjectName("pushButton")
        self.form_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.button_add)
        self.button_add.setText("ADD DATA")

        self.line = QtWidgets.QFrame(self.scroll_area_widget_contents)
        self.form_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.line)

        self.button_create = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.button_create.setObjectName("button_create")
        self.form_layout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.button_create)
        self.button_create.setText("CREATE")
        self.button_create.clicked.connect(lambda: self.pie_default())

    def pie_default(self):
        sizes = [15, 30]
        labels = 'Frogs', 'Hogs'
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        static_canvas = FigureCanvas(Figure())

        self.central_layout.addWidget(static_canvas)

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)





