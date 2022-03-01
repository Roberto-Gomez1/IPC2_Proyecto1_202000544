from xml.dom import minidom
from help import Menu
from lectura import lectura
def main():
    txt_data = ""
    txt_intrucciones = ""
    opcion = Menu()
    lexico_intrucciones = None
    while opcion != 5 :
        if opcion == 1:
            #archivo = str(input("Ingrese su opcion:"))
            archivo ='C:/Users/carlo/Downloads/entrada.xml'
            metodo=lectura.leer(archivo)
        #elif opcion == 2:
        #elif opcion == 3:
        #elif opcion ==4:
        #elif opcion == 5:
            print("Terminando el programa...")
        opcion = Menu();

if __name__ == "__main__":
    main()