from abc import abstractmethod, ABC

class Silla(ABC):
    @abstractmethod
    def tiene_patas(self):
        pass

class SillaVictoriana(Silla):
    def tiene_patas(self):
        print("Me siento en una silla victoriana")

class SillaModerna(Silla):
    def tiene_patas(self):
        print("Me siento en una silla moderna")

