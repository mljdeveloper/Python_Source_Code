"""
Dicionarios ( Dictionary)

OBS: em algumas lingyagens de programação, os dicionarios Python são
conhecidos por mapas

Dicionarios são coleções do tipo chave/valor.
Listas
[0, 1, 2, 3] chave fica implicita
[1, 2, 3, 4] valoes

Tupla
[0, 1, 2, 3] chave fica implicita
(1, 2, 3, 4)

Dicionarios são representados por chaves {}

print(type({}))

OBS: Sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipo de dados;

# Criação de Dicionario
# Forma1 ( Mais Comum )
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma2 ( Menos Comum )
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos
print(paises['br'])
print(paises['py'])
# OBS: caso tentamos acessar uma chave inexisten, ocorre um erro de KeyError

# Forma 2 - Acessando via GET - Recomendada
print(paises.get('br'))
print(paises.get('ru'))
# OBS: Acesando via get um elemento inexiste, nao ocorre erro, mas devolve None

OBS: o tipo None em Python é sempre considerado False

# caso o get nao encontra o objeto com a chave informada sera retornado o valor NONE
# e não sera gerado KeyERROR
pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f' {pais}')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('br', 'Não Encontrado')
print(pais)

# podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive
# lista, tupla, dicionario, como chaves de dicionarios
# tuplas por exemplos são bastantes interessantes de serem utilizadas como chave de dicionarios,
# pois as mesmas são imutaveis
localidades = {
    (35.3141, 39.6172): 'Escritorio em Tokio',
    (40.5554, 23.4343): 'Escritorio em Nova York',
    (59.3346, 19.5454): 'Escritorio em Sao Paulo'
}

print(localidades)
print(type(localidades))

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma mais Comum de adicionar elemento em um dicionario
receita['abr'] = 350
print(receita)

nova_dado = {'mai': 500}
receita.update(nova_dado)
print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario
# é a mesma
# Conclusao 2: Em dicionarios, Não podemos ter chaves repetidas.

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Remover dados de um dicionario

# Forma 1
print(receita)
ret = receita.pop('mar') # forma mais comum de remover um valor do dicionario
print(ret)
print(receita)
# OBS 1: Para remover um elemento do dicionario é obrigatorio passar a chave como parametro,
# caso nao encontre sera gerado um KeyError

# OBS 2: Ao remover um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev'] # Nao retorna um valor caso remover com DEL
print(receita)
del receita['fev'] # Se caso nao encontrar a chave no dicionario, sera gerado um KeError

# Imagine que vc tenha um comercio eletronico, onde temos um carrinho de compras
# no qual adicionamos produtos.

Carrinho de Compras
 Produto 1:
    - nome;
    - quantiade;
    - preço
 Produto 2:
    - nome;
    - quantidade;
    - preço


# 1 - Poderiamos utilizar uma lista para isso? SIM
carrinho = []
produto1 = ['PlayStation', 1, 2300.00]
produto2 = ['God of War', 2, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber qual é o indice de cada informãção no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? SIM
produto1 = ('PlayStation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teriamos que saber qual é o indice de cada informãção no produto.

# 3 - Poderiamos utilizar um Dicionario para isso? SIM
carrinho = []
produto1 = {'nome': 'PlayStation 4', 'qtde': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'qtde': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta Forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))


# limpar o dicionario
d.clear()
print(d)


# Copiando um dicionario para outro
# forma 1  Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)
print(d)

# forma 2 Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(novo)
print(d)


"""
# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'Valor Default')
print(usuario)
print(type(usuario))


# O metodo fromkeys recebe dois parametros: um interavel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave
# o valor informado

veja = {}.fromkeys('teste','valor')
print(veja)

veja = {}.fromkeys('123', 'abc')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
