# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetDateTimeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetDateTimeForm(object):
    def setupUi(self, GetDateTimeForm):
        GetDateTimeForm.setObjectName("GetDateTimeForm")
        GetDateTimeForm.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(GetDateTimeForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_message = QtWidgets.QLabel(GetDateTimeForm)
        self.lbl_message.setObjectName("lbl_message")
        self.verticalLayout.addWidget(self.lbl_message)
        self.cw_date = QtWidgets.QCalendarWidget(GetDateTimeForm)
        self.cw_date.setObjectName("cw_date")
        self.verticalLayout.addWidget(self.cw_date)
        self.te_time = QtWidgets.QTimeEdit(GetDateTimeForm)
        self.te_time.setObjectName("te_time")
        self.verticalLayout.addWidget(self.te_time)
        self.pb_done = QtWidgets.QPushButton(GetDateTimeForm)
        self.pb_done.setObjectName("pb_done")
        self.verticalLayout.addWidget(self.pb_done)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GetDateTimeForm)
        QtCore.QMetaObject.connectSlotsByName(GetDateTimeForm)

    def retranslateUi(self, GetDateTimeForm):
        _translate = QtCore.QCoreApplication.translate
        GetDateTimeForm.setWindowTitle(_translate("GetDateTimeForm", "Выбор даты и времени"))
        self.lbl_message.setText(_translate("GetDateTimeForm", "Выберите дату и время для напоминания"))
        self.pb_done.setText(_translate("GetDateTimeForm", "Ок"))
