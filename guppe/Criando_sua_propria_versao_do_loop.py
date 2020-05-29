"""
Criando sua propria versao de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

iter([1, 2, 3, 4, 5])

for letra in 'Marcos Luiz de Jesus':
    print(letra)
iter('Marcos Luiz de Jesus')
"""

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Marcos Luiz de Jesusaaa')