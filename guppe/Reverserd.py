"""
 Reversed

 OBS: Não confunda com a funcao reverse() que estudamos na listas
 A função reverse só funciona nas listas.
 Já a função reversed() funciona com qualquer iteravel
 Sua função é inverter o iteravel
"""
# Lista
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(list(res))

# Tupla
res = reversed(lista)
print(tuple(res))

# Conjunto (Set) Em conjunto nao definimos a ordem dos elementos
res = reversed(lista)
print(set(res))
print(res)
print(type(res))

# Pode iterar sobre o reversed
for letra in reversed('Marcos Luiz de Jesus'):
    print(letra, end='')
print('\n')
print(''.join(list(reversed('Marcos Luiz de Jesus'))))

#Utilizando o slice de strings

print('marcos Luiz de jesus'[::-1])

for n in reversed(range(0, 10)):
    print(n, end='')
print('\n')
for n in range(9, -1, -1):
    print(n, end='')