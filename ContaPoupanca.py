from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo = 0.00, limite = 1000.00, juros = 0.01):
        self.__saldo = saldo
        self.__limite = limite
        self.__juros = juros

    def cadastrar(self):
        return print(f'Conta Poupança cadastrada com sucesso')
    
    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            return print(f'Deposito feito, saldo atual: {self.__saldo}')
        else:
            return print(f'Numero inválido')