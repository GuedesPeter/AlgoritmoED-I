# # Fracamente privado (_)
# - Fortemente tipado (__)

class Pessoa:
    def __init__(self,codigo,nome,endereco,telefone):
        self.__codigo = codigo
        self.nome =nome
        self._endereco = endereco
        self.__telefone = telefone

    def get_Fone(self):
         print(self.__telefone)

    def imprime_nome(self):
        print(f'Nome: {self.nome}')

    def imprime_telefone(self):
        self.get_Fone()