from nivel1 import SoporteNivel1
from nivel2 import SoporteNivel2
from nivel3 import SoporteNivel3


def main():
    nivel1 = SoporteNivel1()
    nivel2 = SoporteNivel2()
    nivel3 = SoporteNivel3()

    nivel1.set_siguiente(nivel2)
    nivel2.set_siguiente(nivel3)

    solicitudes = [
        "restablecer contraseña",
        "problema de instalacion",
        "problema grave"
    ]

    for solicitud in solicitudes:
        print(f"Solicitud: {solicitud}")
        nivel1.manejar_solicitud(solicitud)

if __name__ == "__main__":
    main()