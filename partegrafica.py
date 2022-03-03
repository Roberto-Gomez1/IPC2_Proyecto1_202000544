from ListaGeneral import *
from MetodosRuta import *
from Salida import *
from ListaSalida import *
import xml.etree.ElementTree as ET
import xml.etree.cElementTree as cET
from Lista import *
from Matriz import *
from ClaseNodo import terrenos
import os
import time
import sys
 
from graphviz import Digraph
dot = Digraph(comment='The Round Table')
listaDatos= Lista()
nombret=Lista()
ListaTerrenos = listageneral()
Ruta = ListaRutaa()
Salida= salidaxml()
name = ''
combustible=0
def Menu(ruta):
    global name
    print("********MENU PRINCIPAL********")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiate")
    print("5. Generar gráfica")
    print("6. Salida")
    opcion = input('Ingrese una Opcion: ')
    if opcion == "1":
        
        ruta= input('ingrese ruta de archivo: ')
      
        print("almacenando ruta...")
        print("")
        CargarArchivo(ruta)
        Menu(ruta)
       
    elif opcion == "2":
        
        name = input('ingrese nombre del terreno: ')
        ProcesarArchivo(name,ruta)
       
    elif opcion == "3":
      
        ArchivoSalida(name)
        Menu(ruta)
       # archivo(ruta)
    elif opcion == "4":
       
       Estudiante(ruta)
    elif opcion == "5":
        
        Graficar(ruta)
    elif opcion  == "6":
        print('gracias, vuelva pronto')
        fin()
    else:
        print("Opcion inexistente")
        Menu(None)
        
def CargarArchivo(ruta):
    print("------------------------CARGANDO ARCHIVO-------------------------")
    print('-Extrayendo Datos...')
    print('')
    time.sleep(3)
    tree = ET.parse(ruta)
    root = tree.getroot()
    #print(root)
    
    for valores in root:
        #print(valores.tag)
        global listaDatos
        for elemento in valores:
            for dimensiones in elemento.iter('dimension'):#dimensionales
                for subelementodx in elemento.iter('m'):
                    dx=subelementodx.text
                for subelementody in elemento.iter('n'):
                    dy=subelementody.text
            for xy in elemento.iter('posicioninicio'):#coordenadas iniciales
                for subelementox in elemento.iter('x'):
                    a = subelementox.text
                for subelementoy in elemento.iter('y'):
                    b = subelementoy.text
            for yx in elemento.iter('posicionfin'):#coordenadas finales
                for subelementoxf in elemento.iter('x'):
                    c = subelementoxf.text
                for subelementoyf in elemento.iter('y'):
                    d = subelementoyf.text
                
            for datos in elemento.iter('posicion'):#datos del terreno
               # print(datos.text)
                listaDatos.Add(datos.attrib['x'], datos.attrib['y'], datos.text)
        ListaTerrenos.AddT(valores.attrib['nombre'], a,b,c,d,dx,dy, listaDatos)
        
        
    ListaTerrenos.mostrarT()
    
    print('Archivo cargado con exito!')
    time.sleep(3)
    Menu(ruta)
def ProcesarArchivo(nombre,ruta):
    print("------------------------PROCESANDO ARCHIVO-------------------------")
    print('-calculando la ruta')
    print('-calculando el combustible')
    print('')
    time.sleep(3)
    print(nombre)
    global listaDatos
    global combustible
   
    #terrenox= listageneral()
    terrenox = ListaTerrenos.EncontrarTerreno(nombre)
    dimensionx= terrenox.dimx
    dimensiony = terrenox.dimy
    print('----------------------------------------------')
    print('POSICION INICIAL:')
    actual= terrenox.matriz.BuscarCoordenada(terrenox.xi,terrenox.yi)
    print('('+actual.x+','+actual.y+')')
    actual.etiqueta.acumulado=actual.valor
    actual.etiqueta.anterior= None
    actual.etiqueta.terminal=True
    final= terrenox.matriz.BuscarCoordenada(terrenox.xf,terrenox.yf)
    print('POSICION FINAL:')
    print('('+final.x+', '+final.y+')')
    print("")
   # final.etiqueta.acumulado=final.valor
    #final.etiqueta.anterior= None
   # final.etiqueta.terminal=True
    gas =0
    
    while not final.etiqueta.terminal: 
        arx=int(actual.x)-1
        ary=int(actual.y)
        arriba = terrenox.matriz.BuscarCoordenada(str(arx),str(ary))
    
        abx=int(actual.x)+1
        aby=int(actual.y)
    
        abajo = terrenox.matriz.BuscarCoordenada(str(abx),str(aby))
        dx = int(actual.x)
        dy = int(actual.y)+1
        derecho = terrenox.matriz.BuscarCoordenada(str(dx),str(dy))
        ix = int(actual.x)
        iy = int(actual.y)-1
        izquierda = terrenox.matriz.BuscarCoordenada(str(ix),str(iy))
        if arriba is not None and not arriba.etiqueta.terminal:
            aux=0
            acumuladofa=0
            if arriba.etiqueta.acumulado==0:
                acumuladofa = int(actual.etiqueta.acumulado) + int(arriba.valor)
                terrenox.matriz.addE(arriba.x,arriba.y,acumuladofa,actual,arriba.etiqueta.repeticiones)
            else:
                aux=int(actual.etiqueta.acumulado) + int(arriba.valor)
                if(aux<arriba.etiqueta.acumulado):
                    terrenox.matriz.addE(arriba.x,arriba.y,aux,actual,arriba.etiqueta.repeticiones)
        if abajo is not None and not abajo.etiqueta.terminal:
            aux=0
            acumuladofb=0
            if abajo.etiqueta.acumulado==0:
                acumuladofb = int(actual.etiqueta.acumulado) + int(abajo.valor)
                terrenox.matriz.addE(abajo.x,abajo.y,acumuladofb,actual,abajo.etiqueta.repeticiones)
            else:
                aux=int(actual.etiqueta.acumulado) + int(abajo.valor)
                if(aux<abajo.etiqueta.acumulado):
                    terrenox.matriz.addE(abajo.x,abajo.y,aux,actual,abajo.etiqueta.repeticiones)
        if derecho is not None and not derecho.etiqueta.terminal:
            aux=0
            acumuladofc=0
            if derecho.etiqueta.acumulado==0:
                acumuladofc = int(actual.etiqueta.acumulado) + int(derecho.valor)
                terrenox.matriz.addE(derecho.x,derecho.y,acumuladofc,actual,derecho.etiqueta.repeticiones)
            else:
                aux=int(actual.etiqueta.acumulado) + int(derecho.valor)
                if(aux<derecho.etiqueta.acumulado):
                    terrenox.matriz.addE(derecho.x,derecho.y,aux,actual,derecho.etiqueta.repeticiones)
        if izquierda is not None and not izquierda.etiqueta.terminal:
            aux=0
            acumuladofd=0
            if izquierda.etiqueta.acumulado==0:
                acumuladofd = int(actual.etiqueta.acumulado) + int(izquierda.valor)
                terrenox.matriz.addE(izquierda.x,izquierda.y,acumuladofd,actual,izquierda.etiqueta.repeticiones)
            else:
                aux=int(actual.etiqueta.acumulado)+ int(izquierda.valor)
                if(aux<izquierda.etiqueta.acumulado):
                    terrenox.matriz.addE(izquierda.x,izquierda.y,aux,actual,izquierda.etiqueta.repeticiones)
        minimo = terrenox.matriz.Minimo(actual)
        actual = minimo
        if(actual.x==final.x and actual.y==final.y and actual.etiqueta.terminal):
            gas = actual.etiqueta.acumulado
            break
        gas= actual.etiqueta.acumulado
    final = terrenox.matriz.BuscarCoordenada(terrenox.xf,terrenox.yf)
    camino=final
    while camino is not None:
        #print('('+camino.x+','+camino.y+')')
        Ruta.Add(camino.x,camino.y,camino.valor)
        camino = camino.etiqueta.anterior
   

    
    #print('----------------------------\n')
  
  #  while camino is not None:
   #     for x in range(1,int(dimensionx),1):
    #        cadena =''
      #      for y in range(1,int(dimensiony),1):
       #         if(int(camino.x)==x and int(camino.y)==y):
         #           cadena=cadena+'|1'
          #      else:
            #        cadena=cadena+'|0'
              #  camino = camino.etiqueta.anterior
           # cadena=cadena+'|'
           # print(cadena)

   # Ruta.mostrarL()
    print('coordenadas de la ruta optima:')
    Ruta.invertir()
    Ruta.mostrarL()
    print('')
    print('reporte de la ruta optima:')
    Ruta.mostrar(dimensionx,dimensiony)
    Salida.AddX(terrenox.nombre ,terrenox.xi,terrenox.yi,terrenox.xf,terrenox.yf,dimensionx,dimensiony,Ruta)
    print('\n')
    print('Gasolina consumida durante la ruta: '+str(gas))
    combustible=gas
    print('----------------------------------------------')
    #listaDatos.reporte(Ruta,dimensionx,dimensiony)

    #print(arriba)
    #print(terrenox)
    time.sleep(3)
    Menu(ruta)   

def ArchivoSalida(nombre):
    global Salida
    global combustible
    S = Salida.EncontrarT(nombre)
    dimx=S.dimx
    dimy = S.dimy
    posix= S.xi
    posiy = S.yi
    posfx = S.xf
    posfy = S.yf

    print("------------------------Escribiendo archivo de salida-------------------------")
    ruta = input("Ingrese la ruta para guardar el archivo de salida: ")
    archivo = open(ruta + ".xml",'w')
    cadena = ''
    cadena=cadena+'<terreno nombre='+nombre+'>\n'
    cadena=cadena+'\t<posicioninicio>\n'
    cadena=cadena+'\t\t<x>'+posix+'</x>\n'
    cadena=cadena+'\t\t<y>'+posiy+'</y>\n'
    cadena=cadena+'\t</posicioninicio>\n'
    cadena=cadena+'\t<posicionfin>\n'
    cadena=cadena+'\t\t<x>'+posfx+'</x>\n'
    cadena=cadena+'\t\t<y>'+posfy+'</y>\n'
    cadena=cadena+'\t</posicionfin>\n'
    cadena=cadena+'\t<combustible>'+str(combustible)+'</combustible>\n'
    cadena=cadena+ Ruta.xml()
    cadena=cadena+'</terreno>'
    archivo.write(cadena)
    print('')
    print('archivo creado con exito!')
    


    #archivo.write('<terreno nombre={}>').format(nombre)
    #archivo.write('</terreno>')
    time.sleep(1)

    print("***¡Archivo guardado con exito!***")
def Estudiante(ruta):
    print('----------------------DATO DEL ESTUDIANTE---------------------')
    time.sleep(3)
    print('Daniel Alexander Barrera Figueroa')
    print('202004783')
    print('Introduccion a la programacion y computacion 2 SECCION "D" ')
    print('Ingenieria en Ciencias y Sistemas')
    print('4to semestre')
    print('--------------------------------------------------------------')
    time.sleep(3)
    Menu(ruta)
def Graficar(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
   

    numero_grafo = 1
    for grafos in root: 
        
        print(str(numero_grafo)+". "+grafos.attrib['nombre'])
        numero_grafo+=1
    grafoE= input("Ingrese nombre de la matriz a graficar: ")  
    print('NOMBRE DEL TERRENO: '+grafoE)
    contador=0
    for grafos in root:   
        contG=1 
        if grafoE == grafos.attrib['nombre']:
            with open("Grafica.dot", mode='w') as f:

                for dimensiones in grafos.iter('dimension'):
                    for filas in dimensiones.iter('m'):
                        n=int(filas.text)
                    for subelementody in dimensiones.iter('n'):
                        m=int(subelementody.text)
                f.write("digraph Figura {\n")
                f.write('label= "'+grafos.attrib['nombre']+'\nDIMENSIONES\n'+ 'M:'+str(m)+' N: '+str(n)+'"\n')
                #f.write('label1= "DIMENSIONES"\n')
                #f.write('label2= M: "'+m+' N: '+n+'"\n')
                f.write('node[shape=box fillcolor="#FFEDBB" ]')
                f.write("rankdir=UD\n")
              
                #f.write('edge[dir = "both"]')
                f.write('bgcolor = "#009900"\n') 
               
                
                
              
                
                for ele in grafos.iter('posicion'):
                   
                    f.write('valor' + str(contG) + '[ label ="' + ele.text + '",shape=box,style =filled,fillcolor=yellow];\n')


                    if contG<= m:
                        
                        f.write('valor' + str(contG) + '->valor' + str(contG + m) + ';\n')
                    elif contG > m and contG <= (m * n) - m:
                        
                        f.write(' valor' + str(contG) + '->valor' + str(contG + m) + ';\n')
                    elif contG == (m * n) - m:
                        break

                    contG = contG + 1
                

                   
                
                f.write("}\n")
                f.close()

                os.system('dot -Tpdf Grafica.dot -o reporte.pdf')
                os.system('reporte.pdf')
    #time.sleep(3)
    Menu(ruta)
def fin():
    sys.exit()

Menu(None)