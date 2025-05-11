"""
Ejercicio 2 
Crear la siguiente jerarquía de clases para representar diferentes figuras geométricas 
utilizando herencia, clases abstractas y polimorfismo. 
1.  Clase Abstracta: Define una clase abstracta llamada FiguraGeometrica que 
contenga los siguientes métodos abstractos:  
○  area(self): devuelve el área de la figura. 
○  perimetro(self): devuelve el perímetro de la figura. 
 
2.  Clases Derivadas: 
 
○  Clase Circulo: Deriva de FiguraGeometrica e implementa los métodos area y 
perimetro. El constructor debe recibir el radio del círculo. 
○  Clase Rectangulo: Deriva de FiguraGeometrica e implementa los métodos 
area y perimetro. El constructor debe recibir la base y la altura del rectángulo. 
○  Clase Triangulo: Deriva de FiguraGeometrica e implementa los métodos 
area y perimetro. El constructor debe recibir los tres lados del triángulo. 
3.  Polimorfismo: Crea una lista de diversas figuras geométricas (por ejemplo, uno de 
cada tipo: Circulo, Rectangulo, Triangulo) y escribe un bucle que recorra la lista 
llamando a los métodos area y perimetro de cada figura, mostrando los resultados.
"""

from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Circulo de radio {self.radio}"


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"Rectangulo de base {self.base} y altura {self.altura}"


class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def __str__(self):
        return f"Triangulo de lados {self.lado1}, {self.lado2} y {self.lado3}"

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 4, 5)

figuras = [circulo, rectangulo, triangulo]

print("\nArea y perimetro de las figuras:")
for figura in figuras:
    print(f"\n{figura}")
    print(f"Area: {figura.area():.2f}")
    print(f"Perimetro: {figura.perimetro():.2f}")    