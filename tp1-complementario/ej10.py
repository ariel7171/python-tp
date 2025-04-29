"""
Ejercicio 10
Ingresar por teclado un número entre 1 y 7, mostrar a qué día de la semana corresponde el número ingresado. 
Por ejemplo, si ingresa 1, muestra DOMINGO.
Usar match. 
"""

diaDeLaSemana = int(input("Ingrese un número del 1 al 7: "))

match diaDeLaSemana:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")