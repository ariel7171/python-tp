"""
Ejercicio 3 
Extiende el programa anterior que implementa figuras geométricas con los siguientes 
requisitos: 
Clase FiguraBidimensional: Crea una nueva clase llamada FiguraBidimensional que Esta 
clase debe contener un método clonar(self) que devuelve una copia de la instancia (puedes 
usar copy para realizar la clonación).  
Clase FiguraTridimensional: Crea una clase diferente llamada FiguraTridimensional, que 
debe incluir un método calcular_volumen(self) que deberá ser implementado por las clases 
derivadas que representen figuras tridimensionales.  
Crear la clase Derivada Cubo: Crea una nueva clase llamada Cubo que derive de 
FiguraGeometrica FiguraBidimensional, FiguraTridimensional. Esta clase debe tener un 
constructor que acepte el lado del cubo. 
Modificar la clase Circulo para que herede ahora también de FiguraBidimensional.
"""
from abc import ABC, abstractmethod
from tp7.ej2 import FiguraGeometrica
import math
import copy

class FiguraBidimensional(ABC):
    def clonar(self):
        return copy.deepcopy(self)


class FiguraTridimensional(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass

class Circulo(FiguraGeometrica, FiguraBidimensional):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Circulo de radio {self.radio}"

class Cubo(FiguraGeometrica, FiguraBidimensional, FiguraTridimensional):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return 6 * self.lado ** 2
    
    def perimetro(self):
        return 12 * self.lado
    
    def calcular_volumen(self):
        return self.lado ** 3
    
    def __str__(self):
        return f"Cubo de lado {self.lado}"

circulo = Circulo(5)
cubo = Cubo(3)

print(f"\n{circulo}")
print(f"Area: {circulo.area():.2f}")
print(f"Perímetro: {circulo.perimetro():.2f}")
    
circulo_copia = circulo.clonar()
circulo_copia.radio += 2

print(f"\nCirculo copia modificada: {circulo_copia}")
print(f"Area: {circulo_copia.area():.2f}")
print(f"Perímetro: {circulo_copia.perimetro():.2f}")

print(f"\n{cubo}")
print(f"Area: {cubo.area():.2f}")
print(f"Perimetro: {cubo.perimetro():.2f}")
print(f"Volumen: {cubo.calcular_volumen():.2f}")

cubo_copia = cubo.clonar()
cubo_copia.lado += 2

print(f"\nCubo copia modificada: {cubo_copia}")
print(f"Area: {cubo_copia.area():.2f}")
print(f"Perimetro: {cubo_copia.perimetro():.2f}")
print(f"Volumen: {cubo_copia.calcular_volumen():.2f}")