"""
Debuggando com PDB
PDB = Python Debuger

# Debugando no pycharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))



# Exemplo com o PDB - Pyhton Debugger Exemplo 1
# Precisamos importar a biblioteca PDB e então utilizar a função set_trace()
# Comando basicos do PDB
# L (listar onde estamos no codigo)
# n (proximo linha)
# p ( imprimi variavel)
# c (continua a execucao - finaliza o debug

import pdb

nome = 'marcos'
sobrenome = 'luiz'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com o PDB - Pyhton Debugger Exemplo 2
# Precisamos importar a biblioteca PDB e então utilizar a função set_trace()
# Comando basicos do PDB
# L (listar onde estamos no codigo)
# n (proximo linha)
# p ( imprimi variavel)
# c (continua a execucao - finaliza o debug



nome = 'marcos'
sobrenome = 'luiz'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""


# Exemplo com o PDB - Pyhton Debugger Exemplo 3
# Precisamos importar a biblioteca PDB e então utilizar a função set_trace()
# Comando basicos do PDB
# L (listar onde estamos no codigo)
# n (proximo linha)
# p ( imprimi variavel)
# c (continua a execucao - finaliza o debug

# A partir do python 3.7, não é mais necesario importar a biblioteca
#pdb, pois o comando debug foi incorporado como funcao built-in (integrada)
#chamada breakpoint


nome = 'marcos'
sobrenome = 'luiz'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)