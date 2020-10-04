# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(292, 382)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_3, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_4, 4, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(500)

        self.gridLayout_4.addWidget(self.spinBox_5, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(500)

        self.gridLayout_4.addWidget(self.spinBox_6, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(500)

        self.gridLayout_4.addWidget(self.spinBox_7, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 292, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

