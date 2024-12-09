from typing_extensions import override
from auto_builder import AutoBuilder
from motor import Motor
from auto import Auto

class FordBuilder(AutoBuilder):
    def set_marca(self):
        self.auto.marca = "Ford"
    
    def set_modelo(self):
        self.auto.modelo = "Fiesta"
    
    def set_puertas(self):
        self.auto.puertas = 3
    
    def set_motor(self):
        self.auto.motor = Motor("V8", "700 HP")