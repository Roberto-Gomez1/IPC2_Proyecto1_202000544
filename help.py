from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import ForwardRef
import webbrowser
from io import open
def Menu():
    print("-----------------MENU ANALIZADOR------------------")
    print("\t --- Seleccione una opcion ---")
    print('\t       1. Cargar coordenadas')
    print('\t       2. Analizar XML')
    print('\t       3. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida