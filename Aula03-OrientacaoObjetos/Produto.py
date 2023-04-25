class Produto:
    def __init__(self,nome,preco,categoria):
        self.id = None
        self.nome = nome
        self.preco = float(preco)
        self.categoria = categoria



    def imprimirProduto(self):
        print("Nome: ", self.nome)
        print("Preço: R$", self.preco)
        print("Categoria: ", self.categoria.nome)

 