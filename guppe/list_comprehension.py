"""
Utilizando list comprehension nós podemos gerar novas listas com dados
processados a partir de outro iteravel

Sintaxe
[dado for dado in interavel]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)




Para entender melhor o que esta acontecendo deemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

"""


# List Comprehension versus loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])



amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.capitalize() for amigo in amigos])
