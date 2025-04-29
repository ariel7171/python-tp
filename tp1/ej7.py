"""
Ejercicio 7 (usando for)
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números 
impares desde 1 hasta ese número separados por comas.
"""

NUMERO_INICIAL = 1

numeroIngresado = int(input("Ingrese un numero entero positivo: "))

for indice in range(NUMERO_INICIAL, numeroIngresado + 1):
    if indice % 2 != 0:
        print(indice, end=", ")