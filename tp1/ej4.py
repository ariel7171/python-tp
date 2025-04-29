# Ejercicio 4
# Pedir una cadena y dos índices (inicio y fin), y mostrar la subcadena que se encuentra 
# entre esos índices.

cadenaIngresada = input("Ingrese una cadena de texto: ")
inicio = int(input("Ingrese el inicio: "))
fin = int(input("Ingrese el fin: "))

print(cadenaIngresada[inicio:fin])