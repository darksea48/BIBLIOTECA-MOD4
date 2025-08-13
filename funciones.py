import os

ARCHIVO = "biblioteca.txt"

# Funciones
def limpiar_pantalla():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux, macOS
        os.system('clear')

def cargar_datos(archivo: str):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            lineas = [linea.strip() for linea in lineas]
            return lineas
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error al abrir el archivo")
        
def guardar_datos(archivo: str, datos: list):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            for dato in datos:
                f.write(f"{dato}")
                if dato != datos[-1]:
                    f.write('\n')
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error al abrir el archivo")

def agregar_dato(archivo: str, dato: str):
    datos = cargar_datos(archivo)
    datos.append(dato)
    guardar_datos(archivo, datos)