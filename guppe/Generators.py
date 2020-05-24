"""
Generators Expression

Em aulas anteriores nos estuamos:
- List Comprehension;
- Dictionary Comprehension
- Set Comprehension;
Não vimos:
- Tuple comprehension.. porque elas se chama generators

nome = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiano', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes])

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiano', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

#List Cpmre
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

#Qual e a utilidade de getsizeof() => retorna a quantidade de bytes em memoria
#do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string 'Marcos' esta ocupando em memoria.

print(getsizeof('Marcos'))

print(getsizeof('Marcos Luiz de Jesus'))

from sys import getsizeof

# gerando uma lista de numeros com List comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])

# gerando uma lista de numeros com Set comprehension

set_comp = getsizeof({x * 10 for x in range(1000)})

# gerando uma lista de numeros com Dictionary comprehension

dic_comp = getsizeof({x: x * 10 for x in range(1000)})

gen = getsizeof(x * 10 for x in range(1000))
print('Para fazer a mesma tarefa gastamos em memoria:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dic Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Posso iterar no generator expression? SIM!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

"""



