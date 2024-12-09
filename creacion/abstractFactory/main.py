from fabrica_muebles_modernos import FabricaMueblesModernos
from fabrica_muebles_victorianos import FabricaMueblesVictorianos

def main():
    fabrica_muebles_modernos = FabricaMueblesModernos()
    fabrica_muebles_victorianos = FabricaMueblesVictorianos()

    print("Muebles Modernos")
    mesa = fabrica_muebles_modernos.crear_mesa()
    mesa.tiene_patas()

    silla = fabrica_muebles_modernos.crear_silla()
    silla.tiene_patas()

    print("Muebles Victorianos")
    mesa = fabrica_muebles_victorianos.crear_mesa()
    mesa.tiene_patas()

    silla = fabrica_muebles_victorianos.crear_silla()
    silla.tiene_patas()

if __name__ == "__main__":
    main()

