# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewTaskForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewTaskForm(object):
    def setupUi(self, ViewTaskForm):
        ViewTaskForm.setObjectName("ViewTaskForm")
        ViewTaskForm.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(ViewTaskForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_title = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout_2.addWidget(self.lbl_title, 1, 0, 1, 1)
        self.pb_delete = QtWidgets.QPushButton(ViewTaskForm)
        self.pb_delete.setText("")
        self.pb_delete.setObjectName("pb_delete")
        self.gridLayout_2.addWidget(self.pb_delete, 0, 3, 1, 1)
        self.lbl_set_time = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_set_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_set_time.setObjectName("lbl_set_time")
        self.gridLayout_2.addWidget(self.lbl_set_time, 1, 2, 1, 3)
        self.pb_close = QtWidgets.QPushButton(ViewTaskForm)
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")
        self.gridLayout_2.addWidget(self.pb_close, 0, 4, 1, 1)
        self.lbl_type_record = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_type_record.setObjectName("lbl_type_record")
        self.gridLayout_2.addWidget(self.lbl_type_record, 0, 0, 1, 1)
        self.lbl_set_time_2 = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_set_time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set_time_2.setObjectName("lbl_set_time_2")
        self.gridLayout_2.addWidget(self.lbl_set_time_2, 3, 2, 1, 3)
        self.lbl_set_day = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_set_day.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set_day.setObjectName("lbl_set_day")
        self.gridLayout_2.addWidget(self.lbl_set_day, 2, 2, 1, 3)
        self.pb_edit = QtWidgets.QPushButton(ViewTaskForm)
        self.pb_edit.setText("")
        self.pb_edit.setObjectName("pb_edit")
        self.gridLayout_2.addWidget(self.pb_edit, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.lbl_time_left = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_time_left.setObjectName("lbl_time_left")
        self.gridLayout_2.addWidget(self.lbl_time_left, 4, 2, 1, 3)
        self.lbl_show_left_time = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_show_left_time.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_show_left_time.setObjectName("lbl_show_left_time")
        self.gridLayout_2.addWidget(self.lbl_show_left_time, 5, 2, 1, 3)
        self.lbl_topic = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_topic.setObjectName("lbl_topic")
        self.gridLayout_2.addWidget(self.lbl_topic, 2, 0, 1, 1)
        self.lbl_description = QtWidgets.QLabel(ViewTaskForm)
        self.lbl_description.setObjectName("lbl_description")
        self.gridLayout_2.addWidget(self.lbl_description, 3, 0, 1, 1)
        self.vl_paragraphs = QtWidgets.QVBoxLayout()
        self.vl_paragraphs.setObjectName("vl_paragraphs")
        self.gridLayout_2.addLayout(self.vl_paragraphs, 4, 0, 2, 1)

        self.retranslateUi(ViewTaskForm)
        QtCore.QMetaObject.connectSlotsByName(ViewTaskForm)

    def retranslateUi(self, ViewTaskForm):
        _translate = QtCore.QCoreApplication.translate
        ViewTaskForm.setWindowTitle(_translate("ViewTaskForm", "Просмотр задачи"))
        self.lbl_title.setText(_translate("ViewTaskForm", "Название"))
        self.lbl_set_time.setText(_translate("ViewTaskForm", "Заданная дата и время"))
        self.lbl_type_record.setText(_translate("ViewTaskForm", "Тип"))
        self.lbl_set_time_2.setText(_translate("ViewTaskForm", "Установленное время"))
        self.lbl_set_day.setText(_translate("ViewTaskForm", "Установленный день"))
        self.lbl_time_left.setText(_translate("ViewTaskForm", "Времени осталось"))
        self.lbl_show_left_time.setText(_translate("ViewTaskForm", "оставшееся время"))
        self.lbl_topic.setText(_translate("ViewTaskForm", "Тема"))
        self.lbl_description.setText(_translate("ViewTaskForm", "Описание"))
