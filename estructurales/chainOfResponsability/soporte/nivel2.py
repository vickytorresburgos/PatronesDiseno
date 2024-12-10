from manejador import Manejador

class SoporteNivel2(Manejador):
    def manejar_solicitud(self, solicitud):
        if solicitud == "problema de instalacion":
            print("Soporte Nivel 2: Instalacion realizada con exito")

        else:
            print("Soporte Nivel 2: No puedo manejar esa solicitud")
            super().manejar_solicitud(solicitud)