# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

import chart_test
import gameStat
import searchMatch

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.gameStat = gameStat.gameStat()
        self.groupBoxes = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    \n"
"    background-color: rgb(170, 255, 255);\n"
"    \n"
"    border-bottom: 3px solid rgb(0, 170, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    border:none;\n"
"    \n"
"    \n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    color : rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(170, 255, 255);\n"
"    border : none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_8.setStyleSheet("#frame_8{\n"
"    border:none;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.formLayout = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    border:none;\n"
"    \n"
"    \n"
"}")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("picture/23.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_9.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet("#frame_13{\n"
"    background-color:rgb(170, 255, 255);\n"
"    border-right: 3px solid rgb(0, 170, 255);\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_9{\n"
"    color:rgb(255, 255, 255);\n"
"    border:none;\n"
"    background-color: rgb(170, 255, 255);\n"
"\n"
"\n"
"}    \n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("picture/29.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.verticalLayout_3.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("#pushButton_10{\n"
"    color:rgb(255, 255, 255);\n"
"    border:none;\n"
"    background-color: rgb(170, 255, 255);\n"
"\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("picture/30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_6.addWidget(self.pushButton_10)
        self.verticalLayout_3.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_3.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_3.addWidget(self.frame_18)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet("#frame_14{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_14)
        self.stackedWidget.setStyleSheet("#page{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#page_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#page_3{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#page_4{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(30, 100, 281, 261))
        self.pushButton_11.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border:none")
        self.pushButton_11.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("picture/yasuo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(530, 210, 371, 71))
        self.lineEdit.setStyleSheet("\n"
"    border : 3px solid rgb(211, 217, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_12 = QtWidgets.QPushButton(self.page)
        self.pushButton_12.setGeometry(QtCore.QRect(350, 0, 461, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_12.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("#pushButton_12{\n"
"    color : rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border : none;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.comboBox_3 = QtWidgets.QComboBox(self.page)
        self.comboBox_3.setGeometry(QtCore.QRect(390, 210, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("    background-color: rgb(255, 255, 255);\n"
"    border : 3px solid rgb(211, 217, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_15 = QtWidgets.QPushButton(self.page)
        self.pushButton_15.setGeometry(QtCore.QRect(540, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("    border : 3px solid rgb(211, 217, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_200 = QtWidgets.QLabel(self.page)
        self.label_200.setGeometry(QtCore.QRect(590, 150, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_200.setFont(font)
        self.label_200.setStyleSheet("color :rgb(255, 0, 0);")
        self.label_200.setObjectName("label_200")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 220, 371, 71))
        self.lineEdit_2.setStyleSheet("\n"
"    border : 3px solid rgb(211, 217, 255);\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 220, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("    background-color: rgb(255, 255, 255);\n"
"    border : 3px solid rgb(211, 217, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 40, 461, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("#pushButton_13{\n"
"    color : rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border : none;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 100, 261, 251))
        self.pushButton_14.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border:none")
        self.pushButton_14.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("picture/TFT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_16.setGeometry(QtCore.QRect(600, 330, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("    border : 3px solid rgb(211, 217, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_201 = QtWidgets.QLabel(self.page_2)
        self.label_201.setGeometry(QtCore.QRect(600, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_201.setFont(font)
        self.label_201.setStyleSheet("color :rgb(255, 0, 0);")
        self.label_201.setObjectName("label_201")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 995, 607))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setMinimumSize(QtCore.QSize(941, 171))
        self.groupBox_2.setMaximumSize(QtCore.QSize(941, 171))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_26 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 0, 101, 101))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("profileicon/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon6)
        self.pushButton_17.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_18 = QtWidgets.QLabel(self.frame_26)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 81, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_26)
        self.label_19.setGeometry(QtCore.QRect(120, 9, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_40.setGeometry(QtCore.QRect(170, 100, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("background-color: rgb(137, 194, 255);\n"
"color : rgb(255, 255, 255);")
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_9.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_41.setGeometry(QtCore.QRect(40, 0, 101, 101))
        self.pushButton_41.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("profileicon/5290.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_41.setIcon(icon7)
        self.pushButton_41.setIconSize(QtCore.QSize(198, 100))
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_20 = QtWidgets.QLabel(self.frame_27)
        self.label_20.setGeometry(QtCore.QRect(40, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_42.setGeometry(QtCore.QRect(40, 0, 131, 131))
        self.pushButton_42.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("profileicon/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_42.setIcon(icon8)
        self.pushButton_42.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_42.setObjectName("pushButton_42")
        self.horizontalLayout_9.addWidget(self.frame_28)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_9.addWidget(self.line)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_9.addWidget(self.label_25)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_2.setGeometry(QtCore.QRect(-1, -4, 1021, 601))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1019, 599))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_4.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.frame_118 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_118.setGeometry(QtCore.QRect(30, 0, 561, 143))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_118.sizePolicy().hasHeightForWidth())
        self.frame_118.setSizePolicy(sizePolicy)
        self.frame_118.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_118.setObjectName("frame_118")
        self.label_237 = QtWidgets.QLabel(self.frame_118)
        self.label_237.setGeometry(QtCore.QRect(180, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_237.setFont(font)
        self.label_237.setObjectName("label_237")
        self.pushButton_366 = QtWidgets.QPushButton(self.frame_118)
        self.pushButton_366.setGeometry(QtCore.QRect(360, 100, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_366.setFont(font)
        self.pushButton_366.setStyleSheet("background-color: rgb(137, 194, 255);\n"
"color : rgb(255, 255, 255);")
        self.pushButton_366.setObjectName("pushButton_366")
        self.pushButton_365 = QtWidgets.QPushButton(self.frame_118)
        self.pushButton_365.setGeometry(QtCore.QRect(30, 0, 101, 101))
        self.pushButton_365.setText("")
        self.pushButton_365.setIcon(icon7)
        self.pushButton_365.setIconSize(QtCore.QSize(198, 100))
        self.pushButton_365.setObjectName("pushButton_365")
        self.label_236 = QtWidgets.QLabel(self.frame_118)
        self.label_236.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_236.setFont(font)
        self.label_236.setObjectName("label_236")
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setMaximumSize(QtCore.QSize(920, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_8.addWidget(self.label_21)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("#frame_4{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 13, 0, 13)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_10.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 10, 41, 41))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"    border:none;\n"
"    \n"
"    \n"
"    \n"
"}")
        self.pushButton_7.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("picture/音乐开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon9)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 10, 41, 41))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"    border:none;\n"
"    \n"
"    \n"
"}")
        self.pushButton_8.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("picture/28.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon10)
        self.pushButton_8.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # view more history button on the bottom of the scroll area
        self.tft_view_more = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.tft_view_more.setMaximumSize(QtCore.QSize(941, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(10)
        font.setWeight(75)
        self.tft_view_more.setFont(font)
        self.tft_view_more.setText("View more history")
        self.tft_view_more.clicked.connect(self.tft_view_more_history)
        self.tft_view_more.hide()

        self.lol_view_more = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.lol_view_more.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lol_view_more.setFont(font)
        self.lol_view_more.setText("View more history")
        self.lol_view_more.clicked.connect(self.lol_view_more_history)
        self.lol_view_more.hide()

    # text settings autogenerated by pyqt5 designer
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Match Up History "))
        self.pushButton_9.setText(_translate("MainWindow", " LOL"))
        self.pushButton_10.setText(_translate("MainWindow", " TFT"))
        self.pushButton_12.setText(_translate("MainWindow", "Search for Legue of Legends"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "North America"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Brazil"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "EU Nordic & East"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "EU West"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Japan"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Korea"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Latin America North"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Latin America South"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Oceania"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "PBE(public beta enviroment)"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Philippines"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Russia"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Singapore"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Thailand"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Turkey"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "Taiwan"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "Vietnam"))
        self.pushButton_15.setText(_translate("MainWindow", "Search"))
        self.label_200.setText(_translate("MainWindow", "Wrong name searched"))
        self.lineEdit_2.setText(_translate("MainWindow", ""))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "North America"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Brazil"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "EU Nordic & East"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "EU West"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Japan"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Korea"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Latin America North"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Latin America South"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Oceania"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "PBE(public beta enviroment)"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Philippines"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Russia"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Singapore"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Thailand"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Turkey"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Taiwan"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Vietnam"))
        self.pushButton_13.setText(_translate("MainWindow", "Search for Teamfight Tactics"))
        self.pushButton_16.setText(_translate("MainWindow", "Search"))
        self.label_201.setText(_translate("MainWindow", "Wrong name searched"))
        self.pushButton_40.setText(_translate("MainWindow", "Renew"))
        self.pushButton_366.setText(_translate("MainWindow", "Renew"))
        self.label_21.setText(_translate("MainWindow", "Match History"))

        # All functions
        # button functions

        self.pushButton_10.clicked.connect(self.display)
        self.pushButton_9.clicked.connect(self.display2)
        self.pushButton_15.clicked.connect(self.search_lol_name)
        self.pushButton_40.clicked.connect(self.search_lol_name)
        self.pushButton_16.clicked.connect(self.search_tft_name)
        self.pushButton_366.clicked.connect(self.search_tft_name)
        self.label_200.hide()
        self.label_201.hide()

    # change region buttons
    def display(self):
        self.stackedWidget.setCurrentIndex(1)

    def display2(self):
        self.stackedWidget.setCurrentIndex(0)

    # functions after user clicked search button
    # retrieve information for two input bar to create searchMatch based on given information
    def search_lol_name(self):

        # Get the search query from the search bar
        lol_query = self.lineEdit.text()
        lol_region_text = self.comboBox_3.currentText()
        if lol_query == "":
            print("False")
        else:
            self.Summoner = searchMatch.SearchMatch(lol_region_text, 'lol', lol_query)
            if not self.Summoner.searchComplete:
                self.label_200.show()
                QtCore.QTimer.singleShot(3000, self.label_200.hide)
                print("wrong name entered")
            else:
                # delete all existing match groupBox
                for i in self.groupBoxes:
                    i.deleteLater()
                # generate win rate graph
                self.win_rate_count()
                # generate static data of Summoner
                self.lol_stat()
                # generate at most 20 match group boxes
                self.lol_generate_boxes(20)
                self.stackedWidget.setCurrentIndex(2)
                print("right name entered")

    # retrieve information for two input bar to create searchMatch based on given information
    def search_tft_name(self):
        # search function for tft
        tft_query = self.lineEdit_2.text()
        tft_region_text = self.comboBox_2.currentText()
        if tft_query == "":
            print("False")
        else:
            self.Summoner = searchMatch.SearchMatch(tft_region_text, 'tft', tft_query)
            if not self.Summoner.searchComplete:
                self.label_201.show()
                QtCore.QTimer.singleShot(3000, self.label_201.hide)
                print("wrong name entered")
            else:
                # delete all existing match groupBox
                for i in self.groupBoxes:
                    i.deleteLater()

                # generate 20 boxes and append to the scroll widget
                self.tft_generate_boxes(20)
                self.stackedWidget.setCurrentIndex(3)
                print("right name entered")

    # view more history function
    def tft_view_more_history(self):
        self.verticalLayout_8.removeWidget(self.tft_view_more)
        num_match = len(self.groupBoxes)
        # change the match details of the Summoner to new match data
        self.Summoner.tft_view_more(num_match)
        # generate 10 boxes and append to the scroll widget
        self.tft_generate_boxes(10)
        self.stackedWidget.setCurrentIndex(3)

    def lol_view_more_history(self):
        self.verticalLayout_9.removeWidget(self.tft_view_more)
        num_match = len(self.groupBoxes)
        # change the match details of the Summoner to new match data
        self.Summoner.lol_view_more(num_match)
        # generate 10 boxes and append to the scroll widget
        self.lol_generate_boxes(10)
        self.stackedWidget.setCurrentIndex(2)

    def lol_generate_boxes(self, num):
        # remove the view more button if the button exist
        try:
            self.verticalLayout_9.removeWidget(self.lol_view_more)
            self.lol_view_more.hide()
        except AttributeError:
            pass
        self.groupBoxes = []
        self.viewCheck = True  # check if error caught in the range
        # create groupboxes and layout for each match
        for i in range(len(self.Summoner.match_details)):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
            groupBox.setMinimumSize(QtCore.QSize(941, 191))
            self.groupBoxes.append(groupBox)
            self.lol_groupBox(0, i)
        if len(self.Summoner.match_details) == num and self.viewCheck:
            self.verticalLayout_9.addWidget(self.lol_view_more)
            self.lol_view_more.show()

    # generate groupboxes and attach to the main windows
    def tft_generate_boxes(self, num):
        # remove the view more button if the button exist
        try:
            self.verticalLayout_8.removeWidget(self.tft_view_more)
            self.tft_view_more.hide()
        except AttributeError:
            pass
        self.groupBoxes = []
        self.viewCheck = True  # check if error caught in the range
        # create groupboxes and layout for each match
        for i in range(len(self.Summoner.match_details)):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
            groupBox.setMinimumSize(QtCore.QSize(0, 230))
            groupBox.setMaximumSize(QtCore.QSize(1000, 16777215))
            self.groupBoxes.append(groupBox)
            try:
                self.tft_groupBox(0, i)
            except KeyError:
                self.gameStat.change_version("13.4.1")
                try:
                    self.tft_groupBox(0, i)
                except KeyError:
                    groupBox.hide()
                    self.viewCheck = False
                    break
        self.gameStat.change_version("13.6.1")
        if len(self.Summoner.match_details) == num and self.viewCheck:
            self.verticalLayout_8.addWidget(self.tft_view_more)
            self.tft_view_more.show()

    # return the index of the in-match data of the summoner being searched
    def find_self_participant(self, index):
        participants_list = self.Summoner.match_details[index]['info']['participants']
        # find index of summoner in lol game
        if self.Summoner.gameType == 'lol':
            for participant in participants_list:
                if participant['summonerName'] == self.Summoner.summonerName:
                    return participants_list.index(participant)
        # find index of summoner in tft games
        elif self.Summoner.gameType == 'tft':
            for participant in participants_list:
                if participant['puuid'] == self.Summoner.me['puuid']:
                    return participants_list.index(participant)

    # return victory or lost based on the win boolean retrieved from api
    def win_or_lose(self, bool):
        if bool:
            return "Victory"
        else:
            return "Lost"

    # helper function to determine how long since the indicated game finished
    def time_previous(self, gameTime):
        currentTime = time.time()
        timeDiff = int(currentTime) - int(gameTime / 1000)
        if timeDiff < 3600:
            return f"{int(timeDiff / 60)} minutes ago"
        elif 3600 < timeDiff < 86400:
            return f"{int(timeDiff / 3600)} hours ago"
        elif timeDiff > 86400:
            return f"{int(timeDiff / 86400)} days ago"

    def lol_stat(self):
        # set win rate graph display
        win_rate_graph = QtGui.QIcon()
        win_rate_graph.addPixmap(
            QtGui.QPixmap("win_rate.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.pushButton_42.setIcon(win_rate_graph)

        # display profile icon
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(f"profileicon/{self.Summoner.me['profileIconId']}.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon17)

        # display ranked emblem image of summoner
        if len(self.Summoner.rankedInfo) != 0:
            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap(f"ranked-emblem/emblem-{self.Summoner.rankedInfo[0]['tier']}.png"),
                             QtGui.QIcon.Normal,
                             QtGui.QIcon.Off)
            self.pushButton_41.setIcon(icon18)
        else:

            self.pushButton_41.setIcon(QtGui.QIcon("items/7050.png"))

        _translate = QtCore.QCoreApplication.translate
        # set level of summoner
        self.label_18.setText(_translate("MainWindow", f"lv : {self.Summoner.me['summonerLevel']}"))
        # set the summoner name display
        self.label_19.setText(_translate("MainWindow", f"{self.Summoner.summonerName}"))
        # set the ranked text
        try:
            self.label_20.setText(_translate("MainWindow", f"{self.Summoner.rankedInfo[0]['tier']}"))
        except IndexError:
            self.label_20.setText(_translate("MainWindow", "N/A"))
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setText("Match history")
        self.verticalLayout_9.addWidget(self.label_25)

    # create a match groupbox
    def lol_groupBox(self, start, index):
        self_Participant = self.Summoner.match_details[index]['info']['participants'][self.find_self_participant(index)]
        # groupBox set
        lol_parentBoxes = []
        # set vertical layout for first 2 frames ----- [0, 1]
        layoutWidget = QtWidgets.QWidget(self.groupBoxes[start + index])
        layoutWidget.setGeometry(QtCore.QRect(10, 20, 191, 161))
        lol_parentBoxes.append(layoutWidget)
        verticalLayout = QtWidgets.QVBoxLayout(layoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        lol_parentBoxes.append(verticalLayout)
        # set vertical layout for middle 2 frames ----- [2, 3]
        layoutWidget = QtWidgets.QWidget(self.groupBoxes[start + index])
        layoutWidget.setGeometry(QtCore.QRect(250, 20, 371, 180))
        lol_parentBoxes.append(layoutWidget)
        verticalLayout = QtWidgets.QVBoxLayout(layoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        lol_parentBoxes.append(verticalLayout)
        # set groupBox for all champ display groupbox ----- [4, 5]
        frame = QtWidgets.QFrame(self.groupBoxes[start + index])
        frame.setGeometry(QtCore.QRect(649, 20, 281, 161))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        lol_parentBoxes.append(frame)
        horizontalLayout = QtWidgets.QHBoxLayout(frame)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        lol_parentBoxes.append(horizontalLayout)

        # frame set
        lol_info_frames = []
        for i in range(2):
            frame = QtWidgets.QFrame(lol_parentBoxes[0])
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            lol_parentBoxes[1].addWidget(frame)
            lol_info_frames.append(frame)
        # rank solo and game history time frame
        lol_info_frames[0].setGeometry(QtCore.QRect(1, 1, 189, 75))
        # game time and win/lose frame
        lol_info_frames[1].setGeometry(QtCore.QRect(1, 85, 189, 75))

        # frame set
        lol_Summoner_frame = []
        for i in range(2):
            frame = QtWidgets.QFrame(lol_parentBoxes[2])
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            lol_parentBoxes[3].addWidget(frame)
            lol_Summoner_frame.append(frame)
        # champion image part
        lol_Summoner_frame[0].setGeometry(QtCore.QRect(1, 1, 369, 96))
        # item frame
        lol_Summoner_frame[1].setGeometry(QtCore.QRect(1, 110, 369, 57))

        # frame set
        lol_Participants_frame = []
        for i in range(2):
            frame = QtWidgets.QFrame(lol_parentBoxes[4])
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            lol_parentBoxes[5].addWidget(frame)
            lol_Participants_frame.append(frame)
        # left part summoners frame
        lol_Participants_frame[0].setGeometry(QtCore.QRect(1, 1, 135, 159))
        # right part summoners frame
        lol_Participants_frame[1].setGeometry(QtCore.QRect(145, 1, 135, 159))


        # label set in frame[0]
        # label of one frame
        lol_matchInfo = []
        for i in range(2):
            info = QtWidgets.QLabel(lol_info_frames[0])
            lol_matchInfo.append(info)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)

        lol_matchInfo[0].setGeometry(QtCore.QRect(10, 10, 111, 18))
        lol_matchInfo[0].setFont(font)
        # set Queue name
        lol_matchInfo[0].setText(self.gameStat.identify_queue(self.Summoner.match_details[index]['info']['queueId']))

        # xxx hours ago label
        lol_matchInfo[1].setGeometry(QtCore.QRect(10, 40, 181, 31))
        lol_matchInfo[1].setFont(font)
        # set how many time passed
        lol_matchInfo[1].setText(f"{self.time_previous(self.Summoner.match_details[index]['info']['gameEndTimestamp'])}")

        # label set in frame[1]
        # label of one frame
        # win/lose and game time info
        lol_GameTime = []
        for i in range(2):
            info = QtWidgets.QLabel(lol_info_frames[1])
            lol_GameTime.append(info)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)

        lol_GameTime[0].setGeometry(QtCore.QRect(10, 10, 70, 18))
        lol_GameTime[0].setFont(font)
        # set the text for Victory or Lost
        lol_GameTime[0].setText(
            f"{self.win_or_lose(self_Participant['win'])}")
        # set background color for the groupbox based on win or lose of the game
        if self_Participant['win']:
            self.groupBoxes[start + index].setStyleSheet("background-color: rgb(137, 194, 255);")
        else:
            self.groupBoxes[start + index].setStyleSheet("background-color: rgb(255, 103, 89);")

        lol_GameTime[1].setGeometry(QtCore.QRect(10, 40, 70, 18))
        lol_GameTime[1].setFont(font)
        # set game duration
        lol_GameTime[1].setText(f"{int(self.Summoner.match_details[index]['info']['gameDuration'] / 60)}m {self.Summoner.match_details[index]['info']['gameDuration'] % 60}s")


        # pushButtons and labels in frame[2]
        # Champ icon pushButton
        lol_match_champ = QtWidgets.QPushButton(lol_Summoner_frame[0])
        lol_match_champ.setGeometry(QtCore.QRect(30, 0, 61, 61))
        lol_match_champ.setIconSize(QtCore.QSize(70, 70))

        # summoner Spell
        lol_Spell = []
        for i in range(2):
            lolSpell_icon = QtWidgets.QPushButton(lol_Summoner_frame[0])
            lolSpell_icon.setGeometry(QtCore.QRect(100, i * 30, 31, 34))
            lolSpell_icon.setIconSize(QtCore.QSize(30, 30))
            lol_Spell.append(lolSpell_icon)

        # text labels setting in frame[2]
        lol_frame2Text = []
        for i in range(3):
            info = QtWidgets.QLabel(lol_Summoner_frame[0])
            lol_frame2Text.append(info)

        # level label
        lol_frame2Text[0].setGeometry(QtCore.QRect(30, 70, 61, 20))
        lol_frame2Text[0].setFont(font)
        # set champion level of the summoner
        lol_frame2Text[0].setText(f"lv:{self_Participant['champLevel']}")

        # Kill/Death/Assist label
        font1 = QtGui.QFont()
        font1.setFamily("Bodoni MT Black")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)

        lol_frame2Text[1].setGeometry(QtCore.QRect(230, 20, 131, 20))
        lol_frame2Text[1].setFont(font1)
        # set KDA of the Summoner
        lol_frame2Text[1].setText(f"{self_Participant['kills']} / {self_Participant['deaths']} / {self_Participant['assists']}")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        # total kda count
        lol_frame2Text[2].setGeometry(QtCore.QRect(240, 60, 121, 20))
        lol_frame2Text[2].setFont(font)
        # Set total KDA of the summoner
        lol_frame2Text[2].setText(f"{self.cal_KDA(self_Participant['kills'], self_Participant['deaths'], self_Participant['assists'])} KDA")

        # Runes pushButtons
        lol_Runes = []
        for i in range(2):
            lolRune_icon = QtWidgets.QPushButton(lol_Summoner_frame[0])
            lolRune_icon.setGeometry(QtCore.QRect(140, i * 30, 31, 34))
            lolRune_icon.setIconSize(QtCore.QSize(30, 30))
            lol_Runes.append(lolRune_icon)

        # frame[3]
        # item pushButtons in frame[3]
        lol_items = []
        # 9 item icon pushButtons
        for i in range(7):
            lolItem_icon = QtWidgets.QPushButton(lol_Summoner_frame[1])
            lolItem_icon.setGeometry(QtCore.QRect(30 + 40 * i, 10, 41, 41))
            lolItem_icon.setIconSize(QtCore.QSize(30, 30))
            lol_items.append(lolItem_icon)
        lol_items[-1].setStyleSheet("    QPushButton {\n"
                                         "        border-radius: 16px;\n"
                                         "        \n"
                                         "        \n"
                                         "    background-color: rgb(0, 170, 255);\n"
                                         "    }")
        # frame[4]
        # left side summoner name and icon pushButtons and labels
        # summoner icon pushbutton
        lol_left_SummonerIcon = []
        # 5 player icon pushButtons
        for i in range(5):
            lolSummoner_icon = QtWidgets.QPushButton(lol_Participants_frame[0])
            lolSummoner_icon.setGeometry(QtCore.QRect(0, 30 * i, 31, 31))
            lolSummoner_icon.setIconSize(QtCore.QSize(25, 25))
            lol_left_SummonerIcon.append(lolSummoner_icon)

        # summoner name text label
        lol_left_SummonerLabel = []
        # 5 player icon pushButtons
        for i in range(5):
            lolSummoner_name = QtWidgets.QLabel(lol_Participants_frame[0])
            lolSummoner_name.setGeometry(QtCore.QRect(40, 10 + 30 * i, 90, 18))
            lolSummoner_name.setFont(font)
            lol_left_SummonerLabel.append(lolSummoner_name)

        # frame[5]
        # right side summoner name and icon pushButtons and labels
        # summoner icon pushbuttons
        lol_right_SummonerIcon = []
        # 5 player icon pushButtons
        for i in range(5):
            lolSummoner2_icon = QtWidgets.QPushButton(lol_Participants_frame[1])
            lolSummoner2_icon.setGeometry(QtCore.QRect(0, 30 * i, 31, 31))
            lolSummoner2_icon.setIconSize(QtCore.QSize(25, 25))
            lol_right_SummonerIcon.append(lolSummoner2_icon)

        # summoner name text label
        lol_right_SummonerLabel = []
        # 5 player icon pushButtons
        for i in range(5):
            lolSummoner_name = QtWidgets.QLabel(lol_Participants_frame[1])
            lolSummoner_name.setGeometry(QtCore.QRect(40, 10 + 30 * i, 90, 18))
            lolSummoner_name.setFont(font)
            lol_right_SummonerLabel.append(lolSummoner_name)

        # add groupbox to vertical layout
        self.verticalLayout_9.addWidget(self.groupBoxes[index])

        # Summoner match info img display
        # items img display
        for i in range(7):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"item/{self_Participant[f'item{i}']}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            lol_items[i].setIcon(icon)

            # summoner champ icon display
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"champion-icon/{self_Participant['championId']}.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            lol_match_champ.setIcon(icon)

        # summoner Spell display
        for i in range(2):
            summonerSpell = QtGui.QIcon()
            summonerSpell.addPixmap(
                QtGui.QPixmap(
                    f"summonerSpell/{self.gameStat.identify_Summoner_spell(self_Participant[f'summoner{i + 1}Id'])}"),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off)
            lol_Spell[i].setIcon(summonerSpell)

        # summoner Rune display
        runeUrlPath = 'https://ddragon.canisback.com/img/'
        rune = QtGui.QIcon()
        primaryRunePath = self.gameStat.identify_runes(
            self_Participant['perks']['styles'][0]['selections'][0]['perk'])
        primaryRuneimg = QtGui.QImage()
        primaryRuneimg.loadFromData(requests.get(runeUrlPath + primaryRunePath).content)
        rune.addPixmap(QtGui.QPixmap(primaryRuneimg),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        lol_Runes[0].setIcon(rune)

        rune2 = QtGui.QIcon()
        subRunePath = self.gameStat.identify_runes(
            self_Participant['perks']['styles'][1]['style'])
        subRuneimg = QtGui.QImage()
        subRuneimg.loadFromData(requests.get(runeUrlPath + subRunePath).content)
        rune2.addPixmap(QtGui.QPixmap(subRuneimg),
                        QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        lol_Runes[1].setIcon(rune2)

        # participants name display
        for i in range(5):
            lol_left_SummonerLabel[i].setText(self.Summoner.match_details[index]['info']['participants'][i]['summonerName'])
            lol_right_SummonerLabel[i].setText(self.Summoner.match_details[index]['info']['participants'][5 + i]['summonerName'])
        # participants champion img display
        for i in range(5):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"champion-icon/{self.Summoner.match_details[index]['info']['participants'][i]['championId']}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            lol_left_SummonerIcon[i].setIcon(icon)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f"champion-icon/{self.Summoner.match_details[index]['info']['participants'][5 + i]['championId']}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            lol_right_SummonerIcon[i].setIcon(icon)
        print(f"match {index} completed")

    # create a match groupbox
    def tft_groupBox(self, start, index):
        # groupBox set
        # frame set
        self.tft_frames = []
        for i in range(3):
            frame = QtWidgets.QFrame(self.groupBoxes[start + index])
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.tft_frames.append(frame)
        self.tft_frames[0].setGeometry(QtCore.QRect(10, 40, 241, 161))
        self.tft_frames[1].setGeometry(QtCore.QRect(260, 10, 711, 141))
        self.tft_frames[2].setGeometry(QtCore.QRect(310, 160, 621, 71))

        # label set
        # label of 1 frame
        self.matchInfo = []
        for i in range(3):
            info = QtWidgets.QLabel(self.tft_frames[0])
            self.matchInfo.append(info)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        # match placement of summoner
        self.matchInfo[0].setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.matchInfo[0].setFont(font)
        self.matchInfo[0].setText(self.placement_trans(
            self.Summoner.match_details[index]['info']['participants'][self.find_self_participant(index)]['placement']))
        # game queue name
        self.matchInfo[1].setGeometry(QtCore.QRect(10, 60, 181, 41))
        font.setPointSize(10)
        self.matchInfo[1].setFont(font)
        self.matchInfo[1].setText(self.gameStat.identify_tft_queue(
            self.Summoner.match_details[index]['info']['queue_id']))
        # game time period
        self.matchInfo[2].setText(
            self.time_previous(self.Summoner.match_details[index]['info']['game_datetime']))
        self.matchInfo[2].setGeometry(QtCore.QRect(10, 100, 191, 41))
        self.matchInfo[2].setFont(font)
        # rank place text
        try:
            self.label_236.setText(f"{self.Summoner.rankedInfo[0]['tier']}")
        except KeyError:
            self.label_236.setText("N/A")
        except IndexError:
            self.label_236.setText("N/A")
        # summoner Name
        self.label_237.setText(f"{self.Summoner.summonerName}")
        # traits are labels for 3 frame
        # traits level
        self.traitLevels = []
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        for i in range(9):
            traitLevel = QtWidgets.QLabel(self.tft_frames[2])
            traitLevel.setGeometry(QtCore.QRect(40 + i * 60, 40, 31, 21))
            traitLevel.setFont(font)
            self.traitLevels.append(traitLevel)

        # push button for 2 frame
        # tactics icon setting
        self.tac_icons = []
        for i in range(9):
            tac_icon = QtWidgets.QPushButton(self.tft_frames[1])
            tac_icon.setGeometry(QtCore.QRect(i * 80, 30, 69, 69))
            tac_icon.setIconSize(QtCore.QSize(60, 60))
            self.tac_icons.append(tac_icon)

        # items buttons
        self.tac_items = []
        for i in range(27):
            tac_item = QtWidgets.QPushButton(self.tft_frames[1])
            tac_item.setGeometry(QtCore.QRect(i * 20 + int(i/3) * 20, 100, 21, 21))
            tac_item.setIconSize(QtCore.QSize(35, 35))
            self.tac_items.append(tac_item)

        # stars buttons
        self.tac_stars = []
        for i in range(9):
            star = QtWidgets.QPushButton(self.tft_frames[1])
            star.setGeometry(QtCore.QRect(20 + i * 80, 0, 31, 31))
            star.setIconSize(QtCore.QSize(35, 35))
            self.tac_stars.append(star)

        # pushButtons for 3 frame
        # 9 buttons
        self.traits = []
        for i in range(9):
            trait = QtWidgets.QPushButton(self.tft_frames[2])
            trait.setGeometry(QtCore.QRect(30 + (i * 60), 0, 47, 41))
            trait.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.traits.append(trait)

        # add groupbox to vertical layout
        self.verticalLayout_8.addWidget(self.groupBoxes[index])

        # settings for images
        self_Participant = self.Summoner.match_details[index]['info']['participants'][self.find_self_participant(index)]
        imageurl = f"https://ddragon.leagueoflegends.com/cdn/{self.gameStat.version}/img/"
        numUnit = len(self_Participant['units'])
        item_count = 0
        # display image of champion and items
        for i in range(numUnit if numUnit < 10 else 9):
            champIcon = QtGui.QIcon()
            unitImg = QtGui.QImage()
            champ = self_Participant['units'][i]['character_id']
            if champ == "TFT8_Zac":
                unitImg.loadFromData(requests.get('https://ddragon.leagueoflegends.com/cdn/13.4.1/img/tft-hero-augment/TFT8_Zac.TFT_Set8.png').content)
            else:
                unitImg.loadFromData(requests.get(
                    imageurl + "tft-hero-augment/" + self.gameStat.identify_tft_champion(champ)).content)
            champIcon.addPixmap(QtGui.QPixmap(unitImg), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tac_icons[i].setIcon(champIcon)

            # display star image
            starIcon = QtGui.QIcon()
            starIcon.addPixmap(QtGui.QPixmap(self._star_trans(self_Participant['units'][i]['tier'])),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tac_stars[i].setIcon(starIcon)
            for j in range(len(self_Participant['units'][i]['itemNames'])):
                itemIcon = QtGui.QIcon()
                itemImg = QtGui.QImage()
                itemName = self.tft_item_trans(self_Participant['units'][i]['itemNames'][j])
                itemImg.loadFromData(
                    requests.get(imageurl + "tft-item/" + self.gameStat.identify_tft_item(itemName)).content)
                itemIcon.addPixmap(QtGui.QPixmap(itemImg), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.tac_items[item_count + j].setIcon(itemIcon)
            item_count += 3

        active_traits = []
        for i in self_Participant['traits']:
            if i['tier_current'] != 0:
                active_traits.append(i)
        active_traits = sorted(active_traits, key=lambda d: d['tier_current'], reverse=True)
        for i in range(len(active_traits) if len(active_traits) < len(self.traits) else len(self.traits)):
            trait_icon = QtGui.QIcon()
            traitImg = QtGui.QImage()
            traitImg.loadFromData(requests.get(
                imageurl + "tft-trait/" + self.gameStat.identify_tft_trait(
                    active_traits[i]['name'])).content)
            trait_icon.addPixmap(QtGui.QPixmap(traitImg), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.traits[i].setIcon(trait_icon)

            # display trait level text
            self.traitLevels[i].setText(f"{active_traits[i]['num_units']}")
        # display ranked emblem image of summoner
        if len(self.Summoner.rankedInfo) != 0:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self._trans_rank()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_365.setIcon(icon)
        else:
            self.pushButton_365.setIcon(QtGui.QIcon("items/7050.png"))
        print(f"Match {index} finished")
        
    def _star_trans(self, level):
        # based on the level of the given champion level produce the name of different star picture
        if level == 1:
            return "picture/bronze.png"
        elif level == 2:
            return "picture/silver.png"
        elif level == 3:
            return "picture/gold.png"

    # translate TFT rank given by api to fileName
    def _trans_rank(self):
        # try to get the ranked info of the summoner, if None then return address to empty picture for output
        try:
            rank = self.Summoner.rankedInfo[0]['tier']
        except KeyError:
            return "items/7050.png"
        # translate from rank given to address to file
        trans = rank[0]
        trans += rank[1:].lower()
        return f"tft-regalia/TFT_Regalia_{trans}.png"

    # translate Api tft item data to json file indicator
    def tft_item_trans(self, itemName):
        # by the information given back from Api, translate to actual item address
        if itemName.split("_")[0] == "TFT5":
            return "Set5_RadiantItems/" + itemName
        elif itemName.split("_")[0] == "TFT7":
            return "TFT7_ShimmerscaleItems/" + itemName
        elif itemName.split("_")[0] == "TFT8" and itemName.split("_")[-1] == "GenAE":
            return "TFT8_GenAEItems/" + itemName
        elif itemName.split("_")[0] == "TFT8":
            return "TFT8_EmblemItems/" + itemName
        return itemName

    # translate number placement to numeric
    def placement_trans(self, placement):
        # translate
        if placement < 1:
            return "N/A"
        elif placement == 1:
            return "1st place"
        elif placement == 2:
            return "2nd place"
        elif placement == 3:
            return "3rd place"
        else:
            return f"{placement}th place"

    # calculate the KDA given kill death assists
    def cal_KDA(self, kill, death, assist):
        if death == 0:
            return "Perfect KDA"
        else:
            return round((kill + assist) / death, 1)

    # calculate the win rate of the summoner then graph the win rate graph using function from chart_test
    def win_rate_count(self):
        win_count = 0
        for i in self.Summoner.match_details:
            if i['info']['participants'][self.find_self_participant(i in self.Summoner.match_details)]['win']:
                win_count += 1
        if len(self.Summoner.match_details) == 0:
            return "No available match"
        graph = chart_test.WinLoseCircleGraph(round(win_count / len(self.Summoner.match_details), 2))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
