"""
POO = Heranca ( Inheritance )

A ideia de heranca é de reaproveitar codigo, tambem de extender nossas classes.

OBS: Com heranca, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e metodos da classe herdada

Cliente
   - nome;
   - sobrenome;
   - cpf;
   - renda;

Funcionario
   - nome;
   - sobrenome;
   - cpf;
   - matricula;

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e
 metodos da classe

OBS: Quando uma classe herda de outra classe, a classe é conhecida por
    (Pessoa)
   - Super Classe
   - Classe Mae
   - Classe Pai
   - Classe Base

OBS: Quando uma classe herda de outra classe, ela é chamada:
   [Cliente, Funcionario]
   - Sub Classe;
   - Classe Filha;
   - Classe Especifica


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    '''Funcionario herda de Pessoa'''

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cli1 = Cliente('Marcos', 'Jesus', '132.026.011-11', 50000)

fun1 = Funcionario('Eliane', 'Jesus', '333.444.011-11', 12345)

print(cli1.nome_completo())

print(fun1.nome_completo())

print(cli1.__dict__)
print(fun1.__dict__)

# SobreEscrita de Metodos (Overriding)

SobreEscrita de metodo, ocorre quando reescrevemos um metodo presente na super
classe em classes filhas

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionario {self.__matricula} Nome: {self._Pessoa__nome}'


cli1 = Cliente('Marcos', 'Jesus', '132.026.011-11', 50000)
fun1 = Funcionario('Eliane', 'Jesus', '333.444.011-11', 12345)

print(cli1.nome_completo())

print(fun1.nome_completo())