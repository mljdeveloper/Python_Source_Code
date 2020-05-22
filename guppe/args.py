"""
Entendendo o *args

- o *args é um parametro, como outro qualquer. Isso siginifca que você poderá
chamar de qualquer coisa, desde que ele comece com asteriscos

*xis
Mas por convenção, utilizamos o *args para defini-lo
Mas o que é o *args?
O parametro utiilizado em uma função, coloca os valore extras informados como
entrada em um tupla. Entao desde ja lembre-se que tuplas são imutaveis

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(1, 2, 3))

# print(soma_todos_numeros(2, 4) # TypeError

# Entendendo o *args

#def soma_todos_numeros(*args):
#    total = 0
#    for numero in args:
#        total = total + numero
#    return total

# OU

def soma_todos_numeros(*args):
    return sum(args)  # Valores dentro de uma TUPLA

print(soma_todos_numeros())
print(soma_todos_numeros(2))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(3, 4, 5))
print(soma_todos_numeros(3, 4, 5, 6.7))


# Outro exemplo de utilização de args


def verifica_info(*args):
    if 'Marcos' in args and 'Luiz' in args:
        return 'Bem vindo Marcos Luiz'
    return 'Eu nao sei que você é...'


print(verifica_info())
print(verifica_info(1, True, 'Marcos', 'Luiz'))
print(verifica_info(1, 'Luiz', 'Andre', 10))


"""


def soma_todos(*args):
    return sum(args)


print(soma_todos())
print(soma_todos(10))
print(soma_todos(10,20))

numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos(*numeros))  # Desempacotador, passar * para tratar a lista em questao
# O Asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados, Desta forma, ele saberá
# que precisará antes desempacoter estes dados

