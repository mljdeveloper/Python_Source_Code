"""
Funcoes com retorno
numeros = [1, 2, 3]
print(f'Eu sou a lista original {numeros}')
ret = numeros.pop()
print(f'retorno de pop() {ret}')

novonumero = []
novonumero.insert(0, 'ok')
novonumero.append(ret)
print(novonumero)

print(f'Alguem roubou um elemento da minha lista {numeros}')
print(f'Eu sou a nota lista {novonumero}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é none

def quadrado_de_7():
    print(7 * 7) # isso não é retorno de função


def diz_oi():
    return 'Oi,'


# Exemplo de retorno de função

def quadrado_de_7():
    return 7 * 7  # isso não é retorno de função

print(f'Retorno da funcao quadrado_de_7 {quadrado_de_7()}')

print(f' {diz_oi()} Marcos!')


OBS: Funções em python, retorna valor com a palavra reservada return


OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função
def diz_oi():
    return 'oi'
    print('acho que ninguem me viu!!!')


print(diz_oi())

2 - POdemos ter, em um função, diferentes returns;

def nova_funcaio():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcaio())

3 - Podemos, em uma função, retornar qualquer tipo de dados, até mesmo multiplos valores
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um numero pseudo- randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim
# codificação desnecessária


def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
"""



