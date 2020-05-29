"""
Entendendo Iterators e Iterables

Iterator ->
 - Um objeto que pode ter iterado
 - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() é chamada

Iterable ->
 - Um objeto que irá retornar um iterator quando a função iter() for chamada
"""

nome = 'Marcos'  # É um iterable masi nao é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable masi nao é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for letra in nome:
    print(f'{letra}', end='')

