"""
Listas aninhadas ( Nested Listas )

- Algumas linguagens de programaçõ possuem uma estrutura de dados chamadas de arrays:
- Unidimensional (arrays/vetores);
- Multidimensional (Matrizes)

Em Python não existe arrays, mas sim LISTAS

numeros = [1, 2, 3, 4, 5]

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3 x 3
print(listas)

print(type(listas))

print(listas[0][1]) # 0 = Linha, 1 = Coluna resultado é 2 conforme exemplo

print(listas[2][1])
"""

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3 x 3


# Iterando com Loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

# Lista Comprehesion
# Para cada lista em listas
# Para cada valor em lista
# imprima valor
[[print(valor) for valor in lista] for lista in listas]

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)


# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
