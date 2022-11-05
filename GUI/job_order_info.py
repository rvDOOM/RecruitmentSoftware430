# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_order_info.ui'
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
        MainWindow.resize(800, 577)
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.open_reqs_table = QTableWidget(self.centralwidget)
        if (self.open_reqs_table.columnCount() < 3):
            self.open_reqs_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(200, 200, 200));
        self.open_reqs_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(200, 200, 200));
        self.open_reqs_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.open_reqs_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.open_reqs_table.setObjectName(u"open_reqs_table")
        self.open_reqs_table.setGeometry(QRect(20, 290, 761, 201))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_reqs_table.sizePolicy().hasHeightForWidth())
        self.open_reqs_table.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.open_reqs_table.setFont(font)
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
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(670, 500, 111, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.toolButton_2.setFont(font1)
        self.toolButton_2.setCheckable(False)
        self.toolButton_2.setAutoRepeat(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 551))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.job_order_label = QLabel(self.frame)
        self.job_order_label.setObjectName(u"job_order_label")
        self.job_order_label.setGeometry(QRect(10, 20, 361, 45))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setUnderline(True)
        self.job_order_label.setFont(font2)
        self.job_order_label.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 80, 341, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.company_data = QLabel(self.gridLayoutWidget)
        self.company_data.setObjectName(u"company_data")
        self.company_data.setFont(font)

        self.horizontalLayout_4.addWidget(self.company_data)

        self.is_label_2 = QLabel(self.gridLayoutWidget)
        self.is_label_2.setObjectName(u"is_label_2")
        self.is_label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.is_label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.is_data = QLabel(self.gridLayoutWidget)
        self.is_data.setObjectName(u"is_data")
        self.is_data.setFont(font)

        self.horizontalLayout_5.addWidget(self.is_data)

        self.is_label = QLabel(self.gridLayoutWidget)
        self.is_label.setObjectName(u"is_label")
        self.is_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.is_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.rec_name_data = QLabel(self.gridLayoutWidget)
        self.rec_name_data.setObjectName(u"rec_name_data")
        self.rec_name_data.setFont(font)

        self.horizontalLayout_10.addWidget(self.rec_name_data)

        self.rec_name_label = QLabel(self.gridLayoutWidget)
        self.rec_name_label.setObjectName(u"rec_name_label")
        self.rec_name_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.rec_name_label)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.open_reqs_label = QLabel(self.frame)
        self.open_reqs_label.setObjectName(u"open_reqs_label")
        self.open_reqs_label.setGeometry(QRect(10, 230, 761, 45))
        self.open_reqs_label.setFont(font2)
        self.open_reqs_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.open_reqs_table.raise_()
        self.toolButton_2.raise_()
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.open_reqs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem1 = self.open_reqs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"# of Reqs", None));
        ___qtablewidgetitem2 = self.open_reqs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Recruiter", None));
#if QT_CONFIG(accessibility)
        self.open_reqs_table.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Get Req Info", None))
        self.job_order_label.setText(QCoreApplication.translate("MainWindow", u"Job Order Information", None))
        self.company_data.setText(QCoreApplication.translate("MainWindow", u"Company: ", None))
        self.is_label_2.setText(QCoreApplication.translate("MainWindow", u"Grant Associates", None))
        self.is_data.setText(QCoreApplication.translate("MainWindow", u"Industry Sector:", None))
        self.is_label.setText(QCoreApplication.translate("MainWindow", u"Software Engineering", None))
        self.rec_name_data.setText(QCoreApplication.translate("MainWindow", u"Recruiter: ", None))
        self.rec_name_label.setText(QCoreApplication.translate("MainWindow", u"Doe, John", None))
        self.open_reqs_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Open Reqs</span></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

