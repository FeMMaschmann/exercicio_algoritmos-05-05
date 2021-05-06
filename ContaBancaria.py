from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):
    @property
    def saldo(self):
        pass
    
    @property
    def limite(self):
        pass

    @saldo.setter
    @limite.setter

    @abstractmethod
    def cadastrar(self):       
        pass

    @abstractmethod
    def depositar(self, modelo, cor, preco):
        pass