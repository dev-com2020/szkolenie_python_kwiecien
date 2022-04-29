from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Sekwencje(object):
    def setupUi(self, Sekwencje):
        if Sekwencje.objectName():
            Sekwencje.setObjectName(u"Sekwencje")
        Sekwencje.resize(550, 225)
        self.formLayoutWidget = QWidget(Sekwencje)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 531, 161))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.sekwencjaLineEdit = QLineEdit(self.formLayoutWidget)
        self.sekwencjaLineEdit.setObjectName(u"sekwencjaLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sekwencjaLineEdit)

        self.sekwencjaLabel = QLabel(self.formLayoutWidget)
        self.sekwencjaLabel.setObjectName(u"sekwencjaLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.sekwencjaLabel)

        self.line = QFrame(self.formLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line)

        self.komplementarnaLabel = QLabel(self.formLayoutWidget)
        self.komplementarnaLabel.setObjectName(u"komplementarnaLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.komplementarnaLabel)

        self.komplementarnaLineEdit = QLineEdit(self.formLayoutWidget)
        self.komplementarnaLineEdit.setObjectName(u"komplementarnaLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.komplementarnaLineEdit)

        self.sekwRNALabel = QLabel(self.formLayoutWidget)
        self.sekwRNALabel.setObjectName(u"sekwRNALabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sekwRNALabel)

        self.sekwRNALineEdit = QLineEdit(self.formLayoutWidget)
        self.sekwRNALineEdit.setObjectName(u"sekwRNALineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sekwRNALineEdit)

        self.sekwAminokwLabel = QLabel(self.formLayoutWidget)
        self.sekwAminokwLabel.setObjectName(u"sekwAminokwLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sekwAminokwLabel)

        self.sekwAminokwLineEdit = QLineEdit(self.formLayoutWidget)
        self.sekwAminokwLineEdit.setObjectName(u"sekwAminokwLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sekwAminokwLineEdit)

        self.pushButton = QPushButton(Sekwencje)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 190, 75, 23))
        self.pushButton_2 = QPushButton(Sekwencje)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 190, 75, 23))

        self.retranslateUi(Sekwencje)

        QMetaObject.connectSlotsByName(Sekwencje)
    # setupUi

    def retranslateUi(self, Sekwencje):
        Sekwencje.setWindowTitle(QCoreApplication.translate("Sekwencje", u"Sekwencje", None))
        self.sekwencjaLabel.setText(QCoreApplication.translate("Sekwencje", u"Sekwencje DNA", None))
        self.komplementarnaLabel.setText(QCoreApplication.translate("Sekwencje", u"Komplementarna", None))
        self.sekwRNALabel.setText(QCoreApplication.translate("Sekwencje", u"Sekw.RNA", None))
        self.sekwAminokwLabel.setText(QCoreApplication.translate("Sekwencje", u"Sekw.aminokw.", None))
        self.pushButton.setText(QCoreApplication.translate("Sekwencje", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Sekwencje", u"PushButton", None))
    # retranslateUi

