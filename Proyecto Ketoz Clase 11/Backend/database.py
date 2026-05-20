import sqlite3
import os

# Definimos la ruta absoluta para que la BD siempre se cree en la carpeta Backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "ketoz_logistica.db")

def inicializar_db():
    print("⚙️ Inicializando Base de Datos...")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS envios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                destino TEXT,
                peso REAL,
                categoria TEXT,
                costo REAL
            )
        ''')
        conn.commit()
    print("✅ Base de datos lista.")