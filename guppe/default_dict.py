"""
Módulo Collections - Default Dict
https://docs.python.org/3/library/collections.html#collections.defaultdict

dic1 = {'curso': 'Programação em Python: Essencial'}
print(dic1)
print(dic1['curso'])
# print(dic1['outro']) # Gera um KeyError quando não existe

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

OBS: Lambda são funções sem nome, que podem ou não receber parametro de entrada e retornar
valores.
"""
# fazendo o import
from collections import defaultdict

dic1 = defaultdict(lambda: 0)

print(dic1)
dic1['curso'] = 'Programação em Python: Essencial'
print(dic1)

print(dic1['outro'])
print(dic1)
print(dic1['outro1'])
print(dic1)




