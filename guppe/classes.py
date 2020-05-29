"""
 POO -  Classes

 Em POO, Classes são modelos do objeto do mundo real sendo representados
 computacionamente

 Imagine que voce queira fazer um sistema para automatizar o controle das lampadas
 da sua casa.

 Classes podem conter:
    - Atributos - Representam as caracteristicas do objeto, Ou seja, pelos atributos
    conseguimos reprensentar computacionamente os estados de um objeto. No casao da
    lampada, possivelemente iriamos querer saber se a lampada é 110 ou 220, se ela
    é branca, amarela, vermelha ou outra cor e qual e a luminosidade dela e etc.

    - Metodos (funcoes) -> Reprensentam os comportamentos do objeto, ou seja, as
    acoes que este objeto podem realizar em seu sistema, no caso da lampada, por exemplo
    um comportamento comum, que muito provalvemente que iriamos querer reprensentar
    no nosso sistema, seria o deligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra reservada 'pass', em Python quando temos um bloco de codigo
que ainda nao esta implementado

OBS: Quando nomeamos nossas classe em Python, utilizamos por convenção o nome com
inicial em maiusculo. Se o nome for composto, utiliza-se as inicias de ambas as
palavras em maiusculo, todas juntas.

OBS: Quando estamos planejando um software e definimos quais classes teremos que
ter no sistema, chamamos esses objetos que serao mapeados para classes de
Entidade.

"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))
