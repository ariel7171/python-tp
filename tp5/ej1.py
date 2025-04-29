"""
Ejercicio 1
Dada una lista de palabras, usar filter y lambda para quedarse solo con aquellas cuya longitud sea 
mayor o igual a 5 caracteres. 
#Ejemplo 
#palabras = ["sol", "estrella", "luna", "universo", "mar"] 
#salida esperada ["estrella", "universo"]
"""

palabras = ["sol", "estrella", "luna", "universo", "mar"]

print(list(filter(lambda palabra: len(palabra) >= 5, palabras)))
