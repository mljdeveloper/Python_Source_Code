"""
Módulo Collections - Named Tuple
#Recap Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e
tambem parametros

from collections import namedtuple

# Precisamos definir o nome e parametros
# Forma1

cachorro = namedtuple('cachorro', 'idade raca nome')
print(cachorro)

#Forma2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

#Forma3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)

# Acessando os dados
# Forma1
print(ray[0])
print(ray[1])
print(ray[2])


# Forma2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('chow-chow'))
print(ray.count('chow-chow'))
"""

