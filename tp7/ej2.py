"""
Ejercicio 2 - Radiobutton Crear una interfaz con tres controles de tipo Radiobutton etiquetados "Rojo", "Verde" y 
"Azul". Cuando el usuario seleccione uno de los botones, el color de fondo de la ventana 
debe cambiar al color correspondiente. 
Si la variable ventana1 representa la ventana principal (instancia de tk.Tk), podés usar el 
método .configure() para cambiar el fondo, indicando el color deseado mediante el 
parámetro bg.  
Por ejemplo: ventana1.configure(bg="red")   # para rojo
"""

import tkinter as tk

ventana1 = tk.Tk()
ventana1.title("Cambiar color de fondo")
ventana1.geometry("300x150")

color_fondo = tk.StringVar(value="white")

def cambiar_color():
    ventana1.configure(bg=color_fondo.get())

tk.Radiobutton(ventana1, text="Rojo", variable=color_fondo, value="red", command=cambiar_color).pack(anchor="w", padx=20, pady=5)
tk.Radiobutton(ventana1, text="Verde", variable=color_fondo, value="green", command=cambiar_color).pack(anchor="w", padx=20, pady=5)
tk.Radiobutton(ventana1, text="Azul", variable=color_fondo, value="blue", command=cambiar_color).pack(anchor="w", padx=20, pady=5)

ventana1.mainloop()