#CLASSE ABSTRATA
from abc import ABC, abstractmethod # IMPORTANDO SINALIZADORES DE CLASSE ABSTRATA

class Veiculo(ABC): # SINALIZADOR QUE INDICA QUE ESTA CLASSE É ABSTRATA -  (ABC)
    def __init__(self,modelo = None,ano = None):
        self.modelo = modelo 
        self.ano = ano

    def imprimir(self):
        print('Modelo: ',self.modelo)
        print('Ano: ',self.ano)

    @abstractmethod # DECLARA O METODO COMO ABSTRATO
    def imprimirEspecifico(self):
        pass