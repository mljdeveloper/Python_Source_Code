"""
o bloco with

# 1 abrimos o arquivo
# 2  trablhamos com o arquivo
# 3 fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados apos o bloco with.

"""

#o bloco with - forma Pythônica para manipular arquivos
# com with, o arquivo é fechado automaticamente.

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
