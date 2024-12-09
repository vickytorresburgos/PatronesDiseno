from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def get_detalles(self, nivel = 0):
        pass
