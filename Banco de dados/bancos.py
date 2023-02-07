""" Vejamos o exemplo de calsses, mas dessa vez vamos modelar contas correntes de um banco
    Imagine o banco Tatu, precisando de um novo programa para controlar o saldo dos seus 
    correntistas. Cada conta corrente pode ter um ou mais clientes como titular. O banco
    controla apenas o nome e o número de telefone de cada cliente
    
    A conta corrente apresenta um saldo e uma lista de operações saques e depósito. Quando
    o cliente fizer um depósito, aumentaremos o saldo. Por enquanto, o banco não oferece contas
    especiais ou seja o cliente não pode sacar mais dinheiro que seu saldo permite"""

""" Para solucionar o problema do banco, precisamos de uma classe para armazenar nossas contas"""

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
    def abre_conta(self, conta):
        self.contas.append(conta)
    def lista_contas(self):
        for c in self.contas:
            c.resumo()