from moneda_insertada import MonedaInsertada
from moneda_no_insertada import MonedaNoInsertada
from dispensando_producto import DispensandoProducto

class MaquinaExpendedora:
    def __init__(self):
        self.sin_moneda = MonedaNoInsertada(self)
        self.moneda_insertada = MonedaInsertada(self)
        self.dispensando_producto = DispensandoProducto(self)

        self.estado_actual = self.sin_moneda

    def cambiar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado

    def insertar_moneda(self):
        self.estado_actual.insertar_moneda()

    def seleccionar_producto(self):
        self.estado_actual.seleccionar_producto()
    
    def soltar_producto(self):
        self.estado_actual.soltar_producto()