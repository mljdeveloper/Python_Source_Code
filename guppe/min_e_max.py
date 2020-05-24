"""
Min e Max

max() -> retorna o maior valor de um iteravel ou o maior de dois ou mais elemento.

# Exemplos

lista = [1, 2, 3, 8, 99, 34, 129]
print(max(lista))

tupla = (1, 2, 3, 8, 99, 34, 129)
print(max(tupla))

conjunto = {1, 2, 3, 8, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 8, 'e': 99, 'f': 34, 'g': 129}
print(max(dicionario.values()))

# Exemplos

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('informe o segunfo valor: '))

print(max(val1, val2))

# Exemplos

print(max('a', 'b', 'c', 'd', 'e'))

print(max(3.145, 5.789))

min() -> retorna o menor valor em um iteravel ou o menor valor de dois ou mais elementos

# Exemplos

lista = [1, 2, 3, 8, 99, 34, 129]
print(min(lista))

tupla = (1, 2, 3, 8, 99, 34, 129)
print(min(tupla))

conjunto = {1, 2, 3, 8, 99, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 8, 'e': 99, 'f': 34, 'g': 129}
print(min(dicionario.values()))

# Exemplos

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('informe o segunfo valor: '))

print(min(val1, val2))
"""


nomes = ['arya', 'samson', 'dora', 'tim', 'ollivander']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))


musicas = [
    {'titulo': "ThunderStruck", 'tocou': 3},
    {'titulo': "Dead Skin Mask", 'tocou': 2},
    {'titulo': "Back in Black", 'tocou': 4},
    {'titulo': "Too old to rock in roll, too young to die", 'tocou': 23},
    {'titulo': "Fuscao Preto", 'tocou': 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])


print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])