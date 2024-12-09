from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def consultar_datos(self):
        pass