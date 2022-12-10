# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'complete.ui'
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
        MainWindow.resize(919, 786)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(239, 239, 239, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(247, 247, 247, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(119, 119, 119, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(159, 159, 159, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_candidate_button = QPushButton(self.centralwidget)
        self.main_candidate_button.setObjectName(u"main_candidate_button")
        self.main_candidate_button.setGeometry(QRect(10, 150, 61, 61))
        self.new_button = QPushButton(self.centralwidget)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setGeometry(QRect(10, 10, 61, 61))
        self.company_button = QPushButton(self.centralwidget)
        self.company_button.setObjectName(u"company_button")
        self.company_button.setGeometry(QRect(10, 80, 61, 61))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(89, 19, 811, 711))
        self.Homepage = QWidget()
        self.Homepage.setObjectName(u"Homepage")
        self.stackedWidget.addWidget(self.Homepage)
        self.Addpage = QWidget()
        self.Addpage.setObjectName(u"Addpage")
        self.label_6 = QLabel(self.Addpage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 170, 101, 21))
        font = QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_19 = QLabel(self.Addpage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(410, 0, 121, 21))
        self.label_19.setFont(font)
        self.frame_4 = QFrame(self.Addpage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 200, 371, 201))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 351, 181))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.first_name_label = QLabel(self.layoutWidget_2)
        self.first_name_label.setObjectName(u"first_name_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.first_name_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.first_name_label)

        self.candidate_first_name_input = QLineEdit(self.layoutWidget_2)
        self.candidate_first_name_input.setObjectName(u"candidate_first_name_input")

        self.horizontalLayout_5.addWidget(self.candidate_first_name_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.last_name_label = QLabel(self.layoutWidget_2)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.last_name_label)

        self.candidate_last_name_input = QLineEdit(self.layoutWidget_2)
        self.candidate_last_name_input.setObjectName(u"candidate_last_name_input")

        self.horizontalLayout_6.addWidget(self.candidate_last_name_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.address_label = QLabel(self.layoutWidget_2)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.address_label)

        self.address_input = QLineEdit(self.layoutWidget_2)
        self.address_input.setObjectName(u"address_input")

        self.horizontalLayout_9.addWidget(self.address_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.number_label = QLabel(self.layoutWidget_2)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.number_label)

        self.number_input = QLineEdit(self.layoutWidget_2)
        self.number_input.setObjectName(u"number_input")

        self.horizontalLayout_7.addWidget(self.number_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.email_label = QLabel(self.layoutWidget_2)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.email_label)

        self.email_input = QLineEdit(self.layoutWidget_2)
        self.email_input.setObjectName(u"email_input")

        self.horizontalLayout_8.addWidget(self.email_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.candidate_button = QPushButton(self.layoutWidget_2)
        self.candidate_button.setObjectName(u"candidate_button")
        self.candidate_button.setFont(font1)

        self.verticalLayout_3.addWidget(self.candidate_button)

        self.frame_3 = QFrame(self.Addpage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 30, 371, 141))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 351, 119))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.agency_name_input = QLineEdit(self.layoutWidget)
        self.agency_name_input.setObjectName(u"agency_name_input")

        self.horizontalLayout.addWidget(self.agency_name_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.industry_sector_input = QLineEdit(self.layoutWidget)
        self.industry_sector_input.setObjectName(u"industry_sector_input")

        self.horizontalLayout_2.addWidget(self.industry_sector_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_25.addWidget(self.label_16)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_25.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_25)

        self.agency_button = QPushButton(self.layoutWidget)
        self.agency_button.setObjectName(u"agency_button")
        self.agency_button.setFont(font1)

        self.verticalLayout.addWidget(self.agency_button)

        self.label = QLabel(self.Addpage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 101, 21))
        self.label.setFont(font)
        self.frame_5 = QFrame(self.Addpage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(420, 210, 351, 481))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame_5)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(15, 10, 321, 451))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.agency_list = QListWidget(self.layoutWidget_4)
        self.agency_list.setObjectName(u"agency_list")

        self.verticalLayout_4.addWidget(self.agency_list)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_22 = QLabel(self.layoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.position_name_input = QLineEdit(self.layoutWidget_4)
        self.position_name_input.setObjectName(u"position_name_input")

        self.horizontalLayout_12.addWidget(self.position_name_input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.layoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.num_openings_input = QLineEdit(self.layoutWidget_4)
        self.num_openings_input.setObjectName(u"num_openings_input")

        self.horizontalLayout_13.addWidget(self.num_openings_input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.layoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.recruiter_dropdown = QComboBox(self.layoutWidget_4)
        self.recruiter_dropdown.setObjectName(u"recruiter_dropdown")

        self.horizontalLayout_14.addWidget(self.recruiter_dropdown)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.position_button = QPushButton(self.layoutWidget_4)
        self.position_button.setObjectName(u"position_button")
        self.position_button.setFont(font1)

        self.verticalLayout_6.addWidget(self.position_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.frame_9 = QFrame(self.Addpage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(410, 30, 351, 131))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame_9)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 10, 331, 111))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.recruiter_first_name_input = QLineEdit(self.layoutWidget_3)
        self.recruiter_first_name_input.setObjectName(u"recruiter_first_name_input")

        self.horizontalLayout_10.addWidget(self.recruiter_first_name_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.recruiter_last_name_input = QLineEdit(self.layoutWidget_3)
        self.recruiter_last_name_input.setObjectName(u"recruiter_last_name_input")

        self.horizontalLayout_11.addWidget(self.recruiter_last_name_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.recruiter_button = QPushButton(self.layoutWidget_3)
        self.recruiter_button.setObjectName(u"recruiter_button")
        self.recruiter_button.setFont(font1)

        self.verticalLayout_5.addWidget(self.recruiter_button)

        self.label_2 = QLabel(self.Addpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 170, 111, 21))
        self.label_2.setFont(font)
        self.label_9 = QLabel(self.Addpage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 0, 301, 20))
        self.label_10 = QLabel(self.Addpage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 170, 201, 20))
        self.label_11 = QLabel(self.Addpage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(540, 170, 301, 20))
        self.label_12 = QLabel(self.Addpage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(550, 0, 301, 20))
        self.frame_2 = QFrame(self.Addpage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 430, 371, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(90)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 351, 246))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.candidate_box = QComboBox(self.layoutWidget1)
        self.candidate_box.setObjectName(u"candidate_box")

        self.horizontalLayout_3.addWidget(self.candidate_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_15)

        self.company_box = QComboBox(self.layoutWidget1)
        self.company_box.setObjectName(u"company_box")

        self.horizontalLayout_17.addWidget(self.company_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_2 = QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.listWidget = QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_9.addWidget(self.listWidget)


        self.horizontalLayout_18.addLayout(self.verticalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget1)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_2.addWidget(self.dateTimeEdit)

        self.interview_button = QPushButton(self.layoutWidget1)
        self.interview_button.setObjectName(u"interview_button")

        self.verticalLayout_2.addWidget(self.interview_button)

        self.label_13 = QLabel(self.Addpage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 400, 121, 21))
        self.label_13.setFont(font)
        self.stackedWidget.addWidget(self.Addpage)
        self.Companypage = QWidget()
        self.Companypage.setObjectName(u"Companypage")
        self.job_order_label = QLabel(self.Companypage)
        self.job_order_label.setObjectName(u"job_order_label")
        self.job_order_label.setGeometry(QRect(10, 9, 759, 42))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setUnderline(True)
        self.job_order_label.setFont(font2)
        self.job_order_label.setAlignment(Qt.AlignCenter)
        self.open_reqs_table = QTableWidget(self.Companypage)
        if (self.open_reqs_table.columnCount() < 3):
            self.open_reqs_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.open_reqs_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        self.open_reqs_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.open_reqs_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.open_reqs_table.setObjectName(u"open_reqs_table")
        self.open_reqs_table.setGeometry(QRect(10, 382, 759, 156))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_reqs_table.sizePolicy().hasHeightForWidth())
        self.open_reqs_table.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setUnderline(False)
        self.open_reqs_table.setFont(font3)
#if QT_CONFIG(accessibility)
        self.open_reqs_table.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.open_reqs_table.setLayoutDirection(Qt.LeftToRight)
        self.open_reqs_table.setAutoFillBackground(False)
        self.open_reqs_table.setRowCount(0)
        self.open_reqs_table.horizontalHeader().setCascadingSectionResizes(False)
        self.open_reqs_table.horizontalHeader().setDefaultSectionSize(125)
        self.open_reqs_table.horizontalHeader().setStretchLastSection(True)
        self.open_reqs_table.verticalHeader().setVisible(False)
        self.open_reqs_label = QLabel(self.Companypage)
        self.open_reqs_label.setObjectName(u"open_reqs_label")
        self.open_reqs_label.setGeometry(QRect(10, 347, 759, 29))
        self.open_reqs_label.setFont(font2)
        self.open_reqs_label.setAlignment(Qt.AlignCenter)
        self.interview_table = QTableWidget(self.Companypage)
        if (self.interview_table.columnCount() < 4):
            self.interview_table.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.interview_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.interview_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.interview_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.interview_table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.interview_table.setObjectName(u"interview_table")
        self.interview_table.setGeometry(QRect(10, 185, 759, 156))
        self.interview_table.setFont(font1)
        self.interview_table.horizontalHeader().setDefaultSectionSize(180)
        self.interview_table.horizontalHeader().setStretchLastSection(True)
        self.interview_table.verticalHeader().setVisible(False)
        self.gridLayoutWidget = QWidget(self.Companypage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 57, 759, 87))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.is_data = QLabel(self.gridLayoutWidget)
        self.is_data.setObjectName(u"is_data")
        self.is_data.setFont(font3)

        self.horizontalLayout_15.addWidget(self.is_data)

        self.sector_label = QLabel(self.gridLayoutWidget)
        self.sector_label.setObjectName(u"sector_label")
        self.sector_label.setFont(font3)

        self.horizontalLayout_15.addWidget(self.sector_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.num_emp_label = QLabel(self.gridLayoutWidget)
        self.num_emp_label.setObjectName(u"num_emp_label")
        self.num_emp_label.setFont(font1)

        self.horizontalLayout_16.addWidget(self.num_emp_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(8)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setFont(font1)
        self.comboBox.setMinimumContentsLength(15)

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.view_button = QPushButton(self.gridLayoutWidget)
        self.view_button.setObjectName(u"view_button")
        self.view_button.setFont(font1)

        self.horizontalLayout_4.addWidget(self.view_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.open_reqs_label_2 = QLabel(self.Companypage)
        self.open_reqs_label_2.setObjectName(u"open_reqs_label_2")
        self.open_reqs_label_2.setGeometry(QRect(10, 150, 759, 29))
        self.open_reqs_label_2.setFont(font2)
        self.open_reqs_label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.Companypage)
        self.Candidatepage = QWidget()
        self.Candidatepage.setObjectName(u"Candidatepage")
        self.verticalLayout_7 = QVBoxLayout(self.Candidatepage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.Candidatepage)
        self.frame.setObjectName(u"frame")
        font4 = QFont()
        font4.setUnderline(True)
        self.frame.setFont(font4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.get_info_button = QPushButton(self.frame)
        self.get_info_button.setObjectName(u"get_info_button")
        self.get_info_button.setFont(font3)

        self.gridLayout.addWidget(self.get_info_button, 2, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.number_data_3 = QLabel(self.frame)
        self.number_data_3.setObjectName(u"number_data_3")
        self.number_data_3.setFont(font3)

        self.horizontalLayout_22.addWidget(self.number_data_3)

        self.number_label_4 = QLabel(self.frame)
        self.number_label_4.setObjectName(u"number_label_4")
        self.number_label_4.setFont(font3)

        self.horizontalLayout_22.addWidget(self.number_label_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.address_data_3 = QLabel(self.frame)
        self.address_data_3.setObjectName(u"address_data_3")
        self.address_data_3.setFont(font3)

        self.horizontalLayout_23.addWidget(self.address_data_3)

        self.address_label_4 = QLabel(self.frame)
        self.address_label_4.setObjectName(u"address_label_4")
        self.address_label_4.setFont(font3)

        self.horizontalLayout_23.addWidget(self.address_label_4)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_11)


        self.verticalLayout_11.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.email_label_4 = QLabel(self.frame)
        self.email_label_4.setObjectName(u"email_label_4")
        self.email_label_4.setFont(font3)

        self.horizontalLayout_24.addWidget(self.email_label_4)

        self.email_data_3 = QLabel(self.frame)
        self.email_data_3.setObjectName(u"email_data_3")
        self.email_data_3.setFont(font3)

        self.horizontalLayout_24.addWidget(self.email_data_3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_12)


        self.verticalLayout_11.addLayout(self.horizontalLayout_24)


        self.gridLayout.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        self.list_label = QLabel(self.frame)
        self.list_label.setObjectName(u"list_label")
        self.list_label.setFont(font2)
        self.list_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.list_label, 0, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.work_history_label_3 = QLabel(self.frame)
        self.work_history_label_3.setObjectName(u"work_history_label_3")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setUnderline(True)
        self.work_history_label_3.setFont(font5)
        self.work_history_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.work_history_label_3)

        self.work_history_table_3 = QTableWidget(self.frame)
        if (self.work_history_table_3.columnCount() < 2):
            self.work_history_table_3.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.work_history_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.work_history_table_3.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        if (self.work_history_table_3.rowCount() < 1):
            self.work_history_table_3.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.work_history_table_3.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.work_history_table_3.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.work_history_table_3.setItem(0, 1, __qtablewidgetitem11)
        self.work_history_table_3.setObjectName(u"work_history_table_3")
        sizePolicy1.setHeightForWidth(self.work_history_table_3.sizePolicy().hasHeightForWidth())
        self.work_history_table_3.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(9)
        font6.setUnderline(False)
        self.work_history_table_3.setFont(font6)
#if QT_CONFIG(accessibility)
        self.work_history_table_3.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.work_history_table_3.setLayoutDirection(Qt.LeftToRight)
        self.work_history_table_3.setAutoFillBackground(False)
        self.work_history_table_3.horizontalHeader().setCascadingSectionResizes(False)
        self.work_history_table_3.horizontalHeader().setDefaultSectionSize(125)
        self.work_history_table_3.horizontalHeader().setStretchLastSection(True)
        self.work_history_table_3.verticalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.work_history_table_3)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.list_data = QListWidget(self.frame)
        QListWidgetItem(self.list_data)
        self.list_data.setObjectName(u"list_data")
        self.list_data.setFont(font3)
        self.list_data.setSortingEnabled(True)

        self.gridLayout.addWidget(self.list_data, 1, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.work_history_label_4 = QLabel(self.frame)
        self.work_history_label_4.setObjectName(u"work_history_label_4")
        self.work_history_label_4.setFont(font5)
        self.work_history_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.work_history_label_4)

        self.interview_table2 = QTableWidget(self.frame)
        if (self.interview_table2.columnCount() < 4):
            self.interview_table2.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.interview_table2.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.interview_table2.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.interview_table2.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.interview_table2.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        if (self.interview_table2.rowCount() < 1):
            self.interview_table2.setRowCount(1)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.interview_table2.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.interview_table2.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.interview_table2.setItem(0, 1, __qtablewidgetitem18)
        self.interview_table2.setObjectName(u"interview_table2")
        sizePolicy1.setHeightForWidth(self.interview_table2.sizePolicy().hasHeightForWidth())
        self.interview_table2.setSizePolicy(sizePolicy1)
        self.interview_table2.setFont(font6)
#if QT_CONFIG(accessibility)
        self.interview_table2.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.interview_table2.setLayoutDirection(Qt.LeftToRight)
        self.interview_table2.setAutoFillBackground(False)
        self.interview_table2.horizontalHeader().setCascadingSectionResizes(False)
        self.interview_table2.horizontalHeader().setDefaultSectionSize(80)
        self.interview_table2.horizontalHeader().setStretchLastSection(True)
        self.interview_table2.verticalHeader().setVisible(False)

        self.verticalLayout_12.addWidget(self.interview_table2)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame)

        self.label_17 = QLabel(self.Candidatepage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_7.addWidget(self.label_17)

        self.label_18 = QLabel(self.Candidatepage)
        self.label_18.setObjectName(u"label_18")
        font7 = QFont()
        font7.setPointSize(8)
        self.label_18.setFont(font7)

        self.verticalLayout_7.addWidget(self.label_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.Candidatepage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_21)

        self.comboBox_2 = QComboBox(self.Candidatepage)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_19.addWidget(self.comboBox_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.Candidatepage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_25)

        self.lineEdit_2 = QLineEdit(self.Candidatepage)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_20.addWidget(self.lineEdit_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.pushButton = QPushButton(self.Candidatepage)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.Candidatepage)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_21 = QHBoxLayout(self.widget1)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_13 = QVBoxLayout(self.widget2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 919, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_candidate_button.setText(QCoreApplication.translate("MainWindow", u"Candidate\n"
"Dir.", None))
        self.new_button.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.company_button.setText(QCoreApplication.translate("MainWindow", u"Company\n"
"Info", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add Req", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Add Recruiter", None))
        self.first_name_label.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.number_label.setText(QCoreApplication.translate("MainWindow", u"Phone Number: ", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"E-mail: ", None))
        self.candidate_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Company Name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Industry Sector:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Number of Employees: ", None))
        self.agency_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add Company", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Company List", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Position Name:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Number of Openings:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Recruiter ", None))
        self.position_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.recruiter_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Candidate", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Candidate: ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Company:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Get Open Reqs", None))
        self.interview_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"New Interview", None))
        self.job_order_label.setText(QCoreApplication.translate("MainWindow", u"Company Information", None))
        ___qtablewidgetitem = self.open_reqs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem1 = self.open_reqs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"# of Reqs", None));
        ___qtablewidgetitem2 = self.open_reqs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Recruiter", None));
#if QT_CONFIG(accessibility)
        self.open_reqs_table.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.open_reqs_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Open Reqs</span></p></body></html>", None))
        ___qtablewidgetitem3 = self.interview_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem4 = self.interview_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem5 = self.interview_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Candidate", None));
        ___qtablewidgetitem6 = self.interview_table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        self.is_data.setText(QCoreApplication.translate("MainWindow", u"Industry Sector:", None))
        self.sector_label.setText(QCoreApplication.translate("MainWindow", u"Software Engineering", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Number Of Employees: ", None))
        self.num_emp_label.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.view_button.setText(QCoreApplication.translate("MainWindow", u"View Company", None))
        self.open_reqs_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Scheduled Interviews</span></p></body></html>", None))
        self.get_info_button.setText(QCoreApplication.translate("MainWindow", u"Get Candidate Info", None))
        self.number_data_3.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.number_label_4.setText(QCoreApplication.translate("MainWindow", u"(917) 885 -0987", None))
        self.address_data_3.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.address_label_4.setText(QCoreApplication.translate("MainWindow", u"23 Sunset Blvd.\n"
"NoWhere, SA, 11234", None))
        self.email_label_4.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.email_data_3.setText(QCoreApplication.translate("MainWindow", u"na@na.com", None))
        self.list_label.setText(QCoreApplication.translate("MainWindow", u"Candidate List", None))
        self.work_history_label_3.setText(QCoreApplication.translate("MainWindow", u"Work History", None))
        ___qtablewidgetitem7 = self.work_history_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"YOE", None));
        ___qtablewidgetitem8 = self.work_history_table_3.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem9 = self.work_history_table_3.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.work_history_table_3.isSortingEnabled()
        self.work_history_table_3.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.work_history_table_3.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem11 = self.work_history_table_3.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Arch Industries", None));
        self.work_history_table_3.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(accessibility)
        self.work_history_table_3.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)

        __sortingEnabled1 = self.list_data.isSortingEnabled()
        self.list_data.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_data.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Bob Ross", None));
        self.list_data.setSortingEnabled(__sortingEnabled1)

        self.work_history_label_4.setText(QCoreApplication.translate("MainWindow", u"Interviews", None))
        ___qtablewidgetitem12 = self.interview_table2.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem13 = self.interview_table2.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem14 = self.interview_table2.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem15 = self.interview_table2.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem16 = self.interview_table2.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.interview_table2.isSortingEnabled()
        self.interview_table2.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.interview_table2.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem18 = self.interview_table2.item(0, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Arch Industries", None));
        self.interview_table2.setSortingEnabled(__sortingEnabled2)

#if QT_CONFIG(accessibility)
        self.interview_table2.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Add Work History", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"* Highlight candidate's name from the list above", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Company:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Years of Experience: ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

