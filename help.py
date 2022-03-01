from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import ForwardRef
import webbrowser
from io import open
def Menu():
    print("-----------------MENU ANALIZADOR------------------")
    print("\t --- Seleccione una opcion ---")
    print('\t       1. Cargar xml')
    print('\t       2. Cargar Intrucciones')
    print('\t       3. Analizar')
    print('\t       4. Obtener Grafica')
    print('\t       5. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida