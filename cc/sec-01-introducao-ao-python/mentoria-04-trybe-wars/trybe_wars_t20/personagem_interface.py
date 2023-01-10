from abc import ABC, abstractmethod


class PersonagemInterface(ABC):
    @abstractmethod
    def fala(self):
        raise NotImplementedError
