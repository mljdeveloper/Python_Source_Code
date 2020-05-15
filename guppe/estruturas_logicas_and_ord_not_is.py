"""
Estruturas logicas
and (e) or (ou) not (nao) is (é)
Operadores unarios - not
Operacoes binarios - and, or, is

Para o 'and' ambos os valores precisam ser True
Para o 'or' um dos valores precisam ser True
Para o 'not' o valor do boolean é invertido
Para o 'is' um valor é comparado com um segundo valor.
"""
ativo = True
logado = True

if ativo and logado:
    print('(AND) Bem-vindo usuário!')
else:
    print('(AND) Você precisa ativar sua conta, por favor check seu email')

if ativo or logado:
    print('(OR) Bem-vindo usuário!')
else:
    print('(OR) Você precisa ativar sua conta, por favor check seu email')

if not ativo:
    print('(NOT) Você precisa ativar sua conta, por favor check seu email')
else:
    print('(NOT) Bem-vindo usuário!')


if ativo is False:
    print('(IS) Voce precisa ativar sua conta')
else:
    print('(IS) Bem-vindo usuário!')
# Ativo é falso?
print(ativo is False)
