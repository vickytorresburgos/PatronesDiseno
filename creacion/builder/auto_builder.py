from abc import ABC, abstractmethod
from auto import Auto

class AutoBuilder(ABC):
    def __init__(self):
        self.auto = Auto()

    @abstractmethod
    def set_motor(self):
        pass

    @abstractmethod
    def set_marca(self):
        pass

    @abstractmethod
    def set_modelo(self):
        pass

    @abstractmethod
    def set_puertas(self):
        pass

    def get_auto(self):
        auto_terminado = self.auto
        self.auto = Auto()
        return auto_terminado