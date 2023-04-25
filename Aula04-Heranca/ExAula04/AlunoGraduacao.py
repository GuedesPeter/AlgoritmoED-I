from Aluno import Aluno

class AlunoGraduacao(Aluno): 
    def __init__(self,codigo,nome,matricula,semestre):
        super().__init__(codigo,nome,matricula)
        self.semestre = semestre
    

    def imprimir(self):
        print("--------------------------Aluno Graduação------------------------------")
        print('Codigo:',self.codigo)
        print('Nome:',self.nome)
        print('Matricula:',self.matricula)
        print('Ano:',self.semestre)
        print('----------------------------------------------------------------')