"""
Leitura de Arquivo

Para ler o conteudo de um arquivo em Python, utilizamos a funcao integrada open()
que literamente siginifica 'abrir'.

Open() -> Na forma mais simples de utilização nós passamos apenas um parametro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalharemos.

https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundErro
"""

arquivo = ''
try:
   arquivo = open('c:\Brady/Acessos.txt')
except FileNotFoundError as err:
    print(f'Ocorreu um erro: {err}')
except UnicodeDecodeError as erra:
    print(f'Ocorreu um erro: {erra}')

# mode r -> Modo de Leitura. r -> read() - Ler

#print(arquivo)

ret = arquivo.read()
print(type(ret))
print(ret)


#print(type(arquivo))

# Para ler o conteudo de um arquivo, apos a sua abertura, devemos utilizar a função read()
# OBS. O Python, utiliza um recurso para trabalhar com arquivos chamado cursor.
# Esse cursor funciona como o cursor quando estamos escrevendo
#print(arquivo.read())
