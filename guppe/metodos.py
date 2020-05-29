"""
POO - Metodos

 - Metodos (funcoes) -> Representa os comportamentos do objeto. Ou seja, as ações
 que este objeto pode realizar no seu sistema.

 Em Python, dividimos os metodos, em 2 grupos, Metodos de Instancia e Metodos de Classe

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado
de dunder (DOuble Underline)

OBS: Os metodos/funcoes dunder em Python são chamados de metodos magicos

us1 = Usuario('Marcos', 'Jesus', 'meuemail@uol.com', '123')
print(us1.nome_completo())
us1.correr(100)

p1 = Produto('arroz', 'comida', 6000)
print(p1.desconto(5))


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuario criado com sucesso')

senha = input('Informe a senha para acesso: ')
if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')


# Metodos de classe em Python são conhecidos como Metodos Estaticos em outras linguagens


# Metodos de Classe

us1 = Usuario('Marcos', 'Jesus', 'meuemail@uol.com', '123')
us1 = Usuario('Marcos', 'Jesus', 'meuemail@uol.com', '123')
Usuario.conta_usuarios() # Forma correta - Deve ser usar a classe direto e nao a instancia

#us1.conta_usuarios() # Forma Incorreta


us1 = Usuario('Marcos', 'Jesus', 'marcosluizdejesus@uol.com', '123')

#print(us1._Usuario__gera_usuario()) # Forma Incorreta. Não USAR

"""


# Metodos de Instancia

# o metodo dunder __init__ é um metodo especial, chamado de construtor e
# sua função é construir o objeto a ser criado
# Metodos são escritos em letras minusculas. Se o nome for composto os nomes serão
# separados por underline

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retornar o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod   # Metodo de Classe
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuario(s) no sistema')

    @staticmethod
    def definicao():  # Nao tem acesso a classe e nem acesso a instancia
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def correr(self, metros): # Metode de Instancia
        print(f'{self.__nome} Estou correndo {metros} metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):                 # metodo inicia com (__) = metodo privado
        return self.__email.split('@')[0]


# Metodo Estatico

print(Usuario.contador)
print(Usuario.definicao())
us1 = Usuario('Marcos', 'Jesus', 'marcosluizdejesus@uol.com', '123')
print(us1.contador)
print(us1.definicao())
