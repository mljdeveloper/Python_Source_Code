"""
usuario = Usuario('marcos', 'luiz', '1323213', 'marcos@uol.com', '123', '123')
print(type(usuario))
print(usuario)
print(usuario.__dict__)
print(usuario.__str__)

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf, email, sexo=''):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__nomecompleto = self.__nome + ' ' + self.__sobrenome
        self.__cpf = cpf
        self.__email = email
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def nome_completo(self):
        return self.__nomecompleto

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def sexo(self):
        return self.__sexo

    def __str__(self):
        return self.__nomecompleto


class Usuario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, email, senha, contrasenha):
        super().__init__(nome, sobrenome, cpf, email)
        self.__senha = senha
        self.__contrasenha = contrasenha

    @property
    def senha(self):
        return self.__senha

    @property
    def contrasenha(self):
        return self.__contrasenha

    def __str__(self):
        return self._Pessoa__nome + ' ' + self._Pessoa__sobrenome


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, email, matricula, datanasc, dataadm, datadem,
                 cargo, centrocusto, ativo, codempresa, datacad):
        super().__init__(nome, sobrenome, cpf, email)
        self.__matricula = matricula
        self.__datanasc = datanasc
        self.__dataadm = dataadm
        self.__datadem = datadem
        self.__cargo = cargo
        self.__centrocusto = centrocusto
        self.__ativo = ativo
        self.__codempresa = codempresa
        self.__datacad = datacad

    @property
    def matricula(self):
        return self.__matricula

    @property
    def datanasc(self):
        return self.__datanasc

    @property
    def dataadm(self):
        return self.__dataadm

    @property
    def datadem(self):
        return self.__datadem

    @property
    def cargo(self):
        return self.__cargo

    @property
    def centrocusto(self):
        return self.__centrocusto

    @property
    def ativo(self):
        return self.__ativo

    @property
    def codempresa(self):
        return self.__codempresa

    @property
    def datatacad(self):
        return self.__datacad

    def __str__(self):
        return self.__matricula + ' ' + self._Pessoa.__nome_completo
