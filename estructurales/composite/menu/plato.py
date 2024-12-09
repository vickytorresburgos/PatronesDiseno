from elemento_menu import ElementoMenu

class Plato(ElementoMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre} Precio: {self.precio}")

    def obtener_precio(self):
        return self.precio    