"""
Sorted

Obs: Apesar do nome, não confunda com a função sort() da função list()

Podemos utilizar o sorted com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar elementos.

lista = [4, 7, 3, 8, 1, 6, 2, 5, 9]

lista2 = sorted(lista)  # Ordena em ordem crescente

print(tuple(lista)) # converte para tupla
print(set(lista)) # converte para set

print(lista2)

print(sorted(lista, reverse=True))  # Ordena em ordem decrescente

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adodo pizza"]},
    {"username": "carla", "tweets": ["Eu adoro gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
# ordenado pelo username, order alfabetica do Z ao A
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# ordenado pelo username, order alfabetica do A ao Z
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# ordenado pelo tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


musicas = [
    {'titulo': "ThunderStruck", 'tocou': 3},
    {'titulo': "Dead Skin Mask", 'tocou': 2},
    {'titulo': "Back in Black", 'tocou': 4},
    {'titulo': "Too old to rock in roll, too young to die", 'tocou': 23},
    {'titulo': "Fuscao Preto", 'tocou': 32},
]
 # Ordena de menos tocada para a mais tocada
print(sorted(musicas, key=lambda  musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda  musica: musica['tocou'], reverse=True))

"""

