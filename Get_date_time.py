import sys
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from Формы.Ui_GetDateTimeForm import Ui_GetDateTimeForm


class GetDateTimeForm(QWidget, Ui_GetDateTimeForm):
    closed = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QtGui.QIcon('значки окон/datetime.png'))

        self.pb_done.clicked.connect(self.get_date_time)

    def get_date_time(self):
        date = self.cw_date.selectedDate().toString('dd:MM:yyyy')
        time = self.te_time.time().toString('hh:mm')
        date_time = datetime.strptime(date + ' ' + time, '%d:%m:%Y %H:%M')
        now_date_time = datetime.now()
        seconds = (date_time - now_date_time).total_seconds()
        if seconds > 0:
            self.closed.emit(date, time)
            self.close()
        else:
            QMessageBox.about(self, 'Ошибка', 'Нельзя отправлять уведомления себе в прошлое, '
                                              'это может породить временной парадокс')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GetDateTimeForm()
    wnd.show()
    sys.exit(app.exec())
