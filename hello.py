# plain blank window 

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.show()
sys.exit(app.exec_())
