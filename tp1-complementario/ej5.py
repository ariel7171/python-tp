"""
Ejercicio 5
Calcular el perímetro y área de un triángulo, ingresar los datos por consola.
"""

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

perimetro = base + base + altura
area = (base * altura) / 2

print("El perimetro del triangulo es: " + str(perimetro))
print("El area del triangulo es: " + str(area))