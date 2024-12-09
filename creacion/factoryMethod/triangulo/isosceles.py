from triangulo import Triangulo

class Isosceles(Triangulo):
    def get_descripcion(self):
        return "Isosceles"
    
    def get_area(self):
        return self.lado1 + self.lado2 + self.lado3