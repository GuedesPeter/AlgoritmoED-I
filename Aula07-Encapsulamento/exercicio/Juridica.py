from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self,codigo,nome,endereco,telefone,cnpf,inscEstadual,qtdFuncionarios): 
        super().__init__(codigo,nome,endereco,telefone)
        self.__cnpf = cnpf
        self.__inscEstadual = inscEstadual
        self.qtdFuncionarios = qtdFuncionarios
        

   