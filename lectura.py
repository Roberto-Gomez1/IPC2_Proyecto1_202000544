import xml.etree.ElementTree as ET
from ListaPatrones import nodoDoblemente
from ListaPiso import listaSimple,nodo, pisos
from coordenadas import nodoDoblementeP
class lectura:
    
    def leer(entrada):
        
        listaPisos = listaSimple()
        tree = ET.parse(entrada)
        root = tree.getroot()
        for item in root:
            id = 0
            nombre1 = item.attrib['nombre'].replace(" ", "").replace("\n","")
            filas1 = item[0].text.replace(" ","")
            columnas1 = item[1].text.replace(" ","")
            celdas = int(filas1) * int(columnas1)    
            voltear1= item[2].text.replace(" ","")
            deslizar1= item[3].text.replace(" ","")
            temporal = pisos(nombre1, filas1, columnas1,voltear1,deslizar1)
            listaPisos.insertar(temporal)           
            #listaPisos.insertar(temporal)
            for aa in item.find('patrones'):
                id += 1
                codigopatron = aa.attrib['codigo'].replace("\n","")
                patronletras = aa.text.replace(" ","").replace("\n","")
                aux_patron =str(patronletras)
                aux_codigo = str(codigopatron)
                aux_contador = 0
                temporal.coordenadas.insertar(nodoDoblementeP(-44,filas1,columnas1,aux_codigo))
                for x in range(int(filas1)):
                    for y in range(int(columnas1)):
                        nodotemporal2 = nodoDoblementeP(id,x,y,aux_patron[aux_contador])
                        temporal.coordenadas.insertar(nodotemporal2)
                        aux_contador += 1
                #print('termina el patron')
                temporal.coordenadas.insertar(nodoDoblementeP(-45,-45,-45,aux_codigo))
                nodotemporal = nodoDoblemente(codigopatron,patronletras)
                temporal.patrones.insertar(nodotemporal)
            temporal.coordenadas.recorrer()
            print('termina el patron')
            temporal.patrones.ordenamiento_bubble()
            temporal.patrones.recorrer()
            temporal.coordenadas.graficar()
        #listaPisos.mostrar()
        listaPisos.ordenamiento_bubble()
        listaPisos.mostrar()
