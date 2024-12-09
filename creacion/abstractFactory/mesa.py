from abc import abstractmethod, ABC

class Mesa(ABC):
    @abstractmethod
    def tiene_patas(self):
        pass

class MesaVictoriana(Mesa):
    def tiene_patas(self):
        print("Pongo el mantel en una mesa victoriana")

class MesaModerna(Mesa):
    def tiene_patas(self):
        print("Pongo el mantel en una mesa moderna")

