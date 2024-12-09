from abc import abstractmethod

class Triangulo: #superclase 
    @abstractmethod
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    @abstractmethod
    def get_descripcion(self): #metodos abstractos
        pass

    @abstractmethod
    def get_area(self):
        pass