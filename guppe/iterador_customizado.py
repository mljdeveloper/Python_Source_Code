"""
Escrevendo um iterador customizado

for n in range(11):
    print(n, end='')
"""

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

contador = Contador(menor=1, maior= 61)

print(contador.menor, contador.maior)


for n in Contador(1, 100):
    print(n)

