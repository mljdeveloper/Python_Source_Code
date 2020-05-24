"""
Modulos Customizados

Como modulos Python nada mais são do que arquivos Python, então TODOS os arquivos
que criamos neste curso são módulos python prontos para serem utilizados

from funcos_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""

import funcos_com_parametros as fcp
from Map import cidades, c_para_f

print(fcp.lista)
print(fcp.soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(list(map(c_para_f, cidades)))

