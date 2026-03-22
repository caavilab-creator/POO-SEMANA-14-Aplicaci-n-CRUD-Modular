# Sistema de Registro de Visitantes

Aplicación CRUD modular desarrollada en Python con Tkinter para gestionar el flujo de personas en una oficina.

## 📋 Características

- Registrar nuevos visitantes
- Visualizar lista de visitantes en tabla
- Eliminar registros
- Validación de datos

## 📁 Estructura del Proyecto

visitas_app/
├── main.py # Punto de entrada
├── modelos/
│ └── visitante.py # Clase Visitante
├── servicios/
│ └── visita_servicio.py # Lógica CRUD
└── ui/
└── app_tkinter.py # Interfaz gráfica

## 🚀 Ejecución

1. Navegar a la carpeta del proyecto:
```bash
cd visitas_app
python main.py