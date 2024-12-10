from manejador import Manejador

class SoporteNivel1(Manejador):
    def manejar_solicitud(self, solicitud):
        if solicitud == "restablecer contraseña":
            print("Soporte Nivel 1: Contraseña restablecida")

        else:
            print("Soporte Nivel 1: No puedo manejar esa solicitud")
            super().manejar_solicitud(solicitud)