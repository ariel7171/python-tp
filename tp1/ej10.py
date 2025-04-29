"""
Ejercicio 10 (usando for)
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
letras de la palabra introducida empezando por la última.
"""

palabraIngresada = input("Ingrese una palabra: ")

for i in range(len(palabraIngresada) - 1, -1, -1):
    print(palabraIngresada[i], end=", ")