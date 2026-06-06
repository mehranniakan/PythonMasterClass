import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton

## Logic of Calculation ##

def calculator():
    result = 'Please Enter Weight and Height'
    w = float(weight_entry.text())
    h = float(height_entry.text())

    bmi = w//h**2

    if bmi < 18.5:
        result = f'Your BMI is {bmi} and your Underweight'
    elif 18.5 <= bmi < 25:
        result =  f'Your BMI is {bmi} and your Normal weight'
    elif 25 <= bmi < 30:
        result =  f'Your BMI is {bmi} and your 1st class of obesity'
    elif 30 <= bmi < 40:
        result =  f'Your BMI is {bmi} and your 2nd class of obesity'
    elif bmi > 40:
        result =  f'Your BMI is {bmi} and your 3th class of obesity'

    result_label.setText(result)


## PyQt UI Design ##
app = QApplication(sys.argv)
app.setApplicationName('BMI')


window = QMainWindow()
window.setWindowTitle('BMI Calculator')
window.setFixedSize(QSize(300, 400))

widget = QWidget()

main_layout = QVBoxLayout()
widget.setLayout(main_layout)


weight_layout = QHBoxLayout()
height_layout = QHBoxLayout()

result_label = QLabel('Please Enter Weight and Height')
result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

main_layout.addWidget(result_label)
main_layout.addLayout(weight_layout)
main_layout.addLayout(height_layout)

submit_button = QPushButton('Calculate')
submit_button.clicked.connect(calculator)
main_layout.addWidget(submit_button)

weight_layout.addWidget(QLabel('Weight(kg) :'))
weight_entry = QLineEdit()
weight_layout.addWidget(weight_entry)

height_layout.addWidget(QLabel('Height(m) :'))
height_entry = QLineEdit()
height_layout.addWidget(height_entry)

window.setCentralWidget(widget)

window.show()

app.exec()