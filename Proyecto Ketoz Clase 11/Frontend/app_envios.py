import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from Backend.logistica import RegistroEnvios

class AppLogistica:
    def __init__(self, root):
        self.root = root
        self.root.title("Ketoz - Sistema de Clasificación Logística")
        self.root.geometry("400x550")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)

        self.construir_gui()

    def construir_gui(self):
        # --- 1. PROCESAMIENTO DE IMÁGENES (Librería Pillow) ---
        try:
            # Buscamos el logo dinámicamente en la carpeta Frontend
            base_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(base_dir, "logo.png")
            
            # Cargamos y redimensionamos la imagen con Pillow
            imagen_pil = Image.open(logo_path)
            imagen_pil = imagen_pil.resize((150, 150), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(imagen_pil)
            
            lbl_logo = tk.Label(self.root, image=self.logo_img, bg="#f4f4f4")
            lbl_logo.pack(pady=15)
        except Exception:
            # Si olvidan poner el archivo logo.png, el programa no colapsa
            lbl_logo = tk.Label(self.root, text="🏍️ KETOZ LOGÍSTICA", font=("Arial", 16, "bold"), bg="#f4f4f4")
            lbl_logo.pack(pady=20)

        # --- 2. TÍTULO Y CAMPOS DE ENTRADA ---
        tk.Label(self.root, text="Registro de Envío B2B", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#333").pack(pady=5)

        # Destino (Usamos Combobox para evitar errores de tipeo del usuario)
        tk.Label(self.root, text="Destino del Repuesto:", font=("Arial", 11), bg="#f4f4f4").pack(pady=5)
        self.cmb_destino = ttk.Combobox(self.root, values=["Bogota", "Medellin", "Cali", "Barranquilla", "Bucaramanga"], state="readonly", font=("Arial", 11))
        self.cmb_destino.pack(pady=5)

        # Peso (Entry normal)
        tk.Label(self.root, text="Peso del Paquete (kg):", font=("Arial", 11), bg="#f4f4f4").pack(pady=5)
        self.entry_peso = tk.Entry(self.root, font=("Arial", 11), justify="center")
        self.entry_peso.pack(pady=5)

        # --- 3. BOTONES ---
        # Botón de Registrar
        btn_registrar = tk.Button(self.root, text="📦 Generar Manifiesto", bg="#2a9d8f", fg="white", font=("Arial", 12, "bold"), cursor="hand2", command=self.registrar_evento)
        btn_registrar.pack(pady=20, fill="x", padx=50)

        # Botón de Limpiar
        btn_limpiar = tk.Button(self.root, text="🧹 Limpiar Campos", bg="#e76f51", fg="white", font=("Arial", 10), cursor="hand2", command=self.limpiar_formulario)
        btn_limpiar.pack(pady=5, fill="x", padx=100)

    # --- 4. SEGURIDAD Y EVENTOS (try-except) ---
    def registrar_evento(self):
        destino = self.cmb_destino.get().strip()
        peso_str = self.entry_peso.get().strip()

        try:
            # Validación 1: Campos vacíos
            if not destino or not peso_str:
                raise ValueError("Por favor complete todos los campos (Destino y Peso).")
            
            # Validación 2: Formato del peso numérico
            try:
                peso = float(peso_str)
            except ValueError:
                raise ValueError("El peso debe ser un número válido (ej: 12.5).")

            # Validación 3: Lógica de negocio
            if peso <= 0:
                raise ValueError("El peso debe ser mayor a 0 kg.")

            # Clasificación Logística
            if peso < 2:
                categoria = 'Documento'
                costo = 5000
            elif peso <= 20:
                categoria = 'Paqueteria'
                costo = 15000
            else:
                categoria = 'Carga'
                costo = 50000

            # Guardar en Base de Datos conectando con el Backend
            RegistroEnvios.guardar_envio(destino, peso, categoria, costo)

            # Alerta de Éxito
            mensaje_exito = f"El paquete ha sido registrado en la base de datos.\n\nDestino: {destino}\nCategoría: {categoria}\nCosto: ${costo}"
            messagebox.showinfo("✅ Envío Registrado", mensaje_exito)
            
            self.limpiar_formulario()

        except ValueError as ve:
            # Alertas de error humano (Validaciones)
            messagebox.showwarning("⚠️ Advertencia", str(ve))
        except Exception as e:
            # Alertas de error de sistema (Base de datos o Python)
            messagebox.showerror("❌ Error Crítico", f"Ha ocurrido un error inesperado:\n{e}")

    def limpiar_formulario(self):
        self.cmb_destino.set('')
        self.entry_peso.delete(0, tk.END)