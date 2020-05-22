"""
Map

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
    ''' Calcula a area de circulo com raio 'r' '''
    return math.pi * (r ** 2)

print(area(1))

raios = [2, 5, 7.1, 0.3, 10, 44]

#forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)


# Forma 2 - Map

# Map é um função que recebe dois parametros: O primeiro a função, o segudo um iteravel
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))


# Forma 3 - Map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

print(list(map(lambda x: math.pi * (x ** 2), raios)))

#Apos  utilizar a funcao map(), depois da primeira utilizacao do resultado, ele zera.
# Para fixar - Map
# Temos dados iteraveis

# dados: a1, a2, .... an
# temos a função
# Funcao: f(x)

#Utilizamos a funcao map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplicar a funcao

# O map object: f(1), f(a2), f(...), f(n)

"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26),
           ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5 * dado[1] + 32))

print(list(map(c_para_f, cidades)))



