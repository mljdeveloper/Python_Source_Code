"""
POO - Heranca Multipla

Heranca Multipla nada mais é do que a possibilidade de uma classe herdar de multiplas
classes fazendo com que a classe filha herde todos os atributos e metodos de todas as
classes herdadas.

OBS: A heranca multipla pode ser feita de duas maneiras:
  - Por Multiderivação Direta;
  - Por Multiderivação Indireta;
# Exemplo 1 = multiderivacao direta

class Base1:
    pass

class Base2:
    pass

class MultiDerivada(Base1, Base2):
    pass

# Exemplo 2 - multiderivacao indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da Terra!'


class Pinguim(Aquatico, Terrestre): # vai executar o metodo da classe que esta
    #escrito primeiro, caso aqui, Aquatico

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Method Resolution Order - MRO


# Objeto é instancia de..

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instancia de Object? {isinstance(tux, object)}')

