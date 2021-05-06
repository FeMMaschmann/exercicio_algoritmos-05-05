from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

linha = '---------------------------------'
print(linha)

c_corrente = ContaCorrente(300.00, 1500.00, False, True)
c_corrente.cadastrar()
c_corrente.depositar(1000.00)

print(linha)

c_poupanca = ContaPoupanca(600.00, 3000.00, 0.2)
c_poupanca.cadastrar()
c_poupanca.depositar(2400.00)

print(linha)
