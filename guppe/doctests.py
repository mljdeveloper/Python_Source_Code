"""
DocTests
São testes que colocamos na docstring das funcoes e metodos python
Para rodar doctes segue a sintaxe

python -m doctest -v nome_do_modulo.py

Exemplo
Para testar retirar # e colocar 3 aspas dupla (docstring)
def soma(a, b):
    # soma os numeros a e b
    #>>> soma (1, 2)
    3

    #>>> soma (10, 5)
    15
    #
    return a + b
"""

# Exemplo de TDD

def duplicar(valores):
    """
    duplicar os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


print(duplicar(['a', 'b']))

# Erro inesperado

#quando for string a aspas deve ser simples e não duplas no doctestes
def fala_oi():
    """
    Fala oi
    >>> fala_oi()
    'oi'

    """
    return "oi"

print(fala_oi())


# Um ultimo caso estranho...

def verdade():
    """
    Retorna Verdade
    >>> verdade()
    True
    """
    return True

print(verdade())