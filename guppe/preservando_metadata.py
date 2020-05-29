"""
Preservando metadatas com wraps

Metadatas -> sao dados intrísecos em arquivos
wraps -> São funcoes que envolvem elementos com diversas finalidades
# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        '''Eu sou uma funcao (logar) dentro da outra'''
        print(f'Voce esta chamando  {funcao.__name__}')
        print(f'aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    '''Soma dois numeros.'''
    return a + b

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)
"""
# Resolucao do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao) # Preservou o metada da funcao soma, chamada abaixo
    def logar(*args, **kwargs):
        """Eu sou uma funcao (logar) dentro da outra"""
        print(f'Voce esta chamando  {funcao.__name__}')
        print(f'aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros."""
    return a + b

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)