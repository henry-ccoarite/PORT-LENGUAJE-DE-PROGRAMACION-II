import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, filedialog
import time
import uuid
import json
import csv
import os

# --- Constantes para persistencia ---
DATA_FILE = "users_data.json" # Archivo JSON donde se guarda la "base de datos" de usuarios y transacciones
AUTO_EXPORT_FILE = "movimientos_automaticos.csv" # Archivo CSV de exportación automática

# --- 1. Clases de Lógica de Negocio (Polimorfismo) ---

class Metodo_Pago:
    """Clase base para todos los métodos de pago."""
    def realizar_pago(self, monto):
        # Utiliza el símbolo de moneda genérico aquí, será reemplazado en el procesador.
        return [
            f"Procesando pago de ${monto:.2f}...",
            "Mensaje Específico no definido."
        ]

class Tarjeta(Metodo_Pago):
    def realizar_pago(self, monto):
        mensajes = super().realizar_pago(monto)
        mensajes[1] = "Pago completado con Tarjeta de crédito. Datos registrados."
        return mensajes

class PayPal(Metodo_Pago):
    def realizar_pago(self, monto):
        mensajes = super().realizar_pago(monto)
        mensajes[1] = "Pago realizado mediante PayPal (Requiere datos de tarjeta)."
        return mensajes

class Efectivo(Metodo_Pago):
    def realizar_pago(self, monto):
        mensajes = super().realizar_pago(monto)
        mensajes[1] = "Pago realizado en efectivo."
        return mensajes

class Yape(Metodo_Pago):
    """Implementación de pago con Yape (Transferencia simple)."""
    def realizar_pago(self, monto):
        mensajes = super().realizar_pago(monto)
        mensajes[1] = "Pago realizado mediante Yape (Transferencia)."
        return mensajes

# --- 2. Interfaz de Autenticación (Inicial) ---

class AuthApp:
    """
    Ventana inicial para Login y Creación de Cuenta.
    Maneja la 'base de datos' de usuarios y la persistencia de datos (JSON).
    """
    def __init__(self, master):
        self.master = master
        master.title("Autenticación BCP Terminal")
        master.geometry("400x350")
        master.resizable(False, False)

        # Cargar usuarios existentes o usar un default si no existe el archivo.
        self.users = self._load_users()

        # Variables de control
        self.phone_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.is_creating = tk.BooleanVar(value=False)
        self.main_frame = None

        self._configurar_estilos()
        self._crear_widgets()
        
        # Guardar datos al cerrar la ventana principal
        master.protocol("WM_DELETE_WINDOW", self._on_app_close)

    def _on_app_close(self):
        """Maneja el cierre de la ventana principal, asegurando el guardado de datos."""
        self._save_users()
        self.master.destroy()

    def _load_users(self):
        """Carga los datos de usuarios desde el archivo JSON."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    # Si el archivo está vacío o no es un JSON válido, retorna el valor por defecto
                    content = f.read()
                    if not content:
                        return self._default_users()
                    return json.loads(content)
            except json.JSONDecodeError:
                messagebox.showerror("Error de Carga", "El archivo de datos de usuarios está corrupto. Se iniciará con datos vacíos/por defecto.")
                return self._default_users()
            except Exception as e:
                messagebox.showerror("Error de Archivo", f"No se pudo leer el archivo de datos: {e}")
                return self._default_users()
        return self._default_users()

    def _default_users(self):
        """Define los usuarios por defecto si no se puede cargar el archivo."""
        # Se asegura que la base de datos siempre tenga un estado inicial si no existe el archivo.
        return {
            "987654321": {"name": "Usuario Demo", "history": []},
            "111222333": {"name": "Admin Test", "history": []}
        }

    def _save_users(self):
        """Guarda los datos de usuarios en el archivo JSON."""
        # Esta es la función de persistencia que asegura que los datos NO se borren.
        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, indent=4, ensure_ascii=False)
            print(f"Datos de usuarios guardados en {DATA_FILE}")
        except Exception as e:
            messagebox.showerror("Error de Guardado", f"No se pudo guardar la información: {e}")

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Auth.TFrame', background='#F8F8F8')
        style.configure('AuthHeader.TLabel', font=('Helvetica', 16, 'bold'), foreground='#CC0000', background='#F8F8F8')
        style.configure('AuthLabel.TLabel', font=('Arial', 10, 'bold'), background='#F8F8F8', foreground='#333333')
        style.configure('Auth.TButton', font=('Arial', 10, 'bold'), foreground='white', background='#0066CC', padding=8)
        style.map('Auth.TButton', background=[('active', '#004C99')])
        style.configure('Toggle.TButton', font=('Arial', 9), foreground='#CC0000', background='#F8F8F8', borderwidth=0)


    def _validate_phone_input(self, action, index, value_if_allowed, prior_value, text, widget_name):
        """Valida que la entrada del celular sean solo números y no exceda 9 dígitos."""
        if action == '1': # 1 means insert
            if not text.isdigit():
                return False
            if len(value_if_allowed) > 9:
                return False
        return True

    def _crear_widgets(self):
        self.main_frame = ttk.Frame(self.master, padding="30 20", style='Auth.TFrame')
        self.main_frame.pack(fill='both', expand=True)

        ttk.Label(self.main_frame, text="BIENVENIDO", style='AuthHeader.TLabel').pack(pady=(0, 10))
        ttk.Label(self.main_frame, text="Inicie Sesión o Regístrese", font=('Arial', 10), background='#F8F8F8').pack(pady=(0, 20))

        self.vcmd_phone = self.master.register(self._validate_phone_input)

        # 1. Campo de Celular
        ttk.Label(self.main_frame, text="Número de Celular (9 dígitos):", style='AuthLabel.TLabel').pack(anchor='w', pady=(5, 0))
        self.phone_entry = ttk.Entry(self.main_frame, 
                                     textvariable=self.phone_var, 
                                     font=('Consolas', 11), 
                                     width=25,
                                     validate='key', 
                                     validatecommand=(self.vcmd_phone, '%d', '%i', '%P', '%s', '%S', '%W'))
        self.phone_entry.pack(fill='x', pady=(0, 10))

        # 2. Campo de Nombre Completo (Manejado por pack_forget/pack)
        self.name_label = ttk.Label(self.main_frame, text="Nombre Completo:", style='AuthLabel.TLabel')
        self.name_entry = ttk.Entry(self.main_frame, textvariable=self.name_var, font=('Consolas', 11))
        
        # 3. Botones de Acción
        self.action_button = ttk.Button(self.main_frame, text="Iniciar Sesión", command=self._handle_action, style='Auth.TButton')
        self.action_button.pack(fill='x', pady=(15, 10))

        # 4. Botón para alternar modo (La opción de registro/login faltante)
        self.toggle_button = ttk.Button(self.main_frame, text="¿No tienes cuenta? Regístrate aquí.", command=self._toggle_mode, style='Toggle.TButton')
        self.toggle_button.pack(pady=(5, 0))
        
        # Estado inicial (Login)
        self._set_mode_login()


    def _toggle_mode(self):
        """Alterna entre modo Login y modo Registro."""
        if self.is_creating.get():
            self._set_mode_login()
        else:
            self._set_mode_signup()

    def _set_mode_login(self):
        """Configura la UI para el modo Iniciar Sesión."""
        self.is_creating.set(False)
        self.master.title("Iniciar Sesión")
        # Asegurarse de que los widgets de registro estén ocultos
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        # Repack el botón de acción para mantener el orden
        self.action_button.pack_forget()
        self.action_button.config(text="Iniciar Sesión")
        self.action_button.pack(fill='x', pady=(15, 10))
        self.toggle_button.config(text="¿No tienes cuenta? Regístrate aquí.")
        self.master.geometry("400x250") # Tamaño ajustado para login

    def _set_mode_signup(self):
        """Configura la UI para el modo Crear Cuenta (REGISTRO)."""
        self.is_creating.set(True)
        self.master.title("Crear Cuenta")
        
        # Insertar los widgets de registro antes del botón de acción
        self.action_button.pack_forget()
        self.name_label.pack(anchor='w', pady=(5, 0))
        self.name_entry.pack(fill='x', pady=(0, 10))
        
        self.action_button.config(text="Crear Cuenta")
        self.action_button.pack(fill='x', pady=(15, 10))
        self.toggle_button.config(text="Ya tengo cuenta. Iniciar Sesión.")
        self.master.geometry("400x350") # Tamaño ajustado para registro
        
    def _handle_action(self):
        """Llama a la función de acción (Login o Crear Cuenta) según el modo actual."""
        if self.is_creating.get():
            self._create_account()
        else:
            self._login()

    def _login(self):
        phone = self.phone_var.get()
        if len(phone) != 9:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un número de celular de 9 dígitos.")
            return
            
        if phone in self.users:
            # Obtener todos los datos del usuario, incluido el historial
            user_data = self.users[phone]
            
            # Ocultar la ventana de autenticación y abrir la aplicación principal
            self.master.withdraw()
            # Pasamos la referencia al diccionario completo de usuarios y la función de guardar
            self._open_main_app(user_data, self.users, self._save_users)
        else:
            messagebox.showerror("Error de Sesión", "Número de celular no registrado. Por favor, regístrese.")

    def _create_account(self):
        phone = self.phone_var.get()
        full_name = self.name_var.get().strip()

        if len(phone) != 9 or not phone.isdigit():
            messagebox.showwarning("Error", "El número de celular debe tener exactamente 9 dígitos.")
            return
        if not full_name:
            messagebox.showwarning("Error", "El nombre completo no puede estar vacío.")
            return
        if phone in self.users:
            messagebox.showwarning("Error", "Este número de celular ya está registrado. Por favor, inicie sesión.")
            return

        # Crear el nuevo usuario con un historial vacío
        new_user_data = {"name": full_name, "history": []}
        self.users[phone] = new_user_data
        
        # Guardar inmediatamente los nuevos datos, cumpliendo con el requisito de persistencia.
        self._save_users() 
        
        messagebox.showinfo("Éxito", f"Cuenta creada para {full_name}. Iniciando sesión automáticamente.")
        
        # Auto-login
        self.master.withdraw()
        # Pasamos la referencia al diccionario completo de usuarios y la función de guardar
        self._open_main_app(new_user_data, self.users, self._save_users)

    def _open_main_app(self, user_data, all_users_ref, save_func):
        """Inicializa y abre la aplicación principal de pagos, pasando los datos del usuario y referencias de persistencia."""
        main_root = Toplevel(self.master)
        # Pasamos el diccionario de usuario, la referencia a TODOS los usuarios y la función de guardar
        app = PaymentTerminalApp(main_root, user_data, all_users_ref, save_func)
        
        # Al cerrar el terminal, guardamos datos y volvemos a la autenticación
        main_root.protocol("WM_DELETE_WINDOW", lambda: self._on_terminal_close(main_root, save_func))

    def _on_terminal_close(self, main_root, save_func):
        """Maneja el cierre de la ventana del terminal, guardando y volviendo a la autenticación."""
        save_func() # Guardar los datos actualizados
        main_root.destroy()
        self.master.deiconify() # Muestra nuevamente la ventana de autenticación
        self.phone_var.set("")
        self.name_var.set("")


# --- 3. Interfaz Gráfica (Tkinter) - PaymentTerminalApp ---

class PaymentTerminalApp:
    def __init__(self, master, user_data, all_users_ref, save_func):
        self.master = master
        # Referencia al diccionario de todos los usuarios y la función de guardado
        self.all_users = all_users_ref
        self.save_users_func = save_func
        
        self.user_data = user_data
        self.user_name = user_data.get("name", "Desconocido")
        # El historial de pagos es una referencia directa a la lista del usuario
        self.historial_pagos = user_data.get("history", [])
        
        master.title(f"Terminal de Pagos BCP Style 💳 - Usuario: {self.user_name}")
        master.geometry("450x660")
        master.resizable(False, False)

        # Variables de control
        self.monto_var = tk.StringVar(value="50.00")
        self.metodo_var = tk.StringVar(value="Tarjeta")
        self.moneda_var = tk.StringVar(value="Dólares")
        
        # VARIABLES PARA DATOS DEL TITULAR
        self.dni_var = tk.StringVar(value="")
        self.card_number_var = tk.StringVar(value="")
        self.titular_var = tk.StringVar(value="")
        
        self.last_transaction_data = None
        
        self.opciones_pago = {
            "Tarjeta": Tarjeta,
            "PayPal": PayPal,
            "Efectivo": Efectivo,
            "Yape": Yape
        }

        # Registro de función de validación (solo números y max 7 dígitos para DNI)
        self.vcmd = master.register(self._validate_dni_input)
        
        self._configurar_estilos()
        self._crear_widgets()
        # Cargar historial al iniciar
        self._actualizar_historial()

    def _validate_dni_input(self, action, index, value_if_allowed, prior_value, text, widget_name):
        """Valida que la entrada del DNI sean solo números y no exceda 7 dígitos."""
        if action == '1': # 1 means insert
            if not text.isdigit():
                return False
            if len(value_if_allowed) > 7:
                return False
        return True

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Main.TFrame', background='#FFFFFF')
        style.configure('Header.TLabel', 
                        font=('Helvetica', 18, 'bold'), 
                        foreground='#CC0000', 
                        background='#FFFFFF')
        style.configure('TLabel', 
                        font=('Arial', 10), 
                        background='#FFFFFF', 
                        foreground='#333333')
        style.configure('TRadiobutton', background='#FFFFFF', foreground='#333333')
        style.configure('Process.TButton', 
                        font=('Arial', 12, 'bold'), 
                        foreground='white', 
                        background='#CC0000', 
                        padding=10)
        style.map('Process.TButton',
                  background=[('active', '#A30000')])
        
        style.configure('Boleta.TButton', 
                        font=('Arial', 10, 'bold'), 
                        foreground='white', 
                        background='#CC0000', # Rojo BCP
                        padding=5)
        style.map('Boleta.TButton',
                  background=[('active', '#A30000')])
                    
        # Nuevo estilo para el botón de exportación
        style.configure('Export.TButton', 
                        font=('Arial', 10, 'bold'), 
                        foreground='white', 
                        background='#0066CC', # Azul
                        padding=5)
        style.map('Export.TButton',
                  background=[('active', '#004C99')])

    def _obtener_simbolo(self):
        if self.moneda_var.get() == "Soles":
            return "S/."
        return "$"

    def _actualizar_etiqueta_monto(self):
        simbolo = self._obtener_simbolo()
        self.monto_label.config(text=f"Monto a Pagar ({simbolo}):")

    def _crear_widgets(self):
        main_frame = ttk.Frame(self.master, padding="30 20", style='Main.TFrame')
        main_frame.pack(fill='both', expand=True)

        ttk.Label(main_frame, text="TERMINAL DE PAGO", style='Header.TLabel').pack(pady=(0, 5))
        
        # Etiqueta de usuario autenticado
        ttk.Label(main_frame, text=f"Autenticado como: {self.user_name}", font=('Arial', 10, 'italic'), foreground='#0066CC', background='#FFFFFF').pack(pady=(0, 15))

        # Sección de Moneda
        moneda_frame = ttk.Frame(main_frame, style='Main.TFrame')
        moneda_frame.pack(fill='x', pady=5)
        
        ttk.Label(moneda_frame, text="Moneda:", font=('Arial', 11, 'bold')).pack(side='left', padx=(0, 10))
        
        ttk.Radiobutton(moneda_frame, text="Dólares ($)", variable=self.moneda_var, value="Dólares", 
                        command=self._actualizar_etiqueta_monto, style='TRadiobutton').pack(side='left', padx=10)
        ttk.Radiobutton(moneda_frame, text="Soles (S/.)", variable=self.moneda_var, value="Soles", 
                        command=self._actualizar_etiqueta_monto, style='TRadiobutton').pack(side='left', padx=10)
        
        # Sección de Monto
        monto_frame = ttk.Frame(main_frame, style='Main.TFrame')
        monto_frame.pack(fill='x', pady=10)
        
        self.monto_label = ttk.Label(monto_frame, 
                                     text=f"Monto a Pagar ({self._obtener_simbolo()}):", 
                                     font=('Arial', 11, 'bold'))
        self.monto_label.pack(side='left', padx=(0, 10))
        
        self.monto_entry = ttk.Entry(monto_frame, 
                                     textvariable=self.monto_var, 
                                     font=('Consolas', 12), 
                                     width=15, 
                                     justify='right', 
                                     foreground='#CC0000')
        self.monto_entry.pack(side='right', fill='x', expand=True)

        # Sección Método de Pago
        ttk.Label(main_frame, text="Seleccione Método de Pago:", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(15, 5))
        
        metodo_frame = ttk.Frame(main_frame, style='Main.TFrame')
        metodo_frame.pack(fill='x', pady=5)
        
        opciones = list(self.opciones_pago.keys())
        for i, nombre in enumerate(opciones):
            row = i // 2
            col = i % 2
            rb = ttk.Radiobutton(metodo_frame, 
                                 text=nombre, 
                                 variable=self.metodo_var, 
                                 value=nombre,
                                 command=self._manejar_seleccion_metodo_pago,
                                 style='TRadiobutton')
            rb.grid(row=row, column=col, padx=15, pady=5, sticky='w')
        
        # --- Frame para Detalles de Tarjeta/Titular (DNI, Tarjeta, Titular) ---
        self.card_details_frame = ttk.Frame(main_frame, style='Main.TFrame')

        # Frame contenedor para DNI y Titular (ROW 1)
        dni_titular_frame = ttk.Frame(self.card_details_frame, style='Main.TFrame')
        dni_titular_frame.pack(fill='x', pady=(0, 5))
        
        # 1. Columna 0: DNI
        dni_sub_frame = ttk.Frame(dni_titular_frame, style='Main.TFrame')
        dni_sub_frame.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        ttk.Label(dni_sub_frame, text="DNI/NIF del Titular (7 dig.):", font=('Arial', 10, 'bold')).pack(anchor='w')
        self.dni_entry = ttk.Entry(dni_sub_frame, 
                                     textvariable=self.dni_var, 
                                     font=('Consolas', 10), 
                                     width=10, 
                                     validate='key', 
                                     validatecommand=(self.vcmd, '%d', '%i', '%P', '%s', '%S', '%W')) # Validación
        self.dni_entry.pack(fill='x', pady=(0, 5))
        
        # 2. Columna 1: Nombre del Titular
        titular_sub_frame = ttk.Frame(dni_titular_frame, style='Main.TFrame')
        titular_sub_frame.pack(side='left', fill='x', expand=True)
        
        ttk.Label(titular_sub_frame, text="Nombre del Titular:", font=('Arial', 10, 'bold')).pack(anchor='w')
        ttk.Entry(titular_sub_frame, textvariable=self.titular_var, font=('Consolas', 10), width=30).pack(fill='x', pady=(0, 5))

        # 3. Número de Tarjeta (ROW 2 - Full width)
        ttk.Label(self.card_details_frame, text="Número de Tarjeta:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(5,0))
        ttk.Entry(self.card_details_frame, textvariable=self.card_number_var, font=('Consolas', 10), width=40).pack(fill='x', pady=(0, 10))

        
        # --- Botón de Procesar Pago ---
        self.process_button = ttk.Button(main_frame, 
                                         text="Procesar Pago", 
                                         command=self.procesar_pago, 
                                         style='Process.TButton')
        self.process_button.pack(pady=(10, 5), fill='x')

        # --- Botones Adicionales (Boleta y Exportar) ---
        extra_buttons_frame = ttk.Frame(main_frame, style='Main.TFrame')
        extra_buttons_frame.pack(fill='x', pady=(0, 10))
        
        # Botón para Ver Última Boleta
        self.receipt_button = ttk.Button(extra_buttons_frame,
                                         text="Ver Última Boleta",
                                         command=self._generar_boleta,
                                         state='disabled', # Inicialmente deshabilitado
                                         style='Boleta.TButton')
        self.receipt_button.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        # Botón para Exportar a CSV (Exportación manual con diálogo)
        self.export_button = ttk.Button(extra_buttons_frame,
                                         text="Exportar Todos los Movimientos (CSV)",
                                         command=self._export_to_csv,
                                         style='Export.TButton')
        self.export_button.pack(side='right', fill='x', expand=True, padx=(5, 0))


        ttk.Label(main_frame, text="Estado de la Transacción:", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(10, 5))

        self.resultado_text = tk.Text(main_frame, height=3, width=40, state='disabled', 
                                     font=('Arial', 10), bd=1, relief='solid', 
                                     padx=5, pady=5, foreground='#0066CC', background='#E0E0E0')
        self.resultado_text.pack(fill='x')
        
        ttk.Label(main_frame, text="Historial de Pagos (Usuario Actual):", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(15, 5))

        # --- Frame para Historial y Scrollbar ---
        historial_frame = ttk.Frame(main_frame, style='Main.TFrame')
        historial_frame.pack(fill='both', expand=True)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(historial_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.historial_text = tk.Text(historial_frame, height=5, width=40, state='disabled', 
                                     font=('Arial', 10), bd=1, relief='solid', 
                                     padx=5, pady=5, foreground='#333333', background='#F0F0F0',
                                     yscrollcommand=scrollbar.set) # Vincula el texto al scrollbar
        self.historial_text.pack(side=tk.LEFT, fill='both', expand=True)

        # Vincula el scrollbar al texto
        scrollbar.config(command=self.historial_text.yview)

        # Configurar la visibilidad inicial de los campos y el tamaño de la ventana
        self._manejar_seleccion_metodo_pago()

    def _manejar_seleccion_metodo_pago(self):
        """Muestra u oculta el frame de detalles de tarjeta según el método de pago."""
        metodo = self.metodo_var.get()

        # Mostrar campos de tarjeta/DNI/Titular solo para Tarjeta o PayPal
        if metodo in ["Tarjeta", "PayPal"]:
            self.card_details_frame.pack(fill='x', pady=10)
            self.master.geometry("450x780") # Tamaño más grande para campos visibles
        else:
            self.card_details_frame.pack_forget()
            self.master.geometry("450x660") # Tamaño original para campos ocultos

    def _generar_boleta(self):
        """Genera y muestra una boleta (recibo) en una ventana Toplevel."""
        if not self.last_transaction_data:
            messagebox.showinfo("Información", "Primero debe realizar un pago para generar una boleta.")
            return

        data = self.last_transaction_data
        monto = data["monto"]
        metodo = data["metodo"]
        timestamp = data["timestamp"]
        simbolo = data["simbolo"]
        extra_data = data["extra_data"]

        boleta_window = Toplevel(self.master)
        boleta_window.title("Boleta Electrónica de Pago")
        boleta_window.geometry("350x450")
        boleta_window.resizable(False, False)
        boleta_window.transient(self.master)
        boleta_window.grab_set()

        # Estilos para la boleta
        boleta_style = ttk.Style()
        boleta_style.configure('Boleta.TFrame', background='#FFFFFF', borderwidth=2, relief='groove')
        boleta_style.configure('BoletaHeader.TLabel', font=('Courier', 14, 'bold'), foreground='#CC0000', background='#FFFFFF')
        boleta_style.configure('BoletaDetail.TLabel', font=('Courier', 10), background='#FFFFFF', anchor='w')
        boleta_style.configure('BoletaTotal.TLabel', font=('Courier', 12, 'bold'), foreground='#000000', background='#F0F0F0', padding=5)

        boleta_frame = ttk.Frame(boleta_window, padding="20", style='Boleta.TFrame')
        boleta_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # 1. Cabecera
        ttk.Label(boleta_frame, text="TERMINAL BCP STYLE", style='BoletaHeader.TLabel').pack(pady=(0, 10))
        ttk.Label(boleta_frame, text="------------------------------------", font=('Courier', 10), background='#FFFFFF').pack(fill='x')

        # 2. Detalles de Transacción
        txn_id = data.get("txn_id", str(uuid.uuid4())[:8].upper())
        txn_date = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(timestamp))

        details = [
            ("Fecha y Hora:", txn_date),
            ("Transacción ID:", txn_id),
            ("Método de Pago:", metodo),
            ("", "")
        ]

        for label, value in details:
            if label:
                ttk.Label(boleta_frame, text=f"{label.ljust(18)}{value.center(20)}", style='BoletaDetail.TLabel').pack(fill='x')
        
        ttk.Label(boleta_frame, text="------------------------------------", font=('Courier', 10), background='#FFFFFF').pack(fill='x', pady=5)
        
        # 3. Detalles del Cliente (Si aplica)
        card_num = extra_data.get("Tarjeta", "")
        # Enmascarar solo si es una cadena de dígitos de más de 4 caracteres.
        masked_card = f"**** **** **** {card_num[-4:]}" if len(card_num) > 4 and card_num.isdigit() else "N/A"
        
        if metodo in ["Tarjeta", "PayPal"]:
            ttk.Label(boleta_frame, text="[ DATOS DEL CLIENTE ]", font=('Courier', 10, 'bold'), background='#FFFFFF').pack(fill='x', pady=5)
            ttk.Label(boleta_frame, text=f"Titular: {extra_data.get('Titular', 'N/A')}", style='BoletaDetail.TLabel').pack(fill='x')
            ttk.Label(boleta_frame, text=f"DNI/NIF: {extra_data.get('DNI', 'N/A')}", style='BoletaDetail.TLabel').pack(fill='x')
            ttk.Label(boleta_frame, text=f"Tarjeta: {masked_card}", style='BoletaDetail.TLabel').pack(fill='x', pady=(0, 5))
            ttk.Label(boleta_frame, text="------------------------------------", font=('Courier', 10), background='#FFFFFF').pack(fill='x')


        # 4. Total
        total_frame = ttk.Frame(boleta_frame, style='BoletaTotal.TLabel')
        total_frame.pack(fill='x', pady=10)
        
        ttk.Label(total_frame, text="TOTAL PAGADO:", font=('Courier', 12, 'bold'), background='#F0F0F0').pack(side='left')
        ttk.Label(total_frame, text=f"{simbolo}{monto:.2f}", font=('Courier', 14, 'bold'), foreground='#CC0000', background='#F0F0F0').pack(side='right')

        # 5. Mensaje de Status
        ttk.Label(boleta_frame, text="------------------------------------", font=('Courier', 10), background='#FFFFFF').pack(fill='x', pady=5)
        ttk.Label(boleta_frame, text="¡TRANSACCIÓN APROBADA!", font=('Courier', 12, 'bold'), foreground='#008000', background='#FFFFFF').pack(pady=5)
        ttk.Label(boleta_frame, text="Gracias por su pago.", style='BoletaDetail.TLabel').pack(pady=(0, 10))

        # Botón para cerrar
        ttk.Button(boleta_window, text="Cerrar", command=boleta_window.destroy, style='Process.TButton').pack(pady=10)

    def _actualizar_resultado(self, mensaje, borrar=False):
        self.resultado_text.config(state='normal')
        if borrar:
            self.resultado_text.delete('1.0', tk.END)
        self.resultado_text.insert(tk.END, mensaje + "\n")
        self.resultado_text.see(tk.END)
        self.resultado_text.config(state='disabled')

    def _actualizar_historial(self):
        """Actualiza el widget de historial usando self.historial_pagos (la lista del usuario)."""
        self.historial_text.config(state='normal')
        self.historial_text.delete('1.0', tk.END)
        
        # Utilizamos reversed() para mostrar la transacción más reciente primero
        for data in reversed(self.historial_pagos):
            monto = data["monto"]
            metodo = data["metodo"]
            timestamp = data["timestamp"]
            simbolo = data["simbolo"]
            extra_data = data["extra_data"]
            
            # Se incluye la fecha y hora completa en el formato DD/MM/AAAA HH:MM:SS
            fecha_hora_formateada = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(timestamp))
            
            # Línea base de la transacción
            linea = f"[{fecha_hora_formateada}] {simbolo}{monto:.2f} ({metodo})"
            
            # Añadir detalles de tarjeta si existen (solo para Tarjeta/PayPal)
            if extra_data and metodo in ["Tarjeta", "PayPal"]:
                card_num = extra_data.get("Tarjeta", "")
                masked_card = f"**** {card_num[-4:]}" if len(card_num) > 4 and card_num.isdigit() else "N/A"
                
                detalles = []
                if extra_data.get('Titular', ''):
                    detalles.append(f"Titular: {extra_data['Titular']}")
                if extra_data.get('DNI', ''):
                    detalles.append(f"DNI: {extra_data['DNI']}")
                if masked_card != "N/A":
                    detalles.append(f"Tarj: {masked_card}")
                
                if detalles:
                    linea += " | " + ", ".join(detalles)

            # La nueva transacción se inserta al inicio (1.0), por lo que aparece arriba.
            self.historial_text.insert('1.0', linea + "\n")
            
        self.historial_text.config(state='disabled')

    def _write_all_data_to_csv(self, filename):
        """
        Lógica central para escribir datos de TODOS los usuarios a un CSV.
        Esta función es llamada por la exportación manual y la automática.
        """
        # Definir las cabeceras del CSV
        headers = [
            'ID_TRANSACCION', 'FECHA_HORA', 'CELULAR_USUARIO', 'NOMBRE_USUARIO',
            'MONTO', 'SIMBOLO', 'METODO_PAGO', 'DNI_TITULAR', 'NOMBRE_TITULAR', 'NUMERO_TARJETA_COMPLETO'
        ]
        
        total_records = 0
        
        try:
            # Usar 'newline=' para evitar líneas en blanco en Windows, y ';' como delimitador para Excel
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(headers) # Escribir la cabecera

                # Iterar sobre todos los usuarios y sus historiales
                for phone, user_data in self.all_users.items():
                    user_name = user_data.get("name", "Desconocido")
                    history = user_data.get("history", [])

                    for data in history:
                        total_records += 1
                        timestamp = data["timestamp"]
                        # Formato YYYY-MM-DD para fácil clasificación en Excel
                        fecha_hora_formateada = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
                        
                        extra_data = data.get("extra_data", {})
                        
                        row = [
                            data.get("txn_id", 'N/A'),
                            fecha_hora_formateada,
                            phone,
                            user_name,
                            # Usar coma (,) como separador decimal en el string para Excel regional
                            f"{data['monto']:.2f}".replace('.', ','), 
                            data['simbolo'],
                            data['metodo'],
                            extra_data.get('DNI', 'N/A'),
                            extra_data.get('Titular', 'N/A'),
                            extra_data.get('Tarjeta', 'N/A') # Número de tarjeta completo (no enmascarado)
                        ]
                        writer.writerow(row)
            return total_records

        except Exception as e:
            raise Exception(f"Error al escribir el archivo CSV: {e}")


    def _export_to_csv(self):
        """Exporta el historial completo de transacciones de TODOS los usuarios a un archivo CSV (MANUAL)."""
        
        # Usamos filedialog para que el usuario elija dónde guardar el archivo
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Archivos CSV", "*.csv")],
            initialfile="movimientos_exportados.csv",
            title="Guardar Movimientos de Pago"
        )
        
        if not filename:
            return # Cancelado por el usuario

        try:
            total_records = self._write_all_data_to_csv(filename)
            messagebox.showinfo("Exportación Exitosa", f"Se exportaron {total_records} movimientos a:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error de Exportación", str(e))


    def _auto_export_to_csv(self):
        """
        Exporta automáticamente el historial completo a un archivo fijo sin diálogo.
        Responde al requerimiento del usuario "se actualice en mi Exel directamente sin pedir nada".
        """
        try:
            total_records = self._write_all_data_to_csv(AUTO_EXPORT_FILE)
            self._actualizar_resultado(f"💾 Transacción Guardada y Auto-Actualizada en CSV: {AUTO_EXPORT_FILE}", borrar=False)
        except Exception as e:
             # Solo mostrar advertencia en el área de estado, no un messagebox intrusivo
             self._actualizar_resultado(f"⚠️ Advertencia Auto-Guardado CSV: {str(e)}", borrar=False)


    def procesar_pago(self):
        """Procesa el pago, lo registra, guarda la base de datos (JSON) y exporta automáticamente a CSV."""
        try:
            monto = float(self.monto_var.get())
        except ValueError:
            messagebox.showerror("Error", "Monto inválido. Por favor, ingrese un número.")
            return

        if monto <= 0:
            messagebox.showerror("Error", "El monto debe ser positivo.")
            return

        metodo = self.metodo_var.get()
        simbolo = self._obtener_simbolo()

        extra_data = {}
        if metodo in ["Tarjeta", "PayPal"]:
            dni = self.dni_var.get().strip()
            titular = self.titular_var.get().strip()
            card = self.card_number_var.get().strip()

            if not dni or len(dni) != 7 or not dni.isdigit():
                 messagebox.showerror("Error de Validación", "Por favor, ingrese un DNI/NIF válido (7 dígitos).")
                 return
            if not titular:
                messagebox.showerror("Error de Validación", "Por favor, ingrese el nombre del titular.")
                return
            if metodo == "Tarjeta" and (len(card) < 13 or not card.isdigit()):
                messagebox.showerror("Error de Validación", "Por favor, ingrese un número de tarjeta válido.")
                return

            extra_data = {
                "DNI": dni,
                "Titular": titular,
                "Tarjeta": card
            }

        # 1. Ejecutar el pago usando polimorfismo
        metodo_clase = self.opciones_pago[metodo]
        procesador = metodo_clase()
        mensajes = procesador.realizar_pago(monto)

        # 2. Construir datos de la transacción
        transaction_data = {
            "txn_id": str(uuid.uuid4())[:8].upper(),
            "timestamp": time.time(),
            "monto": monto,
            "metodo": metodo,
            "simbolo": simbolo,
            "moneda": self.moneda_var.get(),
            "extra_data": extra_data
        }
        
        # 3. Guardar en el historial (referencia directa al diccionario del usuario)
        self.historial_pagos.append(transaction_data)
        
        # 4. Actualizar la referencia de la última transacción para la boleta
        self.last_transaction_data = transaction_data

        # 5. Actualizar UI
        self._actualizar_resultado("\n".join(mensajes), borrar=True)
        self._actualizar_historial()
        self.receipt_button.config(state='normal')
        
        # 6. PERSISTENCIA: Guardar en el archivo JSON (base de datos)
        # Esto es crucial para que "NO se borre ese base de datos".
        self.save_users_func()
        
        # 7. EXPORTACIÓN AUTOMÁTICA (Respuesta al requerimiento "Actualizar Excel cada rato")
        self._auto_export_to_csv()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()
