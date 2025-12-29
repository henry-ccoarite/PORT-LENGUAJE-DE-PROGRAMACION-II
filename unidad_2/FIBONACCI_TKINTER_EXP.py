import tkinter as tk

def fibonacci_secuencia(n):
    if not isinstance(n, int):
        raise TypeError("Debe ingresar un número entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n == 0:
        return "0"
    if n == 1:
        return "0, 1"

    a, b = 0, 1
    salida = "0, 1"

    for _ in range(2, n + 1):
        a, b = b, a + b
        salida += ", " + str(b)

    return salida

def calcular_fibonacci():
    texto_resultado.config(state="normal")
    texto_resultado.delete("1.0", tk.END)

    try:
        n = int(entry_numero.get())
        secuencia = fibonacci_secuencia(n)
        texto_resultado.insert(tk.END, secuencia)
    except ValueError as ve:
        texto_resultado.insert(tk.END, "Error de valor: " + str(ve))
    except TypeError as te:
        texto_resultado.insert(tk.END, "Error de valor: " + str(te))
    except Exception as e:
        texto_resultado.insert(tk.END, "Error inesperado: " + str(e))

    texto_resultado.config(state="disabled")

ventana = tk.Tk()
ventana.title("Secuencia de Fibonacci")
ventana.geometry("500x350")
ventana.config(bg="#1e1e1e")

titulo = tk.Label(
    ventana,
    text="Fibonacci hasta n",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="#7dcfff"
)
titulo.pack(pady=12)

frame = tk.Frame(ventana, bg="#1e1e1e")
frame.pack(pady=5)

label_n = tk.Label(
    frame,
    text="Ingrese n:",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
label_n.grid(row=0, column=0, padx=10, pady=5)

entry_numero = tk.Entry(frame, font=("Arial", 12), width=10)
entry_numero.grid(row=0, column=1, pady=5)

boton = tk.Button(
    ventana,
    text="Generar Secuencia",
    font=("Arial", 12, "bold"),
    bg="#61afef",
    fg="black",
    width=20,
    command=calcular_fibonacci
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
