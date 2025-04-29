"""
Ejercicio 12 (usando while)
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba “salir” que terminará.
"""

palabraIngresada = input("Ingrese una palabra: ")

while palabraIngresada != "salir":
    print(palabraIngresada)
    palabraIngresada = input("Ingrese una palabra: ")