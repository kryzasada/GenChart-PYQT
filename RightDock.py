from PyQt5 import QtCore, QtWidgets


class Dock():
        def __init__(self, MainWindow):
                self.mainWindowInClass = MainWindow

        def right_up(self):
                self.dockWidget_1 = QtWidgets.QDockWidget(self.mainWindowInClass)

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.dockWidget_1.sizePolicy().hasHeightForWidth())

                self.dockWidget_1.setSizePolicy(sizePolicy)
                self.dockWidget_1.setMinimumSize(QtCore.QSize(130, 20))
                self.dockWidget_1.setObjectName("dockWidget_1")

                self.dockWidget_1Contents = QtWidgets.QWidget()
                self.dockWidget_1Contents.setObjectName("dockWidget_1Contents")
                self.dockWidget_1.setWidget(self.dockWidget_1Contents)
                self.mainWindowInClass.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_1)

        def right_down(self):
                self.dockWidget_2 = QtWidgets.QDockWidget(self.mainWindowInClass)

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())

                self.dockWidget_2.setSizePolicy(sizePolicy)
                self.dockWidget_2.setMinimumSize(QtCore.QSize(130, 20))
                self.dockWidget_2.setObjectName("dockWidget_2")

                self.dockWidgetContents_2 = QtWidgets.QWidget()
                self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
                self.dockWidget_2.setWidget(self.dockWidgetContents_2)
                self.mainWindowInClass.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
