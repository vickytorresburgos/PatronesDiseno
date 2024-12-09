from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def insertar_moneda(self):
        pass

    @abstractmethod
    def seleccionar_producto(self):
        pass

    @abstractmethod
    def soltar_producto(self):
        pass

    