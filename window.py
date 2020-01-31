from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
import dock, menuStatusBar


class firstConfiguration:
    def contain(self, main_window):
        main_window.resize(568, 431)
        main_window.setWindowIcon(QtGui.QIcon("Image/Icons/blank-logo.ico"))
        main_window.setWindowTitle("GenChart - First Time Configuration")

        self.central_widget = QtWidgets.QWidget(main_window)
        main_window.setCentralWidget(self.central_widget)

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
        self.language_combo_box.addItem("Polish")

        self.font_label = QtWidgets.QLabel(self.central_widget)
        self.font_label.setGeometry(QtCore.QRect(40, 90, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_label.setFont(font)
        self.font_label.setText("Font:")

        self.font_combo_box = QtWidgets.QFontComboBox(self.central_widget)
        self.font_combo_box.setGeometry(QtCore.QRect(130, 90, 141, 22))
        self.font_combo_box.setCurrentFont(QtGui.QFont("Arial"))

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
        self.resolution_combo_box.setGeometry(QtCore.QRect(380, 60, 141, 22))
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
        self.theme_label.setText("Theme")

        self.theme_combo_box = QtWidgets.QComboBox(self.central_widget)
        self.theme_combo_box.setGeometry(QtCore.QRect(130, 140, 141, 22))
        self.theme_combo_box.addItem("Default")
        self.theme_combo_box.addItem("Eclippy")
        self.theme_combo_box.addItem("Ubuntu")

        self.theme_stacked = QtWidgets.QStackedWidget(self.central_widget)
        self.theme_stacked.setGeometry(QtCore.QRect(290, 140, 231, 221))
        self.theme_stacked.setObjectName("stackedWidget")

        self.theme_page1 = QtWidgets.QWidget()
        self.theme_page1.setObjectName("page")
        self.theme_page1.setStyleSheet("background-color: rgb(125, 125, 125);")

        self.theme_page2 = QtWidgets.QWidget()
        self.theme_page2.setObjectName("page_2")
        self.theme_page2.setStyleSheet("background-color: #1CE;")

        self.theme_stacked.addWidget(self.theme_page1)
        self.theme_stacked.addWidget(self.theme_page2)

        self.line3_horizontal = QtWidgets.QFrame(self.central_widget)
        self.line3_horizontal.setGeometry(QtCore.QRect(20, 370, 531, 16))
        self.line3_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.start_button = QtWidgets.QPushButton(self.central_widget)
        self.start_button.setGeometry(QtCore.QRect(460, 390, 75, 23))
        self.start_button.setText("START")

        QtCore.QMetaObject.connectSlotsByName(main_window)


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

            menu_bar = menuStatusBar.MenuBar(main_window, showDock)
            status_bar = menuStatusBar.StatusBar(main_window)

            QtCore.QMetaObject.connectSlotsByName(main_window)

            """
                style_css = "Theme/darkorange.css"
                style = open(style_css, "r")
                app.setStyleSheet(style.read())
            """