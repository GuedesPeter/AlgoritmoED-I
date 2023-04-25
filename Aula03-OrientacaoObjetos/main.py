
from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido
from Pessoa import Pessoa #CLIENTE
from Cidade import Cidade

cidade1 = Cidade('Porto Alegre')
pessoa1 = Pessoa('Maria','(51) 33224455',cidade1)

cat1 = Categoria('Bebidas')
cat2 = Categoria('Alimentos')

produto1 = Produto('Coca Cola',7.99,cat1)
produto2 = Produto('Fanta',6.95,cat1)
produto3 = Produto('Arroz',3.95,cat2)
 
pedido1 = Pedido('27/03/2023','Rua A,100',pessoa1)
pedido1.addProdutos(produto1)
pedido1.addProdutos(produto2)
pedido1.imprimirPedido()

