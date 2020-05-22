"""
List Comprehesion

Nos podemos adicionar estruturas condicionais logicas
as nossas list comprehesion

"""

print(10/2)
print(10 % 2)

# Exemplos
# 1
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar
# Qualquer numero par modulo de 2 é 0 e 0 em Python é false. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer numero impar modulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# comece a ler o comando a partir do final, ou seja, a partir do for
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)






