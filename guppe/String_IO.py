"""
StringIO
ATENÇÂO: Para ler ou escrever dados de um arquivo do sistema operacional o software
precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para Escrever no arquivo

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal'
# Podemos criar um arquivo em memoria ja com uma string inserida ou mesmo vazio
# para inserirmos texto depois

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write(' Outro Texto')
arquivo.seek(0)
print(arquivo.read())