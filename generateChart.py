# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT, FigureCanvas
from matplotlib.figure import Figure
import linecache
import math

import dock


def tool_bar():
        static_canvas = FigureCanvas(Figure())

        NavigationToolbar2QT.toolitems = (('Home', 'Reset original view', 'home', 'home'),
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
        if chart_type == 'Percent_pie':
            self.percent()

    def contain(self):
        for i in reversed(range(dock.dock_data[1].central_layout.count())):
            dock.dock_data[1].central_layout.itemAt(i).widget().deleteLater()

        self.all = 0
        self.all += dock.dock_data[1].upper_first_value_spinBox.value()
        self.outer_sizes = []
        try:
            self.outer_sizes.append(dock.dock_data[1].upper_first_value_spinBox.value())
            if self.outer_sizes[-1] <= 0.0:
                raise ValueError("VALUE = 0")

            for x in range(0, len(dock.dock_data[1].add_data)):
                self.outer_sizes.append(dock.dock_data[1].add_data[x].second_block_value_spinBox.value())
                self.all += float(dock.dock_data[1].add_data[x].second_block_value_spinBox.value())
                if self.outer_sizes[-1] <= 0.0:
                    raise ValueError("VALUE = 0")

        except ValueError:
            value_error = QtWidgets.QMessageBox()
            value_error.setWindowTitle(linecache.getline("Language/Language.txt", 402)[:-1])
            value_error.setText(linecache.getline("Language/Language.txt", 403)[:-1])
            value_error.setInformativeText(linecache.getline("Language/Language.txt", 404)[:-1])
            value_error.setIcon(QtWidgets.QMessageBox.Critical)
            value_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            value_error.exec_()

        self.outer_labels = []
        self.legend_labels = []
        if dock.dock_settings[1].check_box4_settings.checkState() == 2:
            self.legend_labels.append(dock.dock_data[1].upper_first_Name_write.text())
        else:
            self.legend_labels.append(" ")
        if dock.dock_data[1].upper_first_Name_check.checkState():
            self.outer_labels.append(dock.dock_data[1].upper_first_Name_write.text())
        else:
            self.outer_labels.append("")

        for x in range(0, len(dock.dock_data[1].add_data)):
            if dock.dock_settings[1].check_box4_settings.checkState() == 2:
                self.legend_labels.append(str(dock.dock_data[1].add_data[x].second_block_Name_write.text()))
            else:
                self.legend_labels.append("")
            if dock.dock_data[1].add_data[x].second_block_Name_check.checkState():
                self.outer_labels.append(str(dock.dock_data[1].add_data[x].second_block_Name_write.text()))
            else:
                self.outer_labels.append("")

        self.outer_colors1 = []
        for x in range(0, len(dock.dock_settings[1].buttons_color)):
            self.outer_colors1.append(dock.dock_settings[1].buttons_color[x].palette().button().color().name())

        self.outer_colors2 = []
        self.outer_colors2.append(dock.dock_settings[4].button_color3.palette().button().color().name())
        self.outer_colors2.append(dock.dock_settings[4].button_color2.palette().button().color().name())

        self.outer_explode = []
        for x in range(0, len(dock.dock_settings[1].spin_box_explode)):
            self.outer_explode.append(float(dock.dock_settings[1].spin_box_explode[x].value() / 10))

        self.outer_radius = dock.dock_settings[4].spin_box_size.value() / -10

        self.outer_shadow1 = 0
        if dock.dock_settings[1].check_box1_settings.checkState():
            self.outer_shadow1 = dock.dock_settings[1].check_box1_settings.checkState()

        self.outer_shadow2 = 0
        if dock.dock_settings[4].check_box1.checkState():
            self.outer_shadow2 = dock.dock_settings[4].check_box1.checkState()

        self.outer_rotatelabels = 0
        if dock.dock_settings[1].check_box2_settings.checkState():
            self.outer_rotatelabels = dock.dock_settings[1].check_box2_settings.checkState()

        data_autopct_list = {'100%': '%1.0f%%',
                             '100.0%': '%1.1f%%',
                             '100.00%': '%1.2f%%',
                             '----': '',
                             '1': (lambda p: '{:,.1f}'.format(p * self.all / 100)),
                             '100%  (1)': (lambda p: '{:1.0f}%({:,.0f})'.format(p, p * self.all / 100)),
                             '100.0%  (1)': (lambda p: '{:1.1f}%({:,.0f})'.format(p, p * self.all / 100)),
                             '100.00%  (1)': (lambda p: '{:1.2f}%({:,.0f})'.format(p, p * self.all / 100)),
                             '100%     1': (lambda p: '{:1.0f}%\n{:,.0f}'.format(p, p * self.all / 100)),
                             '100.0%    1': (lambda p: '{:1.1f}%\n{:,.0f}'.format(p, p * self.all / 100)),
                             '100.00%    1': (lambda p: '{:1.2f}%\n{:,.0f}'.format(p, p * self.all / 100))}

        self.outer_autopct = data_autopct_list[dock.dock_settings[1].Data_autopct.currentText()]
        if not dock.dock_settings[1].check_box5_settings.checkState():
            self.outer_autopct = ''

        self.outer_wedgeprops1 = {'edgecolor': 'white'}
        if dock.dock_settings[1].check_box3_settings.checkState() == 1:
            self.outer_wedgeprops1 = {'edgecolor': 'black', 'linewidth': 1}
        elif dock.dock_settings[1].check_box3_settings.checkState() == 2:
            self.outer_wedgeprops1 = {'edgecolor': 'black', 'linewidth': 2}

        self.outer_wedgeprops2 = {'edgecolor': 'white'}
        if dock.dock_settings[4].check_box2.checkState() == 1:
            self.outer_wedgeprops2 = {'edgecolor':
                                          dock.dock_settings[4].button_color1.palette().button().color().name(),
                                      'linewidth': 1}
        elif dock.dock_settings[4].check_box2.checkState() == 2:
            self.outer_wedgeprops2 = {'edgecolor':
                                          dock.dock_settings[4].button_color1.palette().button().color().name(),
                                      'linewidth': 2}

        self.outer_textprops = {'color': "black"}
        if not dock.dock_settings[1].button_data_color.palette().button().color().name() == '#f0f0f0':
            self.outer_textprops = {'color': "white"}

    def basic(self):
        try:
            if self.outer_sizes[-1] <= 0.0:
                raise ValueError("VALUE = 0")

            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            static_chart.pie(
                             self.outer_sizes,
                             labels=self.outer_labels,
                             wedgeprops=self.outer_wedgeprops1,
                             colors=self.outer_colors1,
                             explode=self.outer_explode,
                             autopct=self.outer_autopct,
                             shadow=self.outer_shadow1,
                             startangle=90,
                             rotatelabels=self.outer_rotatelabels,
                             textprops=self.outer_textprops)

            if dock.dock_settings[1].check_box4_settings.checkState():
                static_chart.legend(
                                    self.legend_labels,
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
        self.outer_wedgeprops1.update({'width': 0.5})

        try:
            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            static_chart.pie(
                             self.outer_sizes,
                             labels=self.outer_labels,
                             wedgeprops=self.outer_wedgeprops1,
                             colors=self.outer_colors1,
                             explode=self.outer_explode,
                             autopct=self.outer_autopct,
                             shadow=self.outer_shadow1,
                             startangle=90,
                             rotatelabels=self.outer_rotatelabels,
                             textprops=self.outer_textprops,
                             pctdistance=0.75)

            if dock.dock_settings[1].check_box4_settings.checkState():
                static_chart.legend(
                                    self.legend_labels,
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

    def percent(self):

        sort = sorted(self.outer_sizes)
        resize = str(math.floor(sort[-1]))
        resize += '.'
        outer_sizes2 = []
        for x in range(len(self.outer_sizes)):
            val = round(10 ** resize[::1].find('.') - self.outer_sizes[x], 2)
            outer_sizes2.append([val, self.outer_sizes[x]])

        self.outer_radius2 = self.outer_radius * -1

        self.outer_wedgeprops2['width'] = self.outer_radius2

        try:
            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            for x in range(len(self.outer_sizes)):
                static_chart.pie(outer_sizes2[x],
                                 radius=1+self.outer_radius,
                                 colors=self.outer_colors2,
                                 startangle=90,
                                 shadow=self.outer_shadow2,
                                 wedgeprops=self.outer_wedgeprops2)

                static_chart.text(0.01,
                                  1.07 + self.outer_radius,
                                  self.outer_labels[x],
                                  horizontalalignment='center',
                                  verticalalignment='center')

                self.outer_radius += self.outer_radius2

            static_chart.set_title(dock.dock_settings[4].line_edit_title.text())
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

        self.outer_labels = []
        self.outer_labels.append(dock.dock_data[1].upper_first_Name_write.text())
        for x in range(0, len(dock.dock_data[1].add_data)):
            self.outer_labels.append(str(dock.dock_data[1].add_data[x].second_block_Name_write.text()))

        self.all = 0
        self.all += dock.dock_data[1].upper_first_value_spinBox.value()
        self.outer_height = []
        try:
            self.outer_height.append(dock.dock_data[1].upper_first_value_spinBox.value())

            for x in range(0, len(dock.dock_data[1].add_data)):
                self.outer_height.append(dock.dock_data[1].add_data[x].second_block_value_spinBox.value())
                self.all += float(dock.dock_data[1].add_data[x].second_block_value_spinBox.value())

        except ValueError:
            value_error = QtWidgets.QMessageBox()
            value_error.setWindowTitle(linecache.getline("Language/Language.txt", 402)[:-1])
            value_error.setText(linecache.getline("Language/Language.txt", 403)[:-1])
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

            if dock.dock_data[1].upper_TextValue_check.isChecked():
                if dock.dock_data[1].upper_first_value_check.checkState():
                    static_chart.annotate(self.outer_height[0],
                                          xy=(0, self.outer_height[0]+(self.outer_linewidth / 100 / 2)),
                                          ha='center',
                                          va='bottom')

                for x, y in enumerate(self.outer_height[1:]):
                    if dock.dock_data[1].add_data[x].second_block_value_check.checkState():
                        static_chart.annotate(y,
                                              xy=(x+1, y+(self.outer_linewidth / 100 / 2)),
                                              ha='center',
                                              va='bottom')

            static_chart.set_title(dock.dock_settings[2].line_edit_title.text())
            static_chart.set_xlabel(dock.dock_settings[2].line_edit_lineX.text())
            static_chart.set_ylabel(dock.dock_settings[2].line_edit_lineY.text())

            dock.dock_data[1].central_layout.addWidget(static_canvas)
            dock.dock_data[1].central_layout.addWidget(toolbar)

        except ValueError:
            pass


class LineChart:
    def __init__(self, chart_type):
        self.contain()
        if chart_type == 'Basic_line':
            self.basic()

    def contain(self):
        for i in reversed(range(dock.dock_data[1].central_layout.count())):
            dock.dock_data[1].central_layout.itemAt(i).widget().deleteLater()

        self.outer_labels = []
        self.outer_labels.append(dock.dock_data[1].upper_first_Name_write.text())
        for x in range(0, len(dock.dock_data[1].add_data)):
            self.outer_labels.append(str(dock.dock_data[1].add_data[x].second_block_Name_write.text()))

        self.all = 0
        self.all += dock.dock_data[1].upper_first_value_spinBox.value()
        self.outer_height = []
        try:
            self.outer_height.append(dock.dock_data[1].upper_first_value_spinBox.value())

            for x in range(0, len(dock.dock_data[1].add_data)):
                self.outer_height.append(dock.dock_data[1].add_data[x].second_block_value_spinBox.value())
                self.all += float(dock.dock_data[1].add_data[x].second_block_value_spinBox.value())

        except ValueError:
            value_error = QtWidgets.QMessageBox()
            value_error.setWindowTitle(linecache.getline("Language/Language.txt", 402)[:-1])
            value_error.setText(linecache.getline("Language/Language.txt", 404)[:-1])
            value_error.setIcon(QtWidgets.QMessageBox.Critical)
            value_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
            value_error.exec_()

        self.outer_color = dock.dock_settings[3].button_line_color.palette().button().color().name()

        self.outer_linewidth = dock.dock_settings[3].spin_box_line_size.value()

        self.outer_label = dock.dock_settings[3].line_edit_legend.text()

    def basic(self):
        try:
            self.outer_height = [int(x) for x in self.outer_height]

            static_canvas, toolbar = tool_bar()
            static_chart = static_canvas.figure.subplots()
            static_chart.plot(self.outer_labels,
                              self.outer_height,
                              color=self.outer_color,
                              linewidth=self.outer_linewidth,
                              label=self.outer_label)

            static_chart.set_title(dock.dock_settings[3].line_edit_title.text())
            static_chart.set_xlabel(dock.dock_settings[3].line_edit_lineX.text())
            static_chart.set_ylabel(dock.dock_settings[3].line_edit_lineY.text())

            if self.outer_label:
                static_chart.legend()

            dock.dock_data[1].central_layout.addWidget(static_canvas)
            dock.dock_data[1].central_layout.addWidget(toolbar)

        except ValueError:
            pass