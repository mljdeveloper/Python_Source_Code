"""
**Kwargs

Poderiamos chamar este parametro de **xis mas por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores
extras em uma tupla, o **Kwargs exige que utilizamoes parametros nomeados, e transforma
esses parametros extrar em um dicionario

# def cores_favoritas(**kwargs):
#    print(kwargs)

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor.upper()}')


cores_favoritas(marcos="preto", julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parametros *args e **kargs não são obrigatorios


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'Marcos' in kwargs and kwargs['Marcos'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Marcos'
    elif 'Marcos' in kwargs:
        return f"{kwargs['Marcos']} marcos"
    return "Não tenho certeza quem você é"


print(cumprimento_especial())
print(cumprimento_especial(Marcos='Python'))
print(cumprimento_especial(Marcos='oi'))
print(cumprimento_especial(Marcos='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM)
- Parametros obrigatorios
- *args
- Parametros Default ( não obrigatorios )
- ** Kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(45, 'Marcos')
minha_funcao(45, 'Marcos', 4, 5, 3, solteiro=True)
minha_funcao(45, 'Marcos', eu='nao', você='vai')

# Entenda porque é importante manter a ordem dos parametros na declaração
# a = 1
# b = 2
# args = 3,
# instrutor = 'Marcos''
# kwargs = {'sobrenome': 'Luiz', 'cargo': 'Programador'}

# Funcao com a ordem correta de parametros
def mostra_info_CERTA(a, b, *args, instrutor='Marcos', **kwargs):
    return [a, b, args, instrutor, kwargs]

# Funcao com a ordem INCORRETA de parametros
def mostra_info_ERRADA(a, b, instrutor='Marcos', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info_CERTA(1, 2, 3, sobrenome='Luiz', cargo='Programador'))

print(mostra_info_ERRADA(1, 2, 3, sobrenome='Luiz', cargo='Programador'))

# Desempacotamento com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Marcos', 'sobrenome': 'Luiz'}

print(mostra_nomes(**nomes))

"""

def soma_tudo(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3, }

soma_tudo(*lista)  # * desempacota lista
soma_tudo(*tupla)   # * desempacota tupla
soma_tudo(*conjunto)  # * desempacota conjunto

dic = dict(a=1, b=2, c=3)
soma_tudo(**dic)  # ** desempacota dicionario

# OBS! Os nomes da have em um dicionario devem ser o mesmo dos parametros da funcao



