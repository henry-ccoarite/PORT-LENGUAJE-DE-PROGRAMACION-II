import tkinter as tk
from typing import TypeVar

T = TypeVar('T', int, float)

class CalculadoraFactorial:
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def calcular():
    texto_resultado.config(state="normal")
    try:
        n = int(entry_numero.get())
        cal = CalculadoraFactorial(n)
        resultado = cal.calcular_factorial()
        # Insertar el resultado al final sin borrar lo anterior
        texto_resultado.insert(tk.END, f"El factorial de {n} es: {resultado}\n")
    except ValueError as ve:
        texto_resultado.insert(tk.END, f"Error: {ve}\n")
    texto_resultado.config(state="disabled")

ventana = tk.Tk()
ventana.title("Calculadora de Factorial")
ventana.geometry("450x300")
ventana.config(bg="#1e1e1e")

titulo = tk.Label(
    ventana,
    text="Calculadora de Factorial",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="#7dcfff"
)
titulo.pack(pady=10)

frame = tk.Frame(ventana, bg="#1e1e1e")
frame.pack(pady=5)

label_num = tk.Label(
    frame,
    text="Ingrese un número:",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
label_num.grid(row=0, column=0, padx=10, pady=5)

entry_numero = tk.Entry(frame, font=("Arial", 12), width=10)
entry_numero.grid(row=0, column=1, pady=5)

boton = tk.Button(
    ventana,
    text="Calcular Factorial",
    font=("Arial", 12, "bold"),
    bg="#61afef",
    fg="black",
    width=20,
    command=calcular
)
boton.pack(pady=10)

texto_resultado = tk.Text(
    ventana,
    font=("Arial", 12),
    height=8,
    width=55,
    bg="#282c34",
    fg="#98c379",
    wrap="word"
)
texto_resultado.pack(pady=10)
texto_resultado.config(state="disabled")

ventana.mainloop()
