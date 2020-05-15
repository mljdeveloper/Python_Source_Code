"""
Saindo de loops com break
Funciona da mesma forma que nas linguagens C ou Java

Utilizamos o break para sair de loops de maneira projetada

"""
# exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print(f'sai do loop no numero {numero}')


# exemplo 2
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
