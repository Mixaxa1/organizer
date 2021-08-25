import sqlite3
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from DataBaseWork import DataBaseWork
from Record_type import RecordType
from Формы.Ui_ViewNoteForm import Ui_ViewNoteForm


class ViewNoteForm(QWidget, Ui_ViewNoteForm):
    COMMANDS = ['edit', 'delete']
    delete_record = pyqtSignal(int, str)
    edit_record = pyqtSignal(int, RecordType)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.record_type = RecordType.NOTE
        self.database = DataBaseWork()

        self.init_ui()

    def init_ui(self):
        self.pb_close.setIcon(QIcon('значки\close.png'))
        self.pb_close.clicked.connect(self.close)

        self.pb_delete.setIcon(QIcon('значки\delete.png'))
        self.pb_delete.clicked.connect(lambda: self.edit_or_delete(self.record_type))

        self.pb_edit.setIcon(QIcon('значки\edit.png'))
        self.pb_edit.clicked.connect(lambda: self.edit_or_delete(self.record_type))

    def load_record(self, id, record_type):
        self.record = self.database.get_record(record_type, id)

        self.id = id

        self.title = self.record[1]

        self.lbl_title.setText(self.record[1])
        self.lbl_topic.setText(self.record[2])
        self.lbl_description.setText(self.record[3])
        self.lbl_create_date_time_text.setText(self.record[4][:10] + ' в ' + self.record[4][11:])

    def edit_or_delete(self, record_type):
        if self.sender().objectName()[3:] == self.COMMANDS[0]:
            self.edit_record.emit(self.id, record_type)
        elif self.sender().objectName()[3:] == self.COMMANDS[1]:
            self.delete_record.emit(self.id, record_type.value)

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ViewNoteForm()
    wnd.show()
    sys.exit(app.exec())
