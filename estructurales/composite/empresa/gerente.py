from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
        self.subordinados = []

    def agregar_empleado(self, empleado):
        self.subordinados.append(empleado)

    def eliminar_empleado(self, empleado):
        self.subordinados.remove(empleado)

    def get_detalles(self, nivel=0):
        print(f"{'   ' * nivel}- {self.puesto}: {self.nombre}")
        for empleado in self.subordinados:
            empleado.get_detalles(nivel = nivel + 1)