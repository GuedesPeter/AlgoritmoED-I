
from Automovel import Automovel

class Moto(Automovel):
    def __init__(self,marca,qtdRodas,modelo,velocidade,potMotor,partEletrica=True):
        super().__init__(self,marca,qtdRodas,modelo,velocidade,potMotor)
        self.partEletrica = partEletrica

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f'Partida Elétrica: {self.partEletrica}')