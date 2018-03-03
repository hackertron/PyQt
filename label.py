import sys
from PyQt5 import QtWidgets, QtGui


app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

label1 = QtWidgets.QLabel(w)
label1.setText('i am label')

label2 = QtWidgets.QLabel(w)
label2.setPixmap(QtGui.QPixmap('lab.png'))

w.setWindowTitle('Empty Window')
w.setGeometry(200, 200, 200, 200)

label1.move(50, 50)
label2.move(100,100)

w.show()
sys.exit(app.exec_())
