"""
Ejercicio 3
Usar reduce (de functools) y lambda para calcular la suma de todos los números de una lista.
#Ejemplo numeros = [3, 7, 1, 9, 4]
#salida esperada 24
"""

from functools import reduce

numeros = [3, 7, 1, 9, 4]

print(reduce(lambda x, y: x + y, numeros))
