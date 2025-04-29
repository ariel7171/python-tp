"""
Ejercicio 11
Idem al ejercicio 10, pero simulando match con un diccionario.
"""

diccionario = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}

diaDeLaSemana = int(input("Ingrese un número del 1 al 7: "))

print(diccionario[diaDeLaSemana])