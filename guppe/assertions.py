"""
 Assertions

 # ALERTA: Cuidado ao utilizar 'assert'

 Se um programa Python for executado com o parametro -O, nenhum assertion
 será validado, ou Seja, todas as suas validações ja eram.
"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os numeros precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 1)


def comer_fast_food(comida):
    assert  comida in [
        'pizza',
        'sorvete',
        'doces',
        'batta frita',
        'cachorro quente'
       ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

