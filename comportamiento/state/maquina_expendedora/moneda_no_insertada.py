from estado import Estado

class MonedaNoInsertada(Estado):
    def __init__(self, maquina):
        self.maquina = maquina

    def insertar_moneda(self):
        print("moneda insertada correctamente")
        self.maquina.cambiar_estado(self.maquina.moneda_insertada)

    def seleccionar_producto(self):
        print("debes insertar una moneda para seleccionar un producto")

    def soltar_producto(self):
        print("debes insertar una moneda para soltar un producto")
