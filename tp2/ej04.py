# Ejercicio 4
# Dado un diccionario que representa un cliente con posibles claves "nombre", "edad" y "profesion". 
# para identificar si:
# ● Es mayor de edad (edad >= 18)
# ● Es menor
# ● No se indica la edad crear la función clasificar_cliente(cliente) 
# Ejemplo: {"nombre": "Ana", "edad": 17} → "Menor de edad" 
# {"nombre": "Carlos", "edad": 21, "profesion": "médico"} → "Mayor de edad" 
# {"nombre": "Lucía"} → "Edad no especificada"

def clasificar_cliente(cliente):
    if "edad" in cliente:
        if cliente["edad"] >= 18:
            return "Mayor de edad"
        else:
            return "Menor de edad"
    else:
        return "Edad no especificada"

cliente1 = {"nombre": "Ana", "edad": 17}
cliente2 = {"nombre": "Carlos", "edad": 21, "profesion": "médico"}
cliente3 = {"nombre": "Lucía"}

print(clasificar_cliente(cliente1))
print(clasificar_cliente(cliente2)) 
print(clasificar_cliente(cliente3))