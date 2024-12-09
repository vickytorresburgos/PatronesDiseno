from sujeto import Sujeto

class Producto(Sujeto):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = False

    def cambiar_disponibilidad(self, estado):
        self.disponible = estado
        print(f"El producto: {self.nombre} ahora esta {'disponible' if estado else 'agotado'}.")

