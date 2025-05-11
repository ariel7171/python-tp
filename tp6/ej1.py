"""
Ejercicio 1 
Crear una clase Guerrero que sea reciba como atributos: 
●  Nombre del guerrero. 
●  Vida del guerrero. 
●  Ataque del guerrero. 
●  Arma. 
 
Como métodos deberá tener: 
●  __str__. 
●  Atacar. 
●  Mejorar arma. (Deberá mejorar la categoría del arma) 
 
El atributo Arma será otra clase que tendrá los siguientes atributos: 
●  Tipo de arma. 
●  Ataque del arma. 
●  Categoria del arma. 
 
y la clase Arma tendrá los siguientes métodos: 
●  __str__. 
●  Mejorar categoria. (Deberá aumentar el daño del arma) 
 
Una vez creadas ambas clases, deberá crear dos guerreros, uno será “John Snow” y el 
otro será un “caminante blanco” y deberá hacer que “John Snow” ataqué al caminante 
blanco.
"""

class Arma:
    def __init__(self, tipo: str, ataque: int, categoria: int):
        self.tipo = tipo
        self.ataque = ataque
        self.categoria = categoria

    def __str__(self):
        return f"Arma {self.tipo}: {self.ataque} de ataque, {self.categoria} de categoria"

    def mejorarcategoria(self):
        self.categoria += 1
        self.ataque += self.categoria

class Guerrero:
    def __init__(self, nombre: str, vida: int, ataque: int, arma: Arma):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.arma = arma

    def __str__(self):
        return f"Guerrero {self.nombre}: {self.vida} de vida, {self.ataque} de ataque, {self.arma}"

    def atacar(self, guerrero):
        guerrero.vida -= self.ataque + self.arma.ataque

    def mejorarama(self):
        self.arma.mejorarcategoria()


john_snow = Guerrero("John Snow", 100, 1, Arma("Espada", 1, 1))
caminante_blanco = Guerrero("Caminante blanco", 100, 1, Arma("Espada", 1, 1))

john_snow.atacar(caminante_blanco)

print(john_snow)
print(caminante_blanco)

john_snow.mejorarama()

john_snow.atacar(caminante_blanco)

print(john_snow)
print(caminante_blanco)