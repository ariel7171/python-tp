# Ejercicio 2
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os

def chequearRango(num):
    return num < 1 or num > 10

def ejercicio2():
    try:
        num1 = int(input("Ingrese un numero entero entre 1 y 10: "))
        num2 = int(input("Ingrese un numero entero entre 1 y 10: "))
        if chequearRango(num1) or chequearRango(num2):
            print("El número debe estar entre 1 y 10")
            return
        if not os.path.exists(f"tabla-{num1}.txt"):
            print(f"El fichero tabla-{num1}.txt no existe")
            return
        with open(f"tabla-{num1}.txt", "r") as f:
            print(f.readlines()[num2+1])
    except ValueError:
        print("Debe ingresar dos numeros enteros")

ejercicio2()