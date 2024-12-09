from triangulo_factory import TrianguloFactory
from isosceles import Isosceles

class IsoscelesFactory(TrianguloFactory):
    def crear_triangulo(self, lado1, lado2, lado3):
        return Isosceles(lado1, lado2, lado3)