from Automovel import Automovel 

class Carro(Automovel):
    def __init__(self,marca,qtdRodas,modelo,velocidade,potMotor,qtdPortas):
        super().__init__(self,marca,qtdRodas,modelo,velocidade,potMotor)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f'Qtde. Portas: {self.qtdPortas}')
