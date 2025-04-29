"""
Ejercicio 3
Se necesita elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco,
correspondientes a un postulante, y muestre su puntaje final considerando que por cada respuesta correcta
tendrá 3 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.
"""

NUMERO_RESPUESTAS_CORRECTAS = 3
NUMERO_RESPUESTAS_INCORRECTAS = -1
NUMERO_RESPUESTAS_EN_BLANCO = 0

respuestasCorrectas = int(input("Ingrese el numero de respuestas correctas: "))
respuestasIncorrectas = int(input("Ingrese el numero de respuestas incorrectas: "))
respuestasEnBlanco = int(input("Ingrese el numero de respuestas en blanco: "))

puntajeFinal = (
    NUMERO_RESPUESTAS_CORRECTAS * respuestasCorrectas
    + NUMERO_RESPUESTAS_INCORRECTAS * respuestasIncorrectas
    + NUMERO_RESPUESTAS_EN_BLANCO * respuestasEnBlanco
)

print("El puntaje final es de: " + str(puntajeFinal))