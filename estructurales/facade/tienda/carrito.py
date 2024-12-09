class Carrito:
    def validar_carrito(self, carrito):
        if len(carrito) == 0:
            print("Carrito es invalido")
            return False
        else:
            print("Carrito es valido")