import random
import sqlite3
import sys
from datetime import datetime
from win10toast import ToastNotifier

from PyQt5 import QtCore, QtMultimedia, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QTableWidgetItem

from DataBaseWork import DataBaseWork
from Edit_note_form import EditNoteForm
from Edit_reminder_form import EditReminderForm
from Edit_task_form import EditTaskForm
from Play_Sounds import PlaySounds
from Record_type import RecordType
from View_note_form import ViewNoteForm
from View_reminder_form import ViewReminderForm
from View_task_form import ViewTaskForm
from Формы.Ui_OrganizerForm import Ui_OrganizerForm


class OrganizerForm(QMainWindow, Ui_OrganizerForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pictures = ['6-4.ico', 'biohazard.ico', 'cheetah.ico', 'food.ico', 'marvin.ico',
                         'parrot.ico', 'space.ico', 'space_cat.ico', 'unicorn.ico', 'viper.ico']
        self.record_types = ['Заметка', 'Напоминание', 'Задача']
        self.timers = {'Reminders': {}, 'Tasks': {}}
        self.filter = False
        self.database = DataBaseWork()
        self.form = EditNoteForm()
        self.sounds = PlaySounds()

        self.update_records()

        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QtGui.QIcon('значки окон/organizer.png'))

        self.pb_create.clicked.connect(self.create_record)

        self.tw_records.doubleClicked.connect(self.open_record)

        self.filter_all.triggered.connect(self.change_filter)
        self.filter_notes.triggered.connect(self.change_filter)
        self.filter_reminders.triggered.connect(self.change_filter)
        self.filter_tasks.triggered.connect(self.change_filter)

    def open_record(self):
        self.form.close()

        id = self.tw_records.currentItem().row()
        record_type = self.tw_records.item(id, 0).text()
        title = self.tw_records.item(id, 1).text()

        if record_type == self.record_types[0]:
            record_type = RecordType.NOTE.value
            self.form = ViewNoteForm()
        elif record_type == self.record_types[1]:
            record_type = RecordType.REMINDER.value
            self.form = ViewReminderForm()
        elif record_type == self.record_types[2]:
            record_type = RecordType.TASK.value
            self.form = ViewTaskForm()

        id = self.database.get_id(record_type, title)

        self.show_record(id, record_type)

    def create_record(self):
        record_type, btn_pressed = QInputDialog.getItem(self, " ", 'Выберите тип записи', self.record_types, 1, False)

        if btn_pressed:
            if not self.record.isEmpty():
                self.form.close()

            if record_type == self.record_types[0]:
                self.form = EditNoteForm()
            elif record_type == self.record_types[1]:
                self.form = EditReminderForm()
            elif record_type == self.record_types[2]:
                self.form = EditTaskForm()

            self.form.closed.connect(self.show_record)
            self.record.addWidget(self.form, 0, 0)

    def edit_record(self, id, record_type):
        if record_type == RecordType.NOTE:
            self.form = EditNoteForm()
        elif record_type == RecordType.REMINDER:
            self.form = EditReminderForm()
        elif record_type == RecordType.TASK:
            self.form = EditTaskForm()

        self.form.closed.connect(self.show_record)
        self.record.addWidget(self.form, 0, 0)
        self.form.load_record(id, record_type.value)

    def delete_record(self, id, record_type):
        self.database.delete_record(id, record_type)

        if record_type != RecordType.NOTE.value and id in self.timers[record_type]:
            self.timers[record_type][id].stop()
            self.timers[record_type][id].deleteLater()

        self.update_records()

    def update_records(self):
        self.form.close()
        con = sqlite3.connect("Records.db")
        cur = con.cursor()

        notes = []
        reminders = []
        tasks = []

        if not self.filter or self.filter == RecordType.NOTE.value:
            notes = self.database.get_records_by_type(RecordType.NOTE.value)

        if not self.filter or self.filter == RecordType.REMINDER.value:
            reminders = self.database.get_records_by_type(RecordType.REMINDER.value)

        if not self.filter or self.filter == RecordType.TASK.value:
            tasks = self.database.get_records_by_type(RecordType.TASK.value)

        records = notes + reminders + tasks

        self.tw_records.setRowCount(0)
        self.tw_records.setColumnCount(3)

        for i in range(len(records)):
            if records[i] in notes:
                record_type = self.record_types[0]
            elif records[i] in reminders:
                record_type = self.record_types[1]
                self.create_update_timer(records[i], RecordType.REMINDER.value)
            elif records[i] in tasks:
                record_type = self.record_types[2]
                self.create_update_timer(records[i], RecordType.TASK.value)

            if records[i] != []:
                self.tw_records.insertRow(i)
                self.tw_records.setItem(i, 0, QTableWidgetItem(record_type))
                self.tw_records.setItem(i, 1, QTableWidgetItem(str(records[i][1])))
                self.tw_records.setItem(i, 2, QTableWidgetItem(str(records[i][2])))

    def change_filter(self):
        if self.sender() == self.filter_all:
            self.filter = False
        elif self.sender() == self.filter_notes:
            self.filter = RecordType.NOTE.value
        elif self.sender() == self.filter_reminders:
            self.filter = RecordType.REMINDER.value
        elif self.sender() == self.filter_tasks:
            self.filter = RecordType.TASK.value

        self.update_records()

    def create_update_timer(self, record, record_type):
        set_date_time = datetime.strptime(record[5], '%Y-%m-%d %H:%M:%S')

        if int((set_date_time - datetime.now()).total_seconds()) >= 0:

            add_date_time = datetime.now()
            seconds = int(str(int((set_date_time - add_date_time).total_seconds())) + '000')

            if record[0] in self.timers[record_type]:
                timer = self.timers[record_type][record[0]]
                timer.stop()

            timer = QTimer()
            timer.timeout.connect(lambda: self.send_notification(record_type, record[1], record[2]))
            timer.setSingleShot(True)
            timer.start(seconds)
            self.timers[record_type].update({record[0]: timer})

    def show_record(self, id, record_type):
        self.update_records()

        if record_type == RecordType.NOTE.value:
            self.form = ViewNoteForm()
        elif record_type == RecordType.REMINDER.value:
            self.form = ViewReminderForm()
        elif record_type == RecordType.TASK.value:
            self.form = ViewTaskForm()

        self.record.addWidget(self.form, 0, 0)
        self.form.load_record(id, record_type)

        self.form.delete_record.connect(self.delete_record)
        self.form.edit_record.connect(self.edit_record)

    def send_notification(self, record_type, title, topic):
        toaster = ToastNotifier()

        icon = 'картинки ico/' + random.choice(self.pictures)
        
        if record_type == RecordType.REMINDER.value:
            self.sounds.remind.play()

            toaster.show_toast(topic, title, threaded=True,
                               icon_path=icon, duration=5)
         
        elif record_type == RecordType.TASK.value:
            self.sounds.fail.play()

            toaster.show_toast('Внимание', f'Время на выполнение задния {title} истекло', threaded=True,
                               icon_path=icon, duration=5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = OrganizerForm()
    wnd.show()
    sys.exit(app.exec())
