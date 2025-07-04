import tkinter as tk
from tkinter import ttk
import joblib
import numpy as np
import pandas as pd

class DiabetesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Predicción de Diabetes")
        self.root.geometry("500x500")
        
        # Cargar modelo y escalador
        self.modelo = joblib.load('mejor_modelo_diabetes.pkl')
        self.escalador = joblib.load('escalador_diabetes.pkl')
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Título
        ttk.Label(self.root, text="Predicción de Diabetes", font=("Arial", 16)).pack(pady=10)
        
        # Campos de entrada
        self.campos = [
            ("Embarazos (Pregnancies)", 0, 17),
            ("Glucosa (Glucose)", 0, 200),
            ("Presión Arterial (BloodPressure)", 0, 122),
            ("Espesor de Piel (SkinThickness)", 0, 99),
            ("Insulina (Insulin)", 0, 846),
            ("IMC (BMI)", 0.0, 67.1),
            ("Función de Pedigrí (DiabetesPedigreeFunction)", 0.078, 2.42),
            ("Edad (Age)", 21, 81)
        ]
        
        self.entradas = []
        
        for i, (texto, min_val, max_val) in enumerate(self.campos):
            frame = ttk.Frame(self.root)
            frame.pack(fill='x', padx=20, pady=5)
            
            ttk.Label(frame, text=texto, width=30).pack(side='left')
            
            if texto.startswith("IMC") or texto.startswith("Función"):
                # Campos decimales
                entrada = ttk.Entry(frame, width=15)
                entrada.pack(side='right', padx=5)
                self.entradas.append(entrada)
            else:
                # Campos enteros
                spin = ttk.Spinbox(frame, from_=min_val, to=max_val, width=10)
                spin.set(min_val)
                spin.pack(side='right', padx=5)
                self.entradas.append(spin)
        
        # Botón de predicción
        ttk.Button(self.root, text="Predecir", command=self.predecir).pack(pady=20)
        
        # Resultado
        self.resultado = ttk.Label(
            self.root, 
            text="Ingrese los datos y haga clic en Predecir", 
            font=("Arial", 12)
        )
        self.resultado.pack(pady=10)
        
        # Interpretación
        self.interpretacion = ttk.Label(
            self.root, 
            text="", 
            font=("Arial", 10),
            wraplength=450,
            justify='left'
        )
        self.interpretacion.pack(pady=10)
    
    def predecir(self):
        try:
            # Obtener valores
            valores = []
            for entrada in self.entradas:
                valor = entrada.get()
                if valor.replace('.', '', 1).isdigit():  # Comprobar si es número
                    valores.append(float(valor))
                else:
                    self.resultado.config(text="Error: Todos los valores deben ser números")
                    return
            
            # Convertir a array y escalar
            datos = np.array(valores).reshape(1, -1)
            datos_escalados = self.escalador.transform(datos)
            
            # Predecir
            prediccion = self.modelo.predict(datos_escalados)[0]
            probabilidad = self.modelo.predict_proba(datos_escalados)[0][1]
            
            # Mostrar resultado
            if prediccion == 1:
                self.resultado.config(text=f"Resultado: DIABETES (Probabilidad: {probabilidad*100:.1f}%)", foreground='red')
                self.interpretacion.config(text="El modelo predice que el paciente tiene diabetes. "
                                              "Se recomienda consultar con un médico para una evaluación más completa.")
            else:
                self.resultado.config(text=f"Resultado: NO DIABETES (Probabilidad: {probabilidad*100:.1f}%)", foreground='green')
                self.interpretacion.config(text="El modelo predice que el paciente no tiene diabetes. "
                                              "Mantener hábitos saludables para prevenir.")
        
        except Exception as e:
            self.resultado.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiabetesApp(root)
    root.mainloop()