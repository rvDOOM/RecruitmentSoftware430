# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_objects_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 626)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionView_Agency_s = QAction(MainWindow)
        self.actionView_Agency_s.setObjectName(u"actionView_Agency_s")
        self.actionView_Candidate_s = QAction(MainWindow)
        self.actionView_Candidate_s.setObjectName(u"actionView_Candidate_s")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 781, 561))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 40, 331, 131))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 311, 111))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.verticalLayout.addWidget(self.pushButton)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 210, 331, 201))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 311, 179))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.lineEdit_5 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.lineEdit_6 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.lineEdit_9 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_9.addWidget(self.lineEdit_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.lineEdit_7 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_7.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_17 = QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_17)

        self.lineEdit_8 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_8.addWidget(self.lineEdit_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.pushButton_3 = QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(360, 210, 411, 331))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(15, 10, 381, 301))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setUnderline(True)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.listView = QListView(self.layoutWidget1)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_4.addWidget(self.listView)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.lineEdit_12 = QLineEdit(self.layoutWidget1)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_12.addWidget(self.lineEdit_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.lineEdit_13 = QLineEdit(self.layoutWidget1)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_13.addWidget(self.lineEdit_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.pushButton_5 = QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.verticalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 21))
        self.label.setFont(font1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 111, 21))
        self.label_2.setFont(font1)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 180, 101, 21))
        self.label_6.setFont(font1)
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(360, 10, 121, 21))
        self.label_19.setFont(font1)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(360, 40, 331, 131))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame_9)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 10, 311, 111))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.lineEdit_10 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_10.addWidget(self.lineEdit_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_21 = QLabel(self.layoutWidget_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_21)

        self.lineEdit_11 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_11.addWidget(self.lineEdit_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.pushButton_4 = QPushButton(self.layoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.verticalLayout_5.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAdd)
        self.menuMenu.addAction(self.actionView_Candidate_s)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionView_Agency_s.setText(QCoreApplication.translate("MainWindow", u"View Agency's", None))
        self.actionView_Candidate_s.setText(QCoreApplication.translate("MainWindow", u"View Candidate's", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Agency Name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Industry Sector:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Phone Number: ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"E-mail: ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Agency List", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Position Name:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Number of Openings:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Recruiter ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Agency", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Candidate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add Req", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Add Recruiter", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

