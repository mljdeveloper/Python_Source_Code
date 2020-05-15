"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python são representados por chaves {}

# Interar sobre dicionarios
# imprimi as chaves
for chave in receita:
    print(chave)

# imprimi os valores

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(chave + ' ' + str(receita[chave]))

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de Dicionario

for chave, valor in receita.items():
print(f'chave={chave} e valor={valor}')
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Soma*, valor Maximo*, valor minimo*, tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


"""

