"""
Tipo FloatingPointError

Tipo real, decimal

OBS: os separadores de casas decimais na programção python é o ponto e não a
virgula
"""


valor = 1, 44
print(valor)
print(type(valor))

valor = 1.44
print(valor)
print(type(valor))

# é possivel fazer dupla atribuicao
valor1, valor2 = 1, 33
print(valor1)
print(valor2)


# podemos converter um float para um int
# Ao converter valores de float par inteiros, nós perdemos precisão
res = int(valor)
print(res)
print(type(res))

# podemos trabalhar com numeros complexos
variavel = 5j
print(variavel)
print(type(variavel))

nome = "Angelina Jolie"
print(nome)
print(nome[0:4])