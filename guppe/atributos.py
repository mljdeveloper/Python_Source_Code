"""
 POO - Atributos

 Atributos -> Representa as caracteristicas do objeto, Ou seja, pelos atributos
 nos conseguimos represntar computacionamente os estados de um objeto.

 Em Python, dividismos os atributos em 3 grupos:
   - Atributos de instancia;
   - Atributos de classe;
   - Atributos Dinamicos;

 # Atributo de Instancia: São atributos declarados dentro do metodo construtor
 # OBS: Metodo construtor: É um metodo especial utilizado para a construção
 do objeto

Em Python, por convenção, ficou estabelecido que, todo atribudo de uma classe é PUBLICO.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado deve ser tratado como privado, ou sejam
que deve ser acessado/utilizado somente dentro da propria classe onde esta declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido tambem como Name Mangling.

#print(acesso._Acesso__senha) # Temos acesso. mas nao deveriamos fazer este acesso.

# OBS. Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
#nao vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe


pessoa = Usuario('marcos', 'oi@oi.com.br', '123')

print(pessoa.nome)
print(pessoa.email)
print(pessoa.senha)
print(type(pessoa))

acesso = Acesso('Marcos', '123')
print(acesso.email)

acesso.mostra_senha()
acesso.mostra_nome()


# O que significa atributos de instancia?

# Significa, que ao criarmos instancia/objetos de uma classe, todas as instancias
# terão estes atributos

user1 = Acesso('marcos@uol.com', '123456')
user2 = Acesso('eliane@uol.com', '665544')


user1.mostra_nome()
user2.mostra_nome()


p1 = Produto('PlayStation4', 'Video Game', 2000)
p2 = Produto('X Box', 'Video Game', 3400)

print(p1.valor, p1.id)
print(p2.valor, p2.id)

# Obs. Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo
#de classe




"""
# Classes com atributos de Instancia Publico
class Lampada:

    def __init__(self, voltagem, cor):  # <- Metodo Construtor
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

class ContaCorrete:

    def __init__(self, numero, limite, saldo): # <- Metodo Construtor
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo

#class Produto:

#    def __init__(self, nome, descricao, valor): # <- Metodo Construtor
#        self.nome = nome
#        self.descricao = descricao
#        self. valor = valor


class Usuario:

    def __init__(self, nome, email, senha): # <- Metodo Construtor
        self.nome = nome
        self.email = email
        self.senha = senha



# Atributos Publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_nome(self):
        print(self.email)


# Atributo de Classe

#p1 = Produto('PlayStation4', 'Video Game', 2000)
#p1 = Produto('X Box', 'Video Game', 3400)

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe
# ou seja, fora do construtor, Geralmente ja inicializamos um valor, e este valor
#é compartilhado entre todas as instanias da classe, ou seja, ao inves de cada
#instancia de ter seus proprios valores, como e o caso dos atributos, com os atributos
#de classe todas as instancias terao o mesmo valor para este atributo


# Refatorar a class Produto

class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0
    def __init__(self, nome, descricao, valor): # <- Metodo Construtor
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self. valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinamicos
# Um atributo que pode ser criado em tempo de execução
# OBS: O Atributo dinamico, sera exclusivo da instancia que o criou

p1 = Produto('Arroz', 'Comida', 200)
p2 = Produto('Feijoao', 'Comida', 100)
p2.peso = '5kg' # Note que na classe Produto nao existe o atributo peso

print(f'Produto: {p2.nome}, Descricao: {p2.descricao} Valor: {p2.valor}, Peso: {p2.peso}')
#print(f'Produto: {p1.nome}, Descricao: {p1.descricao} Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando Atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)