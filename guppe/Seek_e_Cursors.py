"""
Seek e Cursor
Seek() - A função seek() é para movimentar o cursor pelo arquivo. Ele recebe um
# parametro que indice onde queremos colocar o cursor.


# seek(). A funcao seek() é utilizada para a movimentacao
arquivo = open('texto.txt')
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())

for i in range(0, 10):
    print(arquivo.read())
    arquivo.seek(0)

# readline() - Funcao que ler o arquivo linha a linha

print(arquivo.readline())

linhas = arquivo.readlines()

print(len(linhas))

OBS: Quando abrimos um arquivo com a funcao open() é criada uma conexao entre o arquivo
no disco do computador e o nosos programa. Essa conexao é chamada de streaming.
Ao finalizar os trabalhos com o arquivo devemos fechar a conexão. Para isso
utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo:
2 - Trabalhar o arquivo:
3 - Fechar o arquivo
"""
# 1) Abrir o arquivo
arquivo = open('texto.txt')

# 2) Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed)
# Verifica se o arquivo esta aberto ou fechado)

# 3) Fechar o arquivo
arquivo.closed

#Se tentarmos manipular o arquivo apos o seu fechamento. teremos um valuerror

