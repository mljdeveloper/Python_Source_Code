"""
 Funcoes de maior grandeza -Higher Order Functions - HOF
 O que isso significa?

 - Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
 que retornam funcoes como resultrado ou mesmo que podemos passar funcoes como
 argumentos para outras funcoes, e ate mesmo criar variaveis do tipo de funcoes
 nos nossos programas.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen

# Exemplo - Definindo as funcoes

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funcoes
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas

# Em Python podemos tambem ter funcoes dentro de funcoes, que são conhecidas por Nested
# Functions ou tambem Inner Functions ( Funcoes Internas )

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Rodrigo'))

print(cumprimento('Renato'))

print(cumprimento('Rafael'))

# Retornando funcoes de outras funcoes

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkk', 'yayayayayaya', 'lollololol'))
    return rir


# testando
rindo = faz_me_rir()

print(rindo())


# Inner Functions ( Funções Internas / Nested Functions) Podem acessar o escopo
# de funcoes mais externas


from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahah', 'lololololol', 'kkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())

"""

