"""
Modulo random e o que são módulos?
- Em Python, módulos nada mais são do que outros arquivos Python

Módulo random possuem varias funcoes para geração de numeros pseudo-aleatorio
# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado)

import random

random () Gerar um numero real pseudo-aleatorio entre 0 e 1

# Ao realizar o import de todo o módulo, todas as funões, atributos, classes e propriedades
# que estiverem dentro do módulo, ficaram disponiveis (ficaram em mémoria)
# Caso voce saiba quais funções você precisa utilizar deste módulo
# então esta nao seria a forma ideal de utilizaçao. Nós veremos uma forma melhor.

print(random.random())

# Forma 2 - Importando uma função especifica do modulo (Forma recomendada)

from random import random

# No import aima, estamos falando: Do módul randrom, importe a função random

for n in range(0, 10):
    print(random())

# uniform() -> Gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

#for i in range(10):
#    print(uniform(3, 10))


from random import randint

for i in range(6):
    print(randint(1, 60), end=', ')

# Choice() -> Mostra um valor aleatorio entre um iteravel

from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

#pedra   perde do papel   e ganha da tesoura
#papel   perde da tesoura e ganha da pedra
#tesoura perde da pedra   e ganha do papel

def disputa(valor1, valor2):
    if valor1 == 'pedra':
        if valor1 == 'pedra' and valor2 == 'papel':
            return 'papel'
        elif valor1 == 'pedra' and valor2 == 'tesoura':
            return 'pedra'
    elif valor1 == 'papel':
        if valor1 == 'papel' and valor2 == 'tesoura':
            return 'tesoura'
        elif valor1 == 'papel' and valor2 == 'pedra':
            return 'papel'
    elif valor1 == 'tesoura':
        if valor1 == 'tesoura' and valor2 == 'pedra':
            return 'pedra'
        elif valor1 == 'tesoura' and valor2 == 'papel':
            return 'tesoura'

computador = choice(jogadas)
humano = 'tesoura'
print(f'Computador jogou: {computador}')
print(f'Humano jogou: {humano}')
resultado = disputa(computador, humano)
if resultado == computador:
    print(f'O Computador ganho com {resultado}')
elif resultado == humano:
    print(f'O Humano ganhou com {resultado}')
else:
    print('Ninguem ganhou!!')
"""

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)
shuffle(cartas)
print(cartas.pop())







