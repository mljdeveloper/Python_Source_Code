"""
Módulo Collections: Ordered Dict

# Em um dicionario, a ordem de inserção dos elementos não é garantida

dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dic1)

for chave, valor in dic1.items():
    print(f'chave={chave}: valor={valor}')

OrderedDict -> é um dicionario, que garante a ordem de inserção dos elementos

dic1 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(dic1)

for chave, valor in dic1.items():
    print(f'chave={chave}: valor={valor}')

# Em um dicionario, a ordem de inserção dos elementos não é garantida

from _collections import OrderedDict



# Entendendo a diference entre Dic e OrdereDict

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}
print(dic1 == dic2) # True


odic1 = OrderedDict({'a': 1, 'b': 2})
odic2 = OrderedDict({'b': 2, 'a': 1})
print(odic1 == odic2) # False
"""
