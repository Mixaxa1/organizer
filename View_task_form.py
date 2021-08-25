import sqlite3
import sys

from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGroupBox, QVBoxLayout, QMessageBox

from Record_type import RecordType
from Play_Sounds import PlaySounds
from View_reminder_form import ViewReminderForm


class ViewTaskForm(ViewReminderForm):
    def __init__(self):
        super().__init__()

        self.record_type = RecordType.TASK

        self.points = {}
        self.completed = False
        self.sounds = PlaySounds()

    def init_ui(self):
        super().init_ui()

        self.setWindowTitle('Просмотр задачи')

        self.pb_complete = QPushButton('Завершить')
        self.pb_complete.clicked.connect(self.congratulation)
        self.main_info.insertWidget(3, self.pb_complete)

        self.points_group = QGroupBox("Пункты")
        self.main_info.insertWidget(3, self.points_group)

        self.tasks = QVBoxLayout()
        self.points_group.setLayout(self.tasks)

    def load_record(self, id, record_type):
        super().load_record(id, record_type)

        self.points_info = self.database.get_points(id)

        for point in self.points_info:
            text = str(point[2])
            check_box = QCheckBox(text)

            if point[3]:
                check_box.toggle()

            check_box.toggled.connect(self.change_flag)

            self.points.update({check_box: point[0]})
            self.tasks.insertWidget(-1, check_box)

        self.completed = self.record[6]
        if self.completed:
            self.complete_task()

        self.check_flags()

    def change_flag(self):
        check_box = self.sender()

        self.database.update_point_state(check_box.isChecked(), self.points[check_box])

        self.check_flags()

    def check_flags(self):
        flags = [check_box.isChecked() for check_box in self.points.keys()]
        if all(flags):
            self.pb_complete.setEnabled(True)
        else:
            self.pb_complete.setEnabled(False)

    def congratulation(self):
        self.sounds.success.play()

        QMessageBox.about(self, 'Юху', 'Поздравляю вы успешно выполнили задачу')

        self.complete_task()

    def complete_task(self):
        self.completed = True

        self.pb_complete.deleteLater()
        self.pb_edit.deleteLater()

        for check_box in self.points.keys():
            check_box.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = ViewTaskForm()
    wnd.show()
    sys.exit(app.exec())
