from manejador import Manejador

class SoporteNivel3(Manejador):
    def manejar_solicitud(self, solicitud):
        print(f"Soporte Nivel 3: Atendiendo solicitud: {solicitud}")
