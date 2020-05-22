"""
Utilizando lambdas

Conhecidas por expressão lambdas, ou simplesmente lambdas, são funcoes sem nome,
ou seja, funcoes anonimas.

# Funco am python


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressao Lambda

lambda x: 3 * x + 1

# E como utilizar a expressao lambda?

calc = lambda x: 3 * x + 1
print(calc(20))

# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('marcos', 'luiz'))

# Em funcoes Python podemos ter nenhuma ou varias entradas. Em Lambas tambem


amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.05

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())

print(uma(3))

print(duas(3, 4))

print(tres(3, 4, 6))

autores = ['Issac Asimov','Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert',
           'Orson Scott Card', 'Douglas Adams', 'H . G Wells', 'Leigh Brackett']

#print original
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

#print ordenado por sobrenome
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[0])

#print ordenado por nome
print(autores)


# Função Quadratica

#f(x) = a * x ** 2 + b * x + c

# definindo a funcao

def geradora_funcao_quadratica(a, b, c):
    '''
    Retorna a funcaof(x) = a * x ** 2 + b * x + c
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))
# os 3 primeiros sao argumentos da funcao (3, 0, 1)
# o ultimo parametro e o argumento da lambda (2)

"""