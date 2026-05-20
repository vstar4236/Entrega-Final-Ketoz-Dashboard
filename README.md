# 📦 Ketoz Logística - Ecosistema Integral & Business Intelligence

Este repositorio contiene la entrega final para la **Clase 12: Dashboard (Proyecto Final)**. Representa el ecosistema tecnológico End-to-End para la gestión, clasificación y análisis de envíos B2B de repuestos de motocicletas.

## 🏗️ Arquitectura del Proyecto
El sistema está dividido en cuatro capas funcionales:

1. **Frontend (`app_envios.py`):** Interfaz gráfica en Tkinter con procesamiento de imágenes (Pillow) y validación estricta de reglas de negocio.
2. **Backend (`logistica.py` & `database.py`):** Lógica orientada a objetos para el cálculo de fletes y categorización de carga.
3. **Base de Datos (`ketoz_logistica.db`):** Motor SQLite que garantiza la persistencia segura de los manifiestos generados.
4. **Inteligencia de Negocios (`Ketoz_MVP_Final.pbix`):** Dashboard en Power BI construido bajo un **Modelo Estrella**, con integración de una Tabla Calendario y medidas DAX avanzadas (Inteligencia de Tiempo, CALCULATE, DIVIDE) para responder a preguntas clave del negocio.

## 👥 Integrantes del Grupo
* **Matías Mondragón** (Líder de Proyecto)
* **Arianne Amorocho**
* **Mariana Peña**

## 🚀 Instrucciones de Ejecución (Python)
1. Instalar dependencias necesarias: `pip install Pillow`
2. Ejecutar el orquestador principal: `python main.py`

## ⚠️ Nota Técnica para Evaluación (Power BI)
El ecosistema backend en Python (`main.py` y `database.py`) ya está configurado con rutas relativas (`os.path.dirname`) y funcionará automáticamente al clonar el repositorio. 

Sin embargo, dado que Power BI almacena rutas absolutas en Power Query, al abrir el archivo `.pbix` por primera vez es necesario actualizar la ruta del origen de datos para que el Dashboard funcione correctamente:
1. Abrir Power BI Desktop.
2. Ir a **Inicio > Transformar datos > Configuración de origen de datos**.
3. Seleccionar la ruta actual y hacer clic en **Cambiar origen**.
4. Buscar y seleccionar el archivo `ketoz_logistica.db` incluido en la carpeta de este repositorio.
5. Cerrar y presionar **Actualizar**.

---
*Desarrollado para el Tercer Corte - Universidad de La Sabana (2026).*
