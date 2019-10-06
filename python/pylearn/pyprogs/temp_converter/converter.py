import sys
from PyQt5 import QtCore, QtWidgets, uic

form_class = uic.loadUiType("tempconv.ui")[0]

class Converter(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)
        self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)
        self.action_CtoF.triggered.connect(self.btn_CtoF_clicked)
        self.action_FtoC.triggered.connect(self.btn_FtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btn_CtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel * 9 / 5.0 + 32
        self.spinFahr.setValue(int(fahr + 0.5))

    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5 / 9.0
        self.editCel.setText(str(cel))

    def menuExit_selected(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
converter = Converter()
converter.show()
app.exec_()
