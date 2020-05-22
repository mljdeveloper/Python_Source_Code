"""
- Funcoes com parametros padrão ( default parameteres )

- Funcoes onde a passagem de parametro seja opcional

# Exemplo de função onde a passagem de parametro é opcional

print('Marcos Luiz')
print((3*3) * 'Marcos ')

def quadrado(numero): # Parametro Obrigatorio
    return numero * 2

print(quadrado(10))

def exponencial(numero, potencia=2): # 2 é o valor padrão para potencia, caso usuario nao informe
    return numero ** potencia


print(exponencial(5,6))

print(exponencial(3))  # por padrão eleva ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuario

# OBS: Em funções python, os parametros com valores default ( padrão ) DEVEM
sempre estar ao final da declaração

def soma (num1=0, num2=2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # TypeError caso o valor do num2 não for padrão
print(soma())  # TypeError caso nenhun dos parametros tiverem valor padrão


def mostra_informacao(nome='Marcos', instrutor=False):
    if nome == 'Marcos' and instrutor:
        return 'Bem vindo instrutor Marcos!'
    elif nome == 'Marcos':
        return 'Eu pensei que você fosse o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Joao', True))
print(mostra_informacao('Marcos'))
print(mostra_informacao('Marcos', False))

# Outros Exemplos


def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(3, 2, subtracao))


instrutor = 'Geeek'

def diz_oi():
    intrustor = 'Python'
    return f'Oi {intrustor}'

print(diz_oi())

#OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global,
#a local tera preferencia


def diz_io(prof):
    prof = 'Geek'
    return f'ola {prof}'

print(diz_oi())

# ATENCAO com variaveis globais ( se puder evitar, evite)
total = 0

def incrementa():
    total = total + 1 # esse erro ocorre porque a total local nao foi inicializada localmente
    return total

total = 0

def incrementa():
    global total # avisando que queremos atualizar a variavel global, que esta declarada acima
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())


"""


# podemos ter funcoes que são declaradas dentro de funcoes
# e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador

    return dentro()


print(fora())
print(fora())
print(fora())



