# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt5.QtCore import QThread, QTime, QTimer, pyqtSignal, Qt
#
#
# class TimeUpdater(QThread):
#     time_signal = pyqtSignal(str)
#
#     def run(self):
#         timer = QTimer()
#         timer.timeout.connect(self.emit_time)
#         timer.start(1000)
#         self.exec_()
#
#     def emit_time(self):
#         current_time = QTime.currentTime().toString("HH:mm:ss")
#         self.time_signal.emit(current_time)
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Hozirgi vaqt")
#         self.setGeometry(200, 200, 300, 100)
#
#         self.time_label = QLabel("Hozirgi vaqt:", self)
#         self.time_label.setAlignment(Qt.AlignCenter)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.time_label)
#         self.setLayout(layout)
#
#         self.time_updater = TimeUpdater()
#         self.time_updater.time_signal.connect(self.update_time)
#         self.time_updater.start()
#
#     def update_time(self, current_time):
#         self.time_label.setText(f"Hozirgi vaqt: {current_time}")
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
# from PyQt5.QtCore import QThread, pyqtSignal, Qt
# import time
#
# class ProgressThread(QThread):
#     progress_signal = pyqtSignal(int)
#
#     def run(self):
#         for i in range(101):
#             self.progress_signal.emit(i)
#             time.sleep(0.05)
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Progress Bar Example")
#         self.setGeometry(300, 300, 400, 200)
#
#         self.progressBar = QProgressBar(self)
#         self.progressBar.setAlignment(Qt.AlignCenter)
#         self.progressBar.setValue(0)
#
#         self.startButton = QPushButton("Ishni boshlash", self)
#         self.startButton.clicked.connect(self.start_progress)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.progressBar)
#         layout.addWidget(self.startButton)
#         self.setLayout(layout)
#
#     def start_progress(self):
#         self.progress_thread = ProgressThread()
#         self.progress_thread.progress_signal.connect(self.update_progress_bar)
#         self.progress_thread.start()
#
#     def update_progress_bar(self, value):
#         self.progressBar.setValue(value)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())

import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QColor

class ColorThread(QThread):
    color_signal = pyqtSignal(str)

    def run(self):
        random_color = "#{:02X}{:02X}{:02X}".format(
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        )
        self.color_signal.emit(random_color)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tasodifiy Rang Generatori")
        self.setGeometry(300, 300, 300, 200)

        self.colorLabel = QLabel(self)
        self.colorLabel.setText("Rang namoyishi")
        self.colorLabel.setAlignment(Qt.AlignCenter)
        self.colorLabel.setStyleSheet("background-color: #FFFFFF;")  # Initial color

        self.refreshButton = QPushButton("Rangni yangilash", self)
        self.refreshButton.clicked.connect(self.update_color)

        layout = QVBoxLayout()
        layout.addWidget(self.colorLabel)
        layout.addWidget(self.refreshButton)
        self.setLayout(layout)

    def update_color(self):
        self.color_thread = ColorThread()
        self.color_thread.color_signal.connect(self.set_label_color)
        self.color_thread.start()

    def set_label_color(self, color_code):
        self.colorLabel.setStyleSheet(f"background-color: {color_code};")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
