"""
Sistema de arquivos - Navegacao

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do modo os

os -> Operating System - Sistema Operacional
# getcwd() -> pega o current work diretory - diretorio corrente
# retorna o caminho absoluto
print(os.getcwd())

# Para mudar o diretorio, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())


os.chdir('..')
print(os.getcwd())


os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('c:\\brady'))

print(os.path.isabs('c:\\brady'))

#OBS para usuarios Windows
# Se você é usuario utilizando um computador com windows
# tera que ter cuidado ao verificar diretorios.

import sys
# Podemos checar se um diretorio é absoluto ou relativo

# Podemos identificar o sistema operacional com o módulo os

print(os.name) # posix(Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional

print(sys.platform)

print(os.getcwd())
newdir = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(newdir)
print(os.getcwd())

# Veja que o os.path.join(), recebe dois parametros, sendo o primeiro diretorio atual
# e o segundo diretorio, que sera juntado ao atual.

# Podemos listar os arquivos e diretorios com o listdir()

print(os.listdir('c:\\Brady'))

"""

# fazer import

import os

# Podemos listar os arquivos e diretorios com o detalhes com scandir()
scanner = os.scandir('c:\\brady')
lst = list(scanner)
#print(lst)
#print(dir(lst[0]))

print(lst[0].inode())
print(lst[0].is_dir()) # é um diretorio?
print(lst[0].is_file()) # é um arquivo?
print(lst[0].is_symlink()) # é um link simbolico?
print(lst[0].name) # nome do arquivo
print(lst[0].path) # Caminho ate o arquivo
print(lst[0].stat()) # Estatisticas

#OBS: quando utilizamos a funcao scandir() nós precisamos fecha-la, assim
#quando abrirmos um arquivo

scanner.close()
