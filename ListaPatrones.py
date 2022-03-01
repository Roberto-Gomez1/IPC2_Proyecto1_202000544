from coordenadas import Listad_Coordenadas
class nodoDoblemente:
    def __init__(self,codigo = None, patrones=None, siguiente= None, anterior = None):
        self.codigo = codigo
        self.patrones = patrones
        self.siguiente = siguiente
        self.anterior = anterior
        self.coordenadas = Listad_Coordenadas()

class Listad_Patrones:
    def __init__(self):
        self.raiz = nodoDoblemente()
        self.ultimo = self.raiz

    def insertar(self,nuevonodo):
        if self.raiz.codigo is None:
            self.raiz = nuevonodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevonodo
            nuevonodo.anterior = self.raiz
            self.ultimo = nuevonodo
        else:
            self.ultimo.siguiente = nuevonodo
            nuevonodo.anterior = self.ultimo
            self.ultimo=nuevonodo

    def recorrer(self):
        nodoaux = self.raiz
        cadena = ''
        while True:
            if nodoaux.codigo is not None:
                cadena += "Codigo: " + nodoaux.codigo + " Patron: "+ nodoaux.patrones
                if nodoaux.siguiente is not None:
                    cadena +="\n"
                    nodoaux = nodoaux.siguiente
                else: 
                    break
            else:
                break
        print(cadena)


            
        