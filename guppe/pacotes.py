"""
Pacotes
Modulos - É apenas um arquivo Python que pode ter diversas funcoes para utilizarmos

Pacote - E um diretorio contendo uma coleção de modulos

OBS: Nas versoes 2.x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versoes do Python 3.x, não é mais obrigatoria a utilização deste arquivo,
mas normalmente ainda é utilizado para manter a compatibilidade

"""

from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(2, 4))

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())