from particula import Particula
import json

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.__particulas):
            particula = self.__particulas[self.count]
            self.count += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            print(ubicacion)
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def ordenar_por_id_asc(self):
        self.__particulas.sort()

    def ordenar_por_id_des(self):
        self.__particulas.sort(reverse=True)

    def ordenar_por_distancia_asc(self):
        self.__particulas.sort(key=sort_by_distancia)

    def ordenar_por_distancia_des(self):
        self.__particulas.sort(key=sort_by_distancia, reverse=True)

    def ordenar_por_velocidad_asc(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)

    def ordenar_por_velocidad_des(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad, reverse=True)

def sort_by_distancia(particula:Particula):
    return particula.distancia
