# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewNoteForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewNoteForm(object):
    def setupUi(self, ViewNoteForm):
        ViewNoteForm.setObjectName("ViewNoteForm")
        ViewNoteForm.resize(422, 300)
        self.gridLayout = QtWidgets.QGridLayout(ViewNoteForm)
        self.gridLayout.setObjectName("gridLayout")
        self.date_time_info = QtWidgets.QVBoxLayout()
        self.date_time_info.setObjectName("date_time_info")
        self.lbl_create_date_time_text = QtWidgets.QLabel(ViewNoteForm)
        self.lbl_create_date_time_text.setObjectName("lbl_create_date_time_text")
        self.date_time_info.addWidget(self.lbl_create_date_time_text)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.date_time_info.addItem(spacerItem)
        self.gridLayout.addLayout(self.date_time_info, 1, 2, 1, 1)
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setObjectName("buttons")
        self.pb_edit = QtWidgets.QPushButton(ViewNoteForm)
        self.pb_edit.setText("")
        self.pb_edit.setObjectName("pb_edit")
        self.buttons.addWidget(self.pb_edit)
        self.pb_delete = QtWidgets.QPushButton(ViewNoteForm)
        self.pb_delete.setText("")
        self.pb_delete.setObjectName("pb_delete")
        self.buttons.addWidget(self.pb_delete)
        self.pb_close = QtWidgets.QPushButton(ViewNoteForm)
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")
        self.buttons.addWidget(self.pb_close)
        self.gridLayout.addLayout(self.buttons, 0, 2, 1, 1)
        self.main_info = QtWidgets.QVBoxLayout()
        self.main_info.setObjectName("main_info")
        self.lbl_title = QtWidgets.QLabel(ViewNoteForm)
        self.lbl_title.setObjectName("lbl_title")
        self.main_info.addWidget(self.lbl_title)
        self.lbl_topic = QtWidgets.QLabel(ViewNoteForm)
        self.lbl_topic.setObjectName("lbl_topic")
        self.main_info.addWidget(self.lbl_topic)
        self.lbl_description = QtWidgets.QLabel(ViewNoteForm)
        self.lbl_description.setObjectName("lbl_description")
        self.main_info.addWidget(self.lbl_description)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_info.addItem(spacerItem1)
        self.gridLayout.addLayout(self.main_info, 0, 0, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)

        self.retranslateUi(ViewNoteForm)
        QtCore.QMetaObject.connectSlotsByName(ViewNoteForm)

    def retranslateUi(self, ViewNoteForm):
        _translate = QtCore.QCoreApplication.translate
        ViewNoteForm.setWindowTitle(_translate("ViewNoteForm", "Просмотр заметки"))
        self.lbl_create_date_time_text.setText(_translate("ViewNoteForm", "Создано:"))
        self.lbl_title.setText(_translate("ViewNoteForm", "Название"))
        self.lbl_topic.setText(_translate("ViewNoteForm", "Тема"))
        self.lbl_description.setText(_translate("ViewNoteForm", "Описание"))
