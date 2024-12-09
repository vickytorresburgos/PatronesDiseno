from facade import CineFacade

def main():
    luces = True
    pantalla = True
    parlantes = True

    facade = CineFacade()
    pelicula = facade.procesar_cine(pantalla, luces, parlantes)
    print(pelicula)

if __name__ == "__main__":
    main()