"""
Any e All

All() Retorna True se todos os elementos do iteravel são verdadeiros
ou ainda se o iteravel esta vazio.
# Exemplo All

print(all([0,1, 2, 3, 4]))  # False
print(all([1, 2, 3, 4]))  # True
print(all([1, 2, 3, 4]))  # True
print(all([]))  # True

nomes = ['Carlos', 'Camila', 'Carla']
 # verifica se todos os nomes começa com a Letra C
print(all([nome[0] == 'C' for nome in nomes]))


print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


Any() -> Retorna true se qualquer elemento do iteravel for verdadeiro.
Se o iteravel estiver vazio, retorna false

"""
print(any([0, 1, 2, 3, 4]))  # retorna true

print(any([0, False, {}, []]))  # retorna false

nomes = ['Carlos', 'Camila', 'Carla', 'Vanessa']

print(any([nomes[0] == 'C'] for nome in nomes))

print(any([num for num in [4, 2, 10, 6, 6, 8, 9] if num % 2 == 0]))
