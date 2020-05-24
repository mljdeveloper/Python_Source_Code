"""
 Filter

 filter() - Serve para filtrar dados de um determinada coleção.


valores = 1, 2, 3, 4, 5, 6

media = sum(valores) / len(valores)
print(media)
# Biblioteca para trabalhar com dados estatisticos
import statistics

#dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a funçao mean()

media = statistics.mean(dados)

print(media)

#OBS. Assim como a função map(), a filter recebe 2 parametros, sendo
# uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

#Obs: Assim como na funcao map, apos ser utilizada a funcao filter, o valor é zerado da memoria

print(f'Novamente: {list(res)}')


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)
res = filter(None, paises)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))
"""

# A diferença entre map() e filter()
# map() -> Recebe dois parametros, uma funcao e um iteravel e retorna um objeto
#mapeando a funcao para cada elemento do iteravel

# filter -> Recebe dois parametros, uma função e um iteravel e retorna um objeto
# filtrando apenas os elementos de com a função.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adodo pizza"]},
    {"username": "carla", "tweets": ["Eu adoro gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

# Combinas filter e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome
# tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)