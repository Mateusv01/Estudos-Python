""" Podemos criar novos tipos de exceções para diferenciar o tipo de erro gerado pela aplicação
    (que é uma boa prática) """

class NovaException(Exception):
    pass

def lançador():
    raise NovaException

try:
    lançador()
except NovaException as n:
    print("Uma exceção do tipo NovaException foi lançada")


""" Ao desenvolver novos programas, é recomendado que você crie um tipo próprio de exceção
    para servir de super classe a todas as exceções do programa.
    """


class BancoException(Exception):
    pass
class SaldoIndisponível(BancoException):
    pass
class ClienteNãoExiste(BancoException):
    pass
def saque(saldo, valor):
    if valor > saldo:
        raise SaldoIndisponível
    return saldo - valor

try:
    saldo = saque(100, 500)
except SaldoIndisponível:
    print("Erro: Saldo insuficiente")


""" Podemos criar novas exceções que adicionam informações ou atributos"""

class EstoqueException(Exception):
    def __init__(self, mensagem, codigo_de_erro):
        super().__init__(mensagem)
        self.codigo_de_erro = codigo_de_erro

def verifique_quantidade(quantidade):
    if quantidade < 0:
        raise EstoqueException("Quantidade negativa", codigo_de_erro=1)

try:
    verifique_quantidade(-10)
except EstoqueException as ee:
    print(f"Erro: {ee.codigo_de_erro} {ee}")