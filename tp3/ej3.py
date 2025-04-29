# Ejercicio 3
# Crear una función sumar_todo que acepte cualquier 
# cantidad de números y retorne la suma.

def sumar_todo(*args):
    return sum(args)

print(sumar_todo(1, 2, 3, 4, 5))