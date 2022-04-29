import sys
from PyQt5.QtWidgets import QDialog, QApplication
from pierwsza_aplikacja_ui import *


class Pierwsza(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.show()
        self.ui.przycisk.clicked.connect(self.napisz)

    def napisz(self):
        self.ui.etykieta.setText("Witaj !!!")


aplikacja = QApplication(sys.argv)
okno = Pierwsza()
okno.show()
sys.exit(aplikacja.exec_())
