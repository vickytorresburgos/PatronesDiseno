from command import Command

class EncenderLuz(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.encender()

    def undo(self):
        self.luz.apagar()

class ApagarLuz(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.apagar()
    
    def undo(self):
        self.luz.encender()
    
class EncenderVentilador(Command):
    def __init__(self, ventilador):
        self.ventilador = ventilador
    
    def execute(self):
        self.ventilador.encender()
    
    def undo(self):
        self.ventilador.apagar()

class ApagarVentilador(Command):
    def __init__(self, ventilador):
        self.ventilador = ventilador

    def execute(self):
        self.ventilador.apagar()

    def undo(self):
        self.ventilador.encender()