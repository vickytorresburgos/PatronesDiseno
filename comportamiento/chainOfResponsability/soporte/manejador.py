class Manejador:
    def __init__(self):
        self.siguiente = None

    def set_siguiente(self, manejador):
        self.siguiente = manejador

    def manejar_solicitud(self, solicitud):
        if self.siguiente:
            self.siguiente.manejar_solicitud(solicitud)
