import os
import webbrowser
class nodoDoblementeP:
    def __init__(self,id=None,cna_x = None, cna_y=None, letra = None, siguiente= None, anterior = None):
        self.id = id
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
        if self.raiz.cna_x is None:
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
            if nodoaux.cna_x is not None:
                cadena += "Id: "+ str(nodoaux.id)+" Coordenada en x: " + str(nodoaux.cna_x)+ " Coordenada en y: " + str(nodoaux.cna_y) + " Letra del patron: "+ nodoaux.letra
                if nodoaux.siguiente is not None:
                    cadena +="\n"
                    nodoaux = nodoaux.siguiente
                else: 
                    break
            else:
                break
        print(cadena)
    
    
    def graficar(self):
        aux = self.raiz
        graph = " digraph G { \n"
        while aux is not None:
            if aux.siguiente is None:
                None
            else: 
                graph += '{}->{};\n'.format(aux.letra,aux.siguiente.letra)
            aux=aux.siguiente
        graph+="}"

        documentotxt="listaForma1.txt"
        with open(documentotxt,'w') as grafica: 
            grafica.write(graph)
        pdf="listaForma1.pdf"
        os.system("neato -Tpdf "+documentotxt+" -o "+pdf)
        webbrowser.open(pdf)
