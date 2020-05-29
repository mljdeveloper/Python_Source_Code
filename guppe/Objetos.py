"""
POO - Objetos
Objetos são instancias da classe. Ou seja, apos o mapeamento do objeto do mundo real para
sua representação computacional. devemos poder criar quantos objetos foram necessarios.
Podemos pensar nos objetos/instancias de uma classe como variaveis do tipo definido na classe.

#Instancias / Objeto
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar()

print(f' A lampada esta ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrete(5000, 20000)

user1 = Usuario('Marcos', 'Jesus', 'marcosjesus@gmail.com', '123456')


"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def __init__(self):
        pass

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O Cliente {self.__nome} diz Oi! ')



class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O Cliente é {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def __init__(self):
        pass


lamp = Lampada()

cli1 = Cliente('Marcos Luiz', '132.028.023.22')

cc1 = ContaCorrente(10000, 30000, cli1)

cc1.mostra_cliente()

cc1._ContaCorrente__cliente.diz()