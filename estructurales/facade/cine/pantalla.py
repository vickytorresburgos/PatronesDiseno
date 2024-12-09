class Pantalla:
    def validar_pantalla(self, pantalla):
        if not pantalla:
            print("La pantalla no funciona")
            return False
        else:
            print("La pantalla funciona correctamente")
            return True