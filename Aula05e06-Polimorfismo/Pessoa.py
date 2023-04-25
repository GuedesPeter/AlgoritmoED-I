#----------------- HERANÇA -----------------------
from Cidade import Cidade

class Pessoa: #CLIENTE
    def __init__(self,nome,fone,cidade):
        self.id = None
        self.nome = nome
        self.fone = fone
        self.cidade = cidade
        
    def imprimir(self):
        #print(f'ID: {self.id}')
        print(f'Nome: {self.nome}') 
        print(f'Fone: {self.fone}') 
        print(f'Cidade: {self.cidade.nome}') 

    def __str__(self):
        return f'Nome: {self.nome} - Fone: {self.fone}'