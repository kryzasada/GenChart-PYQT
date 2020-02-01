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
    MainWindow2 = QMainWindow()
    window2 = window.main()
    window2.contain(MainWindow2)
    MainWindow2.show()
    sys.exit(app2.exec_())

