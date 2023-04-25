

class Veiculo:
    def __init__(self,marca,qtdRodas,modelo):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self,valorAtual):
        self.velocidade += valorAtual
        print(f'Velocidade Atual: {self.velocidade}Km/h')

    def frear(self,valorAtual):
        if self.velocidade - valorAtual < 0:
            self.velocidade = 0
        else:
            self.velocidade -= valorAtual
        print(f'Velocidade Atual: {self.velocidade}Km/h')

    def imprimirInformacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Qtde.Rodas: {self.qtdRodas}')
        print(f'Modelo: {self.modelo}')
        print(f'Velocidade: {self.velocidade}Km/h')
