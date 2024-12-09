from estado import Estado

class DispensandoProducto(Estado):
    def __init__(self, maquina):
        self.maquina = maquina

    def insertar_moneda(self):
        print("dispensando producto")

    def seleccionar_producto(self):
        print("dispensando producto")

    def soltar_producto(self):
        print("producto dispensado")
        self.maquina.cambiar_estado(self.maquina.sin_moneda)
