# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT, FigureCanvas
from matplotlib.figure import Figure

import dock


def tool_bar():
        static_canvas = FigureCanvas(Figure())

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
        toolbar = NavigationToolbar2QT(static_canvas, static_canvas)

        return static_canvas, toolbar


class PieChart:
    def __init__(self, chart_type):
        self.contain()

        if chart_type == 'Basic_pie':
            self.basic()
        if chart_type == 'Donut_pie':
            self.donut()

    def contain(self):
        for i in reversed(range(dock.dock_data[1].central_layout.count())):
            dock.dock_data[1].central_layout.itemAt(i).widget().deleteLater()

        self.all = 0
        self.outer_sizes = []
        try:
            for x in range(0, len(dock.dock_data[1].line_edit_data), 2):
                self.outer_sizes.append(dock.dock_data[1].line_edit_data[x + 1].text())
                self.all += float(dock.dock_data[1].line_edit_data[x + 1].text())
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
        for x in range(0, len(dock.dock_data[1].line_edit_data), 2):
            self.outer_labels.append(str(dock.dock_data[1].line_edit_data[x].text()))

        self.outer_colors = []
        for x in range(0, len(dock.dock_settings[1].buttons_color)):
            self.outer_colors.append(dock.dock_settings[1].buttons_color[x].palette().button().color().name())

        self.outer_explode = []
        for x in range(0, len(dock.dock_settings[1].spin_box_explode)):
            self.outer_explode.append(float(dock.dock_settings[1].spin_box_explode[x].value() / 10))

        self.outer_shadow = 0
        if dock.dock_settings[1].check_box1_settings.checkState():
            self.outer_shadow = dock.dock_settings[1].check_box1_settings.checkState()

        self.outer_rotatelabels = 0
        if dock.dock_settings[1].check_box2_settings.checkState():
            self.outer_rotatelabels = dock.dock_settings[1].check_box2_settings.checkState()

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
        self.outer_autopct = data_autopct_list[dock.dock_settings[1].Data_autopct.currentText()]
        if not dock.dock_settings[1].check_box5_settings.checkState():
            self.outer_autopct = ''

        self.outer_wedgeprops = {'edgecolor': 'white'}
        if dock.dock_settings[1].check_box3_settings.checkState() == 1:
            self.outer_wedgeprops = {'edgecolor': 'black', 'linewidth': 1}
        elif dock.dock_settings[1].check_box3_settings.checkState() == 2:
            self.outer_wedgeprops = {'edgecolor': 'black', 'linewidth': 2}

        self.outer_textprops = {'color': "black"}
        if not dock.dock_settings[1].button_data_color.palette().button().color().name() == '#f0f0f0':
            self.outer_textprops = {'color': "white"}

    def basic(self):
        try:
            if self.outer_sizes[-1] == '0':
                raise ValueError("VALUE = 0")

            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            static_chart.pie(
                                self.outer_sizes,
                                labels=self.outer_labels,
                                wedgeprops=self.outer_wedgeprops,
                                colors=self.outer_colors,
                                explode=self.outer_explode,
                                autopct=self.outer_autopct,
                                shadow=self.outer_shadow,
                                startangle=90,
                                rotatelabels=self.outer_rotatelabels,
                                textprops=self.outer_textprops)

            if dock.dock_settings[1].check_box4_settings.checkState():
                static_chart.legend(
                                       self.outer_labels,
                                       loc='upper right',
                                       bbox_to_anchor=(1.1, 1.120))
            else:
                static_chart.legend().remove()

            static_chart.set_title(dock.dock_settings[1].line_edit_title.text())

            dock.dock_data[1].central_layout.addWidget( static_canvas)
            dock.dock_data[1].central_layout.addWidget(toolbar)

        except ValueError:
            pass

    def donut(self):
        self.outer_wedgeprops.update({'width': 0.5})

        try:
            if self.outer_sizes[-1] == '0':
                raise ValueError("VALUE = 0")

            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            static_chart.pie(
                                self.outer_sizes,
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

            if dock.dock_settings[1].check_box4_settings.checkState():
                static_chart.legend(
                                       self.outer_labels,
                                       loc='upper right',
                                       bbox_to_anchor=(1.1, 1.120),
                                       )
            else:
                static_chart.legend().remove()

            static_chart.set_title(dock.dock_settings[1].line_edit_title.text())

            dock.dock_data[1].central_layout.addWidget(static_canvas)
            dock.dock_data[1].central_layout.addWidget(toolbar)

        except ValueError:
            pass


class BarChart:
    def __init__(self, chart_type):
        self.contain()

        if chart_type == 'Basic_bar':
            self.basic()

    def contain(self):
        for i in reversed(range(dock.dock_data[1].central_layout.count())):
            dock.dock_data[1].central_layout.itemAt(i).widget().deleteLater()

        self.static_canvas = FigureCanvas(Figure())

        self.outer_labels = []
        for x in range(0, len(dock.dock_data[1].line_edit_data), 2):
            self.outer_labels.append(str(dock.dock_data[1].line_edit_data[x].text()))

        self.all = 0
        self.outer_height = []
        try:
            for x in range(0, len(dock.dock_data[1].line_edit_data), 2):
                self.outer_height.append(dock.dock_data[1].line_edit_data[x + 1].text())
                self.all += float(dock.dock_data[1].line_edit_data[x + 1].text())

        except ValueError:
            self.outer_height2 = 0
            for x in str(self.outer_height[-1]):
                if x == ',':
                    self.outer_height2 = self.outer_height[-1].replace(',', '.')

            if self.outer_height2 == 0:
                self.outer_height2 = 1

            value_error = QtWidgets.QMessageBox()
            value_error.setWindowTitle("VALUE")
            value_error.setText("Value entry error                       ")
            value_error.setInformativeText(
                "Your value: %s \nCorrect: %s " % (str(self.outer_height[-1]), self.outer_height2))
            value_error.setIcon(QtWidgets.QMessageBox.Critical)
            value_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            value_error.exec_()

        self.outer_width = float(dock.dock_settings[2].spin_box_bar_color.value() / 100)

        self.outer_color = dock.dock_settings[2].button_bar_color.palette().button().color().name()

        self.outer_linewidth = dock.dock_settings[2].spin_box_edge_color.value()

        self.outer_edgecolor = dock.dock_settings[2].button_edge_color.palette().button().color().name()

    def basic(self):
        try:
            self.outer_height = [int(x) for x in self.outer_height]

            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            static_chart.bar(
                                self.outer_labels,
                                height=self.outer_height,
                                width=self.outer_width,
                                color=self.outer_color,
                                linewidth=self.outer_linewidth,
                                edgecolor=self.outer_edgecolor)

            if dock.dock_settings[2].check_box_label.isChecked():
                for x, y in enumerate(self.outer_height):
                    static_chart.annotate(
                                             y,
                                             xy=(x, y+(self.outer_linewidth / 100 / 2)),
                                             ha='center',
                                             va='bottom')

            static_chart.set_title(dock.dock_settings[2].title_edit_title.text())
            static_chart.set_xlabel(dock.dock_settings[2].lineX_edit_title.text())
            static_chart.set_ylabel(dock.dock_settings[2].lineY_edit_title.text())

            dock.dock_data[1].central_layout.addWidget(static_canvas)
            dock.dock_data[1].central_layout.addWidget(toolbar)

        except ValueError:
            pass

class LineChart:
    def __init__(self, chart_type):
        self.contain()

        if chart_type == 'Basic_bar':
            self.basic()