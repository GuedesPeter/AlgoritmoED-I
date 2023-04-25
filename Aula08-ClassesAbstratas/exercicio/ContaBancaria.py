from abc import ABC,abstractmethod

class ContaBancaria(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def depositar(self):
        pass