# Ejercicio 6
# Crear una función operar_lista(lista, operacion) que reciba una lista de números 
# y una función que defina qué operación aplicar sobre la lista (suma o multipliacr sus elementos). 
# La idea es practicar pasar funciones por parámetro.

import math

def operar_lista(lista, operacion):
    return operacion(lista)

print(operar_lista([1, 2, 3], sum))
print(operar_lista([1, 2, 3], max))
print(operar_lista([1, 2, 3], min))
print (operar_lista([1, 2, 3], math.prod))