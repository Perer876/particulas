import math
from collections import deque

def distancia_euclidiana(x_1=0, y_1=0, x_2=0, y_2=0):
    return math.sqrt((x_2 - x_1)*(x_2 - x_1) + (y_2 - y_1)*(y_2 - y_1))

def busqueda_profundidad(grafo:dict, origen):
    visitados = []
    pila = deque()
    recorrido = []

    visitados.append(origen)
    pila.append(origen)

    while len(pila) > 0:
        vertice = pila[-1]
        recorrido.append(vertice)
        pila.pop()
        if vertice in grafo:
            adyacencias = grafo[vertice]
        else:
            adyacencias = []

        for ady in adyacencias:
            vertice_adyacente = (ady[0], ady[1])
            if not vertice_adyacente in visitados:
                visitados.append(vertice_adyacente)
                pila.append(vertice_adyacente)
                
    return recorrido



def busqueda_anchura(grafo, origen):
    visitados = []
    cola = deque()
    recorrido = []

    visitados.append(origen)
    cola.append(origen)

    while len(cola) > 0:
        vertice = cola[0]
        recorrido.append(vertice)
        cola.popleft()
        if vertice in grafo:
            adyacencias = grafo[vertice]
        else:
            adyacencias = []

        for ady in adyacencias:
            vertice_adyacente = (ady[0], ady[1])
            if not vertice_adyacente in visitados:
                visitados.append(vertice_adyacente)
                cola.append(vertice_adyacente)
                
    return recorrido