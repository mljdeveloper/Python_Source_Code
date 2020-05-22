"""
 Filter

 filter() - Serve para filtrar dados de um determinada coleção.


"""

valores = 1, 2, 3, 4, 5, 6

media = sum(valores) / len(valores)
print(media)
# Biblioteca para trabalhar com dados estatisticos
import statistics

#dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a funçao mean()

media = statistics.mean(dados)

print(media)

#OBS. Assim como a função map(), a filter recebe 2 parametros, sendo
# uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))

#Obs: Assim como na funcao map, apos ser utilizada a funcao filter, o valor é zerado da memoria

print(f'Novamente: {list(res)}')
