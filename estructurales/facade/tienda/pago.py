class Pago:
    def validar_pago(self, monto):
        if monto < 0 or monto == 0:
            print("Pago es invalido")
            return False
        else:
            print(f"Pago es valido. El monto es: {monto}")
            return True
        