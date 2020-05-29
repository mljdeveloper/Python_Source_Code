"""
Escrevendo em arquivos
Ao abrir um arquivo para leitura, não podemos realizar a escrita nele.
o Contrario é verdadeiro.
Abrir o arquivo no modo de escrita ( w )

Ao abrir um arquivo para escrita, o arquivo é criado para o sistema operacional.

Para escrevermos dados em um arquivo, apos abrir o arquivo, utilizamos a funcao write()
Esta funcao recebe uma string como parametro, caso contrario teremos TypeError

abrindo um arquivo para escrita com o modo 'w', se o arquivo nao existir sera criado,
caso ele exista, o anterior sera apagado e um novo sera criado. Desta forma, todo
o conteudo no arquivo anterior é perdido.

# Exemplo de abrir arquivo para escrever nele ( write )
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos que o marcos ta criando. \n')
    arquivo.write('Podemos colocar quantas linhas quisermos. \n')
    arquivo.write('Esta é a ultima linha.')

with open('marcos.txt', 'w') as arquivo:
    arquivo.write('Marcos ' * 1000)

"""


with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
