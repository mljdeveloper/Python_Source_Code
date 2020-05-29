"""
POO - Propriedades - Properties


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


ct1 = Conta('Marcos', 200, 300)
ct2 = Conta('Eliane', 400, 500)

print(ct1.extrato())
print(ct2.extrato())

soma = ct1.get_saldo() + ct2.get_saldo()
print(soma)

print(ct1.__dict__)
ct1.set_limite(99999)
print(ct1.__dict__)

"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite



ct1 = Conta('Marcos', 200, 300)
ct2 = Conta('Eliane', 400, 500)

print(ct1.extrato())
print(ct2.extrato())

soma = ct1.saldo + ct2.saldo
print(soma)

print(ct1.__dict__)
ct1.limite = 443322
print(ct1.__dict__)

print(ct1.valor_total)
print(ct2.valor_total)