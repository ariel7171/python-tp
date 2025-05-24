import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Gestión de Inventario")
ventana.geometry("600x400")

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill='both')

frame_formulario = ttk.Frame(notebook)
notebook.add(frame_formulario, text="Agregar Producto")

lf_datos = ttk.LabelFrame(frame_formulario, text="Datos del Producto")
lf_datos.pack(padx=10, pady=10, fill="x")

ttk.Label(lf_datos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre = ttk.Entry(lf_datos)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(lf_datos, text="Categoría:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
categorias = ["Alimentos", "Electrónica", "Ropa", "Limpieza"]
combo_categoria = ttk.Combobox(lf_datos, values=categorias, state="readonly")
combo_categoria.grid(row=1, column=1, padx=5, pady=5)
combo_categoria.set("Seleccionar")

ttk.Label(lf_datos, text="Precio:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_precio = ttk.Entry(lf_datos)
entry_precio.grid(row=2, column=1, padx=5, pady=5)

boton_agregar = ttk.Button(frame_formulario, text="Agregar al inventario")
boton_agregar.pack(pady=10)

frame_inventario = ttk.Frame(notebook)
notebook.add(frame_inventario, text="Inventario")

tree = ttk.Treeview(frame_inventario, columns=("Nombre", "Categoría", "Precio"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Categoría", text="Categoría")
tree.heading("Precio", text="Precio")
tree.pack(expand=True, fill="both", padx=10, pady=10)

def agregar_producto():
    nombre = entry_nombre.get()
    categoria = combo_categoria.get()
    precio = entry_precio.get()
    if nombre and categoria != "Seleccionar" and precio:
        tree.insert("", "end", values=(nombre, categoria, precio))
        entry_nombre.delete(0, tk.END)
        combo_categoria.set("Seleccionar")
        entry_precio.delete(0, tk.END)

boton_agregar.config(command=agregar_producto)

ventana.mainloop()
