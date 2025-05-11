
class Paciente:
    def __init__(self, id=None, nombre=None, edad=None, peso_actual=None):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.peso_actual = peso_actual
    
    def __str__(self):
        return f"Paciente {self.id}: {self.nombre}, {self.edad} años, {self.peso_actual}kg"
    
class Alimento:
    def __init__(self, id=None, nombre=None, calorias=None):
        self.id = id
        self.nombre = nombre
        self.calorias = calorias
    
    def __str__(self):
        return f"Alimento {self.id}: {self.nombre}, {self.calorias} calorías"

class PlanComida:
    def __init__(self, id=None, paciente_id=None, alimento_id=None, fecha=None, cantidad=None):
        self.id = id
        self.paciente_id = paciente_id
        self.alimento_id = alimento_id
        self.fecha = fecha
        self.cantidad = cantidad
    
    def __str__(self):
        return f"Plan {self.id}: Paciente {self.paciente_id}, Alimento {self.alimento_id}, Fecha {self.fecha}, Cantidad {self.cantidad}"

