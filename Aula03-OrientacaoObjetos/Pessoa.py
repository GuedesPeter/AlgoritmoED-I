'''Integrando as classe - Pessoa recebe a classe Cidade'''

class Pessoa: #CLIENTE
    def __init__(self,nome,fone,cidade):
        self.id = None
        self.nome = nome
        self.fone = fone
        self.cidade = cidade
        
    def imprimir(self):
        print(f'Nome: {self.nome} - Fone: {self.fone} - Cidade: {self.cidade.nome}')
 