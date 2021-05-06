from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo = 0.00, limite = 1000.00, cartaocredito = False, cartaodebito = True):
        self.__saldo = saldo
        self.__limite = limite
        self.__cartaocredito = cartaocredito
        self.__cartaodebito = cartaodebito

    def cadastrar(self):
        return print(f'Conta Corrente cadastrada com sucesso')
    
    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            return print(f'Deposito feito, saldo atual: {self.__saldo}')
        else:
            return print(f'Numero inválido')