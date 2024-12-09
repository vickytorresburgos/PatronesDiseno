from estado import Estado

class MonedaInsertada(Estado):
    def __init__(self, maquina):
        self.maquina = maquina

    def insertar_moneda(self):
        print("ya hay una moneda insertada")

    def seleccionar_producto(self):
        print("producto seleccionado correctamente")
        self.maquina.cambiar_estado(self.maquina.dispensando_producto)

    def soltar_producto(self):
        print("debes seleccionar un producto para soltarlo")


    