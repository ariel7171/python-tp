"""
Ejercicio 9
Determinar si el alumno está Promocionado (nota mayor o igual a 80), Regular (nota mayor o igual a 60 PERO menor que 80) 
o Desaprobado (nota menor a 60)
"""

nota = int(input("Ingrese la nota: "))

if nota >= 80:
    print("Promocionado")
elif nota >= 60:
    print("Regular")
else:
    print("Desaprobado")