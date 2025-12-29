from typing import TypeVar, Generic
import math
import tkinter as tk
from tkinter import messagebox

T = TypeVar('T', int, float)

class FiguraGeometrica(Generic[T]):
    def area(self) -> float:
        raise NotImplementedError

    def perimetro(self) -> float:
        raise NotImplementedError


class Rectangulo(FiguraGeometrica[T]):
    def __init__(self, base: T, altura: T):
        base_f = float(base)
        altura_f = float(altura)
        if base_f <= 0 or altura_f <= 0:
            raise ValueError("Datos inválidos")
        self.base = base_f
        self.altura = altura_f

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Circulo(FiguraGeometrica[T]):
    def __init__(self, radio: T):
        radio_f = float(radio)
        if radio_f <= 0:
            raise ValueError("Dato inválido")
        self.radio = radio_f

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


def dibujar_rectangulo(r):
    canvas.delete("all")

    x1, y1 = 150, 100
    x2, y2 = x1 + r.base * 10, y1 + r.altura * 10

    canvas.create_rectangle(x1, y1, x2, y2, outline="#00d4ff", width=3)

    canvas.create_text((x1 + x2) / 2, y1 - 25, text=f"Base = {r.base}", fill="white")
    canvas.create_text((x1 + x2) / 2, y2 + 25, text=f"Altura = {r.altura}", fill="white")

    canvas.create_text(x1 - 70, (y1 + y2) / 2, text=f"Área = {r.area():.2f}", fill="#00ff9c")
    canvas.create_text(x2 + 80, (y1 + y2) / 2, text=f"Perímetro = {r.perimetro():.2f}", fill="#00ff9c")

    canvas.create_text(250, 30, text="RECTÁNGULO", fill="white",
                       font=("Consolas", 12, "bold"))


def dibujar_circulo(c):
    canvas.delete("all")

    r = c.radio * 10
    x, y = 250, 220
    x1, y1 = x - r, y - r
    x2, y2 = x + r, y + r

    canvas.create_oval(x1, y1, x2, y2, outline="#00ff9c", width=3)

    canvas.create_text(x, y - r - 25, text=f"Radio = {c.radio}", fill="white")
    canvas.create_text(x, y + r + 25, text=f"Diámetro = {c.radio * 2}", fill="white")

    canvas.create_text(x1 - 80, y, text=f"Área = {c.area():.2f}", fill="#00d4ff")
    canvas.create_text(x2 + 85, y, text=f"Perímetro = {c.perimetro():.2f}", fill="#00d4ff")

    canvas.create_text(250, 30, text="CÍRCULO", fill="white",
                       font=("Consolas", 12, "bold"))


def calcular_rectangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        r = Rectangulo(base, altura)

        lbl_resultado.config(
            text=f"RECTÁNGULO\nÁrea: {r.area():.2f}\nPerímetro: {r.perimetro():.2f}"
        )

        dibujar_rectangulo(r)

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def calcular_circulo():
    try:
        radio = float(entry_radio.get())
        c = Circulo(radio)

        lbl_resultado.config(
            text=f"CÍRCULO\nÁrea: {c.area():.2f}\nPerímetro: {c.perimetro():.2f}"
        )

        dibujar_circulo(c)

    except ValueError as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Figuras Geométricas con Datos Alrededor")
ventana.geometry("850x480")
ventana.configure(bg="#1e1e2f")

panel = tk.Frame(ventana, bg="#1e1e2f")
panel.pack(side="left", padx=20)

tk.Label(panel, text="RECTÁNGULO", bg="#1e1e2f", fg="#00d4ff",
         font=("Segoe UI", 13, "bold")).pack()

tk.Label(panel, text="Base", bg="#1e1e2f", fg="white").pack()
entry_base = tk.Entry(panel)
entry_base.pack()

tk.Label(panel, text="Altura", bg="#1e1e2f", fg="white").pack()
entry_altura = tk.Entry(panel)
entry_altura.pack()

tk.Button(panel, text="Calcular Rectángulo",
          command=calcular_rectangulo,
          bg="#00d4ff").pack(pady=10)

tk.Label(panel, text="CÍRCULO", bg="#1e1e2f", fg="#00ff9c",
         font=("Segoe UI", 13, "bold")).pack(pady=10)

tk.Label(panel, text="Radio", bg="#1e1e2f", fg="white").pack()
entry_radio = tk.Entry(panel)
entry_radio.pack()

tk.Button(panel, text="Calcular Círculo",
          command=calcular_circulo,
          bg="#00ff9c").pack(pady=10)

lbl_resultado = tk.Label(panel, text="", bg="#1e1e2f",
                         fg="white", font=("Consolas", 11),
                         justify="left")
lbl_resultado.pack(pady=15)

canvas = tk.Canvas(ventana, width=520, height=420, bg="black")
canvas.pack(side="right", padx=15)

ventana.mainloop()
