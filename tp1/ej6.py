"""
Ejercicio 6
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

INGREDIENTES_VEGETARIANOS = ["pimiento", "tofu"]
INGREDIENTES_NO_VEGETARIANOS = ["peperoni", "jamon", "salmon"]

tipoDePizzaIngresada = int(
    input(
        "Ingrese 1 si quiere una pizza vegetariana o 2 si quiere una no vegetariana: "
    )
)

if tipoDePizzaIngresada == 1:
    print("Los ingredientes disponibles son: " + ", ".join(INGREDIENTES_VEGETARIANOS))
else:
    print(
        "Los ingredientes disponibles son: " + ", ".join(INGREDIENTES_NO_VEGETARIANOS)
    )

ingredienteIngresado = input("Ingrese el ingrediente que desea: ")

if ingredienteIngresado not in INGREDIENTES_VEGETARIANOS + INGREDIENTES_NO_VEGETARIANOS:
    print("El ingrediente ingresado no es valido")
    exit()

print(
    "La pizza elegida es vegetariana"
    if tipoDePizzaIngresada == 1
    else "La pizza elegida es no vegetariana"
)
print(
    "Los ingredientes que lleva son: " + "mozzarella, tomate y " + ingredienteIngresado
)
