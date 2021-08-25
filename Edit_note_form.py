from datetime import datetime
import sqlite3
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from DataBaseWork import DataBaseWork
from Record_type import RecordType
from Формы.Ui_EditNoteForm import Ui_EditNoteForm


class EditNoteForm(QWidget, Ui_EditNoteForm):
    closed = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.id = False
        self.database = DataBaseWork()
        self.record_type = RecordType.NOTE.value
        self.signal_date_time = ''
        self.points_le = False

        self.init_ui()

    def init_ui(self):
        self.pb_close.setIcon(QIcon('значки\close.png'))
        self.pb_close.clicked.connect(self.close)

        self.pb_save.setIcon(QIcon('значки\save.png'))
        self.pb_save.clicked.connect(self.save_record)

    def load_record(self, id, record_type):
        self.id = id

        self.record = self.database.get_record_info(record_type, id)

        self.old_title = self.record[1]

        self.le_title.setText(self.record[1])
        self.le_topic.setText(self.record[2])
        self.te_description.setText(self.record[3])

    def save_record(self):
        if self.record_type != RecordType.NOTE.value and not self.signal_date_time:
            QMessageBox.about(self, 'Ошибка', 'Для этой записи нужно указать дату и время')
        elif self.record_type == RecordType.TASK.value and (not self.points_le or self.points_le == []):
            QMessageBox.about(self, 'Ошибка', 'Для задачи необходимо указать её пункты')
        else:
            self.get_info()

            if self.id:
                self.save_edited()
            else:
                self.save_new()

    def save_edited(self):
        if not self.database.check_record(self.record_type, self.title) or self.title == self.old_title:
            self.database.save_edited_record(self.record_type, self.id, self.title,
                                             self.topic, self.description, self.signal_date_time)

            if self.record_type == RecordType.TASK.value:
                self.database.save_edited_points(self.id, self.points_le)

            self.send_signal_and_close(self.record_type)
        else:
            QMessageBox.about(self, 'Ошибка', 'Запись с таким же именем существует')

    def save_new(self):
        if not self.database.check_record(self.record_type, self.title):
            self.get_date_time()

            self.database.save_new_record(self.record_type, self.title, self.topic,
                                          self.description, self.add_date_time, self.signal_date_time)

            self.database.get_id(self.record_type, self.title)

            if self.record_type == RecordType.TASK.value:
                self.database.save_points(self.id, self.points_le)

            self.send_signal_and_close(self.record_type)
        else:
            QMessageBox.about(self, 'Ошибка', 'Запись с таким же именем существует')

    def send_signal_and_close(self, record_type):
        self.closed.emit(self.id,  record_type)
        self.close()

    def get_info(self):
        self.title = self.le_title.text()
        self.topic = self.le_topic.text()
        self.description = self.te_description.toPlainText()

    def get_date_time(self):
        self.add_date_time = datetime.now()
        self.add_date_time = self.add_date_time.strftime("%d:%m:%Y %H:%M")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = EditNoteForm()
    wnd.show()
    sys.exit(app.exec())