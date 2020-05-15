"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia à teoria
de conjuntos da Matematica


- Aqui no Python, os conjuntos são chamados de Sets
Dito isto, da mesma forma que na matematica:

- Sets(conjuntos) não possuem valores duplicados;
- Sets(conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Python com chaves {}

Diferença entre Conjunto (set) e Mapas (Dicionarios) em Python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto

# Forma1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo sera
# ignorado e não gerar error e não fara parte do conjunto

# Forma 2 = mais comum

s = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

# Importante lembrar que, alem de não termos valores duplicados, não temos ordem
# lista

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [9, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (9, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# dicionario Não aceitam valores chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([9, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjunto Não aceitam valores duplicados, então temos 8 elementos
conjunto = {9, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s= {1, 'b', True, 34.22, 55}
print(s)
print(type(s))

for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu
# e os visitantes, informam manualmente as cidades de onde vieram.

# Nós adicionamos cada cidade em uma lista python, ja que em uma lista podemos
# adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuida', 'São Paulo', 'Cuiba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas. temos?
# O que vc faria? faria um loop  na lista?

print(len(set(cidades))) # set elimina duplicidade

"""

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
print(s)
print(type(s))

print(dir(set))


