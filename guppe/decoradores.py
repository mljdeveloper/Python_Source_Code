"""
Decoradores (Decorators)

O que são decorators?
- Decorators são funções
- Decorators envolvem outras funcoes e aprimoram o seus comportamentos:
- Decorators tambem sao exemplos de Higher Order Functions;
- Decorators tem uma sintaxe propria, usando "@" (syntax sugar)

|--------------------------------|
|     Function Decorators        |
---------------------------------

_____________________________________
||---------------------------------||
||      Função Comum               ||  <-- Funcao Decorada
||---------------------------------||
|-----------------------------------|

# Decorators como funcoes (Sintaxe não recomendada / Sem Syntax Sugar )

def seja_educada(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Casa do Marcos')

# testando 1
teste = seja_educada(saudacao)
teste()

# testando 2

def raiva():
    print('EU TE ODEIO')

raiva_educada = (seja_educada(raiva))

raiva_educada()

# Decorators com Syntax Sugar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha uma excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Marcos')

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()
"""
"""
|__________________________________________________________|
| Home      | Serviços   |  Produtos      | Administrativo |
------------------------------------------------------------

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servico
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

# OBS: Não e codigo funcional, (que funcione) é apenas um exemplo


def checa_login(request):
    if not requuest.usuario:
        redirect('http://www.suaempresa.com.br/login')
        
def home(request):
    return 'Pode Acessar home'

@checa_login
def servicos(request):
    return 'Pode Acessar servicos'

def produtos(request):
    return 'Pode Acessar produtos'

@checa_login
def admin(request):
    return 'Pode Acessar admin'

# OBS: Não confunda Decorator com Decorator Function

"""