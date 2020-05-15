"""
Listas  (list)

Listas em python funcionam como vetores, matrizes ( vetores ) em outras linguages, com a diferença
de serem DINAMICOS e tambem de podermos colocar QUALQUER tipo de dados

Linguagens C/Java : Arrays
   Possuem tamanho fixo de apenas 1 tipo de dados.
   Se criado como inteiro com tamanho de 5, nunca sera alterado.

Linguagem Python
- Dinamico: Não possui tamanho fixo: Ou Seja, podemos criar a lista e simplesmente ir adicionando elementos
 até ocupar toda memoria do computador.
- Qualquer tipo de dado: Não possuem tiop de dado fixo; ou Seja, podemos colocar qualquer tipo de dados;

As listas em python são representadas por colchetes : []

** EXEMPLOS

# Podemos facilmente checar se determinado valor esta contido na lista
num = 7
if num in lista4:
    print(f'encontrei o numero {num}')
else:
    print(f'não encontrei o numero {num}')

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)


#podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))

#adicionar elementos em listas

Para adicionar elementos/valores em listas, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
lista1.append(1, 2, 4) # Isso é errado

#print(lista1)
lista1.append(100)
#print(lista1)

lista1.append([7, 5, 2])
print(lista1)

if [7, 5, 2] in lista1:
    print('encontrei a lista')
else:
    print('não encontrei a lista')

lista1.extend([233, 454, 333]) # Adiciona multiplos elementos a lista
print(lista1)
lista1.extend('Marcos')
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice

lista1.insert(2, 'Novo Valor')
print(lista1)
lista1.insert(0, 0)
print(lista1)

#podemos facilmente juntar duas listas

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

# Podemos facilmente reverter uma lista utilizando o reverse
lista1.reverse()
print(lista1)

# Com slices, o resultado é igual ao metodo reverse()
print(lista1[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Para saber o tamanho de uma lista. Qtde de elementos
print(len(lista1))
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# POP() retorna o ultimo elemento removido
aa = lista5.pop()
print(aa)
print(lista5)

# podemos remover um elemento pelo indice
lista5.pop(4)
print(lista5)

# podemos remover todos os elementos, limpar a lista.
print(lista5)
lista5.clear()
print(lista5)

# podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 4
print(nova)

# Podemos facilmente converter uma string para uma lista

# exemplo 1
curso = 'Programacao em Python: Essencial'
print(curso)

# Por padrão, o split separa os elementos da lista pelo espaço entre elas
curso = curso.split()
print(curso)

# Exemplo2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# convertendo uma lista em string
lista6 = ['Programação','em','Python:','Essencial']
print(lista6)

# Abaixo estamos falando, pega a lista6, coloca o espaço em cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso1 = 'Programação$em$Python:$Essencial'
curso = curso1.split('$')
print(curso)

nome = 'marcos luiz de jesus'
nome = '*'.join(nome)
print(nome)

# podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando dados
lista6 = [1, 2.3, True, 'Marcos', 'd', [1, 2, 4], 545454545454]
print(lista6)


# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 = Utilizando while

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto=input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)
# fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# fazer acesso aos elementos de forma inversa
print(cores[-2]) #azul

for cor in cores:
    print(cor + ' imprimindo a cor com For')

indice = 0
while indice < len(cores):
    print(cores[indice] + ' imprimindo as cor com While ')
    indice = indice + 1

cores = ['verde', 'amarelo', 'azul', 'branco']
# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)


# listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(43)
print(lista)

# Outros métodos não tão importantes mais também uteis

# Encontrar o indice de um elemento na lista

# em qual indice esta o valor 6?
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(6))

# em qual indice esta o valor 9?
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(9))

# OBS: Caso o elemento nao exista na lista, será apresentado erro
#numeros = [5, 6, 7, 8, 9, 10]
#print(numeros.index(19))

# caso haja elemento duplicado, sera retornado o indice do primeiro elemento encontrado
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
# buscando a partir do indice 1
print(numeros.index(5, 1))
print(numeros.index(5, 2))
print(numeros.index(5, 3))
print(numeros.index(5, 4))
# OBS: Caso o elemento nao exista na lista, será apresentado erro

# Podemos fazer busca dentro de um range, inicio/fim
# Buscar o indice o valor 8 entre o valor 3 e 6
print(numeros.index(8, 3, 6))

#Revisao do slicing

#lista[inicio:fim:passo]
#range(inicio:fim:passo)

#trabalhando com slice de lista com o parametro 'inicio'
lista = [1, 2, 3, 4]
print(lista[:]) # pegando todos os elementos
print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restantes
print(lista[::-1]) # invertendo a leitura de uma lista

#trabalhando com slice de lista com o parametro 'fim'
print(lista[:2]) #comeca em 0, pega ate o indice 2 - 1
print(lista[:4]) #comeca em 0, pega ate o indice 4 - 1
print(lista[1:3]) # comeca em 1, pega ate o indice 3 - 1

#trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2]) # começa em 1, vai até o final de 2 em 2

print(lista[::2]) # começa em 0, vai até o final de 2 em 2

# Invertendo valores em uma lista

nome = ['Marcos', 'Luiz', 'Jesus']
nome[0], nome[1], nome[2] = nome[2], nome[1], nome[0]
print(nome)

nome.reverse()
print(nome)
# Transformar lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(type(tupla))
print(tupla)
# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) #soma
print(max(lista)) #maior valor
print(min(lista)) #menor valor
print(len(lista)) #tamanho da lista

# Desempacotamento de listas


lista = [1, 2, 3, 4]
num1, num2, num3, num4 = lista

print(num1)
print(num2)
print(num3)
print(num4)


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# forma 1
# Ao utilizar o lista.copy(), copiamos os dados da lista para nova lista, mas elas ficaram totalmente
# independentes, ou seja, modificando uma lista, nao afeta a outra. Isso em Python
# é chamado de Deep Copy (copia profunda)

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)
print(lista)
print(nova)

# Forma 2 Shallow copy
# Veja, que utilizamos a copia via atribuição e copiamos o dados da lista para a nova lista, mas apos
# realizar modificação em uma das lista, essa modificação se refletiu em ambas as listas. Isto em Python
# é chamado de Shallow Copy
lista = [5, 6, 7]
print(lista)

nova = lista
nova.append(4)

print(lista)
print(nova)
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 22, 27]

lista2 = ['M', 'a', 'r', 'c', 'o', 's', '', 'l', 'u', 'i', 'z']

lista3 = []

lista4 = list(range(11))

lista5 = list('Marcos Luiz de Jesus')





