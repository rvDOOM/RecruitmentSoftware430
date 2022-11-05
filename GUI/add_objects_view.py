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

        self.agency_name_input = QLineEdit(self.layoutWidget)
        self.agency_name_input.setObjectName(u"agency_name_input")

        self.horizontalLayout.addWidget(self.agency_name_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.industry_sector_input = QLineEdit(self.layoutWidget)
        self.industry_sector_input.setObjectName(u"industry_sector_input")

        self.horizontalLayout_2.addWidget(self.industry_sector_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.agency_button = QPushButton(self.layoutWidget)
        self.agency_button.setObjectName(u"agency_button")
        self.agency_button.setFont(font)

        self.verticalLayout.addWidget(self.agency_button)

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
        self.first_name_label = QLabel(self.layoutWidget_2)
        self.first_name_label.setObjectName(u"first_name_label")
        self.first_name_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.first_name_label)

        self.candidate_first_name_input = QLineEdit(self.layoutWidget_2)
        self.candidate_first_name_input.setObjectName(u"candidate_first_name_input")

        self.horizontalLayout_5.addWidget(self.candidate_first_name_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.last_name_label = QLabel(self.layoutWidget_2)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.last_name_label)

        self.candidate_last_name_input = QLineEdit(self.layoutWidget_2)
        self.candidate_last_name_input.setObjectName(u"candidate_last_name_input")

        self.horizontalLayout_6.addWidget(self.candidate_last_name_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.address_label = QLabel(self.layoutWidget_2)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.address_label)

        self.address_input = QLineEdit(self.layoutWidget_2)
        self.address_input.setObjectName(u"address_input")

        self.horizontalLayout_9.addWidget(self.address_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.number_label = QLabel(self.layoutWidget_2)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.number_label)

        self.number_input = QLineEdit(self.layoutWidget_2)
        self.number_input.setObjectName(u"number_input")

        self.horizontalLayout_7.addWidget(self.number_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.email_label = QLabel(self.layoutWidget_2)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.email_label)

        self.email_input = QLineEdit(self.layoutWidget_2)
        self.email_input.setObjectName(u"email_input")

        self.horizontalLayout_8.addWidget(self.email_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.candidate_button = QPushButton(self.layoutWidget_2)
        self.candidate_button.setObjectName(u"candidate_button")
        self.candidate_button.setFont(font)

        self.verticalLayout_3.addWidget(self.candidate_button)

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

        self.agency_list = QListWidget(self.layoutWidget1)
        self.agency_list.setObjectName(u"agency_list")

        self.verticalLayout_4.addWidget(self.agency_list)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.position_name_input = QLineEdit(self.layoutWidget1)
        self.position_name_input.setObjectName(u"position_name_input")

        self.horizontalLayout_12.addWidget(self.position_name_input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.num_openings_input = QLineEdit(self.layoutWidget1)
        self.num_openings_input.setObjectName(u"num_openings_input")

        self.horizontalLayout_13.addWidget(self.num_openings_input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.recruiter_dropdown = QComboBox(self.layoutWidget1)
        self.recruiter_dropdown.setObjectName(u"recruiter_dropdown")

        self.horizontalLayout_14.addWidget(self.recruiter_dropdown)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.position_button = QPushButton(self.layoutWidget1)
        self.position_button.setObjectName(u"position_button")
        self.position_button.setFont(font)

        self.verticalLayout_6.addWidget(self.position_button)


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

        self.recruiter_first_name_input = QLineEdit(self.layoutWidget_3)
        self.recruiter_first_name_input.setObjectName(u"recruiter_first_name_input")

        self.horizontalLayout_10.addWidget(self.recruiter_first_name_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.recruiter_last_name_input = QLineEdit(self.layoutWidget_3)
        self.recruiter_last_name_input.setObjectName(u"recruiter_last_name_input")

        self.horizontalLayout_11.addWidget(self.recruiter_last_name_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.recruiter_button = QPushButton(self.layoutWidget_3)
        self.recruiter_button.setObjectName(u"recruiter_button")
        self.recruiter_button.setFont(font)

        self.verticalLayout_5.addWidget(self.recruiter_button)

        self.event_label = QLabel(self.frame)
        self.event_label.setObjectName(u"event_label")
        self.event_label.setGeometry(QRect(1, 439, 361, 61))
        self.event_label.setFont(font)
        self.event_label.setAlignment(Qt.AlignCenter)
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
        self.agency_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.first_name_label.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.number_label.setText(QCoreApplication.translate("MainWindow", u"Phone Number: ", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"E-mail: ", None))
        self.candidate_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Agency List", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Position Name:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Number of Openings:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Recruiter ", None))
        self.position_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Agency", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Candidate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add Req", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Add Recruiter", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.recruiter_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.event_label.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

