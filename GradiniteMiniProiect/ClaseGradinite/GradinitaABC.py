from abc import ABC, abstractmethod

class GradinitaABC(ABC):  # Punem ABC dupa clasa , ca sa stim ca metoda este abstracta/o clasa abstracta

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplemented('Metoda nu este implementata')




























