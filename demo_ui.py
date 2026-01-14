# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo1.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSlider,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(457, 277)
        self.state = QLabel(Form)
        self.state.setObjectName(u"state")
        self.state.setGeometry(QRect(70, 30, 91, 31))
        font = QFont()
        font.setPointSize(15)
        self.state.setFont(font)
        self.v = QLabel(Form)
        self.v.setObjectName(u"v")
        self.v.setGeometry(QRect(150, 30, 91, 31))
        self.v.setFont(font)
        self.mode = QLabel(Form)
        self.mode.setObjectName(u"mode")
        self.mode.setGeometry(QRect(230, 30, 91, 31))
        self.mode.setFont(font)
        self.direction = QLabel(Form)
        self.direction.setObjectName(u"direction")
        self.direction.setGeometry(QRect(310, 30, 91, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.direction.setFont(font1)
        self.v_2 = QSlider(Form)
        self.v_2.setObjectName(u"v_2")
        self.v_2.setGeometry(QRect(90, 140, 281, 16))
        self.v_2.setMinimum(-100)
        self.v_2.setMaximum(100)
        self.v_2.setOrientation(Qt.Orientation.Horizontal)
        self.direction_2 = QSlider(Form)
        self.direction_2.setObjectName(u"direction_2")
        self.direction_2.setGeometry(QRect(90, 170, 281, 16))
        self.direction_2.setMinimum(-100)
        self.direction_2.setMaximum(100)
        self.direction_2.setOrientation(Qt.Orientation.Horizontal)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.state.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.v.setText(QCoreApplication.translate("Form", u"\u901f\u5ea6", None))
        self.mode.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None))
        self.direction.setText(QCoreApplication.translate("Form", u"\u89d2\u5ea6", None))
    # retranslateUi

