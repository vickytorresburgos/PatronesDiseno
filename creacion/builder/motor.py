class Motor:
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        self.potencia = potencia

    def __str__(self):
        return f"Motor: {self.modelo}, Potencia: {self.potencia}"
