# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stat_tool.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QFileDialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.data_day = QtWidgets.QTabWidget(Dialog)
        self.data_day.setGeometry(QtCore.QRect(0, 10, 631, 431))
        self.data_day.setObjectName("data_day")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 271, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.symbol_field = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.symbol_field.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.symbol_field.setContentsMargins(0, 0, 0, 0)
        self.symbol_field.setSpacing(7)
        self.symbol_field.setObjectName("symbol_field")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.symbol_field.addWidget(self.label)
        self.symbol = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.symbol.setObjectName("symbol")
        self.symbol_field.addWidget(self.symbol)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 271, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.start_time_field = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.start_time_field.setContentsMargins(0, 0, 0, 0)
        self.start_time_field.setObjectName("start_time_field")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.start_time_field.addWidget(self.label_2)
        self.start_time = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_2)
        self.start_time.setObjectName("start_time")
        self.start_time_field.addWidget(self.start_time)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 220, 271, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.barsize_field = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.barsize_field.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.barsize_field.setContentsMargins(0, 0, 0, 0)
        self.barsize_field.setSpacing(7)
        self.barsize_field.setObjectName("barsize_field")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.barsize_field.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.barsize_field.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 160, 271, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.end_time_field = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.end_time_field.setContentsMargins(0, 0, 0, 0)
        self.end_time_field.setObjectName("end_time_field")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.end_time_field.addWidget(self.label_3)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox.setEnabled(True)
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setObjectName("checkBox")
        self.end_time_field.addWidget(self.checkBox)
        self.end_time = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_3)
        self.end_time.setObjectName("end_time")
        self.end_time_field.addWidget(self.end_time)
        self.data_day.addTab(self.tab, "")
        self.data_mins = QtWidgets.QWidget()
        self.data_mins.setObjectName("data_mins")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.data_mins)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 50, 271, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.symbol_field_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.symbol_field_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.symbol_field_2.setContentsMargins(0, 0, 0, 0)
        self.symbol_field_2.setSpacing(7)
        self.symbol_field_2.setObjectName("symbol_field_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.symbol_field_2.addWidget(self.label_5)
        self.symbol_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.symbol_2.setObjectName("symbol_2")
        self.symbol_field_2.addWidget(self.symbol_2)
        self.data_day.addTab(self.data_mins, "")
        self.buttonBox.raise_()
        self.label_2.raise_()
        self.start_time.raise_()
        self.data_day.raise_()

        self.retranslateUi(Dialog)
        self.data_day.setCurrentIndex(0)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # self.checkBox.che

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Security symbol:"))
        self.label_2.setText(_translate("Dialog", "Start time:"))
        self.label_4.setText(_translate("Dialog", "Frequency:"))
        self.label_3.setText(_translate("Dialog", "End time:"))
        self.checkBox.setText(_translate("Dialog", "now"))
        self.data_day.setTabText(self.data_day.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.label_5.setText(_translate("Dialog", "Security symbol:"))
        self.data_day.setTabText(self.data_day.indexOf(self.data_mins), _translate("Dialog", "Tab 2"))
        self.start_time.setDateTime(QDateTime(2012, 12, 20, 11, 59, 59))
        self.end_time.setDateTime(QDateTime.currentDateTime())
        # self.data_type_day.



    def accept(self):
        print('accept')
        fileName2, ok2 = QFileDialog.getSaveFileName(self,"文件保存",
                                                     "C:/")
        print(fileName2)
        print(ok2)
        # print(self.symbol.text())
        # print(self.start_time.dateTime().toPyDateTime())
        # print(self.data_type_day.isChecked())

    def reject(self):
        pass