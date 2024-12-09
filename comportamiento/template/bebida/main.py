from bebida import BebidaCaliente
from cafe import Cafe
from te import Te
from chocolate import Chocolate

def main():
    print("Bienvenido a la tienda de bebidas calientes")
    print("-----------------------------------------")
    print("--- Preparando Té ---")

    te = Te()
    te.preparar()

    print("--- Preparando Café ---")

    cafe = Cafe()
    cafe.preparar()

    print("--- Preparando Chocolate Caliente ---")

    chocolate = Chocolate()
    chocolate.preparar()


if __name__ == "__main__":
    main()

 