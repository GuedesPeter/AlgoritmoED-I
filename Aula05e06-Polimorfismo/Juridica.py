from Pessoa import Pessoa
#from Fisica import Fisica
#from Cidade import Cidade 


class Juridica(Pessoa):
    def __init__(self,nome,fone,cidade,cnpj = None):
        super().__init__(nome,fone,cidade)
        self.cnpj = cnpj
        self.funcionarios = []
    
    def addFuncionario(self,pFisica):
        self.funcionarios.append(pFisica)

    #POLIMORFISMO --------------------------------------------------------------------
    def imprimir(self):
        super().imprimir() #POLIMORFISMO -----------------------------------
        print(f'CNPJ: {self.cnpj}')
        print(" ----------------------------- Funcionários -----------------------------------")
        if len(self.funcionarios) == 0:
            print('Não possui funcionários')
        else:
            for pFisica in self.funcionarios:
                print(f'Nome Func.: {pFisica.nome}')
                print(f'Fone: {pFisica.fone}')
                print(f'Cidade: {pFisica.cidade.nome}')
                print('----------------------------------------------------------------')
                
    def __str__(self):
        return f'Empresa: {self.nome} - Fone: {self.fone} - CNPJ: {self.cnpj}'

