# Ejercicio 6
# Dadas dos listas del mismo tamaño, usá zip para obtener una lista con la suma 
# de los elementos correspondientes. 
# lista1 = [1, 2, 3] 
# lista2 = [4, 5, 6] 
# Resultado esperado: [5, 7, 9]
# mi_dict = {i:j for i,j in zip(claves, valores)}

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print([i + j for i, j in zip(lista1, lista2)])