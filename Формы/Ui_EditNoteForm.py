# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditNoteForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditNoteForm(object):
    def setupUi(self, EditNoteForm):
        EditNoteForm.setObjectName("EditNoteForm")
        EditNoteForm.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(EditNoteForm)
        self.gridLayout.setObjectName("gridLayout")
        self.main_info = QtWidgets.QGridLayout()
        self.main_info.setObjectName("main_info")
        self.te_description = QtWidgets.QTextEdit(EditNoteForm)
        self.te_description.setPlaceholderText("")
        self.te_description.setObjectName("te_description")
        self.main_info.addWidget(self.te_description, 3, 0, 1, 1)
        self.le_topic = QtWidgets.QLineEdit(EditNoteForm)
        self.le_topic.setObjectName("le_topic")
        self.main_info.addWidget(self.le_topic, 1, 0, 1, 1)
        self.le_title = QtWidgets.QLineEdit(EditNoteForm)
        self.le_title.setObjectName("le_title")
        self.main_info.addWidget(self.le_title, 0, 0, 1, 1)
        self.tasks = QtWidgets.QVBoxLayout()
        self.tasks.setObjectName("tasks")
        self.main_info.addLayout(self.tasks, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.main_info, 0, 0, 2, 1)
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setObjectName("buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons.addItem(spacerItem)
        self.pb_save = QtWidgets.QPushButton(EditNoteForm)
        self.pb_save.setText("")
        self.pb_save.setObjectName("pb_save")
        self.buttons.addWidget(self.pb_save)
        self.pb_close = QtWidgets.QPushButton(EditNoteForm)
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")
        self.buttons.addWidget(self.pb_close)
        self.gridLayout.addLayout(self.buttons, 0, 2, 1, 1)
        self.time_info = QtWidgets.QVBoxLayout()
        self.time_info.setObjectName("time_info")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.time_info.addItem(spacerItem1)
        self.gridLayout.addLayout(self.time_info, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)

        self.retranslateUi(EditNoteForm)
        QtCore.QMetaObject.connectSlotsByName(EditNoteForm)

    def retranslateUi(self, EditNoteForm):
        _translate = QtCore.QCoreApplication.translate
        EditNoteForm.setWindowTitle(_translate("EditNoteForm", "Редактирование заметки"))
        self.te_description.setHtml(_translate("EditNoteForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Описание</p></body></html>"))
        self.le_topic.setText(_translate("EditNoteForm", "Тема"))
        self.le_title.setText(_translate("EditNoteForm", "Название"))
