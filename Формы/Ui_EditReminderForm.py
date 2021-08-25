# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditReminderForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditReminderForm(object):
    def setupUi(self, EditReminderForm):
        EditReminderForm.setObjectName("EditReminderForm")
        EditReminderForm.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(EditReminderForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.pb_save = QtWidgets.QPushButton(EditReminderForm)
        self.pb_save.setText("")
        self.pb_save.setObjectName("pb_save")
        self.gridLayout_2.addWidget(self.pb_save, 0, 2, 1, 1)
        self.pb_close = QtWidgets.QPushButton(EditReminderForm)
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")
        self.gridLayout_2.addWidget(self.pb_close, 0, 3, 1, 1)
        self.pb_set_date_time = QtWidgets.QPushButton(EditReminderForm)
        self.pb_set_date_time.setObjectName("pb_set_date_time")
        self.gridLayout_2.addWidget(self.pb_set_date_time, 1, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.le_title = QtWidgets.QLineEdit(EditReminderForm)
        self.le_title.setObjectName("le_title")
        self.gridLayout_2.addWidget(self.le_title, 0, 0, 1, 1)
        self.le_topic = QtWidgets.QLineEdit(EditReminderForm)
        self.le_topic.setObjectName("le_topic")
        self.gridLayout_2.addWidget(self.le_topic, 1, 0, 1, 1)
        self.le_description = QtWidgets.QTextEdit(EditReminderForm)
        self.le_description.setObjectName("le_description")
        self.gridLayout_2.addWidget(self.le_description, 2, 0, 2, 1)
        self.lbl_set_date_time = QtWidgets.QLabel(EditReminderForm)
        self.lbl_set_date_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set_date_time.setObjectName("lbl_set_date_time")
        self.gridLayout_2.addWidget(self.lbl_set_date_time, 2, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 2, 1, 1)

        self.retranslateUi(EditReminderForm)
        QtCore.QMetaObject.connectSlotsByName(EditReminderForm)

    def retranslateUi(self, EditReminderForm):
        _translate = QtCore.QCoreApplication.translate
        EditReminderForm.setWindowTitle(_translate("EditReminderForm", "Редактирование напоминания"))
        self.pb_set_date_time.setText(_translate("EditReminderForm", "Установить дату и время"))
        self.le_title.setText(_translate("EditReminderForm", "Название"))
        self.le_topic.setText(_translate("EditReminderForm", "Тема"))
        self.le_description.setHtml(_translate("EditReminderForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Описание</p></body></html>"))
        self.lbl_set_date_time.setText(_translate("EditReminderForm", "Дата и время"))
