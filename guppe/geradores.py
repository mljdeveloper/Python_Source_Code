"""
Geradores
- Geradores ( Generators) são Iterators ( Iteradores ):
OBS: o contrario não é verdadeiro, Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funçoes geradoras:
- Funções geradoras utilizam a palavra reservada yield;
- Generators pode serm criados com Expressões Geradoras:

Diferenças entre Funções e Generator Functions ( Funções Geradoras )
___________________________________________________________________________________
| Funcoes                                | Generator Functions                    |
-----------------------------------------------------------------------------------
| Utilizam return                        | Utilizam yield                         |
----------------------------------------------------------------------------------
| retorna uma vez                        | podem utilizar yield multiplas vezes   |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor     | quando executada, retorna um generator |
-----------------------------------------------------------------------------------

gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)

for num in gen:
    print(num, end=' ')

"""


# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator.

gen = list(conta_ate(10))

print(gen)


