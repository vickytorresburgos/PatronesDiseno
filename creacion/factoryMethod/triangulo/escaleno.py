from triangulo import Triangulo

class Escaleno(Triangulo):
    def get_descripcion(self):
        return "Escaleno"
    
    def get_area(self):
        return self.lado1 + self.lado2 + self.lado3