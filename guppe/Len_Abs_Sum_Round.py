"""
 Len() - Retorna o tamanho (ou seja, o numero de itens) de um iteravel
 Abs() - Retorna o valor absoluto de um numero inteiro ou real. De forma basica, seriao seu valor real sem o sinal
 Sum() - Recebe como parametro um iteravel, podendo receber um valor inicial e retorna a soma total dos elementos incluindo o valor inicial
 Round() - Retorna um numero arredondado para n digito de precisão apos a casa decimal
 se a precisão não for informada, retorna o inteiro mais proximo da entrada

# Len()
print(len('Marcos Luiz de Jesus'))

print(len([1, 2, 3, 4, 5, 6]))

print(len((1, 2, 3, 4, 5, 6)))
print(len({1, 2, 3, 4, 5, 6}))

# Por debaixo dos panos, quando utilizamos a funcao len() o Python faz o seguinte:

# Dunder len
print('Marcos Luiz de Jesus'.__len__())

print(abs(-5))
print(abs(5))

# Sum()
# Obs: o Valor inicial default=0
print(sum([1, 2, 3, 4, 5], 5))

print(sum([1, 2, 3, 4, 5]))

print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3}.values()))

# Round
print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.21221212, 2))
print(round(1.2199999, 2))
"""



