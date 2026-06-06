import sys
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QSpinBox, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, \
    QHBoxLayout, QMessageBox

class CountDownGui(QMainWindow):
    main_counter_label = None
    counter_minute_entry = None
    counter_second_entry = None
    clock_seprator = None
    welcome_label = None
    start_button = None
    stop_button = None
    total_time = 0
    min_val = None
    sec_val = None

    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.my_timer)

        self.setFixedSize(400, 300)
        self.setWindowTitle("CountDown")
        self.create_widgets()
        self.app_alignment()
        self.app_connection()


    def create_widgets(self):
        self.welcome_label = QLabel("Welcome to CountDownApp")
        self.welcome_label.setFont(QFont('Arial', 16))

        self.main_counter_label = QLabel()
        self.main_counter_label.setFont(QFont('Arial', 16))
        self.main_counter_label.hide()

        self.counter_minute_entry = QSpinBox()
        self.clock_seprator = QLabel(':')
        self.counter_second_entry = QSpinBox()

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

    def app_alignment(self):
        main_layout = QVBoxLayout()

        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.welcome_label)

        counter_layout = QHBoxLayout()
        counter_layout.addWidget(self.counter_minute_entry)
        counter_layout.addWidget(self.clock_seprator)
        counter_layout.addWidget(self.counter_second_entry)
        counter_layout.addWidget(self.main_counter_label)

        counter_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(counter_layout)

        main_layout.addWidget(self.start_button)
        main_layout.addWidget(self.stop_button)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def app_connection(self):
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)

    def start(self):
        if self.total_time == 0:
            self.min_val = self.counter_minute_entry.value()
            self.sec_val = self.counter_second_entry.value()

        if 1 <= self.min_val <= 60 and 0 <= self.sec_val <= 59 :

            self.start_input_changer()

            self.total_time = (self.min_val * 60 + self.sec_val)

            self.show_remaining_time()

            self.timer.start(1000)
        else:
            self.show_message("Invalid Input", "Enter minute between 0 and 60 and seconds between 0 and 59")

    def stop(self):
        self.timer.stop()
        self.start_button.setEnabled(True)

    def my_timer(self):

        if self.total_time > 0:
            self.total_time -= 1
            self.show_remaining_time()

        else:
            self.timer.stop()
            self.show_message("Finished", "Time is up!")
            self.stop_input_changer()

    def show_remaining_time(self):
        self.min_val, self.sec_val = divmod(self.total_time, 60)
        self.main_counter_label.setText(f'{self.min_val:02d}:{self.sec_val:02d}')

    def start_input_changer(self):
        self.counter_minute_entry.hide()
        self.counter_second_entry.hide()
        self.clock_seprator.hide()

        self.main_counter_label.show()
        self.start_button.setEnabled(False)

    def stop_input_changer(self):
        self.counter_minute_entry.show()
        self.counter_second_entry.show()
        self.clock_seprator.show()

        self.main_counter_label.hide()
        self.start_button.setEnabled(True)

    def show_message(self, title, message):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.exec_()


app = QApplication(sys.argv)

window = CountDownGui()

window.show()

app.exec_()