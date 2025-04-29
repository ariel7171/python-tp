"""
Ejercicio 7
Calcular el perímetro y área de un círculo. Tener en cuenta que PI es una constante.
"""

import math

radio = float(input("Ingrese el radio del circulo: "))

perimetro = 2 * math.pi * radio
area = math.pi * radio**2

print("El perimetro del circulo es: " + str(perimetro))
print("El area del circulo es: " + str(area))
