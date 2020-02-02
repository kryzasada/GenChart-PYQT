# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.13.0
#
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import linecache

import window

try:
    file_line = linecache.getline("settings.txt", 3)
    if file_line == "First start = 1\n":
        old_file = open("settings.txt").read()
        old_file = old_file.replace('First start = 1', 'First start = 0')
        new_file = open("settings.txt", 'w')
        new_file.write(old_file)
        new_file.close()

        app1 = QApplication(sys.argv)
        MainWindow1 = QMainWindow()
        window1 = window.firstConfiguration()
        window1.contain(MainWindow1)
        window1.start_button.clicked.connect(lambda: MainWindow1.close())
        MainWindow1.show()
        sys.exit(app1.exec_())

finally:
    linecache.clearcache()

    app2 = QApplication(sys.argv)

    """ Set font and theme in main window """
    font_line = linecache.getline("settings.txt", 7)
    theme_line = linecache.getline("settings.txt", 8)
    if not theme_line[theme_line.find("=")+2: -1] == "Default":
        style_css = "Theme/%s.qss" % theme_line[theme_line.find("=")+2: -1]
        style = open(style_css, "r")
        app2.setStyleSheet(style.read() + "* {font-family: %s;}" % font_line[font_line.find("=")+2: -1])
    else:
        app2.setStyleSheet("* {font-family: %s;}" % font_line[font_line.find("=") + 2: -1])

    """ Set language in main window """
    if linecache.getline("settings.txt", 4) == "Language = English\n":
        new_language_file = open("Language/languageEnglish.txt").read()
    elif linecache.getline("settings.txt", 4) == "Language = Polski\n":
        new_language_file = open("Language/languagePolish.txt").read()

    new_file = open("Language/Language.txt", 'w')
    new_file.write(new_language_file)
    new_file.close()

    MainWindow2 = QMainWindow()
    window2 = window.main()
    window2.contain(MainWindow2)
    MainWindow2.show()
    sys.exit(app2.exec_())
