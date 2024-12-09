from fabrica_muebles import FabricaMuebles
from mesa import MesaModerna
from silla import SillaModerna

class FabricaMueblesModernos(FabricaMuebles):
    def crear_mesa(self):
        return MesaModerna()
    
    def crear_silla(self):
        return SillaModerna()