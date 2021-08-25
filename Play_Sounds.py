from PyQt5 import QtCore, QtMultimedia


class PlaySounds:
    def __init__(self):
        self.remind = self.load_mp3('mp3/reminder.mp3')
        self.fail = self.load_mp3('mp3/task_fail.mp3')
        self.success = self.load_mp3('mp3/task_success.mp3')

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        return player