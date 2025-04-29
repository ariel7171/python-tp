"""
Ejercicio 4
Calcular el perímetro y área de un rectángulo, ingresar los datos por consola.
"""

ladoA = float(input("Ingrese el lado A del rectangulo: "))
ladoB = float(input("Ingrese el lado B del rectangulo: "))

perimetro = 2 * (ladoA + ladoB)
area = ladoA * ladoB

print("El perimetro del rectangulo es: " + str(perimetro))
print("El area del rectangulo es: " + str(area))