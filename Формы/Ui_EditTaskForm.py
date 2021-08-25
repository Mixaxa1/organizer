# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTaskForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditTaskForm(object):
    def setupUi(self, EditTaskForm):
        EditTaskForm.setObjectName("EditTaskForm")
        EditTaskForm.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(EditTaskForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_close = QtWidgets.QPushButton(EditTaskForm)
        self.pb_close.setText("")
        self.pb_close.setObjectName("pb_close")
        self.gridLayout_2.addWidget(self.pb_close, 0, 3, 1, 1)
        self.pb_set_date_time = QtWidgets.QPushButton(EditTaskForm)
        self.pb_set_date_time.setObjectName("pb_set_date_time")
        self.gridLayout_2.addWidget(self.pb_set_date_time, 1, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.pb_save = QtWidgets.QPushButton(EditTaskForm)
        self.pb_save.setText("")
        self.pb_save.setObjectName("pb_save")
        self.gridLayout_2.addWidget(self.pb_save, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        self.vl_paragraphs = QtWidgets.QVBoxLayout()
        self.vl_paragraphs.setObjectName("vl_paragraphs")
        self.gridLayout_2.addLayout(self.vl_paragraphs, 4, 0, 1, 1)
        self.gl_add_del_paragraph = QtWidgets.QGridLayout()
        self.gl_add_del_paragraph.setObjectName("gl_add_del_paragraph")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gl_add_del_paragraph.addItem(spacerItem2, 1, 0, 1, 1)
        self.pb_add_par = QtWidgets.QPushButton(EditTaskForm)
        self.pb_add_par.setObjectName("pb_add_par")
        self.gl_add_del_paragraph.addWidget(self.pb_add_par, 2, 0, 1, 1)
        self.pb_del_par = QtWidgets.QPushButton(EditTaskForm)
        self.pb_del_par.setObjectName("pb_del_par")
        self.gl_add_del_paragraph.addWidget(self.pb_del_par, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gl_add_del_paragraph.addItem(spacerItem3, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gl_add_del_paragraph, 3, 1, 1, 3)
        self.le_title = QtWidgets.QLineEdit(EditTaskForm)
        self.le_title.setObjectName("le_title")
        self.gridLayout_2.addWidget(self.le_title, 0, 0, 1, 1)
        self.le_topic = QtWidgets.QLineEdit(EditTaskForm)
        self.le_topic.setObjectName("le_topic")
        self.gridLayout_2.addWidget(self.le_topic, 1, 0, 1, 1)
        self.le_description = QtWidgets.QTextEdit(EditTaskForm)
        self.le_description.setObjectName("le_description")
        self.gridLayout_2.addWidget(self.le_description, 2, 0, 2, 1)
        self.lbl_set_date_time = QtWidgets.QLabel(EditTaskForm)
        self.lbl_set_date_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set_date_time.setObjectName("lbl_set_date_time")
        self.gridLayout_2.addWidget(self.lbl_set_date_time, 2, 1, 1, 3)

        self.retranslateUi(EditTaskForm)
        QtCore.QMetaObject.connectSlotsByName(EditTaskForm)

    def retranslateUi(self, EditTaskForm):
        _translate = QtCore.QCoreApplication.translate
        EditTaskForm.setWindowTitle(_translate("EditTaskForm", "Редактирование задачи"))
        self.pb_set_date_time.setText(_translate("EditTaskForm", "Установить дату и время"))
        self.pb_add_par.setText(_translate("EditTaskForm", "Добавить пункт"))
        self.pb_del_par.setText(_translate("EditTaskForm", "Удалить пункт"))
        self.le_title.setText(_translate("EditTaskForm", "Название"))
        self.le_topic.setText(_translate("EditTaskForm", "Тема"))
        self.le_description.setHtml(_translate("EditTaskForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Описание</p></body></html>"))
        self.lbl_set_date_time.setText(_translate("EditTaskForm", "Дата и время"))
