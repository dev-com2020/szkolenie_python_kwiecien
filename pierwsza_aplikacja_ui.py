from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 447)
        self.przycisk = QPushButton(Dialog)
        self.przycisk.setObjectName(u"przycisk")
        self.przycisk.setGeometry(QRect(180, 340, 201, 31))
        self.etykieta = QLabel(Dialog)
        self.etykieta.setObjectName(u"etykieta")
        self.etykieta.setGeometry(QRect(176, 190, 181, 20))
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.etykieta.setFont(font)
        self.etykieta.setCursor(QCursor(Qt.OpenHandCursor))
        self.etykieta.setTextFormat(Qt.AutoText)
        self.etykieta.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Moja pierwsza aplikacja", None))
        self.przycisk.setText(QCoreApplication.translate("Dialog", u"Kliknij!", None))
        self.etykieta.setText("")
    # retranslateUi

