import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

button1 = QtWidgets.QPushButton(w)
label1 = QtWidgets.QLabel(w)
button1.setText('Push Button')
label1.setText('press')
vertical_box = QtWidgets.QVBoxLayout()
vertical_box.addWidget(button1)
vertical_box.addWidget(label1)
w.setLayout(vertical_box)

button1.move(100, 100)
label1.move(150, 150)

w.setWindowTitle('Empty Window')
w.setGeometry(200, 200, 200, 200)
w.show()
sys.exit(app.exec_())

