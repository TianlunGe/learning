# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_TabWidget(object):

    def __init__(self, data):
        self.data = data
        # self.dr = Figure_Canvas()
        pass

    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1040, 721)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ori_data = QtWidgets.QTableWidget(self.tab)
        self.ori_data.setGeometry(QtCore.QRect(30, 100, 731, 521))
        self.ori_data.setShowGrid(True)
        self.ori_data.setObjectName("ori_data")
        self.ori_data.setColumnCount(2)
        self.ori_data.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ori_data.setItem(1, 1, item)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.stats_info = QtWidgets.QTableWidget(self.tab1)
        self.stats_info.setGeometry(QtCore.QRect(30, 100, 731, 521))
        self.stats_info.setShowGrid(True)
        self.stats_info.setObjectName("stats_info")
        self.stats_info.setColumnCount(2)
        self.stats_info.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_info.setItem(1, 1, item)
        TabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(60, 90, 1200, 600))
        self.graphicsView.setObjectName("graphicsView")
        # self.openGLWidget = QtWidgets.QOpenGLWidget(self.tab_2)
        # self.openGLWidget.setGeometry(QtCore.QRect(560, 70, 300, 200))
        # self.openGLWidget.setObjectName("openGLWidget")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(80, 360, 281, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(550, 350, 331, 221))
        self.widget.setObjectName("widget")
        TabWidget.addTab(self.tab_2, "")

        self.save_stat = QtWidgets.QPushButton(self.tab_2)
        self.save_stat.setGeometry(QtCore.QRect(300, 640, 75, 23))
        self.save_stat.setObjectName("save_stat")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.ori_data.setSortingEnabled(False)
        item = self.ori_data.verticalHeaderItem(0)
        item.setText(_translate("TabWidget", "time"))
        item = self.ori_data.verticalHeaderItem(1)
        item.setText(_translate("TabWidget", "time2"))
        item = self.ori_data.horizontalHeaderItem(0)
        item.setText(_translate("TabWidget", "Close"))
        item = self.ori_data.horizontalHeaderItem(1)
        item.setText(_translate("TabWidget", "High"))
        __sortingEnabled = self.ori_data.isSortingEnabled()
        self.ori_data.setSortingEnabled(False)
        item = self.ori_data.item(0, 0)
        item.setText(_translate("TabWidget", "1"))
        item = self.ori_data.item(0, 1)
        item.setText(_translate("TabWidget", "2"))
        item = self.ori_data.item(1, 0)
        item.setText(_translate("TabWidget", "0"))
        item = self.ori_data.item(1, 1)
        item.setText(_translate("TabWidget", "3"))
        self.ori_data.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("TabWidget", "symbol:start_time - end_time"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))
        self.stats_info.setSortingEnabled(False)
        item = self.stats_info.verticalHeaderItem(0)
        item.setText(_translate("TabWidget", "time"))
        item = self.stats_info.verticalHeaderItem(1)
        item.setText(_translate("TabWidget", "time2"))
        item = self.stats_info.horizontalHeaderItem(0)
        item.setText(_translate("TabWidget", "Close"))
        item = self.stats_info.horizontalHeaderItem(1)
        item.setText(_translate("TabWidget", "High"))
        __sortingEnabled = self.stats_info.isSortingEnabled()
        self.stats_info.setSortingEnabled(False)
        item = self.stats_info.item(0, 0)
        item.setText(_translate("TabWidget", "1"))
        item = self.stats_info.item(0, 1)
        item.setText(_translate("TabWidget", "2"))
        item = self.stats_info.item(1, 0)
        item.setText(_translate("TabWidget", "0"))
        item = self.stats_info.item(1, 1)
        item.setText(_translate("TabWidget", "3"))
        self.stats_info.setSortingEnabled(__sortingEnabled)

        dr = Figure_Canvas()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        # dr.test()
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.save_stat.clicked.connect(self.change)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "页"))

    def change(self):
        dr = Figure_Canvas()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
        dr.test(x, y)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()


import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)
        self.x = [1,2,3,4,5,6,7,8,9]
        self.y = [23,21,32,13,3,132,13,3,1]

    def test(self,x, y):
        # x = [1,2,3,4,5,6,7,8,9]
        # y = [23,21,32,13,3,132,13,3,1]
        # self.x[0] = self.x[0] + 1
        self.axes.plot(x, y)