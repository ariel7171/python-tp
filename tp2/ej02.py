# Ejercicio 2
# Generar una matriz de 3x3 con los números del 1 al 9 usando comprensión de listas anidadas. 
# Resultado esperado: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([[i + j for j in range(1, 4)] for i in range(0, 9, 3)])
