"""
 Modos de abertura de arquivo

 r - > abre para leitura ( read )
 w -> abre para escritra, sobreescreve caso o arquivo ja exista ( write )
 x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo
 exista gera FileExistsError.
 a -> Abre para escrita, adicionando o conteudo ao final do arquivo
 + -> Abre o modo de atualizaçao
 OBS: abrindo no modo 'a', append, se o arquivo nao existir sera criado, caso exista
 ser adicionado ao final. Com o modo 'a' nao controlamos o cursor

try:
    with open('Jesus.txt', 'x') as arquivo:
        arquivo.write('teste de conteudo 2.\n')
except:
    print('Arquivo ja existe')

Exemplo a
with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

"""
# Recupera o arquivo existente
novoarquivo = ''
with open('texto.txt', 'r') as arquivo:
    novo_arquivo = arquivo.read()
print(novo_arquivo)

# adiciona nova linhas e ao final adiciona o conteudo do arquivo existente
with open('texto.txt', 'w') as arq:
    arq.write('Este e o meu novo arquivo que vou gravar na primeira linha6. \n')
    arq.write(novo_arquivo)


