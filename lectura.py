import xml.etree.ElementTree as ET
from ListaPiso import pisos, listaSimple,nodo
from ListaPatrones import Listad_Patrones, nodoDoblemente
class lectura:
    
    def leer(entrada):
        
        listaPisos = listaSimple()
        ListaPatrones = Listad_Patrones()
        tree = ET.parse(entrada)
        root = tree.getroot()
        for item in root:
            nombre1 = item.attrib['nombre'].replace(" ", "").replace("\n","")
            filas1 = item[0].text.replace(" ","")
            columnas1 = item[1].text.replace(" ","")
            celdas = int(filas1) * int(columnas1)    
            voltear1= item[2].text.replace(" ","")
            deslizar1= item[3].text.replace(" ","")
            temporal = pisos(nombre1, filas1, columnas1,voltear1,deslizar1)            
            listaPisos.insertar(temporal)
            for aa in item.find('patrones'):
                codigopatron = aa.attrib['codigo'].replace("\n","")
                patronletras = aa.text.replace(" ","").replace("\n","")
                cn_x = 0
                cn_y=0
                for i  in str(patronletras):
                    for x in range(int(filas1)):

                        for y in range(int(columnas1)):


                            print(x,y,i)
                print('termina el patron')
                nodotemporal = nodoDoblemente(codigopatron,patronletras)
                ListaPatrones.insertar(nodotemporal)
        listaPisos.mostrar()
        ListaPatrones.recorrer()
