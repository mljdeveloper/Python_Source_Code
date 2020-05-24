"""
Levantando os proprios erros com raise

raise -> Lança exceções

Obs. o raise não é uma função. é uma palavra reservada assim como def.

para simplicar, pense no raise como sendo util para que possamos criar nossas proprias
excecoes e mensagens

A forma geral de utilização é:

raise TipoDoErro('mensagem de erro')

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'o texto {texto} sera impresso na cor {cor}')


colore('Marcos', 3)

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f' A cor precisa ser uma entre {cores}')
    print(f'o texto {texto} sera impresso na cor {cor}')


colore('Marcos', 'vermelho')

OBS: o raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""

# exemplo real

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f' A cor precisa ser uma entre {cores}')
    print(f'o texto {texto} sera impresso na cor {cor}')


colore('Marcos', 'vermelho')
