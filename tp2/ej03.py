# Ejercicio 3
# Implementar una función que reciba una cadena que indique el día de la semana y 
# devuelva si es “Laboral”, “Fin de semana” o “No válido”. Usar match.

def dia_semana(dia):
    match dia:
        case "lunes":
            return "Laboral"
        case "martes":
            return "Laboral"
        case "miercoles":
            return "Laboral"
        case "jueves":
            return "Laboral"
        case "viernes":
            return "Laboral"
        case "sabado":
            return "Fin de semana"
        case "domingo":
            return "Fin de semana"
        case _:
            return "No valido"

print(dia_semana("domingo"))