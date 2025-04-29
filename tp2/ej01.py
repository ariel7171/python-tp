# Ejercicio 1
# A partir de una lista de palabras, creá una lista con aquellas que tengan más de 4 letras, 
# usando comprensión de listas. palabras = ["sol", "luna", "mar", "montaña", "río", "estrella"] 
# Resultado esperado: ["montaña", "estrella"]

palabras = ["sol", "luna", "mar", "montaña", "río", "estrella"]

print([palabra for palabra in palabras if len(palabra) > 4])