import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años."

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        salario_formato = f"{self.salario:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
        return f"Estoy chambeando como {self.profesion} y gano ${salario_formato} al mes."
        
class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad
        
    def estudiar(self):
        return f"Estudio la carrera de {self.carrera} en la {self.universidad}."

class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def Mostrar_informacion(self):
        output = "========= INFORMACION DE LA PERSONA =========\n"
        output += self.presentarse() + "\n"
        output += self.trabajar() + "\n"
        output += self.estudiar() + "\n"
        output += "============================================="
        return output

class MultirolApp:
    
    # Diccionario con los datos iniciales
    PERSONAS_DATA = {
        "Juanita (Persona 1)": {
            "nombre": "Juanita",
            "edad": "25",
            "profesion": "Desarrollador de software",
            "salario": "2500",
            "carrera": "INGENIERIA ESTADISTICA E INFORMATICA",
            "universidad": "Universidad Nacional del Altiplano"
        },
        "Pedro (Persona 2)": {
            "nombre": "Pedro Antonio",
            "edad": "30",
            "profesion": "Ingeniero Civil",
            "salario": "4500",
            "carrera": "Arquitectura",
            "universidad": "Universidad Nacional de Ingeniería"
        },
        "Carlos (Persona 3)": {
            "nombre": "Carlos Javier",
            "edad": "22",
            "profesion": "Asistente de Marketing",
            "salario": "1500",
            "carrera": "Comunicación Social",
            "universidad": "Universidad Católica Santa María"
        }
    }
    
    # Contador para las nuevas personas
    nueva_persona_counter = 4

    def __init__(self, master):
        self.master = master
        master.title("Herencia Múltiple: Gestión Dinámica de Roles")
        master.geometry("500x650") # Aumento de altura para el nuevo botón
        
        # Variables de control
        self.nombre_var = tk.StringVar()
        self.edad_var = tk.StringVar()
        self.profesion_var = tk.StringVar()
        self.salario_var = tk.StringVar()
        self.carrera_var = tk.StringVar()
        self.universidad_var = tk.StringVar()
        self.selector_var = tk.StringVar()
        
        
        # --- Selector de Persona ---
        tk.Label(master, text="Seleccione la Persona:", font=("Arial", 11, "bold")).pack(pady=10)
        
        self.selector_combo = ttk.Combobox(
            master, 
            textvariable=self.selector_var, 
            values=list(self.PERSONAS_DATA.keys()), 
            state="readonly",
            font=("Arial", 10),
            width=35
        )
        self.selector_combo.set("Juanita (Persona 1)")
        self.selector_combo.bind("<<ComboboxSelected>>", self.cargar_persona_seleccionada)
        self.selector_combo.pack(pady=5)
        
        
        # --- Widgets de Entrada ---
        input_frame = tk.Frame(master, padx=10, pady=5)
        input_frame.pack(pady=5)

        etiquetas = ["Nombre:", "Edad:", "Profesión:", "Salario:", "Carrera:", "Universidad:"]
        variables = [self.nombre_var, self.edad_var, self.profesion_var, self.salario_var, self.carrera_var, self.universidad_var]
        
        for i, (label_text, var) in enumerate(zip(etiquetas, variables)):
            tk.Label(input_frame, text=label_text, font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=3)
            tk.Entry(input_frame, textvariable=var, width=35, font=("Arial", 10)).grid(row=i, column=1, padx=10, pady=3)

        # --- Botones de Acción ---
        action_frame = tk.Frame(master)
        action_frame.pack(pady=10)
        
        tk.Button(action_frame, text="Mostrar/Actualizar Info", command=self.mostrar_info_gui, bg="#32CD32", fg="black", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        
        # Nuevo Botón para Agregar Persona
        tk.Button(action_frame, text="✅ Agregar Nueva Persona", command=self.agregar_nueva_persona, bg="#1E90FF", fg="white", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        
        
        # --- Área de Salida ---
        tk.Label(master, text="Resultado de la Herencia:", font=("Arial", 10, "underline")).pack()
        self.output_text = tk.Text(master, height=7, width=55, state=tk.DISABLED, wrap=tk.WORD, font=('Consolas', 10), bg="#F0F0F0")
        self.output_text.pack(padx=10, pady=5)
        
        # Cargar los datos iniciales al inicio
        self.cargar_persona_seleccionada(None)

    def agregar_nueva_persona(self):
        """Guarda la información de los campos como una nueva persona en el diccionario y actualiza el Combobox."""
        try:
            nombre = self.nombre_var.get()
            profesion = self.profesion_var.get()
            carrera = self.carrera_var.get()
            universidad = self.universidad_var.get()
            
            edad = self.edad_var.get()
            salario = self.salario_var.get()
            
            # Validación de campos
            if not all([nombre, edad, profesion, salario, carrera, universidad]):
                 raise ValueError("Todos los campos deben estar llenos para agregar una nueva persona.")
            
            # Verificación de tipos
            int(edad)
            float(salario)
            
            # Crear la clave de la nueva persona
            nueva_key = f"{nombre} (Persona {self.nueva_persona_counter})"
            
            # Guardar en el diccionario global (simulado)
            self.PERSONAS_DATA[nueva_key] = {
                "nombre": nombre,
                "edad": edad,
                "profesion": profesion,
                "salario": salario,
                "carrera": carrera,
                "universidad": universidad
            }
            
            # Actualizar el Combobox y seleccionarla
            self.selector_combo['values'] = list(self.PERSONAS_DATA.keys())
            self.selector_combo.set(nueva_key)
            
            self.nueva_persona_counter += 1
            
            # Mostrar la información de la persona recién agregada
            self.mostrar_info_gui()
            messagebox.showinfo("Éxito", f"¡Nueva persona '{nombre}' agregada y seleccionada correctamente!")

        except ValueError as e:
            messagebox.showerror("Error de Validación", f"Error al agregar persona: {e}\nAsegúrese de que Edad y Salario sean números.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado al guardar: {e}")


    def cargar_persona_seleccionada(self, event):
        """Carga los datos de la persona seleccionada en los campos de entrada."""
        selected_key = self.selector_var.get()
        data = self.PERSONAS_DATA.get(selected_key)
        
        if data:
            self.nombre_var.set(data["nombre"])
            self.edad_var.set(data["edad"])
            self.profesion_var.set(data["profesion"])
            self.salario_var.set(data["salario"])
            self.carrera_var.set(data["carrera"])
            self.universidad_var.set(data["universidad"])
            
            # Muestra automáticamente la información al cargar
            self.mostrar_info_gui()


    def mostrar_info_gui(self):
        """Crea la instancia de PersonaMultirol con los datos de los campos y muestra la información."""
        try:
            nombre = self.nombre_var.get()
            profesion = self.profesion_var.get()
            carrera = self.carrera_var.get()
            universidad = self.universidad_var.get()
            
            # Usa los datos de las variables, asumiendo que ya se validaron o están siendo validados aquí
            edad = int(self.edad_var.get())
            salario = float(self.salario_var.get())
            
            persona = PersonaMultirol(nombre, edad, profesion, salario, carrera, universidad)
            
            info = persona.Mostrar_informacion()
            
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, info)
            self.output_text.config(state=tk.DISABLED)
            
        except ValueError:
            # Captura errores si los campos están vacíos o tienen formato incorrecto
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "ERROR: Complete o corrija los campos (Edad/Salario deben ser números).")
            self.output_text.config(state=tk.DISABLED)
            # No muestra messagebox, ya que el botón "Agregar" se encarga de la validación estricta
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultirolApp(root)
    root.mainloop()
