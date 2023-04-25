#from Pessoa import Pessoa
from Cidade import Cidade
from Fisica import Fisica 
from Juridica import Juridica



c1 = Cidade("POA")
c2 = Cidade("Cidreira")

pf1 = Fisica('João','3322-5500',c1,"000.111.222-33")

pj1 = Juridica('Mercado do Zé',"9988775501",c2,"00.111.222/0001-88")

pf2 = Fisica('Maria','22334455',c2,"000.222.111-77")

#pj1.imprimir()
pj1.addFuncionario(pf1)
pj1.addFuncionario(pf2)
pj1.imprimirFuncionarios()




