import tkinter as tk
from tkinter import messagebox

class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        resultado = []
        for i in range(1, 11):
            operacion = f"{self.numero} x {i} = {self.numero * i}"
            resultado.append(operacion)
        return resultado


def generar_tabla():
    try:
        numero = int(entry.get())  # tomar número del cuadro de texto
        mitabla = Tabla(numero)
        resultadof = mitabla.multiplicar()

        # Limpiar el texto anterior
        text_area.delete("1.0", tk.END)

        # Mostrar la tabla
        for linea in resultadof:
            text_area.insert(tk.END, linea + "\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número entero válido.")


# Ventana principal
root = tk.Tk()
root.title("Tabla de Multiplicar")

# Entrada de número
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Ingrese un número:")
label.pack(side="left")

entry = tk.Entry(frame, width=10)
entry.pack(side="left", padx=5)

btn = tk.Button(frame, text="Generar", command=generar_tabla)
btn.pack(side="left")

# Área de texto para mostrar la tabla
text_area = tk.Text(root, width=30, height=12, fg="blue")
text_area.pack(pady=10)

root.mainloop()
