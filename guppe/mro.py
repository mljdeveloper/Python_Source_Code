"""
POO - MRO - Methog Resolution Order

Em Python, a gente pode conferir a ordem de execução dos metodos (MRO) de 3 formas;
  - Via propriedade da classe__mro__
  - Via metodo mro()
  - Via help
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


class Pinguim(Terrestre, Aquatico):  # vai executar o metodo da classe que esta
                                     # escrito primeiro, caso aqui, Aquatico

    def __init__(self, nome):
        super().__init__(nome)



tux = Pinguim('Tux')

print(tux.cumprimentar())  # Method Resolution Order - MRO


# Pinguim(Aquatico, Terrestre)
# Eu sou Tux do mar! # Classe aquatica escrita primeiro


# Pinguim(Terrestre, Aquatico)
# Eu sou Tux da Terra! # Classe Terrestre escrita primeiro
