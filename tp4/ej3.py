"""
Ejercicio 3
Escribir un programa para gestionar una agenda telefónica con los nombres y los teléfonos de los clientes de una empresa.
El programa incluir las funciones: ● def busca_contacto(archivo, cliente):
Función que devuelve el teléfono de un cliente de un fichero dado.
Parámetros:
archivo: Es un fichero con los nombres y teléfonos de clientes.
cliente: Es una cadena con el nombre del cliente.
Devuelve: El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o el fichero no existe.
● def agrega_contacto(archivo, cliente, telf):
Función que añade el teléfono de un cliente de un fichero dado.
Parámetros:
file: Es un fichero con los nombres y teléfonos de clientes.
cliente: Es una cadena con el nombre del cliente.
telf: Es una cadena con el teléfono del cliente.
Devuelve:
Un mensaje informando sobre si el teléfono se ha añadido o ha habido algún problema.
● def elimina_contacto(archivo, cliente):
Función que elimina el teléfono de un fichero dado.
Parámetros:
file: Es un fichero con los nombres y teléfonos de contacto.
cliente: Es una cadena con el nombre del contacto.
Devuelve:
Un mensaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
● def crea_directorio(archivo):
Función que crea un fichero vacío para guardar una agenda telefónica.
Parámetros:
archivo: Es un fichero.
Devuelve:
Un mensaje informando sobre si el fichero se ha creado correctamente o no.
● def menu():
Función que presenta un menú con las operaciones disponibles y devuelve la opción seleccionada por el usuario.
Devuelve:
La opción seleccionada por el usuario.
● def Principal():
Función que lanza la aplicación
●
Crear el fichero con una agenda telefónica si no existe, para consultar el teléfono de un cliente,
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. La agenda debe estar guardada
en el fichero de texto agenda.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas
y cada cliente en una línea distinta.
"""

import os


def menu():
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Eliminar contacto")
    print("4. Crear agenda")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion


def busca_contacto(archivo, cliente):
    with open(archivo, "r") as f:
        for linea in f:
            contacto = linea.split(",")
            if contacto[0] == cliente:
                return contacto[1]
        return "El contacto no existe"


def agrega_contacto(archivo, cliente, telf):
    with open(archivo, "a") as f:
        f.write(f"{cliente},{telf}\n")
        return "Contacto agregado"


def elimina_contacto(archivo, cliente):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    with open(archivo, "w") as f:
        for linea in lineas:
            contacto = linea.split(",")
            if contacto[0] != cliente:
                f.write(linea)
        return "Contacto eliminado"


def crea_directorio(archivo):
    if os.path.exists(archivo):
        return "El fichero ya existe"
    else:
        with open(archivo, "w") as f:
            return "Fichero creado"


def principal():
    agenda = "tp4/agenda.txt"
    while True:
        opcion = menu()
        if opcion == 1:
            cliente = input("Ingrese el nombre del contacto: ")
            print(busca_contacto(agenda, cliente))
        elif opcion == 2:
            cliente = input("Ingrese el nombre del contacto: ")
            telf = input("Ingrese el telefono del contacto: ")
            print(agrega_contacto(agenda, cliente, telf))
        elif opcion == 3:
            cliente = input("Ingrese el nombre del contacto: ")
            print(elimina_contacto(agenda, cliente))
        elif opcion == 4:
            print(crea_directorio(agenda))
        elif opcion == 5:
            break

principal()