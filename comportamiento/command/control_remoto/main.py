from control_remoto import ControlRemoto
from dispositivos import Luz, Ventilador
from concrete_command import EncenderLuz, ApagarLuz, EncenderVentilador, ApagarVentilador

def main():
    luz = Luz()
    ventilador = Ventilador()

    encender_luz = EncenderLuz(luz)
    apagar_luz = ApagarLuz(luz)

    control_remoto = ControlRemoto()

    print("----Control de la luz----")

    control_remoto.asignar_comando(encender_luz)
    control_remoto.apretar_boton()
    control_remoto.apretar_deshacer()

    encender_ventilador = EncenderVentilador(ventilador)
    apagar_ventilador = ApagarVentilador(ventilador)

    print("----Control del ventilador----")

    control_remoto.asignar_comando(encender_ventilador)
    control_remoto.apretar_boton()
    control_remoto.apretar_deshacer()


if __name__ == "__main__":
    main()