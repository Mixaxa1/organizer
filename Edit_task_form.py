import sqlite3
import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QLineEdit

from Edit_reminder_form import EditReminderForm
from Record_type import RecordType


class EditTaskForm(EditReminderForm):
    def __init__(self):
        super().__init__()

        self.record_type = RecordType.TASK.value
        self.points_le = []

    def init_ui(self):
        super().init_ui()

        self.setWindowTitle('Редактирование задачи')

        self.pb_add_check_box = QPushButton('Добавить пункт')
        self.time_info.insertWidget(0, self.pb_add_check_box)
        self.pb_add_check_box.clicked.connect(self.add_point)

        self.pb_del_check_box = QPushButton('Удалить пункт')
        self.time_info.insertWidget(1, self.pb_del_check_box)
        self.pb_del_check_box.clicked.connect(self.del_point)

    def load_record(self, id, record_type):
        super().load_record(id, record_type)

        self.points = self.record[6]

        self.load_points(id)

    def add_point(self):
        new = QLineEdit('Новый пункт')
        self.points_le.append([new, False])
        self.tasks.insertWidget(-1, self.points_le[-1][0])

    def del_point(self):
        if len(self.points_le) > 0:
            self.tasks.itemAt(len(self.points_le) - 1).widget().setParent(None)
            self.points_le.pop(-1)
        else:
            QMessageBox.about(self, 'Ошибка', 'Нечего удалять')

    def load_points(self, id):
        self.points = self.database.get_points(id)

        for i in range(len(self.points)):
            self.points[i] = [*self.points[i]]

            text = self.points[i][2]
            le_point = QLineEdit(text)

            self.points_le.append([le_point, self.points[i][0]])
            self.tasks.insertWidget(-1, le_point)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = EditTaskForm()
    wnd.show()
    sys.exit(app.exec())
