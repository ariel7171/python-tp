"""
Ejercicio 3 - Checkbutton - Button 
Diseñar una interfaz que incluya un Checkbutton con el siguiente mensaje:  "¿Está de acuerdo con los términos y condiciones?" 
También debe incluirse un botón que, inicialmente, esté deshabilitado. 
Cuando el usuario marque (tilde) el Checkbutton, el botón debe activarse automáticamente. 
Si se desmarca, el botón debe volver a desactivarse.
"""

import tkinter as tk

ventana = tk.Tk()
ventana.title("Aceptación de Términos")
ventana.geometry("400x150")

acepta = tk.BooleanVar()

def actualizar_estado():
    if acepta.get():  
        boton_aceptar.config(state="normal")
    else:
        boton_aceptar.config(state="disabled")

check = tk.Checkbutton(
    ventana,
    text="¿Está de acuerdo con los términos y condiciones?",
    variable=acepta,
    command=actualizar_estado
)
check.pack(pady=20)

boton_aceptar = tk.Button(ventana, text="Aceptar", state="disabled")
boton_aceptar.pack()

ventana.mainloop()