# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.0
#

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
import dock, menuStatusBar
import linecache
import time


class firstConfiguration:
    def contain(self, main_window):
        self.main_window = main_window
        self.main_window.resize(568, 265)
        self.main_window.setWindowIcon(QtGui.QIcon("Image/Icons/blank-logo.ico"))
        self.main_window.setWindowTitle("GenChart - First Time Configuration")

        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.main_window.setCentralWidget(self.central_widget)

        self.title_label = QtWidgets.QLabel(self.central_widget)
        self.title_label.setGeometry(QtCore.QRect(20, 0, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.title_label.setFont(font)
        self.title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setText("GemChart configuration:")

        self.line1_horizontal = QtWidgets.QFrame(self.central_widget)
        self.line1_horizontal.setGeometry(QtCore.QRect(20, 40, 531, 16))
        self.line1_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.language_label = QtWidgets.QLabel(self.central_widget)
        self.language_label.setGeometry(QtCore.QRect(40, 60, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.language_label.setFont(font)
        self.language_label.setText("Language:")

        self.language_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.language_combo_box.setGeometry(QtCore.QRect(130, 60, 141, 22))
        self.language_combo_box.addItem("English")
        self.language_combo_box.addItem("Polski")
        self.language_combo_box.currentIndexChanged.connect(lambda: self.change_language())

        self.font_label = QtWidgets.QLabel(self.central_widget)
        self.font_label.setGeometry(QtCore.QRect(40, 90, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_label.setFont(font)
        self.font_label.setText("Font:")

        self.font_combo_box = QtWidgets.QFontComboBox(self.central_widget)
        self.font_combo_box.setGeometry(QtCore.QRect(130, 90, 141, 22))
        self.font_combo_box.setCurrentFont(QtGui.QFont("Arial"))
        self.font_combo_box.currentFontChanged.connect(lambda: self.change_font())

        self.line1_vertical = QtWidgets.QFrame(self.central_widget)
        self.line1_vertical.setGeometry(QtCore.QRect(280, 47, 3, 80))
        self.line1_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.resolution_label = QtWidgets.QLabel(self.central_widget)
        self.resolution_label.setGeometry(QtCore.QRect(300, 60, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resolution_label.setFont(font)
        self.resolution_label.setText("Resolution:")

        self.resolution_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.resolution_combo_box.setGeometry(QtCore.QRect(390, 60, 141, 22))
        self.resolution_combo_box.addItem("800 x 600")

        self.line2_horizontal = QtWidgets.QFrame(self.central_widget)
        self.line2_horizontal.setGeometry(QtCore.QRect(20, 120, 531, 16))
        self.line2_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.theme_label = QtWidgets.QLabel(self.central_widget)
        self.theme_label.setGeometry(QtCore.QRect(40, 140, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.theme_label.setFont(font)
        self.theme_label.setText("Theme: ")

        self.theme_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.theme_combo_box.setGeometry(QtCore.QRect(130, 140, 141, 22))
        self.theme_combo_box.addItem("Default")
        self.theme_combo_box.addItem("Integrid")
        self.theme_combo_box.addItem("Ubuntu")
        self.theme_combo_box.addItem("Eclippy")
        self.theme_combo_box.addItem("Combinear")
        self.theme_combo_box.currentIndexChanged.connect(lambda: self.change_theme())

        self.theme_stacked = QtWidgets.QStackedWidget(self.central_widget)
        self.theme_stacked.setGeometry(QtCore.QRect(154, 170, 320, 200))
        self.theme_stacked.setStyleSheet("border: 0.5px solid black")
        self.theme_stacked.hide()

        self.theme_page1 = QtWidgets.QWidget()
        self.theme_page1.setStyleSheet("border-image: url(Image/Theme/Default.png) 0 0 0 0 stretch stretch;")

        self.theme_page2 = QtWidgets.QWidget()
        self.theme_page2.setStyleSheet("border-image: url(Image/Theme/Integrid.png) 0 0 0 0 stretch stretch;")

        self.theme_page3 = QtWidgets.QWidget()
        self.theme_page3.setObjectName("page_2")
        self.theme_page3.setStyleSheet("border-image: url(Image/Theme/Ubuntu.png) 0 0 0 0 stretch stretch;")

        self.theme_page4 = QtWidgets.QWidget()
        self.theme_page4.setObjectName("page_2")
        self.theme_page4.setStyleSheet("border-image: url(Image/Theme/Eclippy.png) 0 0 0 0 stretch stretch;")

        self.theme_page5 = QtWidgets.QWidget()
        self.theme_page5.setObjectName("page_2")
        self.theme_page5.setStyleSheet("border-image: url(Image/Theme/Combinear.png) 0 0 0 0 stretch stretch;")

        self.theme_stacked.addWidget(self.theme_page1)
        self.theme_stacked.addWidget(self.theme_page2)
        self.theme_stacked.addWidget(self.theme_page3)
        self.theme_stacked.addWidget(self.theme_page4)
        self.theme_stacked.addWidget(self.theme_page5)

        self.transparent_label = QtWidgets.QLabel(self.central_widget)
        self.transparent_label.setStyleSheet("background-color: #F0F0F0")

        self.preview_theme_label = QtWidgets.QLabel(self.central_widget)
        self.preview_theme_label.setGeometry(QtCore.QRect(40, 165, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.preview_theme_label.setFont(font)
        self.preview_theme_label.setText("Preview: ")

        self.preview_theme_checkBox = QtWidgets.QCheckBox(self.central_widget)
        self.preview_theme_checkBox.setGeometry(QtCore.QRect(130, 165, 81, 22))
        self.preview_theme_checkBox.stateChanged.connect(lambda: self.show_preview())

        self.line2_vertical = QtWidgets.QFrame(self.central_widget)
        self.line2_vertical.setGeometry(QtCore.QRect(280, 127, 3, 87))
        self.line2_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line3_horizontal = QtWidgets.QFrame(self.central_widget)
        self.line3_horizontal.setGeometry(QtCore.QRect(20, 206, 531, 16))
        self.line3_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.start_button = QtWidgets.QPushButton(self.central_widget)
        self.start_button.setGeometry(QtCore.QRect(460, 226, 75, 23))
        self.start_button.setText("START")
        self.start_button.clicked.connect(lambda: self.save_settings())

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def change_language(self):
        if self.language_combo_box.currentText() == "Polski":
            self.main_window.setWindowTitle("GenChart - Pierwsza konfiguracja")
            self.title_label.setText("Konfigurator GemChart:")
            self.language_label.setText("Język:")
            self.font_label.setText("Font:")
            self.resolution_label.setText("Rozdzielczość:")
            self.theme_label.setText("Motyw: ")
            self.preview_theme_label.setText("Podgląd: ")
            self.start_button.setText("START")

        elif self.language_combo_box.currentText() == "English":
            self.main_window.setWindowTitle("GenChart - First Time Configuration")
            self.title_label.setText("GemChart configuration:")
            self.language_label.setText("Language:")
            self.font_label.setText("Font:")
            self.resolution_label.setText("Resolution:")
            self.theme_label.setText("Theme: ")
            self.preview_theme_label.setText("Preview: ")

    def change_font(self):
        self.title_label.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 11))
        self.language_label.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.font_label.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.resolution_label.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.theme_label.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.preview_theme_label.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.start_button.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))

        self.language_combo_box.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.resolution_combo_box.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))
        self.theme_combo_box.setFont(QtGui.QFont(self.font_combo_box.currentFont().family(), 10))

    def change_theme(self):
        x = self.theme_combo_box.currentText()
        if x == "Default":
            self.theme_stacked.setCurrentIndex(0)
        elif x == "Integrid":
            self.theme_stacked.setCurrentIndex(1)
        elif x == "Ubuntu":
            self.theme_stacked.setCurrentIndex(2)
        elif x == "Eclippy":
            self.theme_stacked.setCurrentIndex(3)
        elif x == "Combinear":
            self.theme_stacked.setCurrentIndex(4)

    def show_preview(self):
        if self.preview_theme_checkBox.checkState():
            self.line2_vertical.hide()
            self.theme_stacked.show()

            self.window_animation = QtCore.QPropertyAnimation(self.main_window, b"size")
            self.window_animation.setDuration(800)
            self.window_animation.setStartValue(QtCore.QSize(568, 265))
            self.window_animation.setEndValue(QtCore.QSize(568, 431))
            self.window_animation.start()

            self.button_animation = QtCore.QPropertyAnimation(self.start_button, b"geometry")
            self.button_animation.setDuration(800)
            self.button_animation.setStartValue(QtCore.QRect(460, 226, 75, 23))
            self.button_animation.setEndValue(QtCore.QRect(460, 390, 75, 23))
            self.button_animation.start()

            self.label_animation = QtCore.QPropertyAnimation(self.transparent_label, b"geometry")
            self.label_animation.setDuration(800)
            self.label_animation.setStartValue(QtCore.QRect(154, 210, 320, 60))
            self.label_animation.setEndValue(QtCore.QRect(154, 376, 320, 60))
            self.label_animation.start()

            self.line_animation = QtCore.QPropertyAnimation(self.line3_horizontal, b"geometry")
            self.line_animation.setDuration(800)
            self.line_animation.setStartValue(QtCore.QRect(20, 206, 531, 16))
            self.line_animation.setEndValue(QtCore.QRect(20, 370, 531, 16))
            self.line_animation.start()

        else:
            self.window_animation = QtCore.QPropertyAnimation(self.main_window, b"size")
            self.window_animation.setDuration(800)
            self.window_animation.setStartValue(QtCore.QSize(568, 431))
            self.window_animation.setEndValue(QtCore.QSize(568, 265))
            self.window_animation.start()

            self.button_animation = QtCore.QPropertyAnimation(self.start_button, b"geometry")
            self.button_animation.setDuration(800)
            self.button_animation.setStartValue(QtCore.QRect(460, 390, 75, 23))
            self.button_animation.setEndValue(QtCore.QRect(460, 226, 75, 23))
            self.button_animation.start()

            self.label_animation = QtCore.QPropertyAnimation(self.transparent_label, b"geometry")
            self.label_animation.setDuration(800)
            self.label_animation.setStartValue(QtCore.QRect(154, 376, 320, 60))
            self.label_animation.setEndValue(QtCore.QRect(154, 210, 320, 60))
            self.label_animation.start()
            self.label_animation.finished.connect(lambda: self.theme_stacked.hide())

            self.line_animation = QtCore.QPropertyAnimation(self.line3_horizontal, b"geometry")
            self.line_animation.setDuration(800)
            self.line_animation.setStartValue(QtCore.QRect(20, 370, 531, 16))
            self.line_animation.setEndValue(QtCore.QRect(20, 206, 531, 16))
            self.line_animation.start()
            self.line_animation.finished.connect(lambda: self.line2_vertical.show())

    def save_settings(self):
        old_file = open("settings.txt").read()
        old_file = old_file.replace(linecache.getline("settings.txt", 4),
                                    ("Language = %s\n" % self.language_combo_box.currentText()))
        old_file = old_file.replace(linecache.getline("settings.txt", 7),
                                    ("Font = %s\n" % self.font_combo_box.currentFont().family()))

        if self.resolution_combo_box.currentText() == "800 x 600":
            old_file = old_file.replace(linecache.getline("settings.txt", 5), ("Resolution1 = %s\n" % "800"))
            old_file = old_file.replace(linecache.getline("settings.txt", 6), ("Resolution2 = %s\n" % "600"))

        old_file = old_file.replace(linecache.getline("settings.txt", 8),
                                    ("Theme= %s\n" % self.theme_combo_box.currentText()))

        new_file = open("settings.txt", 'w')
        new_file.write(old_file)
        new_file.close()

class main:
    def contain(self, main_window):
            main_window.resize(800, 600)
            main_window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
            main_window.setTabShape(QtWidgets.QTabWidget.Triangular)
            main_window.setWindowIcon(QtGui.QIcon("Image/Icons/blank-logo.ico"))
            main_window.setWindowTitle("GenChart")

            self.centralwidget = QtWidgets.QWidget(main_window)
            self.centralwidget.setObjectName("centralwidget")
            main_window.setCentralWidget(self.centralwidget)

            self.central_layout = QtWidgets.QVBoxLayout(self.centralwidget)

            showDock = dock.Dock(main_window, self.central_layout)
            showDock.right_up()
            showDock.right_down()
            showDock.left_chart()

            self.menu_bar = menuStatusBar.MenuBar(main_window, showDock)
            status_bar = menuStatusBar.StatusBar(main_window)

            QtCore.QMetaObject.connectSlotsByName(main_window)


class UserSetting(QtWidgets.QWidget):
    def contain(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(551, 321)
        main_window.setWindowTitle(linecache.getline("Language/Language.txt", 502)[:-1])

        self.treeWidget = QtWidgets.QTreeWidget(main_window)
        self.treeWidget.setHeaderLabel("GenChart")
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 151, 261))
        self.treeWidget.currentItemChanged.connect(self.treeWidget_clicked)

        item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget,
                                           [linecache.getline("Language/Language.txt", 504)[:-1]],
                                           type=1)
        item_1_1 = QtWidgets.QTreeWidgetItem(item_1,
                                             [linecache.getline("Language/Language.txt", 506)[:-1]],
                                             type=11)
        item_1_2 = QtWidgets.QTreeWidgetItem(item_1,
                                             [linecache.getline("Language/Language.txt", 511)[:-1]],
                                             type=12)
        item_1_2_1 = QtWidgets.QTreeWidgetItem(item_1_2,
                                               [linecache.getline("Language/Language.txt", 513)[:-1]],
                                               type=121)
        item_1_2_2 = QtWidgets.QTreeWidgetItem(item_1_2,
                                               [linecache.getline("Language/Language.txt", 515)[:-1]],
                                               type=122)
        item_1_2_3 = QtWidgets.QTreeWidgetItem(item_1_2,
                                               [linecache.getline("Language/Language.txt", 517)[:-1]],
                                               type=123)
        item_2 = QtWidgets.QTreeWidgetItem(self.treeWidget,
                                           [linecache.getline("Language/Language.txt", 522)[:-1]],
                                           type=2)
        item_2_1 = QtWidgets.QTreeWidgetItem(item_2,
                                             [linecache.getline("Language/Language.txt", 524)[:-1]],
                                             type=21)

        self.treeWidget.expandItem(item_1)
        self.treeWidget.expandItem(item_1_2)
        self.treeWidget.expandItem(item_2)

        self.title_label = QtWidgets.QLabel(main_window)
        self.title_label.setGeometry(QtCore.QRect(180, 10, 351, 21))
        self.title_label.setStyleSheet("background-color: rgb(212, 212, 212); color: black;")
        self.title_label.setText(" ")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        self.main_stackedWidget = QtWidgets.QStackedWidget(main_window)
        self.main_stackedWidget.setGeometry(QtCore.QRect(180, 40, 351, 161))
        # self.main_stackedWidget.setStyleSheet("border: 1px solid #bbbbbb;")

        """ Stacked widget page 0 """
        self.page_0 = QtWidgets.QWidget()
        self.main_stackedWidget.addWidget(self.page_0)

        self.label_p0 = QtWidgets.QLabel(self.page_0)
        self.label_p0.setGeometry(QtCore.QRect(80, 50, 47, 13))
        self.label_p0.setText("")

        """ Stacked widget page 1 """
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1-user_interface")
        self.main_stackedWidget.addWidget(self.page_1)

        self.label_language_p1 = QtWidgets.QLabel(self.page_1)
        self.label_language_p1.setGeometry(QtCore.QRect(20, 10, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_language_p1.setFont(font)
        self.label_language_p1.setText(linecache.getline("Language/Language.txt", 532)[:-1])

        self.comboBox_language_p1 = QtWidgets.QComboBox(self.page_1)
        self.comboBox_language_p1.setGeometry(QtCore.QRect(120, 10, 141, 22))
        self.comboBox_language_p1.setObjectName("combo_box_language")
        self.comboBox_language_p1.addItem("English")
        self.comboBox_language_p1.addItem("Polski")
        self.comboBox_language_p1.currentTextChanged.connect(lambda: self.button_save.setEnabled(True))

        self.label_font_p1 = QtWidgets.QLabel(self.page_1)
        self.label_font_p1.setGeometry(QtCore.QRect(20, 40, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_font_p1.setFont(font)
        self.label_font_p1.setText(linecache.getline("Language/Language.txt", 533)[:-1])

        self.comboBox_font_p1 = QtWidgets.QFontComboBox(self.page_1)
        self.comboBox_font_p1.setGeometry(QtCore.QRect(120, 40, 141, 22))
        self.comboBox_font_p1.currentFontChanged.connect(lambda: self.button_save.setEnabled(True))

        self.label_resolution_p1 = QtWidgets.QLabel(self.page_1)
        self.label_resolution_p1.setGeometry(QtCore.QRect(20, 70, 100, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_resolution_p1.setFont(font)
        self.label_resolution_p1.setText(linecache.getline("Language/Language.txt", 534)[:-1])

        self.comboBox_resolution_p1 = QtWidgets.QComboBox(self.page_1)
        self.comboBox_resolution_p1.setGeometry(QtCore.QRect(120, 70, 141, 22))
        self.comboBox_resolution_p1.addItem("800 x 600")
        self.comboBox_resolution_p1.currentTextChanged.connect(lambda: self.button_save.setEnabled(True))

        self.label_theme_p1 = QtWidgets.QLabel(self.page_1)
        self.label_theme_p1.setGeometry(QtCore.QRect(20, 100, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_theme_p1.setFont(font)
        self.label_theme_p1.setText(linecache.getline("Language/Language.txt", 535)[:-1])

        self.comboBox_theme_p1 = QtWidgets.QComboBox(self.page_1)
        self.comboBox_theme_p1.setGeometry(QtCore.QRect(120, 100, 141, 22))
        self.comboBox_theme_p1.addItem("Default")
        self.comboBox_theme_p1.addItem("Integrid")
        self.comboBox_theme_p1.addItem("Ubuntu")
        self.comboBox_theme_p1.addItem("Eclippy")
        self.comboBox_theme_p1.addItem("Combinear")
        self.comboBox_theme_p1.currentTextChanged.connect(lambda: self.button_save.setEnabled(True))

        """ Stacked widget page 2 """
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2 dock Type of chart")
        self.main_stackedWidget.addWidget(self.page_2)

        self.label_dock_position_p2 = QtWidgets.QLabel(self.page_2)
        self.label_dock_position_p2.setGeometry(QtCore.QRect(20, 10, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dock_position_p2.setFont(font)
        self.label_dock_position_p2.setText(linecache.getline("Language/Language.txt", 543)[:-1])

        self.comboBox_dock_position_p2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_dock_position_p2.setGeometry(QtCore.QRect(130, 10, 141, 22))
        self.comboBox_dock_position_p2.setObjectName("combo_box_language_5")
        self.comboBox_dock_position_p2.addItem(linecache.getline("Language/Language.txt", 545)[:-1])
        self.comboBox_dock_position_p2.addItem(linecache.getline("Language/Language.txt", 546)[:-1])
        self.comboBox_dock_position_p2.addItem(linecache.getline("Language/Language.txt", 547)[:-1])
        self.comboBox_dock_position_p2.addItem(linecache.getline("Language/Language.txt", 548)[:-1])
        self.comboBox_dock_position_p2.currentTextChanged.connect(lambda: self.button_save.setEnabled(True))

        self.label_stack_docks_p2 = QtWidgets.QLabel(self.page_2)
        self.label_stack_docks_p2.setGeometry(QtCore.QRect(20, 40, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_stack_docks_p2.setFont(font)
        self.label_stack_docks_p2.setText(linecache.getline("Language/Language.txt", 552)[:-1])

        self.check_stack_docks_p2 = QtWidgets.QCheckBox(self.page_2)
        self.check_stack_docks_p2.setGeometry(QtCore.QRect(130, 40, 21, 24))
        self.check_stack_docks_p2.setText("")
        self.check_stack_docks_p2.stateChanged.connect(lambda: self.button_save.setEnabled(True))

        """ Stacked widget page 3 """
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3 dock Value")
        self.main_stackedWidget.addWidget(self.page_3)

        self.label_dock_position_p3 = QtWidgets.QLabel(self.page_3)
        self.label_dock_position_p3.setGeometry(QtCore.QRect(20, 10, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dock_position_p3.setFont(font)
        self.label_dock_position_p3.setText(linecache.getline("Language/Language.txt", 543)[:-1])

        self.comboBox_dock_position_p3 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_dock_position_p3.setGeometry(QtCore.QRect(130, 10, 141, 22))
        self.comboBox_dock_position_p3.setObjectName("combo_box_language_5")
        self.comboBox_dock_position_p3.addItem(linecache.getline("Language/Language.txt", 545)[:-1])
        self.comboBox_dock_position_p3.addItem(linecache.getline("Language/Language.txt", 546)[:-1])
        self.comboBox_dock_position_p3.addItem(linecache.getline("Language/Language.txt", 547)[:-1])
        self.comboBox_dock_position_p3.addItem(linecache.getline("Language/Language.txt", 548)[:-1])
        self.comboBox_dock_position_p3.currentTextChanged.connect(lambda: self.button_save.setEnabled(True))
        self.label_stack_docks_p3 = QtWidgets.QLabel(self.page_3)
        self.label_stack_docks_p3.setGeometry(QtCore.QRect(20, 40, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_stack_docks_p3.setFont(font)
        self.label_stack_docks_p3.setText(linecache.getline("Language/Language.txt", 552)[:-1])

        self.check_stack_docks_p3 = QtWidgets.QCheckBox(self.page_3)
        self.check_stack_docks_p3.setGeometry(QtCore.QRect(130, 40, 21, 24))
        self.check_stack_docks_p3.setText("")
        self.check_stack_docks_p3.stateChanged.connect(lambda: self.button_save.setEnabled(True))

        """ Stacked widget page 4 """
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4 dock Settings")
        self.main_stackedWidget.addWidget(self.page_4)

        self.label_dock_position_p4 = QtWidgets.QLabel(self.page_4)
        self.label_dock_position_p4.setGeometry(QtCore.QRect(20, 10, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dock_position_p4.setFont(font)
        self.label_dock_position_p4.setText(linecache.getline("Language/Language.txt", 543)[:-1])

        self.comboBox_dock_position_p4 = QtWidgets.QComboBox(self.page_4)
        self.comboBox_dock_position_p4.setGeometry(QtCore.QRect(130, 10, 141, 22))
        self.comboBox_dock_position_p4.setObjectName("combo_box_language_5")
        self.comboBox_dock_position_p4.addItem(linecache.getline("Language/Language.txt", 545)[:-1])
        self.comboBox_dock_position_p4.addItem(linecache.getline("Language/Language.txt", 546)[:-1])
        self.comboBox_dock_position_p4.addItem(linecache.getline("Language/Language.txt", 547)[:-1])
        self.comboBox_dock_position_p4.addItem(linecache.getline("Language/Language.txt", 548)[:-1])
        self.comboBox_dock_position_p4.currentTextChanged.connect(lambda: self.button_save.setEnabled(True))

        self.label_stack_docks_p4 = QtWidgets.QLabel(self.page_4)
        self.label_stack_docks_p4.setGeometry(QtCore.QRect(20, 40, 120, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_stack_docks_p4.setFont(font)
        self.label_stack_docks_p4.setText(linecache.getline("Language/Language.txt", 552)[:-1])

        self.check_stack_docks_p4 = QtWidgets.QCheckBox(self.page_4)
        self.check_stack_docks_p4.setGeometry(QtCore.QRect(130, 40, 21, 24))
        self.check_stack_docks_p4.setText("")
        self.check_stack_docks_p4.stateChanged.connect(lambda: self.button_save.setEnabled(True))

        """ Stacked widget page 5 """
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5 general")
        self.main_stackedWidget.addWidget(self.page_5)

        self.label_dock_position_p5 = QtWidgets.QLabel(self.page_5)
        self.label_dock_position_p5.setGeometry(QtCore.QRect(50, 40, 140, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dock_position_p5.setFont(font)
        self.label_dock_position_p5.setText(linecache.getline("Language/Language.txt", 557)[:-1])

        """  """
        self.horizontal_line = QtWidgets.QFrame(main_window)
        self.horizontal_line.setGeometry(QtCore.QRect(10, 275, 531, 16))
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.button_reset = QtWidgets.QPushButton(main_window)
        self.button_reset.setGeometry(QtCore.QRect(300, 290, 75, 23))
        self.button_reset.setText(linecache.getline("Language/Language.txt", 559)[:-1])
        self.button_reset.clicked.connect(self.default_settings)

        self.button_cancel = QtWidgets.QPushButton(main_window)
        self.button_cancel.setGeometry(QtCore.QRect(460, 290, 75, 23))
        self.button_cancel.setText(linecache.getline("Language/Language.txt", 561)[:-1])

        self.button_save = QtWidgets.QPushButton(main_window)
        self.button_save.setGeometry(QtCore.QRect(380, 290, 75, 23))
        self.button_save.setText(linecache.getline("Language/Language.txt", 560)[:-1])
        self.button_save.clicked.connect(self.save_settings)

        self.main_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def treeWidget_clicked(self, type):
        if type.type() == 11:
            self.main_stackedWidget.setCurrentIndex(1)
            self.title_label.setText(linecache.getline("Language/Language.txt", 506)[:-1])

        elif type.type() == 121:
            self.main_stackedWidget.setCurrentIndex(2)
            self.title_label.setText(linecache.getline("Language/Language.txt", 511)[:-1] +
                                     " - " +
                                     linecache.getline("Language/Language.txt", 513)[:-1])

        elif type.type() == 122:
            self.main_stackedWidget.setCurrentIndex(3)
            self.title_label.setText(linecache.getline("Language/Language.txt", 511)[:-1] +
                                     " - " +
                                     linecache.getline("Language/Language.txt", 515)[:-1])

        elif type.type() == 123:
            self.title_label.setText(linecache.getline("Language/Language.txt", 511)[:-1] +
                                     " - " +
                                     linecache.getline("Language/Language.txt", 517)[:-1])
            self.main_stackedWidget.setCurrentIndex(4)

        elif type.type() == 21:
            self.main_stackedWidget.setCurrentIndex(5)
            self.title_label.setText(linecache.getline("Language/Language.txt", 524)[:-1])

    def default_settings(self):
        self.comboBox_language_p1.setCurrentText("English")
        self.comboBox_font_p1.setCurrentFont(QtGui.QFont("Arial"))
        self.comboBox_resolution_p1.setCurrentText("800 x 600")
        self.comboBox_theme_p1.setCurrentText("Default")
        self.comboBox_dock_position_p2.setCurrentIndex(2)
        self.check_stack_docks_p2.setCheckState(0)
        self.comboBox_dock_position_p3.setCurrentIndex(0)
        self.check_stack_docks_p3.setCheckState(0)
        self.comboBox_dock_position_p4.setCurrentIndex(0)
        self.check_stack_docks_p4.setCheckState(0)

    def starting_settings(self):
        self.comboBox_language_p1.setCurrentText(linecache.getline("settings.txt", 4)
                                                 [linecache.getline("settings.txt", 4).find("=") + 2: -1])
        self.comboBox_font_p1.setCurrentFont(QtGui.QFont(linecache.getline("settings.txt", 7)
                                                         [linecache.getline("settings.txt", 7).find("=") + 2: -1]))
        if (linecache.getline("settings.txt", 5) == 'Resolution1 = 800\n'
                and linecache.getline("settings.txt", 6) == 'Resolution2 = 600\n'):
            self.comboBox_resolution_p1.setCurrentText("800 x 600")

        self.comboBox_theme_p1.setCurrentText(linecache.getline("settings.txt", 8)
                                              [linecache.getline("settings.txt", 8).find("=") + 2: -1])

        self.comboBox_dock_position_p2.setCurrentIndex(int(linecache.getline("settings.txt", 9)
                                                           [linecache.getline("settings.txt", 9).find("=") + 2: -1]))
        if linecache.getline("settings.txt", 10)[linecache.getline("settings.txt", 10).find("=") + 2: -1] == "2":
            self.check_stack_docks_p2.setCheckState(2)
        else:
            self.check_stack_docks_p2.setCheckState(False)

        self.comboBox_dock_position_p3.setCurrentIndex(int(linecache.getline("settings.txt", 11)
                                                           [linecache.getline("settings.txt", 11).find("=") + 2:-1]))
        if linecache.getline("settings.txt", 12)[linecache.getline("settings.txt", 12).find("=") + 2: -1] == "2":
            self.check_stack_docks_p3.setCheckState(2)
        else:
            self.check_stack_docks_p3.setCheckState(False)

        self.comboBox_dock_position_p4.setCurrentIndex(int(linecache.getline("settings.txt", 13)
                                                           [linecache.getline("settings.txt", 13).find("=") + 2:-1]))
        if linecache.getline("settings.txt", 14)[linecache.getline("settings.txt",14).find("=") + 2: -1] == "2":
            self.check_stack_docks_p4.setCheckState(2)
        else:
            self.check_stack_docks_p4.setCheckState(False)

        self.button_save.setEnabled(False)

    def save_settings(self):
        information_message = QtWidgets.QMessageBox()
        information_message.setWindowTitle(linecache.getline("Language/Language.txt", 565)[:-1])
        information_message.setText(linecache.getline("Language/Language.txt", 566)[:-1])
        information_message.setIcon(QtWidgets.QMessageBox.Information)
        information_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        information_message.exec_()

        old_file = open("settings.txt").read()

        old_file = old_file.replace(linecache.getline("settings.txt", 4),
                                    ("Language = %s\n" % self.comboBox_language_p1.currentText()))
        old_file = old_file.replace(linecache.getline("settings.txt", 7),
                                    ("Font = %s\n" % self.comboBox_font_p1.currentFont().family()))
        old_file = old_file.replace(linecache.getline("settings.txt", 8),
                                    ("Theme = %s\n" % self.comboBox_theme_p1.currentText()))

        if self.comboBox_resolution_p1.currentText() == "800 x 600":
            old_file = old_file.replace(linecache.getline("settings.txt", 5), ("Resolution1 = %s\n" % "800"))
            old_file = old_file.replace(linecache.getline("settings.txt", 6), ("Resolution2 = %s\n" % "600"))

        print(self.comboBox_dock_position_p2.currentIndex())

        old_file = old_file.replace(linecache.getline("settings.txt", 9),
                                    ("Type of chart position = %s\n" % self.comboBox_dock_position_p2.currentIndex()))
        old_file = old_file.replace(linecache.getline("settings.txt", 10),
                                    ("Type of chart stack = %s\n" % self.check_stack_docks_p2.checkState()))

        old_file = old_file.replace(linecache.getline("settings.txt", 11),
                                    ("Value position = %s\n" % self.comboBox_dock_position_p3.currentIndex()))
        old_file = old_file.replace(linecache.getline("settings.txt", 12),
                                    ("Value stack = %s\n" % self.check_stack_docks_p3.checkState()))

        old_file = old_file.replace(linecache.getline("settings.txt", 13),
                                    ("Settings position = %s\n" % self.comboBox_dock_position_p4.currentIndex()))
        old_file = old_file.replace(linecache.getline("settings.txt", 14),
                                    ("Settings stack = %s\n" % self.check_stack_docks_p4.checkState()))

        new_file = open("settings.txt", 'w')
        new_file.write(old_file)
        new_file.close()
