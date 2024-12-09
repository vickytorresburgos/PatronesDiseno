from database import Database

class RealDatabase(Database):
    def __init__(self):
        self.datos = {
            "usuario1": "Datos de usuario1",
            "usuario2": "Datos de usuario2"
        }

    def consultar_datos(self, usuario):
        return self.datos.get(usuario, "Usuario no encontrado")