from empleado_normal import EmpladoNormal
from gerente import Gerente

def main():
    empleado1 = EmpladoNormal("Juan", "Administrativo")
    empleado2 = EmpladoNormal("Laura", "Diseñadora")
    empleado3 = EmpladoNormal("Martin", "Operativo")
    empleado4 = EmpladoNormal("Martina", "QA")
    empleado5 = EmpladoNormal("Alberto", "Desarrollo")

    gerente1 = Gerente("Marcelo", "Jefe de Desarrollo")
    gerente2 = Gerente("Mariana", "Directora General")

    gerente1.agregar_empleado(empleado1)
    gerente1.agregar_empleado(empleado2)

    gerente2.agregar_empleado(empleado3)
    gerente2.agregar_empleado(empleado4)
    gerente2.agregar_empleado(gerente1)

    gerente2.get_detalles()

    gerente1.get_detalles()

if __name__ == "__main__":
    main()        