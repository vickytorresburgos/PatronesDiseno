from auto_builder import AutoBuilder
from motor import Motor

class FiatBuilder(AutoBuilder):
    def set_marca(self):
        self.auto.marca = "Fiat"
    
    def set_modelo(self):
        self.auto.modelo = "Cronos"
    
    def set_puertas(self):
        self.auto.puertas = 4
    
    def set_motor(self):
        self.auto.motor = Motor("V6", "500 HP")