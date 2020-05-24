"""
Funcoes com Parametro ( de entrada )

- Funcoes que recebem dados para serem processados dentro da mesma;
- Tipo de Funcoes:::
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Funçoes sem Entrada
def quadrado_de_7():
    return 7 * 7


def quadrado(numero):  # funcao recebe parametro
    return numero ** 2
    #  return numero * numero


print(quadrado_de_7())
print(quadrado(5))
print(quadrado(8))
print(quadrado(3))


def cantar_parabens(nome):
    print('Parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida!')
    print(f'Viva o/a {nome}')


cantar_parabens('Ana')

# Funcoes podem ter n parametros de entrada, Ou seja, podemos receber como entrada
# em uma função quantos parametros forem necessários. Eles são separados por vírgula


def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

def outra(num1, num2, msg):
    return (num1 + num2) * msg

print(soma(2, 5))
print(multiplica(4, 5))
print(outra(1, 2, 'Marcos '))


# Nomeado parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Marcos', 'Luiz'))

# A diferença entre parâmetro e Argumentos
# Parametros são variaveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função


# Argumentos nomeados ( Keyword arguments )

# Caso utilizemos nomes do parametros nos argumentos para informa-los,
#podemos utilizar qualquer ordem

print(nome_completo(nome='Marcos', sobrenome='Luiz'))
print(nome_completo(sobrenome='Luiz', nome='Marcos'))

# Erro comum na utilização de return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(lista)
