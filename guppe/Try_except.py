"""
o bloco try/except

Utilizamos o bloco try/except para tratar error que podem ocorrer no nosso codigo.
Previnindo assim que o programa pare de funcionar e o usuario receba
mensagens de erro inesperadas.

A forma geral mais simples é

try
  // execução do problema
except:
  // o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro generico
try:
    marcos()
except:
    print('deu algum problema')

# Tente executar a função geek(), caso vc encontre erro, imprima a mensagem de erro.

# Exemplo 1 - Tratando um erro generico
try:
    len(5)
except:
    print('deu algum problema')

OBS: Tratar erro de forma generica não é a melhor forma de tratamento de erros.
o ideial é SEMPRE tratar de forma especifica

# Exemplo 3  - Tratando um erro especifico

try:
    marcos()
except NameError:
    print('Voce esta utilizando uma funcao inexistente')
except TypeError:
    print('voce nao esta executando uma funcao corretamente')

try:
    len(5)
except NameError as err:
    print(f'A Aplicacao gerou o seguinte erro:  {err}')
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
except:
    print('Deu um erro qualquer')
"""

try:
    marcos()
except NameError as err:
    print(f'A Aplicacao gerou o seguinte erro:  {err}')
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
except:
    print('Deu um erro qualquer')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Marcos'}

print(pega_valor(dic, 'nome'))
