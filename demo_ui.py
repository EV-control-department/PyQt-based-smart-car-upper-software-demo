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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(465, 264)
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
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 451, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.v = QLabel(self.horizontalLayoutWidget)
        self.v.setObjectName(u"v")
        font = QFont()
        font.setPointSize(15)
        self.v.setFont(font)

        self.horizontalLayout.addWidget(self.v)

        self.direction = QLabel(self.horizontalLayoutWidget)
        self.direction.setObjectName(u"direction")
        self.direction.setFont(font)

        self.horizontalLayout.addWidget(self.direction)

        self.state = QLabel(self.horizontalLayoutWidget)
        self.state.setObjectName(u"state")
        self.state.setFont(font)

        self.horizontalLayout.addWidget(self.state)

        self.mode = QLabel(self.horizontalLayoutWidget)
        self.mode.setObjectName(u"mode")
        self.mode.setFont(font)

        self.horizontalLayout.addWidget(self.mode)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.v.setText(QCoreApplication.translate("Form", u"\u901f\u5ea6", None))
        self.direction.setText(QCoreApplication.translate("Form", u"\u89d2\u5ea6", None))
        self.state.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.mode.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None))
    # retranslateUi

