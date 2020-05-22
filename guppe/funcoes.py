"""
Definindo Funcoes

- Funcoes são pequenos trechos de codigo que realizam tarefas especificas:
- Pode ou não receber entradas de dados e retornar uma saida de dados:
- Muito uteis para executar procedimentos similares por repetidas vezeds:

OBS: Se voce escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada

"""

# Exemplo de utilização de funções

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando funcao integrada Bult-in do Python
print(cores)
"""
Em Python, a forma geral de definiar uma função é;

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (snake case)

parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula,
podendo ser opcionais ou não

bloco_da_funcao -> Tambem chamado de corpo da função ou implementação, é onde o processamento
da função acontece.
neste bloco, pode ter ou não retono da função

OBJ: Veja que para definiar um função, utilizamos a palavra reservada 'def'
informando ao Python qu estamos definindo uma função. Tambem abrimos o bloco
de codigo com o ja conhecido dois pontos : que é utilizado em Python para definir
blocos.
"""

# Definindo a primeira função

def diz_oi(nome):
    print(nome)

def cantar_parabens():
    print('Parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida!')


for i in range(1, 10):
    diz_oi('Olá')  # Para chamar uma função, utiliza-se sempre o ()

cantar_parabens()


for i in range(11):
    diz_oi('OKOK')


# Em Python, podemos inclusive criar variaveis do tipo de uma funcao e executar a funcao
#atraves da variavel

canta = cantar_parabens


def ola():
    return 'ola'
