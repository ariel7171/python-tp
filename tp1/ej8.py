"""
Ejercicio 8 (usando for)
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.
"""

numeroIngresado = int(input("Ingrese un numero entero positivo: "))

for indice in range(numeroIngresado, -1, -1):
    print(indice, end=", ")