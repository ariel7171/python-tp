# Ejercicio 5
# Dada una lista de palabras, usá enumerate para obtener una lista con los índices 
# de las palabras que tienen más de 5 letras.
# palabras = ["hola", "murciélago", "sol", "universo"] 
# Resultado esperado: [1, 3]

palabras = ["hola", "murciélago", "sol", "universo"]

nueva_lista = [indice for indice, palabra in enumerate(palabras) if len(palabra) > 5]
print(nueva_lista)



        

#print([i for i, palabra in enumerate(palabras) if len(palabra) > 5])