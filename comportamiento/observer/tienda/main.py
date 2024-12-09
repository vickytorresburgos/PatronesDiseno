from comprador import Comprador
from vendedor import Vendedor
from producto import Producto

def main():
    producto = Producto("Microondas BGH")

    cliente = Comprador("Juan")
    vendedor = Vendedor("Marta")

    producto.adjuntar(cliente)
    producto.adjuntar(vendedor)

    producto.cambiar_disponibilidad(True)

    producto.eliminar(vendedor)
    producto.cambiar_disponibilidad(False)

if __name__ == "__main__":
    main()