"""
Ejercicio 9 (usando for)
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""

numeroIngresado = int(input("Ingrese un numero entero: "))

for i in range(1, numeroIngresado + 1):
    print("*" * i)