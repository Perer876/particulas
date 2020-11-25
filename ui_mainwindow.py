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
        MainWindow.resize(624, 485)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPor_id = QAction(MainWindow)
        self.actionPor_id.setObjectName(u"actionPor_id")
        self.actionPor_distancia = QAction(MainWindow)
        self.actionPor_distancia.setObjectName(u"actionPor_distancia")
        self.action_OrderByIdAsc = QAction(MainWindow)
        self.action_OrderByIdAsc.setObjectName(u"action_OrderByIdAsc")
        self.action_OrderByDistanciaDes = QAction(MainWindow)
        self.action_OrderByDistanciaDes.setObjectName(u"action_OrderByDistanciaDes")
        self.action_OrderByVelocidadAsc = QAction(MainWindow)
        self.action_OrderByVelocidadAsc.setObjectName(u"action_OrderByVelocidadAsc")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_3.addWidget(self.salida, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.destinoX_spinBox = QSpinBox(self.groupBox_2)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoX_spinBox, 3, 1, 1, 1)

        self.label_id = QLabel(self.groupBox_2)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.label_velocidad = QLabel(self.groupBox_2)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.velocidad_lineEdit = QLineEdit(self.groupBox_2)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 1, 1, 1)

        self.origenY_spinBox = QSpinBox(self.groupBox_2)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenY_spinBox, 2, 1, 1, 1)

        self.agregarInicio_pushButton = QPushButton(self.groupBox_2)
        self.agregarInicio_pushButton.setObjectName(u"agregarInicio_pushButton")

        self.gridLayout.addWidget(self.agregarInicio_pushButton, 8, 0, 1, 2)

        self.mostrar_pushButton = QPushButton(self.groupBox_2)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 9, 0, 1, 2)

        self.label_origenX = QLabel(self.groupBox_2)
        self.label_origenX.setObjectName(u"label_origenX")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox_2)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenX_spinBox, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)

        self.label_destinoX = QLabel(self.groupBox_2)
        self.label_destinoX.setObjectName(u"label_destinoX")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.label_destinoY = QLabel(self.groupBox_2)
        self.label_destinoY.setObjectName(u"label_destinoY")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.label_origenY = QLabel(self.groupBox_2)
        self.label_origenY.setObjectName(u"label_origenY")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.groupBox_2)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoY_spinBox, 4, 1, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox_2)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 1, 1, 1)

        self.agregarFinal_pushButton = QPushButton(self.groupBox_2)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.gridLayout.addWidget(self.agregarFinal_pushButton, 7, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_5.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_5.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_5.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrarTabla_pushButton = QPushButton(self.tab_2)
        self.mostrarTabla_pushButton.setObjectName(u"mostrarTabla_pushButton")

        self.gridLayout_5.addWidget(self.mostrarTabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_6.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_6.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 624, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        self.menuOrdenar_particulas_por = QMenu(self.menuOrdenar)
        self.menuOrdenar_particulas_por.setObjectName(u"menuOrdenar_particulas_por")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.menuOrdenar_particulas_por.menuAction())
        self.menuOrdenar_particulas_por.addAction(self.action_OrderByIdAsc)
        self.menuOrdenar_particulas_por.addAction(self.action_OrderByDistanciaDes)
        self.menuOrdenar_particulas_por.addAction(self.action_OrderByVelocidadAsc)
        self.menuVer.addAction(self.actionGrafo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.actionPor_id.setText(QCoreApplication.translate("MainWindow", u"Por id", None))
        self.actionPor_distancia.setText(QCoreApplication.translate("MainWindow", u"Por distancia", None))
        self.action_OrderByIdAsc.setText(QCoreApplication.translate("MainWindow", u"Id (ascendente)", None))
        self.action_OrderByDistanciaDes.setText(QCoreApplication.translate("MainWindow", u"Distancia (descendente)", None))
        self.action_OrderByVelocidadAsc.setText(QCoreApplication.translate("MainWindow", u"Velocidad (ascendente)", None))
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+G", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.agregarInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"Red: ", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrarTabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menuOrdenar_particulas_por.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar particulas por", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
    # retranslateUi

