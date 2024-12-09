class ControlRemoto:
    def __init__(self):
        self.comando_actual = None
    
    def asignar_comando(self, comando):
        self.comando_actual = comando
    
    def apretar_boton(self):
        if self.comando_actual:
            self.comando_actual.execute()

    def apretar_deshacer(self):
        if self.comando_actual:
            self.comando_actual.undo()