from maquina_expendedora import MaquinaExpendedora

def main():
    maquina = MaquinaExpendedora()

    print("----proceso de compra----")

    maquina.seleccionar_producto()
    maquina.insertar_moneda()
    maquina.seleccionar_producto()
    maquina.soltar_producto()

    print("----proceso de compra sin moneda----")
    maquina.seleccionar_producto()
    

if __name__ == "__main__":
    main()