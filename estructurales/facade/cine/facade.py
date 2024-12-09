from pantalla import Pantalla
from luces import Luces
from sonido import Sonido

class CineFacade:
    def __init__(self):
        self.pantalla = Pantalla()
        self.luces = Luces()
        self.sonido = Sonido()

    def procesar_cine(self, pantalla, luces, parlantes):
        if not self.pantalla.validar_pantalla(pantalla):
            return "La pantalla no funciona"
        
        if not self.luces.validar_luces(luces):
            return "Las luces no funcionan"
        
        if not self.sonido.validar_sonido(parlantes):
            return "Los parlantes no funcionan"

        else:
            return "La pelicula puede reproducirse correctamente"