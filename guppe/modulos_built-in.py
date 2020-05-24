"""
Modulos Builtin ( Modulos integrados, que ja vem instalados no Python)
https://docs.python.org/3/py-modindex.html
Python | Modulos Builtin

# Utilizando alias (apelidos) para modulos e funcoes
import random as rdm

print(rdm.random())

# Utilizando alias (apelidos) para modulos e funcoes
from random import randint as rdi

print(rdi(5, 89))

# podemos importar todas as funções de um módulo utilizando o *
from random import *

print(random())

# Importando todo o modulo

import random
print(random.random())
"""

from random import (
   random as rdm,
   randint as rdi,
   shuffle as sff,
   choice as cho
)

print(rdi(4, 6))
print(rdm())
numeros = ['10', '2', '3', '4', '5']
sff(numeros)
print(numeros)

print(cho('Marcos Luiz'))

from math import pi
print(pi)