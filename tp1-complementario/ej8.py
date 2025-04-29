"""
Ejercicio 8
Evaluar si dos N° solicitados por consola, son iguales, o en caso contrario identificar si 
el primero es mayor o menor que el segundo.
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 == num2:
    print("Los numeros son iguales")
elif num1 > num2:
    print("El primer numero es mayor que el segundo")
else:
    print("El primer numero es menor que el segundo")