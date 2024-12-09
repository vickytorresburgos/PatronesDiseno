from elemento_menu import ElementoMenu

class Promo(ElementoMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar_elementos(self, elementos):
        self.elementos.append(elementos)

    def eliminar_elementos(self, elementos):
        self.elementos.remove(elementos)
    
    def mostrar_detalles(self):
        print(f"Promo: {self.nombre}")
        for elemento in self.elementos:
            elemento.mostrar_detalles()
        print((f"Nombre de la promo: {self.nombre} Precio: ${self.calcular_total()}"))

    def obtener_precio(self):
        return self.calcular_total()
    
    def calcular_total(self):
        return sum([elemento.obtener_precio() for elemento in self.elementos])