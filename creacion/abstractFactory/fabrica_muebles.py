from abc import ABC, abstractmethod

class FabricaMuebles(ABC):
    @abstractmethod
    def crear_silla(self):
        pass

    @abstractmethod
    def crear_mesa(self):
        pass