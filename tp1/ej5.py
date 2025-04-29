"""
Ejercicio 5
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática 
el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar $400 y si es mayor de 18 años, $800
"""

EDAD_MINIMA = 4
EDAD_MAXIMA = 18
MONTO_MINIMO = 400
MONTO_MAXIMO = 800

edadIngresada = int(input("Ingrese su edad: "))

if edadIngresada < EDAD_MINIMA:
    print("Puede entrar gratis")
elif edadIngresada >= EDAD_MINIMA and edadIngresada <= EDAD_MAXIMA:
    print("Debe pagar $" + str(MONTO_MINIMO))
else:
    print("Debe pagar $" + str(MONTO_MAXIMO))
