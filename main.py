from xml.dom import minidom
from help import Menu
from lectura import lectura
def main():
    txt_data = ""
    txt_intrucciones = ""
    opcion = Menu()
    lexico_intrucciones = None
    while opcion != 3 :
        if opcion == 1:
            archivo = str(input("Ingrese su ruta para el archivo:"))
            print("se ha cargado la direccion del archivo")
            #archivo ='C:/Users/carlo/Downloads/entrada.xml'
            
        elif opcion == 2:
            metodo=lectura.leer(archivo)
            print("Se ha analizado la informacion y creado los nodos")
        elif opcion == 3:
            print("Terminando el programa...")
        opcion = Menu();

if __name__ == "__main__":
    main()