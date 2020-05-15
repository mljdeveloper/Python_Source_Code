
# Entrada de dados
#print ("Qual é o seu nome?")
#nome = input()
nome = input("Qual seu nome?")
# processamento

# Saida de Dados
# Exemplo de print 'antigo' 2.x  python
print('Seja bem vindo(a) %s' % nome)

#print("Qual a sua idade?")
#idade = input()
idade = int(input("Qual a sua idade?"))

print ('A %s tem %s anos ' % (nome, idade))

# print moderno versao 3.x do python
#print('A {0} tem {1} anos'.format(nome, idade))

# exemplo de print mais atual, a partir do 3.7
print(f'Seja bem-vindo - Exemplo mais atual de print {nome}')

print(f'O {nome} nasceu em {2020 - idade}')