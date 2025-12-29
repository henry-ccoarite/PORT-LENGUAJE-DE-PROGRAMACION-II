import math
import tkinter as tk
from tkinter import messagebox

def calcular_hipotenusa():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser números positivos")

        hip = math.sqrt(a**2 + b**2)
        label_resultado.config(text=f"Hipotenusa: {hip:.2f}")

    except ValueError as ve:
        messagebox.showerror("Error de valor", str(ve))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))


# ----------------- INTERFAZ -----------------
ventana = tk.Tk()
ventana.title("Calculadora de Hipotenusa")
ventana.geometry("380x280")
ventana.config(bg="#1e1e1e")

# Título
titulo = tk.Label(
    ventana, 
    text="Cálculo de Hipotenusa",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="#7dcfff"
)
titulo.pack(pady=12)

# Frame para inputs
frame = tk.Frame(ventana, bg="#1e1e1e")
frame.pack(pady=10)

# Input A
label_a = tk.Label(frame, text="Cateto A:", font=("Arial", 12), bg="#1e1e1e", fg="white")
label_a.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_a = tk.Entry(frame, font=("Arial", 12), width=12)
entry_a.grid(row=0, column=1, pady=5)

# Input B
label_b = tk.Label(frame, text="Cateto B:", font=("Arial", 12), bg="#1e1e1e", fg="white")
label_b.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_b = tk.Entry(frame, font=("Arial", 12), width=12)
entry_b.grid(row=1, column=1, pady=5)

# Botón
boton = tk.Button(
    ventana,
    text="Calcular Hipotenusa",
    font=("Arial", 12, "bold"),
    bg="#61afef",
    fg="black",
    width=20,
    command=calcular_hipotenusa
)
boton.pack(pady=15)

# Resultado
label_resultado = tk.Label(
    ventana,
    text="Hipotenusa: ",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="#98c379"
)
label_resultado.pack(pady=10)

ventana.mainloop()
