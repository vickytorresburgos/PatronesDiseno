class Envio:
    def validar_envio(self, direccion):
        if direccion == "":
            print("Direccion es invalida")
            return False
        else:
            print(f"Direccion es valida. La direccion de envio es: {direccion}")
            return True