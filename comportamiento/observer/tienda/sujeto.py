class Sujeto:
    def __init__(self):
        self.observadores = []

    def adjuntar(self, observador):
        self.observadores.append(observador)

    def eliminar(self, observador):
        self.observadores.remove(observador)
    
    def notificar(self):
        for observador in self.observadores:
            observador.actualizar()