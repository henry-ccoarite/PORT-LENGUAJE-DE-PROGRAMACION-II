import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from numpy import linspace, meshgrid, cos, sin, pi

# Deshabilitar la ventana emergente de Matplotlib (para evitar problemas de visualización)
plt.ioff()

# --- 1. Clases de Figuras Geométricas ---
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        if self.lado is not None:
            return self.lado ** 2
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        if self.radio is not None:
            return math.pi * (self.radio ** 2)
        return 0

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        if self.base is not None and self.altura is not None:
            return (self.base * self.altura) / 2
        return 0

# --- 2. Interfaz Gráfica con Tkinter y Canvas (3D Matplotlib) ---
class CalculadoraAreas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora y Visualizador de Áreas 📐 (3D)")
        self.root.geometry("800x600") 
        self.root.resizable(True, False)
        
        # Configuración de estilos
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', font=('Arial', 10))
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#4a4a4a')

        # Contenedor principal con dos columnas
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # --- Columna 0: Controles e Historial ---
        control_frame = ttk.Frame(root, padding="20 10 10 20", borderwidth=2, relief="groove")
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        
        title = ttk.Label(control_frame, text="Calculadora de Áreas", style='Title.TLabel')
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(control_frame, text="Selecciona una figura:", font=("Arial", 11)).grid(row=1, column=0, columnspan=2, pady=(10, 5))
        
        self.figura_var = tk.StringVar(value="Cuadrado")
        figuras = ["Cuadrado", "Círculo", "Triángulo"]
        
        # Botones de radio para selección
        for i, figura in enumerate(figuras):
            ttk.Radiobutton(control_frame, text=figura, variable=self.figura_var, 
                            value=figura, command=self.cambiar_figura).grid(
                            row=2, column=i, padx=5, pady=5, sticky='w')
        
        # Frame para inputs de parámetros
        self.input_frame = ttk.Frame(control_frame, padding="10")
        self.input_frame.grid(row=3, column=0, columnspan=3, pady=10, sticky='ew')
        
        # Botón calcular
        ttk.Button(control_frame, text="Calcular y Dibujar (3D)", 
                   command=self.calcular_area).grid(row=4, column=0, columnspan=3, pady=10)
        
        # Resultado del área
        ttk.Label(control_frame, text="Área Calculada:", font=("Arial", 12)).grid(row=5, column=0, sticky='w', pady=5)
        self.resultado_label = ttk.Label(control_frame, text="0.00", 
                                         font=("Arial", 14, "bold"), foreground="green")
        self.resultado_label.grid(row=5, column=1, sticky='e', pady=5)
        
        # Historial (Reducido en tamaño para dar espacio al Canvas)
        ttk.Label(control_frame, text="Historial:", font=("Arial", 11, "bold")).grid(row=6, column=0, columnspan=2, pady=(10, 5), sticky='w')
        self.historial_text = tk.Text(control_frame, height=5, width=40, state='disabled')
        self.historial_text.grid(row=7, column=0, columnspan=2, pady=5, sticky='ew')

        # --- Columna 1: Canvas de Dibujo (Matplotlib 3D) ---
        canvas_frame = ttk.Frame(root, padding="10", borderwidth=2, relief="groove")
        canvas_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        ttk.Label(canvas_frame, text="Visualización Gráfica 3D", style='Title.TLabel').pack(pady=5)
        
        # Inicialización de la figura de Matplotlib
        self.fig = Figure(figsize=(4, 4), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=canvas_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Inicializar campos y Canvas
        self.cambiar_figura()

    def cambiar_figura(self):
        # Limpiar frame de inputs
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        figura = self.figura_var.get()
        
        self.entrada1 = tk.StringVar()
        self.entrada2 = tk.StringVar()
        
        if figura == "Cuadrado":
            ttk.Label(self.input_frame, text="Lado:").grid(row=0, column=0, padx=5, sticky='w')
            ttk.Entry(self.input_frame, width=15, textvariable=self.entrada1).grid(row=0, column=1, padx=5)
            
        elif figura == "Círculo":
            ttk.Label(self.input_frame, text="Radio:").grid(row=0, column=0, padx=5, sticky='w')
            ttk.Entry(self.input_frame, width=15, textvariable=self.entrada1).grid(row=0, column=1, padx=5)
            
        elif figura == "Triángulo":
            ttk.Label(self.input_frame, text="Base:").grid(row=0, column=0, padx=5, sticky='w')
            ttk.Entry(self.input_frame, width=15, textvariable=self.entrada1).grid(row=0, column=1, padx=5)
            
            ttk.Label(self.input_frame, text="Altura:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
            ttk.Entry(self.input_frame, width=15, textvariable=self.entrada2).grid(row=1, column=1, padx=5, pady=5)
            
        self.resultado_label.config(text="0.00")
        
        # Limpiar y reiniciar el gráfico 3D
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_box_aspect([1, 1, 1])
        self.canvas.draw()
        
    def dibujar_figura(self, figura_tipo, param1, param2=None):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_title(f"Visualización 3D: {figura_tipo}")
        self.ax.set_box_aspect([1, 1, 1])
        
        try:
            # Factor de profundidad/altura constante para la extrusión
            D = max(param1, param2 if param2 is not None else 0) / 2.0 
            if D < 0.1: D = 0.5 # Mínimo para que sea visible

            if figura_tipo == "Cuadrado":
                L = param1
                # Definición de 8 vértices del cuboide
                v = [
                    (0, 0, 0), (L, 0, 0), (L, L, 0), (0, L, 0), # Base (Z=0)
                    (0, 0, D), (L, 0, D), (L, L, D), (0, L, D)  # Tapa (Z=D)
                ]
                # Definición de 6 caras
                faces = [
                    [v[0], v[1], v[5], v[4]], # Lateral 1
                    [v[2], v[3], v[7], v[6]], # Lateral 2
                    [v[0], v[3], v[7], v[4]], # Lateral 3
                    [v[1], v[2], v[6], v[5]], # Lateral 4
                    [v[0], v[1], v[2], v[3]], # Base
                    [v[4], v[5], v[6], v[7]]  # Tapa
                ]
                
                faces_collection = Poly3DCollection(faces, facecolors='#79b8e8', linewidths=1, edgecolors='#1c70b8', alpha=.80)
                self.ax.add_collection3d(faces_collection)
                
                # Centrar y establecer límites
                limit = L * 1.5
                self.ax.set_xlim([-limit/2, limit/2])
                self.ax.set_ylim([-limit/2, limit/2])
                self.ax.set_zlim([0, D * 2])
                self.ax.set_xticks([])
                self.ax.set_yticks([])
                self.ax.set_zticks([])
                
            elif figura_tipo == "Círculo":
                R = param1
                H = R / 2 # Altura del cilindro
                
                z = linspace(0, H, 50)
                theta = linspace(0, 2 * pi, 50)
                theta_grid, z_grid = meshgrid(theta, z)
                
                x_grid = R * cos(theta_grid)
                y_grid = R * sin(theta_grid)
                
                # Cuerpo del cilindro
                self.ax.plot_surface(x_grid, y_grid, z_grid, color='#f2a5a5', alpha=0.8, edgecolor='#d14040', linewidth=0.5)
                
                # Base y Tapa (Simple discs)
                self.ax.plot_surface(x_grid, y_grid, z_grid * 0, color='#f2a5a5', alpha=0.9) # Base Z=0
                self.ax.plot_surface(x_grid, y_grid, z_grid * 0 + H, color='#f2a5a5', alpha=0.9) # Tapa Z=H

                # Centrar y establecer límites
                limit = R * 2.5
                self.ax.set_xlim([-limit, limit])
                self.ax.set_ylim([-limit, limit])
                self.ax.set_zlim([0, H * 2])
                self.ax.set_xticks([])
                self.ax.set_yticks([])
                self.ax.set_zticks([])
                
            elif figura_tipo == "Triángulo":
                B = param1 # Base
                A = param2 # Altura
                D = min(B, A) / 2 # Profundidad/Espesor
                if D < 0.1: D = 0.5

                # Vertices for the triangular base (P3 arriba, P1/P2 abajo)
                v_base = [
                    (-B / 2, 0, 0), # P1 (x, y, z)
                    (B / 2, 0, 0),  # P2
                    (0, A, 0)       # P3
                ]
                
                # Vertices for the top triangle (extruded by D)
                v_top = [
                    (p[0], p[1], D) for p in v_base
                ]
                
                v = v_base + v_top
                
                # Definición de 5 caras: 2 triángulos (base/tapa) y 3 rectángulos (laterales)
                faces = [
                    [v[0], v[1], v[2]],       # Triángulo Base (Abajo)
                    [v[3], v[4], v[5]],       # Triángulo Tapa (Arriba)
                    [v[0], v[1], v[4], v[3]], # Lateral 1 (Base inferior)
                    [v[1], v[2], v[5], v[4]], # Lateral 2 (Lado derecho)
                    [v[2], v[0], v[3], v[5]]  # Lateral 3 (Lado izquierdo)
                ]
                
                faces_collection = Poly3DCollection(faces, facecolors='#79e89d', linewidths=1, edgecolors='#30c458', alpha=.80)
                self.ax.add_collection3d(faces_collection)
                
                # Centrar y establecer límites
                max_coord = max(B, A, D) * 1.5
                self.ax.set_xlim([-max_coord/2, max_coord/2])
                self.ax.set_ylim([0, A * 1.5])
                self.ax.set_zlim([0, D * 2])
                self.ax.set_xticks([])
                self.ax.set_yticks([])
                self.ax.set_zticks([])
                
        except Exception as e:
            self.ax.text(0.5, 0.5, 0.5, "Error al dibujar la figura 3D.", color='red', transform=self.ax.transAxes)
            print(f"Error en dibujar_figura: {e}")

        self.canvas.draw()

    def calcular_area(self):
        try:
            figura_tipo = self.figura_var.get()
            
            # Obtener valores de las variables de control (StringVar)
            val1_str = self.entrada1.get().strip()
            val2_str = self.entrada2.get().strip() if hasattr(self, 'entrada2') else ""
            
            if not val1_str:
                raise ValueError("Debe ingresar un valor para el primer parámetro.")
            param1 = float(val1_str)
            
            param2 = None
            if figura_tipo == "Triángulo":
                if not val2_str:
                    raise ValueError("Debe ingresar un valor para la altura del Triángulo.")
                param2 = float(val2_str)
            
            area = 0.0

            # Polimorfismo y Cálculo
            if figura_tipo == "Cuadrado":
                figura = Cuadrado(param1)
                area = figura.area()
            elif figura_tipo == "Círculo":
                figura = Circulo(param1)
                area = figura.area()
            elif figura_tipo == "Triángulo":
                figura = Triangulo(param1, param2)
                area = figura.area()
                
            # Mostrar resultado
            self.resultado_label.config(text=f"{area:.2f}", foreground="green")
            
            # Dibujar la figura
            self.dibujar_figura(figura_tipo, param1, param2)
            
            # Agregar al historial
            mensaje = f"Calculado {figura_tipo}: Área = {area:.2f}"
            self.historial_text.config(state='normal')
            self.historial_text.insert('1.0', mensaje + '\n')
            self.historial_text.config(state='disabled')
            
        except ValueError as ve:
            self.resultado_label.config(text="ERROR", foreground="red")
            messagebox.showerror("Error de Entrada", str(ve))
        except Exception as e:
            self.resultado_label.config(text="ERROR", foreground="red")
            messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {e}")

# --- 3. Inicialización ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAreas(root)
    root.mainloop()
