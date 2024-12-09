from observador import Observador


class Vendedor(Observador):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def actualizar(self):
        print(f"{self.nombre} debes actualizar el stock")