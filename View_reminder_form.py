import sys

from PyQt5.QtWidgets import QApplication, QLabel

from Record_type import RecordType
from View_note_form import ViewNoteForm


class ViewReminderForm(ViewNoteForm):
    def __init__(self):
        super().__init__()

        self.record_type = RecordType.REMINDER

    def init_ui(self):
        super().init_ui()

        self.setWindowTitle('Просмотр напоминания')

        self.lbl_set_date_time_text = QLabel('Напоминание на:')
        self.date_time_info.insertWidget(1, self.lbl_set_date_time_text)

        self.lbl_set_date_time = QLabel('Времени осталось')
        self.date_time_info.insertWidget(2, self.lbl_set_date_time)


    def load_record(self, id, record_type):
        super().load_record(id, record_type)

        self.signal_date_time = self.record[5]
        date, time = self.signal_date_time.split()
        date = date.split('-')[::-1]
        self.lbl_set_date_time.setText(':'.join(date) + ' в ' + time[:-3])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ViewReminderForm()
    wnd.show()
    sys.exit(app.exec())
