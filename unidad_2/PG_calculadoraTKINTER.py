import tkinter as tk
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Los valores deben ser int o float")
            self.a = a
            self.b = b
        except Exception as e:
            raise TypeError(f"Error al asignar valores: {e}")

    def sumar(self) -> T:
        try:
            return self.a + self.b
        except Exception as e:
            raise TypeError(f"Error en la suma: {e}")
    
    def restar(self) -> T:
        try:
            return self.a - self.b
        except Exception as e:
            raise TypeError(f"Error en la resta: {e}")

    def multiplicar(self) -> T:
        try:
            return self.a * self.b
        except Exception as e:
            raise TypeError(f"Error en la multiplicación: {e}")
    
    def dividir(self) -> float:
        try:
            if self.b == 0:
                raise ArithmeticError("No se puede dividir entre 0")
            return self.a / self.b
        except ArithmeticError as e:
            raise ArithmeticError(f"Error en la división: {e}")
        except Exception as e:
            raise TypeError(f"Error inesperado en la división: {e}")


def presionar(valor):
    visor.insert(tk.END, valor)

def limpiar():
    visor.delete(0, tk.END)
    mensaje.set("")

def operar(op):
    try:
        datos = visor.get().split()
        a = float(datos[0])
        b = float(datos[2])
        calc = Calculadora[float](a, b)

        if op == "+":
            r = calc.sumar()
        elif op == "-":
            r = calc.restar()
        elif op == "*":
            r = calc.multiplicar()
        elif op == "/":
            r = calc.dividir()

        texto = f"{a} {op} {b} = {r}"
        historial.insert(tk.END, texto)
        visor.delete(0, tk.END)
        visor.insert(0, r)
        mensaje.set("")
    except ArithmeticError as e:
        mensaje.set(f"ERROR ARITMÉTICO: {e}")
    except TypeError as e:
        mensaje.set(f"ERROR DE TIPO: {e}")
    except Exception as e:
        mensaje.set("FORMATO: A + B")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("360x520")
ventana.configure(bg="#e0f2fe")

visor = tk.Entry(ventana, font=("Arial", 20, "bold"), justify="right", bg="#bfdbfe", fg="#020617")
visor.pack(fill="x", padx=10, pady=10)

mensaje = tk.StringVar()
tk.Label(ventana, textvariable=mensaje, bg="#e0f2fe", fg="#1d4ed8", font=("Arial", 10, "bold")).pack()

frame = tk.Frame(ventana, bg="#e0f2fe")
frame.pack()

botones = [
    ("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
    ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
    ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
    ("0",3,0), (".",3,1), ("C",3,2), ("+",3,3)
]

for (texto, fila, col) in botones:
    if texto == "C":
        tk.Button(frame, text=texto, command=limpiar, bg="#93c5fd", fg="#020617", width=6, height=2).grid(row=fila, column=col, padx=4, pady=4)
    elif texto in "+-*/":
        tk.Button(frame, text=texto, command=lambda t=texto: presionar(f" {t} "), bg="#60a5fa", fg="#020617", width=6, height=2).grid(row=fila, column=col, padx=4, pady=4)
    else:
        tk.Button(frame, text=texto, command=lambda t=texto: presionar(t), bg="#dbeafe", fg="#020617", width=6, height=2).grid(row=fila, column=col, padx=4, pady=4)

tk.Button(ventana, text="=", command=lambda: operar(visor.get().split()[1] if len(visor.get().split()) == 3 else ""), bg="#2563eb", fg="white", font=("Arial", 14, "bold"), height=2).pack(fill="x", padx=10, pady=10)

tk.Label(ventana, text="HISTORIAL", bg="#e0f2fe", fg="#1e40af", font=("Arial", 12, "bold")).pack()

historial = tk.Listbox(ventana, height=6, bg="#dbeafe", fg="#020617", selectbackground="#93c5fd")
historial.pack(fill="x", padx=10, pady=10)

ventana.mainloop()
