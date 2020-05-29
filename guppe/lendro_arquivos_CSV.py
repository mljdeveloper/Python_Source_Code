"""
Lendro Arquivos CSV
CSV = Comma Separeted Values = Valores Separados por Virgula


# Possivel de se trabalhar, mas não é o ideal ( muito trabalho )

with open('original.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui 2 formas diferente para ler dados em arquivos CSV:
 - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas

 from csv import reader

with open('original.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o Cabeçalho
    # cada linha é uma lista
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')


 - DictReader -> Peremite que iteremos sobre as lonhas do arquivo CSV como OrderedDicts;
 # DictReader
from csv import DictReader

with open('original.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    # cada linha é um OrderedDict
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")



"""


# DictReader com Outro separador
from csv import DictReader

with open('original.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # <- Mudar aqui para ; ou espaço em branco.. etc
    # cada linha é um OrderedDict
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")



