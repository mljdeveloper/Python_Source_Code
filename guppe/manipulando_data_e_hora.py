"""
Manipulando Data e Hora

Python tem um modulo built-in ( integrado ) para se trabalhar com data e hora
chamado datetime

print(dir(datetime))

datamin = datetime.MINYEAR
datamax = datetime.MAXYEAR

print(datamin)
print(datamax)

# retorna data e hora corrente
# 2020-05-28 18:44:39.236758               BR 28/05/2020
print(datetime.datetime.now())
#datetime.datetime(year, month, day, hour, minute, second, microsecond)
# datetime.datetime(2020, 5, 28, 18, 46, 22, 688855)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 20:00:00

inicio = inicio.replace(hour=20, minute=55, second=0, microsecond=0)

print(inicio)

Recebendo dados do usuario e convertendo para data


evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
print(type(nascimento))


"""

import datetime

evento = datetime.datetime.now()

# acessa individual dos elemtnos da data e hora
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

