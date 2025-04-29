# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10, 
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# donde “n” es el número introducido, y la muestre por pantalla. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os

def ejercicio1():
    try:
        num = int(input("Ingrese un número entero entre 1 y 10: "))
        if num < 1 or num > 10:
            print("El número debe estar entre 1 y 10")
            return
        if not os.path.exists(f"tabla-{num}.txt"):
            print(f"El fichero tabla-{num}.txt no existe")
            return
        with open(f"tabla-{num}.txt", "r") as f:
            print(f.read())
    except ValueError:
        print("Debe ingresar un número entero")

ejercicio1()