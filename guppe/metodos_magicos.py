"""
POO - Metodos Magicos

metodos magicos são todos os metodos que utilizam dunder.

dunder init -> __init__ ( Construtor )

Dunder -> Double Underscore

dunder repr -> Representacao do Objeto __repr__

    def __repr__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    Metodo magico __str__ tem preferencia para mostrar, caso existem os dois na classe
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrita por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        return 'Um objeto do tipo livro foi deletado da memoria'

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __iter__(self):
        for i in range(self.titulo):
            yield f'titulo #{i+1}'

    def __mul__(self, outro):
        if  isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Nao posso multiplicar'

l1 = Livro('Python Rocks!', 'Geek University', 400)
l2 = Livro('Inteligencia Artificial com Python!', 'Geek University', 500)


print(l1)
print(l2)

print(len(l1))

print(l1 + l2)

print(l1 * 3)