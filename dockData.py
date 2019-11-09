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

        self.label_value = QtWidgets.QLabel(self.scroll_area_widget_contents)
        self.label_value.setObjectName("label")
        self.label_value.setText("VALUE")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_value)

        self.label_name = QtWidgets.QLabel(self.scroll_area_widget_contents)
        self.label_name.setObjectName("label_name")
        self.label_name.setText("NAME")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)


        self.line_edit_value = QtWidgets.QLineEdit(self.scroll_area_widget_contents)
        self.line_edit_value.setObjectName("line_edit_value")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.line_edit_value)



        self.line_edit_name = QtWidgets.QLineEdit(self.scroll_area_widget_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_name.sizePolicy().hasHeightForWidth())
        self.line_edit_name.setSizePolicy(sizePolicy)
        self.line_edit_name.setObjectName("line_edit_name")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_edit_name)

        self.pushButton = QtWidgets.QPushButton(self.scroll_area_widget_contents)
        self.pushButton.setObjectName("pushButton")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton.setText("ADD")
        self.pushButton.clicked.connect(lambda: self.pie_default())

    def pie_default(self):
        sizes = [15, 30]
        labels = 'Frogs', 'Hogs'
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        static_canvas = FigureCanvas(Figure())

        self.central_layout.addWidget(static_canvas)

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)





