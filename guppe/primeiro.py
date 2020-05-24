
def funcao1():
    print('Marcos Luiz - primeiro.py')

if __name__ == '__main__':
    funcao1()
    print(f'primeiro.py esta sendo executado diretamente.{__name__}')
else:
    print(f'primeiro.py foi importado. {__name__}')
