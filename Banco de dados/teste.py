from clientes import Cliente
from contas import Conta
from bancos import Banco
joão = Cliente("João da Silva", "132-777")
maria = Cliente("Maria Almeida", "555-213")

conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria,joão], 2, 500)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)

print(conta1.extrato())
print(conta2.extrato())

josé = Cliente("José vargas", "777-222")
contaJM = Conta([joão, maria], 100)
contaJ = Conta([josé], 10)

tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)

print(tatu.lista_contas())

from contas import ContaEspecial

conta3 = ContaEspecial([maria,joão], 2, 500, 1000)
conta3.deposito(0)
conta3.saque(100)

conta3.extrato()