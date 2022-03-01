class pisos:
    def __init__(self, nombre, filas, columnas, voltear, deslizar):
        #self.id = id
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.voltear = voltear
        self.deslizar = deslizar

class nodo:
    def __init__(self,pisos = None, siguiente = None, tamano = 0):
        self.pisos = pisos
        self.siguiente= siguiente
        self.tamano =tamano 

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
        
