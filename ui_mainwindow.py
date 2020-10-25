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
        MainWindow.resize(533, 476)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.agregarFinal_pushButton = QPushButton(self.groupBox_2)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.gridLayout.addWidget(self.agregarFinal_pushButton, 7, 0, 1, 2)

        self.origenY_spinBox = QSpinBox(self.groupBox_2)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenY_spinBox, 2, 1, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox_2)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenX_spinBox, 1, 1, 1, 1)

        self.label_destinoX = QLabel(self.groupBox_2)
        self.label_destinoX.setObjectName(u"label_destinoX")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.groupBox_2)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoY_spinBox, 4, 1, 1, 1)

        self.agregarInicio_pushButton = QPushButton(self.groupBox_2)
        self.agregarInicio_pushButton.setObjectName(u"agregarInicio_pushButton")

        self.gridLayout.addWidget(self.agregarInicio_pushButton, 8, 0, 1, 2)

        self.label_origenX = QLabel(self.groupBox_2)
        self.label_origenX.setObjectName(u"label_origenX")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_red = QLabel(self.groupBox)
        self.label_red.setObjectName(u"label_red")

        self.gridLayout_4.addWidget(self.label_red, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.label_green = QLabel(self.groupBox)
        self.label_green.setObjectName(u"label_green")

        self.gridLayout_4.addWidget(self.label_green, 1, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.green_spinBox, 1, 1, 1, 1)

        self.label_blue = QLabel(self.groupBox)
        self.label_blue.setObjectName(u"label_blue")

        self.gridLayout_4.addWidget(self.label_blue, 2, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(500)

        self.gridLayout_4.addWidget(self.blue_spinBox, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)

        self.destinoX_spinBox = QSpinBox(self.groupBox_2)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoX_spinBox, 3, 1, 1, 1)

        self.label_destinoY = QLabel(self.groupBox_2)
        self.label_destinoY.setObjectName(u"label_destinoY")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.label_id = QLabel(self.groupBox_2)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox_2)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 1, 1, 1)

        self.label_origenY = QLabel(self.groupBox_2)
        self.label_origenY.setObjectName(u"label_origenY")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.label_velocidad = QLabel(self.groupBox_2)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.velocidad_lineEdit = QLineEdit(self.groupBox_2)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 1, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox_2)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 9, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout_3.addWidget(self.salida, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 533, 20))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.agregarInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"Red: ", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

