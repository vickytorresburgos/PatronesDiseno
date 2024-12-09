from triangulo_factory import TrianguloFactory
from escaleno import Escaleno

class EscalenoFactory(TrianguloFactory):
    def crear_triangulo(self, lado1, lado2, lado3):
        return Escaleno(lado1, lado2, lado3)