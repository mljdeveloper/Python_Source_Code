"""
JSON e Pickle

JSON ->  JavaScript Objet Notation


ret = json.dumps(['produto', {'PlayStatoin': ('2TB', 'Novo', '220v', 2340)}])
print(type(ret))
print(ret)

import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)
ret = json.dumps(felix.__dict__)

print(ret)

Integrando o JSON com o Pickle

pip install jsonpickle

# Escrevendo o arquivo json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)



"""
# Lendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

