from observador import Observador

class Comprador(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self):
        print(f"{self.nombre}, el producto esta disponible")