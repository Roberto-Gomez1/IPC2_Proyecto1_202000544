class nodoDoblementeP:
    def __init__(self,cna_x = None, cna_y=None, letra = None, siguiente= None, anterior = None):
        self.cna_x = cna_x
        self.cna_y = cna_y
        self.letra = letra
        self.siguiente = siguiente
        self.anterior = anterior

class Listad_Coordenadas:
    def __init__(self):
        self.raiz = nodoDoblementeP()
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
                cadena += "Coordenada en x: " + nodoaux.cna_x+ "Coordenada en y: " + nodoaux.cna_y + " Letra del patron: "+ nodoaux.letra
                if nodoaux.siguiente is not None:
                    cadena +="\n"
                    nodoaux = nodoaux.siguiente
                else: 
                    break
            else:
                break
        print(cadena)
