import sys, sqlite3
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMessageBox

from Edit_note_form import EditNoteForm
from Get_date_time import GetDateTimeForm
from Record_type import RecordType


class EditReminderForm(EditNoteForm):
    def __init__(self):
        super().__init__()

        self.record_type = RecordType.REMINDER.value
        self.signal_date_time = False

    def init_ui(self):
        super().init_ui()

        self.setWindowTitle('Редактирование напоминания')

        self.pb_set_date_time = QPushButton('Установить дату и время', self)
        self.time_info.insertWidget(0, self.pb_set_date_time)

        self.lbl_set_date_time_text = QLabel('Напоминание сработает')
        self.time_info.insertWidget(1, self.lbl_set_date_time_text)

        self.lbl_set_date_time = QLabel('')
        self.time_info.insertWidget(2, self.lbl_set_date_time)

        self.pb_set_date_time.clicked.connect(self.get_date_time_from_user)

    def load_record(self, id, record_type):
        super().load_record(id, record_type)

        self.signal_date_time = self.record[5]
        date, time = self.signal_date_time.split()
        date = date.split('-')[::-1]
        self.lbl_set_date_time.setText(':'.join(date) + ' в ' + time[:-3])

    def get_date_time_from_user(self):
        self.window = GetDateTimeForm()
        self.window.closed.connect(self.set_date_time)
        self.window.show()

    def set_date_time(self, date, time):
        self.signal_date_time = date + ' ' + time
        self.signal_date_time = datetime.strptime(self.signal_date_time, '%d:%m:%Y %H:%M')
        self.lbl_set_date_time.setText(date + ' в ' + time)

    def get_info(self):
        super().get_info()

        self.signal_date_time = self.lbl_set_date_time.text().split()
        self.signal_date_time = self.signal_date_time[0] + ' ' + self.signal_date_time[2]
        self.signal_date_time = datetime.strptime(self.signal_date_time, '%d:%m:%Y %H:%M')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = EditReminderForm()
    wnd.show()
    sys.exit(app.exec())