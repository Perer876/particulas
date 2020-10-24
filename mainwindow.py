from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula
from algoritmos import distancia_euclidiana

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

    @Slot()
    def click_agregarFinal(self):
        iD = self.ui.id_lineEdit.text()
        velocidad = self.ui.velocidad_lineEdit.text()
        # Verificamos que las casillas libres no esten vacias y tambien que solo contengan números.
        if (iD.isnumeric() and velocidad.isnumeric()):
            origenX = self.ui.origenX_spinBox.value()
            origenY = self.ui.origenY_spinBox.value()
            destinoX = self.ui.destinoX_spinBox.value()
            destinoY = self.ui.destinoY_spinBox.value()
            red = self.ui.red_spinBox.value()
            green = self.ui.green_spinBox.value()
            blue = self.ui.blue_spinBox.value()
            # Instanciamos una particula para solamente agregarla al final de la lista.
            particula = Particula(int(iD), origenX, origenY, destinoX, destinoY, int(velocidad), red, green, blue)
            self.__particulas.agregar_final(particula)

    @Slot()
    def click_agregarInicio(self):
        iD = self.ui.id_lineEdit.text()
        velocidad = self.ui.velocidad_lineEdit.text()
        # Verificamos que las casillas libres no esten vacias y tambien que solo contengan números.
        if (iD.isnumeric() and velocidad.isnumeric()):
            origenX = self.ui.origenX_spinBox.value()
            origenY = self.ui.origenY_spinBox.value()
            destinoX = self.ui.destinoX_spinBox.value()
            destinoY = self.ui.destinoY_spinBox.value()
            red = self.ui.red_spinBox.value()
            green = self.ui.green_spinBox.value()
            blue = self.ui.blue_spinBox.value()
            # Instanciamos una particula para solamente agregarla al final de la lista.
            particula = Particula(int(iD), origenX, origenY, destinoX, destinoY, int(velocidad), red, green, blue)
            self.__particulas.agregar_inicio(particula)
