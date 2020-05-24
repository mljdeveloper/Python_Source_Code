"""
Try Except Else Finally

Dica de quando e onde tratar o código:
Toda entrada do usuario deve ser tratada!
OBS: A função do usuário é destruir seu sistema

# Else => É executado somente se não ocorrer o erro.
num = 0
try:
    num = int(input('Informe um numero:'))
except ValueError as err:
    print(f'Valor Incorreto')
else:
    print(f'Você digitou {num}')


# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o numero {num}')
finally:
    print('Depois do bloco try/except')

# OBS: o bloco finally é SEMPRE executado. Independente se houve excecão ou não

# o finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais completo CORRETO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'valor incorreto'
    except ZeroDivisionError:
        return 'Numero não pode ser dividido por zero'

num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')
print(dividir(num1, num2))

# Exemplo mais completo GENERICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')
print(dividir(num1, num2))


"""

# Exemplo mais completo SEMI-GENERICO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'
        
num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')
print(dividir(num1, num2))
