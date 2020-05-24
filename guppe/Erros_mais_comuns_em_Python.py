"""
 Erros mais comuns programando em Python
 E importante prestar atencao e aprender a ler as saidas de erros geradas pela execução
 do nosso codigo.

 - SyntaxError -> Ocorre quando o Python encontra um erro de syntaxe. Ou seja,
 voce escreveu algo que o Python nao reconhece como parte da linguagem

# Exemplos SyntaxError
A)
def funcao:
    print('Marcos')
B)
None = 1
Def = 1

C) usar return somente dentro da uma funcao
return

# Exemplos NameError
Ocorre quando uma variavel ou função nao foi definida

A)
print(funcaoa)


funcaoa <- funcao nao definida, gera erro

B)
a = 18
if a < 10:
    msg = 'É menor que 10'

print(msg)
para ajustar o problema acima, basta declarar a variavel msg fora do if como msg = ''

# Exemplos TypeError
Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a)
print(len(5))

Ocorreu o erro porque tipo INT não tem a função len()

print('Geek' + [])
#Não é possivel concatenar string com lista

print('Geek' + 4)
Não é possivel concatenar string com inteiro, a nao ser que o int sera convertido str(4)

# Exemplos IndexError
Ocorre quando tentamos acessar um elemento em uma lista o outro tipo de dados indexado
utilizando um indice invalido
a)
lista = ['Marcos']
print(lista[2])

Lista acima não possuem index 2, somente index 1, isso ocorre index erro

lista = ['Marcos']
print(lista[0])

# Exemplos ValueError
Ocorre quando um função/operacao built-in(integrada) recebe um argumento com tipo
correto mas valor inapropriado

print(int('Marcos'))
argumento esperar receber um numero e nao letra dentro da string

# Exemplos KeyError
Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

dic = {}
print(dic['nome'])
nao existe a chave 'nome' para exibir


# Exemplos KeyError

dic = {'nome': 'marcos'}
print(dic['nome'])

# Exemplos attributeError
Ocorre quando uma variavel nao tem um atributo/funcao.

tupla = (11, 2, 31, 4)
print(tupla.sort())
# Na tupla, nao existe a funcao sort, logo, ocorre o erro attributeError

# Exemplos IdentationError
Ocorre quando não respeitamos a identação do python (4 espaços)

def funcao():
print('ok')
#deve ser colocado 4 espaços para eliminar o erro

for i in range(10):
print(i)

"""




