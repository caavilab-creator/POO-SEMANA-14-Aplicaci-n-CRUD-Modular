from modelos.visitante import Visitante
from typing import List, Optional


class VisitaServicio:
    def __init__(self):
        # Base de datos en memoria
        self._visitantes: List[Visitante] = []
    
    def registrar_visitante(self, visitante: Visitante) -> None:
        # La validación de campos vacíos ya la hizo el modelo Visitante.
        # Aquí solo validamos reglas de negocio (duplicados).
        if self._obtener_por_cedula(visitante.cedula):
            raise ValueError(f"Ya existe un visitante registrado con la cédula {visitante.cedula}.")
        self._visitantes.append(visitante)
    
    def obtener_todos(self) -> List[Visitante]:
        # Devuelve la lista actual de visitantes
        return self._visitantes
    
    def actualizar_visitante(self, visitante_actualizado: Visitante) -> None:
        # Buscamos el índice y el objeto al mismo tiempo
        for i, v in enumerate(self._visitantes):
            if v.cedula == visitante_actualizado.cedula:
                # Actualizamos el objeto en la lista
                self._visitantes[i] = visitante_actualizado
                return
        # Si termina el bucle y no hizo 'return', lanzamos error
        raise ValueError("No se encontró el visitante para actualizar.")
    
    def eliminar_visitante(self, cedula: str) -> None:
        visitante = self._obtener_por_cedula(cedula)
        if visitante:
            self._visitantes.remove(visitante)
        else:
            raise ValueError("El visitante no existe o ya fue eliminado.")
    
    def _obtener_por_cedula(self, cedula: str) -> Optional[Visitante]:
        # Método auxiliar privado que retorna un Visitante o None si no existe
        for v in self._visitantes:
            if v.cedula == cedula:
                return v
        return None