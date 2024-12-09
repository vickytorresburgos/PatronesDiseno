from fabrica_muebles import FabricaMuebles
from mesa import MesaVictoriana
from silla import SillaVictoriana

class FabricaMueblesVictorianos(FabricaMuebles):
    def crear_mesa(self):
        return MesaVictoriana()

    def crear_silla(self):
        return SillaVictoriana()