"""
Ejercicio 4- Listbox
Disponer un Listbox con una serie de nombres de frutas. 
Permitir la selección de varias frutas. 
Cuando se presione un botón recuperar todas las frutas seleccionadas y mostrarlas en una Label.
"""

import tkinter as tk
from tkinter import messagebox

def mostrar_seleccion():
    seleccionados = []
    for i in listbox.curselection():
        seleccionados.append(listbox.get(i))
    label_resultado.config(text="Frutas seleccionadas: " + ", ".join(seleccionados))

ventana = tk.Tk()
ventana.title("Ejercicio 4 - Listbox")

listbox = tk.Listbox(ventana, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

frutas = ["Manzana", "Banana", "Naranja", "Uva", "Pera", "Mango"]
for fruta in frutas:
    listbox.insert(tk.END, fruta)

boton = tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack(pady=5)

label_resultado = tk.Label(ventana, text="Frutas seleccionadas: ")
label_resultado.pack(pady=10)

ventana.mainloop()
