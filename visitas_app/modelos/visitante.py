class Visitante:
    def __init__(self, cedula: str, nombre: str, motivo: str):
        # Al usar las propiedades (setters), forzamos la validación
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo
    
    @property
    def cedula(self) -> str:
        return self._cedula
    
    @cedula.setter
    def cedula(self, value: str):
        # Validación: una cédula no puede estar vacía
        if not value or not value.strip():
            raise ValueError("La cédula no puede estar vacía.")
        self._cedula = value.strip()
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str):
        # Validación: un nombre no puede estar vacío
        if not value or not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value.strip()
    
    @property
    def motivo(self) -> str:
        return self._motivo
    
    @motivo.setter
    def motivo(self, value: str):
        # El motivo puede ser vacío pero se limpia de espacios
        self._motivo = value.strip() if value else ""
    
    def __str__(self):
        return f"Visitante(cedula={self.cedula}, nombre={self.nombre}, motivo={self.motivo})"