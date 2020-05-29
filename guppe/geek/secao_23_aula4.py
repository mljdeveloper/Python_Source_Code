"""
def cumprimentar(nome: str) -> str:
    return 10

print(cumprimentar('Marcos'))

print(cumprimentar(10))

"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('Marcos'))

print(cabecalho('Marcos', False))
