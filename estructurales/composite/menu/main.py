from plato import Plato
from promo import Promo


def main():
    plato1 = Plato("Coca Cola", 200)    
    plato2 = Plato("Hamburguesa", 300)    
    plato3 = Plato("Papas Fritas", 400)    
    plato4 = Plato("Pancho", 100) 

    promo1 = Promo("Combo Hamburguesa")

    promo1.agregar_elementos(plato1)
    promo1.agregar_elementos(plato2)
    promo1.agregar_elementos(plato3)
    promo1.calcular_total()

    promo2 = Promo("Combo Panchos")

    promo2.agregar_elementos(plato4)
    promo2.agregar_elementos(plato1)
    promo2.agregar_elementos(plato3)
    promo2.calcular_total()

    promo3 = Promo("Combo XXL")

    promo3.agregar_elementos(promo1)
    promo3.agregar_elementos(promo2)

    promo1.mostrar_detalles()
    promo2.mostrar_detalles()
    promo3.mostrar_detalles()


if __name__ == "__main__":
    main()        




