
from Aluno import Aluno

class AlunoEnsinoMedio( Aluno):
    def __init__(self, codigo, nome, matricula,ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print("--------------------------Aluno Ensino Médio------------------------------")
        print('Codigo:',self.codigo)
        print('Nome:',self.nome)
        print('Matricula:',self.matricula)
        print('Ano:',self.ano)
        print('----------------------------------------------------------------')