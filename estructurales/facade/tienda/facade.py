from carrito import Carrito
from envio import Envio
from pago import Pago

class TiendaFacade:
    def __init__(self):
        self.carrito = Carrito()
        self.envio = Envio()
        self.pago = Pago()

    def procesar_pedido(self, carrito, direccion, monto):
        if self.carrito.validar_carrito(carrito) == False:
            return "Error al validar carrito"

        if self.envio.validar_envio(direccion) == False:
            return "Error al validar el envio"

        if self.pago.validar_pago(monto) == False:
            return "Error al validar el pago"        
        else:
            return "Pedido procesado correctamente"
