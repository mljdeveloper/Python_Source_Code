"""
teste de velocidade com Expressões Geradoras

def nums():
    for num in range(1, 10):
        yield num

gen = nums()
print(gen)

print(next(gen))
print(next(gen))

gen2 = (num for num in range(1, 10))

print(gen2)

print(next(gen2))
print(next(gen2))

# Generator Expression
import time
gen_inicio = time.time()
print(sum(num for num in range(10000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(10000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')

"""

