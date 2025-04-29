# Ejercicio 5
# Crear una función mostrar_info_usuario que imprima 
# todos los datos que recibe. Utiliza *kwargs.

def mostrar_info_usuario(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_info_usuario(nombre="John Doe", edad=30, ciudad="New York")