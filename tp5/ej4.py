"""
Ejercicio 4
Filtrar solo los números pares.
Multiplicar cada uno por sí mismo (elevar al cuadrado).
Reducir la lista resultante para obtener el producto de todos sus elementos. 
#Ejemplo 
nums = [2, 3, 4, 5, 6] 
Pares → [2, 4, 6] 
Cuadrados → [4, 16, 36] 
Producto → 4 * 16 * 36 = 2304 
salida esperada 2304
"""

from functools import reduce

nums = [2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, nums))
cuadrados = list(map(lambda x: x ** 2, pares))
producto = reduce(lambda x, y: x * y, cuadrados)

print("Numeros: ", nums)
print("Pares: ", pares)
print("Cuadrados: ", cuadrados)
print("Producto: ", producto)