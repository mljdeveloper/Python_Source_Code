"""
Tuplas ( Tuple )

Tuplas são bastantes parecidas com listas.
Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por parenteses ();

2 - As tuplas são imutaveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla

print(type(()))

#CUIDADO 1: As tuplas são representadas por parenteses(), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))
print(tupla1)

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#CUIDADO 2: Tupla com 1 elemento, não é uma tupla
tupla3 = (4) # Isso não é uma Tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma Tupla
print(tupla4)
print(type(tupla4))

# CONCLUSÂO, Podemos concluir que tuplas são definidas pela vírgula
# e não pelo uso do parenteses


tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Marcos', 'Luiz', 'Jesus')
nome, nomemeio, ultimonome = tupla

print(nome + ' ' + nomemeio + ' ' + ultimonome)
print(ultimonome + ' ' + nomemeio + ' ' + nome)


# Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas
#serem imutaveis

# Soma*, Valor Maximo*, Valor Minimo* e Tamanho
 # * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla)) #Soma
print(max(tupla)) #Valor Maximo
print(min(tupla)) #Valor Minimo
print(len(tupla)) #Tamanho da Tupla

#Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

# verificando se determinado elemento esta contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla.count('a'))
print(tupla.count('c'))

nome = tuple('marcos luiz de jesus')
print(nome)
print(nome.count('s'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em umaa
#seleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto'
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')

for mes in meses:
    print(mes)

print(len(meses))

# o acesso a elementos de uma tupla tambem é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificando em qual indice um elemento esta na tupla

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto'
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses.index('Outubro'))
print(meses.index('Outubro', 1)) # buscar outubro na tupla, a partir do indice 1

# OBS: Caso o elemento não exista, será gerado ValueError;

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto'
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')
# Slicing
# tupla[inicio:fim:passo]
print(meses[5:9])

# Por que utilizar tuplas?

# - Tuplas são mais rapidas do que listas.
# - Tuplas deixam seu código mais seguro*.
# * Isso porque trabalhar com elementos imutaveis, traz segurança para o codigo


# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(outra)

"""











