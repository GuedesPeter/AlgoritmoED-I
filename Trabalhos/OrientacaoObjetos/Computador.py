from abc import ABC,abstractmethod

class Computador(ABC):
    def __init__(self,modelo=None,cor=None): 
        self.modelo = modelo
        self.cor = cor

    def getInformacoes(self):
        return print(f'Modelo: {self.modelo}\nCor: {self.cor}')
    
    @abstractmethod
    def cadastrar(self):
        pass  