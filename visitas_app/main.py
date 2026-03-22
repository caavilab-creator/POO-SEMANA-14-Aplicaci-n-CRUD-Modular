from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas


def main():
    # Crear las dependencias
    visita_servicio = VisitaServicio()
    
    # Inyectar el servicio en la UI (Inyección de Dependencias)
    app = AppVisitas(visita_servicio)
    
    # Iniciar el loop principal de Tkinter
    app.mainloop()


if __name__ == "__main__":
    main()