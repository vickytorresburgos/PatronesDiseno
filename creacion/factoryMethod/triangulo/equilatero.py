from triangulo import Triangulo

class Equilatero(Triangulo): #subclase de clase Triangulo
    def get_descripcion(self):
        return "Equilatero" 

#subclase redefine(implementa) los metodos abstractos heredados, una vez que se implementan dejan de ser abstractos
# si una subclase no implementa los metodos abstractos heredados, ella misma sera abstracta
    
    def get_area(self):
        return self.lado1 + self.lado2 + self.lado3