import os
import webbrowser

from matplotlib.pyplot import contour
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
        aux_contador = 0
        aux_contador1 = 0
        empieza = "-44"
        termina = "-45"
        aux = self.raiz
        graph = "digraph G { \nrankdir = LR\n"
        
        while aux is not None:
            if str(aux.id) == empieza:
                graph+="subgraph "
                graph+="{}".format(aux.letra)
                graph+= "{ \n"
                aux_nombre = aux.letra
                aux_filas1 = int(aux.cna_x)
                aux_col1=int(aux.cna_y)
                aux = aux.siguiente
                
            aux_contador1+=1
            if aux.letra == "B" or aux.letra == "W":
                if aux.letra == "B":
                    nombrecolor = "black"
                    colorletra = "white"
                elif aux.letra == "W":
                    nombrecolor = "white"
                    colorletra ="black"
                #for i in range(aux.id):
                
                #    if aux_contador< aux_col1:
                graph += '{}[label="{}",color = "black",fontcolor ="{}",fillcolor="{}",style="filled",shape="box"];\n'.format(aux_contador1,aux_contador1,colorletra,nombrecolor)
                        #f.write('valor' + str(contG) + '->valor' + str(contG + m) + ';\n')
                #    elif aux_contador >= aux_col1 and aux_contador <= (aux_col1 * aux_filas1)-1:
                 #       graph += '{}[label="{}",color = "black",fontcolor ="{}",fillcolor="{}",style="filled",shape="box"];\n'.format(aux_contador1,aux.letra,colorletra,nombrecolor)
                        #f.write(' valor' + str(contG) + '->valor' + str(contG + m) + ';\n')
               #     elif aux_contador == (aux_col1 * aux_filas1) - aux_col1:
                #        break

                    #contG = contG + 1
                    
                aux_contador+=1
                    #graph+='rankdir=UD\n'
                #graph += '{}<-{};\n'.format(aux.letra,aux.siguiente)
                aux=aux.siguiente
            
            if str(aux.id) == termina:
                graph+="}\n"
                aux = aux.siguiente 
        aux = self.raiz
        aux_contador2 = 1
        aux_contador3 = 0
        while aux is not None:
            if str(aux.id) == empieza:
                aux_filas2 = int(aux.cna_x)
                aux_col2=int(aux.cna_y)
                aux = aux.siguiente

            aux_contador3 +=1
            if aux.letra == "B" or aux.letra == "W":
                for i in range(aux_contador):
                    if(aux_contador2 == 1 or aux_contador2 == (aux_contador/2)+1):
                        graph += "\nsubgraph cluster_" + str(0 if i==0 else 1)+ "{\nlabel=\""+ ("Patron Inicial" if i==0 else "Patron Final")+ "\"\nrankdir=TB\n"

                    if(aux_contador2 == aux_contador/2):
                        graph += "\n}"
                    if aux_contador2%aux_col2 == 0:
                        aux_contador2+=1
                        continue
                    elif aux_contador2 < (aux_contador):
                        graph += '{}->{};\n'.format(aux_contador2,aux_contador2+1)
                        aux_contador2+=1
                graph += "\n}"    
                aux=aux.siguiente
            if str(aux.id) == termina:
                aux = aux.siguiente
        graph+="}"

        documentotxt="GraficaPisos"+str(aux_contador)+".txt"
        with open(documentotxt,'w') as grafica: 
            
            grafica.write(graph)
        pdf="GraficaPisos"+str(aux_contador)+".pdf"
        os.system("dot -Tpdf "+documentotxt+" -o "+pdf)
        webbrowser.open(pdf)
        #aux_contador +=1
