import tkinter as tk
from tkinter import messagebox

class CL:
    def __init__(self, longitud, altura, ancho, JV, JH):
        self.longitud = longitud
        self.altura = altura
        self.ancho = ancho
        self.JV = JV
        self.JH = JH

    def calcular_CL(self):
        return 1 / ((self.longitud + self.JH) * (self.altura + self.JV))


def calcular():
    try:
        # Obtener valores desde las entradas
        longitud = float(entry_longitud.get())
        altura = float(entry_altura.get())
        ancho = float(entry_ancho.get())
        JV = 0.015
        JH = 0.015

        # Crear objeto y calcular
        operacion = CL(longitud, altura, ancho, JV, JH)
        cl = operacion.calcular_CL()

        # Resultados
        resultado1 = f"La cantidad de ladrillos en un m² es de: {cl:.2f}"
        resultado2 = f"El valor total por m² es de: {cl*1.05:.2f}"
        resultado3 = f"La cantidad total en un área de 8.05 m² es: {cl*8.05*1.05:.2f}"

        # Mostrar en el cuadro de texto
        text_resultados.delete("1.0", tk.END)
        text_resultados.insert(tk.END, resultado1 + "\n")
        text_resultados.insert(tk.END, resultado2 + "\n")
        text_resultados.insert(tk.END, resultado3 + "\n")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


# Crear ventana
ventana = tk.Tk()
ventana.title("Cálculo de Ladrillos")
ventana.geometry("400x350")

# Etiquetas y entradas
tk.Label(ventana, text="Longitud del ladrillo (m):").pack(pady=5)
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

tk.Label(ventana, text="Altura del ladrillo (m):").pack(pady=5)
entry_altura = tk.Entry(ventana)
entry_altura.pack()

tk.Label(ventana, text="Ancho del ladrillo (m):").pack(pady=5)
entry_ancho = tk.Entry(ventana)
entry_ancho.pack()

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)

# Caja de resultados
text_resultados = tk.Text(ventana, height=6, width=45)
text_resultados.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
