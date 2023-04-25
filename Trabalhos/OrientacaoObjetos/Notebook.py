from Computador import Computador

class Notebook(Computador):
    def __init__(self,modelo=None,cor=None,tempoDeBateria=None):
        super().__init__(modelo,cor)
        self.__tempoDeBateria = tempoDeBateria

    
    def getInformacoes(self):
        super().getInformacoes()
        print (f'Tempo de Bateria: {self.__tempoDeBateria}')

    def cadastrar(self,modelo,cor,tempoDeBateria):
        super().cadastrar()
        self.modelo = modelo
        self.cor = cor
        self.__tempoDeBateria = tempoDeBateria