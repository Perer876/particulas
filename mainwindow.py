from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particulas
from particula import Particula
from algoritmos import distancia_euclidiana

DIA_CIR = 5

class MainWindow(QMainWindow):
    def __init__(self):
       super(MainWindow, self).__init__()

       self.__particulas = Particulas()
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)

       self.ui.agregarFinal_pushButton.clicked.connect(self.click_agregarFinal)
       self.ui.agregarInicio_pushButton.clicked.connect(self.click_agregarInicio)
       self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
       self.ui.buscar_pushButton.clicked.connect(self.click_buscar)
       self.ui.mostrarTabla_pushButton.clicked.connect(self.click_mostrarTabla)
       self.ui.dibujar_pushButton.clicked.connect(self.dibujar)
       self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        
       self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
       self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
       self.ui.action_OrderByIdAsc.triggered.connect(self.action_ordenar_por_id_ascendente)
       self.ui.action_OrderByDistanciaDes.triggered.connect(self.action_ordenar_por_distancia_descendente)
       self.ui.action_OrderByVelocidadAsc.triggered.connect(self.action_ordenar_por_velocidad_ascendente)

       self.scene = QGraphicsScene()
       self.ui.graphicsView.setScene(self.scene)
    
    # Inserta un objeto Particula en la fila indicada.
    def insertar_particula_en_tabla(self, particula:Particula, row:int):
        id_widget = QTableWidgetItem(str(particula.id))
        origen_x_widget = QTableWidgetItem(str(particula.origen_x))
        origen_y_widget = QTableWidgetItem(str(particula.origen_y))
        destino_x_widget = QTableWidgetItem(str(particula.destino_x))
        destino_y_widget = QTableWidgetItem(str(particula.destino_y))
        velocidad_widget = QTableWidgetItem(str(particula.velocidad))
        red_widget = QTableWidgetItem(str(particula.red))
        green_widget = QTableWidgetItem(str(particula.green))
        blue_widget = QTableWidgetItem(str(particula.blue))
        distancia_widget = QTableWidgetItem(str(particula.distancia))    
        self.ui.tabla.setItem(row, 0, id_widget)
        self.ui.tabla.setItem(row, 1, origen_x_widget)
        self.ui.tabla.setItem(row, 2, origen_y_widget)
        self.ui.tabla.setItem(row, 3, destino_x_widget)
        self.ui.tabla.setItem(row, 4, destino_y_widget)
        self.ui.tabla.setItem(row, 5, velocidad_widget)
        self.ui.tabla.setItem(row, 6, red_widget)
        self.ui.tabla.setItem(row, 7, green_widget)
        self.ui.tabla.setItem(row, 8, blue_widget)
        self.ui.tabla.setItem(row, 9, distancia_widget)
        
    def sacar_particula(self):
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
            return particula
        else:
            return None

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.__particulas))

    @Slot()
    def click_agregarFinal(self):
        particula = self.sacar_particula()
        if(particula != None):
            self.__particulas.agregar_final(particula)

    @Slot()
    def click_agregarInicio(self):
        particula = self.sacar_particula()
        if(particula != None):
            self.__particulas.agregar_inicio(particula)

    @Slot()
    def click_buscar(self):
        id_particula = self.ui.buscar_lineEdit.text()
        if(id_particula.isnumeric()):
            id_particula = int(id_particula)
            encontrado = False
            for particula in self.__particulas:
                if(particula.id == id_particula):
                    self.ui.tabla.clear()
                    self.ui.tabla.setRowCount(1)
                    self.insertar_particula_en_tabla(particula, 0)
                    encontrado = True
                    return
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atención",
                    f"La partiula con el id {id_particula} no fue encontrado"
                )

    @Slot()
    def click_mostrarTabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ['ID','Origen X','Origen Y','Destino X','Destino Y','Velocidad','Red','Green','Blue','Distancia']
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.__particulas))
        row = 0
        for particula in self.__particulas:
            self.insertar_particula_en_tabla(particula, row)
            row += 1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir Archivo', '.','*.json')[0]
        if self.__particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.','*.json')[0]
        if self.__particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot()
    def action_ordenar_por_id_ascendente(self):
        print("ordenar por id asc")

    @Slot()
    def action_ordenar_por_distancia_descendente(self):
        print("ordenar por distancia des")

    @Slot()
    def action_ordenar_por_velocidad_ascendente(self):
        print("ordenar por velocidad asc")

    @Slot()
    def dibujar(self):
        for particula in self.__particulas:
            pen = QPen()
            pen.setWidth(3)
            
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)
            self.scene.addEllipse(particula.origen_x - DIA_CIR/2, particula.origen_y - DIA_CIR/2,DIA_CIR,DIA_CIR, pen)
            self.scene.addEllipse(particula.destino_x - DIA_CIR/2, particula.destino_y - DIA_CIR/2,DIA_CIR,DIA_CIR, pen)
            self.scene.addLine(particula.origen_x,particula.origen_y, particula.destino_x, particula.destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()
    
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    