import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Geométrica")
        self.geometry("380x320")
        self.resizable(False, False)
        self.configure(bg="#1e293b")

        self.figura_var = tk.StringVar(value="Circulo")

        tk.Label(
            self, text="Calculadora Geométrica",
            bg="#1e293b", fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        frame_opciones = tk.Frame(self, bg="#1e293b")
        frame_opciones.pack()

        tk.Radiobutton(
            frame_opciones, text="Círculo",
            variable=self.figura_var, value="Circulo",
            bg="#1e293b", fg="white",
            selectcolor="#334155",
            command=self.actualizar_campos
        ).grid(row=0, column=0, padx=10)

        tk.Radiobutton(
            frame_opciones, text="Rectángulo",
            variable=self.figura_var, value="Rectangulo",
            bg="#1e293b", fg="white",
            selectcolor="#334155",
            command=self.actualizar_campos
        ).grid(row=0, column=1, padx=10)

        self.frame_inputs = tk.Frame(self, bg="#1e293b")
        self.frame_inputs.pack(pady=15)

        self.label1 = tk.Label(self.frame_inputs, bg="#1e293b", fg="white")
        self.entry1 = tk.Entry(self.frame_inputs, bg="#f8fafc")

        self.label2 = tk.Label(self.frame_inputs, bg="#1e293b", fg="white")
        self.entry2 = tk.Entry(self.frame_inputs, bg="#f8fafc")

        tk.Button(
            self, text="Calcular",
            bg="#38bdf8", fg="black",
            font=("Segoe UI", 10, "bold"),
            command=self.calcular
        ).pack(pady=10)

        self.resultado = tk.Label(
            self, text="",
            bg="#1e293b", fg="#38bdf8",
            font=("Segoe UI", 11, "bold")
        )
        self.resultado.pack(pady=10)

        self.actualizar_campos()

    def actualizar_campos(self):
        for w in self.frame_inputs.winfo_children():
            w.grid_forget()

        if self.figura_var.get() == "Circulo":
            self.label1.config(text="Radio:")
            self.label1.grid(row=0, column=0, padx=5, pady=5)
            self.entry1.grid(row=0, column=1, padx=5, pady=5)
        else:
            self.label1.config(text="Largo:")
            self.label2.config(text="Ancho:")
            self.label1.grid(row=0, column=0, padx=5, pady=5)
            self.entry1.grid(row=0, column=1, padx=5, pady=5)
            self.label2.grid(row=1, column=0, padx=5, pady=5)
            self.entry2.grid(row=1, column=1, padx=5, pady=5)

    def calcular(self):
        try:
            if self.figura_var.get() == "Circulo":
                figura = Circulo(float(self.entry1.get()))
            else:
                figura = Rectangulo(
                    float(self.entry1.get()),
                    float(self.entry2.get())
                )

            self.resultado.config(
                text=f"Área: {figura.area():.2f}\nPerímetro: {figura.perimetro():.2f}"
            )

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")


if __name__ == "__main__":
    app = App()
    app.mainloop()
