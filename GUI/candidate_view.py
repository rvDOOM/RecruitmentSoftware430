# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'candidate_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Candidates(object):
    def setupUi(self, Candidates):
        if not Candidates.objectName():
            Candidates.setObjectName(u"Candidates")
        Candidates.resize(808, 604)
        self.actionAdd = QAction(Candidates)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionView_Candidates = QAction(Candidates)
        self.actionView_Candidates.setObjectName(u"actionView_Candidates")
        self.centralwidget = QWidget(Candidates)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 791, 541))
        font = QFont()
        font.setUnderline(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_data = QListWidget(self.frame)
        QListWidgetItem(self.list_data)
        self.list_data.setObjectName(u"list_data")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setUnderline(False)
        self.list_data.setFont(font1)
        self.list_data.setSortingEnabled(True)

        self.gridLayout.addWidget(self.list_data, 1, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.number_data = QLabel(self.frame)
        self.number_data.setObjectName(u"number_data")
        self.number_data.setFont(font1)

        self.horizontalLayout_2.addWidget(self.number_data)

        self.number_label = QLabel(self.frame)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.number_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.address_data = QLabel(self.frame)
        self.address_data.setObjectName(u"address_data")
        self.address_data.setFont(font1)

        self.horizontalLayout.addWidget(self.address_data)

        self.address_label = QLabel(self.frame)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setFont(font1)

        self.horizontalLayout.addWidget(self.address_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.email_label = QLabel(self.frame)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.email_label)

        self.email_data = QLabel(self.frame)
        self.email_data.setObjectName(u"email_data")
        self.email_data.setFont(font1)

        self.horizontalLayout_3.addWidget(self.email_data)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.list_label = QLabel(self.frame)
        self.list_label.setObjectName(u"list_label")
        font2 = QFont()
        font2.setPointSize(28)
        font2.setUnderline(True)
        self.list_label.setFont(font2)
        self.list_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.list_label, 0, 0, 1, 1)

        self.get_info_button = QPushButton(self.frame)
        self.get_info_button.setObjectName(u"get_info_button")
        self.get_info_button.setFont(font1)

        self.gridLayout.addWidget(self.get_info_button, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.work_history_label = QLabel(self.frame)
        self.work_history_label.setObjectName(u"work_history_label")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setUnderline(True)
        self.work_history_label.setFont(font3)
        self.work_history_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.work_history_label)

        self.work_history_table = QTableWidget(self.frame)
        if (self.work_history_table.columnCount() < 2):
            self.work_history_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.work_history_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.work_history_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.work_history_table.rowCount() < 1):
            self.work_history_table.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.work_history_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.work_history_table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.work_history_table.setItem(0, 1, __qtablewidgetitem4)
        self.work_history_table.setObjectName(u"work_history_table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_history_table.sizePolicy().hasHeightForWidth())
        self.work_history_table.setSizePolicy(sizePolicy)
        self.work_history_table.setFont(font1)
#if QT_CONFIG(accessibility)
        self.work_history_table.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.work_history_table.setLayoutDirection(Qt.LeftToRight)
        self.work_history_table.setAutoFillBackground(False)
        self.work_history_table.horizontalHeader().setCascadingSectionResizes(False)
        self.work_history_table.horizontalHeader().setDefaultSectionSize(125)
        self.work_history_table.horizontalHeader().setStretchLastSection(True)
        self.work_history_table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.work_history_table)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)

        Candidates.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Candidates)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 19))
        self.menuAdd = QMenu(self.menubar)
        self.menuAdd.setObjectName(u"menuAdd")
        Candidates.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Candidates)
        self.statusbar.setObjectName(u"statusbar")
        Candidates.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAdd.menuAction())
        self.menuAdd.addAction(self.actionAdd)
        self.menuAdd.addAction(self.actionView_Candidates)

        self.retranslateUi(Candidates)

        QMetaObject.connectSlotsByName(Candidates)
    # setupUi

    def retranslateUi(self, Candidates):
        Candidates.setWindowTitle(QCoreApplication.translate("Candidates", u"MainWindow", None))
        self.actionAdd.setText(QCoreApplication.translate("Candidates", u"Add", None))
        self.actionView_Candidates.setText(QCoreApplication.translate("Candidates", u"View Candidates", None))

        __sortingEnabled = self.list_data.isSortingEnabled()
        self.list_data.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_data.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Candidates", u"Bob Ross", None));
        self.list_data.setSortingEnabled(__sortingEnabled)

        self.number_data.setText(QCoreApplication.translate("Candidates", u"Phone Number:", None))
        self.number_label.setText(QCoreApplication.translate("Candidates", u"(917) 885 -0987", None))
        self.address_data.setText(QCoreApplication.translate("Candidates", u"Address:", None))
        self.address_label.setText(QCoreApplication.translate("Candidates", u"23 Sunset Blvd.\n"
"NoWhere, SA, 11234", None))
        self.email_label.setText(QCoreApplication.translate("Candidates", u"E-mail:", None))
        self.email_data.setText(QCoreApplication.translate("Candidates", u"na@na.com", None))
        self.list_label.setText(QCoreApplication.translate("Candidates", u"Candidate List", None))
        self.get_info_button.setText(QCoreApplication.translate("Candidates", u"Get Candidate Info", None))
        self.work_history_label.setText(QCoreApplication.translate("Candidates", u"Work History", None))
        ___qtablewidgetitem = self.work_history_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Candidates", u"YOE", None));
        ___qtablewidgetitem1 = self.work_history_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Candidates", u"Company", None));
        ___qtablewidgetitem2 = self.work_history_table.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Candidates", u"New Row", None));

        __sortingEnabled1 = self.work_history_table.isSortingEnabled()
        self.work_history_table.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.work_history_table.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Candidates", u"5", None));
        ___qtablewidgetitem4 = self.work_history_table.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Candidates", u"Arch Industries", None));
        self.work_history_table.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(accessibility)
        self.work_history_table.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.menuAdd.setTitle(QCoreApplication.translate("Candidates", u"Menu", None))
    # retranslateUi

