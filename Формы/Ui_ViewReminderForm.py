# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewReminderForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewReminderForm(object):
    def setupUi(self, ViewReminderForm):
        ViewReminderForm.setObjectName("ViewReminderForm")
        ViewReminderForm.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(ViewReminderForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_title = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout_2.addWidget(self.lbl_title, 1, 0, 1, 1)
        self.pb_delete = QtWidgets.QPushButton(ViewReminderForm)
        self.pb_delete.setText("")
        self.pb_delete.setObjectName("pb_delete")
        self.gridLayout_2.addWidget(self.pb_delete, 0, 3, 1, 1)
        self.lbl_set_date_time_text = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_set_date_time_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_date_time_text.setObjectName("lbl_set_date_time_text")
        self.gridLayout_2.addWidget(self.lbl_set_date_time_text, 1, 2, 1, 3)
        self.pb_close = QtWidgets.QPushButton(ViewReminderForm)
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")
        self.gridLayout_2.addWidget(self.pb_close, 0, 4, 1, 1)
        self.lbl_type_record = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_type_record.setObjectName("lbl_type_record")
        self.gridLayout_2.addWidget(self.lbl_type_record, 0, 0, 1, 1)
        self.lbl_set_time = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_set_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set_time.setObjectName("lbl_set_time")
        self.gridLayout_2.addWidget(self.lbl_set_time, 3, 2, 1, 3)
        self.lbl_set_date = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_set_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set_date.setObjectName("lbl_set_date")
        self.gridLayout_2.addWidget(self.lbl_set_date, 2, 2, 1, 3)
        self.pb_edit = QtWidgets.QPushButton(ViewReminderForm)
        self.pb_edit.setText("")
        self.pb_edit.setObjectName("pb_edit")
        self.gridLayout_2.addWidget(self.pb_edit, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.lbl_time_left_text = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_time_left_text.setObjectName("lbl_time_left_text")
        self.gridLayout_2.addWidget(self.lbl_time_left_text, 4, 2, 1, 3)
        self.lbl_time_left = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_time_left.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_time_left.setObjectName("lbl_time_left")
        self.gridLayout_2.addWidget(self.lbl_time_left, 5, 2, 1, 3)
        self.lbl_topic = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_topic.setObjectName("lbl_topic")
        self.gridLayout_2.addWidget(self.lbl_topic, 2, 0, 1, 1)
        self.lbl_description = QtWidgets.QLabel(ViewReminderForm)
        self.lbl_description.setObjectName("lbl_description")
        self.gridLayout_2.addWidget(self.lbl_description, 3, 0, 1, 1)

        self.retranslateUi(ViewReminderForm)
        QtCore.QMetaObject.connectSlotsByName(ViewReminderForm)

    def retranslateUi(self, ViewReminderForm):
        _translate = QtCore.QCoreApplication.translate
        ViewReminderForm.setWindowTitle(_translate("ViewReminderForm", "Просмотр напоминания"))
        self.lbl_title.setText(_translate("ViewReminderForm", "Название"))
        self.lbl_set_date_time_text.setText(_translate("ViewReminderForm", "Заданная дата и время"))
        self.lbl_type_record.setText(_translate("ViewReminderForm", "Тип"))
        self.lbl_set_time.setText(_translate("ViewReminderForm", "Установленное время"))
        self.lbl_set_date.setText(_translate("ViewReminderForm", "Установленный день"))
        self.lbl_time_left_text.setText(_translate("ViewReminderForm", "Времени осталось"))
        self.lbl_time_left.setText(_translate("ViewReminderForm", "оставшееся время"))
        self.lbl_topic.setText(_translate("ViewReminderForm", "Тема"))
        self.lbl_description.setText(_translate("ViewReminderForm", "Описание"))
