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
        
    def ordenamiento_bubble(self):
        final = None
        while final != self.primero.siguiente:
            a = b = self.primero
            while b.siguiente != final:
                cicig = b.siguiente
                if b.pisos.nombre > cicig.pisos.nombre:
                    b.siguiente = cicig.siguiente
                    cicig.siguiente=b
                    if b != self.primero:
                        a.siguiente = cicig
                    else:
                        self.primero = cicig
                    b,cicig = cicig,b
                a = b
                b = b.siguiente
            final = b
            