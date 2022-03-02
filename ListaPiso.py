from ListaPatrones import Listad_Patrones
from coordenadas import Listad_Coordenadas


class pisos:
    def __init__(self, nombre, filas, columnas, voltear, deslizar):
        #self.id = id
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.voltear = voltear
        self.deslizar = deslizar
        self.patrones = Listad_Patrones()
        self.coordenadas =Listad_Coordenadas()

class nodo:
    def __init__(self,pisos = None, siguiente = None):
        self.pisos = pisos
        self.siguiente= siguiente

class listaSimple:
    def __init__(self):
        self.primero= None

    def insertar(self, piso):
        if self.primero is None:
            self.primero = nodo(pisos=piso)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(pisos=piso)

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print("Nombre: ", actual.pisos.nombre, " filas: ", actual.pisos.filas, " Columnas: ", actual.pisos.columnas,
             " Precio voltear: ",actual.pisos.voltear, " Precio deslizar: ", actual.pisos.deslizar)
            actual = actual.siguiente
        
