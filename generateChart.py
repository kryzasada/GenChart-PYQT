# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT, FigureCanvas
from matplotlib.figure import Figure

import dock


class PieChart:
    def __init__(self, chart_type):
        self.contain()

        if chart_type == 'Basic':
            self.basic()
        if chart_type == 'Donut':
            self.donut()

    def contain(self):

        for i in reversed(range(dock.dock_data.central_layout.count())):
            dock.dock_data.central_layout.itemAt(i).widget().deleteLater()

        self.static_canvas = FigureCanvas(Figure())

        NavigationToolbar2QT.toolitems = (
            ('Home', 'Reset original view', 'home', 'home'),
            ('Back', 'Back to previous view', 'back', 'back'),
            ('Forward', 'Forward to next view', 'forward', 'forward'),
            (None, None, None, None),
            ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
            ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
            ('', 'Configure subplots', 'subplots', 'configure_subplots'),
            (None, None, None, None),
            (None, None, None, None),
            ('Save', 'Save the figure', 'filesave', 'save_figure'),
        )
        dock.dock_data.toolbar2 = NavigationToolbar2QT(self.static_canvas, self.static_canvas)

        self.all = 0
        self.outer_sizes = []
        try:
            for x in range(0, len(dock.dock_data.line_edit_data), 2):
                self.outer_sizes.append(dock.dock_data.line_edit_data[x + 1].text())
                self.all += float(dock.dock_data.line_edit_data[x + 1].text())
                if self.outer_sizes[-1] == '0':
                    raise ValueError("VALUE = 0")

        except ValueError:
            self.outer_sizes2 = 0
            for x in str(self.outer_sizes[-1]):
                if x == ',':
                    self.outer_sizes2 = self.outer_sizes[-1].replace(',', '.')

            if self.outer_sizes2 == 0:
                self.outer_sizes2 = 1

            value_error = QtWidgets.QMessageBox()
            value_error.setWindowTitle("VALUE")
            value_error.setText("Value entry error                       ")
            value_error.setInformativeText(
                "Your value: %s \nCorrect: %s " % (str(self.outer_sizes[-1]), self.outer_sizes2))
            value_error.setIcon(QtWidgets.QMessageBox.Critical)
            value_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            value_error.exec_()

        self.outer_labels = []
        for x in range(0, len(dock.dock_data.line_edit_data), 2):
            self.outer_labels.append(str(dock.dock_data.line_edit_data[x].text()))

        self.outer_colors = []
        for x in range(0, len(dock.dock_settings.buttons_color)):
            self.outer_colors.append(dock.dock_settings.buttons_color[x].palette().button().color().name())

        self.outer_explode = []
        for x in range(0, len(dock.dock_settings.spin_box_explode)):
            self.outer_explode.append(float(dock.dock_settings.spin_box_explode[x].value() / 10))

        self.outer_shadow = 0
        if dock.dock_settings.check_box1_settings.checkState():
            self.outer_shadow = dock.dock_settings.check_box1_settings.checkState()

        self.outer_rotatelabels = 0
        if dock.dock_settings.check_box2_settings.checkState():
            self.outer_rotatelabels = dock.dock_settings.check_box2_settings.checkState()

        data_autopct_list = {
            '100%': '%1.0f%%',
            '100.0%': '%1.1f%%',
            '100.00%': '%1.2f%%',
            '----': '',
            '1': (lambda p: '{:,.1f}'.format(p * self.all / 100)),
            '100%  (1)': (lambda p: '{:1.0f}%({:,.0f})'.format(p, p * self.all / 100)),
            '100.0%  (1)': (lambda p: '{:1.1f}%({:,.0f})'.format(p, p * self.all / 100)),
            '100.00%  (1)': (lambda p: '{:1.2f}%({:,.0f})'.format(p, p * self.all / 100)),
            '100%     1': (lambda p: '{:1.0f}%\n{:,.0f}'.format(p, p * self.all / 100)),
            '100.0%    1': (lambda p: '{:1.1f}%\n{:,.0f}'.format(p, p * self.all / 100)),
            '100.00%    1': (lambda p: '{:1.2f}%\n{:,.0f}'.format(p, p * self.all / 100)),
        }
        self.outer_autopct = data_autopct_list[dock.dock_settings.Data_autopct.currentText()]
        if not dock.dock_settings.check_box5_settings.checkState():
            self.outer_autopct = ''

        self.outer_wedgeprops = {'edgecolor': 'white'}
        if dock.dock_settings.check_box3_settings.checkState() == 1:
            self.outer_wedgeprops = {'edgecolor': 'black', 'linewidth': 1}
        elif dock.dock_settings.check_box3_settings.checkState() == 2:
            self.outer_wedgeprops = {'edgecolor': 'black', 'linewidth': 2}

        self.outer_textprops = {'color': "black"}
        if not dock.dock_settings.button_data_color.palette().button().color().name() == '#f0f0f0':
            self.outer_textprops = {'color': "white"}

    def basic(self):
        try:
            if self.outer_sizes[-1] == '0':
                raise ValueError("VALUE = 0")

            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.pie(self.outer_sizes,
                                labels=self.outer_labels,
                                wedgeprops=self.outer_wedgeprops,
                                colors=self.outer_colors,
                                explode=self.outer_explode,
                                autopct=self.outer_autopct,
                                shadow=self.outer_shadow,
                                startangle=90,
                                rotatelabels=self.outer_rotatelabels,
                                textprops=self.outer_textprops,
                                )

            if dock.dock_settings.check_box4_settings.checkState():
                self._static_ax.legend(self.outer_labels,
                                       loc='upper right',
                                       bbox_to_anchor=(1.1, 1.120),
                                       )
            else:
                self._static_ax.legend().remove()

            self._static_ax.set_title(dock.dock_settings.line_edit_title.text())

            dock.dock_data.central_layout.addWidget(self.static_canvas)
            dock.dock_data.central_layout.addWidget(dock.dock_data.toolbar2)



        except ValueError:
            pass

    def donut(self):
        self.outer_wedgeprops.update({'width': 0.5})

        try:
            if self.outer_sizes[-1] == '0':
                raise ValueError("VALUE = 0")

            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.pie(self.outer_sizes,
                                labels=self.outer_labels,
                                wedgeprops=self.outer_wedgeprops,
                                colors=self.outer_colors,
                                explode=self.outer_explode,
                                autopct=self.outer_autopct,
                                shadow=self.outer_shadow,
                                startangle=90,
                                rotatelabels=self.outer_rotatelabels,
                                textprops=self.outer_textprops,
                                pctdistance=0.75
                                )

            if dock.dock_settings.check_box4_settings.checkState():
                self._static_ax.legend(self.outer_labels,
                                       loc='upper right',
                                       bbox_to_anchor=(1.1, 1.120),
                                       )
            else:
                self._static_ax.legend().remove()

            self._static_ax.set_title(dock.dock_settings.line_edit_title.text())

            dock.dock_data.central_layout.addWidget(self.static_canvas)
            dock.dock_data.central_layout.addWidget(dock.dock_data.toolbar2)



        except ValueError:
            pass