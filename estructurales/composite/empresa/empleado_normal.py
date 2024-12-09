from empleado import Empleado

class EmpladoNormal(Empleado):
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def get_detalles(self, nivel = 0):
        print(f"{'   ' * nivel}- {self.puesto}: {self.nombre}")