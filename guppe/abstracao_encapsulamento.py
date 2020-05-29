"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso codigo dentro de um grupo logico e
hierarquico utilizando classes

           classe
|----------------------------|
|      atributos e metodos   |
|----------------------------|

# Relembrando atributos/metodos privados em Python
Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um metodo privado
chamado __falar()

Esses elementos privados so devem/deveriam ser acessados
dentro da classe. Mas Python nao bloqueia este acesso
fora da classe. com Python acontece um fenomeno chamado
Name Manglng, que faz uma alteracao na forma de se
acessar os elementos privados, conforme:
_Classe__elemento

Exemplo:
instancia._Pessoa_nome
instancia.Pessoa_falar()


Abstracao, em POO é o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e metodos privados de usuario

conta1 = Conta('Marcos', 150, 1000)

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)

print(conta1.__dict__)
conta1.depositar(150)
print(conta1.__dict__)
conta1.sacar(200)
print(conta1.__dict__)
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo}  do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 Remover o valor da conta de origem
        self.__saldo -= valor
        # 2 Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

conta1 = Conta('Marcos', 200, 1500)
conta1.extrato()
conta2 = Conta('Eliane', 400, 2500)
conta2.extrato()

conta1.transferir(25, conta2)
conta1.extrato()
conta2.extrato()