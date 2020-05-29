"""
teste de memoria com generatos
# Sequencia de Fibonacci

1, 2, 3, 4, 5, 8, 13, 21, 34

# Função usando listas
teste na maquina do curso 449MB
def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums

for n in fib_lista(10):
    print(n)

# teste na maquina do curso 3MB
def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1

for n in fib_gen(10000):
    print(n)
"""
