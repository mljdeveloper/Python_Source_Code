"""
 Zip() -> Cria um iteravel ( Zip Object ) que agrega elemento de cada um dos
 iteraveis passados como entrada em pares

 lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip))

print(list(zip1))
zip1 = zip(lista1, lista2)
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]

# O Zip utiliza como parametro o menor tamanho em iteravel. Isso significa que se
# estiver trabalhando com tamanhos diferentes, ira parar quando os elementos do
# menor iteravel acabar
zip2 = zip(lista1, lista2, lista3)
print(list(zip2))


# Podemos utilizar diferentes iteraveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map()
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))