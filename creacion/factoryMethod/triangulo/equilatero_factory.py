from triangulo_factory import TrianguloFactory
from equilatero import Equilatero

class EquilateroFactory(TrianguloFactory):
    def crear_triangulo(self, lado1, lado2, lado3):
        return Equilatero(lado1, lado2, lado3)
    
# subclase que hereda el metodo abstracto donde se crean los objetos