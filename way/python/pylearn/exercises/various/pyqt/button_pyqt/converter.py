import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

form_class = uic.loadUiType("Converter.ui")[0]


class Converter(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.button_clicked)

	def button_clicked(self):
		x = self.pushButton.x()
		y = self.pushButton.y()
		x += 50
		y += 50
		self.pushButton.move(x, y)


app = QtWidgets.QApplication(sys.argv)
converter = Converter()
converter.show()
app.exec_()
