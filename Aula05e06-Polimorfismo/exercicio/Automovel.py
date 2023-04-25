from Veiculo import Veiculo

class Automovel(Veiculo): 
    def __init__(self,marca,qtdRodas,modelo,velocidade,potMotor):
        super().__init__(self,marca,qtdRodas,modelo,velocidade)
        self.potMotor = potMotor

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f'Potencia do Motor: {self.potMotor}')