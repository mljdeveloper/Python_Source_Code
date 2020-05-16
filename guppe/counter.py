"""
Módulo Colletions - Counter
https://docs.python.org/3/library/collections.html#collections.Counter

Collectoins -> High perfomance Container Datatypes

Counter -> recebe um interavel como parametro e cria um objeto do tipo Collection Counter que
é parecido com um dicionario, contendo como chave o elemento da lista passada como parametro e como valoer a
quantidade de ocorrencias desse elemento


from collections import Counter
# Podemos utilizar qualquer interavel, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 42, 34]

# Exempplo 1
# utilizano o Counter
res = Counter(lista)
print(type(res))

print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como
#valor a quantidade de ocorrencias

# Exemplo 2
print(Counter('Marcos Luiz de Jesus'))


"""

# Utilizando o Counter

from collections import Counter

c = Counter(cats=4, dogs=8)
print(c)

texto = """Voo 2933 da LaMia foi um voo charter, operado pela companhia com a 
identificação LMI2933, a serviço da Associação Chapecoense de Futebol, proveniente 
de Santa Cruz de la Sierra, Bolívia, com destino ao Aeroporto Internacional José 
María Córdova em Rionegro, Colômbia. Na noite de 28 de novembro de 2016, às 21h58, 
no horário local da Colômbia (29 de novembro de 2016 às 2h58 UTC), a aeronave que 
realizava este voo caiu próximo ao local chamado Cerro El Gordo, ao se aproximar 
do aeroporto em Rionegro. A aeronave trazia 77 pessoas a bordo, tendo por passageiros 
atletas, equipe técnica e diretoria do time brasileiro da Chapecoense, jornalistas e 
convidados, que iriam a Medellín, onde o clube disputaria a primeira partida da Final
 da Copa Sul-Americana contra o Atlético Nacional. Entre passageiros e tripulantes, 
 71 pessoas morreram na queda do avião, e seis foram resgatadas com vida.
Dos mortos, vinte eram jornalistas brasileiros, nove eram dirigentes (incluindo 
o presidente do clube), dois eram convidados, quatorze eram da comissão técnica 
(incluindo o treinador e o médico da equipe), dezenove eram jogadores e sete eram 
tripulantes; dos seis ocupantes que sobreviveram, quatro eram passageiros e dois,
 tripulantes. Pelo total de vítimas, esta tragédia torna-se a maior da história 
 com uma delegação esportiva e a maior do jornalismo """


palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))
