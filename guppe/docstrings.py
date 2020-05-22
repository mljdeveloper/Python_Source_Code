"""
Documentando funcoes com DocStrings

"""

print(help(print))

def diz_oi():
    """Uma funcao simples que retorna a string 'oi' """
    return 'Oi!'

# no Terminal do python vc pode digitar


print(diz_oi.__doc__)


def exponencial(numero, potencial=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a potencial informada
    :param numero: Numero que desejamos gerar o exponecial
    :param potencial: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o expoencial de 'numero' por 'potencia'
    """
    return numero ** potencial


print(exponencial(4,2))