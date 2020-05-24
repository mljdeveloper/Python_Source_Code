"""
Reduce

OBS: A partir do Python3+ a funcao reduce(), não é mais uma funcao integrada
(built-in). Agora temos que importar e utilizar esta função a partir do módulo
functools

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela.
Em todo caso, 99% das vezes um loop for é mais legivel.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:
dados = [01, 02, 03, .. an]

E voce tem uma função que recebe dois parametros:

def funcao (x, y)
    return x * y

Assim como maps() e filter(), a função reduce(), recebe dois parametros, a funcao e o iteravel

reduce(funcao, dados)

A funcao reduce(), a funnciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # aplica a funcao nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res = f(res1, a3) # aplica a funcao passando o resultado do passo1 mais
    o terceiro elemento e guarda o res

Ou seja, em cada passo ele aplica a funcao passando como primeiro argumento o resultado
da aplicação anterior. no Final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a funcao reduce(), como:
funcao(funcao(funcao(01, 02), 03), 04),,,,), 0n)

"""
# como funciona na pratica?

# vamo utilizar a funcao reduce(), para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parametros


multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)
