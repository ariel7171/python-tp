"""
Ejercicio 2
Cree una función que reciba dos parámetros: (x, y) y retorne la suma de ambos parámetros. 
Cree una tupla de números (1, 2,3,4) Utilice la función reduce para que se sumen todos los elementos. 
#Ejemplo tupla= (1, 2,3,4) 
#salida esperada 10
"""

from functools import reduce

tupla = (1, 2, 3, 4)

print(reduce(lambda x, y: x + y, tupla))