"""
Sistema de arquivos - Manipulação

# Descobrindo se um arquivo ou diretorio existe
# Path Absolute
print(os.path.exists('c:\\brady\\acessos.txt')) # para saber se existe o arquivo acessos.txt

# Path Relative
print(os.path.exists('geek')) #para saber se existe o diretorio
print(os.path.exists('geek\\university')) #para saber se existe o diretorio

# Descobrindo se um arquivo ou diretorio existe
print(os.path.exists('c:\\brady\\acessos.txt')) # para saber se existe o arquivo acessos.txt

# Criando Arquivos
# Forma 1
open('arquivo_teste.txt', 'w').close()

# Forma 2
open('arquivo_teste2.txt', 'a').close()

# Forma 3
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass  # Não faz nada!!!

"""
import os
# Criando arquivos das formas corretas


os.mknod('c:\\Brady\\Arquivo_novo.txt')
