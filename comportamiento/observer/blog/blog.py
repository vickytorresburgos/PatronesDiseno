class Blog:
    def __init__(self):
        self.suscriptores = []

    def agregar_suscriptor(self, suscriptor):
        self.suscriptores.append(suscriptor)

    def eliminar_suscriptor(self, suscriptor):
        self.suscriptores.remove(suscriptor)

    def notificar(self, titulo):
        for suscriptor in self.suscriptores:
            suscriptor.actualizar(titulo)

    def publicar(self, titulo):
        print(f"Publicando articulo: {titulo}")
        self.notificar(titulo)