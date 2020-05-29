"""
 Metodos de data e hora

# com now() podemos especificar um timezone( Fuso Horario )
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana. weekday()
# Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira
0 Segunda
1 Terça
2 Quarta
3 Quinta
4 Sexta
5 Sabado
6 Domingo

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

import datetime

data = datetime.datetime.today()

nascimento = input('Qual sua data de nascimento ? (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))

semana = ['Segunda-feira', 'Terça-feira', 'Quarta-Feira', 'Quinta-Feira',
          'Sexta-feira', 'Sabado', 'Domingo']

print(f'Voce nasceu em um(a) {semana[nascimento.weekday()]}')
# Formatando data e hora com strftime() (string format time)
import datetime

hoje = datetime.datetime.today()
print(hoje)

hoje_formatadoBR = hoje.strftime('%d/%m/%Y')

print(hoje_formatadoBR)

def formata_data(data):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return f'{data.day} de {meses[data.month - 1]} de {data.year}'


from textblob import TextBlob

def format_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = input('Qual dia da Consulta ? (dd/mm/yyyy): ')

hoje = hoje.split('/')

hoje = datetime.datetime(year=int(hoje[2]), month=int(hoje[1]), day=int(hoje[0]))

print(hoje)
print(format_data(hoje))

# Somente a hora

almoco = datetime.time(12, 30, 0)
print(almoco)

import timeit

#Marcando tempo de execução do nosso codigo ccom timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(teste(5))

print(timeit.timeit(functools.partial(teste, 2), number=10000))

"""


