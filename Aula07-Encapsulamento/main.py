from Conta import Conta

c1 = Conta()
#print(c1.getSaldo()) 

#c1.setSaldo(20)
#print('Novo Saldo: ',c1.getSaldo())

print("Saldo: ",c1.saldo)
c1.saldo = 30
print('Novo Saldo: ',c1.saldo)

c1.depositar(100)
print('Deposito Realizado: ',c1.saldo)
c1.sacar(200)
print('Saldo após o Saque: ',c1.saldo)