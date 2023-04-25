from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self,marca,qtdRodas,modelo,velocidade,numMarchas,bagageiro=False):
        super().__init__(self,marca,qtdRodas,modelo,velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f'N° Marchas: {self.numMarchas}')
        print(f'Bagageiro: {self.bagageiro}')