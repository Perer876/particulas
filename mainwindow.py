from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from classes_particulas.particulas import Particulas
from classes_particulas.particula import Particula
from classes_particulas.algoritmos import distancia_euclidiana

class MainWindow(QMainWindow):
    def __init__(self):
       super(MainWindow, self).__init__()
       self.__particulas = Particulas()
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)
       self.ui.agregarFinal_pushButton.clicked.connect(self.click_agregarFinal)
       self.ui.agregarInicio_pushButton.clicked.connect(self.click_agregarInicio)
       self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
    
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.__particulas))
        # self.__particulas.mostrar()

    @Slot()
    def click_agregarFinal(self):
        if self.ui.id_lineEdit.text() == '':
            iD = 0
        else:
            iD = int(self.ui.id_lineEdit.text())
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        if self.ui.velocidad_lineEdit.text() == '':
            velocidad = 0
        else:
            velocidad = int(self.ui.id_lineEdit.text())
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(iD, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.__particulas.agregar_final(particula)

    @Slot()
    def click_agregarInicio(self):
        if self.ui.id_lineEdit.text() == '':
            iD = 0
        else:
            iD = int(self.ui.id_lineEdit.text())
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        if self.ui.velocidad_lineEdit.text() == '':
            velocidad = 0
        else:
            velocidad = int(self.ui.id_lineEdit.text())
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(iD, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue)
        self.__particulas.agregar_inicio(particula)
