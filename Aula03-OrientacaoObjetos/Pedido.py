class Pedido:
    def __init__(self,data,end,cliente):
        self.data = data
        self.end = end
        self.cliente = cliente
        self.produtos = []

 
    def addProdutos(self,produto):
        self.produtos.append(produto)
        total = 0
        for prod in self.produtos:
            total += prod.preco
        return total

    def imprimirPedido(self):
        print("Data: ", self.data)
        print("End: R$", self.end)
        #Recebe da classe Pessoa
        print("Cliente: ", self.cliente.nome)
        print("Cidade: ", self.cliente.cidade.nome)
        print("Produtos: ")
        total = 0
        #verificando a lista
        if len(self.produtos) == 0:
            print("Pedido Vazio")
        else:
            for prod in self.produtos:
                total += prod.preco
                print("----------------------------------------------------------------")
                print("Produto: ", prod.nome)
                print("Preço: ", prod.preco)
                print("Categoria: ", prod.categoria.nome)
            print("----------------------------------------------------------------")
            print(f"Total: R$ {total:.2f}")

    
        
