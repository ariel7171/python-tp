"""
Ejercicio 1 - Entry, Radiobutton, button Disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles 
Radiobutton permitir seleccionar si queremos sumarlos o restarlos. Al presionar un botón 
mostrar el resultado de la operación seleccionada.
"""

import tkinter as tk

ventana = tk.Tk()
ventana.title("Suma o Resta")

num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()
operacion = tk.IntVar(value=1)  

tk.Label(ventana, text="Ingrese primer valor:").grid(row=0, column=0, padx=3, pady=3)
tk.Entry(ventana, textvariable=num1, width=10).grid(row=0, column=1, padx=3, pady=3)

tk.Label(ventana, text="Ingrese segundo valor:").grid(row=1, column=0, padx=3, pady=3)
tk.Entry(ventana, textvariable=num2, width=10).grid(row=1, column=1, padx=3, pady=3)

tk.Radiobutton(ventana, text="Sumar", variable=operacion, value=1).grid(row=2, column=1, padx=3, pady=3)
tk.Radiobutton(ventana, text="Restar", variable=operacion, value=2).grid(row=3, column=1, padx=3, pady=3)

tk.Button(ventana, text="Operar", command=lambda: calcular()).grid(row=4, column=1, columnspan=1, pady=5)
tk.Label(ventana, textvariable=resultado, font=("Arial", 12)).grid(row=5, column=1, columnspan=1)

def calcular():
    try:
        n1 = int(num1.get())
        n2 = int(num2.get())
        op = operacion.get()
        
        if op == 1:
            res = n1 + n2
        else:
            res = n1 - n2
        
        resultado.set(res)
    except ValueError:
        resultado.set("Error: Ingrese números")

ventana.mainloop()
