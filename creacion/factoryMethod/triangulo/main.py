from equilatero_factory import EquilateroFactory
from escaleno_factory import EscalenoFactory
from isosceles_factory import IsoscelesFactory

def main():
    equilatero = EquilateroFactory()
    escaleno = EscalenoFactory()
    isosceles = IsoscelesFactory()

    # los objetos se instancian desde los creadores

    print(equilatero.crear_triangulo(1,2,3).get_descripcion())
    print(equilatero.crear_triangulo(1,2,3).get_area())
    
    print(escaleno.crear_triangulo(3,4,5).get_descripcion())
    print(escaleno.crear_triangulo(3,4,5).get_area())
   
    print(isosceles.crear_triangulo(4,4,5).get_descripcion())
    print(isosceles.crear_triangulo(4,4,5).get_area())

if __name__ == '__main__':
    main()
