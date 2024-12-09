from database import Database
from database_real import RealDatabase

class ProxyDatabase(Database):
    def __init__(self):
        self.database_real = RealDatabase()
        self.usuario_permitidos = {
            "admin": "1234",
            "usuario1": "4567"
        }
    
    def verificar_acceso(self, usuario, contraseña):
        return self.usuario_permitidos.get(usuario) == contraseña
    
    def consultar_datos(self, usuario, contraseña):
        if self.verificar_acceso(usuario, contraseña):
            return self.database_real.consultar_datos(usuario)
        return "Acceso denegado"