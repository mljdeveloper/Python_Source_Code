"""
Loop for

Loop -> Estrutura de Repeticao
For -> uma dessas estruturas

Python

For item in interavel:
    //execucao
"""
nome = 'Marcos Luiz de Jesus'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

#Exemplo 1 iterando sobre uma string
#for letra in nome:
#    print(letra)

#Exemplo 2 iterando sobre uma lista
##    print(numero)

#Exemplo 3 iterando sobre um range
# nao ler o ultimo numero. ultimo valor nao incluso.
#for numero in numeros:
 #   print(numero)

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(str(valor[0]) + '-' + str(valor[1]))

qtde = int(input("Qtas vezes rodar o loop"))
soma = 0

for n in range(1, qtde+1):
    num = int(input(f'Imprimindo: {n}/{qtde} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Vai corinthians'
for letra in nome:
    print(letra, end='')

emoji = 'U0001F60D'
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

