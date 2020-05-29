"""
Escrevendo em arquivos CSV

writer -> Criar Objeto CSV
writerow -> Escrever uma linha

from csv import writer

bArqExiste = True
arquivo = ''
try:
    arquivo = open('filmes.csv')
    arquivo.close()
except FileNotFoundError as err:
    bArqExiste = False

with open('filmes.csv', 'a') as arquivo:
    escritor_csv = writer(arquivo)

    filme = None
    if not bArqExiste:
        escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Genero: ')
            duracao = input('Informe a Duração (minutos)')
            escritor_csv.writerow([filme, genero, duracao])

"""

# DictWriter
# OBS: As chaves do dicionario devem ser as mesmas utilizadas como cabecalho

from csv import DictWriter

bArqExiste = True
arquivo = ''
try:
    arquivo = open('filmes.csv')
    arquivo.close()
except FileNotFoundError as err:
    bArqExiste = False


with open('filmes.csv', 'a') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    if not bArqExiste:
        escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Genero: ')
            duracao = input('Informe a Duração (minutos)')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duração": duracao})
