"""
Decorators com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto Decorator Pattern


def gritar(funcao):
    def aumentar(*args):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola eu sou o {nome}'

@gritar
def ordernar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor. '

print(saudacao('Marcos'))

print(ordernar('Picanha', 'Batata Frita'))

# Refatorando com a Decorator Pattern
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola, seu sou o/a {nome}'

@gritar
def ordernar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor. '


print(saudacao('Marcos'))

print(ordernar('Picanha', 'Batata Frita'))

@gritar
def lol():
    return 'lol'

print(lol())

#OBS Vale lembrar que podemos utilizar parametros nomeados

print(ordernar(acompanhamento='Batata Frita', principal='Arroz'))

"""

# Decorator com argumentos

def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verificar_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

print(comida_favorita('pizza','Arroz'))
