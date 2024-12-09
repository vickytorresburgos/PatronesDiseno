from facade import TiendaFacade

def main():
    carrito = []
    direccion = "Rioja 467"
    monto = 1000

    facade = TiendaFacade()
    compra = facade.procesar_pedido(carrito, direccion, monto)
    print(compra)

if __name__ == "__main__":
    main()