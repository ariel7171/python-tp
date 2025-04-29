"""
Ejercicio 6
Calcular el perímetro y área de un triángulo, ingresar los datos por consola. Antes de realizar los cálculos, 
verificar que los datos corresponden a un triángulo.
"""

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

if base > 0 and altura > 0:
    perimetro = base + base + altura
    area = (base * altura) / 2

    print("El perimetro del triangulo es: " + str(perimetro))
    print("El area del triangulo es: " + str(area))
else:
    print("Los datos ingresados no corresponden a un triangulo")