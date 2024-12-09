from abc import ABC, abstractmethod

class TrianguloFactory(ABC):
    @abstractmethod
    def crear_triangulo(self, lado1, lado2, lado3):
        pass

# clase creadora, donde se crean los objetos con un metodo abstracto