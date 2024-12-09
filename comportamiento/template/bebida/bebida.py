from abc import ABC, abstractmethod

class BebidaCaliente(ABC):
    def preparar(self):
        self.hervir_agua()
        self.agregar_ingredientes()
        self.mezclar()
        self.servir()

    def hervir_agua(self):
        print("Hirviendo agua")
    
    @abstractmethod
    def agregar_ingredientes(self):
        print("Agregando ingredientes")

    def mezclar(self):
        print("Mezclando")

    def servir(self):
        print("Serviendo")