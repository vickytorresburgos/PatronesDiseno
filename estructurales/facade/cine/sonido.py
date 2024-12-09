class Sonido:
    def validar_sonido(self, parlantes):
        if not parlantes:
            print("Los parlantes funcionan correctamente")
            return False
        else:
            print("Los parlantes no funcionan correctamente")
            return True
