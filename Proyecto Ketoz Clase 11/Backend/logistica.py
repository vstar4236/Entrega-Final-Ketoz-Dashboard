import sqlite3
from Backend.database import DB_NAME

class RegistroEnvios:
    @staticmethod
    def guardar_envio(destino, peso, categoria, costo):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO envios (destino, peso, categoria, costo)
                VALUES (?, ?, ?, ?)
            ''', (destino, peso, categoria, costo))
            conn.commit()