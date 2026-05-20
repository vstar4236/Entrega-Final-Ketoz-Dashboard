import tkinter as tk
from Backend.database import inicializar_db
from Frontend.app_envios import AppLogistica

def iniciar_aplicacion():
    # 1. Aseguramos que la base de datos exista antes de lanzar la interfaz
    inicializar_db()
    
    # 2. Inicializamos la ventana de Tkinter
    root = tk.Tk()
    
    # 3. Lanzamos nuestra clase del Frontend
    app = AppLogistica(root)
    
    # 4. Mantenemos la aplicación abierta
    root.mainloop()

if __name__ == '__main__':
    iniciar_aplicacion()