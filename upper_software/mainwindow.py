# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 481, 91))
        font = QFont()
        font.setPointSize(64)
        font.setBold(True)
        self.label.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 140, 281, 361))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.accelerator = QLabel(self.verticalLayoutWidget)
        self.accelerator.setObjectName(u"accelerator")
        font1 = QFont()
        font1.setPointSize(20)
        self.accelerator.setFont(font1)

        self.verticalLayout.addWidget(self.accelerator)

        self.speed = QLabel(self.verticalLayoutWidget)
        self.speed.setObjectName(u"speed")
        self.speed.setFont(font1)

        self.verticalLayout.addWidget(self.speed)

        self.direction = QLabel(self.verticalLayoutWidget)
        self.direction.setObjectName(u"direction")
        self.direction.setFont(font1)

        self.verticalLayout.addWidget(self.direction)

        self.arm = QLabel(self.verticalLayoutWidget)
        self.arm.setObjectName(u"arm")
        self.arm.setFont(font1)

        self.verticalLayout.addWidget(self.arm)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(520, 140, 160, 361))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.acc_slider = QSlider(self.horizontalLayoutWidget)
        self.acc_slider.setObjectName(u"acc_slider")
        self.acc_slider.setMinimum(-100)
        self.acc_slider.setMaximum(100)
        self.acc_slider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout.addWidget(self.acc_slider)

        self.dir_slider = QSlider(self.horizontalLayoutWidget)
        self.dir_slider.setObjectName(u"dir_slider")
        self.dir_slider.setMinimum(-45)
        self.dir_slider.setMaximum(45)
        self.dir_slider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout.addWidget(self.dir_slider)

        self.arm_slider = QSlider(self.horizontalLayoutWidget)
        self.arm_slider.setObjectName(u"arm_slider")
        self.arm_slider.setMaximum(2)
        self.arm_slider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout.addWidget(self.arm_slider)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"E\u552f\u676f\u4e0a\u4f4d\u673a", None))
        self.accelerator.setText(QCoreApplication.translate("MainWindow", u"\u6cb9\u95e8\uff1a0", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6\uff1a0", None))
        self.direction.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5411\uff1a0", None))
        self.arm.setText(QCoreApplication.translate("MainWindow", u"\u673a\u68b0\u81c2\u4f4d\u7f6e\uff1a0", None))
    # retranslateUi

