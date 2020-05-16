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

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
print(s)
print(type(s))

print(dir(set))

# Remover elementos em um conjunto
#Forma 1
s.remove(3) #Não é indice! Informamos o valor a ser removido
OBS: Caso o valor não exista, sera gerado um KeyError
OBS2: Caso seja excluido, nenhum valor é retornado
print(s)

# Forma 2
s.discard(2) # Caso o valor não exista, não sera gerado Erro.
print(s)

#Copiando um conjunto para outro..

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# forma 2 - Shallow Copy

novo = s
novo.add(4)
print(novo)
print(s)

# Podemos limpar todos os itens do conjunto
s.clear()
print(s)

# Veja que alguns alunos estudam Python tambem estudam Java

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union
unicos1 = estudante_python.union(estudante_java)
print(unicos1)

# Forma 2 - Utilizando o caracter pipe |
unicos2 = estudante_python | estudante_java
print(unicos2)


# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - utilizando intersection

ambos1 = estudante_python.intersection(estudante_java)
print(ambos1)
# Forma 2 - Utilizando o &
ambos2 = estudante_java & estudante_python
print(ambos2)


s = {1, 2, 3}

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudante_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudante_java = {'Fernando', 'Gustavo', 'Patricia','Julia', 'Ana'}

# Gerar um conjunto de estudantes de um curso que não estão no outro.

so_python = estudante_python.difference(estudante_java)
print(so_python)

so_java = estudante_java.difference(estudante_python)
print(so_java)


# Soma*, valor maximo*, valor minimo*, tamanho
# * Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""



