from Computador import Computador

class Desktop(Computador):
    def __init__(self,modelo=None,cor=None,potenciaDaFonte=None): 
        super().__init__(modelo,cor)
        self._potenciaDaFonte = potenciaDaFonte


    def getInformacoes(self):
        super().getInformacoes()
        print(f'Potencia da Fonte: {self._potenciaDaFonte}')

    def cadastrar(self,modelo,cor,potenciaDaFonte):
        super().cadastrar()
        self.modelo = modelo
        self.cor = cor
        self._potenciaDaFonte = potenciaDaFonte

