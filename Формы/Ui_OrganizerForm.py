# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrganizerForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OrganizerForm(object):
    def setupUi(self, OrganizerForm):
        OrganizerForm.setObjectName("OrganizerForm")
        OrganizerForm.resize(800, 435)
        self.centralwidget = QtWidgets.QWidget(OrganizerForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.left_panel = QtWidgets.QGridLayout()
        self.left_panel.setObjectName("left_panel")
        self.pb_create = QtWidgets.QPushButton(self.centralwidget)
        self.pb_create.setObjectName("pb_create")
        self.left_panel.addWidget(self.pb_create, 0, 1, 1, 1)
        self.lbl_all_records = QtWidgets.QLabel(self.centralwidget)
        self.lbl_all_records.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_all_records.setObjectName("lbl_all_records")
        self.left_panel.addWidget(self.lbl_all_records, 0, 0, 1, 1)
        self.tw_records = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_records.setEnabled(True)
        self.tw_records.setObjectName("tw_records")
        self.tw_records.setColumnCount(0)
        self.tw_records.setRowCount(0)
        self.tw_records.horizontalHeader().setVisible(False)
        self.left_panel.addWidget(self.tw_records, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.left_panel, 0, 0, 3, 1)
        self.record = QtWidgets.QGridLayout()
        self.record.setObjectName("record")
        self.gridLayout.addLayout(self.record, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        OrganizerForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OrganizerForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.filters = QtWidgets.QMenu(self.menubar)
        self.filters.setObjectName("filters")
        OrganizerForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OrganizerForm)
        self.statusbar.setObjectName("statusbar")
        OrganizerForm.setStatusBar(self.statusbar)
        self.filter_all = QtWidgets.QAction(OrganizerForm)
        self.filter_all.setObjectName("filter_all")
        self.filter_reminders = QtWidgets.QAction(OrganizerForm)
        self.filter_reminders.setObjectName("filter_reminders")
        self.filter_tasks = QtWidgets.QAction(OrganizerForm)
        self.filter_tasks.setObjectName("filter_tasks")
        self.filter_notes = QtWidgets.QAction(OrganizerForm)
        self.filter_notes.setObjectName("filter_notes")
        self.filters.addAction(self.filter_all)
        self.filters.addAction(self.filter_reminders)
        self.filters.addAction(self.filter_tasks)
        self.filters.addAction(self.filter_notes)
        self.menubar.addAction(self.filters.menuAction())

        self.retranslateUi(OrganizerForm)
        QtCore.QMetaObject.connectSlotsByName(OrganizerForm)

    def retranslateUi(self, OrganizerForm):
        _translate = QtCore.QCoreApplication.translate
        OrganizerForm.setWindowTitle(_translate("OrganizerForm", "Органайзер"))
        self.pb_create.setText(_translate("OrganizerForm", "Создать"))
        self.lbl_all_records.setText(_translate("OrganizerForm", "Все записи"))
        self.filters.setTitle(_translate("OrganizerForm", "Записи"))
        self.filter_all.setText(_translate("OrganizerForm", "Все записи"))
        self.filter_reminders.setText(_translate("OrganizerForm", "Напоминания"))
        self.filter_tasks.setText(_translate("OrganizerForm", "Задачи"))
        self.filter_notes.setText(_translate("OrganizerForm", "Заметки"))
