"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta perfomance

"""

from collections import deque

# Criando deque

deq = deque('geek')
print(deq)

#Adicionando elementos no deque

deq.append('y')  # adiciona no final
print(deq)

deq.appendleft('k')  # adiciona no inicio da lista
print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)
