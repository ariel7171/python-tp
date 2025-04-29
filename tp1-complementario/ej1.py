"""
Ejercicio 1 
Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad constante (m/s) durante 
un tiempo t (s), considerar que es un MRU (Movimiento Rectilíneo Uniforme) 𝑫 = 𝑽 𝒙 𝑻 
"""

velocidad = float(input("Ingrese la velocidad del movimiento: "))
tiempo = float(input("Ingrese el tiempo del movimiento: "))

distanciaRecorrida = velocidad * tiempo

print("La distancia recorrida es de: " + str(distanciaRecorrida))